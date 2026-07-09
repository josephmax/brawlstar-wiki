#!/usr/bin/env python3
"""Compile stable BP facts and strength profile into a runtime_bp_index."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


COMPILER_VERSION = "bp-compile-runtime-v2"
DEFAULT_STRENGTH_PROFILE = (
    "skills/brawl-stars-bp-slot-decision/references/default-strength-profile.json"
)
DEFAULT_TIERS = ["S", "A", "B", "C", "D", "E"]
TIER_VALUE = {"S": 6, "A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "unknown": 0}
META_PRESSURE = {
    "S": "must_answer_pressure",
    "A": "high_priority",
    "B": "playable_meta",
    "C": "contextual",
    "D": "niche_or_counter_only",
    "E": "exception_only",
    "unknown": "unknown",
}
PROOF_THRESHOLD = {
    "S": "map_and_counter_check",
    "A": "standard",
    "B": "standard",
    "C": "elevated",
    "D": "high",
    "E": "exception_only",
    "unknown": "unknown",
}

CAPABILITY_TOKEN_HINTS = {
    "long_range_pressure": ["long_range", "long_sightline", "sniper", "marksman", "open_lane"],
    "projectile_reliability": ["projectile_reliability", "wide_spread", "lane_funnel"],
    "wide_spread": ["wide_spread", "spread", "cone", "fan", "splash"],
    "anti_aggro_poke": ["anti_aggro", "poke", "slow", "knockback", "silence", "stun", "mute"],
    "open_lane_slow": ["open_lane", "slow"],
    "wall_break_for_goal": ["wall_break", "wallbreak", "goal_wallbreak", "break_goal", "goal_barrier"],
    "controlled_wall_break": ["controlled_wall_break", "wall_break", "terrain_transform"],
    "long_range_after_opening": ["long_range_after_opening", "long_range", "wall_break", "wallbreak"],
    "score_window_creation": ["score_window", "scoring_window", "goal_wallbreak", "goal_pressure", "score"],
    "bush_sweep": ["bush_sweep", "bush", "grass", "scout", "vision"],
    "burst_from_short_cover": ["burst", "short_cover", "ambush"],
    "anti_flank_awareness": ["anti_flank", "scout", "vision"],
    "through_wall_or_over_wall_pressure": ["through_wall", "over_wall", "wall_bypass", "thrower"],
    "silence_or_stun_on_ball_carrier": ["silence", "stun", "mute", "ball_carrier"],
    "knockback": ["knockback", "push"],
    "slow_field": ["slow_field", "slow"],
    "lane_block_super": ["lane_block", "choke", "control", "zone"],
    "goal_area_denial": ["goal_area", "goal", "denial", "control"],
}

ROUTE_ONLY_HOOK_TOKENS = {
    "water",
    "jump",
    "dash",
    "assassin",
    "scorer",
    "pure_scorer",
    "short_range",
    "entry",
}

ROUTE_PROOF_TOKENS = {
    "wall_break",
    "wallbreak",
    "long_range",
    "wide_spread",
    "slow",
    "stun",
    "silence",
    "mute",
    "knockback",
    "control",
    "scout",
    "vision",
}

EXPLICIT_MODE_TOKENS = {
    "Heist": ["heist"],
    "Brawl Ball": ["brawl_ball", "brawlball", "goal", "ball"],
    "Hot Zone": ["hot_zone", "hotzone"],
    "Gem Grab": ["gem_grab", "gemgrab", "gem"],
    "Bounty": ["bounty"],
    "Knockout": ["knockout"],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def normalize_key(value: str) -> str:
    return re.sub(r"[^0-9a-z]+", "", str(value).casefold())


def rel(path: Path, repo: Path) -> str:
    try:
        return str(path.relative_to(repo))
    except ValueError:
        return str(path)


def sha256_json(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def sha256_texts(texts: Iterable[str]) -> str:
    digest = hashlib.sha256()
    for text in texts:
        digest.update(text.encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def entity_brawler_names(repo: Path) -> list[str]:
    return sorted(path.stem for path in (repo / "wiki/entities/brawlers").glob("*.md"))


def find_named_page(repo: Path, subdir: str, name: str) -> Path | None:
    directory = repo / subdir
    if not name or not directory.exists():
        return None
    exact = directory / f"{name}.md"
    if exact.exists():
        return exact
    wanted = normalize_key(name)
    for path in directory.glob("*.md"):
        if normalize_key(path.stem) == wanted:
            return path
    return None


def extract_first_code_block(text: str, language: str) -> str:
    pattern = rf"```{re.escape(language)}\s*(.*?)```"
    match = re.search(pattern, text, flags=re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_profile_payload(path: Path) -> dict[str, Any]:
    text = read_text(path)
    if path.suffix.lower() == ".md":
        json_block = extract_first_code_block(text, "json")
        if json_block:
            return json.loads(json_block)
    return json.loads(text)


def load_alias_index(repo: Path, valid_names: set[str]) -> dict[str, str]:
    alias_page = repo / "wiki/concepts/英雄名称归一化.md"
    block = extract_first_code_block(read_text(alias_page), "yaml")
    aliases: dict[str, str] = {}
    current: str | None = None

    for name in valid_names:
        aliases[name] = name
        aliases[normalize_key(name)] = name

    for line in block.splitlines():
        canonical = re.match(r'\s{2}"?([^":]+)"?:\s*$', line)
        if canonical:
            current = canonical.group(1)
            if current in valid_names:
                aliases[current] = current
                aliases[normalize_key(current)] = current
            continue

        alias = re.match(r'\s{4}-\s*"?(.*?)"?\s*$', line)
        if alias and current in valid_names:
            value = alias.group(1)
            aliases[value] = current
            aliases[normalize_key(value)] = current

    return aliases


def normalize_brawler_name(name: str, aliases: dict[str, str]) -> str | None:
    raw = str(name).strip()
    return aliases.get(raw) or aliases.get(normalize_key(raw))


def empty_tiers(tier_order: list[str]) -> dict[str, list[str]]:
    return {tier: [] for tier in tier_order}


def normalize_tier_map(
    tiers: dict[str, Any],
    tier_order: list[str],
    aliases: dict[str, str],
    missing_inputs: list[str],
    label: str,
) -> dict[str, list[str]]:
    result = empty_tiers(tier_order)
    seen: set[str] = set()
    for tier in tier_order:
        for raw_name in tiers.get(tier, []) if isinstance(tiers, dict) else []:
            name = normalize_brawler_name(raw_name, aliases)
            if not name:
                missing_inputs.append(f"{label}: unknown brawler {raw_name}")
                continue
            if name in seen:
                missing_inputs.append(f"{label}: duplicate brawler {name}")
                continue
            result[tier].append(name)
            seen.add(name)
    return result


def has_tier_entries(record: dict[str, Any] | None) -> bool:
    return any(record.get("tiers", {}).get(tier) for tier in record.get("tier_order", DEFAULT_TIERS)) if record else False


def normalize_strength_profile(
    payload: dict[str, Any],
    aliases: dict[str, str],
    missing_inputs: list[str],
) -> dict[str, Any]:
    tier_order = list(payload.get("tier_order") or DEFAULT_TIERS)
    profile = {
        "schema": payload.get("schema") or "brawlstar.strength_profile.v1",
        "profile_id": payload.get("profile_id") or "runtime-supplied-strength-profile",
        "patch_id": payload.get("patch_id") or "current",
        "source": payload.get("source") or {},
        "tier_order": tier_order,
        "profiles": {"global": {"scope": "global", "tiers": empty_tiers(tier_order)}, "modes": {}, "maps": {}},
    }

    source_profiles = payload.get("profiles") or {}
    global_tiers = source_profiles.get("global", {}).get("tiers") or payload.get("global_tiers") or {}
    profile["profiles"]["global"]["tiers"] = normalize_tier_map(
        global_tiers, tier_order, aliases, missing_inputs, "global"
    )

    for mode, record in (source_profiles.get("modes") or {}).items():
        mode_name = record.get("mode") or mode
        profile["profiles"]["modes"][mode_name] = {
            "scope": "mode",
            "mode": mode_name,
            "tiers": normalize_tier_map(record.get("tiers") or {}, tier_order, aliases, missing_inputs, f"mode {mode_name}"),
        }

    for key, record in (source_profiles.get("maps") or {}).items():
        mode = record.get("mode") or key.split("/")[0]
        map_name = record.get("map") or "/".join(key.split("/")[1:])
        scope_key = f"{mode}/{map_name}"
        profile["profiles"]["maps"][scope_key] = {
            "scope": "map",
            "mode": mode,
            "map": map_name,
            "tiers": normalize_tier_map(record.get("tiers") or {}, tier_order, aliases, missing_inputs, f"map {scope_key}"),
        }

    for entry in payload.get("entries") or []:
        name = normalize_brawler_name(entry.get("brawler"), aliases)
        tier = entry.get("tier")
        if not name or tier not in tier_order:
            missing_inputs.append(f"entry: invalid brawler/tier {entry}")
            continue
        if entry.get("map") and entry.get("mode"):
            key = f"{entry['mode']}/{entry['map']}"
            record = profile["profiles"]["maps"].setdefault(
                key,
                {"scope": "map", "mode": entry["mode"], "map": entry["map"], "tiers": empty_tiers(tier_order)},
            )
        elif entry.get("mode"):
            record = profile["profiles"]["modes"].setdefault(
                entry["mode"],
                {"scope": "mode", "mode": entry["mode"], "tiers": empty_tiers(tier_order)},
            )
        else:
            record = profile["profiles"]["global"]
        if name not in [item for values in record["tiers"].values() for item in values]:
            record["tiers"][tier].append(name)

    return profile


def scope_record(profile: dict[str, Any], mode: str, map_name: str) -> tuple[str, str, dict[str, Any] | None]:
    map_key = f"{mode}/{map_name}" if mode and map_name else ""
    map_record = profile["profiles"]["maps"].get(map_key)
    if map_record and any(map_record["tiers"].values()):
        return "map", map_key, map_record
    mode_record = profile["profiles"]["modes"].get(mode)
    if mode_record and any(mode_record["tiers"].values()):
        return "mode", mode, mode_record
    global_record = profile["profiles"]["global"]
    if global_record and any(global_record["tiers"].values()):
        return "global", "global", global_record
    return "unknown", "unknown", None


def strength_lookup(profile: dict[str, Any], mode: str, map_name: str) -> dict[str, dict[str, Any]]:
    effective_scope, scope_key, record = scope_record(profile, mode, map_name)
    if not record:
        return {}

    tier_order = profile["tier_order"]
    flat = [(tier, name) for tier in tier_order for name in record["tiers"].get(tier, [])]
    total = len(flat)
    tier_sizes = {tier: len(record["tiers"].get(tier, [])) for tier in tier_order}
    lookup: dict[str, dict[str, Any]] = {}

    total_rank = 0
    tier_ranks = {tier: 0 for tier in tier_order}
    for tier, name in flat:
        total_rank += 1
        tier_ranks[tier] += 1
        tier_size = tier_sizes[tier]
        within_score = (tier_size - tier_ranks[tier] + 1) / tier_size if tier_size else 0
        ordered_score = (total - total_rank + 1) / total if total else 0
        lookup[name] = {
            "tier": tier,
            "tier_value": TIER_VALUE.get(tier, 0),
            "tier_rank": tier_ranks[tier],
            "tier_size": tier_size,
            "total_rank": total_rank,
            "ranked_count": total,
            "within_tier_score": round(within_score, 4),
            "ordered_score": round(ordered_score, 4),
            "effective_scope": effective_scope,
            "scope_key": scope_key,
            "source": profile["profile_id"],
            "confidence": "external_current_meta",
        }
    return lookup


def unknown_strength(profile_id: str) -> dict[str, Any]:
    return {
        "tier": "unknown",
        "tier_value": 0,
        "tier_rank": None,
        "tier_size": 0,
        "total_rank": None,
        "ranked_count": 0,
        "within_tier_score": 0,
        "ordered_score": 0,
        "effective_scope": "unknown",
        "scope_key": "unknown",
        "source": profile_id,
        "confidence": "unknown",
    }


def extract_yaml_block(text: str, root_key: str) -> str:
    block = extract_first_code_block(text, "yaml")
    marker = f"{root_key}:"
    index = block.find(marker)
    return block[index:] if index >= 0 else block


def extract_named_section(block: str, name: str) -> str:
    pattern = rf"\n  {re.escape(name)}:\n(.*?)(?=\n  [A-Za-z0-9_]+:|\Z)"
    match = re.search(pattern, "\n" + block, flags=re.DOTALL)
    return match.group(1).rstrip() if match else ""


def parse_key_value_lines(block: str, indent: int = 4) -> dict[str, str]:
    result: dict[str, str] = {}
    pattern = re.compile(rf"^\s{{{indent}}}([A-Za-z0-9_]+):\s*(.*?)\s*$")
    for line in block.splitlines():
        match = pattern.match(line)
        if match and match.group(2):
            result[match.group(1)] = match.group(2).strip().strip('"')
    return result


def split_list_entries(block: str) -> list[str]:
    entries: list[list[str]] = []
    current: list[str] = []
    for line in block.splitlines():
        if re.match(r"\s{4}-\s+", line):
            if current:
                entries.append(current)
            current = [line]
        elif current:
            current.append(line)
    if current:
        entries.append(current)
    return ["\n".join(entry) for entry in entries]


def parse_entry(entry: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    lines = entry.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"\s*(?:-\s*)?([A-Za-z0-9_]+):\s*(.*?)\s*$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip().strip('"')
        if value == "":
            values = []
            for child in lines[index + 1 :]:
                child_match = re.match(r"\s{8}-\s*(.*?)\s*$", child)
                if child_match:
                    values.append(child_match.group(1).strip().strip('"'))
                elif re.match(r"\s{4,6}[A-Za-z0-9_]+:", child):
                    break
            data[key] = values
        else:
            data[key] = value
    return data


def compact_entry(entry: dict[str, Any], keys: list[str]) -> dict[str, Any]:
    return {key: entry[key] for key in keys if entry.get(key) not in (None, "", [])}


def as_list(value: Any) -> list[str]:
    if value in (None, "", []):
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    return [str(value)]


def slug(value: str, fallback: str) -> str:
    cleaned = re.sub(r"[^0-9a-z]+", "_", str(value).casefold()).strip("_")
    return cleaned or fallback


def with_entry_id(entry: dict[str, Any], preferred_keys: list[str], fallback_prefix: str, index: int) -> dict[str, Any]:
    result = dict(entry)
    if result.get("id"):
        result["id"] = str(result["id"])
        return result
    for key in preferred_keys:
        if result.get(key):
            result["id"] = slug(str(result[key]), f"{fallback_prefix}_{index}")
            return result
    result["id"] = f"{fallback_prefix}_{index}"
    return result


def index_by_id(entries: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(entry["id"]): entry for entry in entries if entry.get("id")}


def parse_plain_list(block: str) -> list[str]:
    values = []
    for line in block.splitlines():
        match = re.match(r"\s{4}-\s*(.*?)\s*$", line)
        if match and match.group(1):
            values.append(match.group(1).strip().strip('"'))
    return values


def target_values(value: Any) -> list[str]:
    targets: list[str] = []
    for item in as_list(value):
        item = item.strip()
        if item.startswith("[") and item.endswith("]"):
            item = item[1:-1]
        parts = re.split(r"\s+or\s+|_or_|[,/]", item)
        for part in parts:
            cleaned = part.strip().strip("[]").strip().strip('"').strip("'")
            if cleaned:
                targets.append(cleaned.replace("_", " ") if cleaned == "Mr_P" else cleaned)
    return targets


def listish_values(value: Any) -> list[str]:
    if value in (None, "", []):
        return []
    if isinstance(value, list):
        return [str(item).strip().strip("\"'") for item in value if str(item).strip()]
    raw = str(value).strip()
    if raw.startswith("[") and raw.endswith("]"):
        return [part.strip().strip("\"'") for part in raw[1:-1].split(",") if part.strip()]
    return [raw.strip().strip("\"'")]


def wiki_display_text(value: str) -> str:
    text = str(value).strip()
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        if "|" in inner:
            return inner.rsplit("|", 1)[-1].strip()
        return inner.rsplit("/", 1)[-1].strip()
    return text


def hook_example_map_names(hook: dict[str, Any]) -> list[str]:
    return [wiki_display_text(value) for value in listish_values(hook.get("example_maps")) if wiki_display_text(value)]


def hook_text_for_matching(hook: dict[str, Any]) -> str:
    return normalize_key(
        " ".join(
            str(hook.get(key) or "")
            for key in (
                "id",
                "map_feature_type",
                "objective_conversion",
                "bp_use",
            )
        )
    )


def hook_has_route_only_risk(hook_text: str) -> bool:
    return any(token in hook_text for token in ROUTE_ONLY_HOOK_TOKENS) and not any(
        token in hook_text for token in ROUTE_PROOF_TOKENS
    )


def hook_mentions_other_mode(hook_text: str, current_mode: str) -> bool:
    for mode, tokens in EXPLICIT_MODE_TOKENS.items():
        if mode == current_mode:
            continue
        if any(normalize_key(token) in hook_text for token in tokens):
            return True
    return False


def hook_matches_required_capability(hook: dict[str, Any], map_duty: dict[str, Any]) -> bool:
    text = hook_text_for_matching(hook)
    if hook_mentions_other_mode(text, str(map_duty.get("mode") or "")):
        return False
    if hook_has_route_only_risk(text):
        return False
    for capability in map_duty.get("required_capabilities") or []:
        cap_key = normalize_key(capability)
        hints = [cap_key, *CAPABILITY_TOKEN_HINTS.get(capability, [])]
        if any(normalize_key(hint) and normalize_key(hint) in text for hint in hints):
            return True
    return False


def bracket_list_values(line: str) -> list[str]:
    match = re.search(r"\[(.*?)\]", line)
    if not match:
        return []
    return [part.strip().strip("\"'") for part in match.group(1).split(",") if part.strip()]


def extract_mode_from_map(path: Path) -> str:
    text = read_text(path)
    for pattern in (r"^\s*mode:\s*`?([^`\n]+?)`?\s*$", r"^- 模式：`?([^`\n]+?)`?\s*$"):
        match = re.search(pattern, text, flags=re.MULTILINE)
        if match:
            return match.group(1).strip()
    return ""


MODE_HARD_GATES = {
    "Heist": [
        {
            "id": "heist_objective_access",
            "requirement": "provide safe pressure, safe defense, counter-race value, or a named way to enable those jobs",
        }
    ],
    "Gem Grab": [
        {
            "id": "gem_grab_mine_or_carrier_plan",
            "requirement": "provide mine control, carrier safety, carrier punish, or a named support plan for those jobs",
        }
    ],
    "Brawl Ball": [
        {
            "id": "brawl_ball_score_or_reset_plan",
            "requirement": "provide scoring conversion, goal/wall handling, defensive reset, or support for those jobs",
        }
    ],
    "Hot Zone": [
        {
            "id": "hot_zone_time_conversion",
            "requirement": "provide zone body, zone clear, entry denial, sustain, or support that converts into zone time",
        }
    ],
    "Bounty": [
        {
            "id": "bounty_low_risk_kill_or_denial",
            "requirement": "provide low-risk pressure, vision, kill confirmation, or a denial plan that avoids feeding stars",
        }
    ],
    "Knockout": [
        {
            "id": "knockout_pick_or_survival_plan",
            "requirement": "provide first-kill pressure, collapse, anti-engage, late-circle control, or a survival plan",
        }
    ],
}


def mode_hard_gates(mode: str) -> list[dict[str, str]]:
    return MODE_HARD_GATES.get(mode, [])


def slot_pressure_for_map(mode: str, route_gates: list[dict[str, str]], required: list[str]) -> dict[str, list[str]]:
    gate_ids = [gate["id"] for gate in route_gates[:3] if gate.get("id")]
    required_slice = required[:4]
    return {
        "early_pick": [f"cover core {mode} duty"] + [f"prove capability:{cap}" for cap in required_slice[:2]],
        "mid_pick": [f"answer_or_enable_route:{gate_id}" for gate_id in gate_ids],
        "late_pick": [f"punish_unanswered_route:{gate_id}" for gate_id in gate_ids[-2:]],
        "ban": [f"remove_high_strength_candidate_when_no_answer:{cap}" for cap in required_slice[:2]],
    }


def compile_map_duty(path: Path, repo: Path) -> dict[str, Any]:
    text = read_text(path)
    block = extract_yaml_block(text, "map_profile")
    mode = extract_mode_from_map(path)
    required: list[str] = []
    false_positive: list[dict[str, str]] = []
    route_gates: list[dict[str, str]] = []

    for line in block.splitlines():
        if "rewards_capabilities:" in line:
            for capability in bracket_list_values(line):
                if capability not in required:
                    required.append(capability)

    tactical = extract_named_section(block, "tactical_features")
    for entry in split_list_entries(tactical):
        parsed = parse_entry(entry)
        false_positive_capabilities = []
        for line in entry.splitlines():
            if "false_positive_capabilities:" in line:
                false_positive_capabilities.extend(bracket_list_values(line))
        for capability in false_positive_capabilities:
            false_positive.append(
                {
                    "id": f"{parsed.get('id') or 'route'}:{capability}",
                    "route_gate": str(parsed.get("id") or ""),
                    "capability": capability,
                    "reason": str(parsed.get("bp_use") or parsed.get("condition") or ""),
                }
            )
        route_gates.append(
            {
                "id": str(parsed.get("id") or ""),
                "type": str(parsed.get("type") or ""),
                "location": str(parsed.get("location") or ""),
                "condition": str(parsed.get("condition") or ""),
                "payoff": str(parsed.get("payoff") or ""),
                "bp_use": str(parsed.get("bp_use") or ""),
            }
        )

    map_rules = []
    for index, entry in enumerate(split_list_entries(extract_named_section(block, "map_rules")), start=1):
        parsed = parse_entry(entry)
        if parsed:
            rule = with_entry_id(parsed, ["if", "then"], "map_rule", index)
            map_rules.append(rule)
            false_positive.append(
                {
                    "id": rule["id"],
                    "if": str(rule.get("if") or ""),
                    "then": str(rule.get("then") or ""),
                    "because": str(rule.get("because") or ""),
                    "bp_use": str(rule.get("bp_use") or ""),
                }
            )

    for index, value in enumerate(parse_plain_list(extract_named_section(block, "false_positive")), start=1):
        false_positive.append({"id": f"false_positive_note_{index}", "note": value})

    stable_goal = ""
    match = re.search(r"stable_goal:\s*(.*?)\s*$", block, flags=re.MULTILINE)
    if match:
        stable_goal = match.group(1).strip()

    route_gates = [gate for gate in route_gates if gate["id"]]
    return {
        "map": path.stem,
        "mode": mode,
        "source_ref": rel(path, repo),
        "objective_contracts": [stable_goal] if stable_goal else [],
        "required_capabilities": required,
        "route_gates": route_gates,
        "hard_gates": mode_hard_gates(mode),
        "terrain_state_plan": [],
        "false_positive_filters": false_positive,
        "map_rules": map_rules,
        "slot_pressure": slot_pressure_for_map(mode, route_gates, required),
    }


def compile_brawler_card(path: Path, repo: Path, strength: dict[str, Any]) -> dict[str, Any]:
    text = read_text(path)
    block = extract_yaml_block(text, "bp_brawler_profile")
    capabilities = parse_key_value_lines(extract_named_section(block, "capability_vector"))
    slot_notes = parse_key_value_lines(extract_named_section(block, "slot_notes"))
    builds = [
        with_entry_id(
            compact_entry(
                parse_entry(entry),
                [
                    "build",
                    "source",
                    "changes_capabilities",
                    "enables",
                    "mitigates_failure_modes",
                    "best_when",
                    "poor_when",
                    "bp_use",
                ],
            ),
            ["build", "bp_use"],
            "build",
            index,
        )
        for index, entry in enumerate(split_list_entries(extract_named_section(block, "build_switches")), start=1)
    ]
    map_hooks = [
        with_entry_id(
            compact_entry(
                parse_entry(entry),
                [
                    "id",
                    "map_feature_type",
                    "uses_feature_by",
                    "route_or_position",
                    "objective_conversion",
                    "active_when",
                    "fails_if",
                    "example_maps",
                    "bp_use",
                ],
            ),
            ["map_feature_type", "bp_use"],
            "map_hook",
            index,
        )
        for index, entry in enumerate(split_list_entries(extract_named_section(block, "map_feature_hooks")), start=1)
    ]
    objectives = [
        compact_entry(
            parse_entry(entry),
            ["mode", "can_fulfill", "cannot_fulfill", "needs_teammate_support", "false_positive"],
        )
        for entry in split_list_entries(extract_named_section(block, "objective_contracts"))
    ]
    failures = [
        with_entry_id(
            compact_entry(parse_entry(entry), ["id", "active_when", "exposed_by", "mitigation", "bp_use"]),
            ["bp_use", "active_when"],
            "failure",
            index,
        )
        for index, entry in enumerate(split_list_entries(extract_named_section(block, "failure_modes")), start=1)
    ]
    matchup_block = extract_named_section(block, "conditional_matchup_seeds")
    if not matchup_block:
        matchup_block = extract_named_section(block, "conditional_matchups")
    matchups = [
        {
            **compact_entry(
                parse_entry(entry),
                ["target", "direction", "source", "mechanism", "active_when", "fails_when", "bp_use"],
            ),
            "target": target_values(parse_entry(entry).get("target")),
        }
        for entry in split_list_entries(matchup_block)
    ]
    tier = strength["tier"]

    return {
        "brawler": path.stem,
        "source_ref": rel(path, repo),
        "capability_tags": sorted(capabilities),
        "builds": builds,
        "objective_contracts": objectives,
        "map_hooks": map_hooks,
        "failure_modes": failures,
        "slot_notes": slot_notes,
        "strength_visibility": strength,
        "strength_context": {
            "source": strength["source"],
            "meta_pressure": META_PRESSURE.get(tier, "unknown"),
            "overpowered_or_t0_exception": tier == "S",
            "counter_availability": "draft_state_dependent",
            "balance_volatility": "current_meta_external_source",
        },
        "proof_threshold": PROOF_THRESHOLD.get(tier, "unknown"),
        "conditional_matchups": matchups,
    }


def mode_objective_hit(card: dict[str, Any], mode: str) -> bool:
    normalized_mode = normalize_key(mode)
    for contract in card.get("objective_contracts") or []:
        if normalized_mode and normalized_mode in normalize_key(str(contract.get("mode") or "")):
            return True
    return False


def hook_applies_to_map(hook: dict[str, Any], map_duty: dict[str, Any]) -> bool:
    map_name = map_duty["map"]
    example_maps = hook_example_map_names(hook)
    if example_maps:
        if normalize_key(map_name) in {normalize_key(name) for name in example_maps}:
            return True
        return hook_matches_required_capability(hook, map_duty)

    hook_text = json.dumps(hook, ensure_ascii=False)
    if normalize_key(map_name) and normalize_key(map_name) in normalize_key(hook_text):
        return True

    return hook_matches_required_capability(hook, map_duty)


def compile_map_brawler_edge(map_duty: dict[str, Any], card: dict[str, Any]) -> dict[str, Any]:
    active_hooks = []
    for hook in card.get("map_hooks") or []:
        if hook_applies_to_map(hook, map_duty):
            active_hooks.append(compact_entry(hook, ["id", "map_feature_type", "bp_use"]))
    matched_capabilities = matched_capabilities_for_map(map_duty, card)
    fit = "strong" if active_hooks or matched_capabilities else "weak"

    return {
        "map": map_duty["map"],
        "brawler": card["brawler"],
        "fit": fit,
        "active_routes": active_hooks[:4],
        "objective_conversion": matched_capabilities,
        "terrain_dependency": [],
        "required_build": [build.get("build") for build in card.get("builds", [])[:2] if build.get("build")],
        "failure_if": [failure.get("id") for failure in card.get("failure_modes", [])[:4] if failure.get("id")],
        "false_positive_if": [failure.get("bp_use") for failure in card.get("failure_modes", [])[:4] if failure.get("bp_use")],
    }


def compile_draft_edges(card: dict[str, Any]) -> dict[str, Any]:
    answers = []
    answered_by = []
    for matchup in card.get("conditional_matchups") or []:
        edge = {
            "target": matchup.get("target"),
            "bp_use": matchup.get("bp_use"),
        }
        if matchup.get("direction") == "target_favored":
            answered_by.append(edge)
        else:
            answers.append(edge)
    return {"brawler": card["brawler"], "answers": answers, "is_answered_by": answered_by}


def thin_strength_entry(strength: dict[str, Any], proof_threshold: str) -> dict[str, Any]:
    return {
        "tier": strength["tier"],
        "tier_value": strength["tier_value"],
        "tier_rank": strength["tier_rank"],
        "tier_size": strength["tier_size"],
        "total_rank": strength["total_rank"],
        "score": strength["ordered_score"],
        "within_tier_score": strength["within_tier_score"],
        "source": strength["source"],
        "proof_threshold": proof_threshold,
    }


def active_hooks_for_map(card: dict[str, Any], map_duty: dict[str, Any]) -> list[dict[str, Any]]:
    active_hooks = []
    for hook in card.get("map_hooks") or []:
        if hook_applies_to_map(hook, map_duty):
            active_hooks.append(hook)
    return active_hooks


def map_floor_fit(has_map_signal: bool, has_mode_contract: bool) -> str:
    if has_map_signal:
        return "strong"
    return "weak"


def mode_contract_fit(has_mode_contract: bool) -> str:
    return "evidence_only" if has_mode_contract else "none"


def combined_candidate_fit(map_floor: str, mode_fit: str) -> str:
    if map_floor == "strong":
        return "strong"
    if map_floor == "conditional":
        return "conditional"
    return "weak"


def matched_capabilities_for_map(map_duty: dict[str, Any], card: dict[str, Any]) -> list[str]:
    required = set(map_duty.get("required_capabilities") or [])
    matched: set[str] = set()
    normalized_mode = normalize_key(map_duty["mode"])
    for contract in card.get("objective_contracts") or []:
        if normalized_mode and normalized_mode not in normalize_key(str(contract.get("mode") or "")):
            continue
        for capability in as_list(contract.get("can_fulfill")):
            if capability in required:
                matched.add(capability)
    for hook in active_hooks_for_map(card, map_duty):
        feature_type = hook.get("map_feature_type")
        if feature_type and feature_type in required:
            matched.add(feature_type)
    return sorted(matched)


def slot_eligibility(map_floor: str, mode_fit: str) -> dict[str, bool]:
    return {
        "early_pick": map_floor == "strong",
        "response_pick": map_floor in {"strong", "conditional"},
        "late_pick": map_floor in {"strong", "conditional"},
    }


def conditional_lift(card: dict[str, Any], map_floor: str, mode_fit: str) -> list[str]:
    answer_targets = sorted(
        {
            target
            for matchup in card.get("conditional_matchups") or []
            if matchup.get("direction") != "target_favored"
            for target in target_values(matchup.get("target"))
        }
    )
    if not answer_targets:
        return []
    return ["enemy_targets_answered_by_candidate"]


def recall_channels(map_floor: str, card: dict[str, Any]) -> list[str]:
    channels: list[str] = []
    if map_floor == "strong":
        channels.append("map_core")
    elif map_floor == "conditional":
        channels.append("map_secondary")
    if any(matchup.get("direction") != "target_favored" for matchup in card.get("conditional_matchups") or []):
        channels.append("counter_response")
    return channels


def candidate_item(
    map_duty: dict[str, Any],
    card: dict[str, Any],
    strength: dict[str, Any],
) -> dict[str, Any]:
    hooks = active_hooks_for_map(card, map_duty)
    mode_hit = mode_objective_hit(card, map_duty["mode"])
    matched_capabilities = matched_capabilities_for_map(map_duty, card)
    floor_fit = map_floor_fit(bool(hooks or matched_capabilities), mode_hit)
    mode_fit = mode_contract_fit(mode_hit)
    return {
        "brawler": card["brawler"],
        "fit": combined_candidate_fit(floor_fit, mode_fit),
        "map_floor_fit": floor_fit,
        "mode_contract_fit": mode_fit,
        "tier": strength["tier"],
        "rank": strength["total_rank"],
        "score": strength["ordered_score"],
        "proof_threshold": PROOF_THRESHOLD.get(strength["tier"], "unknown"),
        "active_hook_ids": [hook.get("id") for hook in hooks if hook.get("id")][:3],
        "active_map_feature_types": sorted(
            {hook.get("map_feature_type") for hook in hooks if hook.get("map_feature_type")}
        ),
        "matched_capabilities": matched_capabilities,
        "mode_contract_hit": mode_hit,
        "recall_channels": recall_channels(floor_fit, card),
        "slot_eligibility": slot_eligibility(floor_fit, mode_fit),
        "conditional_lift": conditional_lift(card, floor_fit, mode_fit),
        "failure_gates": [failure.get("id") for failure in card.get("failure_modes", [])[:4] if failure.get("id")],
        "required_build_ids": [build.get("id") for build in card.get("builds", [])[:3] if build.get("id")],
        "projection_buckets": [],
    }


def sorted_candidate_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    fit_order = {"strong": 0, "playable": 1, "conditional": 2, "weak": 3, "reject": 4}
    return sorted(items, key=lambda item: (fit_order.get(item["fit"], 9), item["rank"] or 9999))


def build_candidate_items(
    map_duty: dict[str, Any],
    cards: list[dict[str, Any]],
    strengths: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    return sorted_candidate_items(
        [
            candidate_item(map_duty, card, strengths.get(card["brawler"], unknown_strength("unknown")))
            for card in cards
        ]
    )


def candidate_projection_from_items(items: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    projection: dict[str, list[dict[str, Any]]] = {
        "early_pick": [],
        "response_pick": [],
        "late_pick": [],
        "ban_pressure": [],
        "avoid_without_proof": [],
    }

    for item in items:
        eligibility = item.get("slot_eligibility") or {}
        if item["fit"] == "strong" and eligibility.get("early_pick", True):
            projection["early_pick"].append(compact_candidate_item(item))

    for item in items:
        eligibility = item.get("slot_eligibility") or {}
        if (
            item["fit"] in {"strong", "playable", "conditional"}
            and eligibility.get("response_pick", True)
        ):
            projection["response_pick"].append(compact_candidate_item(item))

    for item in items:
        eligibility = item.get("slot_eligibility") or {}
        if item["fit"] in {"strong", "playable", "conditional"} and eligibility.get("late_pick", True):
            projection["late_pick"].append(compact_candidate_item(item))

    for item in items:
        has_map_signal = bool(item.get("active_hook_ids") or item.get("matched_capabilities"))
        if item["fit"] == "strong" and has_map_signal:
            projection["ban_pressure"].append(compact_candidate_item(item))

    for item in items:
        if item["tier"] in {"D", "E"} and item["fit"] == "weak" and len(projection["avoid_without_proof"]) < 6:
            projection["avoid_without_proof"].append(compact_candidate_item(item))

    return projection


def compact_candidate_item(item: dict[str, Any]) -> dict[str, Any]:
    return {
        key: item[key]
        for key in (
            "brawler",
            "fit",
            "tier",
            "rank",
            "active_hook_ids",
            "matched_capabilities",
            "mode_contract_hit",
            "recall_channels",
        )
        if item.get(key) not in (None, "", [])
    }


def build_candidate_index(items: list[dict[str, Any]], projection: dict[str, list[dict[str, Any]]]) -> dict[str, dict[str, Any]]:
    buckets_by_brawler: dict[str, list[str]] = defaultdict(list)
    for bucket, bucket_items in projection.items():
        for item in bucket_items:
            if item.get("brawler"):
                buckets_by_brawler[item["brawler"]].append(bucket)
    result = {}
    for item in items:
        entry = {
            "fit": item["fit"],
            "map_floor_fit": item.get("map_floor_fit"),
            "mode_contract_fit": item.get("mode_contract_fit"),
            "tier": item.get("tier"),
            "rank": item.get("rank"),
            "projection_buckets": buckets_by_brawler.get(item["brawler"], []),
            "active_hook_ids": item.get("active_hook_ids") or [],
            "matched_capabilities": item.get("matched_capabilities") or [],
            "mode_contract_hit": item.get("mode_contract_hit") or False,
            "recall_channels": item.get("recall_channels") or [],
            "slot_eligibility": item.get("slot_eligibility") or {},
            "conditional_lift": item.get("conditional_lift") or [],
            "failure_gates": item.get("failure_gates") or [],
            "required_build_ids": item.get("required_build_ids") or [],
        }
        result[item["brawler"]] = {
            key: value
            for key, value in entry.items()
            if value not in (None, "", [], False)
        }
    return result


def map_context(map_duty: dict[str, Any]) -> dict[str, Any]:
    route_gates = [
        {key: gate[key] for key in ("id", "type", "location", "condition", "payoff", "bp_use") if gate.get(key)}
        for gate in map_duty["route_gates"]
    ]
    return {
        "map": map_duty["map"],
        "mode": map_duty["mode"],
        "source_ref": map_duty["source_ref"],
        "objective_contracts": map_duty["objective_contracts"],
        "required_capabilities": map_duty["required_capabilities"],
        "route_gates": route_gates,
        "hard_gates": map_duty["hard_gates"],
        "slot_pressure": map_duty["slot_pressure"],
        "terrain_state_plan": map_duty["terrain_state_plan"],
        "false_positive_filters": map_duty["false_positive_filters"],
    }


def thin_map_signature(
    map_duty: dict[str, Any],
    cards: list[dict[str, Any]],
    strength_profile: dict[str, Any],
) -> dict[str, Any]:
    strengths = strength_lookup(strength_profile, map_duty["mode"], map_duty["map"])
    items = build_candidate_items(map_duty, cards, strengths)
    projection = candidate_projection_from_items(items)
    return {
        "map_context": map_context(map_duty),
        "candidate_projection": projection,
        "candidate_index": build_candidate_index(items, projection),
    }


def runtime_brawler_card(card: dict[str, Any]) -> dict[str, Any]:
    build_switches = {
        build["id"]: compact_entry(build, ["id", "build", "enables", "mitigates_failure_modes", "bp_use"])
        for build in card.get("builds") or []
        if build.get("id")
    }
    map_hooks = {
        hook["id"]: compact_entry(
            hook,
            ["id", "map_feature_type", "objective_conversion", "active_when", "fails_if", "bp_use"],
        )
        for hook in card.get("map_hooks") or []
        if hook.get("id")
    }
    failure_modes = {
        failure["id"]: compact_entry(failure, ["id", "active_when", "mitigation", "bp_use"])
        for failure in card.get("failure_modes") or []
        if failure.get("id")
    }
    objective_contracts = [
        compact_entry(contract, ["mode", "can_fulfill", "needs_teammate_support", "false_positive"])
        for contract in card.get("objective_contracts") or []
    ]
    return {
        "capability_tags": card.get("capability_tags") or [],
        "build_switches": build_switches,
        "map_hooks": map_hooks,
        "objective_contracts": objective_contracts,
        "failure_modes": failure_modes,
        "slot_notes": card.get("slot_notes") or {},
    }


def matchup_edge(subject: str, target: str, matchup: dict[str, Any]) -> dict[str, Any]:
    return {
        "target": target,
        "mechanism": matchup.get("mechanism"),
        "active_when": matchup.get("active_when"),
        "fails_when": matchup.get("fails_when"),
        "bp_use": matchup.get("bp_use"),
    }


def build_matchup_index(cards: list[dict[str, Any]]) -> dict[str, Any]:
    by_brawler: dict[str, dict[str, list[dict[str, Any]]]] = {}
    for card in cards:
        name = card["brawler"]
        bucket = by_brawler.setdefault(name, {"answers": [], "is_answered_by": []})
        for matchup in card.get("conditional_matchups") or []:
            direction = matchup.get("direction")
            for target in target_values(matchup.get("target")):
                edge = matchup_edge(name, target, matchup)
                if direction == "target_favored":
                    bucket["is_answered_by"].append(edge)
                else:
                    bucket["answers"].append(edge)
    return {"by_brawler": by_brawler}


def audit_summary(
    manifest: dict[str, Any],
    map_pool_signature: dict[str, Any],
    brawler_runtime_cards: dict[str, Any],
    matchup_index: dict[str, Any],
) -> dict[str, Any]:
    candidate_entries = {
        map_name: len(signature.get("candidate_index") or {})
        for map_name, signature in map_pool_signature.items()
    }
    cards_with_hooks = sum(1 for card in brawler_runtime_cards.values() if card.get("map_hooks"))
    by_brawler_matchups = matchup_index.get("by_brawler") or {}
    cards_with_matchups = sum(
        1
        for matchups in by_brawler_matchups.values()
        if matchups.get("answers") or matchups.get("is_answered_by")
    )
    return {
        "map_count": len(map_pool_signature),
        "brawler_count": len(brawler_runtime_cards),
        "candidate_index_entries": candidate_entries,
        "cards_with_map_hooks": cards_with_hooks,
        "cards_with_matchups": cards_with_matchups,
        "matchup_subject_count": len(by_brawler_matchups),
        "missing_inputs": manifest.get("missing_inputs") or [],
    }


def build_runtime_index(args: argparse.Namespace) -> dict[str, Any]:
    repo = Path(args.repo).resolve()
    missing_inputs: list[str] = []
    valid_names = set(entity_brawler_names(repo))
    aliases = load_alias_index(repo, valid_names)

    strength_path = Path(args.strength_profile)
    if not strength_path.is_absolute():
        strength_path = repo / strength_path
    strength_payload = extract_profile_payload(strength_path)
    strength_profile = normalize_strength_profile(strength_payload, aliases, missing_inputs)

    map_paths = []
    for map_name in args.map:
        path = find_named_page(repo, "wiki/entities/maps", map_name)
        if path:
            map_paths.append(path)
        else:
            missing_inputs.append(f"missing map page {map_name}")
    if not map_paths:
        map_paths = sorted((repo / "wiki/entities/maps").glob("*.md"))

    map_duties = [compile_map_duty(path, repo) for path in map_paths]

    requested_brawlers = args.available_brawler or sorted(valid_names)
    brawler_cards = []
    source_texts = [json.dumps(strength_profile, ensure_ascii=False, sort_keys=True)]
    for raw_name in requested_brawlers:
        name = normalize_brawler_name(raw_name, aliases)
        if not name:
            missing_inputs.append(f"available_brawlers: unknown brawler {raw_name}")
            continue
        path = find_named_page(repo, "wiki/entities/brawlers", name)
        if not path:
            missing_inputs.append(f"missing brawler page {name}")
            continue
        source_texts.append(read_text(path))
        card = compile_brawler_card(path, repo, unknown_strength(strength_profile["profile_id"]))
        brawler_cards.append(card)
    for path in map_paths:
        source_texts.append(read_text(path))

    strength_hash = sha256_json(strength_profile)
    map_pool_signature = {
        map_duty["map"]: thin_map_signature(map_duty, brawler_cards, strength_profile)
        for map_duty in map_duties
    }
    brawler_runtime_cards = {
        card["brawler"]: runtime_brawler_card(card)
        for card in brawler_cards
    }
    matchup_index = build_matchup_index(brawler_cards)
    evidence_refs = {
        "strength_profile": rel(strength_path, repo),
        "maps": {duty["map"]: duty["source_ref"] for duty in map_duties},
        "brawlers": {card["brawler"]: card["source_ref"] for card in brawler_cards},
    }
    manifest = {
        "patch_id": args.patch_id or strength_profile.get("patch_id") or "current",
        "map_pool_id": args.map_pool_id or ",".join(duty["map"] for duty in map_duties) or "all_maps",
        "strength_profile_id": strength_profile["profile_id"],
        "strength_profile_hash": strength_hash,
        "source_hash": sha256_texts(source_texts),
        "compiler_version": COMPILER_VERSION,
        "compiled_at": datetime.now(timezone.utc).isoformat(),
        "missing_inputs": missing_inputs,
        "available_brawlers": [card["brawler"] for card in brawler_cards],
        "index_shape": "runtime-v2",
    }

    if args.debug_output:
        debug_payload = {
            "runtime_bp_debug_trace": {
                "manifest": manifest,
                "map_duties": map_duties,
                "brawler_cards": brawler_cards,
                "map_brawler_edges": [
                    compile_map_brawler_edge(map_duty, card)
                    for map_duty in map_duties
                    for card in brawler_cards
                ],
                "draft_edges": [compile_draft_edges(card) for card in brawler_cards],
            }
        }
        debug_path = Path(args.debug_output)
        if not debug_path.is_absolute():
            debug_path = repo / debug_path
        debug_path.parent.mkdir(parents=True, exist_ok=True)
        debug_path.write_text(json.dumps(debug_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    runtime_index = {
        "manifest": manifest,
        "map_pool_signature": map_pool_signature,
        "brawler_runtime_cards": brawler_runtime_cards,
        "matchup_index": matchup_index,
        "evidence_refs": evidence_refs,
    }
    runtime_index["audit_summary"] = audit_summary(
        manifest,
        map_pool_signature,
        brawler_runtime_cards,
        matchup_index,
    )
    runtime_index["audit_summary"]["runtime_payload_bytes_estimate"] = len(
        json.dumps(runtime_index, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    )

    return {"runtime_bp_index": runtime_index}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository root")
    parser.add_argument("--map", action="append", default=[], help="Map name to compile; repeatable")
    parser.add_argument("--mode", default="", help="Mode used when no map page supplies one")
    parser.add_argument("--available-brawler", action="append", default=[], help="Available brawler; repeatable")
    parser.add_argument("--strength-profile", default=DEFAULT_STRENGTH_PROFILE, help="JSON profile or markdown page with JSON block")
    parser.add_argument("--patch-id", default="", help="Override manifest patch_id")
    parser.add_argument("--map-pool-id", default="", help="Override manifest map_pool_id")
    parser.add_argument("--output", default="", help="Write compiled runtime_bp_index JSON to this path")
    parser.add_argument("--debug-output", default="", help="Optionally write thick debug trace JSON to this path")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print runtime index JSON instead of compact output")
    parser.add_argument("--json", action="store_true", help="Emit JSON to stdout")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = build_runtime_index(args)
    output_json = (
        json.dumps(payload, ensure_ascii=False, indent=2)
        if args.pretty
        else json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    )
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_json + "\n", encoding="utf-8")
    if args.json or not args.output:
        print(output_json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
