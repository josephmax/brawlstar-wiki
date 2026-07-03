#!/usr/bin/env python3
"""Create or update draft BP profiles for BP-active brawlers."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[3]
ROSTER = ROOT / "raw/sources/roster/brawlers-roster-2026-06-29.md"
FANDOM_DIR = ROOT / "raw/sources/fandom/heroes"
PLP_DIR = ROOT / "raw/sources/pl-prodigy/brawlers"
ENTITY_DIR = ROOT / "wiki/entities/brawlers"
@dataclass(frozen=True)
class RosterRow:
    name: str
    fandom_url: str
    plp_url: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roster", default=str(ROSTER))
    parser.add_argument("--names", nargs="*")
    parser.add_argument("--overwrite-existing-profile", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def parse_roster(path: Path) -> list[RosterRow]:
    rows: list[RosterRow] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or "---" in line or line.startswith("| canonical_name"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3:
            rows.append(RosterRow(cells[0], cells[1], cells[2]))
    return rows


def has_active_bp_sources(row: RosterRow) -> bool:
    return row.fandom_url != "no_page_found" and row.plp_url != "no_page_found"


def source_suffix(name: str) -> str:
    suffix = name.replace(" & ", "-").replace(" ", "-").replace(".", "")
    suffix = re.sub(r"-+", "-", suffix)
    return suffix.strip("-")


def slug_from_url_or_name(url: str, name: str) -> str:
    if url and url != "no_page_found":
        leaf = unquote(urlparse(url).path.rstrip("/").split("/")[-1])
    else:
        leaf = name
    leaf = leaf.replace("_", " ").replace("&", " ").replace(".", " ")
    return re.sub(r"[^A-Za-z0-9]+", "-", leaf).strip("-").lower()


def capture_rank(path: Path) -> tuple[str, int]:
    text = path.read_text(encoding="utf-8", errors="replace")[:500]
    match = re.search(r"^- Capture date: (\d{4}-\d{2}-\d{2})(?:-v(\d+))?", text, re.M)
    if match:
        return match.group(1), int(match.group(2) or 0)
    return "0000-00-00", 0


def latest_direct_raw(directory: Path, slug: str) -> Path:
    candidates = []
    for path in directory.glob(f"{slug}-*.md"):
        if "Direct Raw Capture" in path.read_text(encoding="utf-8", errors="replace")[:160]:
            candidates.append(path)
    if not candidates:
        raise FileNotFoundError(f"no direct raw for {slug}")
    return sorted(candidates, key=capture_rank)[-1]


def extract_meta(raw: str, field: str, default: str = "unknown") -> str:
    match = re.search(rf"^- {re.escape(field)}: (.*)$", raw, re.M)
    return match.group(1).strip() if match else default


def extract_infobox(raw: str) -> dict[str, str]:
    match = re.search(r"## Infobox Fields\n\n(.*?)(?:\n## |\Z)", raw, re.S)
    fields: dict[str, str] = {}
    if not match:
        return fields
    for line in match.group(1).splitlines():
        if line.startswith("- ") and ": " in line:
            key, value = line[2:].split(": ", 1)
            fields[key.strip()] = value.strip()
    return fields


def extract_json_block(raw: str, heading: str) -> Any:
    match = re.search(rf"## {re.escape(heading)}\n\n```json\n(.*?)\n```", raw, re.S)
    return json.loads(match.group(1)) if match else {}


def labels(items: Any) -> list[str]:
    if not isinstance(items, list):
        return []
    out = []
    for item in items:
        if isinstance(item, dict):
            out.append(str(item.get("label") or item.get("name") or item.get("code") or item.get("key")))
        else:
            out.append(str(item))
    return [x for x in out if x and x != "None"]


def names(items: Any) -> list[str]:
    if not isinstance(items, list):
        return []
    out = []
    for item in items:
        if isinstance(item, dict):
            out.append(str(item.get("name") or item.get("label") or item.get("key")))
        else:
            out.append(str(item))
    return [x for x in out if x and x != "None"]


def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_list(values: list[str], indent: int = 8) -> str:
    pad = " " * indent
    if not values:
        return f"{pad}- \"unknown_pending_review\""
    return "\n".join(f"{pad}- {q(value)}" for value in values)


def first_field(fields: dict[str, str], *keys: str) -> str:
    for key in keys:
        value = fields.get(key)
        if value:
            return value
    return "unknown"


def text_has(text: str, *needles: str) -> bool:
    lower = text.lower()
    return any(needle.lower() in lower for needle in needles)


def range_signal(attack_range: str) -> str:
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", attack_range)]
    if not nums:
        return f"unknown_from_fandom_attack_range:{attack_range}"
    max_range = max(nums)
    if max_range >= 9:
        band = "very_long_or_long"
    elif max_range >= 7:
        band = "long_mid"
    elif max_range >= 5:
        band = "mid"
    else:
        band = "short"
    return f"{band}; fandom_attack_range={attack_range}"


def health_signal(health: str, raw_text: str) -> str:
    nums = [int(x) for x in re.findall(r"\d+", health.replace(",", ""))]
    value = max(nums) if nums else 0
    parts = [f"fandom_health={health}"]
    if value and value < 3500:
        parts.append("low_health_failure_check")
    if value and value >= 5000:
        parts.append("high_health_body_presence_candidate")
    if text_has(raw_text, "heal", "shield"):
        parts.append("self_or_team_sustain_text_present")
    return "; ".join(parts)


def capability_vector(fields: dict[str, str], fandom_raw: str, guide: dict[str, Any]) -> dict[str, str]:
    attack_range = first_field(fields, "AttackRange", "AttackRange1", "AttackRange2")
    reload_value = first_field(fields, "Reload", "Reload1", "Reload2")
    brawler_class = first_field(fields, "Class")
    modes = labels(guide.get("modes")) if isinstance(guide, dict) else []
    text = fandom_raw

    wall_break = "present_from_fandom_text" if text_has(text, "destroy obstacles", "destroy walls", "break walls", "destroying obstacles") else "not_observed_in_selected_raw"
    throw_bypass = "present_from_artillery_or_over_obstacles" if brawler_class == "Artillery" or text_has(text, "over obstacles", "lob", "thrower") else "not_observed_in_selected_raw"
    mobility = []
    if text_has(text, "dash", "jump", "teleport", "fly", "leap", "invisible", "movement speed", "speed boost"):
        mobility.append("mobility_or_speed_tool_text_present")
    if text_has(text, "over water", "water", "lakes"):
        mobility.append("water_or_obstacle_interaction_text_present")

    return {
        "effective_range": range_signal(attack_range),
        "projectile_reliability": "needs_review; raw_mentions_slow_delay_spread_or_random" if text_has(text, "slow", "delay", "spread", "random") else "needs_review; no_obvious_slow_or_random_marker_in_selected_raw",
        "burst": "burst_candidate_from_damage_or_super_text" if text_has(text, "burst", "high damage", "massive damage", "explosion") else "unknown_pending_damage_review",
        "sustained_dps": f"reload_signal_from_fandom={reload_value}",
        "objective_damage": f"heist_candidate_from_plp_modes={ 'Heist' in modes }",
        "mobility": "; ".join(mobility) if mobility else "not_observed_in_selected_raw",
        "survivability": health_signal(first_field(fields, "Health", "Health1", "Health2"), text),
        "engage": "engage_candidate_if_mobility_or_cc_text_activates" if mobility or text_has(text, "stun", "pull", "knock") else "unknown_or_low_without_review",
        "disengage": "disengage_candidate_if_mobility_slow_stun_or_knockback_text_activates" if mobility or text_has(text, "slow", "stun", "knockback") else "unknown_or_low_without_review",
        "anti_aggro": "candidate_from_control_or_escape_text" if text_has(text, "knockback", "stun", "slow", "silence", "pull", "dash", "jump") else "not_observed_in_selected_raw",
        "anti_tank": "candidate_from_high_damage_percent_slow_or_continuous_damage_text" if text_has(text, "high-health", "tank", "slow", "continuous", "damage over time", "poison", "burn") else "unknown_pending_matchup_review",
        "wall_break": wall_break,
        "throw_or_wall_bypass": throw_bypass,
        "area_control": "present_from_area_zone_trap_puddle_or_spawnable_text" if text_has(text, "area", "zone", "puddle", "trap", "mine", "turret", "spawn", "control") else "not_observed_in_selected_raw",
        "scouting_or_vision": "present_from_reveal_vision_bush_text" if text_has(text, "reveal", "vision", "bush", "grass") else "not_observed_in_selected_raw",
        "team_support": "present_from_heal_shield_speed_pull_or_buff_text" if text_has(text, "heal", "shield", "speed boost", "buff", "pull", "teammates", "allies") else "not_observed_in_selected_raw",
        "spawnable_or_pet": "present_from_spawn_turret_pet_minion_text" if text_has(text, "spawn", "turret", "minion", "pet", "bear", "porter") else "not_observed_in_selected_raw",
        "crowd_control": "present_from_slow_stun_knockback_pull_silence_text" if text_has(text, "slow", "stun", "knockback", "pull", "silence") else "not_observed_in_selected_raw",
        "terrain_creation": "present_from_wall_or_puddle_obstacle_creation_text" if text_has(text, "creates", "puddle", "wall") else "not_observed_in_selected_raw",
        "terrain_destruction": wall_break,
    }


def map_hooks(cap: dict[str, str], modes: list[str]) -> list[dict[str, str]]:
    hooks: list[dict[str, str]] = []
    if "long" in cap["effective_range"]:
        hooks.append({
            "map_feature_type": "long_sightline",
            "uses_feature_by": "range pressure candidate from Fandom attack range",
            "objective_conversion": "mode/objective payoff must be checked against active map_bp_factors",
            "active_when": "route offers safe line of sight and target access",
            "fails_if": "enemy has low-cost approach, walls block line, or projectile reliability fails",
            "bp_use": "candidate_generation_not_final",
        })
    if cap["wall_break"].startswith("present"):
        hooks.append({
            "map_feature_type": "wall_break_transform",
            "uses_feature_by": "terrain destruction text present in Fandom raw",
            "objective_conversion": "can create or deny lanes only if our comp benefits after transform",
            "active_when": "key wall blocks objective route or protects enemy pocket",
            "fails_if": "opening wall benefits enemy range/engage more than ours",
            "bp_use": "terrain_state_plan_candidate",
        })
    if cap["throw_or_wall_bypass"].startswith("present"):
        hooks.append({
            "map_feature_type": "thrower_pocket",
            "uses_feature_by": "over-wall or artillery signal from Fandom raw",
            "objective_conversion": "can contest protected zones if pocket remains intact",
            "active_when": "walls survive and enemy lacks cheap wall break or dive",
            "fails_if": "terrain is opened or dive path reaches the pocket",
            "bp_use": "map_factor_fit_candidate",
        })
    if "water_or_obstacle" in cap["mobility"]:
        hooks.append({
            "map_feature_type": "water_crossing_or_obstacle_bypass",
            "uses_feature_by": "raw text mentions water/obstacle interaction",
            "objective_conversion": "must be tied to route, target access, or survival anchor",
            "active_when": "bypass creates real objective access",
            "fails_if": "bypass leads to short-range trap or no objective pressure",
            "bp_use": "false_positive_filter_candidate",
        })
    if not hooks:
        hooks.append({
            "map_feature_type": "unknown_pending_review",
            "uses_feature_by": "no specific map hook extracted from selected raw",
            "objective_conversion": "requires manual map_bp_factor review",
            "active_when": "unknown",
            "fails_if": "unknown",
            "bp_use": "do_not_use_as_bp_signal_yet",
        })
    return hooks


def objective_contracts(modes: list[str], cap: dict[str, str]) -> list[dict[str, Any]]:
    if not modes:
        return [{
            "mode": "unknown_pending_plp_or_manual_review",
            "can_fulfill": ["unknown"],
            "cannot_fulfill": ["unknown"],
            "needs_teammate_support": ["unknown"],
            "false_positive": "PLP did not expose a mode candidate in parsed payload",
        }]
    out = []
    for mode in modes:
        duties = [f"{mode}_candidate_from_plp"]
        if mode == "Heist" and "True" in cap["objective_damage"]:
            duties.append("objective_damage_or_lane_pressure_needs_quant_review")
        if mode in {"Bounty", "Knockout"} and "long" in cap["effective_range"]:
            duties.append("survival_range_pressure_candidate")
        if mode in {"Gem Grab", "Hot Zone"} and cap["area_control"].startswith("present"):
            duties.append("area_control_candidate")
        if mode == "Brawl Ball":
            duties.append("ball_mode_contract_needs_push_clear_score_review")
        out.append({
            "mode": mode,
            "can_fulfill": duties,
            "cannot_fulfill": ["not_inferred_from_source; requires map/matchup review"],
            "needs_teammate_support": ["cover failure modes and convert source candidate into map objective"],
            "false_positive": "PLP mode fit is a seed; do not treat as unconditional map fit",
        })
    return out


def failure_modes(cap: dict[str, str]) -> list[dict[str, str]]:
    failures = []
    if "low_health" in cap["survivability"]:
        failures.append({
            "id": "low_health_pressure",
            "active_when": "enemy can force close-range duel or repeated chip",
            "exposed_by": "Fandom health field and selected mechanics",
            "mitigation": "peel, range discipline, terrain plan, or survivability build",
            "bp_use": "false_positive_filter",
        })
    if "slow_delay_spread_or_random" in cap["projectile_reliability"]:
        failures.append({
            "id": "reliability_into_mobility",
            "active_when": "enemy has speed, dash, cover, or unpredictable pathing",
            "exposed_by": "selected Fandom text markers",
            "mitigation": "pick on constrained routes or pair with control",
            "bp_use": "must_avoid_or_needs_support",
        })
    if cap["throw_or_wall_bypass"].startswith("present"):
        failures.append({
            "id": "pocket_removed_or_dived",
            "active_when": "enemy opens terrain or reaches thrower pocket",
            "exposed_by": "artillery/over-wall capability candidate",
            "mitigation": "ban cheap wall break, draft peel, or choose stable pocket map",
            "bp_use": "map_factor_false_positive_check",
        })
    if cap["wall_break"].startswith("present"):
        failures.append({
            "id": "terrain_transform_backfires",
            "active_when": "opened lane improves enemy range or engage more than ours",
            "exposed_by": "terrain destruction candidate",
            "mitigation": "define exact wall and follow-up before pick",
            "bp_use": "terrain_state_plan_check",
        })
    if len(failures) < 2:
        failures.append({
            "id": "source_signal_not_reviewed",
            "active_when": "BP relies on PLP mode/matchup seed without mechanism validation",
            "exposed_by": "third-party guide fields",
            "mitigation": "convert seed into conditional matchup or map hook before bp_ready",
            "bp_use": "do_not_mark_bp_ready",
        })
    return failures


def profile_block(row: RosterRow, fandom_path: Path, plp_path: Path, fandom_raw: str, plp_raw: str) -> str:
    fields = extract_infobox(fandom_raw)
    guide = extract_json_block(plp_raw, "Guide Fields")
    matchups = extract_json_block(plp_raw, "Matchup Fields")
    cap = capability_vector(fields, fandom_raw, guide if isinstance(guide, dict) else {})
    modes = labels(guide.get("modes")) if isinstance(guide, dict) else []
    gears = labels(guide.get("gears")) if isinstance(guide, dict) else []
    gadget = (guide.get("gadget") or {}).get("label") if isinstance(guide, dict) else "unknown"
    star_power = (guide.get("starPower") or {}).get("label") if isinstance(guide, dict) else "unknown"
    suffix = source_suffix(row.name)
    counters_these = names(matchups.get("countersThese")) if isinstance(matchups, dict) else []
    countered_by = names(matchups.get("counteredBy")) if isinstance(matchups, dict) else []

    lines = [
        "## BP 建模草案",
        "",
        "```yaml",
        "bp_brawler_profile:",
        "  profile_status: draft_from_raw_signals",
        "  review_gate: not_bp_ready; requires conditional matchup and map_bp_factor review",
        "  source_quality:",
        f"    fandom: {q('direct_raw_capture_' + extract_meta(fandom_raw, 'Capture date'))}",
        f"    plp: {q('direct_raw_capture_' + extract_meta(plp_raw, 'Capture date'))}",
        "    user_notes: \"none\"",
        "",
        "  capability_vector:",
    ]
    for key, value in cap.items():
        lines.append(f"    {key}: {q(value)}")

    build = f"{gadget} / {star_power} / {', '.join(gears) if gears else 'gears_unknown'}"
    lines.extend([
        "",
        "  build_switches:",
        f"    - build: {q(build)}",
        f"      source: {q('[[sources/PLP-' + suffix + '|PLP-' + suffix + ']]')}",
        "      changes_capabilities:",
        "        - \"third_party_build_candidate; exact capability delta needs mechanism review\"",
        "      enables:",
    ])
    lines.append(yaml_list([f"mode_candidate:{mode}" for mode in modes], 8))
    lines.extend([
        "      mitigates_failure_modes:",
        "        - \"unknown_until_reviewed_against_failure_modes\"",
        "      best_when: \"PLP mode/matchup seed aligns with current map_bp_factors\"",
        "      poor_when: \"build is copied without checking map route, enemy answers, or slot duty\"",
        "      bp_use: \"build_candidate_not_final_recommendation\"",
        "",
        "  map_feature_hooks:",
    ])
    for hook in map_hooks(cap, modes):
        lines.extend([
            f"    - map_feature_type: {q(hook['map_feature_type'])}",
            f"      uses_feature_by: {q(hook['uses_feature_by'])}",
            f"      objective_conversion: {q(hook['objective_conversion'])}",
            f"      active_when: {q(hook['active_when'])}",
            f"      fails_if: {q(hook['fails_if'])}",
            "      example_maps: []",
            f"      bp_use: {q(hook['bp_use'])}",
        ])

    lines.extend(["", "  objective_contracts:"])
    for contract in objective_contracts(modes, cap):
        lines.extend([
            f"    - mode: {q(contract['mode'])}",
            "      can_fulfill:",
            yaml_list(contract["can_fulfill"], 8),
            "      cannot_fulfill:",
            yaml_list(contract["cannot_fulfill"], 8),
            "      needs_teammate_support:",
            yaml_list(contract["needs_teammate_support"], 8),
            f"      false_positive: {q(contract['false_positive'])}",
        ])

    lines.extend(["", "  failure_modes:"])
    for failure in failure_modes(cap):
        lines.extend([
            f"    - id: {q(failure['id'])}",
            f"      active_when: {q(failure['active_when'])}",
            f"      exposed_by: {q(failure['exposed_by'])}",
            f"      mitigation: {q(failure['mitigation'])}",
            f"      bp_use: {q(failure['bp_use'])}",
        ])

    lines.extend(["", "  conditional_matchup_seeds:"])
    if counters_these:
        lines.extend([
            "    - target:",
            yaml_list(counters_these, 8),
            "      direction: \"subject_favored\"",
            f"      source: {q('[[sources/PLP-' + suffix + '|PLP-' + suffix + ']]')}",
            "      mechanism: \"pending; PLP seed must be explained through capability_vector before use\"",
            "      active_when: \"requires map/mode/build validation\"",
            "      fails_when: \"target has support, map disables mechanism, or source seed lacks local validation\"",
            "      bp_use: \"conditional_matchup_seed_only\"",
        ])
    if countered_by:
        lines.extend([
            "    - target:",
            yaml_list(countered_by, 8),
            "      direction: \"target_favored\"",
            f"      source: {q('[[sources/PLP-' + suffix + '|PLP-' + suffix + ']]')}",
            "      mechanism: \"pending; PLP seed must be explained through capability_vector before use\"",
            "      active_when: \"requires map/mode/build validation\"",
            "      fails_when: \"map or comp removes target's access to the punishment mechanism\"",
            "      bp_use: \"must_avoid_or_protection_seed_only\"",
        ])
    if not counters_these and not countered_by:
        lines.extend([
            "    - target: []",
            "      direction: \"unknown\"",
            "      source: \"PLP payload exposed no matchup list\"",
            "      mechanism: \"unknown\"",
            "      active_when: \"unknown\"",
            "      fails_when: \"unknown\"",
            "      bp_use: \"do_not_use_as_counter_signal\"",
        ])

    lines.extend([
        "",
        "  slot_notes:",
        "    slot_1: \"only if map objective contract and low-cost counter checks are already satisfied; PLP seed alone is insufficient\"",
        "    slot_2_3: \"use as response or plan-building pick after checking enemy slot_1 and map duties\"",
        "    slot_4_5: \"can repair role gaps or answer enemy 2-3, but must not leave a clean slot_6 punish\"",
        "    slot_6: \"can punish exposed enemy draft only when conditional matchup seed is activated by map/mode/build\"",
        "```",
    ])
    return "\n".join(lines) + "\n"


def basic_page(row: RosterRow, fandom_raw: str, plp_raw: str) -> str:
    fields = extract_infobox(fandom_raw)
    guide = extract_json_block(plp_raw, "Guide Fields")
    modes = labels(guide.get("modes")) if isinstance(guide, dict) else []
    suffix = source_suffix(row.name)
    rarity = first_field(fields, "Rarity")
    brawler_class = first_field(fields, "Class")
    return f"""# {row.name}

## 基本信息

- 稀有度：{rarity}
- 定位：{brawler_class}
- 类型：待复核；当前仅由 Fandom 定位和 PLP 竞技信号初始化

## 来源摘要

- Fandom：[[sources/Fandom-{suffix}|Fandom 来源摘要: {row.name}]]
- PLP：[[sources/PLP-{suffix}|PLP 来源摘要: {row.name}]]
- PLP 推荐模式候选：{', '.join(modes) if modes else 'none observed'}

## 角色定位总结

本页是从 2026-06-30 抓取件初始化的英雄实体页。当前只保存稳定来源链接和 BP 草案；所有模式适配、对位和顺位判断仍需通过地图因素与条件化对位模型复核。

"""


def strip_existing_bp_block(text: str) -> str:
    marker = "\n## BP 建模草案\n"
    idx = text.find(marker)
    if idx < 0:
        return text.rstrip() + "\n"
    return text[:idx].rstrip() + "\n"


def upsert_profile(row: RosterRow, *, dry_run: bool, overwrite: bool) -> tuple[str, Path]:
    fs = slug_from_url_or_name(row.fandom_url, row.name)
    ps = slug_from_url_or_name(row.plp_url, row.name)
    fandom_path = latest_direct_raw(FANDOM_DIR, fs)
    plp_path = latest_direct_raw(PLP_DIR, ps)
    fandom_raw = fandom_path.read_text(encoding="utf-8", errors="replace")
    plp_raw = plp_path.read_text(encoding="utf-8", errors="replace")
    path = ENTITY_DIR / f"{row.name}.md"

    existed_before = path.exists()
    if existed_before:
        existing = path.read_text(encoding="utf-8", errors="replace")
        if "bp_brawler_profile:" in existing and not overwrite:
            return "skip_existing_profile", path
        base = strip_existing_bp_block(existing) if overwrite else existing.rstrip() + "\n"
    else:
        base = basic_page(row, fandom_raw, plp_raw).rstrip() + "\n"

    content = base.rstrip() + "\n\n" + profile_block(row, fandom_path, plp_path, fandom_raw, plp_raw)
    suffix = source_suffix(row.name)
    if "## 关联页面" not in content:
        content += f"""
## 关联页面

- [[sources/Fandom-{suffix}|Fandom 来源摘要: {row.name}]]
- [[sources/PLP-{suffix}|PLP 来源摘要: {row.name}]]
"""
    if not dry_run:
        path.write_text(content, encoding="utf-8")
    return "updated" if existed_before else "created", path


def main() -> int:
    args = parse_args()
    ENTITY_DIR.mkdir(parents=True, exist_ok=True)
    rows = [row for row in parse_roster(Path(args.roster)) if has_active_bp_sources(row)]
    if args.names:
        wanted = set(args.names)
        rows = [row for row in rows if row.name in wanted]

    counts: dict[str, int] = {}
    for row in rows:
        status, path = upsert_profile(
            row,
            dry_run=args.dry_run,
            overwrite=args.overwrite_existing_profile,
        )
        counts[status] = counts.get(status, 0) + 1
        print(f"{status}\t{row.name}\t{path.relative_to(ROOT)}")
    print("Summary:")
    for key in sorted(counts):
        print(f"- {key}: {counts[key]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
