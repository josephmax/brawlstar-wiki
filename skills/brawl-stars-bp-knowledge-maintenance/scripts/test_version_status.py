#!/usr/bin/env python3
"""Tests for the version update status checker and its patch index."""
from __future__ import annotations

import datetime as dt
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(SCRIPT_DIR))

import version_status as vs  # noqa: E402

TODAY = dt.date(2026, 11, 12)


def source_page(manifest: dict | None = None, ledger: dict | None = None) -> str:
    parts = ["# patch page\n"]
    if manifest:
        parts.append("```json\n" + json.dumps({"balance_patch_manifest": manifest}) + "\n```\n")
    if ledger:
        parts.append("```json\n" + json.dumps({"version_fold_ledger": ledger}) + "\n```\n")
    return "\n".join(parts)


def ledger(patch_id: str, effective_at: str, brawlers: list[dict], environment: list[dict] | None = None) -> dict:
    return {
        "schema": vs.LEDGER_SCHEMA,
        "patch_id": patch_id,
        "effective_at": effective_at,
        "brawlers": brawlers,
        "environment": environment or [],
    }


def row(name: str, fold: str, note: str = "", rows: list[str] | None = None) -> dict:
    return {
        "brawler": name,
        "kinds": ["balance"],
        "direction": "buff",
        "rows": ["Health increased from 1 to 2"] if rows is None else rows,
        "fold": fold,
        "note": note,
    }


class FixtureRepo:
    """A minimal knowledge repository on disk."""

    def __init__(self, root: Path):
        self.root = root
        for rel in ("wiki/sources", "wiki/entities/brawlers", "wiki/environment/2026-10", "raw/sources/fandom/heroes"):
            (root / rel).mkdir(parents=True)

    def brawler(self, name: str, ready: bool = True) -> None:
        status = "bp_ready" if ready else "draft"
        (self.root / "wiki/entities/brawlers" / f"{name}.md").write_text(
            f"```yaml\nbp_brawler_profile:\n  profile_status: {status}\n```\n", encoding="utf-8"
        )

    def raw(self, slug: str, date: str) -> None:
        (self.root / "raw/sources/fandom/heroes" / f"{slug}-{date}.md").write_text(
            f"# Direct Raw Capture: Fandom {slug}\n\n- Capture date: {date}\n", encoding="utf-8"
        )

    def page(self, name: str, text: str) -> None:
        (self.root / "wiki/sources" / name).write_text(text, encoding="utf-8")

    def pool(self, captured_at: str) -> None:
        (self.root / "wiki/environment/ranked_pool.json").write_text(
            json.dumps({"season": 49, "source": {"captured_at": captured_at, "revision_id": 1}, "maps": [{"map": "A", "mode": "Heist"}]}),
            encoding="utf-8",
        )

    def event(self, name: str, date: str, page_title: str) -> None:
        path = self.root / "wiki/environment/2026-10/archive.sqlite3"
        con = sqlite3.connect(path)
        con.execute("CREATE TABLE IF NOT EXISTS event (name TEXT, date TEXT, page_title TEXT, played_sets TEXT)")
        con.execute("INSERT INTO event VALUES (?,?,?,?)", (name, date, page_title, "60"))
        con.commit()
        con.close()
        (self.root / "wiki/environment/current.json").write_text(
            json.dumps({"observations": [{"db": "wiki/environment/2026-10/archive.sqlite3", "kind": "last_chance_qualifier"}]}),
            encoding="utf-8",
        )


class VersionStatusTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = FixtureRepo(Path(self.tmp.name))
        self.repo.pool("2026-11-05")
        self.repo.event("LCQ", "2026-10-17 – 2026-10-18", "Brawl Stars Championship/2026/Last Chance Qualifier")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def status(self) -> dict:
        return vs.collect(self.repo.root, TODAY, 35, 45)

    def codes(self, level: str) -> list[tuple[str, str]]:
        return [(item["code"], item["subject"]) for item in self.status()["findings"] if item["level"] == level]

    def test_closed_ledger_with_fresh_raw_has_nothing_open(self) -> None:
        self.repo.brawler("Hank")
        self.repo.raw("hank", "2026-11-04")
        self.repo.page("patch.md", source_page(ledger=ledger("2026-11-03-release", "2026-11-03", [row("Hank", "numbers_only")])))
        status = self.status()
        self.assertEqual(status["counts"], {"error": 0, "open": 0, "info": 0})
        self.assertEqual(status["latest_patch"]["patch_id"], "2026-11-03-release")
        self.assertEqual(status["latest_event"]["end_date"], "2026-10-18")

    def test_pending_and_partial_folds_stay_open(self) -> None:
        for name in ("Hank", "Lou"):
            self.repo.brawler(name)
            self.repo.raw(name.lower(), "2026-11-04")
        self.repo.page(
            "patch.md",
            source_page(ledger=ledger("p", "2026-11-03", [row("Hank", "partial", "only breakpoints"), row("Lou", "pending")])),
        )
        self.assertEqual(self.codes("open"), [("fold_partial", "Hank"), ("fold_pending", "Lou")])

    def test_raw_older_than_patch_is_open(self) -> None:
        self.repo.brawler("Hank")
        self.repo.raw("hank", "2026-10-21")
        self.repo.page("patch.md", source_page(ledger=ledger("p", "2026-11-03", [row("Hank", "no_model_change")])))
        self.assertEqual(self.codes("open"), [("raw_stale", "Hank")])

    def test_ledger_errors(self) -> None:
        self.repo.brawler("Hank")
        self.repo.raw("hank", "2026-11-04")
        self.repo.page(
            "patch.md",
            source_page(
                manifest={"patch_id": "p", "effective_at": "2026-11-03", "changes": [{"brawler": "Shade"}, {"brawler": "multiple"}]},
                ledger=ledger(
                    "p",
                    "2026-11-03",
                    [row("Hank", "deferred"), row("Hnak", "pending"), row("Hank", "done")],
                    [{"id": "maps", "status": "later"}],
                ),
            ),
        )
        codes = {code for code, _ in self.codes("error")}
        self.assertEqual(
            codes,
            {"ledger_incomplete", "unknown_brawler", "invalid_fold", "invalid_environment_status", "duplicate_brawler"},
        )

    def test_deferred_requires_a_reason(self) -> None:
        self.repo.brawler("Hank")
        self.repo.raw("hank", "2026-11-04")
        self.repo.page("patch.md", source_page(ledger=ledger("p", "2026-11-03", [row("Hank", "deferred")])))
        self.assertEqual(self.codes("error"), [("note_missing", "Hank")])

    def test_manifest_only_patch_is_legacy_before_cutoff_and_error_after(self) -> None:
        self.repo.page("old.md", source_page(manifest={"patch_id": "old", "effective_at": "2026-08-06", "changes": [{"brawler": "Hank"}]}))
        self.repo.page("new.md", source_page(manifest={"patch_id": "new", "effective_at": "2026-12-01", "changes": [{"brawler": "Hank"}]}))
        index = {patch["patch_id"]: patch for patch in vs.load_patch_index(self.repo.root)}
        self.assertEqual(index["old"]["brawlers"]["Hank"]["fold"], "legacy")
        self.assertFalse(index["old"]["has_ledger"])
        findings = {(item["patch_id"], item["level"]) for item in self.status()["findings"] if item["code"] == "ledger_missing"}
        self.assertEqual(findings, {("old", "info"), ("new", "error")})

    def test_environment_items_and_stale_inputs(self) -> None:
        self.repo.pool("2026-09-17")
        self.repo.brawler("Vince", ready=False)
        self.repo.page(
            "patch.md",
            source_page(ledger=ledger("p", "2026-11-03", [], [{"id": "new_maps", "status": "pending", "note": "pool not rechecked"}])),
        )
        codes = self.codes("open")
        self.assertIn(("environment_pending", "new_maps"), codes)
        self.assertIn(("ranked_pool_stale", "Season 49"), codes)
        self.assertIn(("profile_not_ready", "Vince"), codes)
        late = vs.collect(self.repo.root, dt.date(2027, 1, 1), 35, 45)
        self.assertIn("esports_event_stale", [item["code"] for item in late["findings"]])

    def test_unarchived_events_only_lists_what_follows_the_archive(self) -> None:
        base = "Brawl Stars Championship/2026"
        known = {f"{base}/Season 6/EMEA/Monthly Finals", f"{base}/Last Chance Qualifier"}
        titles = [
            f"{base}/Season 1/EMEA/Monthly Finals",
            f"{base}/Season 6/EMEA/Monthly Finals",
            f"{base}/Season 7/EMEA/Monthly Finals",
            f"{base}/Season 7/EMEA/Monthly Qualifier",
            f"{base}/Chinese Mainland/June/Monthly Finals",
            f"{base}/Last Chance Qualifier",
            "Brawl Stars World Finals/2026",
            "Brawl Stars World Finals/2026/Additional Content",
        ]
        self.assertEqual(
            vs.unarchived_events(titles, known, 2026),
            ["Brawl Stars Championship/2026/Season 7/EMEA/Monthly Finals", "Brawl Stars World Finals/2026"],
        )


class RealRepositoryTest(unittest.TestCase):
    """The committed ledgers must stay structurally valid."""

    def test_committed_ledgers_have_no_errors(self) -> None:
        status = vs.collect(REPO, TODAY, 35, 45)
        errors = [item for item in status["findings"] if item["level"] == "error"]
        self.assertEqual(errors, [])

    def test_november_and_september_ledgers_cover_the_official_notes(self) -> None:
        index = {patch["patch_id"]: patch for patch in vs.load_patch_index(REPO)}
        november = index["2026-11-03-release"]
        september = index["2026-09-16-maintenance"]
        self.assertTrue(november["has_ledger"] and september["has_ledger"])
        self.assertEqual(len(november["brawlers"]), 34)
        self.assertEqual(len(september["brawlers"]), 18)
        self.assertEqual(november["brawlers"]["Hank"]["rows"], ["Health increased from 5500 to 6000"])
        self.assertIn("balance", november["brawlers"]["Cosmo"]["kinds"])
        self.assertIn("new_hypercharge", november["brawlers"]["Cosmo"]["kinds"])

    def test_reading_archives_does_not_modify_them(self) -> None:
        archives = sorted((REPO / "wiki/environment").glob("**/*.sqlite3"))
        before = {path: path.read_bytes() for path in archives}
        vs.collect(REPO, TODAY, 35, 45)
        self.assertEqual(before, {path: path.read_bytes() for path in archives})


if __name__ == "__main__":
    unittest.main()
