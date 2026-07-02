#!/usr/bin/env python3
"""Capture Brawl Stars brawler raw source pages from Fandom and PL Prodigy."""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import quote, unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
ROSTER = ROOT / "raw/sources/roster/brawlers-roster-2026-06-29.md"
FANDOM_DIR = ROOT / "raw/sources/fandom/heroes"
PLP_DIR = ROOT / "raw/sources/pl-prodigy/brawlers"

USER_AGENT = "Codex brawlstar wiki capture/1.0"
@dataclass(frozen=True)
class RosterRow:
    name: str
    fandom_url: str
    plp_url: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--roster", default=str(ROSTER))
    parser.add_argument("--names", nargs="*", help="Optional subset of canonical names.")
    parser.add_argument("--sites", nargs="+", choices=["fandom", "plp"], default=["fandom", "plp"])
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--force", action="store_true", help="Write this date even if another direct capture exists.")
    parser.add_argument("--sleep", type=float, default=0.25)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def parse_roster(path: Path) -> list[RosterRow]:
    rows: list[RosterRow] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or "---" in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0] == "canonical_name":
            continue
        rows.append(RosterRow(cells[0], cells[1], cells[2]))
    return rows


def has_active_bp_sources(row: RosterRow) -> bool:
    return row.fandom_url != "no_page_found" and row.plp_url != "no_page_found"


def slug_from_url_or_name(url: str, name: str) -> str:
    if url and url != "no_page_found":
        parsed = urlparse(url)
        leaf = unquote(parsed.path.rstrip("/").split("/")[-1])
    else:
        leaf = name
    leaf = leaf.replace("_", " ")
    leaf = leaf.replace("&", " ")
    leaf = leaf.replace(".", " ")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", leaf).strip("-").lower()
    return slug or re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower()


def direct_capture_exists(directory: Path, slug: str) -> bool:
    for path in directory.glob(f"{slug}-*.md"):
        try:
            head = path.read_text(encoding="utf-8", errors="replace")[:120]
        except OSError:
            continue
        if "Direct Raw Capture" in head:
            return True
    return False


def run_curl(url: str, *, timeout: int = 40) -> str:
    cmd = [
        "curl",
        "-L",
        "--compressed",
        "--retry",
        "3",
        "--connect-timeout",
        "12",
        "--max-time",
        str(timeout),
        "-A",
        USER_AGENT,
        url,
    ]
    proc = subprocess.run(cmd, check=False, text=True, capture_output=True)
    if proc.returncode != 0:
        stderr = proc.stderr.strip() or f"curl exit {proc.returncode}"
        raise RuntimeError(stderr)
    return proc.stdout


def fandom_api_url(title: str) -> str:
    params = (
        "action=query&prop=revisions&rvprop=timestamp%7Ccontent&rvslots=main"
        f"&titles={quote(title, safe='')}&format=json&formatversion=2"
    )
    return f"https://brawlstars.fandom.com/api.php?{params}"


def extract_balanced_template(wikitext: str, marker_re: re.Pattern[str]) -> str:
    match = marker_re.search(wikitext)
    if not match:
        return ""
    start = match.start()
    depth = 0
    idx = start
    while idx < len(wikitext) - 1:
        pair = wikitext[idx : idx + 2]
        if pair == "{{":
            depth += 1
            idx += 2
            continue
        if pair == "}}":
            depth -= 1
            idx += 2
            if depth == 0:
                return wikitext[start:idx]
            continue
        idx += 1
    return wikitext[start:]


def split_template_params(template: str) -> list[str]:
    inner = template.strip()
    if inner.startswith("{{"):
        inner = inner[2:]
    if inner.endswith("}}"):
        inner = inner[:-2]

    parts: list[str] = []
    start = 0
    brace_depth = 0
    link_depth = 0
    idx = 0
    while idx < len(inner):
        pair = inner[idx : idx + 2]
        if pair == "{{":
            brace_depth += 1
            idx += 2
            continue
        if pair == "}}" and brace_depth:
            brace_depth -= 1
            idx += 2
            continue
        if pair == "[[":
            link_depth += 1
            idx += 2
            continue
        if pair == "]]" and link_depth:
            link_depth -= 1
            idx += 2
            continue
        if inner[idx] == "|" and brace_depth == 0 and link_depth == 0:
            parts.append(inner[start:idx])
            start = idx + 1
        idx += 1
    parts.append(inner[start:])
    return parts


def extract_infobox(wikitext: str) -> dict[str, str]:
    marker = re.compile(r"\{\{\s*(?:Brawler|[A-Za-z0-9 .&'-]+)[ _]Infobox\b", re.I)
    template = extract_balanced_template(wikitext, marker)
    if not template:
        return {}

    fields: dict[str, str] = {}
    for param in split_template_params(template)[1:]:
        if "=" not in param:
            continue
        key, value = param.split("=", 1)
        key = re.sub(r"\s+", " ", key).strip()
        value = re.sub(r"\s+", " ", value).strip()
        if key:
            fields[key] = value
    return fields


def clean_heading(raw: str) -> str:
    return re.sub(r"\s+", " ", raw.replace("_", " ")).strip()


def section_blocks(wikitext: str) -> list[tuple[str, str]]:
    heading_re = re.compile(r"^(={2,6})\s*(.+?)\s*\1\s*$", re.M)
    matches = list(heading_re.finditer(wikitext))
    blocks: list[tuple[str, str]] = []

    if matches:
        lead = wikitext[: matches[0].start()].strip()
    else:
        lead = wikitext.strip()
    if lead:
        blocks.append(("Lead excerpt", lead))

    stack: dict[int, str] = {}
    for idx, match in enumerate(matches):
        level = len(match.group(1))
        title = clean_heading(match.group(2))
        stack = {k: v for k, v in stack.items() if k < level}
        stack[level] = title
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(wikitext)
        body = wikitext[match.end() : end].strip()
        path = " / ".join(stack[k] for k in sorted(stack))
        if body:
            blocks.append((path, body))
    return blocks


def selected_fandom_excerpts(wikitext: str, *, per_block_limit: int = 4200, total_limit: int = 26000) -> list[tuple[str, str, bool]]:
    keywords = (
        "attack",
        "super",
        "trait",
        "gadget",
        "star power",
        "hypercharge",
        "tips",
        "strategy",
        "recommended build",
        "game modes",
        "maps",
    )
    out: list[tuple[str, str, bool]] = []
    total = 0
    for title, body in section_blocks(wikitext):
        title_l = title.lower()
        if title != "Lead excerpt" and not any(key in title_l for key in keywords):
            continue
        excerpt = body.strip()
        truncated = False
        if len(excerpt) > per_block_limit:
            excerpt = excerpt[:per_block_limit].rstrip()
            truncated = True
        if total + len(excerpt) > total_limit:
            remaining = max(0, total_limit - total)
            if remaining < 600:
                break
            excerpt = excerpt[:remaining].rstrip()
            truncated = True
        out.append((title, excerpt, truncated))
        total += len(excerpt)
    return out


def capture_fandom(row: RosterRow, capture_date: str, *, force: bool, dry_run: bool) -> tuple[str, Path | None]:
    slug = slug_from_url_or_name(row.fandom_url, row.name)
    out = FANDOM_DIR / f"{slug}-{capture_date}.md"
    if out.exists():
        return "skip_exists_this_date", out
    if not force and direct_capture_exists(FANDOM_DIR, slug):
        return "skip_existing_direct", None
    if dry_run:
        return "would_capture", out

    title = unquote(urlparse(row.fandom_url).path.rstrip("/").split("/")[-1]).replace("_", " ")
    data = json.loads(run_curl(fandom_api_url(title)))
    page = data.get("query", {}).get("pages", [{}])[0]
    if "missing" in page:
        out.write_text(
            f"# Inaccessible Raw Capture: Fandom {row.name}\n\n"
            f"- Title: {row.name}\n"
            f"- URL: {row.fandom_url}\n"
            f"- Capture date: {capture_date}\n"
            "- Source type: Fandom hero page\n"
            "- Capture status: missing_page\n",
            encoding="utf-8",
        )
        return "missing_page", out

    revision = page.get("revisions", [{}])[0]
    timestamp = revision.get("timestamp", "unknown")
    wikitext = revision.get("slots", {}).get("main", {}).get("content", "")
    infobox = extract_infobox(wikitext)
    excerpts = selected_fandom_excerpts(wikitext)

    lines = [
        f"# Direct Raw Capture: Fandom {row.name}",
        "",
        f"- Title: {page.get('title', row.name)}",
        f"- URL: {row.fandom_url}",
        f"- Capture date: {capture_date}",
        "- Correction note: parser supports generic and brawler-specific infobox templates.",
        f"- Source last edited: {timestamp}",
        "- Capture method: Fandom MediaWiki API revisions content via curl",
        "- Capture boundary: selected hero mechanics and BP-relevant tips/build excerpts; cosmetic/history/skin/voice sections omitted.",
        f"- Full source wikitext length at capture: {len(wikitext)} characters",
        "",
        "## Infobox Fields",
        "",
    ]
    if infobox:
        for key, value in infobox.items():
            lines.append(f"- {key}: {value}")
    else:
        lines.append("- no_infobox_fields_extracted")
    lines.extend(["", "## Selected Wikitext Excerpts", ""])
    for title, excerpt, truncated in excerpts:
        lines.extend([f"### {title}", "", excerpt, ""])
        if truncated:
            lines.extend(["[TRUNCATED in raw capture: selected excerpt only; re-fetch source for full page.]", ""])
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return "captured", out


def flight_payload(html_text: str) -> str:
    pieces: list[str] = []
    pattern = re.compile(r"<script>self\.__next_f\.push\((.*?)\)</script>", re.S)
    for match in pattern.finditer(html_text):
        try:
            arr = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        if len(arr) > 1 and isinstance(arr[1], str):
            pieces.append(arr[1])
    return "".join(pieces)


def raw_decode_after(text: str, key: str) -> Any | None:
    idx = text.find(key)
    if idx < 0:
        return None
    decoder = json.JSONDecoder()
    try:
        obj, _ = decoder.raw_decode(text[idx + len(key) :])
        return obj
    except json.JSONDecodeError:
        return None


def compact_guide_record(record: dict[str, Any]) -> dict[str, Any]:
    catalog = record.get("catalogEntry") or {}
    build = record.get("build") or {}
    compact: dict[str, Any] = {
        "key": record.get("key"),
        "internalName": record.get("internalName"),
        "name": record.get("name"),
        "slug": record.get("slug"),
        "id": record.get("id"),
        "description": record.get("description"),
        "catalog_class": (catalog.get("class") or {}).get("name"),
        "catalog_rarity": (catalog.get("rarity") or {}).get("name"),
    }
    for key in [
        "gadget",
        "starPower",
        "gears",
        "notes",
        "notesRaw",
        "modes",
        "modesRaw",
        "counters",
        "countersRaw",
        "avoid",
        "avoidRaw",
        "sourceRow",
        "gearsRaw",
    ]:
        compact[key] = build.get(key)
    for key in ["guideHref", "hasLegacyGuide", "legacySlug", "legacyGuideHref"]:
        compact[key] = record.get(key)
    return compact


def html_title(html_text: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html_text, re.S | re.I)
    return html.unescape(re.sub(r"\s+", " ", match.group(1)).strip()) if match else "unknown"


def meta_description(html_text: str) -> str:
    match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', html_text, re.S | re.I)
    return html.unescape(match.group(1)).strip() if match else "unknown"


def capture_plp(row: RosterRow, capture_date: str, *, force: bool, dry_run: bool) -> tuple[str, Path | None]:
    if row.plp_url == "no_page_found":
        return "skip_no_page_found", None
    slug = slug_from_url_or_name(row.plp_url, row.name)
    out = PLP_DIR / f"{slug}-{capture_date}.md"
    if out.exists():
        return "skip_exists_this_date", out
    if not force and direct_capture_exists(PLP_DIR, slug):
        return "skip_existing_direct", None
    if dry_run:
        return "would_capture", out

    html_text = run_curl(row.plp_url, timeout=45)
    flight = flight_payload(html_text)
    record = raw_decode_after(flight, '"guideRecord":')
    if not isinstance(record, dict):
        out.write_text(
            f"# Inaccessible Raw Capture: PLP {row.name}\n\n"
            f"- Title: {html_title(html_text)}\n"
            f"- URL: {row.plp_url}\n"
            f"- Capture date: {capture_date}\n"
            "- Source type: third-party competitive guide\n"
            "- Capture status: payload_not_found\n",
            encoding="utf-8",
        )
        return "payload_not_found", out

    guide_fields = compact_guide_record(record)
    matchups = record.get("matchups")
    if not isinstance(matchups, dict):
        matchups = raw_decode_after(flight, '"matchups":') or {}
    gear_availability = record.get("gearAvailability") or {}
    source_updated_at = gear_availability.get("sourceUpdatedAt", "unknown")

    lines = [
        f"# Direct Raw Capture: PLP {row.name}",
        "",
        f"- Title: {html_title(html_text)}",
        f"- URL: {row.plp_url}",
        f"- Capture date: {capture_date}",
        "- Correction note: nested `build` fields are preserved explicitly.",
        "- Source type: third-party competitive guide",
        "- Capture method: public Next.js page payload + metadata via curl",
        "- Capture boundary: structured guide/loadout/mode/matchup fields only; page HTML and marketing UI omitted.",
        f"- Payload sourceUpdatedAt: {source_updated_at}",
        f"- Meta description: {meta_description(html_text)}",
        "",
        "## Guide Fields",
        "",
        "```json",
        json.dumps(guide_fields, ensure_ascii=False, indent=2),
        "```",
        "",
        "## Matchup Fields",
        "",
        "```json",
        json.dumps(matchups, ensure_ascii=False, indent=2),
        "```",
    ]
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return "captured", out


def main() -> int:
    args = parse_args()
    roster = parse_roster(Path(args.roster))
    names = set(args.names or [])
    targets = [row for row in roster if has_active_bp_sources(row)]
    if names:
        targets = [row for row in targets if row.name in names]
    if args.limit:
        targets = targets[: args.limit]

    FANDOM_DIR.mkdir(parents=True, exist_ok=True)
    PLP_DIR.mkdir(parents=True, exist_ok=True)

    counts: dict[str, int] = {}
    failures: list[str] = []
    for row in targets:
        for site in args.sites:
            try:
                if site == "fandom":
                    status, path = capture_fandom(row, args.date, force=args.force, dry_run=args.dry_run)
                else:
                    status, path = capture_plp(row, args.date, force=args.force, dry_run=args.dry_run)
                counts[f"{site}:{status}"] = counts.get(f"{site}:{status}", 0) + 1
                suffix = f" -> {path.relative_to(ROOT)}" if path else ""
                print(f"{site}\t{row.name}\t{status}{suffix}")
            except Exception as exc:  # Keep the long batch moving.
                key = f"{site}:error"
                counts[key] = counts.get(key, 0) + 1
                failures.append(f"{site}\t{row.name}\t{exc}")
                print(f"{site}\t{row.name}\terror\t{exc}", file=sys.stderr)
            time.sleep(args.sleep)

    print("\nSummary:")
    for key in sorted(counts):
        print(f"- {key}: {counts[key]}")
    if failures:
        print("\nFailures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
