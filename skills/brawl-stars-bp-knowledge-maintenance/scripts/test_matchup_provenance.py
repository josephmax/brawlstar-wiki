#!/usr/bin/env python3
"""Regress reviewed attribution cases through the real BP compiler.

These are bounded evidence decisions, not an automatic strategy judge. A new
source may justify promoting a held candidate; review that source and update
the case together rather than treating absence as proof of no advantage.
"""

import importlib.util
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[3]
COMPILER = ROOT / "skills/brawl-stars-bp-slot-decision/scripts/compile_runtime_index.py"
spec = importlib.util.spec_from_file_location("matchup_compiler", COMPILER)
compiler = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compiler)


class MatchupProvenanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = [
            compiler.compile_brawler_card(path, ROOT)
            for path in sorted((ROOT / "wiki/entities/brawlers").glob("*.md"))
        ]
        cls.gray = next(card for card in cls.cards if card["brawler"] == "Gray")

    def test_gray_squeak_candidate_is_not_a_reviewed_counter_mechanism(self):
        # PLP supplies a direction, not a per-target explanation. Keep the
        # immutable observation even while withdrawing its unsupported promotion.
        raw = (ROOT / "raw/sources/pl-prodigy/brawlers/gray-2026-06-30.md").read_text()
        block = raw.split("## Matchup Fields", 1)[1]
        data = json.loads(re.search(r"```json\s*(.*?)```", block, re.S).group(1))
        self.assertIn("Squeak", [item["name"] for item in data["countersThese"]])
        self.assertFalse(any("Squeak" in row["target"] for row in self.gray["conditional_matchups"]),
                         "Gray/Squeak needs its own reviewed mechanism before runtime promotion")
        index = compiler.build_matchup_index(self.cards)["by_brawler"]["Gray"]
        self.assertNotIn("Squeak", [edge["target"] for edge in index["answers"]])

    def test_reviewed_group_keeps_its_conditions_and_other_targets(self):
        index = compiler.build_matchup_index(self.cards)["by_brawler"]["Gray"]
        for target in ("Sprout", "Grom", "Dynamike"):
            with self.subTest(target=target):
                edge = next(edge for edge in index["answers"] if edge["target"] == target)
                self.assertTrue(edge["mechanism"])
                self.assertIn("守门", edge["active_when"])
                self.assertIn("被守", edge["fails_when"])
        self.assertIn("Carl", [edge["target"] for edge in index["answers"]])
        self.assertIn("Stu", [edge["target"] for edge in index["is_answered_by"]])


class MaintainerReviewTest(unittest.TestCase):
    """2026-10-28 maintainer decisions survive the actual runtime projection."""
    @classmethod
    def setUpClass(cls):
        cls.cards = [compiler.compile_brawler_card(p, ROOT)
                     for p in sorted((ROOT / "wiki/entities/brawlers").glob("*.md"))]
        cls.index = compiler.build_matchup_index(cls.cards)["by_brawler"]

    def edge(self, subject, direction, target):
        matches = [r for r in self.index[subject][direction] if r["target"] == target]
        self.assertEqual(len(matches), 1, (subject, direction, target, matches))
        return matches[0]

    def test_rejected_or_unresolved_pairs_are_not_promoted_in_either_page(self):
        for a, b in [("Finx", "Gigi"), ("Finx", "Shade"), ("Wendy", "Pierce"),
                     ("Gene", "Bea"), ("Rico", "Tara"), ("Berry", "Sirius"),
                     ("Nori", "Starr Nova")]:
            for subject, target in [(a, b), (b, a)]:
                with self.subTest(subject=subject, target=target):
                    for direction in ["answers", "is_answered_by"]:
                        self.assertNotIn(target, [e["target"] for e in self.index[subject][direction]])

    def test_confirmed_edges_use_target_specific_mechanisms(self):
        cases = [
            ("Edgar", "answers", "Squeak", "回血", "投掷"),
            ("Nori", "is_answered_by", "Bolt", "Toss Up", "长线爆发"),
            ("Wendy", "answers", "Bolt", "减速", "pokers"),
            ("Rosa", "answers", "Bolt", "减速", "低血远程"),
            ("Jacky", "answers", "Doug", "Pneumatic Booster", "低中血"),
            ("Jacky", "answers", "Hank", "打断", "低中血"),
            ("Berry", "is_answered_by", "Gray", "Walking Cane", "高身体"),
            ("Stu", "answers", "Gigi", "风筝", "throwers/snipers"),
            ("Stu", "answers", "Squeak", "Breakthrough", "throwers/snipers"),
        ]
        for subject, direction, target, required, forbidden in cases:
            with self.subTest(subject=subject, target=target):
                edge = self.edge(subject, direction, target)
                self.assertIn(required, edge["mechanism"])
                self.assertNotIn(forbidden, edge["mechanism"])
                self.assertTrue(edge["active_when"])
                self.assertTrue(edge["fails_when"])

    def test_build_terrain_and_escape_conditions_survive_compilation(self):
        cases = [
            ("Nori", "is_answered_by", "Bolt", "active_when", ["Toss Up", "满速"]),
            ("Wendy", "answers", "Bolt", "active_when", ["Slowing Shield"]),
            ("Rosa", "answers", "Bolt", "active_when", ["Unfriendly Bushes", "极限充能"]),
            ("Jacky", "answers", "Doug", "active_when", ["Pneumatic Booster", "极限充能"]),
            ("Eve", "is_answered_by", "Grom", "fails_when", ["水路", "射程"]),
            ("Berry", "is_answered_by", "Juju", "fails_when", ["位移", "击退"]),
            ("Stu", "answers", "Squeak", "fails_when", ["钢墙"]),
            ("Berry", "is_answered_by", "8-Bit", "active_when", ["开阔", "长线"]),
            ("Berry", "answers", "8-Bit", "active_when", ["墙", "增伤器"]),
        ]
        for subject, direction, target, field, fragments in cases:
            with self.subTest(subject=subject, target=target, field=field):
                for fragment in fragments:
                    self.assertIn(fragment, self.edge(subject, direction, target)[field])
        self.assertNotIn("蓄力位", self.edge("Eve", "is_answered_by", "Grom")["mechanism"])

    def test_reciprocal_rows_and_unrelated_group_members_remain_consistent(self):
        for subject, direction, target, token in [
            ("Squeak", "is_answered_by", "Edgar", "回血"),
            ("Bolt", "is_answered_by", "Rosa", "减速"),
            ("Juju", "answers", "Berry", "位移"),
        ]:
            with self.subTest(subject=subject, target=target):
                edge = self.edge(subject, direction, target)
                self.assertIn(token, str(edge))
        for subject, direction, target in [("Finx", "answers", "Piper"),
                                          ("Edgar", "answers", "Sprout"),
                                          ("Wendy", "answers", "Max"),
                                          ("Rico", "is_answered_by", "Sprout"),
                                          ("Berry", "is_answered_by", "Trunk")]:
            self.edge(subject, direction, target)
        raw = (ROOT / "raw/sources/pl-prodigy/brawlers/finx-2026-06-30.md").read_text()
        data = json.loads(re.search(r"```json\s*(.*?)```", raw.split("## Matchup Fields", 1)[1], re.S).group(1))
        gigi = next(x for x in data["countersThese"] if x["name"] == "Gigi")
        self.assertEqual(gigi["winRate"], 0.628)


if __name__ == "__main__":
    unittest.main()
