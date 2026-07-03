#!/usr/bin/env python3
"""Coordinate runtime_bp_index lookup and compile locks for BP decide mode."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import socket
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_INDEX_DIR = "outputs/runtime-bp-index"
DEFAULT_STRENGTH_PROFILE_ID = "default_current_version_unknown"


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return utc_now().isoformat()


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def short_hash(payload: Any) -> str:
    data = json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode("utf-8")).hexdigest()[:16]


def safe_key(value: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in ("-", "_", ".") else "-" for ch in value.strip())
    return cleaned.strip(".-") or "runtime-index"


def derive_index_key(args: argparse.Namespace) -> str:
    if args.index_key:
        return safe_key(args.index_key)

    payload = {
        "patch_id": args.patch_id or "default-current",
        "map_pool_id": args.map_pool_id or "current-ranked",
        "available_pool": sorted(args.available_pool),
        "strength_profile_id": args.strength_profile_id or DEFAULT_STRENGTH_PROFILE_ID,
        "strength_profile_hash": args.strength_profile_hash or "unknown",
    }
    return f"bp-{short_hash(payload)}"


def compute_compile_input_hash(args: argparse.Namespace, runtime_index_key: str) -> str:
    if args.compile_input_hash:
        return args.compile_input_hash
    payload = {
        "runtime_index_key": runtime_index_key,
        "patch_id": args.patch_id,
        "map_pool_id": args.map_pool_id,
        "available_pool": sorted(args.available_pool),
        "strength_profile_id": args.strength_profile_id or DEFAULT_STRENGTH_PROFILE_ID,
        "strength_profile_hash": args.strength_profile_hash,
    }
    return short_hash(payload)


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None


def extract_manifest(payload: dict[str, Any] | None) -> dict[str, Any] | None:
    if not payload:
        return None
    if "runtime_bp_index" in payload and isinstance(payload["runtime_bp_index"], dict):
        payload = payload["runtime_bp_index"]
    manifest = payload.get("manifest")
    return manifest if isinstance(manifest, dict) else None


def index_validation_error(index_path: Path, args: argparse.Namespace) -> str | None:
    manifest = extract_manifest(read_json(index_path))
    if manifest is None:
        return "missing_or_invalid_manifest"

    expected_fields = {
        "patch_id": args.patch_id,
        "map_pool_id": args.map_pool_id,
        "strength_profile_id": args.strength_profile_id,
        "strength_profile_hash": args.strength_profile_hash,
    }
    for field, expected in expected_fields.items():
        if expected and str(manifest.get(field, "")) != str(expected):
            return f"manifest_mismatch:{field}"
    return None


def index_is_valid(index_path: Path, args: argparse.Namespace) -> bool:
    return index_path.exists() and index_validation_error(index_path, args) is None


def default_owner() -> str:
    user = os.environ.get("USER") or os.environ.get("LOGNAME") or "unknown-user"
    return f"{user}@{socket.gethostname()}:{os.getpid()}"


def create_lock(lock_path: Path, payload: dict[str, Any]) -> bool:
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    try:
        fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        handle.write(data)
    return True


def lock_age_seconds(lock_path: Path) -> float | None:
    payload = read_json(lock_path) or {}
    started_at = parse_iso(payload.get("started_at"))
    if started_at is None:
        return None
    return (utc_now() - started_at).total_seconds()


def make_lock_payload(
    args: argparse.Namespace,
    runtime_index_key: str,
    compile_input_hash: str,
    attempt: int,
) -> dict[str, Any]:
    return {
        "state": "compiling",
        "runtime_index_key": runtime_index_key,
        "owner": args.owner or default_owner(),
        "started_at": iso_now(),
        "compile_input_hash": compile_input_hash,
        "attempt": attempt,
    }


def poll_for_index(index_path: Path, args: argparse.Namespace) -> bool:
    for poll in range(max(args.max_polls, 0)):
        if index_is_valid(index_path, args):
            return True
        if poll + 1 < args.max_polls and args.poll_delay > 0:
            time.sleep(args.poll_delay)
    return False


def output(payload: dict[str, Any], json_mode: bool) -> None:
    if json_mode:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    for key, value in payload.items():
        print(f"{key}: {value}")


def release_lock(lock_path: Path, args: argparse.Namespace, runtime_index_key: str) -> int:
    if not lock_path.exists():
        payload = {
            "status": "released",
            "runtime_index_key": runtime_index_key,
            "lock_path": str(lock_path),
            "lock_existed": False,
        }
        output(payload, args.json)
        return 0

    try:
        lock_path.unlink()
    except OSError as exc:
        payload = {
            "status": "runtime_index_compile_failed",
            "runtime_index_key": runtime_index_key,
            "reason": f"lock_release_failed:{exc}",
            "lock_path": str(lock_path),
            "lock_owned": False,
        }
        output(payload, args.json)
        return 2

    payload = {
        "status": "released",
        "runtime_index_key": runtime_index_key,
        "lock_path": str(lock_path),
        "lock_existed": True,
    }
    output(payload, args.json)
    return 0


def run_precheck(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    index_dir = Path(args.index_dir)
    if not index_dir.is_absolute():
        index_dir = repo / index_dir

    runtime_index_key = derive_index_key(args)
    compile_input_hash = compute_compile_input_hash(args, runtime_index_key)
    index_path = index_dir / f"{runtime_index_key}.json"
    lock_path = index_dir / f"{runtime_index_key}.lock"

    base_payload: dict[str, Any] = {
        "runtime_index_key": runtime_index_key,
        "index_path": str(index_path),
        "lock_path": str(lock_path),
    }

    if args.release_lock:
        return release_lock(lock_path, args, runtime_index_key)

    validation_error = index_validation_error(index_path, args) if index_path.exists() else None
    if index_path.exists() and validation_error is None:
        payload = {
            **base_payload,
            "status": "ready",
            "lock_owned": False,
            "waited": False,
        }
        output(payload, args.json)
        return 0

    lock_payload = make_lock_payload(args, runtime_index_key, compile_input_hash, attempt=1)
    if create_lock(lock_path, lock_payload):
        payload = {
            **base_payload,
            "status": "compile_required",
            "lock_owned": True,
            "compile_input_hash": compile_input_hash,
            "index_validation_error": validation_error,
        }
        output(payload, args.json)
        return 0

    if poll_for_index(index_path, args):
        payload = {
            **base_payload,
            "status": "ready",
            "lock_owned": False,
            "waited": True,
        }
        output(payload, args.json)
        return 0

    age = lock_age_seconds(lock_path)
    if age is not None and age > args.stale_seconds:
        previous = read_json(lock_path) or {}
        try:
            lock_path.unlink()
        except OSError:
            lock_path = index_dir / f"{runtime_index_key}.lock"

        attempt = int(previous.get("attempt") or 1) + 1
        recovered_payload = make_lock_payload(args, runtime_index_key, compile_input_hash, attempt=attempt)
        if create_lock(lock_path, recovered_payload):
            payload = {
                **base_payload,
                "status": "compile_required",
                "lock_owned": True,
                "compile_input_hash": compile_input_hash,
                "recovered_stale_lock": True,
                "previous_lock_age_seconds": age,
            }
            output(payload, args.json)
            return 0

    payload = {
        **base_payload,
        "status": "runtime_index_compile_failed",
        "lock_owned": False,
        "reason": "missing_or_stale_runtime_bp_index_after_bounded_wait",
        "max_polls": args.max_polls,
        "stale_seconds": args.stale_seconds,
    }
    output(payload, args.json)
    return 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository root")
    parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR, help="Runtime index directory")
    parser.add_argument("--index-key", default="", help="Explicit runtime_index_key")
    parser.add_argument("--patch-id", default="", help="Expected manifest patch_id")
    parser.add_argument("--map-pool-id", default="", help="Expected manifest map_pool_id")
    parser.add_argument("--available-pool", action="append", default=[], help="Available brawler; repeatable")
    parser.add_argument("--strength-profile-id", default="", help="Expected manifest strength_profile_id")
    parser.add_argument("--strength-profile-hash", default="", help="Expected manifest strength_profile_hash")
    parser.add_argument("--compile-input-hash", default="", help="Compile input hash to store in the lock")
    parser.add_argument("--owner", default="", help="Lock owner label")
    parser.add_argument("--max-polls", type=int, default=12, help="Maximum polls when another compile owns the lock")
    parser.add_argument("--poll-delay", type=float, default=2.0, help="Seconds between polls")
    parser.add_argument("--stale-seconds", type=float, default=600.0, help="Lock age before one recovery attempt")
    parser.add_argument("--release-lock", action="store_true", help="Release the lock after compile completes")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    return parser.parse_args()


def main() -> int:
    return run_precheck(parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
