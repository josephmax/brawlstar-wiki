import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[1]
SCRIPT = SKILL_DIR / "scripts" / "build_hero_briefs.py"
sys.path.insert(0, str(SKILL_DIR / "scripts"))

import build_hero_briefs as briefs  # noqa: E402

EVENT = {
    "archive": "wiki/environment/2026-10/archive.sqlite3",
    "kind": "last_chance_qualifier",
    "names": ["LCQ"],
    "page_titles": ["LCQ"],
    "start_date": "2026-10-17",
    "end_date": "2026-10-18",
    "played_sets": 60,
    "played_series": 15,
    "scopes": {
        "global": [
            {
                "brawler": "Gray",
                "pick_sets": 3,
                "set_wins_when_picked": 1,
                "local_ban_nominations": 5,
                "local_ban_set_coverage": 5,
                "global_ban_nominations": 0,
                "global_ban_series_coverage": 3,
            }
        ],
        "mode": [
            {
                "mode": "Bounty",
                "brawler": "Gray",
                "pick_sets": 3,
                "set_wins_when_picked": 1,
                "local_ban_nominations": 5,
                "local_ban_set_coverage": 5,
                "global_ban_nominations": 0,
                "global_ban_series_coverage": 3,
            }
        ],
        "map": [],
    },
}


def patch(patch_id, effective_at, names, has_ledger=True, fold="pending"):
    return {
        "patch_id": patch_id,
        "effective_at": effective_at,
        "has_ledger": has_ledger,
        "brawlers": {
            name: {"kinds": ["balance"], "direction": "nerf", "rows": ["row"] if has_ledger else [], "fold": fold, "note": ""}
            for name in names
        },
    }


class HeroBriefUnitTest(unittest.TestCase):
    def test_profile_markdown_drops_only_the_breakpoint_profile(self):
        page = (
            "# Gray\n\n```yaml\nbp_brawler_profile:\n  profile_status: bp_ready\n```\n\n"
            "## combat_breakpoint_profile\n\n```json\n{\n  \"combat_breakpoint_profile\": {\"brawler\": \"Gray\"}\n}\n```\n\n"
            "## 关联页面\n\n- [[sources/Fandom-Gray]]\n"
        )
        text = briefs.profile_markdown(page)
        self.assertNotIn("combat_breakpoint_profile", text)
        self.assertIn("bp_brawler_profile", text)
        self.assertIn("[[sources/Fandom-Gray]]", text)

    def test_event_record_is_withheld_when_the_brawler_changed_after_the_event(self):
        after = [patch("nov", "2026-11-03", ["Gray"])]
        block = briefs.esports_block("Gray", EVENT, after)
        self.assertEqual(block["status"], "withheld")
        self.assertEqual(block["changed_by"], [{"patch_id": "nov", "effective_at": "2026-11-03"}])
        self.assertNotIn("overall", block)

    def test_event_record_is_shown_when_only_other_brawlers_or_older_patches_changed(self):
        patches = [patch("sep", "2026-09-16", ["Gray"]), patch("nov", "2026-11-03", ["Shade"])]
        block = briefs.esports_block("Gray", EVENT, patches)
        self.assertEqual(block["status"], "ok")
        self.assertEqual(block["overall"]["pick_rate"], 0.05)
        self.assertEqual(block["overall"]["win_rate_when_picked"], 0.3333)
        self.assertEqual(block["overall"]["global_ban_rate"], 0.2)
        self.assertEqual(block["by_mode"][0]["mode"], "Bounty")

    def test_event_without_a_record_is_no_sample_not_zero(self):
        self.assertEqual(briefs.esports_block("Bo", EVENT, [])["status"], "no_sample")
        self.assertEqual(briefs.esports_block("Bo", None, [])["status"], "no_event")

    def test_recent_changes_are_newest_first_and_skip_pre_ledger_patches(self):
        patches = [
            patch("jun", "2026-06-29", ["Gray"], has_ledger=False, fold="legacy"),
            patch("sep", "2026-09-16", ["Gray"], fold="folded"),
            patch("nov", "2026-11-03", ["Gray"], fold="partial"),
        ]
        changes = briefs.recent_changes("Gray", patches)
        self.assertEqual([item["patch_id"] for item in changes], ["nov", "sep"])
        self.assertEqual([item["folded_into_profile"] for item in changes], [False, True])
        self.assertEqual(changes[0]["official_rows"], ["row"])


class HeroBriefRepositoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.briefs = briefs.build(REPO_ROOT)

    def test_every_brawler_has_a_brief_within_the_size_contract(self):
        names = {path.stem for path in (REPO_ROOT / "wiki/entities/brawlers").glob("*.md")}
        self.assertEqual(set(self.briefs), names)
        for name, brief in self.briefs.items():
            size = len(json.dumps(brief, ensure_ascii=False))
            self.assertLessEqual(size, briefs.MAX_BRIEF_CHARS, name)
            self.assertEqual(self.manifest["brawlers"][name]["chars"], size)
            self.assertNotIn("combat_breakpoint_profile", brief["profile_markdown"], name)

    def test_strict_event_rule_holds_for_every_brawler(self):
        event = self.manifest["latest_event"]
        self.assertIsNotNone(event)
        changed_after = {
            name
            for item in self.manifest["patches"]
            if (item["effective_at"] or "") > event["end_date"]
            for name in item["brawlers"]
        }
        for name, brief in self.briefs.items():
            withheld = brief["esports"]["status"] == "withheld"
            self.assertEqual(withheld, name in changed_after, name)

    def test_unfolded_patch_rows_reach_the_brief_verbatim(self):
        ledgered = [item for item in self.manifest["patches"] if item["has_ledger"]]
        self.assertTrue(ledgered)
        latest = ledgered[-1]
        for name, row in latest["brawlers"].items():
            change = self.briefs[name]["recent_changes"][0]
            self.assertEqual(change["patch_id"], latest["patch_id"], name)
            self.assertTrue(change["official_rows"], name)
            self.assertEqual(change["folded_into_profile"], row["fold"] in briefs.FOLDED, name)

    def test_cli_writes_manifest_last_and_leaves_archives_untouched(self):
        archives = sorted((REPO_ROOT / "wiki/environment").glob("**/*.sqlite3"))
        before = {path: path.read_bytes() for path in archives}
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--repo", str(REPO_ROOT), "--output", tmp],
                capture_output=True,
                text=True,
                check=True,
            )
            summary = json.loads(result.stdout)
            manifest = json.loads((Path(tmp) / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(summary["briefs"], len(manifest["brawlers"]))
            for item in manifest["brawlers"].values():
                self.assertTrue((Path(tmp) / item["file"]).is_file())
        self.assertEqual(before, {path: path.read_bytes() for path in archives})


if __name__ == "__main__":
    unittest.main()
