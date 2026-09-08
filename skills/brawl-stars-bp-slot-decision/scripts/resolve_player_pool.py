"""Resolve minimal official player rows from stdin using the canonical wiki index."""
import argparse
import json
import sys
from pathlib import Path
from compile_runtime_index import entity_brawler_names, load_alias_index, normalize_key


def resolve(repo: Path, rows: list[dict], min_power: int = 11) -> dict:
    names = set(entity_brawler_names(repo))
    aliases = load_alias_index(repo, names)
    resolved = []
    for row in rows:
        raw = row.get("name") or ""
        key = normalize_key(raw)
        name = aliases.get(raw) or (aliases.get(key) if key else None)
        power = row.get("power")
        if not isinstance(power, int) or isinstance(power, bool) or power < 1:
            raise ValueError("player power must be a positive integer")
        reason = "unmapped" if name is None else "below_min_power" if power < min_power else None
        resolved.append({"id": row["id"], "name": raw, "canonical": name, "power": power, "reason": reason})
    return {"min_power": min_power, "brawlers": resolved,
            "eligible_ids": sorted({row["canonical"] for row in resolved if row["reason"] is None})}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    try:
        payload = json.load(sys.stdin)
        print(json.dumps(resolve(Path(args.repo), payload["brawlers"]), ensure_ascii=False))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(2)
