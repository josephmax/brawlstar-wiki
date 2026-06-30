#!/usr/bin/env python3
"""Audit brawler BP profile quality gates."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTITY_DIR = ROOT / "wiki/entities/brawlers"
OUT = ROOT / "wiki/syntheses/英雄BP建模质量审计.md"

AUTO_PLACEHOLDERS = [
    "draft_from_raw_signals",
    "not_bp_ready",
    "needs_review",
    "unknown_pending",
    "unknown_or_low_without_review",
    "unknown_until_reviewed",
    "not_observed_in_selected_raw",
    "not_inferred_from_source",
    "pending;",
    "mechanism: \"pending",
    "PLP mode fit is a seed",
    "seed_only_not_final",
    "candidate_not_final",
    "do_not_use_as",
    "requires map/mode/build validation",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def profile_text(page: str) -> str:
    marker = "bp_brawler_profile:"
    idx = page.find(marker)
    return page[idx:] if idx >= 0 else ""


def status(profile: str) -> str:
    match = re.search(r"profile_status:\s*([^\n]+)", profile)
    return match.group(1).strip().strip('"') if match else "missing"


def count_list_items(section: str) -> int:
    return len(re.findall(r"^\s+-\s+", section, re.M))


def section(profile: str, key: str) -> str:
    pattern = rf"\n  {re.escape(key)}:\n(.*?)(?=\n  [a-zA-Z0-9_]+:|\Z)"
    match = re.search(pattern, "\n" + profile, re.S)
    return match.group(1) if match else ""


def audit_file(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="replace")
    profile = profile_text(text)
    blockers: list[dict[str, str]] = []
    current_status = status(profile)

    if not profile:
        blockers.append({
            "blocker_type": "missing_profile",
            "evidence": "bp_brawler_profile block not found",
            "required_fix": "create reviewed bp_brawler_profile from Fandom/PLP sources",
        })
    else:
        for token in AUTO_PLACEHOLDERS:
            if token in profile:
                blockers.append({
                    "blocker_type": "auto_placeholder",
                    "evidence": token,
                    "required_fix": "replace automatic placeholder with reviewed mechanism, condition, or remove field",
                })
        if count_list_items(section(profile, "failure_modes")) < 3:
            blockers.append({
                "blocker_type": "missing_failure_modes",
                "evidence": "fewer than 3 failure mode list items",
                "required_fix": "add at least 3 BP-consumable failure modes",
            })
        hooks = section(profile, "map_feature_hooks")
        if count_list_items(hooks) < 2:
            blockers.append({
                "blocker_type": "missing_map_hooks",
                "evidence": "fewer than 2 map hook list items",
                "required_fix": "add reviewed hooks with route, objective payoff, and failure condition",
            })
        if "example_maps: []" in profile or "example_maps:\n        - \"unknown_pending_review\"" in profile:
            blockers.append({
                "blocker_type": "missing_map_route_or_objective",
                "evidence": "empty example_maps or map hook not tied to concrete maps",
                "required_fix": "connect hooks to concrete Ranked maps or explicitly mark not reviewed",
            })
        if "mechanism:" not in profile:
            blockers.append({
                "blocker_type": "missing_mechanism",
                "evidence": "no mechanism field in matchup seeds",
                "required_fix": "add matchup mechanism or remove seed from reviewed scope",
            })
        if not all(slot in profile for slot in ["slot_1:", "slot_2_3:", "slot_4_5:", "slot_6:"]):
            blockers.append({
                "blocker_type": "missing_slot_specificity",
                "evidence": "one or more slot notes missing",
                "required_fix": "write slot-specific jobs and risks",
            })
        if "[[sources/Fandom-" not in profile or "[[sources/PLP-" not in profile:
            blockers.append({
                "blocker_type": "source_traceability_gap",
                "evidence": "profile missing Fandom or PLP source wikilink",
                "required_fix": "add source links to profile fields",
            })

    blocker_types = sorted({b["blocker_type"] for b in blockers})
    return {
        "brawler": path.stem,
        "path": str(path.relative_to(ROOT)),
        "current_status": current_status,
        "blocker_count": len(blockers),
        "blocker_types": blocker_types,
        "blockers": blockers,
        "can_upgrade_to_reviewed": len(blockers) == 0 and current_status in {"draft", "draft_from_raw_signals"},
        "can_upgrade_to_bp_ready": False,
    }


def render_markdown(rows: list[dict[str, object]]) -> str:
    counts: dict[str, int] = {}
    for row in rows:
        counts[str(row["current_status"])] = counts.get(str(row["current_status"]), 0) + 1
    blocker_counts: dict[str, int] = {}
    for row in rows:
        for blocker_type in row["blocker_types"]:
            blocker_counts[str(blocker_type)] = blocker_counts.get(str(blocker_type), 0) + 1

    lines = [
        "# 英雄 BP 建模质量审计",
        "",
        "状态：`quality_gate_audit`。生成日期：2026-06-30。",
        "",
        "本页由 `tools/audit_bp_profile_quality.py` 根据 [[syntheses/英雄BP建模质量门槛|英雄 BP 建模质量门槛]] 生成。它只审计结构和明显占位符，不替代人工机制复核。",
        "",
        "## 汇总",
        "",
        f"- 审计英雄数：{len(rows)}",
    ]
    for key in sorted(counts):
        lines.append(f"- 当前状态 `{key}`：{counts[key]}")
    lines.extend([
        f"- 可直接升级 reviewed：{sum(1 for row in rows if row['can_upgrade_to_reviewed'])}",
        f"- 可直接升级 bp_ready：0",
        "",
        "## 阻塞类型统计",
        "",
    ])
    for key, value in sorted(blocker_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{key}`：{value}")
    lines.extend([
        "",
        "## 英雄队列",
        "",
        "| brawler | current_status | blocker_count | blocker_types | next action |",
        "| --- | --- | ---: | --- | --- |",
    ])
    for row in sorted(rows, key=lambda r: (-int(r["blocker_count"]), str(r["brawler"]))):
        blockers = ", ".join(f"`{b}`" for b in row["blocker_types"]) or "none"
        if row["can_upgrade_to_reviewed"]:
            action = "eligible_for_reviewed"
        elif row["current_status"] == "bp_ready" and row["blocker_count"] == 0:
            action = "bp_ready_structural_gate_passed"
        elif row["current_status"] == "reviewed" and row["blocker_count"] == 0:
            action = "needs_reviewed_edges_and_ranked_map_hooks_for_bp_ready"
        else:
            action = "review_and_fix_blockers"
        lines.append(
            f"| [[entities/brawlers/{row['brawler']}|{row['brawler']}]] | `{row['current_status']}` | {row['blocker_count']} | {blockers} | {action} |"
        )
    lines.extend([
        "",
        "## 关联页面",
        "",
        "- [[syntheses/英雄BP建模质量门槛|英雄 BP 建模质量门槛]]",
        "- [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]",
        "- [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]",
        "- [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    rows = [audit_file(path) for path in sorted(ENTITY_DIR.glob("*.md"))]
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        markdown = render_markdown(rows)
        if args.write:
            OUT.write_text(markdown, encoding="utf-8")
            print(OUT.relative_to(ROOT))
        else:
            print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
