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


if __name__ == "__main__":
    unittest.main()
