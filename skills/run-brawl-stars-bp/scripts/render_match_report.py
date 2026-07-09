#!/usr/bin/env python3
"""Render human-readable Brawl Stars BP match reports."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from string import Template
from typing import Any


BIAS_OPTIONS = ("conservative", "balanced", "aggressive", "high_variance")

REPORT_TEMPLATE = Template(
    """# 对战-$map

## 对局摘要

- 地图 / 模式: $map ($mode)
- 策略偏好: 蓝方 `$blue_strategy_bias`; 红方 `$red_strategy_bias`
- 强度权重: `$strength_weight`
- 禁用: 蓝方 $blue_ban_names; 红方 $red_ban_names
- 选择顺序: 蓝方 1 楼 -> 红方 2-3 楼 -> 蓝方 4-5 楼 -> 红方 6 楼
- 最终阵容: 蓝方 $blue_comp; 红方 $red_comp

## 禁用阶段

### 蓝方禁用

$blue_bans

### 红方禁用

$red_bans

- 禁用后不可用池: $unavailable_pool

## 选择时间线

$draft_timeline

## 玩家最终陈述

### 蓝方

- 阵容: $blue_comp
- 获胜思路: $blue_win_condition
- 角色职责与配装:
$blue_role_builds
- 关键风险: $blue_key_risks

### 红方

- 阵容: $red_comp
- 获胜思路: $red_win_condition
- 角色职责与配装:
$red_role_builds
- 关键风险: $red_key_risks

## 稳定知识引用

$stable_refs$execution_metadata
"""
)


def assign_strategy_bias(rng: random.Random | None = None) -> str:
    """Choose one player style before spawning a player agent."""
    chooser = rng or random
    return chooser.choice(BIAS_OPTIONS)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def inline_list(value: Any, empty: str = "无") -> str:
    items = [str(item) for item in as_list(value) if str(item)]
    return ", ".join(f"`{item}`" for item in items) if items else empty


def plain_list(value: Any, empty: str = "无", limit: int | None = None) -> str:
    items = [str(item) for item in as_list(value) if str(item)]
    if limit is not None:
        items = items[:limit]
    return "；".join(items) if items else empty


def text(value: Any, empty: str = "未提交") -> str:
    if value is None:
        return empty
    if isinstance(value, list):
        return "; ".join(str(item) for item in value) or empty
    return str(value) if str(value) else empty


def render_bans(bans: list[dict[str, Any]]) -> str:
    if not bans:
        return "- 无"
    lines: list[str] = []
    for ban in bans:
        brawler = text(ban.get("brawler"), "未知")
        summary = text(ban.get("report_summary") or ban.get("intent"), "未提交摘要")
        factors = plain_list(ban.get("priority_factors"), limit=3)
        risk = text(ban.get("risk_summary") or ban.get("risk_if_open"), "主要风险：未提交")
        matchup = text(ban.get("matchup_summary"), "")
        matchup_part = f" 对位依据：{matchup}。" if matchup else ""
        lines.append(f"- `{brawler}`: {summary} 关键因素：{factors}。{matchup_part}{risk}")
    return "\n".join(lines)


def render_rejected(options: list[dict[str, Any]]) -> str:
    if not options:
        return "无"
    rendered = []
    for option in options:
        name = text(option.get("brawler_or_pair"), "未知")
        reason = text(option.get("reason_rejected"), "未提交理由")
        rendered.append(f"`{name}` ({reason})")
    return "; ".join(rendered)


def render_turn(turn: dict[str, Any]) -> str:
    decision = turn.get("decision", {})
    state = turn.get("known_state", {})
    title = text(turn.get("title") or turn.get("turn_id"), "回合")
    picks = inline_list(decision.get("picks"))
    heading = f"### {title} - {picks}"
    lines = [
        heading,
        "",
        f"- 可见状态: 己方选择 {inline_list(state.get('own_picks'))}; 敌方选择 {inline_list(state.get('enemy_picks'))}; 不可用 {inline_list(state.get('unavailable_pool'))}。",
        f"- 选择摘要: {text(decision.get('report_summary') or decision.get('construct_direction'))}",
        f"- 关键因素: {plain_list(decision.get('priority_factors'), limit=4)}",
    ]
    if decision.get("matchup_summary"):
        lines.append(f"- 对位依据: {text(decision.get('matchup_summary'))}")
    lines.extend(
        [
            f"- 主要风险: {text(decision.get('risk_summary'), '主要风险：未提交')}",
            f"- 构筑提示: {text(decision.get('build_summary'), '构筑重点：无硬性构筑')}",
            f"- 备选取舍: {render_rejected(as_list(decision.get('rejected_options')))}",
        ]
    )
    return "\n".join(lines)


def render_execution_metadata(metadata: dict[str, Any] | None) -> str:
    if not metadata:
        return ""
    has_real_signal = any(
        metadata.get(key)
        for key in (
            "token_usage_captured",
            "timestamps_captured",
            "failure_reason",
        )
    )
    if not has_real_signal:
        return ""
    lines = ["", "## 执行元数据", ""]
    if metadata.get("player_execution"):
        lines.append(f"- 玩家执行: {metadata['player_execution']}")
    if metadata.get("token_usage_captured"):
        lines.append(f"- 捕获 token 用量: {metadata['token_usage_captured']}")
    elif metadata.get("token_usage_note"):
        lines.append(f"- Token 用量: {metadata['token_usage_note']}")
    if metadata.get("timestamps_captured"):
        lines.append(f"- 捕获时间戳: {metadata['timestamps_captured']}")
    if metadata.get("failure_reason"):
        lines.append(f"- 失败原因: {metadata['failure_reason']}")
    return "\n" + "\n".join(lines)


def render_role_builds(value: Any) -> str:
    rows = as_list(value)
    if not rows:
        return "  - 未提交"
    rendered: list[str] = []
    for row in rows:
        if isinstance(row, dict):
            name = text(row.get("brawler"), "未知")
            role = text(row.get("role_summary"), "未提交职责").rstrip("。；; ")
            build = text(row.get("build_summary"), "未提交配装")
            rendered.append(f"  - `{name}`：{role}；{build}")
        else:
            rendered.append(f"  - {row}")
    return "\n".join(rendered)


def render_match_report(data: dict[str, Any]) -> str:
    blue = data.get("blue_player", {})
    red = data.get("red_player", {})
    ban_phase = data.get("ban_phase", {})
    blue_ban_rows = as_list(ban_phase.get("blue_bans"))
    red_ban_rows = as_list(ban_phase.get("red_bans"))
    substitutions = {
        "map": text(data.get("map"), "未知地图"),
        "mode": text(data.get("mode"), "未知模式"),
        "blue_strategy_bias": text(data.get("blue_strategy_bias"), "未分配"),
        "red_strategy_bias": text(data.get("red_strategy_bias"), "未分配"),
        "strength_weight": text(data.get("strength_weight"), "0.4"),
        "blue_comp": inline_list(blue.get("comp")),
        "red_comp": inline_list(red.get("comp")),
        "blue_ban_names": inline_list([row.get("brawler") for row in blue_ban_rows if isinstance(row, dict)]),
        "red_ban_names": inline_list([row.get("brawler") for row in red_ban_rows if isinstance(row, dict)]),
        "blue_bans": render_bans(blue_ban_rows),
        "red_bans": render_bans(red_ban_rows),
        "unavailable_pool": inline_list(ban_phase.get("unavailable_pool")),
        "draft_timeline": "\n\n".join(render_turn(turn) for turn in as_list(data.get("turns"))),
        "blue_win_condition": text(blue.get("win_condition")),
        "blue_role_builds": render_role_builds(blue.get("role_builds")),
        "blue_key_risks": text(blue.get("key_risks")),
        "red_win_condition": text(red.get("win_condition")),
        "red_role_builds": render_role_builds(red.get("role_builds")),
        "red_key_risks": text(red.get("key_risks")),
        "stable_refs": "\n".join(f"- {ref}" for ref in as_list(data.get("stable_refs"))) or "- 无",
        "execution_metadata": render_execution_metadata(data.get("execution_metadata")),
    }
    return REPORT_TEMPLATE.substitute(substitutions).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a human-readable Brawl Stars BP match report.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    report = render_match_report(data)
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
