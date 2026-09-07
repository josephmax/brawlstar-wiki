#!/usr/bin/env python3
"""Fetch high-rank pick/use rates from Brawl Planet (Legendary+).

Brawl Planet exposes its data as static JSON on Google Cloud Storage:
  https://storage.googleapis.com/brawlanalyzer-public/<file>.json.gz
The `.json.gz` suffix is a naming convention; the payload is plain JSON.

Files:
  pl-l1-results.json.gz  -> Legendary I+ per-map per-brawler stats
  pl-m1-results.json.gz  -> Mythic I+ (alternative tier floor)
  pl-m3-results.json.gz  -> Mythic III+ (verified 2026-09-07, not linked in site nav)
  pl-d1-results.json.gz  -> Diamond I band (verified 2026-09-07)
  pl-results.json.gz     -> Diamond I+ (default powerleague page)
  brawlers.json.gz       -> brawler catalog (names, rarity, future flag)

No higher-tier floor exists (verified 2026-09-07: masters/elite/pro candidates 403;
site nav exposes only d1/m1/l1 variants). `pl-l1` is a rank FLOOR: the Legendary I+
sample already contains every higher in-game tier (Masters and above); the source
just cannot slice per-tier stats.

Ranked-pool filter: by default the signal only covers the current Ranked map pool
(`wiki/environment/ranked_pool.json`, `brawlstar.ranked_pool_manifest.v1`). The
global aggregate counts only in-pool active maps and `per_map` keeps in-pool rows
only; out-of-pool / inactive entries are reported in `summary.excluded_maps` for
audit. Pass `--no-ranked-pool-filter` to fetch the raw ladder-wide data instead.

Output: `brawlstar.environment_signal_pickrate.v1` — per-map use/win rates plus a
match-weighted global aggregate, as the pick-rate half of the BP environment signal.
The ban-rate half comes from monthly Liquipedia aggregation (aggregate_environment_signal.py).

Archive: write to `wiki/environment/pickrate.sqlite3` via `--db` (SQLite row storage,
persistent knowledge-base layer); the slot-decision compile folds it into the
runtime_bp_index via the `wiki/environment/current.json` pointer. `--output` writes a
JSON export for review. Tier generation is forbidden.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import _environment_sqlite as envdb
from typing import Any

GCS_BASE = "https://storage.googleapis.com/brawlanalyzer-public"
DEFAULT_FILES = {
    "pickrate": "pl-l1-results.json.gz",
    "brawlers": "brawlers.json.gz",
}
TIER_FILE_MAP = {
    "l1": "pl-l1-results.json.gz",
    "m1": "pl-m1-results.json.gz",
    "m3": "pl-m3-results.json.gz",
    "d1": "pl-d1-results.json.gz",
    "default": "pl-results.json.gz",
}
DEFAULT_UA = "Mozilla/5.0 brawlstar-wiki-maintainer/1.0 (https://github.com/josephmax/brawlstar-wiki)"
RANK_FLOOR = "legendary_plus"
RANKED_POOL_MANIFEST = Path(__file__).resolve().parents[3] / "wiki" / "environment" / "ranked_pool.json"


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


def pool_key(map_name: Any, mode_name: Any) -> tuple[str, str]:
    """Match key for a (map, mode) pair, case-insensitive.

    Map names keep punctuation because distinct maps can differ only there,
    e.g. "Safe Zone" vs "Safe(r) Zone". Mode names drop punctuation/spaces
    because the raw source field spells them without a space ("brawlball",
    "gemgrab", "hotzone") while display form uses "Brawl Ball" etc.
    """
    map_norm = str(map_name or "").strip().casefold()
    mode_norm = re.sub(r"[^0-9a-z]+", "", str(mode_name or "").casefold())
    return (map_norm, mode_norm)


def load_ranked_pool(path: Path) -> dict[str, Any]:
    """Load the current ranked-pool manifest; fail loudly when it is missing/stale."""
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(
            f"ERROR: ranked-pool manifest not found: {path}\n"
            "Update wiki/environment/ranked_pool.json for the current season, or pass "
            "--no-ranked-pool-filter to fetch unfiltered ladder-wide data."
        ) from exc
    maps = manifest.get("maps")
    if manifest.get("schema") != "brawlstar.ranked_pool_manifest.v1" or not isinstance(maps, list) or not maps:
        raise SystemExit(f"ERROR: invalid ranked-pool manifest (need brawlstar.ranked_pool_manifest.v1 with non-empty 'maps'): {path}")
    return manifest


def build_signal(
    pickrate: dict[str, Any],
    brawlers: list[dict[str, Any]],
    canonical: set[str],
    ranked_pool: dict[str, Any] | None = None,
) -> dict[str, Any]:
    future_names = {
        str(b.get("name") or "").upper()
        for b in (brawlers or [])
        if isinstance(b, dict) and b.get("future")
    }
    pool_set: set[tuple[str, str]] | None = None
    if ranked_pool is not None:
        pool_set = {pool_key(m.get("map"), m.get("mode")) for m in ranked_pool["maps"]}
    per_map: dict[str, dict[str, Any]] = {}
    global_ur: dict[str, float] = {}
    global_wr: dict[str, float] = {}
    global_weight: dict[str, int] = {}
    map_count = 0
    total_matches = 0
    active_maps = 0
    pool_seen: set[tuple[str, str]] = set()
    excluded_maps: list[dict[str, Any]] = []

    for key, entry in (pickrate or {}).items():
        if not isinstance(entry, dict):
            continue
        map_count += 1
        matches = int(entry.get("match_count") or 0)
        total_matches += matches
        is_active = bool(entry.get("active"))
        if is_active:
            active_maps += 1
        in_pool = pool_set is None or pool_key(entry.get("map"), entry.get("mode")) in pool_set
        if pool_set is not None:
            if in_pool:
                pool_seen.add(pool_key(entry.get("map"), entry.get("mode")))
            else:
                excluded_maps.append({
                    "map": entry.get("map"),
                    "mode": entry.get("modeFormatted") or entry.get("mode"),
                    "reason": "not_in_ranked_pool",
                })
                continue
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
            entry_out = {
                "map": entry.get("map"),
                "mode": entry.get("modeFormatted") or entry.get("mode"),
                "match_count": matches,
                "active": is_active,
                "latest_match_time": entry.get("latest_match_time"),
                "individual": rows,
            }
            if pool_set is not None:
                entry_out["ranked_pool"] = True
            per_map[key] = entry_out

    aggregate = {
        name: {
            "use_rate": round(global_ur[name] / global_weight[name], 2),
            "win_rate": round(global_wr[name] / global_weight[name], 2),
        }
        for name in global_ur
    }

    summary: dict[str, Any] = {
        "map_entries": map_count,
        "active_maps": active_maps,
        "total_matches": total_matches,
        "brawlers_with_sample": len(aggregate),
    }
    if pool_set is not None:
        missing = sorted(
            str(m.get("map"))
            for m in ranked_pool["maps"]
            if pool_key(m.get("map"), m.get("mode")) not in pool_seen
        )
        summary["ranked_pool"] = {
            "filtered": True,
            "season": ranked_pool.get("season"),
            "pool_map_count": len(ranked_pool["maps"]),
            "pool_maps_in_source": len(pool_seen),
            "pool_maps_missing_from_source": missing,
        }
        summary["excluded_maps"] = sorted(excluded_maps, key=lambda e: str(e.get("map")))

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
        "summary": summary,
        "global": aggregate,
        "per_map": per_map,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=str(Path(__file__).resolve().parents[3]))
    parser.add_argument("--user-agent", default=DEFAULT_UA)
    parser.add_argument("--tier", default="l1", choices=sorted(TIER_FILE_MAP), help="GCS stat file floor: l1 (Legendary+, default), m1, m3, d1, or default (Diamond+).")
    parser.add_argument("--ranked-pool-manifest", default=str(RANKED_POOL_MANIFEST), help="Ranked-pool manifest used to filter maps (default: wiki/environment/ranked_pool.json).")
    parser.add_argument("--no-ranked-pool-filter", action="store_true", help="Fetch raw ladder-wide data without Ranked-pool filtering.")
    parser.add_argument("--output", default="", help="Write JSON to this path (optional export).")
    parser.add_argument("--db", default="", help="Write the pickrate tables into this .sqlite3 (row/column storage).")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pickrate_url = f"{GCS_BASE}/{TIER_FILE_MAP[args.tier]}"
    brawlers_url = f"{GCS_BASE}/{DEFAULT_FILES['brawlers']}"
    pickrate = load_json_bytes(fetch(pickrate_url, args.user_agent))
    brawlers = load_json_bytes(fetch(brawlers_url, args.user_agent))
    canonical = canonical_names(Path(args.repo))
    ranked_pool = None if args.no_ranked_pool_filter else load_ranked_pool(Path(args.ranked_pool_manifest))
    signal = build_signal(pickrate, brawlers, canonical, ranked_pool)
    if ranked_pool is not None:
        pool_summary = (signal.get("summary") or {}).get("ranked_pool") or {}
        missing = pool_summary.get("pool_maps_missing_from_source") or []
        if missing:
            print(
                f"WARNING: {len(missing)} ranked-pool maps missing from source data "
                f"(season manifest may be stale): {', '.join(missing)}",
                file=sys.stderr,
            )
    text = json.dumps(signal, ensure_ascii=False, indent=2) + "\n"
    if args.db:
        db_path = Path(args.db)
        db_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_db = db_path.with_name(f"{db_path.name}.tmp{os.getpid()}")
        envdb.write_pickrate(tmp_db, signal)
        os.replace(tmp_db, db_path)
        print(f"WROTE DB {db_path}")
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
