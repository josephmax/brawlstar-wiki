#!/usr/bin/env python3
"""Read-only helper for locating Brawl Stars BP skill references and entity inputs."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


SKILL_REFERENCE_PAGES = [
    "skills/brawl-stars-bp-slot-decision/references/compile-knowledge.md",
    "skills/brawl-stars-bp-slot-decision/references/runtime-decision-knowledge.md",
]


def normalize(value: str) -> str:
    return re.sub(r"[^0-9a-z]+", "", value.casefold())


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def rel(path: Path, repo: Path) -> str:
    try:
        return str(path.relative_to(repo))
    except ValueError:
        return str(path)


def find_named_page(repo: Path, subdir: str, name: str) -> Path | None:
    wanted = normalize(name)
    directory = repo / subdir
    if not directory.exists():
        return None

    exact = directory / f"{name}.md"
    if exact.exists():
        return exact

    for path in directory.glob("*.md"):
        if normalize(path.stem) == wanted:
            return path
    return None


def extract_mode(path: Path) -> str | None:
    text = read_text(path)
    for pattern in (r"^\s*mode:\s*`?([^`\n]+?)`?\s*$", r"^- 模式：`?([^`\n]+?)`?\s*$"):
        match = re.search(pattern, text, flags=re.MULTILINE)
        if match:
            return match.group(1).strip()
    return None


def extract_profile_status(path: Path) -> str | None:
    match = re.search(r"^\s*profile_status:\s*(.+?)\s*$", read_text(path), flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def markdown_line_hits(path: Path, terms: Iterable[str], limit: int) -> list[dict[str, str | int]]:
    text = read_text(path)
    normalized_terms = [normalize(term) for term in terms if term]
    if not text or not normalized_terms:
        return []

    hits: list[tuple[int, int, str]] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        normalized_line = normalize(line)
        score = sum(1 for term in normalized_terms if term in normalized_line)
        if score:
            hits.append((score, line_no, line))

    hits.sort(key=lambda item: (-item[0], item[1]))
    return [{"line": line_no, "text": line} for _, line_no, line in hits[:limit]]


def build_payload(args: argparse.Namespace) -> dict:
    repo = Path(args.repo).resolve()
    map_path = find_named_page(repo, "wiki/entities/maps", args.map) if args.map else None

    brawler_names = []
    for name in args.brawler + args.enemy:
        if name not in brawler_names:
            brawler_names.append(name)

    brawlers: dict[str, dict[str, str | None]] = {}
    for name in brawler_names:
        path = find_named_page(repo, "wiki/entities/brawlers", name)
        brawlers[name] = {
            "path": rel(path, repo) if path else None,
            "profile_status": extract_profile_status(path) if path else None,
        }

    search_terms = list(brawler_names)
    if args.map:
        search_terms.append(args.map)
    if args.mode:
        search_terms.append(args.mode)

    source_paths: list[Path] = []
    if map_path:
        source_paths.append(map_path)
    for info in brawlers.values():
        path_value = info["path"]
        if path_value:
            source_paths.append(repo / str(path_value))

    return {
        "repo": str(repo),
        "skill_reference_pages": [
            {"path": page, "exists": (repo / page).exists()} for page in SKILL_REFERENCE_PAGES
        ],
        "map": {
            "name": args.map,
            "path": rel(map_path, repo) if map_path else None,
            "mode": extract_mode(map_path) if map_path else args.mode,
            "pool_membership": "user_supplied_or_compiled_runtime_index_required",
        },
        "brawlers": brawlers,
        "stable_source_hits": [
            {
                "path": rel(path, repo),
                "hits": markdown_line_hits(path, search_terms, args.limit),
            }
            for path in source_paths
        ],
        "reminders": [
            "Read matched pages before deciding; this script only retrieves candidates.",
            "Before decide, run runtime_index_precheck; it may return ready, compile_required, or runtime_index_compile_failed.",
            "Do not use coarse map tags as direct scoring signals.",
        ],
    }


def print_text(payload: dict) -> None:
    print(f"repo: {payload['repo']}")
    print("skill_reference_pages:")
    for page in payload["skill_reference_pages"]:
        mark = "ok" if page["exists"] else "missing"
        print(f"  - [{mark}] {page['path']}")

    map_info = payload["map"]
    if map_info["name"]:
        print("map:")
        print(f"  name: {map_info['name']}")
        print(f"  path: {map_info['path']}")
        print(f"  mode: {map_info['mode']}")
        print(f"  pool_membership: {map_info['pool_membership']}")

    if payload["brawlers"]:
        print("brawlers:")
        for name, info in payload["brawlers"].items():
            print(f"  - {name}: {info['path']} ({info['profile_status']})")

    print("stable_source_hits:")
    for source in payload["stable_source_hits"]:
        print(f"  - {source['path']}:")
        for hit in source["hits"]:
            print(f"    - L{hit['line']}: {hit['text']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository root containing wiki/")
    parser.add_argument("--map", default="", help="Map name, e.g. Safe Zone")
    parser.add_argument("--mode", default="", help="Mode name when map is unknown")
    parser.add_argument("--brawler", action="append", default=[], help="Known own or candidate brawler; repeatable")
    parser.add_argument("--enemy", action="append", default=[], help="Known enemy brawler; repeatable")
    parser.add_argument("--limit", type=int, default=12, help="Maximum hits per index")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = build_payload(args)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_text(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
