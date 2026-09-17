#!/usr/bin/env python3
"""Tests for audit_capability_edge_coverage."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from audit_capability_edge_coverage import audit_brawler, audit_repo, extract_yaml_block  # noqa: E402

PAGE_FULL = """# Fake Brawler

```yaml
bp_brawler_profile:
  capability_vector:
    anti_aggro: "high as shield-plus-knockback resource; reworked Knockback Spirit gadget knockback"
  conditional_matchups:
    - target: ["Fang", "Mortis"]
      direction: "subject_favored"
      mechanism: "Super shield knockback stops single-lane engage"
      active_when: "Super available"
      fails_when: "diver baits shield"
      bp_use: "anti_aggro_resource_check"
```
"""

PAGE_NO_EDGES = """# Quiet Brawler

```yaml
bp_brawler_profile:
  capability_vector:
    anti_aggro: "low"
```
"""

ATOMS = {
    "Fake": [
        {"id": "gadget_knockback", "keywords": ["Knockback Spirit"]},
        {"id": "homing_spirits", "keywords": ["homing spirit"]},
    ],
}


class CapabilityEdgeCoverageTests(unittest.TestCase):
    def test_yaml_block_extraction(self):
        self.assertIn("capability_vector", extract_yaml_block(PAGE_FULL))

    def test_atom_in_capability_but_not_edges_is_seed(self):
        result = audit_brawler(extract_yaml_block(PAGE_FULL), ATOMS["Fake"])
        by_id = {r["atom"]: r for r in result["atoms"]}
        self.assertTrue(by_id["gadget_knockback"]["capability_covered"])
        self.assertFalse(by_id["gadget_knockback"]["edge_covered"])
        self.assertIn("gadget_knockback", result["review_seeds"])
        self.assertTrue(result["conditional_matchups_section_present"])

    def test_atom_covered_in_edge_is_not_seed(self):
        page = PAGE_FULL.replace(
            "mechanism: \"Super shield knockback stops single-lane engage\"",
            "mechanism: \"Knockback Spirit gadget knockback chases divers\"",
        )
        result = audit_brawler(extract_yaml_block(page), ATOMS["Fake"])
        by_id = {r["atom"]: r for r in result["atoms"]}
        self.assertTrue(by_id["gadget_knockback"]["edge_covered"])
        self.assertNotIn("gadget_knockback", result["review_seeds"])
        self.assertTrue(by_id["gadget_knockback"]["matching_edges"])

    def test_missing_capability_coverage_is_fold_gap(self):
        result = audit_brawler(extract_yaml_block(PAGE_FULL), ATOMS["Fake"])
        by_id = {r["atom"]: r for r in result["atoms"]}
        self.assertFalse(by_id["homing_spirits"]["capability_covered"])
        self.assertIn("homing_spirits", result["fold_gaps"])

    def test_atom_in_build_switches_counts_as_folded(self):
        page = PAGE_FULL.replace(
            'bp_brawler_profile:\n  capability_vector:',
            'bp_brawler_profile:\n  build_switches:\n    - build: "x"\n      changes_capabilities:\n        - "homing spirit support"\n  capability_vector:',
        )
        result = audit_brawler(extract_yaml_block(page), ATOMS["Fake"])
        by_id = {r["atom"]: r for r in result["atoms"]}
        self.assertTrue(by_id["homing_spirits"]["capability_covered"])
        self.assertNotIn("homing_spirits", result["fold_gaps"])

    def test_page_without_matchups_reports_absence(self):
        result = audit_brawler(extract_yaml_block(PAGE_NO_EDGES), ATOMS["Fake"])
        self.assertFalse(result["conditional_matchups_section_present"])
        self.assertEqual(len(result["review_seeds"]), len(ATOMS["Fake"]))

    def test_repo_audit_reports_missing_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Fake.md").write_text(PAGE_FULL, encoding="utf-8")
            report, missing = audit_repo(root, ATOMS, brawlers=["Fake", "Ghost"])
            self.assertIn("Fake", report)
            self.assertIn("Ghost", missing)
            payload = json.dumps(report)
            self.assertIn("review_seeds", payload)


if __name__ == "__main__":
    unittest.main()
