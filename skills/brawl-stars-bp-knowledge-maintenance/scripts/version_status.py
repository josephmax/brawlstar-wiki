#!/usr/bin/env python3
"""Report what the knowledge base still owes the current game version.

Read-only. It answers one question for a maintainer or an agent: after the
latest patch, season rotation and esports event, which steps of the version
update pipeline (`references/version-update.md`) are still open?

Inputs are existing knowledge-base files only:

- `wiki/sources/*.md`: `balance_patch_manifest` and `version_fold_ledger` blocks
- `wiki/entities/brawlers/*.md`: canonical names and profile status
- `raw/sources/fandom/heroes/`: capture dates of affected brawlers
- `wiki/environment/`: ranked pool manifest and archived esports events

`load_patch_index` is also the single parser other tools import when they need
"which brawler changed in which patch" (for example the hero brief builder).
Nothing here judges strength; a ledger row is a bookkeeping fact.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sqlite3
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path
from typing import Any

LEDGER_SCHEMA = "brawlstar.version_fold_ledger.v1"
# A patch on or after this date must carry a ledger; older manifests are legacy.
LEDGER_REQUIRED_FROM = "2026-09-16"
OPEN_FOLDS = {"pending", "partial"}
CLOSED_FOLDS = {"folded", "model_changed", "numbers_only", "no_model_change", "deferred"}
NOTE_REQUIRED_FOLDS = {"partial", "folded", "deferred"}
ENV_OPEN = {"pending"}
ENV_CLOSED = {"done", "not_applicable", "deferred"}
USER_AGENT = "brawlstar-wiki-maintainer/1.0 (https://github.com/josephmax/brawlstar-wiki)"

JSON_BLOCK = re.compile(r"```json\n(.*?)\n```", re.S)
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def json_blocks(text: str) -> list[dict[str, Any]]:
    blocks = []
    for match in JSON_BLOCK.finditer(text):
        try:
            value = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            blocks.append(value)
    return blocks


def canonical_brawlers(repo: Path) -> dict[str, Path]:
    return {path.stem: path for path in sorted((repo / "wiki/entities/brawlers").glob("*.md"))}


def load_patch_index(repo: Path) -> list[dict[str, Any]]:
    """Every known patch, oldest first, with its affected brawlers.

    A patch with a `version_fold_ledger` is authoritative. A patch that only has
    a breakpoint manifest is `legacy`: its brawler list comes from the manifest
    rows and may be incomplete (the manifest is breakpoint-oriented).
    """
    patches: dict[str, dict[str, Any]] = {}
    for path in sorted((repo / "wiki/sources").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "balance_patch_manifest" not in text and "version_fold_ledger" not in text:
            continue
        rel = str(path.relative_to(repo))
        for block in json_blocks(text):
            manifest = block.get("balance_patch_manifest")
            ledger = block.get("version_fold_ledger")
            if isinstance(manifest, dict) and manifest.get("patch_id"):
                entry = patches.setdefault(manifest["patch_id"], {"patch_id": manifest["patch_id"]})
                entry.setdefault("effective_at", manifest.get("effective_at"))
                entry["manifest_page"] = rel
                rows = manifest.get("changes") or manifest.get("items") or []
                entry["manifest_brawlers"] = sorted(
                    {row["brawler"] for row in rows if isinstance(row.get("brawler"), str) and row["brawler"] != "multiple"}
                )
            if isinstance(ledger, dict) and ledger.get("patch_id"):
                entry = patches.setdefault(ledger["patch_id"], {"patch_id": ledger["patch_id"]})
                entry["effective_at"] = ledger.get("effective_at") or entry.get("effective_at")
                entry["ledger_page"] = rel
                entry["ledger"] = ledger
    index = []
    for entry in patches.values():
        ledger = entry.get("ledger")
        if ledger:
            brawlers = {
                row["brawler"]: {
                    "kinds": row.get("kinds") or [],
                    "direction": row.get("direction"),
                    "rows": row.get("rows") or [],
                    "fold": row.get("fold"),
                    "note": row.get("note") or "",
                }
                for row in ledger.get("brawlers") or []
                if isinstance(row.get("brawler"), str)
            }
        else:
            brawlers = {
                name: {"kinds": ["balance"], "direction": None, "rows": [], "fold": "legacy", "note": ""}
                for name in entry.get("manifest_brawlers", [])
            }
        names = [row.get("brawler") for row in (ledger or {}).get("brawlers") or []]
        index.append(
            {
                "duplicate_brawlers": sorted({name for name in names if names.count(name) > 1}),
                "patch_id": entry["patch_id"],
                "effective_at": entry.get("effective_at"),
                "source_page": entry.get("ledger_page") or entry.get("manifest_page"),
                "has_ledger": bool(ledger),
                "brawlers": brawlers,
                "environment": (ledger or {}).get("environment") or [],
                "upstream": (ledger or {}).get("upstream") or {},
                "manifest_brawlers": entry.get("manifest_brawlers", []),
            }
        )
    index.sort(key=lambda item: (item["effective_at"] or "", item["patch_id"]))
    return index


def raw_slug(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", name.replace("&", " ").replace(".", " ")).strip("-").lower()


def latest_capture_date(directory: Path, slug: str) -> str | None:
    """Newest capture date among `<slug>.md` and `<slug>-YYYY-MM-DD.md`."""
    pattern = re.compile(rf"{re.escape(slug)}(?:-\d{{4}}-\d{{2}}-\d{{2}}(?:-v\d+)?)?\.md")
    best = None
    for path in directory.glob(f"{slug}*.md"):
        if not pattern.fullmatch(path.name):
            continue
        head = path.read_text(encoding="utf-8", errors="replace")[:500]
        match = re.search(r"^- Capture date: (\d{4}-\d{2}-\d{2})", head, re.M) or re.search(
            r"-(\d{4}-\d{2}-\d{2})(?:-v\d+)?\.md$", path.name
        )
        if match and (best is None or match.group(1) > best):
            best = match.group(1)
    return best


def archived_events(repo: Path) -> list[dict[str, Any]]:
    """Every event in `wiki/environment/<YYYY-MM>/archive.sqlite3`.

    `current.json` names which archive feeds compile; an archive it points to
    but that is absent is reported as `missing`. Archives it does not point to
    are still listed, because "the latest event we hold" is a fact about the
    archive directory, not about the compile pointer.
    """
    env = repo / "wiki/environment"
    kinds: dict[str, str] = {}
    pointer_path = env / "current.json"
    if pointer_path.exists():
        pointer = json.loads(pointer_path.read_text(encoding="utf-8"))
        monthly = pointer.get("monthly") or {}
        if monthly.get("db"):
            kinds[monthly["db"]] = "monthly_finals"
        for item in pointer.get("observations") or []:
            if item.get("db"):
                kinds[item["db"]] = item.get("kind") or "observation"
    refs = {str(path.relative_to(repo)): "archived" for path in sorted(env.glob("*/archive.sqlite3"))}
    refs.update(kinds)
    events = []
    for ref, kind in sorted(refs.items()):
        path = repo / ref
        if not path.exists():
            events.append({"archive": ref, "kind": kind, "missing": True})
            continue
        con = sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True)
        try:
            for name, date, page_title, played_sets in con.execute(
                "SELECT name, date, page_title, played_sets FROM event"
            ):
                dates = DATE.findall(date or "")
                events.append(
                    {
                        "archive": ref,
                        "kind": kind,
                        "name": name,
                        "page_title": page_title,
                        "date": date,
                        "end_date": max(dates) if dates else None,
                        "played_sets": int(played_sets or 0),
                    }
                )
        finally:
            con.close()
    return events


def days_between(earlier: str | None, later: dt.date) -> int | None:
    if not earlier:
        return None
    try:
        return (later - dt.date.fromisoformat(earlier[:10])).days
    except ValueError:
        return None


def finding(level: str, code: str, subject: str, message: str, patch_id: str | None = None) -> dict[str, Any]:
    return {"level": level, "code": code, "patch_id": patch_id, "subject": subject, "message": message}


def collect(repo: Path, today: dt.date, pool_max_age: int, event_max_age: int) -> dict[str, Any]:
    canon = canonical_brawlers(repo)
    patches = load_patch_index(repo)
    findings: list[dict[str, Any]] = []
    fandom_raw = repo / "raw/sources/fandom/heroes"

    for patch in patches:
        pid, effective = patch["patch_id"], patch["effective_at"] or ""
        if not patch["has_ledger"]:
            level = "error" if effective >= LEDGER_REQUIRED_FROM else "info"
            findings.append(
                finding(
                    level,
                    "ledger_missing",
                    patch["source_page"] or pid,
                    "补丁来源页没有 version_fold_ledger"
                    + ("；该补丁晚于账本启用日期，必须补账。" if level == "error" else "（账本启用前的历史补丁，仅按断点清单识别受影响英雄）。"),
                    pid,
                )
            )
            continue
        if patch["duplicate_brawlers"]:
            findings.append(
                finding("error", "duplicate_brawler", ", ".join(patch["duplicate_brawlers"]), "同一英雄在账本中出现多行；合并为一行。", pid)
            )
        missing = sorted(set(patch["manifest_brawlers"]) - set(patch["brawlers"]))
        if missing:
            findings.append(
                finding("error", "ledger_incomplete", ", ".join(missing), "断点清单中的英雄未出现在并入账本里。", pid)
            )
        for name, row in patch["brawlers"].items():
            fold = row["fold"]
            if name not in canon:
                findings.append(finding("error", "unknown_brawler", name, "账本英雄名不是 canonical 实体页名。", pid))
                continue
            if fold not in OPEN_FOLDS | CLOSED_FOLDS:
                findings.append(finding("error", "invalid_fold", name, f"未知处置状态 {fold!r}。", pid))
                continue
            if fold in NOTE_REQUIRED_FOLDS and not row["note"].strip():
                findings.append(finding("error", "note_missing", name, f"处置状态 {fold} 必须写明依据或原因。", pid))
            if not row["rows"]:
                findings.append(finding("error", "rows_missing", name, "账本条目缺少官方改动原文行。", pid))
            captured = latest_capture_date(fandom_raw, raw_slug(name))
            if effective and (captured is None or captured < effective):
                findings.append(
                    finding(
                        "open",
                        "raw_stale",
                        name,
                        f"最新 Fandom 抓取件日期 {captured or '无'} 早于补丁生效日 {effective}。",
                        pid,
                    )
                )
            if fold in OPEN_FOLDS:
                findings.append(
                    finding(
                        "open",
                        "fold_" + fold,
                        name,
                        ("尚未处置。" if fold == "pending" else "部分并入：" + row["note"]),
                        pid,
                    )
                )
        for item in patch["environment"]:
            status = item.get("status")
            subject = item.get("id") or item.get("kind") or "environment"
            if status in ENV_OPEN:
                findings.append(finding("open", "environment_pending", subject, item.get("note") or "环境项尚未处置。", pid))
            elif status not in ENV_CLOSED:
                findings.append(finding("error", "invalid_environment_status", subject, f"未知状态 {status!r}。", pid))
            elif status == "deferred" and not (item.get("note") or "").strip():
                findings.append(finding("error", "note_missing", subject, "暂缓的环境项必须写明原因。", pid))

    latest_patch = patches[-1] if patches else None

    pool: dict[str, Any] = {}
    pool_path = repo / "wiki/environment/ranked_pool.json"
    if pool_path.exists():
        data = json.loads(pool_path.read_text(encoding="utf-8"))
        captured = (data.get("source") or {}).get("captured_at")
        age = days_between(captured, today)
        pool = {
            "season": data.get("season"),
            "captured_at": captured,
            "age_days": age,
            "map_count": len(data.get("maps") or []),
            "revision_id": (data.get("source") or {}).get("revision_id"),
        }
        if age is None or age > pool_max_age:
            findings.append(
                finding(
                    "open",
                    "ranked_pool_stale",
                    f"Season {pool['season']}",
                    f"地图池清单抓取于 {captured}，已 {age} 天未复核（阈值 {pool_max_age} 天）。",
                )
            )
    else:
        findings.append(finding("error", "ranked_pool_missing", "ranked_pool.json", "缺少排位地图池清单。"))

    events = archived_events(repo)
    dated = [event for event in events if event.get("end_date")]
    latest_event = max(dated, key=lambda event: event["end_date"]) if dated else None
    for event in events:
        if event.get("missing"):
            findings.append(finding("error", "event_archive_missing", event["archive"], "current.json 指向的赛事归档不存在。"))
    if latest_event:
        age = days_between(latest_event["end_date"], today)
        latest_event = {**latest_event, "age_days": age}
        if age is not None and age > event_max_age:
            findings.append(
                finding(
                    "open",
                    "esports_event_stale",
                    latest_event["name"],
                    f"最近归档赛事结束于 {latest_event['end_date']}，已 {age} 天（阈值 {event_max_age} 天）；按赛事流程核对是否有新赛事。",
                )
            )
    else:
        findings.append(finding("open", "esports_event_missing", "wiki/environment", "没有可用的归档赛事。"))

    not_ready = []
    for name, path in canon.items():
        if not re.search(r"^\s*profile_status:\s*[\"']?bp_ready[\"']?\s*$", path.read_text(encoding="utf-8"), re.M):
            not_ready.append(name)
    for name in not_ready:
        findings.append(finding("open", "profile_not_ready", name, "实体页没有 bp_ready 的 BP profile。"))

    return {
        "schema": "brawlstar.version_status.v1",
        "today": today.isoformat(),
        "latest_patch": {
            "patch_id": latest_patch["patch_id"],
            "effective_at": latest_patch["effective_at"],
            "source_page": latest_patch["source_page"],
        }
        if latest_patch
        else None,
        "patches": [
            {
                "patch_id": patch["patch_id"],
                "effective_at": patch["effective_at"],
                "has_ledger": patch["has_ledger"],
                "brawlers": len(patch["brawlers"]),
                "open_folds": sorted(name for name, row in patch["brawlers"].items() if row["fold"] in OPEN_FOLDS),
            }
            for patch in patches
        ],
        "ranked_pool": pool,
        "latest_event": latest_event,
        "findings": findings,
        "counts": {level: sum(1 for item in findings if item["level"] == level) for level in ("error", "open", "info")},
    }


def fetch_json(url: str, timeout: int = 30) -> Any:
    # curl, like the capture scripts: the system Python often lacks a CA bundle.
    result = subprocess.run(
        ["curl", "-sS", "-L", "--compressed", "--fail", "--max-time", str(timeout), "-A", USER_AGENT, url],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"curl exit {result.returncode}")
    return json.loads(result.stdout)


def unarchived_events(titles: list[str], known: set[str | None], year: int) -> list[str]:
    """Liquipedia event pages that come after what the archive already holds.

    International Monthly Finals count only when their season number is above
    the highest archived season (older seasons predate the archive and are not
    a backlog). The Last Chance Qualifier and World Finals pages count whenever
    they are not archived. Chinese Mainland events are outside this archive.
    """
    season = re.compile(rf"^Brawl Stars Championship/{year}/Season (\d+)/[^/]+/Monthly Finals$")
    archived_seasons = [int(match.group(1)) for title in known if title and (match := season.match(title))]
    newest = max(archived_seasons, default=0)
    special = {f"Brawl Stars Championship/{year}/Last Chance Qualifier", f"Brawl Stars World Finals/{year}"}
    fresh = []
    for title in titles:
        if title in known:
            continue
        match = season.match(title)
        if (match and int(match.group(1)) > newest) or title in special:
            fresh.append(title)
    return sorted(set(fresh))


def online_checks(repo: Path, status: dict[str, Any], today: dt.date) -> list[dict[str, Any]]:
    """Compare recorded upstream revisions with the live pages. Never writes."""
    out: list[dict[str, Any]] = []
    patches = load_patch_index(repo)
    recorded_history = next(
        (
            patch["upstream"].get("fandom_version_history_revision")
            for patch in reversed(patches)
            if patch["upstream"].get("fandom_version_history_revision")
        ),
        None,
    )
    history_title = f"Version History/{today.year}"
    try:
        query = urllib.parse.urlencode(
            {
                "action": "query",
                "prop": "revisions",
                "rvprop": "ids|timestamp",
                "titles": f"Ranked|{history_title}",
                "format": "json",
                "formatversion": "2",
            }
        )
        pages = fetch_json(f"https://brawlstars.fandom.com/api.php?{query}")["query"]["pages"]
        live = {page["title"]: (page.get("revisions") or [{}])[0] for page in pages}
        ranked = live.get("Ranked", {})
        if ranked.get("revid") and ranked["revid"] != status["ranked_pool"].get("revision_id"):
            out.append(
                finding(
                    "open",
                    "upstream_ranked_page_changed",
                    "Fandom: Ranked",
                    f"线上修订 {ranked['revid']}（{ranked.get('timestamp')}）不同于清单记录的 {status['ranked_pool'].get('revision_id')}；核对地图池是否轮换。",
                )
            )
        history = live.get(history_title, {})
        if history.get("revid") and history["revid"] != recorded_history:
            out.append(
                finding(
                    "open",
                    "upstream_version_history_changed",
                    f"Fandom: {history_title}",
                    f"线上修订 {history['revid']}（{history.get('timestamp')}）不同于账本记录的 {recorded_history}；核对是否有新补丁，并把核对后的修订号写回最新账本的 upstream。",
                )
            )
    except Exception as error:  # network failures must not hide offline findings
        out.append(finding("error", "online_check_failed", "Fandom", f"无法检查上游修订：{error}"))
    try:
        time.sleep(2)  # Liquipedia asks for at most one request per two seconds
        query = urllib.parse.urlencode(
            {
                "action": "query",
                "list": "allpages",
                "apprefix": f"Brawl Stars Championship/{today.year}/",
                "aplimit": "500",
                "format": "json",
                "formatversion": "2",
            }
        )
        titles = [page["title"] for page in fetch_json(f"https://liquipedia.net/brawlstars/api.php?{query}")["query"]["allpages"]]
        time.sleep(2)
        finals_title = f"Brawl Stars World Finals/{today.year}"
        query = urllib.parse.urlencode(
            {"action": "query", "list": "allpages", "apprefix": finals_title, "aplimit": "10", "format": "json", "formatversion": "2"}
        )
        titles += [page["title"] for page in fetch_json(f"https://liquipedia.net/brawlstars/api.php?{query}")["query"]["allpages"]]
        fresh = unarchived_events(titles, {event.get("page_title") for event in archived_events(repo)}, today.year)
        if fresh:
            out.append(
                finding(
                    "open",
                    "upstream_event_not_archived",
                    "Liquipedia",
                    "以下赛事页面晚于已归档赛事且未归档（页面存在不代表已开赛，先看页面再决定是否 ingest）：" + "；".join(fresh),
                )
            )
    except Exception as error:
        out.append(finding("error", "online_check_failed", "Liquipedia", f"无法检查赛事列表：{error}"))
    return out


def render(status: dict[str, Any]) -> str:
    lines = [f"版本状态（{status['today']}）"]
    latest = status["latest_patch"]
    if latest:
        lines.append(f"最新补丁：{latest['patch_id']}，生效 {latest['effective_at']}，来源页 {latest['source_page']}")
    pool = status["ranked_pool"]
    if pool:
        lines.append(f"地图池清单：Season {pool['season']}，{pool['map_count']} 图，抓取于 {pool['captured_at']}（{pool['age_days']} 天前）")
    event = status["latest_event"]
    if event:
        lines.append(f"最近归档赛事：{event['name']}，结束 {event['end_date']}（{event['age_days']} 天前），{event['played_sets']} 个 set")
    lines.append("")
    lines.append("补丁账本：")
    for patch in status["patches"]:
        state = "历史（无账本）" if not patch["has_ledger"] else f"未结 {len(patch['open_folds'])}/{patch['brawlers']}"
        lines.append(f"  {patch['effective_at']}  {patch['patch_id']}  {state}")
    labels = {"error": "错误（账本或数据本身有问题）", "open": "待办", "info": "说明"}
    for level in ("error", "open", "info"):
        items = [item for item in status["findings"] if item["level"] == level]
        if not items:
            continue
        lines.append("")
        lines.append(f"{labels[level]}：{len(items)}")
        grouped: dict[tuple[str | None, str], list[dict[str, Any]]] = {}
        for item in items:
            grouped.setdefault((item["patch_id"], item["code"]), []).append(item)
        for (patch_id, code), group in grouped.items():
            head = f"  [{code}]" + (f" {patch_id}" if patch_id else "")
            if len({item["message"] for item in group}) == 1 and len(group) > 1:
                lines.append(f"{head} {group[0]['message']}")
                lines.append("    " + "、".join(item["subject"] for item in group))
            else:
                for item in group:
                    lines.append(f"{head} {item['subject']}：{item['message']}")
    if not status["counts"]["error"] and not status["counts"]["open"]:
        lines.append("")
        lines.append("没有未结事项。")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--repo", default=str(repo_root()), help="Knowledge repository root")
    parser.add_argument("--today", help="Override today's date (YYYY-MM-DD) for reproducible reports")
    parser.add_argument("--pool-max-age-days", type=int, default=35, help="Ranked pool manifest review interval")
    parser.add_argument("--event-max-age-days", type=int, default=45, help="Esports archive review interval")
    parser.add_argument("--online", action="store_true", help="Also compare recorded upstream revisions with live pages")
    parser.add_argument("--json", action="store_true", help="Print the machine-readable report")
    parser.add_argument("--patch-index", action="store_true", help="Print only the derived patch index JSON")
    parser.add_argument("--strict", action="store_true", help="Exit 1 when any error or open item remains")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    if args.patch_index:
        print(json.dumps(load_patch_index(repo), ensure_ascii=False, indent=2))
        return 0
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    status = collect(repo, today, args.pool_max_age_days, args.event_max_age_days)
    if args.online:
        extra = online_checks(repo, status, today)
        status["findings"].extend(extra)
        for item in extra:
            status["counts"][item["level"]] += 1
    print(json.dumps(status, ensure_ascii=False, indent=2) if args.json else render(status))
    if status["counts"]["error"]:
        return 2
    return 1 if args.strict and status["counts"]["open"] else 0


if __name__ == "__main__":
    sys.exit(main())
