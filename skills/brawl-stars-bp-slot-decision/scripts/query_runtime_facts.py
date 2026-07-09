#!/usr/bin/env python3
"""Return a neutral fact window from a compiled runtime_bp_index."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from runtime_index_tools import (
    brawler_matchups,
    canonical_brawler_name,
    candidate_map_fit,
    candidate_strength,
    compact_manifest,
    emit_payload,
    format_query_summary,
    load_runtime_index,
    map_context,
    normalize_key,
    retrieval_log,
    runtime_card_fragment,
    runtime_card_counts,
    strength_scalars,
    strip_tool_internal_keys,
)


EFFORT_LIMITS = {
    "low": 24,
    "high": 32,
}


def map_fact_packet(context: dict[str, Any]) -> dict[str, Any]:
    return strip_tool_internal_keys({
        "map": context.get("map"),
        "mode": context.get("mode"),
        "source_ref": context.get("source_ref"),
        "objective_contracts": context.get("objective_contracts") or [],
        "required_capabilities": context.get("required_capabilities") or [],
        "route_gates": context.get("route_gates") or [],
        "hard_gates": context.get("hard_gates") or [],
        "false_positive_filters": context.get("false_positive_filters") or [],
    })


def bucket_items(index: dict[str, Any], map_name: str, buckets: list[str]) -> list[dict[str, Any]]:
    signature = index["map_pool_signature"][map_name]
    projection = signature.get("candidate_projection") or {}
    candidate_index = signature.get("candidate_index") or {}
    selected_buckets = buckets or list(projection.keys())
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    for bucket in selected_buckets:
        for item in projection.get(bucket) or []:
            name = item.get("brawler")
            if not name or name in seen:
                continue
            enriched = dict(candidate_index.get(name) or {})
            enriched.update(item)
            enriched["retrieval_bucket"] = bucket
            enriched["projection_buckets"] = candidate_index.get(name, {}).get("projection_buckets") or [bucket]
            items.append(enriched)
            seen.add(name)
    if buckets:
        return items
    for name, item in candidate_index.items():
        if name in seen:
            continue
        enriched = dict(item)
        enriched["brawler"] = name
        items.append(enriched)
    return items


def relation_targets(index: dict[str, Any], raw_targets: list[str]) -> set[str]:
    return {canonical_brawler_name(index, raw) for raw in raw_targets}


def edge_matches_target(edge: dict[str, Any], targets: set[str]) -> bool:
    if not targets:
        return True
    return normalize_key(edge.get("target") or "") in {normalize_key(target) for target in targets}


def neutral_relation(edge: dict[str, Any], source: str, target: str, direction: str) -> dict[str, Any]:
    return {
        "source": source,
        "target": target,
        "direction": direction,
        "relation_family": "conditional_matchup",
        "mechanism": edge.get("mechanism"),
        "active_when": edge.get("active_when"),
        "fails_when": edge.get("fails_when"),
    }


def conditional_relations(index: dict[str, Any], brawler: str, targets: set[str]) -> list[dict[str, Any]]:
    relations: list[dict[str, Any]] = []
    matchups = brawler_matchups(index, brawler)
    for edge in matchups.get("answers") or []:
        if not edge_matches_target(edge, targets):
            continue
        relations.append(neutral_relation(edge, brawler, edge.get("target") or "", "outgoing"))
    for edge in matchups.get("is_answered_by") or []:
        if not edge_matches_target(edge, targets):
            continue
        relations.append(neutral_relation(edge, edge.get("target") or "", brawler, "incoming"))
    return relations


def has_relation_to_targets(index: dict[str, Any], brawler: str, targets: set[str]) -> bool:
    return bool(targets and conditional_relations(index, brawler, targets))


def candidate_sort_key(index: dict[str, Any], name: str, item: dict[str, Any]) -> tuple[int, int, str]:
    strength = candidate_strength(index, name, item)
    map_signal = bool(item.get("active_hook_ids") or item.get("matched_capabilities"))
    return (0 if map_signal else 1, int(strength.get("total_rank") or 9999), name)


def fact_payload(index: dict[str, Any], map_name: str, name: str, item: dict[str, Any], targets: set[str]) -> dict[str, Any]:
    fit = candidate_map_fit(index, map_name, name)
    if item:
        fit.update({key: value for key, value in item.items() if key != "brawler"})
    strength = candidate_strength(index, name, fit)
    card = runtime_card_fragment(index, name, fit)
    relations = conditional_relations(index, name, targets)
    buckets = list(
        dict.fromkeys(
            [
                *([item["retrieval_bucket"]] if item.get("retrieval_bucket") else []),
                *(item.get("projection_buckets") or fit.get("projection_buckets") or []),
            ]
        )
    )
    return {
        "id": name,
        "entity_type": "brawler",
        "retrieval_matches": item.get("retrieval_matches") or [],
        "retrieval_buckets": buckets,
        "map_fit": {
            "fit": fit.get("fit"),
            "map_floor_fit": fit.get("map_floor_fit"),
            "mode_contract_fit": fit.get("mode_contract_fit"),
            "mode_contract_hit": fit.get("mode_contract_hit") or False,
        },
        "strength": strength,
        **strength_scalars(strength),
        "map_hook_ids": fit.get("active_hook_ids") or [],
        "matched_capabilities": fit.get("matched_capabilities") or [],
        "failure_gate_ids": fit.get("failure_gates") or fit.get("risk_ids") or [],
        "required_build_ids": fit.get("required_build_ids") or [],
        "runtime_card": card,
        "runtime_card_counts": runtime_card_counts(card),
        "conditional_relations": relations,
        "relation_count": len(relations),
    }


def query_runtime_facts(args: argparse.Namespace) -> dict[str, Any]:
    index = load_runtime_index(args.index)
    context = map_context(index, args.map)
    map_name = context["map"]
    includes = [canonical_brawler_name(index, raw) for raw in args.include_id]
    excludes = {canonical_brawler_name(index, raw) for raw in args.exclude_id}
    targets = relation_targets(index, args.relation_target)
    limit = args.limit if args.limit is not None else EFFORT_LIMITS[args.effort]

    items_by_name: dict[str, dict[str, Any]] = {}
    for item in bucket_items(index, map_name, args.bucket):
        name = item.get("brawler")
        if not name or name in excludes:
            continue
        item = dict(item)
        item["retrieval_matches"] = [f"bucket:{item.get('retrieval_bucket')}"]
        items_by_name[name] = item

    candidate_index = index["map_pool_signature"][map_name].get("candidate_index") or {}
    for name in includes:
        if name in excludes:
            continue
        item = dict(candidate_index.get(name) or {})
        item["brawler"] = name
        item["retrieval_matches"] = list(dict.fromkeys(["include_id", *(items_by_name.get(name, {}).get("retrieval_matches") or [])]))
        items_by_name[name] = item

    for name, item in candidate_index.items():
        if name in excludes or name in items_by_name:
            continue
        if not has_relation_to_targets(index, name, targets):
            continue
        enriched = dict(item)
        enriched["brawler"] = name
        enriched["retrieval_matches"] = ["relation_target"]
        items_by_name[name] = enriched

    ordered_names = [
        name
        for name in includes
        if name in items_by_name
    ]
    remaining = [
        name for name in items_by_name if name not in set(ordered_names)
    ]
    remaining.sort(key=lambda name: candidate_sort_key(index, name, items_by_name[name]))
    ordered_names.extend(remaining)
    if limit:
        ordered_names = ordered_names[:limit]

    fact_window = [
        fact_payload(index, map_name, name, items_by_name[name], targets)
        for name in ordered_names
    ]
    body = {
        "runtime_fact_query": {
            "manifest": compact_manifest(index),
            "scope": {
                "map": map_name,
                "mode": args.mode or context.get("mode"),
            },
            "request": {
                "entity_type": args.entity_type,
                "include_ids": includes,
                "exclude_ids": sorted(excludes),
                "relation_targets": sorted(targets),
                "buckets": args.bucket,
                "fields": args.field,
                "effort": args.effort,
                "limit": limit,
                "limit_source": "explicit" if args.limit is not None else "effort",
            },
            "map_fact_packet": map_fact_packet(context),
            "fact_window": fact_window,
        }
    }
    log = retrieval_log(
        "query_runtime_facts",
        args.index,
        fragments=len(fact_window) + 1,
        payload=body,
    )
    log["entity_fragments"] = len(fact_window)
    log["map_fragments"] = 1
    body["runtime_fact_query"]["retrieval_summary"] = log
    return body


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", required=True, help="Compiled runtime_bp_index JSON path")
    parser.add_argument("--map", required=True, help="Map name covered by the index")
    parser.add_argument("--mode", default="", help="Optional mode echo")
    parser.add_argument("--entity-type", default="brawler", choices=["brawler"], help="Entity type to retrieve")
    parser.add_argument("--include-id", action="append", default=[], help="Entity id to force include; repeatable")
    parser.add_argument("--exclude-id", action="append", default=[], help="Entity id to exclude from the fact window; repeatable")
    parser.add_argument("--relation-target", action="append", default=[], help="Entity id used to filter conditional relation facts; repeatable")
    parser.add_argument("--bucket", action="append", default=[], help="Compiled retrieval bucket id to include; repeatable")
    parser.add_argument("--field", action="append", default=[], help="Requested field hint for callers; repeatable")
    parser.add_argument(
        "--effort",
        choices=sorted(EFFORT_LIMITS),
        default="low",
        help="Recall budget preset: low=24, high=32",
    )
    parser.add_argument("--limit", type=int, default=None, help="Override effort budget; maximum entity fact fragments to return; 0 means no limit")
    parser.add_argument("--summary", action="store_true", help="Emit a compact text summary for agent-readable debugging")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        payload = query_runtime_facts(args)
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"query_runtime_facts error: {exc}", file=sys.stderr)
        return 2
    if args.summary:
        print(format_query_summary(payload["runtime_fact_query"]))
        return 0
    emit_payload(payload, args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
