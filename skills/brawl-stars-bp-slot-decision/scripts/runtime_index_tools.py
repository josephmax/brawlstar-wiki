#!/usr/bin/env python3
"""Shared helpers for querying compiled BP runtime indexes."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


TOOL_INTERNAL_KEYS = {"bp_use", "proof_threshold"}


def strip_tool_internal_keys(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: strip_tool_internal_keys(item)
            for key, item in value.items()
            if key not in TOOL_INTERNAL_KEYS
        }
    if isinstance(value, list):
        return [strip_tool_internal_keys(item) for item in value]
    return value


def normalize_key(value: str) -> str:
    return re.sub(r"[^0-9a-z]+", "", str(value).casefold())


def load_runtime_index(index_path: str) -> dict[str, Any]:
    path = Path(index_path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if "runtime_bp_index" in payload and isinstance(payload["runtime_bp_index"], dict):
        payload = payload["runtime_bp_index"]
    for key in ("manifest", "map_pool_signature", "brawler_runtime_cards", "evidence_refs"):
        if key not in payload:
            raise ValueError(f"runtime index missing {key}")
    return payload


def canonical_map_name(index: dict[str, Any], map_name: str) -> str:
    maps = index.get("map_pool_signature") or {}
    if map_name in maps:
        return map_name
    wanted = normalize_key(map_name)
    for name in maps:
        if normalize_key(name) == wanted:
            return name
    raise ValueError(f"map not covered by runtime index: {map_name}")


def canonical_brawler_name(index: dict[str, Any], brawler: str) -> str:
    brawlers = set((index.get("brawler_runtime_cards") or {}).keys())
    brawlers.update(index.get("manifest", {}).get("available_brawlers") or [])
    if brawler in brawlers:
        return brawler
    wanted = normalize_key(brawler)
    for name in brawlers:
        if normalize_key(name) == wanted:
            return name
    raise ValueError(f"brawler not covered by runtime index: {brawler}")


def compact_manifest(index: dict[str, Any]) -> dict[str, Any]:
    manifest = index.get("manifest") or {}
    keys = [
        "patch_id",
        "map_pool_id",
        "strength_profile_id",
        "strength_profile_hash",
        "compiler_version",
        "index_shape",
    ]
    return {key: manifest.get(key) for key in keys if key in manifest}


def map_context(index: dict[str, Any], map_name: str) -> dict[str, Any]:
    canonical = canonical_map_name(index, map_name)
    source = index["map_pool_signature"][canonical]
    if "map_context" in source:
        return dict(source["map_context"])
    return {
        "map": canonical,
        "mode": source.get("mode"),
        "source_ref": source.get("source_ref"),
        "required_capabilities": source.get("required_capabilities") or [],
        "route_gates": source.get("route_gates") or [],
        "hard_gates": source.get("hard_gates") or [],
        "slot_pressure": source.get("slot_pressure") or {},
        "false_positive_filters": source.get("false_positive_filters") or [],
    }


def candidate_strength(index: dict[str, Any], name: str, item: dict[str, Any]) -> dict[str, Any]:
    tier = item.get("tier") or "unknown"
    rank = item.get("rank")
    return {
        key: value
        for key, value in {
            "tier": tier,
            "total_rank": rank,
        }.items()
        if value is not None
    }


def strength_scalars(strength: dict[str, Any]) -> dict[str, Any]:
    return {
        "strength_tier": strength.get("tier") or "unknown",
        "strength_rank": strength.get("total_rank"),
    }


def retrieval_bucket_hits(index: dict[str, Any], map_name: str, brawler: str) -> dict[str, dict[str, Any]]:
    canonical = canonical_map_name(index, map_name)
    projection = index["map_pool_signature"][canonical].get("candidate_projection") or {}
    hits: dict[str, dict[str, Any]] = {}
    for bucket, items in projection.items():
        for item in items or []:
            if item.get("brawler") == brawler:
                hits[bucket] = strip_tool_internal_keys(item)
    return hits


def candidate_map_fit(index: dict[str, Any], map_name: str, brawler: str) -> dict[str, Any]:
    canonical = canonical_map_name(index, map_name)
    signature = index["map_pool_signature"][canonical]
    item = dict((signature.get("candidate_index") or {}).get(brawler) or {})
    if item:
        item["brawler"] = brawler
    return strip_tool_internal_keys(item)


def runtime_card_fragment(index: dict[str, Any], brawler: str, fit: dict[str, Any]) -> dict[str, Any]:
    card = ((index.get("brawler_runtime_cards") or {}).get(brawler) or {})
    hook_ids = set(fit.get("active_hook_ids") or [])
    build_ids = set(fit.get("required_build_ids") or [])
    risk_ids = set(fit.get("failure_gates") or fit.get("risk_ids") or [])
    map_hooks = {
        key: value
        for key, value in (card.get("map_hooks") or {}).items()
        if not hook_ids or key in hook_ids
    }
    build_switches = {
        key: value
        for key, value in (card.get("build_switches") or {}).items()
        if not build_ids or key in build_ids
    }
    failure_modes = {
        key: value
        for key, value in (card.get("failure_modes") or {}).items()
        if not risk_ids or key in risk_ids
    }
    return {
        "capability_tags": card.get("capability_tags") or [],
        "build_switches": strip_tool_internal_keys(build_switches),
        "map_hooks": strip_tool_internal_keys(map_hooks),
        "objective_contracts": strip_tool_internal_keys(card.get("objective_contracts") or []),
        "failure_modes": strip_tool_internal_keys(failure_modes),
        "slot_notes": strip_tool_internal_keys(card.get("slot_notes") or {}),
    }


def runtime_card_counts(card: dict[str, Any]) -> dict[str, int]:
    return {
        "build_switches": len(card.get("build_switches") or {}),
        "map_hooks": len(card.get("map_hooks") or {}),
        "objective_contracts": len(card.get("objective_contracts") or []),
        "failure_modes": len(card.get("failure_modes") or {}),
        "slot_notes": len(card.get("slot_notes") or {}),
    }


def brawler_matchups(index: dict[str, Any], brawler: str) -> dict[str, list[dict[str, Any]]]:
    return ((index.get("matchup_index") or {}).get("by_brawler") or {}).get(
        brawler,
        {"answers": [], "is_answered_by": []},
    )


def retrieval_log(tool: str, index_path: str, fragments: int, payload: dict[str, Any]) -> dict[str, Any]:
    payload_bytes = len(json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    kb = round(payload_bytes / 1024, 3)
    log = {
        "tool": tool,
        "index_path": str(Path(index_path)),
        "fragments_returned": fragments,
        "payload_bytes": payload_bytes,
        "payload_kb": kb,
    }
    print(f"retrieval_log fragments={fragments} kb={kb}", file=sys.stderr)
    return log


def emit_payload(payload: dict[str, Any], json_mode: bool) -> None:
    if json_mode:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def compact_values(values: Any, limit: int = 4) -> str:
    if not values:
        return "-"
    if isinstance(values, dict):
        seq = list(values.keys())
    elif isinstance(values, list):
        seq = values
    else:
        return str(values)
    shown = [str(value) for value in seq[:limit]]
    if len(seq) > limit:
        shown.append(f"+{len(seq) - limit}")
    return ",".join(shown)


def format_query_summary(query: dict[str, Any]) -> str:
    scope = query.get("scope") or {}
    request = query.get("request") or {}
    retrieval = query.get("retrieval_summary") or {}
    lines = [
        "runtime_fact_query summary",
        f"scope: {scope.get('map', '-')} / {scope.get('mode', '-')}",
        (
            "request: "
            f"buckets={compact_values(request.get('buckets'))} "
            f"include={compact_values(request.get('include_ids'))} "
            f"exclude={compact_values(request.get('exclude_ids'))} "
            f"relation_targets={compact_values(request.get('relation_targets'))} "
            f"effort={request.get('effort', '-')} "
            f"limit={request.get('limit', '-')}"
        ),
        (
            "retrieval: "
            f"entities={retrieval.get('entity_fragments', 0)} "
            f"fragments={retrieval.get('fragments_returned', 0)} "
            f"payload_kb={retrieval.get('payload_kb', 0)}"
        ),
        "candidates:",
    ]
    for item in query.get("fact_window") or []:
        lines.append(
            "- "
            f"{item.get('id', '-')} | "
            f"tier={item.get('strength_tier', 'unknown')} "
            f"rank={item.get('strength_rank', '-')} | "
            f"fit={(item.get('map_fit') or {}).get('fit', '-')} "
            f"floor={(item.get('map_fit') or {}).get('map_floor_fit', '-')} | "
            f"buckets={compact_values(item.get('retrieval_buckets'))} | "
            f"hooks={compact_values(item.get('map_hook_ids'))} | "
            f"caps={compact_values(item.get('matched_capabilities'))} | "
            f"gates={compact_values(item.get('failure_gate_ids'))} | "
            f"relations={item.get('relation_count', 0)}"
        )
    return "\n".join(lines)


def format_hydration_summary(hydration: dict[str, Any]) -> str:
    scope = hydration.get("scope") or {}
    request = hydration.get("request") or {}
    retrieval = hydration.get("retrieval_summary") or {}
    lines = [
        "runtime_fact_hydration summary",
        f"scope: {scope.get('map', '-')} / {scope.get('mode', '-')}",
        (
            "request: "
            f"include={compact_values(request.get('include_ids'))} "
            f"exclude={compact_values(request.get('exclude_ids'))} "
            f"relation_targets={compact_values(request.get('relation_targets'))}"
        ),
        (
            "retrieval: "
            f"entities={retrieval.get('entity_fragments', 0)} "
            f"fragments={retrieval.get('fragments_returned', 0)} "
            f"payload_kb={retrieval.get('payload_kb', 0)}"
        ),
        "entities:",
    ]
    for item in hydration.get("entity_window") or []:
        fit = item.get("candidate_map_fit") or {}
        card_counts = item.get("runtime_card_counts") or {}
        lines.append(
            "- "
            f"{item.get('id', '-')} | "
            f"tier={item.get('strength_tier', 'unknown')} "
            f"rank={item.get('strength_rank', '-')} | "
            f"fit={fit.get('fit', '-')} "
            f"floor={fit.get('map_floor_fit', '-')} | "
            f"buckets={compact_values(item.get('retrieval_bucket_hits'))} | "
            f"hooks={compact_values(fit.get('active_hook_ids'))} | "
            f"builds={card_counts.get('build_switches', 0)} "
            f"risks={card_counts.get('failure_modes', 0)} "
            f"relations={item.get('relation_count', 0)} | "
            f"evidence={item.get('evidence_ref') or '-'}"
        )
    return "\n".join(lines)
