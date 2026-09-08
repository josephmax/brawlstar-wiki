#!/usr/bin/env python3
"""Return a neutral fact window from a compiled runtime_bp_index."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any
from candidate_mask import read_mask, validate_mask, allows, mask_summary

from runtime_index_tools import (
    brawler_matchups,
    cache_load,
    cache_store,
    canonical_brawler_name,
    candidate_map_fit,
    compact_manifest,
    emit_payload,
    format_query_summary,
    load_runtime_index,
    map_context,
    normalize_key,
    query_cache_key,
    retrieval_log,
    runtime_card_fragment,
    runtime_card_counts,
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


def brawler_capability_tags(index: dict[str, Any], brawler: str) -> set[str]:
    card = (index.get("brawler_runtime_cards") or {}).get(brawler) or {}
    return {normalize_key(tag) for tag in (card.get("capability_tags") or [])}


def capability_window_filter(index: dict[str, Any], name: str, wanted: set[str]) -> bool:
    """Keep a brawler when it has any wanted capability tag.

    ``--capability`` is the capability-window retrieval primitive: it turns
    "give me heroes with wall-bypass / crowd-control" into a concrete filter
    over the stable ``runtime_card.capability_tags``, instead of relying on an
    alphabetical window of map-fit candidates.
    """
    if not wanted:
        return True
    return bool(brawler_capability_tags(index, name) & wanted)


# Ordinal scale for capability levels. Mirror of compile_runtime_index.py's
# CAPABILITY_LEVEL_ORDER; test_runtime_index_tools.py asserts both copies
# stay identical so threshold/floor semantics never drift apart.
CAPABILITY_LEVEL_ORDER: dict[str, int] = {
    "none": 0,
    "low": 1,
    "medium_low": 2,
    "medium": 3,
    "medium_high": 4,
    "high": 5,
    "very_high": 6,
}


def brawler_archetypes(index: dict[str, Any], name: str) -> set[str]:
    card = (index.get("brawler_runtime_cards") or {}).get(name) or {}
    return set(card.get("archetypes") or [])


def archetype_window_filter(index: dict[str, Any], name: str, wanted: set[str]) -> bool:
    """``--archetype`` keeps brawlers derived-tagged with any wanted class."""
    if not wanted:
        return True
    return bool(brawler_archetypes(index, name) & wanted)


def parse_floor_spec(spec: str) -> tuple[list[str], str]:
    """Parse "dim1,dim2@level" into (dims, level). Raises ValueError on junk."""
    if "@" not in spec:
        raise ValueError(f"--require-floor expects 'dim1,dim2@level', got: {spec!r}")
    dims_part, level = spec.rsplit("@", 1)
    dims = [d.strip() for d in dims_part.split(",") if d.strip()]
    level = level.strip().lower()
    if not dims or level not in CAPABILITY_LEVEL_ORDER:
        raise ValueError(f"--require-floor expects 'dim1,dim2@level', got: {spec!r}")
    return dims, level


def floor_window_filter(index: dict[str, Any], name: str, floors: list[tuple[list[str], str]]) -> bool:
    """``--require-floor "survivability,disengage@medium"`` keeps brawlers
    whose every named axis reaches at least that level — the "no weak axis /
    dual-duty allrounder" query (R-T / Pearl shape), not a peak query."""
    if not floors:
        return True
    card = (index.get("brawler_runtime_cards") or {}).get(name) or {}
    levels = card.get("capability_levels") or {}
    for dims, level in floors:
        threshold = CAPABILITY_LEVEL_ORDER[level]
        for dim in dims:
            value = CAPABILITY_LEVEL_ORDER.get(levels.get(dim) or "")
            if value is None or value < threshold:
                return False
    return True


FIT_RANK = {"strong": 0, "medium": 1, "weak": 2}


def candidate_sort_key(index: dict[str, Any], name: str, item: dict[str, Any], wanted_capabilities: set[str]) -> tuple[int, int, int, int, int, str]:
    """Order candidates by evidence relevance, not by name.

    Primary: number of requested capability tags matched (0 when no
    capability window is active), so capability-window queries surface the
    requested pool first.
    Then: map fit rank (strong < medium < weak < no-signal), active map hook
    count, matched capability count. Name is only the final tiebreaker so the
    window is stable and not alphabetical-truncated (which used to starve
    W-Z brawlers such as Willow).
    """
    matched = len((brawler_capability_tags(index, name) & wanted_capabilities)) if wanted_capabilities else 0
    fit = (item.get("fit") or "").lower()
    fit_rank = FIT_RANK.get(fit, 3)
    hook_count = len(item.get("active_hook_ids") or [])
    capability_count = len(item.get("matched_capabilities") or [])
    return (0 if matched else 1, fit_rank, -hook_count, -capability_count, 0 if hook_count or capability_count else 1, name)


def map_environment_row(index: dict[str, Any], map_name: str, mode: str | None, name: str) -> dict[str, Any] | None:
    """Return this brawler's Legendary+ per-map ladder row, if one exists.

    Mirrors how hydrate_runtime_facts resolves `environment_ladder_per_map`:
    rows match by map (and by mode when a mode is resolvable).
    """
    for row in (index.get("environment_ladder_per_map") or {}).values():
        if row.get("map") != map_name:
            continue
        if mode and row.get("mode") != mode:
            continue
        individual = row.get("individual") or {}
        if name in individual:
            return {"active": row.get("active"), **(individual[name] or {})}
    return None


def ban_pressure_env_sort_key(
    index: dict[str, Any],
    map_name: str,
    mode: str | None,
    name: str,
    item: dict[str, Any],
    wanted_capabilities: set[str],
) -> tuple[int, ...]:
    """Order ban_pressure recall by the map's own environment ladder.

    Active ladder rows come first by use_rate then win_rate, so the effort
    cut lands on environment-hot candidates instead of hook-count/name
    order. Names without an active row fall back to the generic
    evidence-relevance order (fit, hooks, capabilities, name). Bucket
    membership is unchanged; only presentation order — and therefore which
    names survive the effort truncation — differs.
    """
    row = map_environment_row(index, map_name, mode, name)
    if row is not None and row.get("active"):
        use_rate = row.get("use_rate")
        win_rate = row.get("win_rate")
        return (
            0,
            -(use_rate if isinstance(use_rate, (int, float)) else 0.0),
            -(win_rate if isinstance(win_rate, (int, float)) else 0.0),
            name,
        )
    return (1,) + candidate_sort_key(index, name, item, wanted_capabilities)


def fact_payload(index: dict[str, Any], map_name: str, name: str, item: dict[str, Any], targets: set[str]) -> dict[str, Any]:
    fit = candidate_map_fit(index, map_name, name)
    if item:
        fit.update({key: value for key, value in item.items() if key != "brawler"})
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
        "map_hook_ids": fit.get("active_hook_ids") or [],
        "matched_capabilities": fit.get("matched_capabilities") or [],
        "failure_gate_ids": fit.get("failure_gates") or fit.get("risk_ids") or [],
        "failure_gate_activation": fit.get("failure_gate_activation") or {},
        "required_build_ids": fit.get("required_build_ids") or [],
        "runtime_card": card,
        "runtime_card_counts": runtime_card_counts(card),
        "conditional_relations": relations,
        "relation_count": len(relations),
    }


def query_runtime_facts(args: argparse.Namespace) -> dict[str, Any]:
    mask = read_mask(getattr(args, "candidate_mask_file", None))
    cache_key = query_cache_key("query_runtime_facts", args.index, {
        "mask": mask,
        "capability": args.capability,
        "archetype": args.archetype,
        "require_floor": args.require_floor,
        "map": args.map,
        "mode": args.mode,
        "bucket": args.bucket,
        "include_id": args.include_id,
        "exclude_id": args.exclude_id,
        "relation_target": args.relation_target,
        "effort": args.effort,
        "limit": args.limit,
        "field": args.field,
    })
    cached = cache_load(args.cache_dir, cache_key)
    if cached is not None:
        cached.setdefault("runtime_fact_query", {})["cache_hit"] = True
        return cached

    index = load_runtime_index(args.index)
    validate_mask(mask, index)
    context = map_context(index, args.map)
    map_name = context["map"]
    includes = [canonical_brawler_name(index, raw) for raw in args.include_id]
    excludes = {canonical_brawler_name(index, raw) for raw in args.exclude_id}
    targets = relation_targets(index, args.relation_target)
    wanted_capabilities = {normalize_key(raw) for raw in args.capability}
    # Archetype IDs are schema keys, not brawler names. Keep underscores so
    # thrower_core / tank_front / dual_duty_mid match the compiled card IDs.
    wanted_archetypes = {raw.strip().lower() for raw in args.archetype}
    floors = [parse_floor_spec(raw) for raw in args.require_floor]
    limit = args.limit if args.limit is not None else EFFORT_LIMITS[args.effort]

    def passes_windows(idx: dict[str, Any], name: str) -> bool:
        return (
            capability_window_filter(idx, name, wanted_capabilities)
            and archetype_window_filter(idx, name, wanted_archetypes)
            and floor_window_filter(idx, name, floors)
        )

    items_by_name: dict[str, dict[str, Any]] = {}
    for item in bucket_items(index, map_name, args.bucket):
        name = item.get("brawler")
        if not name or name in excludes or not allows(mask, name):
            continue
        if not passes_windows(index, name):
            continue
        item = dict(item)
        item["retrieval_matches"] = [f"bucket:{item.get('retrieval_bucket')}"]
        items_by_name[name] = item

    candidate_index = index["map_pool_signature"][map_name].get("candidate_index") or {}
    for name in includes:
        if name in excludes or not allows(mask, name):
            continue
        item = dict(candidate_index.get(name) or {})
        item["brawler"] = name
        item["retrieval_matches"] = list(dict.fromkeys(["include_id", *(items_by_name.get(name, {}).get("retrieval_matches") or [])]))
        items_by_name[name] = item

    for name, item in candidate_index.items():
        if name in excludes or name in items_by_name or not allows(mask, name):
            continue
        if not has_relation_to_targets(index, name, targets):
            continue
        if not passes_windows(index, name):
            continue
        enriched = dict(item)
        enriched["brawler"] = name
        enriched["retrieval_matches"] = ["relation_target"]
        items_by_name[name] = enriched

    # An active capability/archetype/floor window scans the FULL candidate
    # index, not just projection buckets: "I need a thrower" must be able to
    # surface a fit=weak thrower on an open map (visible with its weak fit
    # and ranked below strong fits) instead of pretending the hero does not
    # exist. Without a window, plain bucket behavior is unchanged.
    if wanted_capabilities or wanted_archetypes or floors:
        for name, item in candidate_index.items():
            if name in excludes or name in items_by_name or not allows(mask, name):
                continue
            if not passes_windows(index, name):
                continue
            enriched = dict(item)
            enriched["brawler"] = name
            enriched["retrieval_matches"] = ["capability_window"]
            items_by_name[name] = enriched

    ordered_names = [
        name
        for name in includes
        if name in items_by_name
    ]
    remaining = [
        name for name in items_by_name if name not in set(ordered_names)
    ]
    if "ban_pressure" in args.bucket:
        # The effort cut must land on the decision-relevant axis: order
        # ban_pressure recall by the map's own environment ladder (see
        # ban_pressure_env_sort_key) instead of hook-count/name order.
        remaining.sort(
            key=lambda name: ban_pressure_env_sort_key(
                index,
                map_name,
                args.mode or context.get("mode"),
                name,
                items_by_name[name],
                wanted_capabilities,
            )
        )
    else:
        remaining.sort(key=lambda name: candidate_sort_key(index, name, items_by_name[name], wanted_capabilities))
    ordered_names.extend(remaining)
    if limit:
        # Capability/archetype/floor window hits are never truncated by the
        # effort budget: the window's whole point is that every matching
        # brawler is visible, no matter where its name or hook count falls.
        # Only non-matching fill brawlers are capped. Explicit --include-id
        # names are always preserved regardless of any filter.
        if wanted_capabilities or wanted_archetypes or floors:
            def window_hit(name: str) -> bool:
                return (
                    bool(brawler_capability_tags(index, name) & wanted_capabilities)
                    or bool(brawler_archetypes(index, name) & wanted_archetypes)
                    or floor_window_filter(index, name, floors)
                )

            protected = set(includes) | {
                name for name in ordered_names if window_hit(name)
            }
            keep = [name for name in ordered_names if name in protected]
            fill = [name for name in ordered_names if name not in protected]
            ordered_names = keep + fill[:max(0, limit - len(keep))]
        else:
            ordered_names = ordered_names[:limit]

    fact_window = [
        fact_payload(index, map_name, name, items_by_name[name], targets)
        for name in ordered_names
        if allows(mask, name)
    ]
    body = {
        "runtime_fact_query": {
            "candidate_mask": mask_summary(mask),
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
                "capabilities": sorted(wanted_capabilities),
                "archetypes": sorted(wanted_archetypes),
                "require_floor": [f"{','.join(dims)}@{level}" for dims, level in floors],
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
    log["masked_candidate_index_count"] = sum(not allows(mask, name) for name in candidate_index)
    body["runtime_fact_query"]["retrieval_summary"] = log
    cache_store(args.cache_dir, cache_key, body)
    return body


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", required=True, help="Compiled runtime_bp_index JSON path")
    parser.add_argument("--candidate-mask-file", help="Hard candidate_mask.v1 allowlist; include cannot override it")
    parser.add_argument("--map", required=True, help="Map name covered by the index")
    parser.add_argument("--mode", default="", help="Optional mode echo")
    parser.add_argument("--entity-type", default="brawler", choices=["brawler"], help="Entity type to retrieve")
    parser.add_argument("--include-id", action="append", default=[], help="Entity id to force include; repeatable")
    parser.add_argument("--exclude-id", action="append", default=[], help="Entity id to exclude from the fact window; repeatable")
    parser.add_argument("--relation-target", action="append", default=[], help="Entity id used to filter conditional relation facts; repeatable")
    parser.add_argument("--capability", action="append", default=[], help="Capability tag required on the brawler's runtime card (OR semantics; repeatable); --include-id brawlers bypass this filter", metavar="TAG")
    parser.add_argument("--archetype", action="append", default=[], help="Derived archetype class to require, e.g. assassin / sniper / dual_duty_mid (OR semantics; repeatable)", metavar="CLASS")
    parser.add_argument("--require-floor", action="append", default=[], help="Floor constraint 'dim1,dim2@level': every named axis must reach at least that level (AND; repeatable groups)", metavar="DIMS@LEVEL")
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
    parser.add_argument("--cache-dir", default="", help="Directory for cross-query disk cache (same params skip recompute); empty disables")
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
