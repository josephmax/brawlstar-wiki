#!/usr/bin/env python3
"""Contract checks for Brawl Stars BP judge/player skills."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
JUDGE_SKILL = ROOT / "skills" / "run-brawl-stars-bp" / "SKILL.md"
JUDGE_SCHEMA = ROOT / "skills" / "run-brawl-stars-bp" / "references" / "match-report-schema.md"
JUDGE_RENDERER = ROOT / "skills" / "run-brawl-stars-bp" / "scripts" / "render_match_report.py"
PLAYER_SKILL = ROOT / "skills" / "brawl-stars-bp-slot-decision" / "SKILL.md"
PLAYER_COMPILE_REF = ROOT / "skills" / "brawl-stars-bp-slot-decision" / "references" / "compile-knowledge.md"
PLAYER_DECIDE_REF = ROOT / "skills" / "brawl-stars-bp-slot-decision" / "references" / "runtime-decision-knowledge.md"
MAINTENANCE_SKILL = ROOT / "skills" / "brawl-stars-bp-knowledge-maintenance" / "SKILL.md"
AGENTS = ROOT / "AGENTS.md"
MAINTENANCE_REFS = [
    ROOT / "skills" / "brawl-stars-bp-knowledge-maintenance" / "references" / "repo-layering.md",
    ROOT / "skills" / "brawl-stars-bp-knowledge-maintenance" / "references" / "source-ingest.md",
    ROOT / "skills" / "brawl-stars-bp-knowledge-maintenance" / "references" / "brawler-modeling.md",
    ROOT / "skills" / "brawl-stars-bp-knowledge-maintenance" / "references" / "map-modeling.md",
    ROOT / "skills" / "brawl-stars-bp-knowledge-maintenance" / "references" / "audit-and-validation.md",
    ROOT / "skills" / "brawl-stars-bp-knowledge-maintenance" / "references" / "runtime-boundary.md",
]
MAINTENANCE_AGENT = ROOT / "skills" / "brawl-stars-bp-knowledge-maintenance" / "agents" / "openai.yaml"
MAINTENANCE_SCRIPT_DIR = ROOT / "skills" / "brawl-stars-bp-knowledge-maintenance" / "scripts"
MAINTENANCE_SCRIPTS = [
    MAINTENANCE_SCRIPT_DIR / "capture_brawler_sources.py",
    MAINTENANCE_SCRIPT_DIR / "ingest_brawler_sources.py",
    MAINTENANCE_SCRIPT_DIR / "ingest_brawler_bp_profiles.py",
    MAINTENANCE_SCRIPT_DIR / "audit_bp_profile_quality.py",
    MAINTENANCE_SCRIPT_DIR / "test_bp_skill_contract.py",
]


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
    compile_ref = read(PLAYER_COMPILE_REF)
    decide_ref = read(PLAYER_DECIDE_REF)

    required_terms = [
        "compile",
        "decide",
        "references/compile-knowledge.md",
        "references/runtime-decision-knowledge.md",
        "runtime_bp_index",
        "wiki/entities/maps/",
        "wiki/entities/brawlers/",
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
        "runtime_index_precheck",
        "scripts/runtime_index_precheck.py",
        "runtime_index_key",
        "runtime_index_compile_failed",
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

    for term in [
        "compile_input",
        "strength_profile",
        "map_duties",
        "brawler_cards",
        "map_brawler_edges",
        "draft_edges",
        "default_current_version_unknown",
        "User-supplied strength compile",
    ]:
        assert term in compile_ref, term

    for term in [
        "decide_input",
        "runtime_index_precheck",
        "scripts/runtime_index_precheck.py",
        "slot_policy",
        "hard_gate_result",
        "candidate_eval",
        "balanced_threat_probe",
        "bp_recommendation",
        "runtime_index_compile_failed",
    ]:
        assert term in decide_ref, term

    forbidden_runtime_path = "wiki/syntheses/"
    for artifact in [text, compile_ref, decide_ref]:
        assert forbidden_runtime_path not in artifact, forbidden_runtime_path


def test_maintenance_skill_contract() -> None:
    text = read(MAINTENANCE_SKILL)
    agents = read(AGENTS)
    refs = [read(path) for path in MAINTENANCE_REFS]
    agent = read(MAINTENANCE_AGENT)
    all_text = "\n".join([text, *refs])
    governance_text = "\n".join([agents, all_text])

    for term in [
        "LLM-wiki intake gate",
        "Minimal Request Handling",
        "$markdown-llm-wiki",
        "https://github.com/josephmax/skills/tree/main/skills/markdown-llm-wiki",
        "raw/",
        "raw/sources/fandom/maps",
        "raw/sources/pl-prodigy",
        "raw/sources/roster",
        "raw/sources/supercell",
        "wiki/sources/",
        "wiki/entities/brawlers/",
        "wiki/entities/maps/",
        "wiki/syntheses/",
        "skills/run-brawl-stars-bp/",
        "skills/brawl-stars-bp-slot-decision/",
        "skills/brawl-stars-bp-knowledge-maintenance/",
        "outputs/",
        "runtime_bp_index",
        "Map Fandom ingest",
        "raw/sources/fandom/maps",
        "Brawl Stars Fandom map pages",
        "Fandom and PLP are complementary",
        "PLP does not replace Fandom",
        "Fandom does not replace PLP",
        "canonical knowledge writes",
        "Generated audit reports and runtime indexes go to `outputs/`",
        "scripts/audit_bp_profile_quality.py",
        "scripts/capture_brawler_sources.py",
        "scripts/ingest_brawler_sources.py",
        "scripts/ingest_brawler_bp_profiles.py",
        "scripts/test_bp_skill_contract.py",
    ]:
        assert term in governance_text, term

    for term in [
        "source-ingest.md",
        "brawler-modeling.md",
        "map-modeling.md",
        "audit-and-validation.md",
        "runtime-boundary.md",
    ]:
        assert term in text, term

    for term in [
        "display_name",
        "Brawl Stars BP Knowledge Maintenance",
        "$brawl-stars-bp-knowledge-maintenance",
        "allow_implicit_invocation",
    ]:
        assert term in agent, term

    for script in MAINTENANCE_SCRIPTS:
        assert script.exists(), f"missing maintenance script: {script.relative_to(ROOT)}"

    forbidden_terms = [
        "tools/",
        "`tools`",
    ]
    for artifact in [text, *refs]:
        for term in forbidden_terms:
            assert term not in artifact, term


if __name__ == "__main__":
    test_judge_skill_contract()
    test_judge_report_renderer_contract()
    test_player_skill_contract()
    test_maintenance_skill_contract()
    print("bp skill contract ok")
