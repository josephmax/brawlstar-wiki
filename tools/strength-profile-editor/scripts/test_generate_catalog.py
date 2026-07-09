import importlib.util
import json
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO / "tools/strength-profile-editor/scripts/generate_catalog.py"


def load_module():
    spec = importlib.util.spec_from_file_location("generate_catalog", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GenerateCatalogTest(unittest.TestCase):
    def test_build_catalog_from_wiki_sources(self):
        module = load_module()

        catalog = module.build_catalog(REPO)

        self.assertEqual(catalog["schema"], "brawlstar.strength_profile.catalog.v1")
        self.assertEqual(catalog["tiers"], ["S", "A", "B", "C", "D", "E"])
        self.assertEqual(len(catalog["brawlers"]), 104)
        self.assertIn("Brawl Ball", catalog["modes"])
        self.assertIn("Heist", catalog["modes"])
        self.assertIn(
            {"name": "Backyard Bowl", "mode": "Brawl Ball"},
            catalog["maps"],
        )

        by_name = {brawler["name"]: brawler for brawler in catalog["brawlers"]}
        self.assertTrue(by_name["Brock"]["image_url"].startswith("https://cdn.brawlify.com/brawlers/borderless/"))
        self.assertTrue(by_name["Ziggy"]["image_url"].startswith("https://cdn.brawlify.com/brawlers/borderless/"))
        self.assertEqual(sum(1 for brawler in catalog["brawlers"] if brawler["image_url"]), 104)

        self.assertEqual(catalog["alias_index"]["506"], "Edgar")
        self.assertEqual(catalog["alias_index"]["64"], "Cordelius")
        self.assertEqual(catalog["alias_index"]["张雪峰"], "Bolt")
        self.assertEqual(catalog["ambiguous"]["猴子"], ["Brock", "Mico"])

    def test_write_catalog_round_trips_as_json(self):
        module = load_module()
        out_path = REPO / "tools/strength-profile-editor/data/catalog.test.json"

        try:
            module.write_catalog(REPO, out_path)
            parsed = json.loads(out_path.read_text(encoding="utf-8"))
        finally:
            if out_path.exists():
                out_path.unlink()

        self.assertEqual(parsed["schema"], "brawlstar.strength_profile.catalog.v1")
        self.assertEqual(len(parsed["brawlers"]), 104)


if __name__ == "__main__":
    unittest.main()
