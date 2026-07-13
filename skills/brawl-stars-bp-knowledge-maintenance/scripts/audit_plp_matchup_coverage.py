#!/usr/bin/env python3
"""Audit PLP matchup coverage against a compiled runtime matchup index.

PLP matchup fields are useful as review seeds, but they do not include enough
mechanism / active_when / fails_when detail to become runtime edges directly.
This script reports PLP-only pairs so maintainers can convert them into stable
conditional matchup entries in brawler pages.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_OUTPUT = "outputs/plp-matchup-coverage-audit.md"
DATED_CAPTURE_RE = re.compile(r"^(?P<slug>.+)-(?P<date>\d{4}-\d{2}-\d{2})$")


def normalize_key(value: str) -> str:
    return re.sub(r"[^0-9a-z]+", "", str(value).casefold())


def rel(path: Path, repo: Path) -> str:
    try:
        return str(path.relative_to(repo))
    except ValueError:
        return str(path)


def read_json_blocks(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(.*?)```", text, flags=re.DOTALL)
    result: list[dict[str, Any]] = []
    for block in blocks:
        try:
            value = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            result.append(value)
    return result


def latest_plp_raw_paths(raw_dir: Path) -> list[Path]:
    """Return only the newest dated raw capture for each PLP guide slug."""
    selected: dict[str, tuple[str, Path]] = {}
    for path in sorted(raw_dir.glob("*.md")):
        match = DATED_CAPTURE_RE.match(path.stem)
        slug = match.group("slug") if match else path.stem
        capture_date = match.group("date") if match else ""
        current = selected.get(slug)
        candidate = (capture_date, path)
        if current is None or (candidate[0], candidate[1].name) > (current[0], current[1].name):
            selected[slug] = candidate
    return [selected[slug][1] for slug in sorted(selected)]


def load_runtime_index(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and isinstance(payload.get("runtime_bp_index"), dict):
        return payload["runtime_bp_index"]
    return payload


def valid_brawler_names(repo: Path, index: dict[str, Any]) -> set[str]:
    names = set((index.get("manifest") or {}).get("available_brawlers") or [])
    names.update((index.get("brawler_runtime_cards") or {}).keys())
    if not names:
        names.update(path.stem for path in (repo / "wiki/entities/brawlers").glob("*.md"))
    return names


def name_lookup(names: set[str]) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for name in names:
        lookup[name] = name
        lookup[normalize_key(name)] = name
    return lookup


def canonical_name(raw: Any, lookup: dict[str, str]) -> str | None:
    if raw in (None, ""):
        return None
    text = str(raw).strip()
    return lookup.get(text) or lookup.get(normalize_key(text))


def plp_matchup_pairs(repo: Path, raw_dir: Path, lookup: dict[str, str]) -> list[dict[str, Any]]:
    pairs: list[dict[str, Any]] = []
    for path in latest_plp_raw_paths(raw_dir):
        blocks = read_json_blocks(path)
        if not blocks:
            continue
        matchup = blocks[-1]
        subject = canonical_name(matchup.get("name") or path.stem.split("-202")[0], lookup)
        if not subject:
            continue
        for field, direction in (("countersThese", "answers"), ("counteredBy", "is_answered_by")):
            for target_record in matchup.get(field) or []:
                target = canonical_name(
                    target_record.get("name") or target_record.get("slug") or target_record.get("key"),
                    lookup,
                )
                if not target:
                    continue
                pairs.append(
                    {
                        "subject": subject,
                        "direction": direction,
                        "target": target,
                        "plp_source_ref": rel(path, repo),
                        "matchup_tier": target_record.get("matchupTier") or "unknown",
                        "source_kind": target_record.get("source") or "unknown",
                    }
                )
    return pairs


def compiled_matchup_pairs(index: dict[str, Any]) -> set[tuple[str, str, str]]:
    pairs: set[tuple[str, str, str]] = set()
    by_brawler = (index.get("matchup_index") or {}).get("by_brawler") or {}
    for subject, records in by_brawler.items():
        for edge in records.get("answers") or []:
            target = edge.get("target")
            if target:
                pairs.add((subject, "answers", target))
        for edge in records.get("is_answered_by") or []:
            target = edge.get("target")
            if target:
                pairs.add((subject, "is_answered_by", target))
    return pairs


def reviewed_seed(pair: dict[str, Any]) -> dict[str, Any]:
    direction_label = "counter" if pair["direction"] == "answers" else "is countered by"
    return {
        **pair,
        "status": "needs_mechanism_review",
        "review_prompt": (
            f"Review why {pair['subject']} {direction_label} {pair['target']}; "
            "add mechanism, active_when, fails_when, map/mode conditions, and bp_use before promoting to runtime."
        ),
    }


def coverage_payload(repo: Path, runtime_index: Path, raw_dir: Path) -> dict[str, Any]:
    index = load_runtime_index(runtime_index)
    lookup = name_lookup(valid_brawler_names(repo, index))
    plp_pairs = plp_matchup_pairs(repo, raw_dir, lookup)
    compiled_pairs = compiled_matchup_pairs(index)
    plp_pair_keys = {(item["subject"], item["direction"], item["target"]) for item in plp_pairs}
    overlap = plp_pair_keys & compiled_pairs
    plp_only_keys = plp_pair_keys - compiled_pairs

    pair_by_key = {
        (item["subject"], item["direction"], item["target"]): item
        for item in plp_pairs
    }
    plp_only = [
        reviewed_seed(pair_by_key[key])
        for key in sorted(plp_only_keys)
    ]
    by_subject: dict[str, int] = {}
    for item in plp_only:
        by_subject[item["subject"]] = by_subject.get(item["subject"], 0) + 1

    return {
        "plp_matchup_coverage": {
            "summary": {
                "plp_raw_pages": len(latest_plp_raw_paths(raw_dir)),
                "plp_raw_files": len(list(raw_dir.glob("*.md"))),
                "plp_pairs": len(plp_pair_keys),
                "compiled_pairs": len(compiled_pairs),
                "overlap_pairs": len(overlap),
                "plp_only_pairs": len(plp_only),
                "runtime_index": rel(runtime_index, repo),
                "raw_dir": rel(raw_dir, repo),
            },
            "top_subjects": [
                {"subject": subject, "plp_only_pairs": count}
                for subject, count in sorted(by_subject.items(), key=lambda item: (-item[1], item[0]))[:20]
            ],
            "plp_only_seeds": plp_only,
        }
    }


def render_markdown(payload: dict[str, Any]) -> str:
    data = payload["plp_matchup_coverage"]
    summary = data["summary"]
    lines = [
        "# PLP Matchup Coverage Audit",
        "",
        "This generated report lists PLP matchup pairs that are not yet present in the compiled runtime matchup index.",
        "Treat these rows as review seeds, not runtime counter edges.",
        "",
        "## Summary",
        "",
    ]
    for key in (
        "plp_raw_pages",
        "plp_raw_files",
        "plp_pairs",
        "compiled_pairs",
        "overlap_pairs",
        "plp_only_pairs",
        "runtime_index",
        "raw_dir",
    ):
        lines.append(f"- {key}: `{summary.get(key)}`")
    lines.extend(["", "## Top Subjects", ""])
    for item in data["top_subjects"]:
        lines.append(f"- `{item['subject']}`: {item['plp_only_pairs']}")
    lines.extend(["", "## PLP-only Seeds", ""])
    for seed in data["plp_only_seeds"]:
        lines.append(
            f"- `{seed['subject']}` {seed['direction']} `{seed['target']}` "
            f"({seed['matchup_tier']}, {seed['source_kind']}) - {seed['plp_source_ref']}"
        )
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository root")
    parser.add_argument(
        "--runtime-index",
        required=True,
        help="Compiled runtime_bp_index JSON path used as the reviewed matchup baseline",
    )
    parser.add_argument(
        "--raw-dir",
        default="raw/sources/pl-prodigy/brawlers",
        help="PLP raw brawler capture directory",
    )
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Markdown report path for --write")
    parser.add_argument("--write", action="store_true", help="Write markdown audit report")
    parser.add_argument("--json", action="store_true", help="Emit JSON payload")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).resolve()
    runtime_index = Path(args.runtime_index)
    if not runtime_index.is_absolute():
        runtime_index = repo / runtime_index
    raw_dir = Path(args.raw_dir)
    if not raw_dir.is_absolute():
        raw_dir = repo / raw_dir
    payload = coverage_payload(repo, runtime_index, raw_dir)
    if args.write:
        output = Path(args.output)
        if not output.is_absolute():
            output = repo / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render_markdown(payload), encoding="utf-8")
    if args.json or not args.write:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
