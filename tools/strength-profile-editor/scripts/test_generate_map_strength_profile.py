import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "strength-profile-editor" / "scripts" / "generate_map_strength_profile.py"
RUNTIME_INDEX_SCRIPT = REPO / "skills" / "brawl-stars-bp-slot-decision" / "scripts" / "compile_runtime_index.py"
DEFAULT_PROFILE = REPO / "skills" / "brawl-stars-bp-slot-decision" / "references" / "default-strength-profile.json"


class GenerateMapStrengthProfileTest(unittest.TestCase):
    def test_generates_complete_map_scoped_strength_profile_for_editor_import(self):
        with tempfile.TemporaryDirectory() as tmp:
            index_path = Path(tmp) / "runtime-index.json"
            output_path = Path(tmp) / "map-strength-profile.json"
            subprocess.run(
                [
                    sys.executable,
                    str(RUNTIME_INDEX_SCRIPT),
                    "--repo",
                    str(REPO),
                    "--strength-profile",
                    str(DEFAULT_PROFILE),
                    "--output",
                    str(index_path),
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
            )

            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--repo",
                    str(REPO),
                    "--base-profile",
                    str(DEFAULT_PROFILE),
                    "--runtime-index",
                    str(index_path),
                    "--output",
                    str(output_path),
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
            )

            profile = json.loads(output_path.read_text(encoding="utf-8"))

        self.assertEqual("brawlstar.strength_profile.v1", profile["schema"])
        self.assertNotIn("fallback" + "_policy", profile)
        self.assertEqual("ikaoss11-july-2026-screenshot", profile["source"]["base_profile_id"])
        self.assertEqual(27, len(profile["profiles"]["maps"]))
        backyard = profile["profiles"]["maps"]["Brawl Ball/Backyard Bowl"]
        self.assertEqual("map", backyard["scope"])
        self.assertEqual("Brawl Ball", backyard["mode"])
        self.assertEqual("Backyard Bowl", backyard["map"])
        self.assertEqual(104, sum(len(names) for names in backyard["tiers"].values()))
        self.assertIn("Damian", backyard["tiers"]["S"])

        bridge = profile["profiles"]["maps"]["Heist/Bridge Too Far"]
        self.assertEqual(104, sum(len(names) for names in bridge["tiers"].values()))
        self.assertNotIn("Emz", bridge["tiers"]["S"])
        self.assertIn("Emz", bridge["tiers"]["D"])


if __name__ == "__main__":
    unittest.main()
