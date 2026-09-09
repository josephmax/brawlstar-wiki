import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
REPO = SCRIPTS.parents[2]
sys.path.insert(0, str(SCRIPTS))
from candidate_mask import read_mask
from query_matchup_census import census


class CandidateMaskTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp.name)
        cls.index = cls.root / "index.json"
        subprocess.run([sys.executable, str(SCRIPTS / "compile_runtime_index.py"),
                        "--repo", str(REPO), "--map", "Safe Zone", "--no-environment",
                        "--output", str(cls.index)], check=True, capture_output=True)
        cls.data = json.loads(cls.index.read_text())["runtime_bp_index"]

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def mask(self, ids, **extra):
        path = self.root / "mask.json"
        path.write_text(json.dumps({"schema": "candidate_mask.v1", "mode": "allowlist",
                                   "ids": ids, "index_source_hash": self.data["manifest"]["source_hash"], **extra}))
        return str(path)

    def run_cli(self, operation, *args, success=True):
        result = subprocess.run([sys.executable, str(SCRIPTS / f"{operation}_runtime_facts.py"),
                                 "--index", str(self.index), "--map", "Safe Zone", "--json", *args],
                                capture_output=True, text=True)
        if not success:
            self.assertNotEqual(result.returncode, 0)
            return result.stderr
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)["runtime_fact_query" if operation == "query" else "runtime_fact_hydration"]

    def test_all_candidate_entries_and_hydration_respect_mask(self):
        mask = self.mask(["Brock"])
        for flags in [[], ["--bucket", "early_pick"], ["--capability", "wall_break"],
                      ["--archetype", "sniper"], ["--require-floor", "survivability@low"]]:
            result = self.run_cli("query", "--candidate-mask-file", mask, "--include-id", "Meg",
                                  "--include-id", "Brock", "--relation-target", "8-Bit", *flags)
            self.assertEqual([r["id"] for r in result["fact_window"]], ["Brock"])
            self.assertTrue(result["candidate_mask"]["applied"])
            self.assertEqual(result["candidate_mask"]["visible_id_count"], 1)
        unmasked = self.run_cli("hydrate", "--include-id", "Brock", "--relation-target", "8-Bit")
        masked = self.run_cli("hydrate", "--candidate-mask-file", mask, "--include-id", "Brock",
                              "--include-id", "Meg", "--relation-target", "8-Bit")
        self.assertEqual(list(masked["entities"]), ["Brock"])
        self.assertEqual(masked["entities"]["Brock"], unmasked["entities"]["Brock"])
        self.assertTrue(masked["entities"]["Brock"]["conditional_relations"])
        excluded = self.run_cli("query", "--candidate-mask-file", mask, "--include-id", "Brock", "--exclude-id", "Brock")
        self.assertEqual(excluded["fact_window"], [])

    def test_empty_unknown_missing_and_wrong_version_do_not_expand_pool(self):
        mask = self.mask([])
        self.assertEqual(self.run_cli("query", "--candidate-mask-file", mask, "--include-id", "Brock")["fact_window"], [])
        self.assertEqual(self.run_cli("hydrate", "--candidate-mask-file", mask, "--include-id", "Brock")["entities"], {})
        self.assertTrue(self.run_cli("query")["fact_window"])
        self.run_cli("query", "--candidate-mask-file", str(self.root / "missing.json"), success=False)
        self.run_cli("query", "--candidate-mask-file", self.mask(["Unknown Hero"]), success=False)
        self.run_cli("query", "--candidate-mask-file", self.mask(["Brock"], index_source_hash="wrong"), success=False)

    def test_cache_separates_masks_windows_and_changed_index_content(self):
        cache = str(self.root / "cache")
        mask = self.mask(["Brock"])
        args = ["--candidate-mask-file", mask, "--cache-dir", cache, "--include-id", "Brock", "--include-id", "Meg"]
        self.run_cli("query", *args)
        self.assertTrue(self.run_cli("query", *args)["cache_hit"])
        self.mask(["Meg"])
        changed = self.run_cli("query", *args)
        self.assertNotIn("cache_hit", changed)
        self.assertEqual([r["id"] for r in changed["fact_window"]], ["Meg"])
        for flag, value in [("--capability", "wall_break"), ("--archetype", "sniper"), ("--require-floor", "survivability@low")]:
            self.assertNotIn("cache_hit", self.run_cli("query", *args, flag, value))
        original = self.index.read_text()
        try:
            self.index.write_text(original + "\n")
            self.assertNotIn("cache_hit", self.run_cli("query", *args))
        finally:
            self.index.write_text(original)

    def test_census_preserves_global_edges_and_adds_masked_projection(self):
        hero = next(name for name in self.data["brawler_runtime_cards"] if census(self.data, name, set())["answered_by"]["alive"])
        baseline = census(self.data, hero, set())
        chosen = baseline["answered_by"]["alive"][0]["target"]
        mask = read_mask(self.mask([chosen]))
        result = census(self.data, hero, set(), mask)
        self.assertEqual(result["answered_by"], baseline["answered_by"])
        self.assertEqual(result["answers"], baseline["answers"])
        self.assertEqual({r["target"] for r in result["masked_answered_by"]["alive"]}, {chosen})
        self.assertEqual(census(self.data, hero, {chosen}, mask)["masked_answered_by"]["alive_count"], 0)

    def test_each_call_has_its_own_window_without_changing_the_index(self):
        original_index = self.index.read_bytes()
        include = ["--include-id", "Brock", "--include-id", "Meg"]
        for operation, key in [("query", "fact_window"), ("hydrate", "entity_window")]:
            for visible in [["Brock"], ["Meg"], []]:
                with self.subTest(operation=operation, visible=visible):
                    result = self.run_cli(operation, *include, "--candidate-mask-file",
                                          self.mask(visible, context_id="window-only"))
                    self.assertEqual([row["id"] for row in result[key]], visible)
                    self.assertEqual(result["candidate_mask"]["visible_id_count"], len(visible))
            result = self.run_cli(operation, *include)
            self.assertTrue({"Brock", "Meg"}.issubset({row["id"] for row in result[key]}))
            self.assertIsNone(result["candidate_mask"]["visible_id_count"])
        self.assertEqual(self.index.read_bytes(), original_index)

    def test_mask_count_is_not_the_query_match_count(self):
        result = self.run_cli("query", "--candidate-mask-file", self.mask(["Brock", "Meg"]),
                              "--include-id", "Brock", "--exclude-id", "Meg")
        self.assertEqual(result["candidate_mask"]["visible_id_count"], 2)
        self.assertEqual([row["id"] for row in result["fact_window"]], ["Brock"])

if __name__ == "__main__":
    unittest.main()
