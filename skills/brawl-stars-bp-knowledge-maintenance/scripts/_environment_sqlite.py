#!/usr/bin/env python3
"""SQLite storage for the environment archive (row/column, migration-friendly).

The environment/observation data (tournament observation profiles, monthly
signals, Legendary+ pickrate snapshots) is archived as single-file SQLite
databases instead of nested JSON, so other applications can read it with plain
SQL and the vault scripts hydrate it into the same Python structures on load.

Layout:
  wiki/environment/<YYYY-MM>/archive.sqlite3   # profile + monthly signal
  wiki/environment/pickrate.sqlite3            # rolling Legendary+ snapshot

The `meta` table keeps schema version and provenance. Reads expand the rows
back into the exact dict shapes the JSON consumers used, so switching a path
from `.json` to `.sqlite3` is transparent for existing callers.
"""

from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1

# 协议表集合：契约测试校验库内表与此一致；消费侧依赖这些表名/列名。
PROTOCOL_TABLES = (
    "meta",
    "event",
    "series",
    "series_ban",
    "set",
    "set_pick",
    "set_ban",
    "metric_global",
    "metric_mode",
    "metric_map",
    "signal_brawler",
    "ladder_global",
    "ladder_per_map",
)

META_KEY_PREFIXES = ("profile.", "signal.", "pickrate.")


class EnvironmentProtocolError(ValueError):
    """Raised when an archive database does not match the protocol contract
    (unknown `PRAGMA user_version`). Consumers must not read unknown schemas:
    regenerate the archive or upgrade the protocol instead of guessing."""

# ---------------------------------------------------------------- schema ----

_DDL = """
CREATE TABLE IF NOT EXISTS meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS event (
  region TEXT PRIMARY KEY,
  name TEXT, date TEXT, format TEXT, team_number INTEGER,
  page_title TEXT, revision_id INTEGER, revision_timestamp TEXT,
  site TEXT, url TEXT, api_url TEXT,
  series INTEGER, played_series INTEGER, played_sets INTEGER,
  forfeits INTEGER, champion TEXT, runner_up TEXT
);
CREATE TABLE IF NOT EXISTS series (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  event_region TEXT NOT NULL REFERENCES event(region),
  match_id TEXT, team1 TEXT, team2 TEXT,
  score1 INTEGER, score2 INTEGER, status TEXT, mvp TEXT,
  round INTEGER, match_no INTEGER, date TEXT, vod TEXT,
  winner_side INTEGER, winner_team TEXT, map_veto_first_pick_team INTEGER
);
CREATE TABLE IF NOT EXISTS series_ban (
  series_id INTEGER NOT NULL REFERENCES series(id),
  side INTEGER NOT NULL, slot INTEGER NOT NULL, brawler TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "set" (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  series_id INTEGER NOT NULL REFERENCES series(id),
  set_no INTEGER, map TEXT, mode TEXT,
  score1 INTEGER, score2 INTEGER, winner_side INTEGER, winner_team TEXT,
  draft_first_pick_team INTEGER
);
CREATE TABLE IF NOT EXISTS set_pick (
  set_id INTEGER NOT NULL REFERENCES "set"(id),
  side INTEGER NOT NULL, slot INTEGER NOT NULL, brawler TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS set_ban (
  set_id INTEGER NOT NULL REFERENCES "set"(id),
  side INTEGER NOT NULL, slot INTEGER NOT NULL, brawler TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS metric_global (
  brawler TEXT PRIMARY KEY,
  pick_sets INTEGER, set_wins_when_picked INTEGER,
  local_ban_nominations INTEGER, local_ban_set_coverage INTEGER,
  global_ban_nominations INTEGER, global_ban_series_coverage INTEGER
);
CREATE TABLE IF NOT EXISTS metric_mode (
  mode TEXT NOT NULL, brawler TEXT NOT NULL,
  pick_sets INTEGER, set_wins_when_picked INTEGER,
  local_ban_nominations INTEGER, local_ban_set_coverage INTEGER,
  global_ban_nominations INTEGER, global_ban_series_coverage INTEGER,
  PRIMARY KEY (mode, brawler)
);
CREATE TABLE IF NOT EXISTS metric_map (
  map TEXT NOT NULL, mode TEXT NOT NULL, brawler TEXT NOT NULL,
  pick_sets INTEGER, set_wins_when_picked INTEGER,
  local_ban_nominations INTEGER, local_ban_set_coverage INTEGER,
  global_ban_nominations INTEGER, global_ban_series_coverage INTEGER,
  PRIMARY KEY (map, brawler)
);
CREATE TABLE IF NOT EXISTS signal_brawler (
  brawler TEXT PRIMARY KEY,
  picks INTEGER, pick_rate REAL, win_rate_when_picked REAL,
  ban_series INTEGER, ban_rate REAL, ban_set_coverage REAL
);
CREATE TABLE IF NOT EXISTS ladder_global (
  brawler TEXT PRIMARY KEY, use_rate REAL, win_rate REAL
);
CREATE TABLE IF NOT EXISTS ladder_per_map (
  source_key TEXT NOT NULL,
  map TEXT NOT NULL, mode TEXT NOT NULL, match_count INTEGER, active INTEGER,
  latest_match_time INTEGER,
  brawler TEXT NOT NULL, use_rate REAL, win_rate REAL, star_player_rate REAL,
  PRIMARY KEY (source_key, brawler)
);
"""


def connect(db_path: str | Path) -> sqlite3.Connection:
    """Open (creating if needed) an archive database under the protocol.

    Version guard: an existing file whose `PRAGMA user_version` is neither 0
    (fresh) nor `SCHEMA_VERSION` is rejected — a consumer must not guess an
    unknown schema layout. A fresh file is stamped with `SCHEMA_VERSION`.
    """
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    con = sqlite3.connect(str(path))
    con.row_factory = sqlite3.Row
    if exists:
        existing = con.execute("PRAGMA user_version").fetchone()[0]
        if existing not in (0, SCHEMA_VERSION):
            con.close()
            raise EnvironmentProtocolError(
                f"{path}: archive user_version={existing} != protocol {SCHEMA_VERSION}; "
                "regenerate the archive or upgrade the protocol"
            )
    con.execute(f"PRAGMA user_version = {int(SCHEMA_VERSION)}")
    con.executescript(_DDL)
    return con


# ------------------------------------------------------------------ write ----

def _set_meta(con: sqlite3.Connection, key: str, value: Any) -> None:
    con.execute(
        "INSERT OR REPLACE INTO meta (key, value) VALUES (?, ?)",
        (key, json.dumps(value, ensure_ascii=False)),
    )


def _write_event_from_source(con: sqlite3.Connection, row: dict[str, Any]) -> None:
    con.execute(
        "INSERT OR REPLACE INTO event (region, name, date, page_title, revision_id, series, played_series, played_sets, forfeits, champion, runner_up) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (
            row.get("region"),
            row.get("name"),
            row.get("date"),
            row.get("page_title"),
            row.get("revision_id"),
            row.get("series"),
            row.get("played_series"),
            row.get("played_sets"),
            row.get("forfeits"),
            row.get("champion"),
            row.get("runner_up"),
        ),
    )


def _write_series_tables(con: sqlite3.Connection, event: dict[str, Any]) -> None:
    """Write per-set rows from a parsed raw event (matches/sets live only in raw
    captures, not in the aggregated profile; this gives external apps SQL-queryable
    row/column draft data)."""
    ev = event["event"]
    con.execute("DELETE FROM series_ban WHERE series_id IN (SELECT id FROM series WHERE event_region = ?)", (ev.get("region"),))
    con.execute("DELETE FROM set_ban WHERE set_id IN (SELECT id FROM \"set\" WHERE series_id IN (SELECT id FROM series WHERE event_region = ?))", (ev.get("region"),))
    con.execute("DELETE FROM set_pick WHERE set_id IN (SELECT id FROM \"set\" WHERE series_id IN (SELECT id FROM series WHERE event_region = ?))", (ev.get("region"),))
    con.execute("DELETE FROM \"set\" WHERE series_id IN (SELECT id FROM series WHERE event_region = ?)", (ev.get("region"),))
    con.execute("DELETE FROM series WHERE event_region = ?", (ev.get("region"),))
    for match in event.get("matches") or []:
        row = con.execute(
            "INSERT INTO series (event_region, match_id, team1, team2, score1, score2, status, mvp, round, match_no, date, vod, winner_side, winner_team, map_veto_first_pick_team) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                ev.get("region"),
                match.get("match_id"),
                (match.get("teams") or [None, None])[0],
                (match.get("teams") or [None, None])[1],
                (match.get("series_score") or [None, None])[0],
                (match.get("series_score") or [None, None])[1],
                match.get("status"),
                match.get("mvp"),
                match.get("round"),
                match.get("match"),
                match.get("date"),
                match.get("vod"),
                match.get("winner_side"),
                match.get("winner_team"),
                match.get("map_veto_first_pick_team"),
            ),
        )
        series_id = row.lastrowid
        for side_no in (1, 2):
            for idx, name in enumerate((match.get("global_bans") or {}).get(f"team{side_no}") or [], start=1):
                con.execute(
                    "INSERT INTO series_ban VALUES (?,?,?,?)",
                    (series_id, side_no, idx, name),
                )
        for set_no, item in enumerate(match.get("sets") or [], start=1):
            game_score = item.get("game_score") or []
            set_row = con.execute(
                "INSERT INTO \"set\" (series_id, set_no, map, mode, score1, score2, winner_side, winner_team, draft_first_pick_team) "
                "VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    series_id,
                    item.get("set_no", set_no),
                    item.get("map"),
                    item.get("mode"),
                    (game_score or [None, None])[0],
                    (game_score or [None, None])[1],
                    item.get("winner_side"),
                    item.get("winner_team"),
                    item.get("draft_first_pick_team"),
                ),
            )
            set_id = set_row.lastrowid
            for side_no in (1, 2):
                for idx, name in enumerate((item.get("picks") or {}).get(f"team{side_no}") or [], start=1):
                    con.execute("INSERT INTO set_pick VALUES (?,?,?,?)", (set_id, side_no, idx, name))
                for idx, name in enumerate((item.get("local_bans") or {}).get(f"team{side_no}") or [], start=1):
                    con.execute("INSERT INTO set_ban VALUES (?,?,?,?)", (set_id, side_no, idx, name))


def _write_metric_rows(con: sqlite3.Connection, table: str, rows: list[dict[str, Any]], extra: tuple[str, ...] = ()) -> None:
    for row in rows:
        values = (*extra, row.get("brawler"),
                  row.get("pick_sets"), row.get("set_wins_when_picked"),
                  row.get("local_ban_nominations"), row.get("local_ban_set_coverage"),
                  row.get("global_ban_nominations"), row.get("global_ban_series_coverage"))
        placeholders = ",".join("?" for _ in values)
        con.execute(f"INSERT OR REPLACE INTO {table} VALUES ({placeholders})", values)


def write_profile(db_path: str | Path, profile: dict[str, Any], raw_events: list[dict[str, Any]] | None = None) -> None:
    """Write a tournament_observation_profile.v1 into the archive database.

    `source_events` becomes the `event` table, `scopes` become the metric_* row
    tables. Pass `raw_events` (parsed captures with matches/sets) to also fill
    the series/set/pick/ban row tables for external SQL queries.
    """
    con = connect(db_path)
    try:
        _set_meta(con, "profile.schema", profile.get("schema"))
        _set_meta(con, "profile.generated_at", profile.get("generated_at"))
        _set_meta(con, "profile.policy", profile.get("policy"))
        _set_meta(con, "profile.metric_semantics", profile.get("metric_semantics"))
        for row in profile.get("source_events") or []:
            _write_event_from_source(con, row)
        for event in raw_events or []:
            src = event.get("source") or {}
            ev = event["event"]
            con.execute(
                "UPDATE event SET revision_timestamp = ?, format = ?, team_number = ?, site = ?, url = ?, api_url = ? WHERE region = ?",
                (src.get("revision_timestamp"), ev.get("format"), ev.get("team_number"),
                 src.get("site"), src.get("url"), src.get("api_url"), ev.get("region")),
            )
            _write_series_tables(con, event)
        scopes = profile.get("scopes") or {}
        _write_metric_rows(con, "metric_global", scopes.get("global") or [])
        for mode, rows in (scopes.get("mode") or {}).items():
            _write_metric_rows(con, "metric_mode", rows or [], extra=(mode,))
        for map_name, entry in (scopes.get("map") or {}).items():
            _write_metric_rows(con, "metric_map", entry.get("rows") or [], extra=(map_name, entry.get("mode") or ""))
        con.commit()
    finally:
        con.close()


def write_signal(db_path: str | Path, signal: dict[str, Any]) -> None:
    """Write a brawlstar.environment_signal.v1 into the archive database."""
    con = connect(db_path)
    try:
        for key in ("schema", "profile_id", "window", "rank_floor", "captured_at"):
            if signal.get(key) is not None:
                _set_meta(con, f"signal.{key}", signal.get(key))
        _set_meta(con, "signal.source", signal.get("source"))
        for name, row in (signal.get("brawlers") or {}).items():
            con.execute(
                "INSERT OR REPLACE INTO signal_brawler VALUES (?,?,?,?,?,?,?)",
                (name, row.get("picks"), row.get("pick_rate"), row.get("win_rate_when_picked"),
                 row.get("ban_series"), row.get("ban_rate"), row.get("ban_set_coverage")),
            )
        con.commit()
    finally:
        con.close()


def write_pickrate(db_path: str | Path, pickrate: dict[str, Any]) -> None:
    """Write a brawlstar.environment_signal_pickrate.v1 into the pickrate database."""
    con = connect(db_path)
    try:
        for key in ("schema", "window", "rank_floor", "fetched_at"):
            if pickrate.get(key) is not None:
                _set_meta(con, f"pickrate.{key}", pickrate.get(key))
        _set_meta(con, "pickrate.source", pickrate.get("source"))
        _set_meta(con, "pickrate.summary", pickrate.get("summary"))
        for name, row in (pickrate.get("global") or {}).items():
            con.execute(
                "INSERT OR REPLACE INTO ladder_global VALUES (?,?,?)",
                (name, row.get("use_rate"), row.get("win_rate")),
            )
        for map_key, row in (pickrate.get("per_map") or {}).items():
            for name, ind in (row.get("individual") or {}).items():
                con.execute(
                    "INSERT OR REPLACE INTO ladder_per_map (source_key, map, mode, match_count, active, latest_match_time, brawler, use_rate, win_rate, star_player_rate) "
                    "VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (map_key, row.get("map"), row.get("mode"), row.get("match_count"),
                     int(bool(row.get("active"))), row.get("latest_match_time"), name,
                     ind.get("use_rate"), ind.get("win_rate"), ind.get("star_player_rate")),
                )
        con.commit()
    finally:
        con.close()


# ------------------------------------------------------------------- read ----

def _meta_dict(con: sqlite3.Connection, prefix: str) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for row in con.execute("SELECT key, value FROM meta WHERE key LIKE ?", (f"{prefix}.%",)):
        out[row["key"][len(prefix) + 1:]] = json.loads(row["value"])
    return out


def read_raw_events(db_path: str | Path) -> list[dict[str, Any]]:
    """Restore parsed raw events (with matches/sets rows) from the archive db.

    This is the full-detail view used for JSON export or per-set review; the
    aggregated consumers read `read_profile` / `read_signal` instead.
    """
    con = connect(db_path)
    try:
        events: dict[str, dict[str, Any]] = {}
        for row in con.execute("SELECT * FROM event"):
            events[row["region"]] = {
                "schema": "brawl_stars_esports_event.v1",
                "event": {
                    "name": row["name"], "date": row["date"], "region": row["region"],
                    "format": row["format"], "team_number": row["team_number"],
                },
                "source": {
                    key: row[key]
                    for key in ("site", "page_title", "url", "api_url", "revision_id", "revision_timestamp")
                    if row[key] is not None
                },
                "summary": {
                    "series": row["series"], "played_series": row["played_series"],
                    "played_sets": row["played_sets"], "forfeits": row["forfeits"],
                    "champion": row["champion"], "runner_up": row["runner_up"],
                },
                "matches": [],
            }
        series_bans: dict[int, dict[str, list[str]]] = {}
        for row in con.execute("SELECT * FROM series_ban ORDER BY series_id, side, slot"):
            bucket = series_bans.setdefault(row["series_id"], {"team1": [], "team2": []})
            bucket[f"team{row['side']}"].append(row["brawler"])
        set_rows = {row["id"]: row for row in con.execute("SELECT * FROM \"set\" ORDER BY series_id, set_no")}
        set_picks: dict[int, dict[str, list[str]]] = {}
        set_bans: dict[int, dict[str, list[str]]] = {}
        for row in con.execute("SELECT * FROM set_pick ORDER BY set_id, side, slot"):
            set_picks.setdefault(row["set_id"], {"team1": [], "team2": []})[f"team{row['side']}"].append(row["brawler"])
        for row in con.execute("SELECT * FROM set_ban ORDER BY set_id, side, slot"):
            set_bans.setdefault(row["set_id"], {"team1": [], "team2": []})[f"team{row['side']}"].append(row["brawler"])
        for row in con.execute("SELECT * FROM series ORDER BY id"):
            event = events[row["event_region"]]
            event["matches"].append({
                "match_id": row["match_id"],
                "teams": [row["team1"], row["team2"]],
                "series_score": [row["score1"], row["score2"]],
                "status": row["status"],
                "mvp": row["mvp"],
                "round": row["round"],
                "match": row["match_no"],
                "date": row["date"],
                "vod": row["vod"],
                "winner_side": row["winner_side"],
                "winner_team": row["winner_team"],
                "map_veto_first_pick_team": row["map_veto_first_pick_team"],
                "global_bans": series_bans.get(row["id"], {"team1": [], "team2": []}),
                "sets": [
                    {
                        "set_no": s["set_no"], "map": s["map"], "mode": s["mode"],
                        "game_score": [s["score1"], s["score2"]],
                        "winner_side": s["winner_side"], "winner_team": s["winner_team"],
                        "draft_first_pick_team": s["draft_first_pick_team"],
                        "picks": set_picks.get(s["id"], {"team1": [], "team2": []}),
                        "local_bans": set_bans.get(s["id"], {"team1": [], "team2": []}),
                    }
                    for s in set_rows.values()
                    if s["series_id"] == row["id"]
                ],
            })
        return list(events.values())
    finally:
        con.close()


def read_profile(db_path: str | Path) -> dict[str, Any]:
    """Expand an archive database back into a tournament_observation_profile.v1 dict.

    `source_events` and `scopes` round-trip exactly. Per-event `events` entries
    are rebuilt from the `event` table with an empty per-event `scopes` (the
    per-event metric projection is not stored; query the row tables directly for
    per-event or per-set data).
    """
    con = connect(db_path)
    try:
        meta = _meta_dict(con, "profile")
        source_events: list[dict[str, Any]] = []
        events: list[dict[str, Any]] = []
        for row in con.execute("SELECT * FROM event ORDER BY rowid"):
            source_events.append({
                key: row[key]
                for key in ("name", "date", "region", "page_title", "revision_id", "series",
                            "played_series", "played_sets", "forfeits", "champion", "runner_up")
                if row[key] is not None
            })
            events.append({
                "event": {
                    "name": row["name"], "date": row["date"], "region": row["region"],
                    "format": row["format"], "team_number": row["team_number"],
                },
                "summary": {
                    "series": row["series"], "played_series": row["played_series"],
                    "played_sets": row["played_sets"], "forfeits": row["forfeits"],
                    "champion": row["champion"], "runner_up": row["runner_up"],
                },
                "scopes": {},
            })
        scopes: dict[str, Any] = {"global": [], "mode": {}, "map": {}}
        for row in con.execute("SELECT * FROM metric_global"):
            scopes["global"].append(dict(row))
        for row in con.execute("SELECT mode, brawler, pick_sets, set_wins_when_picked, local_ban_nominations, local_ban_set_coverage, global_ban_nominations, global_ban_series_coverage FROM metric_mode"):
            scopes["mode"].setdefault(row["mode"], []).append({k: row[k] for k in row.keys() if k != "mode"})
        for row in con.execute("SELECT * FROM metric_map"):
            entry = scopes["map"].setdefault(row["map"], {"mode": row["mode"], "rows": []})
            entry["rows"].append({k: row[k] for k in row.keys() if k not in ("map", "mode")})
        return {
            "schema": meta.get("schema", "tournament_observation_profile.v1"),
            "generated_at": meta.get("generated_at"),
            "policy": meta.get("policy") or {},
            "metric_semantics": meta.get("metric_semantics") or {},
            "source_events": source_events,
            "events": events,
            "scopes": scopes,
        }
    finally:
        con.close()


def read_signal(db_path: str | Path) -> dict[str, Any]:
    """Expand the signal tables back into a brawlstar.environment_signal.v1 dict."""
    con = connect(db_path)
    try:
        meta = _meta_dict(con, "signal")
        brawlers: dict[str, dict[str, Any]] = {}
        for row in con.execute("SELECT * FROM signal_brawler"):
            brawlers[row["brawler"]] = {
                "picks": row["picks"], "pick_rate": row["pick_rate"],
                "win_rate_when_picked": row["win_rate_when_picked"],
                "ban_series": row["ban_series"], "ban_rate": row["ban_rate"],
                "ban_set_coverage": row["ban_set_coverage"],
            }
        return {
            "schema": meta.get("schema", "brawlstar.environment_signal.v1"),
            "profile_id": meta.get("profile_id"),
            "window": meta.get("window"),
            "rank_floor": meta.get("rank_floor"),
            "source": meta.get("source") or {},
            "captured_at": meta.get("captured_at"),
            "brawlers": brawlers,
        }
    finally:
        con.close()


def read_pickrate(db_path: str | Path) -> dict[str, Any]:
    """Expand the pickrate tables back into a brawlstar.environment_signal_pickrate.v1 dict."""
    con = connect(db_path)
    try:
        meta = _meta_dict(con, "pickrate")
        global_rows: dict[str, dict[str, Any]] = {}
        for row in con.execute("SELECT * FROM ladder_global"):
            global_rows[row["brawler"]] = {"use_rate": row["use_rate"], "win_rate": row["win_rate"]}
        per_map: dict[str, dict[str, Any]] = {}
        for row in con.execute("SELECT * FROM ladder_per_map ORDER BY source_key, brawler"):
            key = row["source_key"]  # GCS 原始 key（保留 Safe Zone / Safe(r) Zone 等变体）
            entry = per_map.setdefault(key, {
                "map": row["map"], "mode": row["mode"], "match_count": row["match_count"],
                "active": bool(row["active"]), "latest_match_time": row["latest_match_time"],
                "individual": {},
            })
            entry["individual"][row["brawler"]] = {
                "use_rate": row["use_rate"], "win_rate": row["win_rate"],
                "star_player_rate": row["star_player_rate"],
            }
        return {
            "schema": meta.get("schema", "brawlstar.environment_signal_pickrate.v1"),
            "window": meta.get("window"),
            "rank_floor": meta.get("rank_floor"),
            "source": meta.get("source") or {},
            "fetched_at": meta.get("fetched_at"),
            "summary": meta.get("summary") or {},
            "global": global_rows,
            "per_map": per_map,
        }
    finally:
        con.close()


def is_sqlite_path(path: str | Path) -> bool:
    return str(path).lower().endswith(".sqlite3") or str(path).lower().endswith(".db")


def load_profile(path: str | Path) -> dict[str, Any]:
    """Unified profile loader: sqlite expands from rows, json loads directly."""
    if is_sqlite_path(path):
        return read_profile(path)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_signal(path: str | Path) -> dict[str, Any]:
    if is_sqlite_path(path):
        return read_signal(path)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_pickrate(path: str | Path) -> dict[str, Any]:
    if is_sqlite_path(path):
        return read_pickrate(path)
    return json.loads(Path(path).read_text(encoding="utf-8"))
