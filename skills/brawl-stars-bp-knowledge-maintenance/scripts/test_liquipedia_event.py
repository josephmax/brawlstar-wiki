#!/usr/bin/env python3
"""Regression tests for deterministic Liquipedia event parsing and analysis."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from _liquipedia_event import (
    analyze_events,
    load_brawler_names,
    load_raw_capture,
    load_raw_wikitext,
    parse_event_wikitext,
    parse_mediawiki_query,
    render_raw_capture,
)


WIKITEXT = r"""
{{DISPLAYTITLE:Example Monthly Finals}}
{{Infobox league
|name=Example Monthly Finals
|date=2026-07-12
|format=Single-elimination
|team_number=4
}}
{{Bracket
|R1M1={{Match
  |date=2026-07-12
  |opponent1={{TeamOpponent|Blue Team}}
  |opponent2={{TeamOpponent|Red Team}}
  |t1b1=Surge|t1b2=Max|t2b1=Max|t2b2=Starr Nova
  |mapveto={{MapVeto|firstpick=2|t1map1=Test Map|t2map1=Other Map}}
  |map1={{Map|map=Test Map|maptype=Gem Grab|score1=2|score2=1
    |t1c1=Meeple|t1c2=Max|t1c3=Ruffs|t2c1=Lou|t2c2=Ash|t2c3=Stu
    |t1b1=Surge|t1b2=8-bit|t1b3=Max|t2b1=Surge|t2b2=Lumi|t2b3=Meg}}
  |map2={{Map|map=Other Map|maptype=Knockout|winner=skip}}
  |mvp=Player One
}}
|R2M1={{Match
  |opponent1={{TeamOpponent|Blue Team|score=W}}
  |opponent2={{TeamOpponent|No Show|score=FF}}
  |t1b1=Damian|t1b2=8-bit|t2b1=Otis|t2b2=Max
  |mapveto={{MapVeto|firstpick=1}}
  |map1={{Map|map=Test Map|maptype=Gem Grab|winner=skip}}
}}
}}
"""

ROOT = Path(__file__).resolve().parents[3]


class LiquipediaEventTest(unittest.TestCase):
    def test_parse_query_api_response(self) -> None:
        payload = {
            "query": {
                "pages": [{
                    "title": "Example/Page",
                    "revisions": [{
                        "revid": 42,
                        "timestamp": "2026-07-13T04:14:39Z",
                        "slots": {"main": {"content": WIKITEXT}},
                    }],
                }]
            }
        }
        parsed = parse_mediawiki_query(payload)
        self.assertEqual(parsed["revision_id"], 42)
        self.assertEqual(parsed["page_title"], "Example/Page")
        self.assertIn("Example Monthly Finals", parsed["wikitext"])

    def test_parse_semantics_and_forfeit(self) -> None:
        event = parse_event_wikitext(
            WIKITEXT,
            source={"page_title": "Example/Page", "revision_id": 42},
            canonical_names={"8bit": "8-Bit", "starrnova": "Starr Nova"},
        )
        self.assertEqual(event["event"]["name"], "Example Monthly Finals")
        self.assertEqual(event["summary"]["series"], 2)
        self.assertEqual(event["summary"]["played_series"], 1)
        self.assertEqual(event["summary"]["played_sets"], 1)
        self.assertEqual(event["summary"]["forfeits"], 1)
        self.assertEqual(event["summary"]["champion"], "Blue Team")
        played = event["matches"][0]
        self.assertEqual(played["map_veto_first_pick_team"], 2)
        self.assertIsNone(played["sets"][0]["draft_first_pick_team"])
        self.assertEqual(played["sets"][0]["winner_team"], "Blue Team")
        self.assertEqual(played["sets"][0]["picks"]["team1"][0], "Meeple")
        self.assertEqual(event["matches"][1]["status"], "forfeit")

    def test_observation_profile_has_atomic_metrics_without_tiers(self) -> None:
        event = parse_event_wikitext(WIKITEXT, source={}, canonical_names={"8bit": "8-Bit"})
        profile = analyze_events([event], generated_at="2026-07-13T00:00:00Z")
        self.assertEqual(profile["schema"], "tournament_observation_profile.v1")
        global_rows = {row["brawler"]: row for row in profile["scopes"]["global"]}
        self.assertEqual(global_rows["Meeple"]["pick_sets"], 1)
        self.assertEqual(global_rows["Meeple"]["set_wins_when_picked"], 1)
        self.assertEqual(global_rows["Surge"]["local_ban_nominations"], 2)
        self.assertEqual(global_rows["Surge"]["local_ban_set_coverage"], 1)
        self.assertNotIn("Damian", global_rows)  # appears only in the forfeited series
        metric_keys = {key for row in global_rows.values() for key in row}
        self.assertNotIn("tier", metric_keys)
        self.assertNotIn("meta_score", metric_keys)
        self.assertNotIn("score", global_rows["Meeple"])

    def test_raw_capture_round_trip(self) -> None:
        event = parse_event_wikitext(WIKITEXT, source={"page_title": "Example/Page"}, canonical_names={})
        raw = render_raw_capture(event, WIKITEXT, captured_at="2026-07-13T00:00:00Z")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "event.md"
            path.write_text(raw, encoding="utf-8")
            loaded = load_raw_capture(path)
        self.assertEqual(loaded["event"]["name"], "Example Monthly Finals")
        self.assertEqual(loaded["summary"]["played_sets"], 1)

    def test_july_event_capture_regressions(self) -> None:
        cases = [
            ("brawl-stars-championship-2026-season-5-emea-monthly-finals-2026-07-13.md", 7, 24, 0, "FUT Esports"),
            ("brawl-stars-championship-2026-season-5-south-america-monthly-finals-2026-07-13.md", 6, 24, 1, "RED Canids"),
        ]
        canonical_names = load_brawler_names(ROOT)
        for filename, played_series, played_sets, forfeits, champion in cases:
            path = ROOT / "raw/sources/liquipedia/events" / filename
            captured = load_raw_capture(path)
            reparsed = parse_event_wikitext(
                load_raw_wikitext(path),
                source=captured["source"],
                canonical_names=canonical_names,
            )
            self.assertEqual(reparsed["summary"]["played_series"], played_series)
            self.assertEqual(reparsed["summary"]["played_sets"], played_sets)
            self.assertEqual(reparsed["summary"]["forfeits"], forfeits)
            self.assertEqual(reparsed["summary"]["champion"], champion)


if __name__ == "__main__":
    unittest.main()
