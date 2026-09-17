#!/usr/bin/env python3
"""Audit whether behavior-rework capability atoms reached a Brawler's matchup edges.

Capability-grounded matchup review per the balance-breakpoint-audit reference:
for each curated rework atom (ability atom + keyword group), check coverage in
(a) the Brawler's capability fields and (b) its ``conditional_matchups`` text.
Missing capability coverage flags an incomplete ingest fold; missing edge
coverage emits a review seed for a maintainer - never an auto-written edge.

The default atom spec covers the 2026-08 rework wave. Override it with
``--atoms-json`` for other waves; the spec maps Brawler name -> list of
``{"id": ..., "keywords": [...]}``.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DEFAULT_ATOMS: dict[str, list[dict[str, object]]] = {
    "Gus": [
        {"id": "knockback_spirit_gadget_knockback", "keywords": ["Knockback Spirit", "妙具击退", "gadget knockback"]},
        {"id": "kooky_popper_ammo_steal", "keywords": ["Kooky Popper", "缴弹", "ammo steal"]},
        {"id": "spirit_animal_speed_window", "keywords": ["Spirit Animal", "speed window", "移速窗口"]},
        {"id": "spooky_pop_wall_pierce_balloon", "keywords": ["Spooky Pop", "穿墙气球"]},
        {"id": "health_bonanza_buffie_homing_spirits", "keywords": ["homing spirit", "追踪灵体", "Health Bonanza Buffie"]},
    ],
    "Poco": [
        {"id": "protective_tunes_purge", "keywords": ["Protective Tunes", "净化"]},
        {"id": "tuning_fork_pulse_heal", "keywords": ["Tuning Fork", "脉冲治疗"]},
        {"id": "da_capo_baseline_heal", "keywords": ["Da Capo", "常驻治疗"]},
    ],
    "El Primo": [
        {"id": "suplex_supplement_grab_throw", "keywords": ["Suplex", "抓取投掷"]},
        {"id": "asteroid_belt_intercept", "keywords": ["Asteroid Belt", "完全免伤", "拦截投射物"]},
        {"id": "gravity_leap_pull", "keywords": ["Gravity Leap", "拉拽"]},
    ],
    "Amber": [
        {"id": "fire_starters_barrel", "keywords": ["Fire Starters", "油桶"]},
        {"id": "wild_flames_oil_trail", "keywords": ["Wild Flames", "油迹"]},
        {"id": "scorching_siphon_trigger", "keywords": ["Scorching Siphon"]},
    ],
    "Chuck": [
        {"id": "super_four_charge_rework", "keywords": ["charge pool", "4 充能", "开局满 Super"]},
        {"id": "rerouting_buffie_damage_shield", "keywords": ["damage-reduction shield", "减伤盾"]},
        {"id": "full_steam_ahead_fire_trail", "keywords": ["fire trail", "火区"]},
        {"id": "hyper_buffie_triple_shot", "keywords": ["additional projectiles", "三连发"]},
    ],
    "Shade": [
        {"id": "jump_scare_short_hop_fear", "keywords": ["Jump Scare", "落地恐惧"]},
        {"id": "frightener_in_wall_heal", "keywords": ["Frightener", "墙内回血"]},
        {"id": "spooky_speedster_move_speed", "keywords": ["Spooky Speedster"]},
    ],
}

FOLD_SECTION_NAMES = ("capability_vector", "build_switches", "map_feature_hooks", "objective_contracts")
EDGE_SECTION_NAMES = ("conditional_matchups",)


def extract_yaml_block(page_text: str) -> str | None:
    match = re.search(r"```yaml\n(.*?)```", page_text, re.S)
    return match.group(1) if match else None


def extract_section(yaml_text: str, section: str) -> str:
    match = re.search(rf"^  {section}:\n(.*?)(?=^  [a-z_]+:|\Z)", yaml_text, re.S | re.M)
    return match.group(1) if match else ""


def text_hits(text: str, keywords: list[str]) -> list[str]:
    lowered = text.lower()
    return [kw for kw in keywords if kw.lower() in lowered]


def audit_brawler(yaml_text: str, atoms: list[dict[str, object]]) -> dict[str, object]:
    fold_sections = {name: extract_section(yaml_text, name) for name in FOLD_SECTION_NAMES}
    edge_sections = {name: extract_section(yaml_text, name) for name in EDGE_SECTION_NAMES}
    fold_text = "\n".join(fold_sections.values())
    edge_text = "\n".join(edge_sections.values())
    results: list[dict[str, object]] = []
    for atom in atoms:
        atom_id = str(atom["id"])
        keywords = list(atom["keywords"])  # type: ignore[arg-type]
        capability_hits = text_hits(fold_text, keywords)
        edge_hits = text_hits(edge_text, keywords)
        edge_hits = text_hits(edge_text, keywords)
        matching_edges: list[str] = []
        if edge_hits:
            for block in re.split(r"\n    - ", edge_text):
                if text_hits(block, keywords):
                    snippet = " ".join(block.split())[:160]
                    matching_edges.append(snippet)
        results.append(
            {
                "atom": atom_id,
                "keywords": keywords,
                "capability_covered": bool(capability_hits),
                "capability_hits": capability_hits,
                "edge_covered": bool(edge_hits),
                "matching_edges": matching_edges,
                "review_seed": not edge_hits,
            }
        )
    return {
        "stable_fields_present": any(fold_sections.values()),
        "conditional_matchups_section_present": bool(edge_sections["conditional_matchups"]),
        "atoms": results,
        "review_seeds": [r["atom"] for r in results if r["review_seed"]],
        "fold_gaps": [r["atom"] for r in results if not r["capability_covered"]],
    }


def audit_repo(entity_dir: Path, atoms_spec: dict[str, list[dict[str, object]]], brawlers: list[str] | None = None):
    requested = brawlers or sorted(atoms_spec)
    report: dict[str, object] = {}
    missing_pages: list[str] = []
    for name in requested:
        atoms = atoms_spec.get(name)
        if atoms is None:
            missing_pages.append(name)
            continue
        page = entity_dir / f"{name}.md"
        if not page.exists():
            missing_pages.append(name)
            continue
        yaml_text = extract_yaml_block(page.read_text(encoding="utf-8"))
        if yaml_text is None:
            missing_pages.append(name)
            continue
        report[name] = audit_brawler(yaml_text, atoms)
    return report, missing_pages


def render_markdown(report: dict[str, object], missing_pages: list[str]) -> str:
    lines = ["# Capability-Rework Edge Coverage Review", ""]
    lines.append("Review seeds only; edges are never written by this audit. See balance-breakpoint-audit reference.")
    lines.append("")
    for name, result in report.items():  # type: ignore[assignment]
        lines.append(f"## {name}")
        if not result["conditional_matchups_section_present"]:  # type: ignore[index]
            lines.append("- no conditional_matchups section found")
        for atom in result["atoms"]:  # type: ignore[index]
            status_cap = "cap=ok" if atom["capability_covered"] else "cap=MISSING(fold gap)"
            status_edge = "edge=ok" if atom["edge_covered"] else "edge=SEED"
            lines.append(f"- `{atom['atom']}` {status_cap} {status_edge}")
        if result["review_seeds"]:  # type: ignore[index]
            lines.append(f"- review seeds: {', '.join(result['review_seeds'])}")  # type: ignore[arg-type]
        if result["fold_gaps"]:  # type: ignore[index]
            lines.append(f"- fold gaps (fix entity fields first): {', '.join(result['fold_gaps'])}")  # type: ignore[arg-type]
        lines.append("")
    if missing_pages:
        lines.append(f"## Missing pages or no atom spec: {', '.join(missing_pages)}")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entity-dir", type=Path, default=Path("wiki/entities/brawlers"))
    parser.add_argument("--brawler", action="append", default=[], help="Brawler to audit; repeatable (default: all in spec)")
    parser.add_argument("--atoms-json", type=Path, default=None, help="Override the default rework-atom spec")
    parser.add_argument("--json-output", type=Path, default=None)
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args(argv)

    atoms_spec = DEFAULT_ATOMS
    if args.atoms_json:
        atoms_spec = json.loads(args.atoms_json.read_text(encoding="utf-8"))

    report, missing_pages = audit_repo(args.entity_dir, atoms_spec, args.brawler or None)
    payload = {"review_seeds": report, "missing": missing_pages}
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(render_markdown(report, missing_pages), encoding="utf-8")
    total_seeds = sum(len(r["review_seeds"]) for r in report.values())  # type: ignore[index]
    total_gaps = sum(len(r["fold_gaps"]) for r in report.values())  # type: ignore[index]
    print(json.dumps({"brawlers_audited": len(report), "review_seeds": total_seeds, "fold_gaps": total_gaps}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
