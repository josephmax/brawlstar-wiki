#!/usr/bin/env python3
"""Capture Brawl Stars Liquipedia event wikitext through the MediaWiki API."""

from __future__ import annotations

import argparse
import gzip
import http.client
import json
import time
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlparse

from _liquipedia_event import load_brawler_names, parse_event_wikitext, parse_mediawiki_query, render_raw_capture, slugify


ROOT = Path(__file__).resolve().parents[3]
RAW_DIR = ROOT / "raw/sources/liquipedia/events"
DEFAULT_USER_AGENT = "brawlstar-wiki-maintainer/1.0 (https://github.com/josephmax/brawlstar-wiki)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", action="append", required=True, help="Liquipedia page title or full brawlstars URL; repeatable.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Capture-date suffix.")
    parser.add_argument("--repo", default=str(ROOT))
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT, help="Must include project/use and contact information.")
    parser.add_argument("--sleep", type=float, default=2.0, help="Seconds between API requests; minimum 2.0.")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def page_title(value: str) -> str:
    if value.startswith("http://") or value.startswith("https://"):
        parsed = urlparse(value)
        marker = "/brawlstars/"
        if marker not in parsed.path:
            raise ValueError(f"not a Liquipedia Brawl Stars URL: {value}")
        return parsed.path.split(marker, 1)[1].strip("/")
    return value.strip().strip("/")


def api_path(title: str) -> str:
    query = (
        "action=query&prop=revisions&rvslots=main&rvprop=ids%7Ctimestamp%7Ccontent"
        f"&titles={quote(title, safe='')}&format=json&formatversion=2"
    )
    return f"/brawlstars/api.php?{query}"


def fetch_json(connection: http.client.HTTPSConnection, path: str, user_agent: str) -> dict:
    connection.request("GET", path, headers={
        "User-Agent": user_agent,
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
    })
    response = connection.getresponse()
    body = response.read()
    if response.status != 200:
        raise RuntimeError(f"Liquipedia API HTTP {response.status}: {body[:300]!r}")
    if response.getheader("Content-Encoding", "").lower() == "gzip":
        body = gzip.decompress(body)
    return json.loads(body.decode("utf-8"))


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).resolve()
    raw_dir = repo / "raw/sources/liquipedia/events"
    titles = [page_title(value) for value in args.event]
    targets = [(title, raw_dir / f"{slugify(title)}-{args.date}.md") for title in titles]
    if args.dry_run:
        for title, target in targets:
            print(f"DRY-RUN {title} -> {target.relative_to(repo)}")
        return 0
    if len(targets) > 1 and args.sleep < 2.0:
        raise ValueError("Liquipedia MediaWiki API requires at least 2 seconds between requests")
    if "(" not in args.user_agent or ")" not in args.user_agent:
        raise ValueError("--user-agent must include project/use and contact information in parentheses")

    canonical_names = load_brawler_names(repo)
    raw_dir.mkdir(parents=True, exist_ok=True)
    connection = http.client.HTTPSConnection("liquipedia.net", timeout=45)
    try:
        fetched = 0
        for title, target in targets:
            if target.exists() and not args.force:
                print(f"SKIP existing {target.relative_to(repo)}")
                continue
            if fetched:
                time.sleep(args.sleep)
            path = api_path(title)
            parsed = parse_mediawiki_query(fetch_json(connection, path, args.user_agent))
            source = {
                "site": "Liquipedia Brawl Stars Wiki",
                "page_title": parsed["page_title"],
                "url": f"https://liquipedia.net/brawlstars/{title}",
                "api_url": f"https://liquipedia.net{path}",
                "revision_id": parsed["revision_id"],
                "revision_timestamp": parsed["revision_timestamp"],
            }
            event = parse_event_wikitext(parsed["wikitext"], source=source, canonical_names=canonical_names)
            captured_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
            target.write_text(render_raw_capture(event, parsed["wikitext"], captured_at=captured_at), encoding="utf-8")
            print(f"WROTE {target.relative_to(repo)} revision={parsed['revision_id']} sets={event['summary']['played_sets']}")
            fetched += 1
    finally:
        connection.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
