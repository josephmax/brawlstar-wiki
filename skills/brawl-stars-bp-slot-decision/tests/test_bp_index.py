import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"
SCRIPT = SKILL_DIR / "scripts" / "bp_index.py"
PRECHECK_SCRIPT = SKILL_DIR / "scripts" / "runtime_index_precheck.py"
FACT_QUERY_SCRIPT = SKILL_DIR / "scripts" / "query_runtime_facts.py"
FACT_HYDRATE_SCRIPT = SKILL_DIR / "scripts" / "hydrate_runtime_facts.py"
COMPILE_REF = SKILL_DIR / "references" / "compile-knowledge.md"
DECIDE_REF = SKILL_DIR / "references" / "runtime-decision-knowledge.md"
REMOVED_TOOL_NAMES = [
    "scripts/query_runtime_index.py",
    "scripts/hydrate_runtime_evidence.py",
    "scripts/decide_with_runtime_index.py",
]


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
            "runtime_index_precheck",
            "scripts/runtime_index_precheck.py",
            "scripts/query_runtime_facts.py",
            "scripts/hydrate_runtime_facts.py",
            "include-id",
            "exclude-id",
            "relation-target",
            "bucket",
            "工具只做事实召回",
            "runtime_index_key",
            "runtime_index_compile_failed",
        ]
        for term in required_terms:
            self.assertIn(term, text)

        self.assertTrue(COMPILE_REF.exists())
        self.assertTrue(DECIDE_REF.exists())
        self.assertTrue(PRECHECK_SCRIPT.exists())
        self.assertTrue(FACT_QUERY_SCRIPT.exists())
        self.assertTrue(FACT_HYDRATE_SCRIPT.exists())
        for name in REMOVED_TOOL_NAMES:
            self.assertFalse((SKILL_DIR / name).exists(), name)
            self.assertNotIn(name, text)
            self.assertNotIn(name, DECIDE_REF.read_text(encoding="utf-8"))
            self.assertNotIn(name, COMPILE_REF.read_text(encoding="utf-8"))
        self.assertNotIn("legacy", text.casefold())
        self.assertNotIn("legacy", DECIDE_REF.read_text(encoding="utf-8").casefold())
        self.assertNotIn("wiki/syntheses/", text)
        self.assertNotIn("wiki/syntheses/", script)
        self.assertNotIn("wiki/syntheses/", PRECHECK_SCRIPT.read_text(encoding="utf-8"))
        self.assertNotIn("wiki/syntheses/", FACT_QUERY_SCRIPT.read_text(encoding="utf-8"))
        self.assertNotIn("wiki/syntheses/", FACT_HYDRATE_SCRIPT.read_text(encoding="utf-8"))

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

    def test_runtime_index_precheck_acquires_compile_lock_when_index_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    str(PRECHECK_SCRIPT),
                    "--repo",
                    tmp,
                    "--index-key",
                    "ranked-default",
                    "--max-polls",
                    "1",
                    "--poll-delay",
                    "0",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)

            self.assertEqual("compile_required", payload["status"])
            self.assertTrue(payload["lock_owned"])
            lock_path = Path(payload["lock_path"])
            self.assertTrue(lock_path.exists())
            lock_payload = json.loads(lock_path.read_text(encoding="utf-8"))
            self.assertEqual("compiling", lock_payload["state"])
            self.assertEqual("ranked-default", lock_payload["runtime_index_key"])

    def test_runtime_index_precheck_default_strength_matches_adopted_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    str(PRECHECK_SCRIPT),
                    "--repo",
                    tmp,
                    "--map-pool-id",
                    "Safe Zone",
                    "--max-polls",
                    "1",
                    "--poll-delay",
                    "0",
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)
            lock_payload = json.loads(Path(payload["lock_path"]).read_text(encoding="utf-8"))

            self.assertEqual("ikaoss11-july-2026-screenshot", lock_payload["strength_profile_id"])

    def test_runtime_index_precheck_fails_after_bounded_wait_on_active_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_dir = Path(tmp) / "outputs" / "runtime-bp-index"
            index_dir.mkdir(parents=True)
            lock_path = index_dir / "ranked-default.lock"
            lock_path.write_text(
                json.dumps(
                    {
                        "state": "compiling",
                        "runtime_index_key": "ranked-default",
                        "owner": "other-agent",
                        "started_at": datetime.now(timezone.utc).isoformat(),
                        "compile_input_hash": "unknown",
                        "attempt": 1,
                    }
                ),
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(PRECHECK_SCRIPT),
                    "--repo",
                    tmp,
                    "--index-key",
                    "ranked-default",
                    "--max-polls",
                    "1",
                    "--poll-delay",
                    "0",
                    "--stale-seconds",
                    "600",
                    "--json",
                ],
                text=True,
                stdout=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)

            self.assertEqual(2, result.returncode)
            self.assertEqual("runtime_index_compile_failed", payload["status"])
            self.assertFalse(payload["lock_owned"])


if __name__ == "__main__":
    unittest.main()
