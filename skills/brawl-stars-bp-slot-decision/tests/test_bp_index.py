import json
import subprocess
import sys
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"
SCRIPT = SKILL_DIR / "scripts" / "bp_index.py"


class BPSkillIndexTest(unittest.TestCase):
    def test_skill_mentions_required_runtime_pages(self):
        text = SKILL_MD.read_text(encoding="utf-8")

        required_pages = [
            "wiki/index.md",
            "wiki/syntheses/BP-推理DSL规范.md",
            "wiki/syntheses/条件化对位模型.md",
            "wiki/syntheses/Ban-Pick-问题拆分.md",
            "wiki/syntheses/地图特征建模Schema.md",
            "wiki/syntheses/地图因素BP表达规范.md",
            "wiki/syntheses/Ranked-Season-46-地图Map-Profile总览.md",
            "wiki/syntheses/英雄BP建模执行状态.md",
            "wiki/syntheses/BP-条件化对位边索引.md",
            "wiki/syntheses/BP-英雄地图特征适配索引.md",
        ]

        for page in required_pages:
            self.assertIn(page, text)

    def test_index_script_finds_ranked_map_brawler_and_matchup_refs(self):
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

        self.assertTrue(payload["map"]["path"].endswith("wiki/entities/maps/Safe Zone.md"))
        self.assertTrue(payload["brawlers"]["Brock"]["path"].endswith("wiki/entities/brawlers/Brock.md"))
        self.assertTrue(payload["brawlers"]["Mortis"]["path"].endswith("wiki/entities/brawlers/Mortis.md"))
        self.assertTrue(payload["index_hits"]["matchups"])
        self.assertTrue(payload["index_hits"]["map_hooks"])


if __name__ == "__main__":
    unittest.main()
