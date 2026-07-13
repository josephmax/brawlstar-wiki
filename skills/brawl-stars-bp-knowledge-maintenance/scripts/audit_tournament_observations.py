#!/usr/bin/env python3
"""Audit tournament observations for stable-fact coverage gaps without promoting them."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--observation-profile", required=True)
    parser.add_argument("--runtime-index", help="Optional compiled runtime index for weak-fit review seeds.")
    parser.add_argument("--repo", default=str(ROOT))
    parser.add_argument("--min-pick-sets", type=int, default=2)
    parser.add_argument("--output", help="Write Markdown report under outputs/.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def runtime_payload(data: dict[str, Any]) -> dict[str, Any]:
    return data.get("runtime_bp_index", data)


def audit(profile: dict[str, Any], repo: Path, runtime: dict[str, Any] | None, min_pick_sets: int) -> dict[str, Any]:
    brawler_dir = repo / "wiki/entities/brawlers"
    map_dir = repo / "wiki/entities/maps"
    gaps: list[dict[str, Any]] = []
    global_names = {row["brawler"] for row in profile["scopes"]["global"]}
    for name in sorted(global_names):
        if not (brawler_dir / f"{name}.md").exists():
            gaps.append({"type": "missing_brawler_entity", "brawler": name, "status": "maintenance_blocker"})
    for map_name, scope in profile["scopes"]["map"].items():
        if not (map_dir / f"{map_name}.md").exists():
            gaps.append({"type": "missing_map_entity", "map": map_name, "mode": scope["mode"], "status": "source_ingest_needed"})

    if runtime:
        signature = runtime_payload(runtime).get("map_pool_signature", {})
        for map_name, scope in profile["scopes"]["map"].items():
            runtime_map = signature.get(map_name)
            if not runtime_map:
                continue
            candidate_index = runtime_map.get("candidate_index", {})
            for row in scope["rows"]:
                if row["pick_sets"] < min_pick_sets:
                    continue
                card = candidate_index.get(row["brawler"])
                if not card:
                    gaps.append({
                        "type": "runtime_candidate_missing",
                        "map": map_name,
                        "brawler": row["brawler"],
                        "pick_sets": row["pick_sets"],
                        "status": "compile_coverage_review",
                    })
                elif card.get("map_floor_fit") in {"weak", "none", None}:
                    gaps.append({
                        "type": "observed_without_concrete_map_fit",
                        "map": map_name,
                        "brawler": row["brawler"],
                        "pick_sets": row["pick_sets"],
                        "compiled_map_floor_fit": card.get("map_floor_fit"),
                        "status": "needs_vod_and_draft_context_review",
                    })
    return {
        "schema": "tournament_knowledge_gap_audit.v1",
        "source_profile_schema": profile.get("schema"),
        "policy": "review seeds only; no automatic entity or runtime promotion",
        "summary": {
            "gap_count": len(gaps),
            "missing_brawler_entities": sum(item["type"] == "missing_brawler_entity" for item in gaps),
            "missing_map_entities": sum(item["type"] == "missing_map_entity" for item in gaps),
            "runtime_review_seeds": sum(item["type"] in {"runtime_candidate_missing", "observed_without_concrete_map_fit"} for item in gaps),
        },
        "gaps": gaps,
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Tournament Observation Knowledge-Gap Audit",
        "",
        f"- schema: `{report['schema']}`",
        f"- gaps: {report['summary']['gap_count']}",
        "- boundary: review seeds only; no automatic entity or runtime promotion",
        "",
        "| 类型 | 地图 | 英雄 | 观察 | 状态 |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for item in report["gaps"]:
        lines.append(
            f"| {item['type']} | {item.get('map', '-')} | {item.get('brawler', '-')} | {item.get('pick_sets', '-')} | {item['status']} |"
        )
    if not report["gaps"]:
        lines.append("| none | - | - | - | clean |")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).resolve()
    profile_path = Path(args.observation_profile) if Path(args.observation_profile).is_absolute() else repo / args.observation_profile
    runtime_path = None if not args.runtime_index else (Path(args.runtime_index) if Path(args.runtime_index).is_absolute() else repo / args.runtime_index)
    report = audit(load_json(profile_path), repo, load_json(runtime_path) if runtime_path else None, args.min_pick_sets)
    text = render_markdown(report)
    if args.output:
        output = Path(args.output) if Path(args.output).is_absolute() else repo / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        print(f"WROTE {output.relative_to(repo) if output.is_relative_to(repo) else output}")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
