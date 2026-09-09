#!/usr/bin/env python3
"""Census of surviving counters for a hero given the current ban set.

Answers the draft question "this opponent pick — can the remaining pool
still answer it?" mechanically: the matchup edges already live in the
compiled index (is_answered_by / answers); this tool only filters them by
who is still available. It is a neutral fact census — it never says whether
to ban, pick, or counter; interpreting counts is the player LLM's job.

Typical use (ban-phase / first-pick threat read):

    python3 query_matchup_census.py \
      --index outputs/runtime-bp-index/default-runtime-index.json \
      --hero "Squeak" \
      --banned "Sprout" --banned "Piper" --banned "Pierce" --banned "Brock" \
      --json
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any
from candidate_mask import read_mask, validate_mask, allows, mask_summary

from runtime_index_tools import (
    brawler_matchups,
    canonical_brawler_name,
    emit_payload,
    load_runtime_index,
    retrieval_log,
)


def project_edges(edges: list[dict[str, Any]] | None, banned: set[str]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for edge in edges or []:
        target = edge.get("target") or ""
        rows.append(
            {
                "target": target,
                "alive": target not in banned,
                "mechanism": edge.get("mechanism"),
                "active_when": edge.get("active_when"),
                "fails_when": edge.get("fails_when"),
            }
        )
    alive = [row for row in rows if row["alive"]]
    return {
        "alive": alive,
        "alive_count": len(alive),
        "total_edges": len(rows),
        "removed_by_bans": len(rows) - len(alive),
    }


def census(index: dict[str, Any], hero: str, banned: set[str], mask: dict[str, Any] | None = None) -> dict[str, Any]:
    matchups = brawler_matchups(index, hero)
    result = {
        "hero": hero,
        "banned": sorted(banned),
        # "who can still punish this hero" — shrinking alive_count means the
        # ban phase removed its predators and the pick got safer.
        "answered_by": project_edges(matchups.get("is_answered_by") or [], banned),
        # "who this hero still punishes" — shrinking alive_count means the
        # ban phase removed its prey and banning/picking it lost value.
        "answers": project_edges(matchups.get("answers") or [], banned),
    }
    if mask is not None:
        validate_mask(mask, index)
        surviving = result["answered_by"]["alive"]
        visible = [row for row in surviving if allows(mask, row["target"])]
        result["candidate_mask"] = mask_summary(mask)
        result["masked_answered_by"] = {
            "alive": visible, "alive_count": len(visible),
            "removed_by_mask": len(surviving) - len(visible),
        }
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", required=True, help="Compiled runtime_bp_index JSON path")
    parser.add_argument("--candidate-mask-file", help="Additional answered_by projection within this recall mask; global census is unchanged")
    parser.add_argument("--hero", required=True, help="Hero to census (canonical or alias)")
    parser.add_argument("--banned", action="append", default=[], help="Hero removed from the pool; repeatable")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        index = load_runtime_index(args.index)
        hero = canonical_brawler_name(index, args.hero)
        banned = {canonical_brawler_name(index, raw) for raw in args.banned}
        mask = read_mask(args.candidate_mask_file)
        payload = {"matchup_census": census(index, hero, banned, mask)}
        payload["matchup_census"]["retrieval_summary"] = retrieval_log(
            "query_matchup_census",
            args.index,
            fragments=(
                payload["matchup_census"]["answered_by"]["total_edges"]
                + payload["matchup_census"]["answers"]["total_edges"]
            ),
            payload=payload,
        )
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"query_matchup_census error: {exc}", file=sys.stderr)
        return 2
    if not args.json:
        census_body = payload["matchup_census"]
        lines = [
            f"matchup census: {census_body['hero']} (banned={len(census_body['banned'])})",
            f"  answered_by: {census_body['answered_by']['alive_count']}/{census_body['answered_by']['total_edges']} alive"
            f" -> {', '.join(row['target'] for row in census_body['answered_by']['alive']) or '无'}",
            f"  answers:     {census_body['answers']['alive_count']}/{census_body['answers']['total_edges']} alive"
            f" -> {', '.join(row['target'] for row in census_body['answers']['alive']) or '无'}",
        ]
        print("\n".join(lines))
        return 0
    emit_payload(payload, True)
    return 0


if __name__ == "__main__":
    main()
