#!/usr/bin/env python3
"""Build a neutral tournament_observation_profile.v1 from event raw captures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from _liquipedia_event import analyze_events, load_raw_capture


ROOT = Path(__file__).resolve().parents[3]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", action="append", required=True, help="Event raw capture; repeatable.")
    parser.add_argument("--repo", default=str(ROOT))
    parser.add_argument("--generated-at", help="Optional fixed ISO timestamp for reproducible output.")
    parser.add_argument("--output", help="Write JSON under outputs/ or another caller-provided path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).resolve()
    paths = [Path(value) if Path(value).is_absolute() else repo / value for value in args.raw]
    profile = analyze_events([load_raw_capture(path) for path in paths], generated_at=args.generated_at)
    text = json.dumps(profile, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = Path(args.output) if Path(args.output).is_absolute() else repo / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        print(f"WROTE {output.relative_to(repo) if output.is_relative_to(repo) else output}")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
