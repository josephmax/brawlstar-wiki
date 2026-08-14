#!/usr/bin/env python3
"""Aggregate a monthly pick/ban environment signal from tournament observation profiles.

Input:  one or more `tournament_observation_profile.v1` JSON files (outputs/esports/).
Output: `brawlstar.environment_signal.v1` — per-brawler monthly pick rate (paired with
        ban rate), intended as the BP environment-signal input layer.

Design decisions (2026-08-14, see wiki/syntheses/BP-强度层语义回归与高分选取率估计器.md):
- high-rank approximation = pro Monthly Finals (rank_floor: legendary_plus_approximation)
- window = monthly; pick and ban are reported as a pair
- This artifact is a draft signal: policy.runtime_consumption stays forbidden until a
  separate reviewed promotion into the compiler's pickrate slot.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def totals(profiles: list[dict[str, Any]]) -> tuple[int, int]:
    played_series = 0
    played_sets = 0
    for profile in profiles:
        for event in profile.get("source_events") or []:
            played_series += int(event.get("played_series") or 0)
            played_sets += int(event.get("played_sets") or 0)
    return played_series, played_sets


def aggregate(profiles: list[dict[str, Any]]) -> dict[str, Any]:
    played_series, played_sets = totals(profiles)
    brawlers: dict[str, dict[str, Any]] = {}
    for profile in profiles:
        for row in (profile.get("scopes") or {}).get("global") or []:
            name = row.get("brawler")
            if not name:
                continue
            entry = brawlers.setdefault(name, {"picks": 0, "set_wins_when_picked": 0, "ban_series": 0, "ban_sets": 0})
            entry["picks"] += int(row.get("pick_sets") or 0)
            entry["set_wins_when_picked"] += int(row.get("set_wins_when_picked") or 0)
            entry["ban_series"] += int(row.get("global_ban_series_coverage") or 0)
            entry["ban_sets"] += int(row.get("local_ban_set_coverage") or 0)

    rows: dict[str, dict[str, Any]] = {}
    for name, entry in sorted(brawlers.items()):
        rows[name] = {
            "picks": entry["picks"],
            "pick_rate": round(entry["picks"] / played_sets, 4) if played_sets else 0,
            "win_rate_when_picked": (
                round(entry["set_wins_when_picked"] / entry["picks"], 4) if entry["picks"] else 0
            ),
            "ban_series": entry["ban_series"],
            "ban_rate": round(entry["ban_series"] / played_series, 4) if played_series else 0,
            "ban_set_coverage": round(entry["ban_sets"] / played_sets, 4) if played_sets else 0,
        }

    return {
        "schema": "brawlstar.environment_signal.v1",
        "profile_id": "monthly-liquipedia-pickban",
        "window": "monthly",
        "rank_floor": "legendary_plus_approximation",
        "source": {
            "kind": "liquipedia-monthly-finals",
            "profiles": [profile.get("profile_id") or Path(profile.get("generated_at") or "").name for profile in profiles],
            "played_series": played_series,
            "played_sets": played_sets,
        },
        "policy": {
            "interpretation": "revealed_draft_preference_draft",
            "tier_generation": "forbidden",
            "runtime_consumption": "forbidden_until_reviewed_promotion",
        },
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "brawlers": rows,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", action="append", required=True, help="tournament_observation_profile.v1 JSON; repeatable.")
    parser.add_argument("--output", default="", help="Write JSON to this path (relative to repo root if not absolute).")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    profiles = [load_json(Path(path)) for path in args.profile]
    signal = aggregate(profiles)
    text = json.dumps(signal, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
