import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[1]
COMPILE_SCRIPT = SKILL_DIR / "scripts" / "compile_runtime_index.py"
FACT_QUERY_SCRIPT = SKILL_DIR / "scripts" / "query_runtime_facts.py"
FACT_HYDRATE_SCRIPT = SKILL_DIR / "scripts" / "hydrate_runtime_facts.py"
REMOVED_TOOL_NAMES = [
    "query_runtime_index.py",
    "hydrate_runtime_evidence.py",
    "decide_with_runtime_index.py",
]
DEFAULT_PROFILE = SKILL_DIR / "references" / "default-strength-profile.json"
FORBIDDEN_TOOL_KEYS = {
    "enemy",
    "our_pick",
    "enemy_pick",
    "bans",
    "decision_type",
    "strategy_bias",
    "strength_weight",
    "decision_seed",
    "judgment_brief",
    "current_team_plan",
    "candidate_shortlist",
    "ability_gate",
    "capability_gate",
    "adjudication",
    "ban_purpose",
    "ban_purposes",
    "must_ban",
    "top_decisions",
    "answers_enemy_picks",
    "is_answered_by_enemy_picks",
    "answers_enemy",
    "proof_threshold",
    "bp_use",
}


def compile_safe_zone_index(tmp: str) -> Path:
    index_path = Path(tmp) / "safe-zone-index.json"
    subprocess.run(
        [
            sys.executable,
            str(COMPILE_SCRIPT),
            "--repo",
            str(REPO_ROOT),
            "--map",
            "Safe Zone",
            "--strength-profile",
            str(DEFAULT_PROFILE),
            "--output",
            str(index_path),
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    return index_path


class RuntimeIndexToolsTest(unittest.TestCase):
    def assert_no_forbidden_keys(self, payload):
        if isinstance(payload, dict):
            for key, value in payload.items():
                self.assertNotIn(key, FORBIDDEN_TOOL_KEYS)
                self.assert_no_forbidden_keys(value)
        elif isinstance(payload, list):
            for value in payload:
                self.assert_no_forbidden_keys(value)

    def test_removed_decision_shaped_tools_are_not_available(self):
        for name in REMOVED_TOOL_NAMES:
            self.assertFalse((SKILL_DIR / "scripts" / name).exists(), name)

    def test_fact_query_uses_neutral_include_exclude_and_relation_targets(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = compile_safe_zone_index(tmp)

            result = subprocess.run(
                [
                    sys.executable,
                    str(FACT_QUERY_SCRIPT),
                    "--index",
                    str(index_path),
                    "--map",
                    "Safe Zone",
                    "--bucket",
                    "early_pick",
                    "--include-id",
                    "Brock",
                    "--exclude-id",
                    "Meg",
                    "--relation-target",
                    "8-Bit",
                    "--limit",
                    "6",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_query"]

        self.assertEqual("Safe Zone", payload["scope"]["map"])
        self.assertEqual("Heist", payload["scope"]["mode"])
        self.assertEqual(["Brock"], payload["request"]["include_ids"])
        self.assertEqual(["Meg"], payload["request"]["exclude_ids"])
        self.assertEqual(["8-Bit"], payload["request"]["relation_targets"])
        self.assertEqual(["early_pick"], payload["request"]["buckets"])

        names = [item["id"] for item in payload["fact_window"]]
        self.assertIn("Brock", names)
        self.assertNotIn("Meg", names)
        self.assertLessEqual(len(names), 6)
        brock = next(item for item in payload["fact_window"] if item["id"] == "Brock")
        self.assertIn("strength_tier", brock)
        self.assertIn("strength_rank", brock)
        self.assertIsInstance(brock["relation_count"], int)
        self.assertEqual(len(payload["fact_window"]) + 1, payload["retrieval_summary"]["fragments_returned"])
        self.assertIn("retrieval_log fragments=", result.stderr)
        self.assert_no_forbidden_keys(payload)

        relation_rows = [
            relation
            for item in payload["fact_window"]
            for relation in item.get("conditional_relations") or []
        ]
        self.assertTrue(any(row["target"] == "8-Bit" for row in relation_rows))
        self.assertTrue(all(row["relation_family"] == "conditional_matchup" for row in relation_rows))

    def test_fact_query_effort_selects_recall_budget(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = compile_safe_zone_index(tmp)

            result = subprocess.run(
                [
                    sys.executable,
                    str(FACT_QUERY_SCRIPT),
                    "--index",
                    str(index_path),
                    "--map",
                    "Safe Zone",
                    "--bucket",
                    "early_pick",
                    "--effort",
                    "high",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_query"]

        self.assertEqual("high", payload["request"]["effort"])
        self.assertEqual(32, payload["request"]["limit"])
        self.assertLessEqual(len(payload["fact_window"]), 32)
        self.assertEqual(len(payload["fact_window"]) + 1, payload["retrieval_summary"]["fragments_returned"])

    def test_fact_query_explicit_limit_overrides_effort_budget(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = compile_safe_zone_index(tmp)

            result = subprocess.run(
                [
                    sys.executable,
                    str(FACT_QUERY_SCRIPT),
                    "--index",
                    str(index_path),
                    "--map",
                    "Safe Zone",
                    "--bucket",
                    "early_pick",
                    "--effort",
                    "low",
                    "--limit",
                    "7",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_query"]

        self.assertEqual("low", payload["request"]["effort"])
        self.assertEqual(7, payload["request"]["limit"])
        self.assertLessEqual(len(payload["fact_window"]), 7)

    def test_fact_hydration_returns_entity_facts_without_decision_language(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = compile_safe_zone_index(tmp)

            result = subprocess.run(
                [
                    sys.executable,
                    str(FACT_HYDRATE_SCRIPT),
                    "--index",
                    str(index_path),
                    "--map",
                    "Safe Zone",
                    "--include-id",
                    "Brock",
                    "--include-id",
                    "Meg",
                    "--relation-target",
                    "8-Bit",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_hydration"]

        self.assertEqual(["Brock", "Meg"], list(payload["entities"].keys()))
        self.assertEqual(["Brock", "Meg"], [item["id"] for item in payload["entity_window"]])
        brock = payload["entities"]["Brock"]
        self.assertIn("runtime_card", brock)
        self.assertIn("map_strength", brock)
        self.assertIn("strength_tier", brock)
        self.assertIn("strength_rank", brock)
        self.assertIn("retrieval_bucket_hits", brock)
        self.assertIn("conditional_relations", brock)
        self.assert_no_forbidden_keys(payload)

    def test_fact_query_summary_mode_avoids_ad_hoc_json_parsing(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = compile_safe_zone_index(tmp)

            result = subprocess.run(
                [
                    sys.executable,
                    str(FACT_QUERY_SCRIPT),
                    "--index",
                    str(index_path),
                    "--map",
                    "Safe Zone",
                    "--bucket",
                    "early_pick",
                    "--include-id",
                    "Brock",
                    "--limit",
                    "3",
                    "--summary",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

        self.assertIn("runtime_fact_query summary", result.stdout)
        self.assertIn("candidates:", result.stdout)
        self.assertIn("Brock", result.stdout)
        self.assertNotIn("Traceback", result.stdout)
        self.assertFalse(result.stdout.lstrip().startswith("{"))

    def test_fact_hydration_summary_mode_avoids_entity_dict_indexing(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = compile_safe_zone_index(tmp)

            result = subprocess.run(
                [
                    sys.executable,
                    str(FACT_HYDRATE_SCRIPT),
                    "--index",
                    str(index_path),
                    "--map",
                    "Safe Zone",
                    "--include-id",
                    "Brock",
                    "--summary",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

        self.assertIn("runtime_fact_hydration summary", result.stdout)
        self.assertIn("entities:", result.stdout)
        self.assertIn("Brock", result.stdout)
        self.assertNotIn("Traceback", result.stdout)
        self.assertFalse(result.stdout.lstrip().startswith("{"))

    def test_fact_query_rejects_business_semantic_arguments(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = compile_safe_zone_index(tmp)

            result = subprocess.run(
                [
                    sys.executable,
                    str(FACT_QUERY_SCRIPT),
                    "--index",
                    str(index_path),
                    "--map",
                    "Safe Zone",
                    "--enemy-pick",
                    "8-Bit",
                    "--json",
                ],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

        self.assertNotEqual(0, result.returncode)
        self.assertIn("unrecognized arguments", result.stderr)


if __name__ == "__main__":
    unittest.main()
