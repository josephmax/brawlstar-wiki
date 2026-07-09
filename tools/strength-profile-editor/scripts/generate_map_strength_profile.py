#!/usr/bin/env python3
"""Generate map-scoped strength_profile JSON from a compiled runtime index."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_TIER_ORDER = ["S", "A", "B", "C", "D", "E"]
FIT_ORDER = {"strong": 0, "playable": 1, "conditional": 2, "weak": 3, "reject": 4}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def unwrap_runtime_index(payload: dict[str, Any]) -> dict[str, Any]:
    if isinstance(payload.get("runtime_bp_index"), dict):
        return payload["runtime_bp_index"]
    return payload


def empty_tiers(tier_order: list[str]) -> dict[str, list[str]]:
    return {tier: [] for tier in tier_order}


def has_map_signal(item: dict[str, Any]) -> bool:
    return bool(item.get("active_hook_ids") or item.get("matched_capabilities"))


def adjusted_tier(global_tier: str, item: dict[str, Any]) -> str:
    fit = item.get("fit") or "conditional"
    signal = has_map_signal(item)

    if fit == "strong":
        if global_tier in {"S", "A"}:
            return "S"
        if global_tier in {"B", "C"}:
            return "A"
        return "B"

    if fit == "playable":
        if signal:
            if global_tier in {"S", "A"}:
                return "A"
            if global_tier == "B":
                return "B"
            if global_tier == "C":
                return "C"
            return "D"
        if global_tier in {"S", "A", "B"}:
            return "B"
        if global_tier == "C":
            return "C"
        if global_tier == "D":
            return "D"
        return "E"

    if fit == "conditional":
        if global_tier in {"S", "A"}:
            return "C"
        if global_tier in {"B", "C"}:
            return "D"
        return "E"

    if fit == "weak":
        if global_tier in {"S", "A", "B", "C"}:
            return "D"
        return "E"

    return "E"


def candidate_sort_key(name: str, item: dict[str, Any]) -> tuple[int, int, int]:
    signal_rank = 0 if has_map_signal(item) else 1
    return (
        FIT_ORDER.get(item.get("fit"), 9),
        signal_rank,
        int(item.get("rank") or 9999),
    )


def build_map_tiers(
    tier_order: list[str],
    candidate_index: dict[str, dict[str, Any]],
) -> dict[str, list[str]]:
    tiers = empty_tiers(tier_order)
    for name, item in sorted(
        candidate_index.items(),
        key=lambda entry: candidate_sort_key(entry[0], entry[1]),
    ):
        global_tier = item.get("tier") or "E"
        tier = adjusted_tier(global_tier, item)
        if tier not in tiers:
            tier = "E"
        tiers[tier].append(name)
    return tiers


def build_profile(base: dict[str, Any], runtime_index: dict[str, Any]) -> dict[str, Any]:
    tier_order = list(base.get("tier_order") or DEFAULT_TIER_ORDER)
    maps: dict[str, Any] = {}

    for map_name, signature in sorted((runtime_index.get("map_pool_signature") or {}).items()):
        context = signature.get("map_context") or {}
        mode = context.get("mode") or signature.get("mode") or ""
        key = f"{mode}/{map_name}"
        maps[key] = {
            "scope": "map",
            "mode": mode,
            "map": map_name,
            "tiers": build_map_tiers(tier_order, signature.get("candidate_index") or {}),
        }

    return {
        "schema": "brawlstar.strength_profile.v1",
        "profile_id": "ikaoss11-ranked-map-adapted-preview",
        "patch_id": base.get("patch_id") or (runtime_index.get("manifest") or {}).get("patch_id") or "current",
        "source": {
            "kind": "generated-map-adapted-strength-preview",
            "base_profile_id": base.get("profile_id"),
            "runtime_index_compiler": (runtime_index.get("manifest") or {}).get("compiler_version"),
            "runtime_index_shape": (runtime_index.get("manifest") or {}).get("index_shape"),
            "method": "map_fit_bucket_first_then_global_strength_order",
        },
        "tier_order": tier_order,
        "profiles": {
            "global": base.get("profiles", {}).get("global") or {"scope": "global", "tiers": empty_tiers(tier_order)},
            "modes": {},
            "maps": maps,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository root, used only for relative default paths")
    parser.add_argument("--base-profile", required=True, type=Path, help="Base global strength_profile JSON")
    parser.add_argument("--runtime-index", required=True, type=Path, help="Compiled runtime_bp_index JSON")
    parser.add_argument("--output", required=True, type=Path, help="Output strength_profile JSON path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        base = load_json(args.base_profile)
        runtime_index = unwrap_runtime_index(load_json(args.runtime_index))
        profile = build_profile(base, runtime_index)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(profile, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError, KeyError) as exc:
        print(f"generate_map_strength_profile error: {exc}", file=sys.stderr)
        return 2
    print(
        json.dumps(
            {
                "output": str(args.output),
                "map_profiles": len(profile["profiles"]["maps"]),
                "profile_id": profile["profile_id"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
