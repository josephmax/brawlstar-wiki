"""Caller-defined recall windows over root entities; related facts stay intact."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def read_mask(path: str | None) -> dict[str, Any] | None:
    if not path:
        return None
    raw = Path(path).read_bytes()
    if len(raw) > 100_000:
        raise ValueError("candidate mask is too large")
    mask = json.loads(raw)
    if not isinstance(mask, dict) or mask.get("schema") != "candidate_mask.v1":
        raise ValueError("unsupported candidate mask schema")
    if mask.get("mode") not in ("allowlist", "unrestricted"):
        raise ValueError("invalid candidate mask mode")
    ids = mask.get("ids")
    if not isinstance(ids, list) or len(ids) > 1000 or any(not isinstance(x, str) or not x for x in ids):
        raise ValueError("candidate mask ids must be a list of canonical names")
    if mask["mode"] == "unrestricted" and ids:
        raise ValueError("unrestricted mask must not contain ids")
    if not isinstance(mask.get("index_source_hash"), str) or not mask["index_source_hash"]:
        raise ValueError("candidate mask must bind to index_source_hash")
    return {**mask, "ids": sorted(set(ids)), "hash": hashlib.sha256(raw).hexdigest()}


def validate_mask(mask: dict[str, Any] | None, index: dict[str, Any]) -> None:
    if mask is None:
        return
    if mask["index_source_hash"] != index["manifest"].get("source_hash"):
        raise ValueError("candidate mask/index version mismatch")
    unknown = set(mask["ids"]) - set(index["brawler_runtime_cards"])
    if unknown:
        raise ValueError("candidate mask contains unknown canonical names: " + ", ".join(sorted(unknown)))


def allows(mask: dict[str, Any] | None, name: str) -> bool:
    return mask is None or mask["mode"] == "unrestricted" or name in mask["ids"]


def mask_summary(mask: dict[str, Any] | None) -> dict[str, Any]:
    return {
        "applied": mask is not None and mask["mode"] == "allowlist",
        "mode": mask["mode"] if mask else "unrestricted",
        "visible_id_count": len(mask["ids"]) if mask and mask["mode"] == "allowlist" else None,
        "context_id": mask.get("context_id") if mask else None,
        "hash": mask["hash"] if mask else None,
    }
