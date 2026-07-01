#!/usr/bin/env python3
"""Render human-readable Brawl Stars BP match reports."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from string import Template
from typing import Any


BIAS_OPTIONS = ("conservative", "balanced", "aggressive", "high_variance")

REPORT_TEMPLATE = Template(
    """# match-$map

## Match Summary

- Map and mode: $map ($mode)
- Strategy bias: Blue `$blue_strategy_bias`; Red `$red_strategy_bias`
- Ban format: simultaneous bans; duplicate bans preserved
- Pick order: Blue slot 1 -> Red slots 2-3 -> Blue slots 4-5 -> Red slot 6
- Final draft: Blue $blue_comp; Red $red_comp
- Duplicated bans: $duplicated_bans
- Draft sequence: $sequence_summary

## Ban Phase

### Blue Bans

$blue_bans

### Red Bans

$red_bans

- Unavailable pool after bans: $unavailable_pool

## Draft Timeline

$draft_timeline

## Player Final Statements

### Blue Player

- Comp: $blue_comp
- Submitted win condition: $blue_win_condition
- Submitted key risks: $blue_key_risks
- Submitted uncertainties: $blue_uncertainties

### Red Player

- Comp: $red_comp
- Submitted win condition: $red_win_condition
- Submitted key risks: $red_key_risks
- Submitted uncertainties: $red_uncertainties

- Judge note: no judge draft evaluation was added.

## Stable Knowledge Refs

$stable_refs$execution_metadata
"""
)


def assign_strategy_bias(rng: random.Random | None = None) -> str:
    """Choose one player style before spawning a player agent."""
    chooser = rng or random
    return chooser.choice(BIAS_OPTIONS)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def inline_list(value: Any, empty: str = "none") -> str:
    items = [str(item) for item in as_list(value) if str(item)]
    return ", ".join(f"`{item}`" for item in items) if items else empty


def text(value: Any, empty: str = "not submitted") -> str:
    if value is None:
        return empty
    if isinstance(value, list):
        return "; ".join(str(item) for item in value) or empty
    return str(value) if str(value) else empty


def render_bans(bans: list[dict[str, Any]]) -> str:
    if not bans:
        return "- none submitted"
    lines: list[str] = []
    for ban in bans:
        brawler = text(ban.get("brawler"), "unknown")
        parts = [
            text(ban.get("intent"), ""),
            text(ban.get("removes_enemy_route"), ""),
            text(ban.get("protects_own_plan"), ""),
            text(ban.get("risk_if_open"), ""),
        ]
        reason = "; ".join(part for part in parts if part)
        lines.append(f"- `{brawler}`: {reason or 'reason not submitted'}")
    return "\n".join(lines)


def render_rejected(options: list[dict[str, Any]]) -> str:
    if not options:
        return "none submitted"
    rendered = []
    for option in options:
        name = text(option.get("brawler_or_pair"), "unknown")
        reason = text(option.get("reason_rejected"), "reason not submitted")
        rendered.append(f"`{name}` ({reason})")
    return "; ".join(rendered)


def render_turn(turn: dict[str, Any]) -> str:
    decision = turn.get("decision", {})
    state = turn.get("known_state", {})
    title = text(turn.get("title") or turn.get("turn_id"), "Turn")
    picks = inline_list(decision.get("picks"))
    heading = f"### {title} - {picks}"
    handoff_label = "Final visible state" if turn.get("is_final_turn") else "State handoff to next turn"
    handoff = text(
        turn.get("state_handoff_to_next_turn")
        or turn.get("final_visible_state")
        or turn.get("state_handoff"),
    )
    return "\n".join(
        [
            heading,
            "",
            f"- Visible state: own picks {inline_list(state.get('own_picks'))}; enemy picks {inline_list(state.get('enemy_picks'))}; unavailable {inline_list(state.get('unavailable_pool'))}.",
            f"- Player submitted reason: {text(decision.get('construct_direction'))}",
            f"- Covers: enemy picks {inline_list(decision.get('answers_enemy_picks'))}; map/objective duties {inline_list(decision.get('answers_map_factors'))}.",
            f"- Required build(s): {text(decision.get('required_builds'))}",
            f"- Rejected options: {render_rejected(as_list(decision.get('rejected_options')))}",
            f"- {handoff_label}: {handoff}",
        ]
    )


def render_execution_metadata(metadata: dict[str, Any] | None) -> str:
    if not metadata:
        return ""
    has_real_signal = any(
        metadata.get(key)
        for key in (
            "token_usage_captured",
            "timestamps_captured",
            "failure_reason",
            "local_continuation_reason",
        )
    )
    if not has_real_signal:
        return ""
    lines = ["", "## Execution Metadata", ""]
    if metadata.get("player_execution"):
        lines.append(f"- Player execution: {metadata['player_execution']}")
    if metadata.get("token_usage_captured"):
        lines.append(f"- Captured token usage: {metadata['token_usage_captured']}")
    elif metadata.get("token_usage_note"):
        lines.append(f"- Token usage: {metadata['token_usage_note']}")
    if metadata.get("timestamps_captured"):
        lines.append(f"- Captured timestamps: {metadata['timestamps_captured']}")
    if metadata.get("failure_reason"):
        lines.append(f"- Failure reason: {metadata['failure_reason']}")
    if metadata.get("local_continuation_reason"):
        lines.append(f"- Local continuation: {metadata['local_continuation_reason']}")
    return "\n" + "\n".join(lines)


def render_match_report(data: dict[str, Any]) -> str:
    blue = data.get("blue_player", {})
    red = data.get("red_player", {})
    ban_phase = data.get("ban_phase", {})
    substitutions = {
        "map": text(data.get("map"), "Unknown Map"),
        "mode": text(data.get("mode"), "Unknown Mode"),
        "blue_strategy_bias": text(data.get("blue_strategy_bias"), "not assigned"),
        "red_strategy_bias": text(data.get("red_strategy_bias"), "not assigned"),
        "blue_comp": inline_list(blue.get("comp")),
        "red_comp": inline_list(red.get("comp")),
        "duplicated_bans": inline_list(ban_phase.get("duplicated_bans")),
        "sequence_summary": text(data.get("sequence_summary"), "sequence summary not submitted"),
        "blue_bans": render_bans(as_list(ban_phase.get("blue_bans"))),
        "red_bans": render_bans(as_list(ban_phase.get("red_bans"))),
        "unavailable_pool": inline_list(ban_phase.get("unavailable_pool")),
        "draft_timeline": "\n\n".join(render_turn(turn) for turn in as_list(data.get("turns"))),
        "blue_win_condition": text(blue.get("win_condition")),
        "blue_key_risks": text(blue.get("key_risks")),
        "blue_uncertainties": text(blue.get("uncertainties")),
        "red_win_condition": text(red.get("win_condition")),
        "red_key_risks": text(red.get("key_risks")),
        "red_uncertainties": text(red.get("uncertainties")),
        "stable_refs": "\n".join(f"- {ref}" for ref in as_list(data.get("stable_refs"))) or "- none submitted",
        "execution_metadata": render_execution_metadata(data.get("execution_metadata")),
    }
    return REPORT_TEMPLATE.substitute(substitutions).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a human-readable Brawl Stars BP match report.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    report = render_match_report(data)
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
