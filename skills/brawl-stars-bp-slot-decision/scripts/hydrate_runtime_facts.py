#!/usr/bin/env python3
"""Hydrate neutral entity facts from a compiled runtime_bp_index."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from query_runtime_facts import conditional_relations, map_fact_packet, relation_targets
from runtime_index_tools import (
    canonical_brawler_name,
    candidate_map_fit,
    candidate_strength,
    compact_manifest,
    emit_payload,
    format_hydration_summary,
    load_runtime_index,
    map_context,
    retrieval_bucket_hits,
    retrieval_log,
    runtime_card_fragment,
    runtime_card_counts,
    strength_scalars,
)


def hydrate_runtime_facts(args: argparse.Namespace) -> dict[str, Any]:
    index = load_runtime_index(args.index)
    context = map_context(index, args.map)
    map_name = context["map"]
    targets = relation_targets(index, args.relation_target)
    excludes = {canonical_brawler_name(index, raw) for raw in args.exclude_id}
    evidence_refs = index.get("evidence_refs") or {}
    brawler_refs = evidence_refs.get("brawlers") or {}
    entities: dict[str, Any] = {}

    for raw_name in args.include_id:
        name = canonical_brawler_name(index, raw_name)
        if name in excludes:
            continue
        fit = candidate_map_fit(index, map_name, name)
        strength = candidate_strength(index, name, fit)
        card = runtime_card_fragment(index, name, fit)
        relations = conditional_relations(index, name, targets)
        entities[name] = {
            "id": name,
            "entity_type": "brawler",
            "map_strength": strength,
            **strength_scalars(strength),
            "evidence_ref": brawler_refs.get(name),
            "retrieval_bucket_hits": retrieval_bucket_hits(index, map_name, name),
            "candidate_map_fit": fit,
            "runtime_card": card,
            "runtime_card_counts": runtime_card_counts(card),
            "conditional_relations": relations,
            "relation_count": len(relations),
        }

    body = {
        "runtime_fact_hydration": {
            "manifest": compact_manifest(index),
            "scope": {
                "map": map_name,
                "mode": args.mode or context.get("mode"),
            },
            "request": {
                "entity_type": args.entity_type,
                "include_ids": [canonical_brawler_name(index, raw) for raw in args.include_id],
                "exclude_ids": sorted(excludes),
                "relation_targets": sorted(targets),
            },
            "map_fact_packet": map_fact_packet(context),
            "entities": entities,
            "entity_window": list(entities.values()),
            "evidence_refs": {
                "strength_profile": evidence_refs.get("strength_profile"),
                "map": (evidence_refs.get("maps") or {}).get(map_name),
            },
        }
    }
    log = retrieval_log(
        "hydrate_runtime_facts",
        args.index,
        fragments=len(entities) + 1,
        payload=body,
    )
    log["entity_fragments"] = len(entities)
    log["map_fragments"] = 1
    body["runtime_fact_hydration"]["retrieval_summary"] = log
    return body


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", required=True, help="Compiled runtime_bp_index JSON path")
    parser.add_argument("--map", required=True, help="Map name covered by the index")
    parser.add_argument("--mode", default="", help="Optional mode echo")
    parser.add_argument("--entity-type", default="brawler", choices=["brawler"], help="Entity type to hydrate")
    parser.add_argument("--include-id", action="append", required=True, help="Entity id to hydrate; repeatable")
    parser.add_argument("--exclude-id", action="append", default=[], help="Entity id to skip; repeatable")
    parser.add_argument("--relation-target", action="append", default=[], help="Entity id used to filter conditional relation facts; repeatable")
    parser.add_argument("--summary", action="store_true", help="Emit a compact text summary for agent-readable debugging")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        payload = hydrate_runtime_facts(args)
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"hydrate_runtime_facts error: {exc}", file=sys.stderr)
        return 2
    if args.summary:
        print(format_hydration_summary(payload["runtime_fact_hydration"]))
        return 0
    emit_payload(payload, args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
