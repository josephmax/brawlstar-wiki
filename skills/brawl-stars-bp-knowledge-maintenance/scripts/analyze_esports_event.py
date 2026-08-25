#!/usr/bin/env python3
"""Build a neutral tournament_observation_profile.v1 from event raw captures.

Names are re-normalized against the live `wiki/concepts/英雄名称归一化.md` rules
before aggregation (raw captures stay immutable; alias fixes take effect on
re-run). Unrecognized names are reported on stderr instead of passing silently.

Output: `--output` writes JSON (for export/review); `--db` writes the archive
SQLite database (row/column storage for external applications) with the
per-set series/pick/ban tables filled from the parsed raw events.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import _environment_sqlite as envdb
from _liquipedia_event import analyze_events, load_brawler_names, load_raw_capture, renormalize_event_names


ROOT = Path(__file__).resolve().parents[3]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", action="append", required=True, help="Event raw capture; repeatable.")
    parser.add_argument("--repo", default=str(ROOT))
    parser.add_argument("--generated-at", help="Optional fixed ISO timestamp for reproducible output.")
    parser.add_argument("--output", help="Write JSON profile to this path (optional export).")
    parser.add_argument("--db", help="Write the archive SQLite database to this path (row/column storage).")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).resolve()
    paths = [Path(value) if Path(value).is_absolute() else repo / value for value in args.raw]
    canonical_names = load_brawler_names(repo)
    events = [renormalize_event_names(load_raw_capture(path), canonical_names) for path in paths]
    profile = analyze_events(events, generated_at=args.generated_at)
    if args.db:
        db_path = Path(args.db) if Path(args.db).is_absolute() else repo / args.db
        envdb.write_profile(db_path, profile, raw_events=events)
        print(f"WROTE DB {db_path.relative_to(repo) if db_path.is_relative_to(repo) else db_path}")
    if args.output:
        text = json.dumps(profile, ensure_ascii=False, indent=2) + "\n"
        output = Path(args.output) if Path(args.output).is_absolute() else repo / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        print(f"WROTE {output.relative_to(repo) if output.is_relative_to(repo) else output}")
    if not args.db and not args.output:
        print(json.dumps(profile, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
