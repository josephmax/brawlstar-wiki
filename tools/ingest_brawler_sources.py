#!/usr/bin/env python3
"""Generate wiki source summaries from captured brawler raw files."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
ROSTER = ROOT / "raw/sources/roster/brawlers-roster-2026-06-29.md"
FANDOM_DIR = ROOT / "raw/sources/fandom/heroes"
PLP_DIR = ROOT / "raw/sources/pl-prodigy/brawlers"
SOURCE_DIR = ROOT / "wiki/sources"
@dataclass(frozen=True)
class RosterRow:
    name: str
    fandom_url: str
    plp_url: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roster", default=str(ROSTER))
    parser.add_argument("--names", nargs="*")
    parser.add_argument("--sites", nargs="+", choices=["fandom", "plp"], default=["fandom", "plp"])
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def parse_roster(path: Path) -> list[RosterRow]:
    rows: list[RosterRow] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or "---" in line or line.startswith("| canonical_name"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3:
            rows.append(RosterRow(cells[0], cells[1], cells[2]))
    return rows


def has_active_bp_sources(row: RosterRow) -> bool:
    return row.fandom_url != "no_page_found" and row.plp_url != "no_page_found"


def source_suffix(name: str) -> str:
    suffix = name.replace(" & ", "-").replace(" ", "-").replace(".", "")
    suffix = re.sub(r"-+", "-", suffix)
    return suffix.strip("-")


def slug_from_url_or_name(url: str, name: str) -> str:
    if url and url != "no_page_found":
        leaf = unquote(urlparse(url).path.rstrip("/").split("/")[-1])
    else:
        leaf = name
    leaf = leaf.replace("_", " ").replace("&", " ").replace(".", " ")
    return re.sub(r"[^A-Za-z0-9]+", "-", leaf).strip("-").lower()


def capture_rank(path: Path) -> tuple[str, int]:
    text = path.read_text(encoding="utf-8", errors="replace")[:500]
    match = re.search(r"^- Capture date: (\d{4}-\d{2}-\d{2})(?:-v(\d+))?", text, re.M)
    if match:
        return match.group(1), int(match.group(2) or 0)
    match = re.search(r"-(\d{4}-\d{2}-\d{2})(?:-v(\d+))?\.md$", path.name)
    if match:
        return match.group(1), int(match.group(2) or 0)
    return "0000-00-00", 0


def latest_direct_raw(directory: Path, slug: str) -> Path:
    candidates = []
    for path in directory.glob(f"{slug}-*.md"):
        head = path.read_text(encoding="utf-8", errors="replace")[:160]
        if "Direct Raw Capture" in head:
            candidates.append(path)
    if not candidates:
        raise FileNotFoundError(f"no direct raw for {slug} in {directory}")
    return sorted(candidates, key=capture_rank)[-1]


def rel_wikilink(path: Path) -> str:
    return "[[../../" + str(path.relative_to(ROOT)).replace("\\", "/") + "]]"


def extract_meta(raw: str, field: str, default: str = "unknown") -> str:
    match = re.search(rf"^- {re.escape(field)}: (.*)$", raw, re.M)
    return match.group(1).strip() if match else default


def extract_infobox(raw: str) -> dict[str, str]:
    match = re.search(r"## Infobox Fields\n\n(.*?)(?:\n## |\Z)", raw, re.S)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.startswith("- ") or ": " not in line:
            continue
        key, value = line[2:].split(": ", 1)
        fields[key.strip()] = value.strip()
    return fields


def extract_headings(raw: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^### (.+)$", raw, re.M)]


def first_field(fields: dict[str, str], *keys: str) -> str:
    for key in keys:
        value = fields.get(key)
        if value:
            return value
    return "unknown"


def list_field_values(fields: dict[str, str], pattern: str) -> list[str]:
    regex = re.compile(pattern)
    vals = []
    for key, value in fields.items():
        if regex.search(key) and value:
            vals.append(value)
    return vals


def extract_json_block(raw: str, heading: str) -> Any:
    pattern = rf"## {re.escape(heading)}\n\n```json\n(.*?)\n```"
    match = re.search(pattern, raw, re.S)
    if not match:
        return {}
    return json.loads(match.group(1))


def labels(items: Any) -> list[str]:
    if not isinstance(items, list):
        return []
    out = []
    for item in items:
        if isinstance(item, dict):
            out.append(str(item.get("label") or item.get("name") or item.get("code") or item.get("key")))
        else:
            out.append(str(item))
    return [x for x in out if x and x != "None"]


def names(items: Any) -> list[str]:
    if not isinstance(items, list):
        return []
    out = []
    for item in items:
        if isinstance(item, dict):
            out.append(str(item.get("name") or item.get("label") or item.get("key")))
        else:
            out.append(str(item))
    return [x for x in out if x and x != "None"]


def fmt_list(values: list[str], fallback: str = "none observed") -> str:
    return ", ".join(values) if values else fallback


def write_fandom_source(row: RosterRow, *, dry_run: bool) -> Path:
    slug = slug_from_url_or_name(row.fandom_url, row.name)
    raw_path = latest_direct_raw(FANDOM_DIR, slug)
    raw = raw_path.read_text(encoding="utf-8", errors="replace")
    fields = extract_infobox(raw)
    headings = extract_headings(raw)
    suffix = source_suffix(row.name)
    out = SOURCE_DIR / f"Fandom-{suffix}.md"

    rarity = first_field(fields, "Rarity")
    brawler_class = first_field(fields, "Class")
    movement = first_field(fields, "MovementSpeed")
    health = first_field(fields, "Health", "Health1")
    attack_range = first_field(fields, "AttackRange", "AttackRange1", "AttackRange2")
    reload = first_field(fields, "Reload", "Reload1", "Reload2")
    attack = first_field(fields, "Attack", "Attack1")
    super_range = first_field(fields, "SuperRange", "SuperRange1", "SuperRange2")
    super_value = first_field(fields, "Super", "Super1", "Super2")
    gadgets = list_field_values(fields, r"^Gadget\d+Name$")

    content = f"""# Fandom 来源摘要: {row.name}

## 来源信息

- 标题：{extract_meta(raw, "Title", row.name)}
- 来源：[{row.name} | Brawl Stars Wiki | Fandom]({row.fandom_url})
- 读取日期：{extract_meta(raw, "Capture date")}
- Fandom 页面最后编辑：{extract_meta(raw, "Source last edited")}
- 分类：Brawlers / Fandom hero page
- 上游 raw：{rel_wikilink(raw_path)}
- source_quality：direct_raw_capture
- source_type：official_or_wiki_mechanics

## 可用范围

- usable_for: stable_mechanics, ability_candidates, build_candidates_from_tips, mode_fit_candidates, map_feature_candidates
- not_usable_for: current_meta_strength_without_overlay, final_counter_claim, unconditional_bp_recommendation

## 页面核心字段

- 稀有度: {rarity}
- 官方定位: {brawler_class}
- 移动速度: {movement}
- 生命值: {health}
- 攻击距离: {attack_range}
- 装填: {reload}
- 普攻数值: {attack}
- Super 距离: {super_range}
- Super 数值: {super_value}
- Gadgets: {fmt_list(gadgets)}

## BP 建模可抽取信号

- `普攻 / Super / Gadget / Star Power / Hypercharge` 可以拆成稳定机制原子。
- `Tips / Recommended Build` 只能进入候选层；如果涉及模式或地图，后续必须转成 objective contract 或 map feature hook。
- 本页不直接生成 counter 或 pick 顺位结论。

## 抓取覆盖

{chr(10).join(f"- {heading}" for heading in headings) if headings else "- no_selected_headings_extracted"}

## 与本地 wiki 的意义

- `{row.name}` 的 Fandom 页面已有 direct raw，可作为稳定机制来源。
- 后续升级 [[entities/brawlers/{row.name}|{row.name}]] 时，应优先从本 raw 抽取机制事实，再与 [[sources/PLP-{suffix}|PLP 竞技信号]] 分层合并。

## 关联页面

- [[entities/brawlers/{row.name}|{row.name}]]
- [[sources/PLP-{suffix}|PLP 来源摘要: {row.name}]]
"""
    if not dry_run:
        out.write_text(content, encoding="utf-8")
    return out


def write_plp_source(row: RosterRow, *, dry_run: bool) -> Path:
    slug = slug_from_url_or_name(row.plp_url, row.name)
    raw_path = latest_direct_raw(PLP_DIR, slug)
    raw = raw_path.read_text(encoding="utf-8", errors="replace")
    guide = extract_json_block(raw, "Guide Fields")
    matchups = extract_json_block(raw, "Matchup Fields")
    suffix = source_suffix(row.name)
    out = SOURCE_DIR / f"PLP-{suffix}.md"

    gadget = (guide.get("gadget") or {}).get("label") if isinstance(guide, dict) else None
    star_power = (guide.get("starPower") or {}).get("label") if isinstance(guide, dict) else None
    gears = labels(guide.get("gears")) if isinstance(guide, dict) else []
    modes = labels(guide.get("modes")) if isinstance(guide, dict) else []
    notes = guide.get("notes") if isinstance(guide, dict) else []
    avoid = labels(guide.get("avoid")) if isinstance(guide, dict) else []
    counters_these = names(matchups.get("countersThese")) if isinstance(matchups, dict) else []
    countered_by = names(matchups.get("counteredBy")) if isinstance(matchups, dict) else []

    content = f"""# PLP 来源摘要: {row.name}

## 来源信息

- 标题：{extract_meta(raw, "Title", f"Best build for {row.name}")}
- 来源：[{row.name} | Power League Prodigy]({row.plp_url})
- 读取日期：{extract_meta(raw, "Capture date")}
- 上游 raw：{rel_wikilink(raw_path)}
- source_quality：direct_raw_capture
- source_type：third_party_competitive_guide
- payload_source_updated_at：{extract_meta(raw, "Payload sourceUpdatedAt")}

## 可用范围

- usable_for: build_candidates, mode_fit_candidates, matchup_candidates, slot_notes_candidates
- not_usable_for: stable_official_mechanics, final_counter_claim, current_meta_strength_without_overlay, unconditional_bp_recommendation

## 结构化字段摘要

- 推荐 Gadget: `{gadget or "unknown"}`
- 推荐 Star Power: `{star_power or "unknown"}`
- 推荐 Gears: {fmt_list(gears)}
- 推荐 Modes: {fmt_list(modes)}
- Notes: {fmt_list([str(x) for x in notes] if isinstance(notes, list) else [str(notes)] if notes else [])}
- Avoid: {fmt_list(avoid)}

## Matchup 候选

- countersThese: {fmt_list([f"`{x}`" for x in counters_these])}
- counteredBy: {fmt_list([f"`{x}`" for x in countered_by])}

这些 matchup 只作为 `conditional_matchup_seed`，不能写成无条件克制。进入 BP 模型前必须补机制、地图条件、build 条件、失效条件和 BP 用途。

## 与本地 wiki 的意义

- 本页为 [[entities/brawlers/{row.name}|{row.name}]] 的 build、mode fit、matchup 候选提供竞技信号。
- 与 Fandom 机制事实发生冲突时，应保留来源差异；PLP 不覆盖稳定机制事实。

## 关联页面

- [[sources/Fandom-{suffix}|Fandom 来源摘要: {row.name}]]
- [[entities/brawlers/{row.name}|{row.name}]]
"""
    if not dry_run:
        out.write_text(content, encoding="utf-8")
    return out


def main() -> int:
    args = parse_args()
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    names_filter = set(args.names or [])
    rows = [row for row in parse_roster(Path(args.roster)) if has_active_bp_sources(row)]
    if names_filter:
        rows = [row for row in rows if row.name in names_filter]

    written: list[Path] = []
    for row in rows:
        if "fandom" in args.sites:
            written.append(write_fandom_source(row, dry_run=args.dry_run))
        if "plp" in args.sites:
            written.append(write_plp_source(row, dry_run=args.dry_run))

    for path in written:
        print(path.relative_to(ROOT))
    print(f"written={0 if args.dry_run else len(written)} planned={len(written)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
