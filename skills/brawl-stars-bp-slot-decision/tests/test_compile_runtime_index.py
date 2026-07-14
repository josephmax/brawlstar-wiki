import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[1]
SCRIPT = SKILL_DIR / "scripts" / "compile_runtime_index.py"
DEFAULT_PROFILE = SKILL_DIR / "references" / "default-strength-profile.json"


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
    def test_default_strength_profile_preserves_tier_and_left_to_right_order(self):
        index = run_compile("--strength-profile", str(DEFAULT_PROFILE))
        safe_zone_strength = index["map_pool_signature"]["Safe Zone"]["candidate_index"]

        self.assertNotIn("strength_prior", index)
        self.assertNotIn("strength_layers", index)
        self.assertEqual("ikaoss11-july-2026-screenshot", index["manifest"]["strength_profile_id"])
        self.assertEqual("runtime-v2", index["manifest"]["index_shape"])
        self.assertIn("Safe Zone", index["map_pool_signature"])
        self.assertEqual("Heist", index["map_pool_signature"]["Safe Zone"]["map_context"]["mode"])
        self.assertIn(
            "long_range_safe_damage",
            index["map_pool_signature"]["Safe Zone"]["map_context"]["required_capabilities"],
        )
        self.assertIn("candidate_projection", index["map_pool_signature"]["Safe Zone"])
        self.assertNotIn("capability_index", index)

        brock = safe_zone_strength["Brock"]
        eight_bit = safe_zone_strength["8-Bit"]
        mico = safe_zone_strength["Mico"]

        self.assertEqual("S", brock["tier"])
        self.assertNotIn("effective_scope", brock)
        self.assertNotIn("scope_key", brock)
        self.assertEqual(1, brock["rank"])
        self.assertEqual("S", eight_bit["tier"])
        self.assertEqual(2, eight_bit["rank"])
        self.assertEqual("E", mico["tier"])
        self.assertEqual(104, mico["rank"])

    def test_runtime_v2_includes_candidate_cards_matchups_and_audit(self):
        index = run_compile("--strength-profile", str(DEFAULT_PROFILE))
        safe_zone = index["map_pool_signature"]["Safe Zone"]
        map_context = safe_zone["map_context"]
        candidate_index = safe_zone["candidate_index"]

        self.assertEqual(104, len(candidate_index))
        self.assertIn("objective_contracts", map_context)
        self.assertIn("hard_gates", map_context)
        self.assertIn("slot_pressure", map_context)
        self.assertIn("false_positive_filters", map_context)
        self.assertIsInstance(map_context["false_positive_filters"][0], dict)
        self.assertNotIn("then:", json.dumps(map_context["false_positive_filters"], ensure_ascii=False))

        ruffs_fit = candidate_index["Ruffs"]
        self.assertEqual("strong", ruffs_fit["fit"])
        self.assertEqual("S", ruffs_fit["tier"])
        self.assertEqual(9, ruffs_fit["rank"])
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

        brock_matchups = index["matchup_index"]["by_brawler"]["Brock"]
        self.assertTrue(any(edge["target"] == "8-Bit" for edge in brock_matchups["answers"]))
        self.assertTrue(any(edge["target"] == "Stu" for edge in brock_matchups["is_answered_by"]))
        meg_matchups = index["matchup_index"]["by_brawler"]["Meg"]
        self.assertTrue(any(edge["target"] == "Nani" for edge in meg_matchups["answers"]))
        self.assertFalse(any(edge["target"].startswith("[") for edge in meg_matchups["answers"]))

        audit = index["audit_summary"]
        self.assertEqual(1, audit["map_count"])
        self.assertEqual(104, audit["brawler_count"])
        self.assertEqual(104, audit["candidate_index_entries"]["Safe Zone"])

    def test_mode_contract_and_strength_do_not_promote_without_map_signal(self):
        index = run_compile_for_map("Bridge Too Far", "--strength-profile", str(DEFAULT_PROFILE))
        bridge = index["map_pool_signature"]["Bridge Too Far"]
        emz = bridge["candidate_index"]["Emz"]

        self.assertEqual("A", emz["tier"])
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
        index = run_compile_for_map("Bridge Too Far", "--strength-profile", str(DEFAULT_PROFILE))
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
        crystal_index = run_compile_for_map(
            "Crystal Arcade",
            "--strength-profile",
            str(DEFAULT_PROFILE),
        )
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

        goldarm_index = run_compile_for_map(
            "Goldarm Gulch",
            "--strength-profile",
            str(DEFAULT_PROFILE),
        )
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

    def test_projection_window_preserves_ability_diversity_before_strength_rank_cutoff(self):
        index = run_compile_for_map("Bridge Too Far", "--strength-profile", str(DEFAULT_PROFILE))
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

    def test_map_strength_overrides_mode_strength_and_mode_overrides_global(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "strength.json"
            profile_path.write_text(
                json.dumps(
                    {
                        "schema": "brawlstar.strength_profile.v1",
                        "profile_id": "override-test",
                        "tier_order": ["S", "A", "B", "C", "D", "E"],
                        "profiles": {
                            "global": {
                                "tiers": {
                                    "S": ["Brock"],
                                    "A": [],
                                    "B": [],
                                    "C": [],
                                    "D": [],
                                    "E": [],
                                }
                            },
                            "modes": {
                                "Heist": {
                                    "mode": "Heist",
                                    "tiers": {
                                        "S": [],
                                        "A": [],
                                        "B": [],
                                        "C": ["Brock"],
                                        "D": [],
                                        "E": [],
                                    },
                                }
                            },
                            "maps": {
                                "Heist/Safe Zone": {
                                    "mode": "Heist",
                                    "map": "Safe Zone",
                                    "tiers": {
                                        "S": [],
                                        "A": [],
                                        "B": [],
                                        "C": [],
                                        "D": ["Brock"],
                                        "E": [],
                                    },
                                }
                            },
                        },
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            index = run_compile("--strength-profile", str(profile_path))
            map_strength = index["map_pool_signature"]["Safe Zone"]["candidate_index"]["Brock"]

        self.assertNotIn("strength_prior", index)
        self.assertEqual("D", map_strength["tier"])
        self.assertEqual(1, map_strength["rank"])
        self.assertNotIn("effective_scope", map_strength)
        self.assertNotIn("scope_key", map_strength)

    def test_single_map_runtime_index_stays_compact(self):
        output = run_compile_raw("--strength-profile", str(DEFAULT_PROFILE))
        self.assertLess(len(output.encode("utf-8")), 1_500_000)

    def test_all_maps_runtime_index_stays_compact(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--repo",
                str(REPO_ROOT),
                "--strength-profile",
                str(DEFAULT_PROFILE),
                "--json",
            ],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        )
        index = json.loads(result.stdout)["runtime_bp_index"]

        self.assertEqual(30, len(index["map_pool_signature"]))
        self.assertLess(len(result.stdout.encode("utf-8")), 5_000_000)


if __name__ == "__main__":
    unittest.main()
