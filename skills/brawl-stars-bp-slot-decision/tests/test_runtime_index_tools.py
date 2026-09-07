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
        # 事实窗口不再携带任何 strength/tier 概念
        self.assertNotIn("strength_tier", brock)
        self.assertNotIn("strength_rank", brock)
        self.assertNotIn("strength", brock)
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
        self.assertNotIn("map_strength", brock)
        self.assertNotIn("strength_tier", brock)
        self.assertNotIn("strength_rank", brock)
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

    # --- Capability-window retrieval (layer 1) ---

    def test_fact_query_capability_filter_keeps_only_matching_brawlers(self):
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
                    "--capability",
                    "throw_or_wall_bypass",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_query"]

        self.assertEqual(["throworwallbypass"], payload["request"]["capabilities"])
        self.assertTrue(payload["fact_window"])
        for item in payload["fact_window"]:
            tags = set(item.get("runtime_card", {}).get("capability_tags") or [])
            self.assertIn("throw_or_wall_bypass", tags)
        self.assert_no_forbidden_keys(payload)

    def test_fact_query_capability_window_is_not_truncated_by_effort_budget(self):
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
                    "5",
                    "--capability",
                    "crowd_control",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_query"]

        # Capability hits are never capped: every crowd-control brawler is
        # visible even when the requested window is small.
        self.assertGreater(len(payload["fact_window"]), 5)
        for item in payload["fact_window"]:
            tags = set(item.get("runtime_card", {}).get("capability_tags") or [])
            self.assertIn("crowd_control", tags)
        self.assert_no_forbidden_keys(payload)

    def test_fact_query_include_id_bypasses_capability_filter(self):
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
                    "5",
                    "--capability",
                    "crowd_control",
                    "--include-id",
                    "Brock",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_query"]

        names = [item["id"] for item in payload["fact_window"]]
        self.assertIn("Brock", names)  # explicit include survives the filter
        self.assert_no_forbidden_keys(payload)

    def test_fact_query_ordering_is_evidence_based_not_alphabetical(self):
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

        names = [item["id"] for item in payload["fact_window"]]
        sorted_alphabetically = sorted(names)
        # The window must not be a bare alphabetical prefix (the old
        # candidate_sort_key starved late-alphabet brawlers such as Willow).
        self.assertNotEqual(names, sorted_alphabetically[: len(names)])

    def test_fact_query_without_capability_keeps_legacy_bucket_behavior(self):
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

        self.assertEqual([], payload["request"]["capabilities"])
        self.assertLessEqual(len(payload["fact_window"]), 32)
        self.assert_no_forbidden_keys(payload)

    # --- Capability dimension cleaning, archetypes, floors, census ---

    def test_capability_level_order_copies_are_identical(self):
        # Import both modules and compare their ordinal scales so threshold
        # semantics can never drift between compile and query sides.
        import importlib.util
        import sys as _sys
        from pathlib import Path as _Path

        skill_scripts = _Path(__file__).resolve().parents[1] / "scripts"
        if str(skill_scripts) not in _sys.path:
            _sys.path.insert(0, str(skill_scripts))

        def load(name, file):
            spec = importlib.util.spec_from_file_location(name, file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module

        compile_mod = load("compile_ri", skill_scripts / "compile_runtime_index.py")
        query_mod = load("query_rf", skill_scripts / "query_runtime_facts.py")
        self.assertEqual(compile_mod.CAPABILITY_LEVEL_ORDER, query_mod.CAPABILITY_LEVEL_ORDER)

    def test_capability_tags_exclude_none_valued_dimensions(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = compile_safe_zone_index(tmp)
            index = json.loads(index_path.read_text(encoding="utf-8"))
            cards = index["runtime_bp_index"]["brawler_runtime_cards"]

            for name, card in cards.items():
                tags = set(card.get("capability_tags") or [])
                levels = card.get("capability_levels") or {}
                # every tag must have a real (non-none) compiled level
                self.assertEqual(tags, set(levels.keys()), name)
                self.assertTrue(all(level != "none" for level in levels.values()), name)

            # range tiles: only heroes with an explicit "X 格" note carry it
            for name, card in cards.items():
                rt = card.get("range_tiles")
                self.assertTrue(rt is None or rt > 0, name)

    def test_fact_query_archetype_filter_keeps_only_members(self):
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
                    "--archetype",
                    "sniper",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_query"]

        self.assertEqual(["sniper"], payload["request"]["archetypes"])
        self.assertTrue(payload["fact_window"])
        for item in payload["fact_window"]:
            archs = set(item.get("runtime_card", {}).get("archetypes") or [])
            self.assertIn("sniper", archs)
        self.assert_no_forbidden_keys(payload)

    def test_fact_query_require_floor_keeps_only_allrounders(self):
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
                    "--require-floor",
                    "survivability,anti_tank@medium",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_query"]

        self.assertEqual(["survivability,anti_tank@medium"], payload["request"]["require_floor"])
        self.assertTrue(payload["fact_window"])
        order = {"none": 0, "low": 1, "medium_low": 2, "medium": 3, "medium_high": 4, "high": 5, "very_high": 6}
        for item in payload["fact_window"]:
            levels = item.get("runtime_card", {}).get("capability_levels") or {}
            for dim in ("survivability", "anti_tank"):
                self.assertIsNotNone(levels.get(dim), f"{item['id']} missing {dim}")
                self.assertGreaterEqual(order[levels[dim]], order["medium"], f"{item['id']}.{dim}")
        self.assert_no_forbidden_keys(payload)

    def test_fact_window_carries_failure_gate_activation(self):
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
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["runtime_fact_query"]

        for item in payload["fact_window"]:
            self.assertIn("failure_gate_activation", item)
            activation = item["failure_gate_activation"]
            self.assertIsInstance(activation, dict)
            for level in activation.values():
                self.assertIn(level, {"high", "medium", "low", "unknown"})

    def test_matchup_census_filters_survivors_by_bans(self):
        census_script = SKILL_DIR / "scripts" / "query_matchup_census.py"
        self.assertTrue(census_script.exists())
        with tempfile.TemporaryDirectory() as tmp:
            index_path = compile_safe_zone_index(tmp)
            index = json.loads(index_path.read_text(encoding="utf-8"))
            matchups = index["runtime_bp_index"]["matchup_index"]["by_brawler"]
            hero = next(
                name
                for name, edges in matchups.items()
                if edges.get("is_answered_by")
            )
            first_predator = matchups[hero]["is_answered_by"][0]["target"]

            base = subprocess.run(
                [sys.executable, str(census_script), "--index", str(index_path), "--hero", hero, "--json"],
                check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            banned = subprocess.run(
                [
                    sys.executable, str(census_script),
                    "--index", str(index_path), "--hero", hero, "--banned", first_predator, "--json",
                ],
                check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )

        base_body = json.loads(base.stdout)["matchup_census"]
        banned_body = json.loads(banned.stdout)["matchup_census"]
        self.assertEqual(base_body["answered_by"]["total_edges"], banned_body["answered_by"]["total_edges"])
        self.assertEqual(
            base_body["answered_by"]["alive_count"] - 1,
            banned_body["answered_by"]["alive_count"],
        )
        self.assertEqual(banned_body["answered_by"]["removed_by_bans"], 1)
        alive_names = {row["target"] for row in banned_body["answered_by"]["alive"]}
        self.assertNotIn(first_predator, alive_names)
        self.assert_no_forbidden_keys(banned_body)


if __name__ == "__main__":
    unittest.main()
