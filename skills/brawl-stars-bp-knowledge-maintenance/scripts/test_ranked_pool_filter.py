#!/usr/bin/env python3
"""Ranked-pool filter tests for fetch_brawlplanet_pickrate.build_signal."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from fetch_brawlplanet_pickrate import build_signal, load_ranked_pool, pool_key

MANIFEST = {
    "schema": "brawlstar.ranked_pool_manifest.v1",
    "season": 48,
    "maps": [
        {"map": "Safe Zone", "mode": "Heist"},
        {"map": "Safe(r) Zone", "mode": "Heist"},
        {"map": "Dry Season", "mode": "Bounty"},
    ],
}

# Two pool+active maps, one pool map flagged inactive by the source, one
# out-of-pool ladder map (Snake Prairie analog), one future-brawler carrier.
PICKRATE = {
    "safezone_heist": {
        "map": "Safe Zone", "mode": "heist", "modeFormatted": "Heist",
        "match_count": 100, "active": True, "latest_match_time": 1,
        "individual": [{"brawler": "GRIFF", "wr": 50.0, "ur": 10.0, "sr": 5.0}],
    },
    "saferrzone_heist": {
        "map": "Safe(r) Zone", "mode": "heist", "modeFormatted": "Heist",
        "match_count": 300, "active": True, "latest_match_time": 2,
        "individual": [{"brawler": "GRIFF", "wr": 52.0, "ur": 20.0, "sr": 6.0}],
    },
    "dryseason_bounty": {
        "map": "Dry Season", "mode": "bounty", "modeFormatted": "Bounty",
        "match_count": 200, "active": False, "latest_match_time": 3,
        "individual": [{"brawler": "GRIFF", "wr": 48.0, "ur": 15.0, "sr": 4.0}],
    },
    "snakeprairie_bounty": {
        "map": "Snake Prairie", "mode": "bounty", "modeFormatted": "Bounty",
        "match_count": 400, "active": True, "latest_match_time": 4,
        "individual": [{"brawler": "GRIFF", "wr": 60.0, "ur": 30.0, "sr": 9.0}],
    },
    # Raw source mode spells multi-word modes without spaces; the manifest uses
    # display form ("Brawl Ball"). Regression: raw "brawlball" must still match.
    "beachball_brawlball": {
        "map": "Beach Ball", "mode": "brawlball", "modeFormatted": "Brawl Ball",
        "match_count": 500, "active": True, "latest_match_time": 5,
        "individual": [{"brawler": "GRIFF", "wr": 55.0, "ur": 25.0, "sr": 8.0}],
    },
}

BRAWLERS = [{"name": "Griff", "rarity": "epic", "future": False}]


class RankedPoolFilterTest(unittest.TestCase):
    def test_pool_key_distinguishes_punctuation_variants(self):
        self.assertNotEqual(pool_key("Safe Zone", "Heist"), pool_key("Safe(r) Zone", "Heist"))
        self.assertEqual(pool_key("Dry Season ", "Bounty"), pool_key("dry season", "bounty"))
        # Raw source modes drop spaces; display form keeps them.
        self.assertEqual(pool_key("X", "brawlball"), pool_key("X", "Brawl Ball"))
        self.assertEqual(pool_key("X", "gemgrab"), pool_key("X", "Gem Grab"))

    def test_filtered_global_counts_only_pool_active_maps(self):
        signal = build_signal(PICKRATE, BRAWLERS, {"Griff"}, MANIFEST)
        # Match-weighted over Safe Zone (100) + Safe(r) Zone (300); Dry Season is
        # in-pool but inactive, Snake Prairie is out-of-pool.
        self.assertEqual(signal["global"]["Griff"], {"use_rate": 17.5, "win_rate": 51.5})

    def test_filtered_per_map_keeps_pool_rows_only_with_label(self):
        signal = build_signal(PICKRATE, BRAWLERS, {"Griff"}, MANIFEST)
        self.assertEqual(sorted(signal["per_map"]), ["dryseason_bounty", "saferrzone_heist", "safezone_heist"])
        self.assertTrue(all(row.get("ranked_pool") is True for row in signal["per_map"].values()))

    def test_filtered_summary_reports_exclusions_and_missing(self):
        signal = build_signal(PICKRATE, BRAWLERS, {"Griff"}, MANIFEST)
        summary = signal["summary"]
        self.assertEqual(summary["ranked_pool"]["filtered"], True)
        self.assertEqual(summary["ranked_pool"]["season"], 48)
        self.assertEqual(summary["ranked_pool"]["pool_map_count"], 3)
        self.assertEqual(summary["ranked_pool"]["pool_maps_in_source"], 3)
        self.assertEqual(summary["ranked_pool"]["pool_maps_missing_from_source"], [])
        self.assertEqual(summary["excluded_maps"], [
            {"map": "Beach Ball", "mode": "Brawl Ball", "reason": "not_in_ranked_pool"},
            {"map": "Snake Prairie", "mode": "Bounty", "reason": "not_in_ranked_pool"},
        ])
        # Source-wide audit counters still describe the full ladder payload.
        self.assertEqual(summary["map_entries"], 5)
        self.assertEqual(summary["active_maps"], 4)

    def test_stale_manifest_warns_via_missing_list(self):
        stale = {**MANIFEST, "maps": MANIFEST["maps"] + [{"map": "Retired Map", "mode": "Heist"}]}
        signal = build_signal(PICKRATE, BRAWLERS, {"Griff"}, stale)
        self.assertEqual(
            signal["summary"]["ranked_pool"]["pool_maps_missing_from_source"],
            ["Retired Map"],
        )

    def test_unfiltered_keeps_ladder_wide_rows(self):
        signal = build_signal(PICKRATE, BRAWLERS, {"Griff"}, None)
        self.assertEqual(len(signal["per_map"]), 5)
        self.assertNotIn("ranked_pool", signal["summary"])
        self.assertTrue(all("ranked_pool" not in row for row in signal["per_map"].values()))

    def test_load_ranked_pool_rejects_missing_and_invalid(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(SystemExit):
                load_ranked_pool(Path(tmp) / "absent.json")
            bad = Path(tmp) / "bad.json"
            bad.write_text(json.dumps({"schema": "other.v9", "maps": []}), encoding="utf-8")
            with self.assertRaises(SystemExit):
                load_ranked_pool(bad)


if __name__ == "__main__":
    unittest.main()
