import json
import subprocess
import sys
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[1]
SCRIPT = SKILL_DIR / "scripts" / "compile_runtime_index.py"


def run_compile(*args):
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--repo",
            str(REPO_ROOT),
            "--map",
            "Safe Zone",
            "--json",
            *args,
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    payload = json.loads(result.stdout)
    return payload["runtime_bp_index"]


def run_compile_for_map(map_name, *args):
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--repo",
            str(REPO_ROOT),
            "--map",
            map_name,
            "--json",
            *args,
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    payload = json.loads(result.stdout)
    return payload["runtime_bp_index"]


def run_compile_raw(*args):
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--repo",
            str(REPO_ROOT),
            "--map",
            "Safe Zone",
            "--json",
            *args,
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    ).stdout


class CompileRuntimeIndexTest(unittest.TestCase):
    def test_manifest_records_empty_environment_slot_without_fabrication(self):
        index = run_compile()
        safe_zone = index["map_pool_signature"]["Safe Zone"]

        # 环境信号槽：当前为空，明确记录，不推断任何 tier/rank
        self.assertNotIn("strength_profile_id", index["manifest"])
        self.assertNotIn("strength_profile_hash", index["manifest"])
        self.assertIsNone(index["manifest"]["pickrate_source"])
        self.assertEqual("empty", index["manifest"]["pickrate_status"])
        self.assertEqual("runtime-v2", index["manifest"]["index_shape"])
        self.assertIn("Safe Zone", index["map_pool_signature"])
        self.assertEqual("Heist", index["map_pool_signature"]["Safe Zone"]["map_context"]["mode"])
        self.assertIn(
            "long_range_safe_damage",
            index["map_pool_signature"]["Safe Zone"]["map_context"]["required_capabilities"],
        )
        self.assertIn("candidate_projection", index["map_pool_signature"]["Safe Zone"])
        self.assertNotIn("capability_index", index)

        # 候选层不再有任何强度/tier 概念
        brock = safe_zone["candidate_index"]["Brock"]
        self.assertNotIn("tier", brock)
        self.assertNotIn("rank", brock)
        self.assertNotIn("score", brock)
        self.assertNotIn("proof_threshold", brock)

    def test_runtime_v2_includes_candidate_cards_matchups_and_audit(self):
        index = run_compile()
        safe_zone = index["map_pool_signature"]["Safe Zone"]
        map_context = safe_zone["map_context"]
        candidate_index = safe_zone["candidate_index"]

        self.assertEqual(105, len(candidate_index))
        self.assertIn("objective_contracts", map_context)
        self.assertIn("hard_gates", map_context)
        self.assertIn("slot_pressure", map_context)
        self.assertIn("false_positive_filters", map_context)
        self.assertIsInstance(map_context["false_positive_filters"][0], dict)
        self.assertNotIn("then:", json.dumps(map_context["false_positive_filters"], ensure_ascii=False))

        ruffs_fit = candidate_index["Ruffs"]
        self.assertEqual("strong", ruffs_fit["fit"])
        self.assertNotIn("tier", ruffs_fit)
        self.assertNotIn("rank", ruffs_fit)
        self.assertIn("early_pick", ruffs_fit["projection_buckets"])
        self.assertIn("ban_pressure", ruffs_fit["projection_buckets"])
        self.assertIn("heist_buffed_lane_and_safe_support", ruffs_fit["active_hook_ids"])
        self.assertTrue(ruffs_fit["mode_contract_hit"])
        self.assertIn("required_build_ids", ruffs_fit)
        self.assertIn("failure_gates", ruffs_fit)
        self.assertNotIn("risk_ids", ruffs_fit)

        ruffs_card = index["brawler_runtime_cards"]["Ruffs"]
        self.assertIn("heist_buffed_lane_and_safe_support", ruffs_card["map_hooks"])
        self.assertIn("active_when", ruffs_card["map_hooks"]["heist_buffed_lane_and_safe_support"])
        self.assertIn("buff_without_conversion", ruffs_card["failure_modes"])
        self.assertIn("slot_1", ruffs_card["slot_notes"])
        # 运行卡不再携带强度上下文
        self.assertNotIn("strength_context", ruffs_card)
        self.assertNotIn("strength_visibility", ruffs_card)
        self.assertNotIn("proof_threshold", ruffs_card)

        brock_matchups = index["matchup_index"]["by_brawler"]["Brock"]
        self.assertTrue(any(edge["target"] == "8-Bit" for edge in brock_matchups["answers"]))
        self.assertTrue(any(edge["target"] == "Stu" for edge in brock_matchups["is_answered_by"]))
        meg_matchups = index["matchup_index"]["by_brawler"]["Meg"]
        self.assertTrue(any(edge["target"] == "Nani" for edge in meg_matchups["answers"]))
        self.assertFalse(any(edge["target"].startswith("[") for edge in meg_matchups["answers"]))

        audit = index["audit_summary"]
        self.assertEqual(1, audit["map_count"])
        self.assertEqual(105, audit["brawler_count"])
        self.assertEqual(105, audit["candidate_index_entries"]["Safe Zone"])

    def test_mode_contract_does_not_promote_without_map_signal(self):
        index = run_compile_for_map("Bridge Too Far")
        bridge = index["map_pool_signature"]["Bridge Too Far"]
        emz = bridge["candidate_index"]["Emz"]

        self.assertNotIn("tier", emz)
        self.assertTrue(emz["mode_contract_hit"])
        self.assertEqual([], emz.get("matched_capabilities") or [])
        self.assertEqual([], emz.get("active_hook_ids") or [])
        self.assertNotEqual("strong", emz["fit"])
        self.assertEqual("weak", emz["map_floor_fit"])
        self.assertEqual("evidence_only", emz["mode_contract_fit"])
        self.assertFalse(emz["slot_eligibility"]["early_pick"])
        self.assertFalse(emz["slot_eligibility"]["late_pick"])
        self.assertIn("enemy_targets_answered_by_candidate", emz["conditional_lift"])
        self.assertIn("counter_response", emz["recall_channels"])
        self.assertIn("heist_primary_dps_false_positive", emz["failure_gates"])
        self.assertNotIn("early_pick", emz.get("projection_buckets", []))
        self.assertNotIn("ban_pressure", emz.get("projection_buckets", []))

    def test_mode_contract_alone_does_not_enter_map_candidate_projection(self):
        index = run_compile_for_map("Bridge Too Far")
        bridge = index["map_pool_signature"]["Bridge Too Far"]

        sandy = bridge["candidate_index"]["Sandy"]
        self.assertTrue(sandy["mode_contract_hit"])
        self.assertEqual([], sandy.get("matched_capabilities") or [])
        self.assertEqual([], sandy.get("active_hook_ids") or [])
        self.assertEqual("weak", sandy["fit"])
        self.assertEqual([], sandy.get("projection_buckets", []))
        self.assertFalse(sandy["slot_eligibility"]["early_pick"])
        self.assertFalse(sandy["slot_eligibility"]["response_pick"])
        self.assertFalse(sandy["slot_eligibility"]["late_pick"])

        projected_names = {
            item["brawler"]
            for bucket in ("early_pick", "response_pick", "late_pick", "ban_pressure")
            for item in bridge["candidate_projection"].get(bucket, [])
        }
        self.assertNotIn("Sandy", projected_names)
        self.assertNotIn("Moe", projected_names)
        self.assertNotIn("Emz", projected_names)

    def test_july_event_map_fit_review_promotes_only_mechanism_backed_hooks(self):
        crystal_index = run_compile_for_map("Crystal Arcade")
        crystal = crystal_index["map_pool_signature"]["Crystal Arcade"]
        expected_hooks = {
            "Griff": "gem_mid_super_area_and_anti_body",
            "Stu": "dash_chain_lane_pressure",
            "Pearl": "gem_heat_shield_mid_anchor",
            "Meeple": "gem_mid_rule_area_carrier_pressure",
        }
        for brawler, hook_id in expected_hooks.items():
            candidate = crystal["candidate_index"][brawler]
            self.assertEqual("strong", candidate["map_floor_fit"])
            self.assertIn(hook_id, candidate["active_hook_ids"])

        glowy = crystal["candidate_index"]["Glowy"]
        self.assertEqual("weak", glowy["map_floor_fit"])
        self.assertEqual([], glowy.get("active_hook_ids") or [])

        goldarm_index = run_compile_for_map("Goldarm Gulch")
        goldarm = goldarm_index["map_pool_signature"]["Goldarm Gulch"]
        charlie = goldarm["candidate_index"]["Charlie"]
        self.assertEqual("strong", charlie["map_floor_fit"])
        self.assertIn(
            "knockout_cocoon_first_pick_and_spider_route_tax",
            charlie["active_hook_ids"],
        )

        damian = goldarm["candidate_index"]["Damian"]
        self.assertEqual("weak", damian["map_floor_fit"])
        self.assertEqual([], damian.get("active_hook_ids") or [])

    def test_projection_window_preserves_ability_diversity(self):
        index = run_compile_for_map("Bridge Too Far")
        bridge = index["map_pool_signature"]["Bridge Too Far"]
        early_pick_names = [
            item["brawler"]
            for item in bridge["candidate_projection"]["early_pick"]
        ]

        self.assertGreater(len(early_pick_names), 8)
        self.assertIn("Brock", early_pick_names)
        self.assertIn("Colt", early_pick_names)
        self.assertIn("Piper", early_pick_names)
        self.assertIn("Nani", early_pick_names)

        for name in early_pick_names:
            item = bridge["candidate_index"][name]
            self.assertTrue(item.get("active_hook_ids") or item.get("matched_capabilities"))
            self.assertNotEqual("weak", item["fit"])

    def test_single_map_runtime_index_stays_compact(self):
        output = run_compile_raw()
        self.assertLess(len(output.encode("utf-8")), 1_500_000)

    def test_all_maps_runtime_index_stays_compact(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--repo",
                str(REPO_ROOT),
                "--json",
            ],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        )
        index = json.loads(result.stdout)["runtime_bp_index"]
        self.assertGreaterEqual(len(index["map_pool_signature"]), 20)
        self.assertLess(len(result.stdout.encode("utf-8")), 5_000_000)


if __name__ == "__main__":
    unittest.main()
