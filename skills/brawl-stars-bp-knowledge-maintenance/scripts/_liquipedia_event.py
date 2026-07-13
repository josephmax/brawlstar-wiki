#!/usr/bin/env python3
"""Pure parsing, rendering, and analysis primitives for Liquipedia event pages."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

RAW_SCHEMA = "liquipedia_event_capture.v1"
EVENT_SCHEMA = "brawl_stars_esports_event.v1"
OBSERVATION_SCHEMA = "tournament_observation_profile.v1"


def normalized_key(value: str) -> str:
    return "".join(char for char in value.casefold() if char.isalnum())


def load_brawler_names(repo: Path) -> dict[str, str]:
    """Read the vault-owned canonical names and aliases; never maintain a second alias table."""
    result: dict[str, str] = {}
    entity_dir = repo / "wiki/entities/brawlers"
    for path in entity_dir.glob("*.md"):
        result[normalized_key(path.stem)] = path.stem

    alias_path = repo / "wiki/concepts/英雄名称归一化.md"
    text = alias_path.read_text(encoding="utf-8")
    match = re.search(r"```yaml\n(.*?)\n```", text, re.S)
    if not match:
        raise ValueError(f"missing fenced YAML aliases: {alias_path}")
    canonical: str | None = None
    in_aliases = False
    for line in match.group(1).splitlines():
        if line == "aliases:":
            in_aliases = True
            continue
        if line == "ambiguous:":
            break
        if not in_aliases:
            continue
        canonical_match = re.match(r'^  "(.*)":(?: \[\])?$', line)
        if canonical_match:
            canonical = canonical_match.group(1)
            result[normalized_key(canonical)] = canonical
            continue
        alias_match = re.match(r'^    - "(.*)"$', line)
        if alias_match and canonical:
            result[normalized_key(alias_match.group(1))] = canonical
    # `ambiguous` is deliberately excluded: it must not be normalized automatically.
    return result


def canonicalize_brawler(value: str, canonical_names: dict[str, str]) -> str:
    value = re.sub(r"<!--.*?-->", "", value, flags=re.S).strip()
    return canonical_names.get(normalized_key(value), value)


def split_top_level(body: str) -> list[str]:
    parts: list[str] = []
    start = 0
    curly = 0
    square = 0
    idx = 0
    while idx < len(body):
        pair = body[idx : idx + 2]
        if pair == "{{":
            curly += 1
            idx += 2
            continue
        if pair == "}}":
            curly -= 1
            idx += 2
            continue
        if pair == "[[":
            square += 1
            idx += 2
            continue
        if pair == "]]":
            square -= 1
            idx += 2
            continue
        if body[idx] == "|" and curly == 0 and square == 0:
            parts.append(body[start:idx])
            start = idx + 1
        idx += 1
    parts.append(body[start:])
    return parts


def extract_balanced(text: str, start: int) -> str:
    depth = 0
    idx = start
    while idx < len(text) - 1:
        pair = text[idx : idx + 2]
        if pair == "{{":
            depth += 1
            idx += 2
            continue
        if pair == "}}":
            depth -= 1
            idx += 2
            if depth == 0:
                return text[start:idx]
            continue
        idx += 1
    raise ValueError(f"unbalanced MediaWiki template at offset {start}")


def parse_template(template: str, expected_name: str) -> tuple[dict[str, str], list[str]]:
    match = re.match(r"\{\{\s*([^|}\n]+)", template)
    actual_name = match.group(1).strip() if match else ""
    if normalized_key(actual_name) != normalized_key(expected_name):
        raise ValueError(f"expected template {expected_name}, got {actual_name or 'unknown'}")
    body = template[match.end() :] if match else template
    if body.endswith("}}"):
        body = body[:-2]
    fields: dict[str, str] = {}
    positional: list[str] = []
    for part in split_top_level(body):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            key, value = part.split("=", 1)
            fields[key.strip()] = value.strip()
        else:
            positional.append(part)
    return fields, positional


def first_template(text: str, name: str) -> str | None:
    marker = re.search(r"\{\{\s*" + re.escape(name) + r"(?=[\s|}])", text, re.I)
    return extract_balanced(text, marker.start()) if marker else None


def clean_text(value: str) -> str:
    value = re.sub(r"<!--.*?-->", "", value, flags=re.S)
    value = re.sub(r"\{\{[^{}]*\}\}", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def team_opponent(value: str) -> tuple[str, str | None]:
    template = first_template(value, "TeamOpponent")
    if not template:
        return clean_text(value), None
    fields, positional = parse_template(template, "TeamOpponent")
    name = clean_text(positional[0]) if positional else "unknown"
    return name, fields.get("score")


def parse_mediawiki_query(payload: dict[str, Any]) -> dict[str, Any]:
    pages = payload.get("query", {}).get("pages", [])
    if not pages:
        raise ValueError("MediaWiki response has no pages")
    page = pages[0]
    if page.get("missing") is True:
        raise ValueError(f"MediaWiki page not found: {page.get('title', 'unknown')}")
    revisions = page.get("revisions") or []
    if not revisions:
        raise ValueError(f"MediaWiki page has no revisions: {page.get('title', 'unknown')}")
    revision = revisions[0]
    slot = revision.get("slots", {}).get("main", {})
    content = slot.get("content") or slot.get("*")
    if content is None:
        raise ValueError("MediaWiki revision has no main-slot content")
    return {
        "page_title": page.get("title"),
        "page_id": page.get("pageid"),
        "revision_id": revision.get("revid"),
        "revision_timestamp": revision.get("timestamp"),
        "wikitext": content,
    }


def _event_region(page_title: str) -> str:
    normalized = page_title.replace("_", " ")
    if "/South America/" in normalized:
        return "South America"
    if "/EMEA/" in normalized:
        return "EMEA"
    parts = normalized.split("/")
    return parts[-2].replace("_", " ") if len(parts) >= 2 else "unknown"


def _parse_int(value: str | None) -> int | None:
    if value is None or not value.strip().isdigit():
        return None
    return int(value.strip())


def _match_templates(wikitext: str) -> Iterable[tuple[int, int, str]]:
    marker_re = re.compile(r"\|R(\d+)M(\d+)\s*=\s*\{\{\s*Match(?=[\s|}])", re.I)
    for marker in marker_re.finditer(wikitext):
        start = wikitext.find("{{", marker.start(), marker.end())
        yield int(marker.group(1)), int(marker.group(2)), extract_balanced(wikitext, start)


def parse_event_wikitext(
    wikitext: str,
    *,
    source: dict[str, Any],
    canonical_names: dict[str, str],
) -> dict[str, Any]:
    """Parse one Liquipedia Brawl Stars event without interpreting picks as recommendations."""
    info_template = first_template(wikitext, "Infobox league")
    info, _ = parse_template(info_template, "Infobox league") if info_template else ({}, [])
    display = re.search(r"\{\{DISPLAYTITLE:(.*?)\}\}", wikitext, re.I | re.S)
    name = clean_text(info.get("name") or (display.group(1) if display else source.get("page_title", "unknown")))
    page_title = str(source.get("page_title") or "")

    matches: list[dict[str, Any]] = []
    for round_no, match_no, template in _match_templates(wikitext):
        fields, _ = parse_template(template, "Match")
        team1, team1_source_score = team_opponent(fields.get("opponent1", "unknown"))
        team2, team2_source_score = team_opponent(fields.get("opponent2", "unknown"))
        teams = {1: team1, 2: team2}

        global_bans: dict[str, list[str]] = {"team1": [], "team2": []}
        for side_no in (1, 2):
            for idx in (1, 2):
                value = fields.get(f"t{side_no}b{idx}", "")
                if value:
                    global_bans[f"team{side_no}"].append(canonicalize_brawler(value, canonical_names))

        veto_first_pick: int | None = None
        veto_template = first_template(fields.get("mapveto", ""), "MapVeto")
        if veto_template:
            veto_fields, _ = parse_template(veto_template, "MapVeto")
            veto_first_pick = _parse_int(veto_fields.get("firstpick"))

        sets: list[dict[str, Any]] = []
        set_wins = {1: 0, 2: 0}
        for set_no in range(1, 6):
            value = fields.get(f"map{set_no}", "")
            if not value or re.search(r"\|\s*winner\s*=\s*skip", value, re.I):
                continue
            map_fields, _ = parse_template(value, "Map")
            score1 = _parse_int(map_fields.get("score1"))
            score2 = _parse_int(map_fields.get("score2"))
            if score1 is None or score2 is None or score1 == score2:
                continue
            winner_side = 1 if score1 > score2 else 2
            set_wins[winner_side] += 1
            picks: dict[str, list[str]] = {"team1": [], "team2": []}
            local_bans: dict[str, list[str]] = {"team1": [], "team2": []}
            for side_no in (1, 2):
                for idx in (1, 2, 3):
                    pick = map_fields.get(f"t{side_no}c{idx}", "")
                    if pick:
                        picks[f"team{side_no}"].append(canonicalize_brawler(pick, canonical_names))
                    ban = map_fields.get(f"t{side_no}b{idx}", "")
                    if ban:
                        local_bans[f"team{side_no}"].append(canonicalize_brawler(ban, canonical_names))
            draft_first_pick = _parse_int(map_fields.get("firstpick"))
            sets.append({
                "set_no": set_no,
                "map": clean_text(map_fields.get("map", "unknown")),
                "mode": clean_text(map_fields.get("maptype", "unknown")),
                "game_score": [score1, score2],
                "winner_side": winner_side,
                "winner_team": teams[winner_side],
                "draft_first_pick_team": draft_first_pick if draft_first_pick in (1, 2) else None,
                "picks": picks,
                "local_bans": local_bans,
            })

        is_forfeit = (team1_source_score or "").upper() == "FF" or (team2_source_score or "").upper() == "FF"
        winner_side: int | None = None
        if is_forfeit:
            if (team1_source_score or "").upper() == "W" or (team2_source_score or "").upper() == "FF":
                winner_side = 1
            elif (team2_source_score or "").upper() == "W" or (team1_source_score or "").upper() == "FF":
                winner_side = 2
        elif sets and set_wins[1] != set_wins[2]:
            winner_side = 1 if set_wins[1] > set_wins[2] else 2
        matches.append({
            "match_id": f"R{round_no}M{match_no}",
            "round": round_no,
            "match": match_no,
            "date": clean_text(fields.get("date", "unknown")),
            "teams": [team1, team2],
            "status": "forfeit" if is_forfeit else ("played" if sets else "unknown"),
            "series_score": [set_wins[1], set_wins[2]] if sets else None,
            "winner_side": winner_side,
            "winner_team": teams.get(winner_side),
            "global_bans": global_bans,
            # Liquipedia MapVeto.firstpick is map-veto initiative, not brawler draft order.
            "map_veto_first_pick_team": veto_first_pick if veto_first_pick in (1, 2) else None,
            "sets": sets,
            "mvp": clean_text(fields.get("mvp", "")) or None,
            "vod": fields.get("vod") or None,
        })

    final = max(matches, key=lambda item: (item["round"], item["match"])) if matches else None
    champion = final.get("winner_team") if final else None
    runner_up = None
    if final and final.get("winner_side") in (1, 2):
        runner_up = final["teams"][1 if final["winner_side"] == 1 else 0]
    played_sets = sum(len(match["sets"]) for match in matches)
    return {
        "schema": EVENT_SCHEMA,
        "source": dict(source),
        "event": {
            "name": name,
            "date": clean_text(info.get("date", "unknown")),
            "region": _event_region(page_title),
            "format": clean_text(info.get("format", "unknown")),
            "team_number": _parse_int(info.get("team_number")),
        },
        "summary": {
            "series": len(matches),
            "played_series": sum(match["status"] == "played" for match in matches),
            "played_sets": played_sets,
            "forfeits": sum(match["status"] == "forfeit" for match in matches),
            "champion": champion,
            "runner_up": runner_up,
        },
        "matches": matches,
    }


def render_raw_capture(event: dict[str, Any], wikitext: str, *, captured_at: str) -> str:
    source = event.get("source", {})
    normalized_wikitext = "\n".join(line.rstrip() for line in wikitext.rstrip().splitlines())
    return f"""# Liquipedia Event Direct Raw Capture: {event['event']['name']}

- Schema: {RAW_SCHEMA}
- Capture timestamp: {captured_at}
- Source URL: {source.get('url', 'unknown')}
- API endpoint: {source.get('api_url', 'unknown')}
- Page title: {source.get('page_title', 'unknown')}
- Revision ID: {source.get('revision_id', 'unknown')}
- Revision timestamp: {source.get('revision_timestamp', 'unknown')}
- License: CC BY-SA 3.0; attribution to Liquipedia contributors
- Wikitext normalization: LF line endings; trailing whitespace stripped

## Parsed Event JSON

```json
{json.dumps(event, ensure_ascii=False, indent=2)}
```

## Source Wikitext

```mediawiki
{normalized_wikitext}
```
"""


def load_raw_capture(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"## Parsed Event JSON\n\n```json\n(.*?)\n```", text, re.S)
    if not match:
        raise ValueError(f"missing Parsed Event JSON in {path}")
    return json.loads(match.group(1))


def load_raw_wikitext(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"## Source Wikitext\n\n```mediawiki\n(.*?)\n```\s*$", text, re.S)
    if not match:
        raise ValueError(f"missing Source Wikitext in {path}")
    return match.group(1)


def slugify(value: str) -> str:
    value = value.replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def _metric_rows(events: list[dict[str, Any]], *, mode: str | None = None, map_name: str | None = None) -> list[dict[str, Any]]:
    pick_sets: Counter[str] = Counter()
    wins: Counter[str] = Counter()
    local_ban_nominations: Counter[str] = Counter()
    local_ban_set_coverage: Counter[str] = Counter()
    global_ban_nominations: Counter[str] = Counter()
    global_ban_series_coverage: Counter[str] = Counter()

    for event in events:
        for match in event["matches"]:
            if mode is None and map_name is None and match["status"] == "played":
                series_bans: list[str] = []
                for side in ("team1", "team2"):
                    series_bans.extend(match["global_bans"][side])
                global_ban_nominations.update(series_bans)
                global_ban_series_coverage.update(set(series_bans))
            for item in match["sets"]:
                if mode is not None and item["mode"] != mode:
                    continue
                if map_name is not None and item["map"] != map_name:
                    continue
                set_bans: list[str] = []
                for side_no, side in ((1, "team1"), (2, "team2")):
                    pick_sets.update(item["picks"][side])
                    if item["winner_side"] == side_no:
                        wins.update(item["picks"][side])
                    set_bans.extend(item["local_bans"][side])
                local_ban_nominations.update(set_bans)
                local_ban_set_coverage.update(set(set_bans))

    names = set(pick_sets) | set(local_ban_nominations) | set(global_ban_nominations)
    rows = [{
        "brawler": name,
        "pick_sets": pick_sets[name],
        "set_wins_when_picked": wins[name],
        "local_ban_nominations": local_ban_nominations[name],
        "local_ban_set_coverage": local_ban_set_coverage[name],
        "global_ban_nominations": global_ban_nominations[name],
        "global_ban_series_coverage": global_ban_series_coverage[name],
    } for name in names]
    return sorted(
        rows,
        key=lambda row: (
            -row["pick_sets"],
            -row["local_ban_set_coverage"],
            -row["global_ban_series_coverage"],
            row["brawler"].casefold(),
        ),
    )


def _scopes(events: list[dict[str, Any]]) -> dict[str, Any]:
    modes = sorted({item["mode"] for event in events for match in event["matches"] for item in match["sets"]})
    maps: dict[str, str] = {}
    for event in events:
        for match in event["matches"]:
            for item in match["sets"]:
                maps[item["map"]] = item["mode"]
    return {
        "global": _metric_rows(events),
        "mode": {mode: _metric_rows(events, mode=mode) for mode in modes},
        "map": {
            map_name: {"mode": maps[map_name], "rows": _metric_rows(events, map_name=map_name)}
            for map_name in sorted(maps)
        },
    }


def analyze_events(events: list[dict[str, Any]], *, generated_at: str | None = None) -> dict[str, Any]:
    if not events:
        raise ValueError("at least one event is required")
    generated_at = generated_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "schema": OBSERVATION_SCHEMA,
        "generated_at": generated_at,
        "policy": {
            "interpretation": "descriptive_observation_only",
            "tier_generation": "forbidden",
            "runtime_consumption": "forbidden_until_separate_reviewed_promotion",
        },
        "metric_semantics": {
            "denominator": "played sets after excluding skipped placeholders and forfeits",
            "pick_sets": "sets where the brawler was picked",
            "set_wins_when_picked": "set wins, not individual game wins and not causal attribution",
            "local_ban_nominations": "per-team per-set ban nominations; duplicates across teams count twice",
            "local_ban_set_coverage": "unique played sets containing at least one local ban nomination",
            "global_ban_nominations": "per-team match-level global ban nominations in played series",
            "global_ban_series_coverage": "unique played series containing at least one global ban nomination",
        },
        "source_events": [{
            "name": event["event"]["name"],
            "date": event["event"]["date"],
            "region": event["event"]["region"],
            "page_title": event.get("source", {}).get("page_title"),
            "revision_id": event.get("source", {}).get("revision_id"),
            **event["summary"],
        } for event in events],
        "events": [{
            "event": event["event"],
            "summary": event["summary"],
            "scopes": _scopes([event]),
        } for event in events],
        "scopes": _scopes(events),
    }
