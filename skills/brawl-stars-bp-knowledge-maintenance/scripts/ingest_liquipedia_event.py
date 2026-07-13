#!/usr/bin/env python3
"""Ingest Liquipedia event captures into source summaries and event entity pages."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

from _liquipedia_event import analyze_events, load_raw_capture


ROOT = Path(__file__).resolve().parents[3]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", action="append", required=True, help="Event raw capture; repeatable.")
    parser.add_argument("--repo", default=str(ROOT))
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def file_suffix(value: str) -> str:
    value = value.replace(":", "").replace("/", "-")
    value = re.sub(r"[^A-Za-z0-9 .&'-]+", "", value)
    return re.sub(r"[ .&]+", "-", value).strip("-")


def result_rows(event: dict) -> str:
    rows = ["| 阶段 | 对阵 | 比分 | 状态 | MVP |", "| --- | --- | --- | --- | --- |"]
    for match in event["matches"]:
        score = "FF" if match["status"] == "forfeit" else "-".join(map(str, match["series_score"] or []))
        rows.append(f"| {match['match_id']} | {match['teams'][0]} vs {match['teams'][1]} | {score} | {match['status']} | {match['mvp'] or '-'} |")
    return "\n".join(rows)


def top_picks(event: dict, limit: int = 10) -> str:
    profile = analyze_events([event], generated_at="source-summary")
    total = event["summary"]["played_sets"]
    rows = ["| 英雄 | 选用 sets | set 胜场 | 选用覆盖 |", "| --- | ---: | ---: | ---: |"]
    picked = sorted(
        (row for row in profile["scopes"]["global"] if row["pick_sets"]),
        key=lambda row: (-row["pick_sets"], -row["set_wins_when_picked"], row["brawler"].casefold()),
    )
    for row in picked[:limit]:
        coverage = f"{row['pick_sets'] / total:.1%}" if total else "n/a"
        rows.append(f"| {row['brawler']} | {row['pick_sets']} | {row['set_wins_when_picked']} | {coverage} |")
    return "\n".join(rows)


def top_bans(event: dict, metric: str, denominator: int, limit: int = 10) -> str:
    profile = analyze_events([event], generated_at="source-summary")
    secondary = "local_ban_nominations" if metric == "local_ban_set_coverage" else "global_ban_nominations"
    label = "set 覆盖" if metric == "local_ban_set_coverage" else "series 覆盖"
    rows = [f"| 英雄 | {label} | nominations | 覆盖率 |", "| --- | ---: | ---: | ---: |"]
    observed = sorted(
        (row for row in profile["scopes"]["global"] if row[metric]),
        key=lambda row: (-row[metric], -row[secondary], row["brawler"].casefold()),
    )
    for row in observed[:limit]:
        coverage = f"{row[metric] / denominator:.1%}" if denominator else "n/a"
        rows.append(f"| {row['brawler']} | {row[metric]} | {row[secondary]} | {coverage} |")
    return "\n".join(rows)


def source_page(event: dict, raw_path: Path, repo: Path, entity_name: str) -> str:
    source = event["source"]
    summary = event["summary"]
    return f"""# Liquipedia 来源摘要: {event['event']['name']}

## 来源信息

- 来源：[{event['event']['name']}]({source.get('url')})
- 页面：`{source.get('page_title')}`
- 抓取 revision：`{source.get('revision_id')}`（{source.get('revision_timestamp')}）
- 上游 raw：[[../../{raw_path.relative_to(repo).as_posix()}]]
- 许可：CC BY-SA 3.0；归属 Liquipedia contributors
- source_quality：structured_mediawiki_capture
- source_type：competitive_event_result_and_draft_observation
- 对应赛事实体：[[../entities/events/{entity_name}|{event['event']['name']}]]

## 可用范围

- usable_for: event_result, played_set_count, map_mode_occurrence, observed_pick, observed_local_ban, observed_global_ban, set_result, mvp_record
- not_usable_for: causal_win_claim, automatic_tier, unconditional_counter_edge, stable_map_fit_without_vod_review, brawler_draft_order_when_map_firstpick_is_empty

## 赛事事实

- 日期：{event['event']['date']}
- 赛区：{event['event']['region']}
- 赛制：{event['event']['format']}
- 冠军：{summary['champion']}
- 亚军：{summary['runner_up']}
- 系列赛：{summary['series']}（实际进行 {summary['played_series']}，弃权 {summary['forfeits']}）
- 实际进行的 sets：{summary['played_sets']}

## 对阵结果

{result_rows(event)}

## 选用观察（按 set）

{top_picks(event)}

以上是描述性样本。选用覆盖率分母为实际进行的 sets；`set 胜场` 不是个人因果胜率，也不能自动生成强度 tier。

## Local ban 观察（按 set）

{top_bans(event, 'local_ban_set_coverage', summary['played_sets'])}

同一 set 内双方重复提名同一英雄时，`nominations` 计 2，`set 覆盖` 只计 1。

## Global ban 观察（按实际 series）

{top_bans(event, 'global_ban_series_coverage', summary['played_series'])}

弃权 series 的页面字段保留在 raw，但不进入以上 global-ban 实战聚合。

## 语义边界

- 一次 series 为双方一次交锋；本页赛制是先赢 3 个 set 的 Bo5 sets。
- 每个 set 固定一个地图 / 模式，并以局内小局比分决定 set 胜负。
- `Match.t1b* / t2b*` 是 series 级 global bans；`Map.t1b* / t2b*` 是 set 级 local ban nominations。
- `MapVeto.firstpick` 只表示地图 veto 的先选方，不是英雄 draft first pick。
- `winner=skip` 与弃权对阵不进入 played-set 分母。

## 关联页面

- [[../index|Wiki Index]]
- [[../concepts/英雄名称归一化|英雄名称归一化]]
"""


def entity_page(event: dict, source_name: str) -> str:
    summary = event["summary"]
    maps = Counter((item["map"], item["mode"]) for match in event["matches"] for item in match["sets"])
    map_lines = "\n".join(f"- {name}（{mode}）：{count} set" for (name, mode), count in sorted(maps.items()))
    return f"""# {event['event']['name']}

## 身份

- 类型：Brawl Stars Championship Monthly Finals
- 日期：{event['event']['date']}
- 赛区：{event['event']['region']}
- 赛制：{event['event']['format']}
- 参赛队数：{event['event']['team_number'] or 'unknown'}
- 来源：[[../../sources/{source_name}|Liquipedia 来源摘要]]

## 结果

- 冠军：{summary['champion']}
- 亚军：{summary['runner_up']}
- 系列赛：{summary['series']}（实际进行 {summary['played_series']}，弃权 {summary['forfeits']}）
- 实际进行的 sets：{summary['played_sets']}

## 地图与模式样本

{map_lines}

## 知识边界

本页保存可持续追踪的赛事事实，不把赛事频率直接写成英雄强度、稳定地图适配或对位结论。逐 set 选用 / ban 明细保留在上游 raw，描述性聚合由 `tournament_observation_profile.v1` 在 `outputs/` 生成。

## 关联页面

- [[../../index|Wiki Index]]
"""


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).resolve()
    for value in args.raw:
        raw_path = Path(value) if Path(value).is_absolute() else repo / value
        event = load_raw_capture(raw_path)
        suffix = file_suffix(event["event"]["name"])
        source_name = f"Liquipedia-{suffix}.md"
        entity_name = f"{suffix}.md"
        targets = {
            repo / "wiki/sources" / source_name: source_page(event, raw_path, repo, entity_name.removesuffix(".md")),
            repo / "wiki/entities/events" / entity_name: entity_page(event, source_name.removesuffix(".md")),
        }
        for path, content in targets.items():
            if args.dry_run:
                print(f"DRY-RUN {path.relative_to(repo)}")
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"WROTE {path.relative_to(repo)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
