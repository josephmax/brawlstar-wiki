"""Small, reproducible GEPA integration trial for the BP practice cards.

The candidate is an extra runtime decision rule. The BP model receives only a
staged public question and neutral facts; private labels stay in this evaluator.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import signal
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

from gepa.optimize_anything import EngineConfig, GEPAConfig, ReflectionConfig, optimize_anything

SEED = (
    "逐项比较所有可见选项。先确认模式目标和队伍缺口，再检查候选兑现路径、"
    "敌方压力、队友配合与资源条件。依据中性事实说明成立和失败条件；证据不足时明确标注。"
)
DEFAULT_TRAIN = ("practice-001-1", "practice-003-1")
DEFAULT_VAL = ("practice-006-1",)


def digest(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def load_env_file(path: Path | None) -> None:
    if path is None:
        return
    for line in path.read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def complete(base_url: str, model: str, api_key: str, messages: list[dict], max_tokens: int) -> dict:
    body = {
        "model": model, "messages": messages, "stream": False,
        "max_tokens": max_tokens, "thinking": {"type": "enabled"},
    }
    request = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=json.dumps(body, ensure_ascii=False).encode(),
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + api_key},
    )
    def wall_timeout(_signum, _frame):
        raise TimeoutError("model call exceeded 90-second wall-clock limit")

    # urllib's timeout is an idle-socket timeout; a slow response can take far
    # longer. GEPA runs serially here, so an absolute timer is safe on macOS.
    can_alarm = threading.current_thread() is threading.main_thread() and hasattr(signal, "setitimer")
    previous_handler = signal.getsignal(signal.SIGALRM) if can_alarm else None
    if can_alarm:
        signal.signal(signal.SIGALRM, wall_timeout)
        signal.setitimer(signal.ITIMER_REAL, 90)
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            return json.load(response)
    finally:
        if can_alarm:
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, previous_handler)


def parse_answer(text: str) -> dict:
    clean = text.strip()
    if clean.startswith("```"):
        clean = re.sub(r"^```(?:json)?\s*|\s*```$", "", clean).strip()
    result = json.loads(clean)
    if not isinstance(result, dict):
        raise ValueError("answer is not a JSON object")
    return result


def grade(answer: dict, expected: dict, allowed: set[str]) -> tuple[float, dict]:
    items = answer.get("options")
    if not isinstance(items, list) or len(items) != len(allowed):
        return 0.0, {"error": "all visible options must be graded once"}
    predicted = {}
    grades = {"correct", "reasonable", "poor", "insufficient_evidence"}
    for item in items:
        if not isinstance(item, dict) or item.get("id") not in allowed or item.get("grade") not in grades:
            return 0.0, {"error": "invalid option id or grade"}
        if not isinstance(item.get("reason"), str) or not item["reason"].strip() or not isinstance(item.get("evidence"), list) or not isinstance(item.get("conditions"), str):
            return 0.0, {"error": "missing reason, evidence list, or conditions"}
        if item["id"] in predicted:
            return 0.0, {"error": "duplicate option id"}
        predicted[item["id"]] = item["grade"]
    if set(predicted) != allowed:
        return 0.0, {"error": "missing option"}
    mismatches = [
        {"option": option_id, "expected": expected["options"][option_id]["proposed_grade"],
         "actual": predicted[option_id], "review_note": expected["options"][option_id]["explanation"]}
        for option_id in sorted(allowed)
        if predicted[option_id] != expected["options"][option_id]["proposed_grade"]
    ]
    expected_best = {i for i in allowed if expected["options"][i]["proposed_grade"] == "correct"}
    actual_best = answer.get("best", [])
    if not isinstance(actual_best, list) or len(actual_best) != len(set(actual_best)) or any(i not in allowed or predicted[i] != "correct" for i in actual_best):
        return 0.0, {"error": "invalid best set"}
    actual_best = set(actual_best)
    option_accuracy = (len(allowed) - len(mismatches)) / len(allowed)
    best_f1 = 2 * len(expected_best & actual_best) / (len(expected_best) + len(actual_best)) if expected_best or actual_best else 1.0
    return round(.7 * option_accuracy + .3 * best_f1, 4), {
        "option_accuracy": option_accuracy, "best_f1": best_f1,
        "mismatches": mismatches, "label_status": expected["status"],
        "note": "Practice labels are provisional, not expert gold; use this only as a plumbing trial.",
    }


def run(args: argparse.Namespace) -> None:
    load_env_file(args.env_file)
    key = os.environ.get(args.key_env)
    if not key:
        raise SystemExit(f"missing {args.key_env}")
    args.out.mkdir(parents=True, exist_ok=True)
    staged = json.loads((args.stage / "manifest.json").read_text())
    ids = set(staged["ids"])
    selected = (*DEFAULT_TRAIN, *DEFAULT_VAL)
    if not set(selected) <= ids:
        raise SystemExit("selected questions missing from staged inputs")
    labels_path = args.labels
    labels = {v["id"]: v for line in labels_path.read_text().splitlines() if (v := json.loads(line))["id"] in selected}
    if len(labels) != len(selected):
        raise SystemExit("missing private labels")
    system = (args.stage / "system.txt").read_text()
    record = {
        "model": args.model, "base_url": args.base_url, "stage_manifest_sha256": digest((args.stage / "manifest.json").read_text()),
        "system_sha256": digest(system), "labels_sha256": hashlib.sha256(labels_path.read_bytes()).hexdigest(),
        "train": DEFAULT_TRAIN, "val": DEFAULT_VAL, "max_metric_calls": args.max_metric_calls,
        "max_candidate_proposals": args.max_candidate_proposals,
    }
    (args.out / "config.json").write_text(json.dumps(record, ensure_ascii=False, indent=2))
    calls = 0

    def evaluator(candidate: str, example: str):
        nonlocal calls
        if len(candidate) > 4000 or len(candidate) < 20:
            return 0.0, {"error": "candidate rule length outside 20..4000 characters"}
        if any(forbidden in candidate for forbidden in ("practice-001", "practice-003", "practice-006", "答案是", "标准答案")):
            return 0.0, {"error": "candidate contains case-specific answer text"}
        calls += 1
        question = json.loads((args.stage / (example + ".json")).read_text())
        allowed = {v["id"] for v in question["question"]["options"]}
        candidate_system = system + "\n\n## 本次候选决策补充规则\n" + candidate
        started = time.monotonic()
        try:
            response = complete(args.base_url, args.model, key,
                                [{"role": "system", "content": candidate_system},
                                 {"role": "user", "content": json.dumps(question, ensure_ascii=False)}],
                                max_tokens=7500)
            choice = response["choices"][0]
            raw = choice["message"].get("content") or ""
            answer = parse_answer(raw)
            score, feedback = grade(answer, labels[example], allowed)
            status = "completed"
            error = None
        except Exception as exc:
            raw, answer, response, score = "", None, {}, 0.0
            error = type(exc).__name__ + ": " + str(exc)[:300]
            feedback = {"error": error}
            status = "failed"
        output = {
            "case_id": example, "candidate_sha256": digest(candidate), "effective_system_sha256": digest(candidate_system),
            "status": status, "score": score, "feedback": feedback, "answer": answer,
            "raw_content": raw, "usage": response.get("usage"), "error": error,
            "elapsed_seconds": round(time.monotonic() - started, 2),
        }
        (args.out / f"call-{calls:03d}-{example}.json").write_text(json.dumps(output, ensure_ascii=False, indent=2))
        if status == "failed" and not isinstance(error, str):
            raise AssertionError("missing failure record")
        if status == "failed" and error.startswith(("TimeoutError:", "HTTPError:", "URLError:")):
            raise RuntimeError(f"provider call failed; see call-{calls:03d}-{example}.json: {error}")
        return score, feedback

    def reflection_lm(prompt):
        messages = prompt if isinstance(prompt, list) else [{"role": "user", "content": prompt}]
        response = complete(args.base_url, args.model, key, messages, max_tokens=6000)
        content = response["choices"][0]["message"].get("content") or ""
        with (args.out / "reflections.jsonl").open("a") as stream:
            stream.write(json.dumps({"prompt_sha256": digest(json.dumps(prompt, ensure_ascii=False)),
                                     "content": content, "usage": response.get("usage")}, ensure_ascii=False) + "\n")
        if not content:
            raise ValueError("reflection model returned empty content")
        return content

    result = optimize_anything(
        seed_candidate=SEED,
        evaluator=evaluator,
        dataset=list(DEFAULT_TRAIN),
        valset=list(DEFAULT_VAL),
        objective="改进有限选项 BP 决策的通用机制比较，保留证据边界。只提出可追加到现有 skill 的中文规则，不写题目答案或英雄名单。",
        background="候选文本会附加到既有完整 BP skill 后。题库标签尚非 gold；不要把分档解释当成无条件游戏事实。",
        config=GEPAConfig(
            engine=EngineConfig(run_dir=str(args.out / "gepa-run"), max_metric_calls=args.max_metric_calls,
                                max_candidate_proposals=args.max_candidate_proposals, parallel=False, use_cloudpickle=False),
            reflection=ReflectionConfig(reflection_lm=reflection_lm, reflection_minibatch_size=1),
        ),
    )
    best = result.best_candidate
    (args.out / "best-candidate.txt").write_text(best if isinstance(best, str) else json.dumps(best, ensure_ascii=False))
    summary = {"calls": calls, "seed_sha256": digest(SEED), "best_sha256": digest(best if isinstance(best, str) else json.dumps(best, ensure_ascii=False)),
               "candidate_changed": best != SEED}
    (args.out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", type=Path, required=True)
    parser.add_argument("--labels", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--model", default="glm-5.3-flash")
    parser.add_argument("--base-url", default="https://open.bigmodel.cn/api/paas/v4")
    parser.add_argument("--key-env", default="GLM_API_KEY")
    parser.add_argument("--env-file", type=Path)
    parser.add_argument("--max-metric-calls", type=int, default=6)
    parser.add_argument("--max-candidate-proposals", type=int, default=1)
    run(parser.parse_args())
