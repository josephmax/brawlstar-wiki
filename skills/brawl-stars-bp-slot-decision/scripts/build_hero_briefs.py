#!/usr/bin/env python3
"""Pre-build one answer-ready brief per brawler from static knowledge.

A hero question should cost one lookup, not a tour of the wiki. Everything a
single-brawler answer needs that does not change between two knowledge commits
is assembled here once per commit:

- the reviewed entity page (minus the maintainer-only breakpoint profile)
- the official rows of recent patches that touched this brawler, and whether
  they are already folded into the page
- the brawler's pick/ban/win record in the latest archived esports event, or
  the patch that makes that record unusable

The only data left for query time is the rolling ladder snapshot, which the
application fetches on its own schedule and gates with `manifest.patches`.

Output is a regenerable artifact (never part of the knowledge base):

    <output>/manifest.json
    <output>/briefs/<Brawler>.json

Statistics here are descriptive. Nothing in a brief is a tier, a fit upgrade,
or an eligibility decision.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any

BRIEF_SCHEMA = "brawlstar.hero_brief.v1"
MANIFEST_SCHEMA = "brawlstar.hero_brief_manifest.v1"
# A brief must fit one tool result without trimming. Exceeding this fails the
# build so the page is fixed at the source instead of being cut at runtime.
MAX_BRIEF_CHARS = 40000
# Patches shown in a brief: the newest ones that touched the brawler.
RECENT_PATCH_LIMIT = 3
FOLDED = {"folded", "model_changed", "numbers_only", "no_model_change"}

BREAKPOINT_SECTION = re.compile(
    r"(?:^##+ *combat_breakpoint_profile *\n+)?```json\n(?:(?!```).)*?\"combat_breakpoint_profile\"(?:(?!```).)*?```\n?",
    re.S | re.M,
)
PROFILE_STATUS = re.compile(r"^\s*profile_status:\s*[\"']?([A-Za-z_]+)[\"']?\s*$", re.M)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def version_ledger():
    """The maintenance skill owns the ledger parser; import it, do not copy it."""
    try:
        import version_status
    except ImportError:
        sys.path.insert(0, str(repo_root() / "skills" / "brawl-stars-bp-knowledge-maintenance" / "scripts"))
        import version_status
    return version_status


def profile_markdown(text: str) -> str:
    """Entity page as the model should read it: runtime facts only."""
    stripped = BREAKPOINT_SECTION.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", stripped).strip() + "\n"


def recent_changes(name: str, patches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    changes = []
    for patch in reversed(patches):
        row = patch["brawlers"].get(name)
        # Pre-ledger patches carry no official rows; the page already reflects them.
        if not row or not patch["has_ledger"]:
            continue
        changes.append(
            {
                "patch_id": patch["patch_id"],
                "effective_at": patch["effective_at"],
                "kinds": row["kinds"],
                "direction": row["direction"],
                "fold": row["fold"],
                "folded_into_profile": row["fold"] in FOLDED,
                "official_rows": row["rows"],
                "note": row["note"],
            }
        )
        if len(changes) == RECENT_PATCH_LIMIT:
            break
    return changes


def latest_event(repo: Path, ledger_module) -> dict[str, Any] | None:
    events = [event for event in ledger_module.archived_events(repo) if event.get("end_date")]
    if not events:
        return None
    newest = max(events, key=lambda event: event["end_date"])
    # One archive can hold several regional pages of the same event round.
    siblings = [event for event in events if event["archive"] == newest["archive"]]
    path = repo / newest["archive"]
    con = sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        played_series = sum(int(row["played_series"] or 0) for row in con.execute("SELECT played_series FROM event"))
        scopes = {
            "global": [dict(row) for row in con.execute("SELECT * FROM metric_global")],
            "mode": [dict(row) for row in con.execute("SELECT * FROM metric_mode")],
            "map": [dict(row) for row in con.execute("SELECT * FROM metric_map")],
        }
    finally:
        con.close()
    return {
        "archive": newest["archive"],
        "kind": newest["kind"],
        "names": sorted({event["name"] for event in siblings}),
        "page_titles": sorted({event["page_title"] for event in siblings if event.get("page_title")}),
        "start_date": min(min(ledger_module.DATE.findall(event["date"])) for event in siblings),
        "end_date": max(event["end_date"] for event in siblings),
        "played_sets": sum(event["played_sets"] for event in siblings),
        "played_series": played_series,
        "scopes": scopes,
    }


def rate(part: int, whole: int) -> float | None:
    return round(part / whole, 4) if whole else None


def esports_block(name: str, event: dict[str, Any] | None, patches: list[dict[str, Any]]) -> dict[str, Any]:
    if not event:
        return {"status": "no_event", "note": "知识库尚无归档赛事。"}
    summary = {
        "names": event["names"],
        "kind": event["kind"],
        "start_date": event["start_date"],
        "end_date": event["end_date"],
        "played_sets": event["played_sets"],
        "played_series": event["played_series"],
    }
    # Strict rule: any balance patch after the event invalidates the whole
    # competitive sample, even when this brawler was not changed. The event
    # describes an environment that no longer exists.
    blocking = [
        patch
        for patch in patches
        if (patch["effective_at"] or "") > event["end_date"]
    ]
    if blocking:
        return {
            "status": "withheld",
            "event": summary,
            "reason": "赛事结束后发生过平衡性调整，整份赛事样本不再代表当前环境，按规则不展示。",
            "changed_by": [
                {"patch_id": patch["patch_id"], "effective_at": patch["effective_at"]} for patch in blocking
            ],
        }
    row = next((item for item in event["scopes"]["global"] if item["brawler"] == name), None)
    if not row:
        return {"status": "no_sample", "event": summary, "note": "该赛事中没有选用或禁用记录。"}
    sets, series = event["played_sets"], event["played_series"]

    def metrics(item: dict[str, Any]) -> dict[str, Any]:
        return {
            "pick_sets": item["pick_sets"],
            "set_wins_when_picked": item["set_wins_when_picked"],
            "win_rate_when_picked": rate(item["set_wins_when_picked"], item["pick_sets"]),
            "local_ban_set_coverage": item["local_ban_set_coverage"],
            "global_ban_series_coverage": item["global_ban_series_coverage"],
        }

    return {
        "status": "ok",
        "event": summary,
        "overall": {
            **metrics(row),
            "pick_rate": rate(row["pick_sets"], sets),
            "local_ban_rate": rate(row["local_ban_set_coverage"], sets),
            "global_ban_rate": rate(row["global_ban_series_coverage"], series),
        },
        "by_mode": [
            {"mode": item["mode"], **metrics(item)}
            for item in sorted(event["scopes"]["mode"], key=lambda item: -item["pick_sets"])
            if item["brawler"] == name
        ],
        "by_map": [
            {"map": item["map"], "mode": item["mode"], **metrics(item)}
            for item in sorted(event["scopes"]["map"], key=lambda item: -item["pick_sets"])
            if item["brawler"] == name
        ],
        "semantics": "pick_rate 与 local_ban_rate 以已进行 set 为分母，global_ban_rate 以已进行 series 为分母；胜率是选用后的 set 胜率，不是个人胜率，也不代表因果。",
    }


def build(repo: Path) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    ledger_module = version_ledger()
    patches = ledger_module.load_patch_index(repo)
    event = latest_event(repo, ledger_module)
    pool_path = repo / "wiki/environment/ranked_pool.json"
    pool = json.loads(pool_path.read_text(encoding="utf-8")) if pool_path.exists() else None

    briefs: dict[str, dict[str, Any]] = {}
    for path in sorted((repo / "wiki/entities/brawlers").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        status = PROFILE_STATUS.search(text)
        briefs[path.stem] = {
            "schema": BRIEF_SCHEMA,
            "brawler": path.stem,
            "page": str(path.relative_to(repo)),
            "profile_status": status.group(1) if status else "missing_profile",
            "profile_markdown": profile_markdown(text),
            "recent_changes": recent_changes(path.stem, patches),
            "esports": esports_block(path.stem, event, patches),
        }

    oversized = {
        name: size
        for name, brief in briefs.items()
        if (size := len(json.dumps(brief, ensure_ascii=False))) > MAX_BRIEF_CHARS
    }
    if oversized:
        raise SystemExit(
            f"hero brief exceeds {MAX_BRIEF_CHARS} chars; shorten the entity page instead of trimming at runtime: {oversized}"
        )

    manifest = {
        "schema": MANIFEST_SCHEMA,
        "max_brief_chars": MAX_BRIEF_CHARS,
        "patches": [
            {
                "patch_id": patch["patch_id"],
                "effective_at": patch["effective_at"],
                "source_page": patch["source_page"],
                "has_ledger": patch["has_ledger"],
                "brawlers": {
                    name: {"kinds": row["kinds"], "direction": row["direction"], "fold": row["fold"]}
                    for name, row in patch["brawlers"].items()
                },
                "open_environment": [
                    {"id": item.get("id"), "kind": item.get("kind"), "note": item.get("note") or ""}
                    for item in patch["environment"]
                    if item.get("status") == "pending"
                ],
            }
            for patch in patches
        ],
        "ranked_pool": (
            {
                "season": pool.get("season"),
                "captured_at": (pool.get("source") or {}).get("captured_at"),
                "maps": pool.get("maps") or [],
            }
            if pool
            else None
        ),
        "latest_event": ({key: value for key, value in event.items() if key != "scopes"} if event else None),
        "brawlers": {
            name: {
                "file": f"briefs/{name}.json",
                "profile_status": brief["profile_status"],
                "chars": len(json.dumps(brief, ensure_ascii=False)),
            }
            for name, brief in briefs.items()
        },
    }
    return manifest, briefs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--repo", default=str(repo_root()), help="Knowledge repository root")
    parser.add_argument("--output", required=True, help="Directory for manifest.json and briefs/")
    args = parser.parse_args()
    manifest, briefs = build(Path(args.repo).resolve())
    out = Path(args.output)
    (out / "briefs").mkdir(parents=True, exist_ok=True)
    for name, brief in briefs.items():
        (out / "briefs" / f"{name}.json").write_text(json.dumps(brief, ensure_ascii=False), encoding="utf-8")
    # The manifest is written last: its presence means the directory is complete.
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    sizes = [item["chars"] for item in manifest["brawlers"].values()]
    print(
        json.dumps(
            {"briefs": len(briefs), "max_chars": max(sizes), "median_chars": sorted(sizes)[len(sizes) // 2]},
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
