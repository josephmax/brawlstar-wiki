#!/usr/bin/env python3
"""SQLite archive storage round-trip tests for the environment layer."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from _environment_sqlite import (
    read_pickrate,
    read_profile,
    read_raw_events,
    read_signal,
    write_pickrate,
    write_profile,
    write_signal,
)
from _liquipedia_event import load_brawler_names, load_raw_capture, renormalize_event_names


REPO = Path(__file__).resolve().parents[3]
RAW_DIR = REPO / "raw" / "sources" / "liquipedia" / "events"


class EnvironmentSqliteTest(unittest.TestCase):
    def _august_raw_events(self):
        canonical = load_brawler_names(REPO)
        raws = [
            "brawl-stars-championship-2026-season-6-emea-monthly-finals-2026-08-14.md",
            "brawl-stars-championship-2026-season-6-south-america-monthly-finals-2026-08-24.md",
            "brawl-stars-championship-2026-season-6-east-asia-monthly-finals-2026-08-24.md",
            "brawl-stars-championship-2026-season-6-north-america-monthly-finals-2026-08-24.md",
        ]
        return [renormalize_event_names(load_raw_capture(RAW_DIR / name), canonical) for name in raws]

    def test_profile_and_raw_events_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "archive.sqlite3"
            events = self._august_raw_events()
            # 从解析出的 raw 事件重建 profile（与 analyze 相同的聚合逻辑）
            from _liquipedia_event import analyze_events
            profile = analyze_events(events)
            write_profile(db, profile, raw_events=events)
            back = read_profile(db)
            self.assertEqual(back["source_events"], profile["source_events"])
            self.assertEqual(back["scopes"], profile["scopes"])
            self.assertEqual(back["generated_at"], profile["generated_at"])
            raw_back = read_raw_events(db)
            self.assertEqual(
                sorted(json.dumps(x, sort_keys=True, ensure_ascii=False) for x in events),
                sorted(json.dumps(x, sort_keys=True, ensure_ascii=False) for x in raw_back),
            )
            # 行列数据可直接 SQL 查询
            import sqlite3
            con = sqlite3.connect(str(db))
            rows = con.execute(
                "SELECT brawler, COUNT(*) c FROM set_pick sp JOIN \"set\" s ON sp.set_id=s.id "
                "WHERE s.map='Crystal Arcade' GROUP BY brawler ORDER BY c DESC LIMIT 1"
            ).fetchall()
            con.close()
            self.assertEqual("Griff", rows[0][0])

    def test_signal_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "archive.sqlite3"
            events = self._august_raw_events()
            from _liquipedia_event import analyze_events
            profile = analyze_events(events)
            write_profile(db, profile, raw_events=events)
            signal = {
                "schema": "brawlstar.environment_signal.v1",
                "profile_id": "monthly-liquipedia-pickban",
                "window": "monthly",
                "rank_floor": "legendary_plus_approximation",
                "source": {"kind": "liquipedia-monthly-finals", "played_series": 28, "played_sets": 110},
                "captured_at": "2026-08-24T00:00:00Z",
                "brawlers": {"Glowy": {"picks": 6, "pick_rate": 0.0545, "win_rate_when_picked": 0.3333,
                                       "ban_series": 1, "ban_rate": 0.0357, "ban_set_coverage": 0.0182}},
            }
            write_signal(db, signal)
            back = read_signal(db)
            self.assertEqual(back["brawlers"], signal["brawlers"])
            self.assertEqual(back["source"], signal["source"])
            self.assertEqual(back["window"], "monthly")

    def test_pickrate_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "pickrate.sqlite3"
            pickrate = {
                "schema": "brawlstar.environment_signal_pickrate.v1",
                "window": "rolling_10_weeks",
                "rank_floor": "legendary_plus",
                "source": {"kind": "brawl-planet"},
                "fetched_at": "2026-08-24T00:00:00Z",
                "summary": {"brawlers_with_sample": 2},
                "global": {"Bolt": {"use_rate": 6.6, "win_rate": 57.32}},
                "per_map": {
                    "safezone_heist": {
                        "map": "Safe Zone", "mode": "Heist", "match_count": 90808,
                        "active": True, "latest_match_time": 1740387937,
                        "individual": {"Bolt": {"use_rate": 7.1, "win_rate": 60.0, "star_player_rate": 1.2}},
                    },
                    "safe(r)zone_heist": {
                        "map": "Safe(r) Zone", "mode": "Heist", "match_count": 100,
                        "active": False, "latest_match_time": 1740000000,
                        "individual": {"Brock": {"use_rate": 9.9, "win_rate": 50.0, "star_player_rate": 0.1}},
                    },
                },
            }
            write_pickrate(db, pickrate)
            back = read_pickrate(db)
            self.assertEqual(back["global"], pickrate["global"])
            self.assertEqual(sorted(back["per_map"]), sorted(pickrate["per_map"]))
            for key in pickrate["per_map"]:
                self.assertEqual(back["per_map"][key], pickrate["per_map"][key])
            # Safe Zone / Safe(r) Zone 两个 GCS 变体必须都保留
            self.assertIn("safe(r)zone_heist", back["per_map"])


if __name__ == "__main__":
    unittest.main()
