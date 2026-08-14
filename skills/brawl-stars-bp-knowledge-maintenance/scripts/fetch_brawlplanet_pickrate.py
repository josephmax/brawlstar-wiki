#!/usr/bin/env python3
"""Fetch high-rank pick/use rates from Brawl Planet (Legendary+).

Brawl Planet exposes its data as static JSON on Google Cloud Storage:
  https://storage.googleapis.com/brawlanalyzer-public/<file>.json.gz
The `.json.gz` suffix is a naming convention; the payload is plain JSON.

Files:
  pl-l1-results.json.gz  -> Legendary I+ per-map per-brawler stats
  pl-m1-results.json.gz  -> Mythic I+ (alternative tier floor)
  pl-results.json.gz     -> Diamond I+ (default powerleague page)
  brawlers.json.gz       -> brawler catalog (names, rarity, future flag)

Output: `brawlstar.environment_signal_pickrate.v1` — per-map use/win rates plus a
match-weighted global aggregate, as the pick-rate half of the BP environment signal.
The ban-rate half comes from monthly Liquipedia aggregation (aggregate_environment_signal.py).

Policy: descriptive draft signal. runtime_consumption stays forbidden until a separate
reviewed promotion into the compiler's pickrate slot. Tier generation is forbidden.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GCS_BASE = "https://storage.googleapis.com/brawlanalyzer-public"
DEFAULT_FILES = {
    "pickrate": "pl-l1-results.json.gz",
    "brawlers": "brawlers.json.gz",
}
DEFAULT_UA = "Mozilla/5.0 brawlstar-wiki-maintainer/1.0 (https://github.com/josephmax/brawlstar-wiki)"
RANK_FLOOR = "legendary_plus"


def fetch(url: str, user_agent: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def load_json_bytes(raw: bytes) -> Any:
    text = raw.decode("utf-8", errors="replace")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        import gzip
        return json.loads(gzip.decompress(raw).decode("utf-8"))


def canonical_names(repo: Path) -> set[str]:
    directory = repo / "wiki" / "entities" / "brawlers"
    return {path.stem for path in directory.glob("*.md")} if directory.exists() else set()


def normalize_key(value: str) -> str:
    return re.sub(r"[^0-9a-z]+", "", str(value).casefold())


def titlecase_brawlplanet(name: str) -> str:
    return re.sub(r"\b[A-Z]+(?:'[A-Z]+)?\b", lambda m: m.group(0).title(), name)


def map_brawler_name(raw: str, canonical: set[str]) -> str | None:
    candidate = titlecase_brawlplanet(str(raw).strip())
    wanted = normalize_key(candidate)
    for name in canonical:
        if normalize_key(name) == wanted:
            return name
    return None


def build_signal(pickrate: dict[str, Any], brawlers: list[dict[str, Any]], canonical: set[str]) -> dict[str, Any]:
    future_names = {
        str(b.get("name") or "").upper()
        for b in (brawlers or [])
        if isinstance(b, dict) and b.get("future")
    }
    per_map: dict[str, dict[str, Any]] = {}
    global_ur: dict[str, float] = {}
    global_wr: dict[str, float] = {}
    global_weight: dict[str, int] = {}
    map_count = 0
    total_matches = 0
    active_maps = 0

    for key, entry in (pickrate or {}).items():
        if not isinstance(entry, dict):
            continue
        map_count += 1
        matches = int(entry.get("match_count") or 0)
        total_matches += matches
        is_active = bool(entry.get("active"))
        if is_active:
            active_maps += 1
        rows: dict[str, dict[str, Any]] = {}
        for row in entry.get("individual") or []:
            raw_name = str(row.get("brawler") or "").upper()
            if raw_name in future_names:
                continue
            name = map_brawler_name(raw_name, canonical)
            if not name:
                continue
            ur = float(row.get("ur") or 0)
            wr = float(row.get("wr") or 0)
            sr = float(row.get("sr") or 0)
            rows[name] = {"use_rate": round(ur, 2), "win_rate": round(wr, 2), "star_player_rate": round(sr, 2)}
            if is_active:
                global_ur[name] = global_ur.get(name, 0) + ur * matches
                global_wr[name] = global_wr.get(name, 0) + wr * matches
                global_weight[name] = global_weight.get(name, 0) + matches
        if rows:
            per_map[key] = {
                "map": entry.get("map"),
                "mode": entry.get("modeFormatted") or entry.get("mode"),
                "match_count": matches,
                "active": is_active,
                "latest_match_time": entry.get("latest_match_time"),
                "individual": rows,
            }

    aggregate = {
        name: {
            "use_rate": round(global_ur[name] / global_weight[name], 2),
            "win_rate": round(global_wr[name] / global_weight[name], 2),
        }
        for name in global_ur
    }

    return {
        "schema": "brawlstar.environment_signal_pickrate.v1",
        "window": "rolling_10_weeks",
        "rank_floor": RANK_FLOOR,
        "source": {
            "kind": "brawlplanet-gcs-static-json",
            "bucket": "brawlanalyzer-public",
            "file": DEFAULT_FILES["pickrate"],
            "page": "https://www.brawlplanet.com/powerleague/pl-l1",
            "sample_size_label": "match_count per map",
        },
        "policy": {
            "interpretation": "revealed_draft_preference_draft",
            "tier_generation": "forbidden",
            "runtime_consumption": "forbidden_until_reviewed_promotion",
        },
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "map_entries": map_count,
            "active_maps": active_maps,
            "total_matches": total_matches,
            "brawlers_with_sample": len(aggregate),
        },
        "global": aggregate,
        "per_map": per_map,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=str(Path(__file__).resolve().parents[3]))
    parser.add_argument("--user-agent", default=DEFAULT_UA)
    parser.add_argument("--tier", default="l1", choices=["l1", "m1", "default"], help="pl-l1 (Legendary+), pl-m1 (Mythic+), or default (Diamond+).")
    parser.add_argument("--output", default="", help="Write JSON to this path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    file_map = {"l1": "pl-l1-results.json.gz", "m1": "pl-m1-results.json.gz", "default": "pl-results.json.gz"}
    pickrate_url = f"{GCS_BASE}/{file_map[args.tier]}"
    brawlers_url = f"{GCS_BASE}/{DEFAULT_FILES['brawlers']}"
    pickrate = load_json_bytes(fetch(pickrate_url, args.user_agent))
    brawlers = load_json_bytes(fetch(brawlers_url, args.user_agent))
    canonical = canonical_names(Path(args.repo))
    signal = build_signal(pickrate, brawlers, canonical)
    text = json.dumps(signal, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
