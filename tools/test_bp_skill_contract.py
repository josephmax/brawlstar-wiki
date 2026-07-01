#!/usr/bin/env python3
"""Contract checks for Brawl Stars BP judge/player skills."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JUDGE_SKILL = ROOT / "skills" / "run-brawl-stars-bp" / "SKILL.md"
JUDGE_SCHEMA = ROOT / "skills" / "run-brawl-stars-bp" / "references" / "match-report-schema.md"
JUDGE_RENDERER = ROOT / "skills" / "run-brawl-stars-bp" / "scripts" / "render_match_report.py"
PLAYER_SKILL = ROOT / "skills" / "brawl-stars-bp-slot-decision" / "SKILL.md"


def read(path: Path) -> str:
    assert path.exists(), f"missing required file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def test_judge_skill_contract() -> None:
    text = read(JUDGE_SKILL)
    schema = read(JUDGE_SCHEMA)

    required_terms = [
        "simultaneous_ban_phase",
        "no_sequential_ban_information",
        "neutral_recorder",
        "deal_cards_only",
        "no_judge_draft_evaluation",
        "style_bias_assigned_at_spawn",
        "do_not_validate_style_compliance",
        "blue_model",
        "red_model",
        "strategy_bias",
        "human_readable_report",
        "randomize_strategy_bias",
        "state_handoff_to_next_turn",
    ]
    for term in required_terms:
        assert term in text or term in schema, term

    for section in [
        "Match Summary",
        "Draft Timeline",
        "Player Final Statements",
        "Execution Metadata",
    ]:
        assert section in schema, section

    forbidden_judge_evaluation_terms = [
        "favored_side:",
        "confidence:",
        "likely_lane_plan",
        "## Final Draft Evaluation",
        "## Draft Evaluation",
        "match_header:",
        "```yaml",
        "## Raw Structured Log",
        "next_player_pressure:",
    ]
    for term in forbidden_judge_evaluation_terms:
        assert term not in schema, term


def test_judge_report_renderer_contract() -> None:
    renderer = read(JUDGE_RENDERER)

    required_terms = [
        "REPORT_TEMPLATE",
        "render_match_report",
        "strategy_bias",
        "Draft Timeline",
        "Player Final Statements",
        "state_handoff_to_next_turn",
    ]
    for term in required_terms:
        assert term in renderer, term

    forbidden_terms = [
        "favored_side",
        "Final Draft Evaluation",
        "```yaml",
        "match_header",
        "Raw Structured Log",
    ]
    for term in forbidden_terms:
        assert term not in renderer, term


def test_player_skill_contract() -> None:
    text = read(PLAYER_SKILL)

    required_terms = [
        "strength_context",
        "meta_pressure",
        "overpowered_or_t0_exception",
        "strategy_bias",
        "conservative",
        "balanced",
        "aggressive",
        "hard_gate_result",
        "candidate_eval",
        "route_based_tank_or_assassin",
        "balanced_threat_probe",
        "proactive_threat_candidate",
        "route_endpoint_payoff",
        "do_not_demote_tank_assassin_for_style_alone",
    ]
    for term in required_terms:
        assert term in text, term

    balanced_section_markers = [
        "`balanced`",
        "must include at least one proactive threat candidate",
        "tank/assassin",
        "unless hard_gate_result.must_avoid",
    ]
    for marker in balanced_section_markers:
        assert marker in text, marker


if __name__ == "__main__":
    test_judge_skill_contract()
    test_judge_report_renderer_contract()
    test_player_skill_contract()
    print("bp skill contract ok")
