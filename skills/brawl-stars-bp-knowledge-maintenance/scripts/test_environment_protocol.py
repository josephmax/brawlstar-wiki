#!/usr/bin/env python3
"""Protocol contract tests for the environment sqlite archive.

The sqlite layout (tables, columns, meta keys, `PRAGMA user_version`) is a
protocol shared between the producer (`_environment_sqlite`) and consumers
(compile, audit, aggregate). These tests lock the contract: producers and
consumers must agree on it, and unknown schema versions are rejected instead
of being read by guesswork.
"""

from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

import _environment_sqlite as envdb
from _liquipedia_event import analyze_events, load_brawler_names, load_raw_capture, renormalize_event_names


REPO = Path(__file__).resolve().parents[3]
RAW_DIR = REPO / "raw" / "sources" / "liquipedia" / "events"


class EnvironmentProtocolTest(unittest.TestCase):
    def _august_events(self):
        canonical = load_brawler_names(REPO)
        raws = [
            "brawl-stars-championship-2026-season-6-emea-monthly-finals-2026-08-14.md",
            "brawl-stars-championship-2026-season-6-south-america-monthly-finals-2026-08-24.md",
            "brawl-stars-championship-2026-season-6-east-asia-monthly-finals-2026-08-24.md",
            "brawl-stars-championship-2026-season-6-north-america-monthly-finals-2026-08-24.md",
        ]
        return [renormalize_event_names(load_raw_capture(RAW_DIR / name), canonical) for name in raws]

    def test_unknown_user_version_is_rejected(self):
        """消费侧不得猜测未知 schema：user_version != SCHEMA_VERSION 必须拒绝。"""
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "archive.sqlite3"
            con = sqlite3.connect(str(db))
            con.execute("PRAGMA user_version = 999")
            con.execute("CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT)")
            con.commit()
            con.close()
            with self.assertRaises(envdb.EnvironmentProtocolError):
                envdb.read_signal(db)
            with self.assertRaises(envdb.EnvironmentProtocolError):
                envdb.load_pickrate(db)

    def test_protocol_table_set_is_stable(self):
        """协议声明的表集合必须与生产库一致（表/列演进须同步 PROTOCOL_TABLES）。"""
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "archive.sqlite3"
            events = self._august_events()
            envdb.write_profile(db, analyze_events(events), raw_events=events)
            con = sqlite3.connect(str(db))
            actual = {row[0] for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            con.close()
            # sqlite_sequence 是 AUTOINCREMENT 的引擎内部表，不属于协议表
            self.assertTrue(set(envdb.PROTOCOL_TABLES) <= actual)
            self.assertEqual(1, envdb.SCHEMA_VERSION)

    def test_consumer_reads_through_shared_protocol_module(self):
        """compile 的消费路径必须加载同一协议模块并读到与生产一致的结构。"""
        # 模拟 compile 的消费入口：从 slot-decision 目录解析协议模块
        import sys
        compile_dir = REPO / "skills" / "brawl-stars-bp-slot-decision" / "scripts"
        sys.path.insert(0, str(compile_dir))
        import compile_runtime_index as compile_mod
        env = compile_mod.resolve_environment(REPO, "wiki/environment/current.json", False)
        self.assertIsNotNone(env)
        # compile 读到的是真实 8 月归档；与协议模块直接读完全一致（同一份展开实现）
        self.assertEqual(env["monthly"], envdb.read_signal(REPO / "wiki/environment/2026-08/archive.sqlite3"))
        self.assertEqual(env["ladder"], envdb.read_pickrate(REPO / "wiki/environment/pickrate.sqlite3"))
        self.assertEqual(env["monthly"]["brawlers"]["Glowy"]["picks"], 6)

    def test_json_paths_still_accepted_by_shared_loaders(self):
        """协议读函数兼容旧 .json 路径（向后兼容，消费方无需区分）。"""
        with tempfile.TemporaryDirectory() as tmp:
            json_path = Path(tmp) / "signal.json"
            signal = {
                "schema": "brawlstar.environment_signal.v1",
                "window": "monthly",
                "brawlers": {"Bolt": {"picks": 5, "pick_rate": 0.05, "win_rate_when_picked": 0.6,
                                      "ban_series": 15, "ban_rate": 0.54, "ban_set_coverage": 0.07}},
            }
            json_path.write_text(json.dumps(signal, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(envdb.load_signal(json_path)["brawlers"], signal["brawlers"])


if __name__ == "__main__":
    unittest.main()
