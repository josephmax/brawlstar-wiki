import json
import subprocess
import sys
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"
SCRIPT = SKILL_DIR / "scripts" / "bp_index.py"
COMPILE_REF = SKILL_DIR / "references" / "compile-knowledge.md"
DECIDE_REF = SKILL_DIR / "references" / "runtime-decision-knowledge.md"


class BPSkillIndexTest(unittest.TestCase):
    def test_skill_uses_mode_specific_references_not_syntheses(self):
        text = SKILL_MD.read_text(encoding="utf-8")
        script = SCRIPT.read_text(encoding="utf-8")

        required_terms = [
            "compile",
            "decide",
            "references/compile-knowledge.md",
            "references/runtime-decision-knowledge.md",
            "wiki/entities/maps/",
            "wiki/entities/brawlers/",
            "runtime_bp_index",
        ]
        for term in required_terms:
            self.assertIn(term, text)

        self.assertTrue(COMPILE_REF.exists())
        self.assertTrue(DECIDE_REF.exists())
        self.assertNotIn("wiki/syntheses/", text)
        self.assertNotIn("wiki/syntheses/", script)

    def test_index_script_finds_ranked_map_and_brawler_pages(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--repo",
                str(REPO_ROOT),
                "--map",
                "Safe Zone",
                "--brawler",
                "Brock",
                "--enemy",
                "Mortis",
                "--json",
            ],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(
            [
                "skills/brawl-stars-bp-slot-decision/references/compile-knowledge.md",
                "skills/brawl-stars-bp-slot-decision/references/runtime-decision-knowledge.md",
            ],
            [page["path"] for page in payload["skill_reference_pages"]],
        )
        self.assertNotIn("runtime_pages", payload)
        self.assertTrue(payload["map"]["path"].endswith("wiki/entities/maps/Safe Zone.md"))
        self.assertTrue(payload["brawlers"]["Brock"]["path"].endswith("wiki/entities/brawlers/Brock.md"))
        self.assertTrue(payload["brawlers"]["Mortis"]["path"].endswith("wiki/entities/brawlers/Mortis.md"))
        self.assertEqual("user_supplied_or_compiled_runtime_index_required", payload["map"]["pool_membership"])
        self.assertTrue(payload["stable_source_hits"])


if __name__ == "__main__":
    unittest.main()
