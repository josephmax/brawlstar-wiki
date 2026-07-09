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
PLAYER_FACT_QUERY_SCRIPT = ROOT / "skills" / "brawl-stars-bp-slot-decision" / "scripts" / "query_runtime_facts.py"
PLAYER_FACT_HYDRATE_SCRIPT = ROOT / "skills" / "brawl-stars-bp-slot-decision" / "scripts" / "hydrate_runtime_facts.py"
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
    MAINTENANCE_SCRIPT_DIR / "audit_plp_matchup_coverage.py",
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
        "query_runtime_facts.py",
        "hydrate_runtime_facts.py",
        "neutral fact-tool calls",
        "decision_audit_narrative",
        "ban位压力查询前12个热门英雄",
        "召回规模",
        "完整阵容",
        "post_draft_review",
        "final_draft_review",
        "cannot change picks",
        "side_asymmetric_ban_strategy",
        "first_pick_initiative",
        "last_counter_leverage",
        "decision_effort_policy",
        "low=24",
        "high=32",
    ]
    for term in required_terms:
        assert term in text or term in schema, term

    for section in [
        "对局摘要",
        "选择时间线",
        "玩家最终陈述",
        "执行元数据",
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
        "对局摘要",
        "选择时间线",
        "玩家最终陈述",
        "角色职责与配装",
        "report_summary",
        "build_summary",
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
        "tool-consumable runtime index",
        "strength_weight",
        "工具只做事实召回",
        "include-id",
        "exclude-id",
        "relation-target",
        "--bucket",
        "map_pool_signature",
        "candidate_index",
        "brawler_runtime_cards",
        "matchup_index",
        "audit_summary",
        "evidence_refs",
        "mode_contract_fit",
        "matched capabilities",
        "stable map hooks and matched capabilities",
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
        "scripts/query_runtime_facts.py",
        "scripts/hydrate_runtime_facts.py",
        "runtime_index_key",
        "runtime_index_compile_failed",
        "--summary",
        "entity_window",
        "strength_tier",
        "strength_rank",
        "retrieval_audit",
        "payload_kb",
        "fragments_returned",
        "turn_decision_trace",
        "final_draft_review",
        "role_build_plan",
        "decision_effort_policy",
        "low=24",
        "high=32",
        "side_asymmetric_ban_strategy",
        "first_pick_initiative",
        "last_counter_leverage",
        "protect_first_pick",
        "deny_blue_safe_opener",
        "preserve_red6_counter_pool",
        "ban_overlap_risk",
        "opener_safety",
        "last_pick_counterability",
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
        "strength_weight",
        "map_pool_signature",
        "candidate_index",
        "brawler_runtime_cards",
        "matchup_index",
        "audit_summary",
        "evidence_refs",
        "debug traces",
        "default_current_version_unknown",
        "User-supplied strength compile",
        "`mode_contract_hit` is only evidence that the brawler page has a contract for this mode",
        "`early_pick`, `response_pick`, `late_pick`, and `ban_pressure` projections require concrete map fit first",
    ]:
        assert term in compile_ref, term

    for term in [
        "decide_input",
        "runtime_index_precheck",
        "scripts/runtime_index_precheck.py",
        "query_runtime_facts.py",
        "hydrate_runtime_facts.py",
        "Neutral Fact Tools",
        "--summary",
        "entity_window",
        "strength_tier",
        "strength_rank",
        "--bucket",
        "candidate_eval",
        "bp_recommendation",
        "runtime_index_compile_failed",
        "retrieval_audit",
        "payload_kb",
        "fragments_returned",
        "turn_decision_trace",
        "final_draft_review",
        "role_build_plan",
        "decision_effort_policy",
        "low=24",
        "high=32",
        "side_asymmetric_ban_strategy",
        "first_pick_initiative",
        "last_counter_leverage",
        "protect_first_pick",
        "deny_blue_safe_opener",
        "preserve_red6_counter_pool",
        "ban_overlap_risk",
        "opener_safety",
        "last_pick_counterability",
    ]:
        assert term in decide_ref, term

    forbidden_runtime_path = "wiki/syntheses/"
    fact_query_script = read(PLAYER_FACT_QUERY_SCRIPT)
    fact_hydrate_script = read(PLAYER_FACT_HYDRATE_SCRIPT)
    for removed in [
        ROOT / "skills" / "brawl-stars-bp-slot-decision" / "scripts" / "query_runtime_index.py",
        ROOT / "skills" / "brawl-stars-bp-slot-decision" / "scripts" / "hydrate_runtime_evidence.py",
        ROOT / "skills" / "brawl-stars-bp-slot-decision" / "scripts" / "decide_with_runtime_index.py",
    ]:
        assert not removed.exists(), f"removed decision-shaped tool still exists: {removed.relative_to(ROOT)}"
    for artifact in [text, compile_ref, decide_ref, fact_query_script, fact_hydrate_script]:
        assert forbidden_runtime_path not in artifact, forbidden_runtime_path
        assert "strength_prior" not in artifact, "strength_prior"
        for retired_effort in ["max=80", "high=50", "medium=12", "low=5"]:
            assert retired_effort not in artifact, retired_effort


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
        "scripts/audit_plp_matchup_coverage.py",
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
