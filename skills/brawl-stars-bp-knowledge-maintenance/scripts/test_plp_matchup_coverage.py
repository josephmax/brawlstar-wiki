import json
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
COMPILE_SCRIPT = (
    REPO_ROOT
    / "skills"
    / "brawl-stars-bp-slot-decision"
    / "scripts"
    / "compile_runtime_index.py"
)
DEFAULT_PROFILE = (
    REPO_ROOT
    / "skills"
    / "brawl-stars-bp-slot-decision"
    / "references"
    / "default-strength-profile.json"
)
AUDIT_SCRIPT = SCRIPT_DIR / "audit_plp_matchup_coverage.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("audit_plp_matchup_coverage", AUDIT_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class PLPMatchupCoverageAuditTest(unittest.TestCase):
    def test_latest_capture_per_brawler_excludes_superseded_matchups(self):
        audit = load_audit_module()
        with tempfile.TemporaryDirectory() as tmp:
            raw_dir = Path(tmp)
            older = raw_dir / "8bit-2026-06-30.md"
            newer = raw_dir / "8bit-2026-07-11.md"
            older.write_text(
                '# Direct Raw Capture: PLP 8-Bit\n\n```json\n'
                '{"name":"8-Bit","countersThese":[{"name":"Colt"}],"counteredBy":[]}\n'
                '```\n',
                encoding="utf-8",
            )
            newer.write_text(
                '# Direct Raw Capture: PLP 8-Bit\n\n```json\n'
                '{"name":"8-Bit","countersThese":[{"name":"Poco"}],"counteredBy":[]}\n'
                '```\n',
                encoding="utf-8",
            )
            lookup = audit.name_lookup({"8-Bit", "Colt", "Poco"})
            pairs = audit.plp_matchup_pairs(REPO_ROOT, raw_dir, lookup)

        self.assertEqual(1, len(pairs))
        self.assertEqual("Poco", pairs[0]["target"])
        self.assertTrue(pairs[0]["plp_source_ref"].endswith("8bit-2026-07-11.md"))

    def test_reports_plp_pairs_missing_from_compiled_matchup_index(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = Path(tmp) / "safe-zone-index.json"
            subprocess.run(
                [
                    sys.executable,
                    str(COMPILE_SCRIPT),
                    "--repo",
                    str(REPO_ROOT),
                    "--map",
                    "Safe Zone",
                    "--strength-profile",
                    str(DEFAULT_PROFILE),
                    "--output",
                    str(index_path),
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(AUDIT_SCRIPT),
                    "--repo",
                    str(REPO_ROOT),
                    "--runtime-index",
                    str(index_path),
                    "--json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            payload = json.loads(result.stdout)["plp_matchup_coverage"]

        summary = payload["summary"]
        self.assertEqual(104, summary["plp_raw_pages"])
        self.assertGreaterEqual(summary["plp_raw_files"], summary["plp_raw_pages"])
        self.assertGreater(summary["plp_pairs"], 1000)
        self.assertGreater(summary["compiled_pairs"], 1000)
        self.assertGreater(summary["overlap_pairs"], 1000)
        self.assertGreater(summary["plp_only_pairs"], 0)
        self.assertLess(summary["plp_only_pairs"], summary["plp_pairs"])

        seed = payload["plp_only_seeds"][0]
        self.assertEqual("needs_mechanism_review", seed["status"])
        self.assertIn(seed["direction"], {"answers", "is_answered_by"})
        self.assertTrue(seed["subject"])
        self.assertTrue(seed["target"])
        self.assertTrue(seed["plp_source_ref"].startswith("raw/sources/pl-prodigy/brawlers/"))
        self.assertIn("matchup_tier", seed)
        self.assertIn("source_kind", seed)
        self.assertIn("review_prompt", seed)


if __name__ == "__main__":
    unittest.main()
