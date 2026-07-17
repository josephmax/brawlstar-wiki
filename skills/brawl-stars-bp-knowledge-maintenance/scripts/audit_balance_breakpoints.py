#!/usr/bin/env python3
"""Audit kill and survival breakpoint changes across ordered balance patches.

This is a maintenance-time evidence generator.  It intentionally does not rank
Brawlers or produce draft recommendations.  Inputs stay source-first:

* the active roster and each Brawler's latest direct Fandom raw capture provide
  current Power 1 base health;
* source-summary Markdown files provide fenced JSON ``balance_patch_manifest``
  blocks;
* Brawler entity pages may provide fenced JSON ``combat_breakpoint_profile``
  blocks for explicit, condition-bearing defensive states.

All comparisons are performed at one requested power level (Power 11 by
default).  The generic Shield gear is a fixed +900 shield at Power 11 and is
therefore never multiplied by the Power 1 -> Power 11 stat scale.
"""

from __future__ import annotations

import argparse
import copy
import itertools
import json
import re
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_ROSTER = ROOT / "raw/sources/roster/brawlers-roster-2026-06-29.md"
DEFAULT_FANDOM_DIR = ROOT / "raw/sources/fandom/heroes"
DEFAULT_ENTITY_DIR = ROOT / "wiki/entities/brawlers"
DEFAULT_SOURCE_DIR = ROOT / "wiki/sources"
DEFAULT_OUTPUT_DIR = ROOT / "outputs/balance-breakpoints"

MANIFEST_SCHEMA = "balance_breakpoint_manifest.v1"
PROFILE_SCHEMA = "brawler_breakpoint_profile.v1"
OUTPUT_SCHEMA = "balance_breakpoint_audit.v1"
SHIELD_GEAR_P11 = Fraction(900)
SUPPORTED_CHANGE_KINDS = {"damage_packet", "target_state", "defense_modifier"}
CHANGE_CLASSES = {
    "breakpoint_supported",
    "temporal_survival_excluded",
    "non_breakpoint",
    "unsupported_mechanic",
    "source_conflict",
}


@dataclass(frozen=True)
class RosterEntry:
    name: str
    fandom_url: str
    slug: str


@dataclass(frozen=True)
class BaseTarget:
    name: str
    slug: str
    raw_path: Path
    health_p1: Fraction


@dataclass(frozen=True)
class Patch:
    patch_id: str
    order_key: tuple[Any, ...]
    source_path: Path
    payload: dict[str, Any]

    @property
    def changes(self) -> list[dict[str, Any]]:
        value = self.payload.get("changes", [])
        return [item for item in value if isinstance(item, dict)]


@dataclass
class WorldState:
    base_health: dict[str, Fraction]
    state_health: dict[tuple[str, str], Fraction]
    packet_damage: dict[tuple[str, str], Fraction]
    defense_overrides: dict[tuple[str, str], Fraction]

    def clone(self) -> "WorldState":
        return WorldState(
            base_health=dict(self.base_health),
            state_health=dict(self.state_health),
            packet_damage=dict(self.packet_damage),
            defense_overrides=dict(self.defense_overrides),
        )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--roster", type=Path, default=DEFAULT_ROSTER)
    parser.add_argument("--fandom-dir", type=Path, default=DEFAULT_FANDOM_DIR)
    parser.add_argument("--entity-dir", type=Path, default=DEFAULT_ENTITY_DIR)
    parser.add_argument(
        "--patch-source",
        "--manifest-source",
        dest="patch_source",
        type=Path,
        action="append",
        default=[],
        help="Markdown source page containing a balance_patch_manifest JSON block; repeatable",
    )
    parser.add_argument(
        "--patch-id",
        action="append",
        default=[],
        help="Keep only this patch in report sections after replaying the complete ordered chain; repeatable",
    )
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--power-level", type=int, default=11, choices=range(1, 12))
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--json-output", "--output", dest="json_output", type=Path)
    parser.add_argument("--markdown-output", "--report", dest="markdown_output", type=Path)
    return parser.parse_args(argv)


def parse_fraction(value: Any, *, field: str = "value") -> Fraction:
    """Parse an integer, decimal, ratio, or percentage without float drift."""

    if isinstance(value, bool) or value is None:
        raise ValueError(f"{field} must be numeric, got {value!r}")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, float):
        return Fraction(str(value))
    if isinstance(value, str):
        text = value.strip().replace(",", "")
        if not text:
            raise ValueError(f"{field} must not be empty")
        if text.endswith("%"):
            return Fraction(text[:-1].strip()) / 100
        try:
            return Fraction(text)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"{field} must be numeric, got {value!r}") from exc
    raise ValueError(f"{field} must be numeric, got {type(value).__name__}")


def power_multiplier(power_level: int) -> Fraction:
    """Return the Brawl Stars linear stat multiplier for Power 1..11."""

    if not 1 <= power_level <= 11:
        raise ValueError("power_level must be between 1 and 11")
    return Fraction(power_level + 9, 10)


def scale_between_powers(value: Any, from_power: int, to_power: int = 11) -> Fraction:
    number = parse_fraction(value)
    return number * power_multiplier(to_power) / power_multiplier(from_power)


def effective_health(
    health: Any,
    *,
    flat_shield: Any = 0,
    damage_reductions: Iterable[Any] = (),
) -> Fraction:
    """Convert health, flat shields, and distinct additive DR to exact EHP."""

    hp = parse_fraction(health, field="health")
    shield = parse_fraction(flat_shield, field="flat_shield")
    reductions = [parse_fraction(item, field="damage_reduction") for item in damage_reductions]
    reduction = sum(reductions, Fraction(0))
    if hp < 0 or shield < 0:
        raise ValueError("health and flat_shield must be non-negative")
    if reduction < 0 or reduction >= 1:
        raise ValueError("additive damage reduction must be in [0, 1)")
    return (hp + shield) / (1 - reduction)


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def hits_to_kill(ehp: Any, packet_damage: Any) -> int:
    durability = parse_fraction(ehp, field="effective_health")
    damage = parse_fraction(packet_damage, field="packet_damage")
    if durability <= 0:
        return 0
    if damage <= 0:
        raise ValueError("packet_damage must be positive")
    return ceil_fraction(durability / damage)


def json_number(value: Fraction | int) -> int | str:
    number = value if isinstance(value, Fraction) else Fraction(value)
    if number.denominator == 1:
        return number.numerator
    return f"{number.numerator}/{number.denominator}"


def slugify(text: str) -> str:
    text = unquote(text).replace("_", " ").replace("&", " ").replace(".", " ")
    return re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()


def slug_from_url_or_name(url: str, name: str) -> str:
    if url and url != "no_page_found":
        leaf = urlparse(url).path.rstrip("/").split("/")[-1]
    else:
        leaf = name
    return slugify(leaf)


def parse_roster(path: Path) -> list[RosterEntry]:
    rows: list[RosterEntry] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or "---" in line or line.startswith("| canonical_name"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        name, fandom_url = cells[:2]
        if fandom_url == "no_page_found":
            continue
        rows.append(RosterEntry(name, fandom_url, slug_from_url_or_name(fandom_url, name)))
    return rows


def capture_rank(path: Path, text: str | None = None) -> tuple[str, int, str]:
    head = text if text is not None else path.read_text(encoding="utf-8", errors="replace")[:600]
    match = re.search(r"^- Capture date: (\d{4}-\d{2}-\d{2})(?:-v(\d+))?", head, re.M)
    if match:
        return match.group(1), int(match.group(2) or 0), path.name
    match = re.search(r"-(\d{4}-\d{2}-\d{2})(?:-v(\d+))?\.md$", path.name)
    if match:
        return match.group(1), int(match.group(2) or 0), path.name
    return "0000-00-00", 0, path.name


def raw_slug(path: Path) -> str:
    return re.sub(r"-\d{4}-\d{2}-\d{2}(?:-v\d+)?\.md$", "", path.name)


def extract_raw_name(text: str) -> str | None:
    match = re.search(r"^# Direct Raw Capture: Fandom (.+)$", text, re.M)
    return match.group(1).strip() if match else None


def extract_infobox(text: str) -> dict[str, str]:
    match = re.search(r"^## Infobox Fields\n\n(.*?)(?:\n## |\Z)", text, re.S | re.M)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if line.startswith("- ") and ": " in line:
            key, value = line[2:].split(": ", 1)
            fields[key.strip()] = value.strip()
    return fields


def first_numeric(value: str, *, field: str) -> Fraction:
    match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
    if not match:
        raise ValueError(f"{field} has no numeric value: {value!r}")
    return parse_fraction(match.group(0), field=field)


def discover_latest_raws(fandom_dir: Path) -> dict[str, tuple[Path, str]]:
    latest: dict[str, tuple[Path, str]] = {}
    for path in fandom_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "# Direct Raw Capture: Fandom " not in text[:300]:
            continue
        slug = raw_slug(path)
        previous = latest.get(slug)
        if previous is None or capture_rank(path, text[:600]) > capture_rank(previous[0], previous[1][:600]):
            latest[slug] = (path, text)
    return latest


def load_base_targets(
    roster_path: Path,
    fandom_dir: Path,
) -> tuple[list[BaseTarget], list[dict[str, Any]], int]:
    """Load roster targets and active direct-raw additions such as Nori.

    Raw-only additions are included when they are direct captures and do not
    carry Fandom's ``FutureUpdate`` marker.  This lets a just-released Brawler
    participate in numeric auditing before PLP coverage or a BP entity profile
    exists, while keeping explicitly future-only pages out.
    """

    roster = parse_roster(roster_path)
    latest = discover_latest_raws(fandom_dir)
    requested: dict[str, str] = {row.slug: row.name for row in roster}
    for slug, (_, text) in latest.items():
        if slug in requested or "{{FutureUpdate}}" in text:
            continue
        name = extract_raw_name(text)
        if name:
            requested[slug] = name

    targets: list[BaseTarget] = []
    exclusions: list[dict[str, Any]] = []
    for slug, name in sorted(requested.items(), key=lambda item: item[1].casefold()):
        raw = latest.get(slug)
        if raw is None:
            exclusions.append({"scope": "base_health", "brawler": name, "reason": "latest_direct_raw_missing"})
            continue
        path, text = raw
        fields = extract_infobox(text)
        health_text = fields.get("Health") or fields.get("Health1")
        if not health_text:
            exclusions.append(
                {
                    "scope": "base_health",
                    "brawler": name,
                    "source": str(path),
                    "reason": "health_field_missing",
                }
            )
            continue
        try:
            health = first_numeric(health_text, field=f"{name}.Health")
        except ValueError as exc:
            exclusions.append(
                {
                    "scope": "base_health",
                    "brawler": name,
                    "source": str(path),
                    "reason": "health_field_unparseable",
                    "detail": str(exc),
                }
            )
            continue
        targets.append(BaseTarget(name, slug, path, health))
    return targets, exclusions, len(roster)


def fenced_json_objects(text: str) -> Iterator[dict[str, Any]]:
    for match in re.finditer(r"```json\s*\n(.*?)\n```", text, re.S | re.I):
        try:
            value = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            yield value


def extract_named_json(path: Path, key: str) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    for value in fenced_json_objects(text):
        if key in value and isinstance(value[key], dict):
            return value[key]
        # Tolerate a direct payload for hand-authored fixtures, while the
        # canonical repository form remains wrapped by the named top-level key.
        if value.get("schema") in {MANIFEST_SCHEMA, PROFILE_SCHEMA}:
            expected = MANIFEST_SCHEMA if key == "balance_patch_manifest" else PROFILE_SCHEMA
            if value.get("schema") == expected:
                return value
    return None


def patch_order(payload: Mapping[str, Any], source_path: Path) -> tuple[Any, ...]:
    effective = str(payload.get("effective_at", payload.get("effective_date", payload.get("date", ""))))
    explicit = payload.get("effective_order", payload.get("order"))
    if explicit is not None:
        try:
            return 0, int(explicit), effective, source_path.name
        except (TypeError, ValueError):
            return 0, str(explicit), effective, source_path.name
    return 1, effective, source_path.name


def discover_patch_sources(source_dir: Path) -> list[Path]:
    paths: list[Path] = []
    for path in source_dir.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if '"balance_patch_manifest"' in text:
            paths.append(path)
    return sorted(paths)


def load_patches(paths: Sequence[Path]) -> tuple[list[Patch], list[dict[str, Any]]]:
    patches: list[Patch] = []
    exclusions: list[dict[str, Any]] = []
    seen: set[str] = set()
    for path in paths:
        payload = extract_named_json(path, "balance_patch_manifest")
        if payload is None:
            exclusions.append({"scope": "patch", "source": str(path), "reason": "manifest_block_missing"})
            continue
        if payload.get("schema") != MANIFEST_SCHEMA:
            exclusions.append(
                {
                    "scope": "patch",
                    "source": str(path),
                    "reason": "manifest_schema_mismatch",
                    "observed": payload.get("schema"),
                }
            )
            continue
        patch_id = str(payload.get("patch_id") or payload.get("id") or path.stem)
        if patch_id in seen:
            exclusions.append({"scope": "patch", "source": str(path), "patch_id": patch_id, "reason": "duplicate_patch_id"})
            continue
        seen.add(patch_id)
        patches.append(Patch(patch_id, patch_order(payload, path), path, payload))
    return sorted(patches, key=lambda patch: patch.order_key), exclusions


def load_profiles(entity_dir: Path) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    profiles: dict[str, dict[str, Any]] = {}
    exclusions: list[dict[str, Any]] = []
    for path in sorted(entity_dir.glob("*.md")):
        profile = extract_named_json(path, "combat_breakpoint_profile")
        if profile is None:
            continue
        if profile.get("schema") != PROFILE_SCHEMA:
            exclusions.append(
                {
                    "scope": "defense_profile",
                    "brawler": path.stem,
                    "source": str(path),
                    "reason": "profile_schema_mismatch",
                    "observed": profile.get("schema"),
                }
            )
            continue
        profiles[path.stem] = profile
    return profiles, exclusions


def load_profile_packets(
    profiles: Mapping[str, Mapping[str, Any]],
    lookup: Mapping[str, str],
    output_power: int,
) -> tuple[
    dict[tuple[str, str], Fraction],
    dict[tuple[str, str], dict[str, Any]],
    list[dict[str, Any]],
]:
    values: dict[tuple[str, str], Fraction] = {}
    metadata: dict[tuple[str, str], dict[str, Any]] = {}
    exclusions: list[dict[str, Any]] = []
    for page_name, profile in profiles.items():
        brawler = canonical_name(profile.get("brawler") or page_name, lookup)
        if brawler not in lookup.values():
            continue
        for packet in profile_lists(profile, "damage_packets"):
            packet_id = str(packet.get("id") or packet.get("packet_id") or "").strip()
            if not packet_id:
                continue
            key = (brawler, packet_id)
            try:
                if packet.get("damage") is None:
                    raise ValueError("damage object missing")
                damage = scaled_amount(packet["damage"], output_power=output_power)
                repeat_model = str(packet.get("repeat_model") or "non_independent")
                active_when = text_list(packet.get("active_when"))
                values[key] = damage
                metadata[key] = {
                    "label": str(packet.get("label") or packet_id),
                    "conditions": active_when,
                    "repeat_model": repeat_model,
                    "packet_unit": str(packet.get("packet_unit") or "unspecified"),
                    "source": "combat_breakpoint_profile",
                }
            except (TypeError, ValueError, ZeroDivisionError) as exc:
                exclusions.append(
                    {
                        "scope": "damage_packet_profile",
                        "brawler": brawler,
                        "packet_id": packet_id,
                        "reason": "invalid_profile_damage_packet",
                        "detail": str(exc),
                    }
                )
    return values, metadata, exclusions


def canonical_map(names: Iterable[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for name in names:
        result[name.casefold()] = name
        result[slugify(name)] = name
    return result


def canonical_name(value: Any, lookup: Mapping[str, str]) -> str:
    text = str(value or "").strip()
    return lookup.get(text.casefold(), lookup.get(slugify(text), text))


def change_kind(change: Mapping[str, Any]) -> str:
    return str(change.get("type") or change.get("kind") or change.get("change_type") or "unsupported")


def change_class(change: Mapping[str, Any]) -> str:
    """Return the support disposition, preserving legacy manifest shorthand."""

    explicit = change.get("change_class")
    if explicit is not None:
        value = str(explicit)
        return value if value in CHANGE_CLASSES else "unsupported_mechanic"
    kind = change_kind(change)
    if kind in SUPPORTED_CHANGE_KINDS:
        return "breakpoint_supported"
    if kind == "source_conflict":
        return "source_conflict"
    if kind == "non_breakpoint":
        return "non_breakpoint"
    if kind == "temporal_survival_excluded":
        return "temporal_survival_excluded"
    return "unsupported_mechanic"


def nested_value(change: Mapping[str, Any], side: str, field: str) -> Any:
    direct = change.get(f"{side}_{field}")
    if direct is not None:
        return direct
    value = change.get(side)
    if isinstance(value, Mapping):
        for key in (field, "value", "amount"):
            if value.get(key) is not None:
                return value[key]
    elif value is not None:
        return value
    return None


def change_power(change: Mapping[str, Any], patch: Patch) -> int:
    value = change.get(
        "power_level",
        change.get("source_power_level", patch.payload.get("power_level", patch.payload.get("source_power_level", 1))),
    )
    return int(value)


def change_supported(change: Mapping[str, Any]) -> bool:
    return (
        change.get("supported", True) is not False
        and change_class(change) == "breakpoint_supported"
        and change_kind(change) in SUPPORTED_CHANGE_KINDS
    )


def packet_key(change: Mapping[str, Any], lookup: Mapping[str, str]) -> tuple[str, str]:
    brawler = canonical_name(change.get("brawler") or change.get("attacker"), lookup)
    packet = str(change.get("packet_id") or change.get("attack_id") or change.get("state_id") or "unspecified_packet")
    return brawler, packet


def packet_value(change: Mapping[str, Any], side: str, patch: Patch, output_power: int) -> Fraction:
    raw = nested_value(change, side, "damage")
    if raw is None:
        raw = change.get(f"{side}_value")
    if raw is None:
        raise ValueError(f"missing {side} damage")
    per_hit = scale_between_powers(raw, change_power(change, patch), output_power)
    hits = change.get("hits_per_packet", change.get("projectiles_per_packet", 1))
    return per_hit * parse_fraction(hits, field="hits_per_packet")


def target_key(change: Mapping[str, Any], lookup: Mapping[str, str]) -> tuple[str, str]:
    brawler = canonical_name(change.get("brawler") or change.get("target"), lookup)
    state_id = str(change.get("state_id") or change.get("target_state_id") or "base")
    return brawler, state_id


def defense_key(change: Mapping[str, Any], lookup: Mapping[str, str]) -> tuple[str, str]:
    brawler = canonical_name(change.get("brawler") or change.get("target"), lookup)
    modifier_id = str(change.get("modifier_id") or change.get("defense_id") or change.get("state_id") or "unnamed_modifier")
    return brawler, modifier_id


def target_health_value(change: Mapping[str, Any], side: str, patch: Patch, output_power: int) -> Fraction:
    raw = nested_value(change, side, "health")
    if raw is None:
        raw = change.get(f"{side}_value")
    if raw is None:
        raise ValueError(f"missing {side} health")
    return scale_between_powers(raw, change_power(change, patch), output_power)


def defense_value(change: Mapping[str, Any], side: str) -> Fraction:
    raw = nested_value(change, side, "damage_reduction")
    if raw is None:
        raw = change.get(f"{side}_ratio", change.get(f"{side}_value"))
    if raw is None:
        raise ValueError(f"missing {side} damage reduction")
    result = parse_fraction(raw, field=f"{side}_damage_reduction")
    # Hand-authored manifests sometimes use 20 for 20%; tolerate that form.
    if result > 1:
        result /= 100
    if result < 0 or result >= 1:
        raise ValueError("damage reduction must be in [0, 1)")
    return result


def change_exclusion(patch: Patch, change: Mapping[str, Any], reason: str, detail: str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {
        "scope": "patch_change",
        "patch_id": patch.patch_id,
        "source": str(patch.source_path),
        "change": dict(change),
        "reason": reason,
    }
    if detail:
        result["detail"] = detail
    return result


def normalize_changes(
    patches: Sequence[Patch],
    lookup: Mapping[str, str],
    output_power: int,
) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    normalized: dict[str, list[dict[str, Any]]] = {}
    exclusions: list[dict[str, Any]] = []
    for patch in patches:
        items: list[dict[str, Any]] = []
        for change in patch.changes:
            kind = change_kind(change)
            if not change_supported(change):
                disposition = change_class(change)
                exclusion = change_exclusion(
                    patch,
                    change,
                    str(change.get("reason") or disposition),
                )
                exclusion["change_class"] = disposition
                exclusions.append(exclusion)
                continue
            try:
                if kind == "damage_packet":
                    key = packet_key(change, lookup)
                    if key[0] not in lookup.values():
                        raise ValueError(f"unknown attacker {key[0]!r}")
                    repeat_model = str(change.get("repeat_model") or "identical")
                    if repeat_model not in {"identical", "resource_gated", "one_off"}:
                        raise ValueError(
                            f"repeat_model {repeat_model!r} cannot use the v1 scalar breakpoint audit"
                        )
                    conditions = change.get("conditions", [])
                    if isinstance(conditions, str):
                        conditions = [conditions]
                    active_when = change.get("active_when")
                    if active_when:
                        conditions = [*conditions, str(active_when)]
                    items.append(
                        {
                            "type": kind,
                            "key": key,
                            "old": packet_value(change, "old", patch, output_power),
                            "new": packet_value(change, "new", patch, output_power),
                            "label": str(change.get("label") or key[1]),
                            "conditions": list(dict.fromkeys(str(item) for item in conditions)),
                            "repeat_model": repeat_model,
                            "packet_unit": str(change.get("packet_unit") or "unspecified"),
                            "source_change": dict(change),
                        }
                    )
                elif kind == "target_state":
                    stat = str(change.get("stat") or change.get("field") or "health")
                    if stat not in {"health", "hp", "base_health"}:
                        raise ValueError(f"unsupported target_state stat {stat!r}")
                    key = target_key(change, lookup)
                    if key[0] not in lookup.values():
                        raise ValueError(f"unknown target {key[0]!r}")
                    items.append(
                        {
                            "type": kind,
                            "key": key,
                            "old": target_health_value(change, "old", patch, output_power),
                            "new": target_health_value(change, "new", patch, output_power),
                            "source_change": dict(change),
                        }
                    )
                elif kind == "defense_modifier":
                    stat = str(change.get("stat") or change.get("field") or "damage_reduction")
                    if stat not in {"damage_reduction", "dr", "reduction"}:
                        raise ValueError(f"unsupported defense_modifier stat {stat!r}")
                    key = defense_key(change, lookup)
                    if key[0] not in lookup.values():
                        raise ValueError(f"unknown target {key[0]!r}")
                    items.append(
                        {
                            "type": kind,
                            "key": key,
                            "target_state_id": str(change.get("state_id") or "body"),
                            "old": defense_value(change, "old"),
                            "new": defense_value(change, "new"),
                            "source_change": dict(change),
                        }
                    )
            except (TypeError, ValueError, ZeroDivisionError) as exc:
                exclusions.append(change_exclusion(patch, change, "invalid_breakpoint_change", str(exc)))
        normalized[patch.patch_id] = items
    return normalized, exclusions


def profile_lists(profile: Mapping[str, Any], *keys: str) -> list[dict[str, Any]]:
    for key in keys:
        value = profile.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    return []


def text_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, (list, tuple)):
        return [str(item) for item in value if item is not None and str(item)]
    return [str(value)]


def scaled_amount(value: Any, *, output_power: int, default_power: int = 1) -> Fraction:
    """Read ``{amount, at_power_level, scaling}`` or a compact scalar."""

    if isinstance(value, Mapping):
        amount = value.get("amount", value.get("value"))
        if amount is None:
            raise ValueError("amount object is missing amount")
        scaling = str(value.get("scaling", "standard"))
        source_power = int(value.get("at_power_level", value.get("power_level", default_power)))
        if scaling in {"flat", "absolute", "none", "power_11_flat"}:
            return parse_fraction(amount, field="amount")
        return scale_between_powers(amount, source_power, output_power)
    return scale_between_powers(value, default_power, output_power)


def formal_modifier_effect(
    modifier: Mapping[str, Any],
    override: Fraction | None,
    *,
    output_power: int,
) -> tuple[Fraction, Fraction, Fraction]:
    """Return (DR, barrier HP, max-health add) for one reviewed modifier."""

    effect = modifier.get("effect", modifier)
    if not isinstance(effect, Mapping):
        raise ValueError("modifier effect must be an object")
    effect_type = str(effect.get("type") or "damage_reduction")
    if effect_type == "damage_reduction":
        ratio = override if override is not None else defense_value({"old": effect.get("ratio", effect.get("value"))}, "old")
        return ratio, Fraction(0), Fraction(0)
    if override is not None:
        amount = override
    else:
        amount_value = effect.get("amount", effect.get("value"))
        if amount_value is None:
            raise ValueError(f"{effect_type} effect is missing amount")
        if isinstance(amount_value, Mapping):
            amount = scaled_amount(amount_value, output_power=output_power)
        else:
            scaling = str(effect.get("scaling", "standard"))
            source_power = int(effect.get("at_power_level", effect.get("power_level", 1)))
            amount = (
                parse_fraction(amount_value, field="modifier_amount")
                if scaling in {"flat", "absolute", "none", "power_11_flat"}
                else scale_between_powers(amount_value, source_power, output_power)
            )
    if effect_type == "barrier_hp":
        return Fraction(0), amount, Fraction(0)
    if effect_type == "max_health_add":
        return Fraction(0), Fraction(0), amount
    raise ValueError(f"unsupported defense effect type {effect_type!r}")


def load_profile_current_inputs(
    targets: Sequence[BaseTarget],
    profiles: Mapping[str, Mapping[str, Any]],
    lookup: Mapping[str, str],
    output_power: int,
) -> tuple[
    dict[tuple[str, str], Fraction],
    dict[tuple[str, str], Fraction],
    list[dict[str, Any]],
]:
    """Index current target-state health and reviewed DR for chain checks."""

    base_health = {
        target.name: scale_between_powers(target.health_p1, 1, output_power)
        for target in targets
    }
    state_values: dict[tuple[str, str], Fraction] = {}
    defense_values: dict[tuple[str, str], Fraction] = {}
    exclusions: list[dict[str, Any]] = []
    for brawler, health in base_health.items():
        # Both aliases are accepted for manifests whose entity page has not yet
        # declared a formal target_states block.
        state_values[(brawler, "body")] = health
        state_values[(brawler, "base")] = health

    for page_name, profile in profiles.items():
        brawler = canonical_name(profile.get("brawler") or page_name, lookup)
        if brawler not in base_health:
            continue
        for target_def in profile_lists(profile, "target_states"):
            state_id = str(target_def.get("id") or target_def.get("state_id") or "").strip()
            if not state_id:
                continue
            try:
                if bool(target_def.get("roster_target")):
                    current = base_health[brawler]
                    if target_def.get("health") is not None:
                        declared = scaled_amount(target_def["health"], output_power=output_power)
                        if declared != current:
                            exclusions.append(
                                {
                                    "scope": "target_state_profile_current_value",
                                    "brawler": brawler,
                                    "target_state": state_id,
                                    "reason": "profile_primary_health_does_not_match_latest_direct_raw",
                                    "profile_current": json_number(declared),
                                    "direct_raw_current": json_number(current),
                                }
                            )
                elif target_def.get("health") is not None:
                    current = scaled_amount(target_def["health"], output_power=output_power)
                else:
                    continue
                state_values[(brawler, state_id)] = current
            except (TypeError, ValueError, ZeroDivisionError) as exc:
                exclusions.append(
                    {
                        "scope": "target_state_profile_current_value",
                        "brawler": brawler,
                        "target_state": state_id,
                        "reason": "invalid_current_target_state_value",
                        "detail": str(exc),
                    }
                )

        for modifier in profile_lists(profile, "defense_modifiers"):
            modifier_id = str(modifier.get("id") or modifier.get("modifier_id") or "").strip()
            effect = modifier.get("effect")
            if not modifier_id or not isinstance(effect, Mapping):
                continue
            if str(effect.get("type") or "damage_reduction") != "damage_reduction":
                continue
            try:
                ratio, _, _ = formal_modifier_effect(modifier, None, output_power=output_power)
                defense_values[(brawler, modifier_id)] = ratio
            except (TypeError, ValueError, ZeroDivisionError) as exc:
                exclusions.append(
                    {
                        "scope": "defense_modifier_profile_current_value",
                        "brawler": brawler,
                        "modifier_id": modifier_id,
                        "reason": "invalid_current_defense_modifier_value",
                        "detail": str(exc),
                    }
                )
    return state_values, defense_values, exclusions


def legal_modifier_sets(modifiers: Sequence[Mapping[str, Any]]) -> Iterator[tuple[Mapping[str, Any], ...]]:
    """Yield every non-empty subset without mutually exclusive loadout groups."""

    for size in range(1, len(modifiers) + 1):
        for subset in itertools.combinations(modifiers, size):
            groups: list[str] = []
            legal = True
            for modifier in subset:
                group = modifier.get("loadout_group")
                if group is None:
                    continue
                group_text = str(group)
                if group_text in groups:
                    legal = False
                    break
                groups.append(group_text)
            if legal:
                yield subset


def reduction_component(value: Any) -> tuple[str | None, Fraction]:
    if isinstance(value, Mapping):
        component_id = value.get("id") or value.get("modifier_id")
        raw = value.get("damage_reduction", value.get("ratio", value.get("value")))
        return (str(component_id) if component_id else None), defense_value({"old": raw}, "old")
    return None, defense_value({"old": value}, "old")


def resolve_variant(
    variant: Mapping[str, Any],
    modifier_defs: Mapping[str, Mapping[str, Any]],
    overrides: Mapping[tuple[str, str], Fraction],
    brawler: str,
) -> tuple[Fraction, Fraction, list[str]]:
    """Resolve one explicit state, adding each named DR component once."""

    variant_id = str(variant.get("id") or variant.get("state_id") or "unnamed_state")
    referenced = variant.get("modifier_ids", variant.get("uses", variant.get("modifiers", [])))
    if isinstance(referenced, str):
        referenced = [referenced]
    reduction = Fraction(0)
    flat_shield = Fraction(0)
    seen: set[str] = set()
    requirements: list[str] = []
    for item in referenced if isinstance(referenced, list) else []:
        modifier_id = str(item.get("id") if isinstance(item, Mapping) else item)
        if modifier_id in seen:
            continue
        seen.add(modifier_id)
        modifier = modifier_defs.get(modifier_id)
        if modifier is None and isinstance(item, Mapping):
            modifier = item
        if modifier is None:
            raise ValueError(f"unknown modifier {modifier_id!r}")
        current = overrides.get((brawler, modifier_id))
        if current is None:
            _, current = reduction_component(modifier)
        reduction += current
        flat_shield += parse_fraction(modifier.get("flat_shield", 0), field="flat_shield")
        requirements.extend(str(x) for x in modifier.get("requirements", modifier.get("requires", [])))

    direct = variant.get("damage_reduction")
    components = variant.get("damage_reduction_components", variant.get("reductions", []))
    if direct is not None:
        reduction += defense_value({"old": direct}, "old")
    component_seen: set[str] = set()
    if not isinstance(components, list):
        components = [components]
    for component in components:
        component_id, ratio = reduction_component(component)
        if component_id and component_id in component_seen:
            continue
        if component_id:
            component_seen.add(component_id)
        reduction += ratio
    flat_shield += parse_fraction(variant.get("flat_shield", 0), field="flat_shield")
    requirements.extend(str(x) for x in variant.get("requirements", variant.get("requires", [])))

    # A patch may target either a named modifier or a fully materialized state.
    if (brawler, variant_id) in overrides:
        reduction = overrides[(brawler, variant_id)]
    if reduction < 0 or reduction >= 1:
        raise ValueError(f"state {variant_id!r} additive damage reduction must be in [0, 1)")
    return reduction, flat_shield, list(dict.fromkeys(requirements))


def build_target_states(
    brawler: str,
    base_health: Fraction,
    profile: Mapping[str, Any] | None,
    world: WorldState,
    *,
    output_power: int = 11,
) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    """Materialize primary body, alternate forms, and legal defense builds."""

    states: dict[str, dict[str, Any]] = {}
    exclusions: list[dict[str, Any]] = []

    def add_state(
        state_id: str,
        health: Fraction,
        barrier_hp: Fraction,
        reduction: Fraction,
        requirements: list[str],
        conditions: list[str],
        *,
        max_health_add: Fraction = Fraction(0),
        entity_class: str = "brawler_body",
        roster_target: bool = False,
        source_modifiers: list[str] | None = None,
    ) -> None:
        try:
            ehp = effective_health(
                health + max_health_add,
                flat_shield=barrier_hp,
                damage_reductions=[reduction],
            )
        except ValueError as exc:
            exclusions.append(
                {
                    "scope": "target_state",
                    "brawler": brawler,
                    "target_state": state_id,
                    "reason": "invalid_defense_state",
                    "detail": str(exc),
                }
            )
            return
        states[state_id] = {
            "state_id": state_id,
            "health": health,
            "max_health_add": max_health_add,
            "barrier_hp": barrier_hp,
            # Compatibility label used by the initial test/API surface.
            "flat_shield": barrier_hp,
            "damage_reduction": reduction,
            "effective_health": ehp,
            "requirements": list(dict.fromkeys(requirements)),
            "conditions": conditions,
            "entity_class": entity_class,
            "roster_target": roster_target,
            "source_modifiers": source_modifiers or [],
        }

    # Formal v1 target definitions.  The latest direct raw remains the primary
    # body's current health; a reviewed body declaration supplies identity and
    # provenance, while alternate/split states supply their own health.
    target_defs = profile_lists(profile or {}, "target_states")
    if not target_defs:
        target_defs = [
            {
                "id": "body",
                "entity_class": "brawler_body",
                "roster_target": True,
            }
        ]
    if not any(bool(item.get("roster_target")) for item in target_defs):
        target_defs[0] = {**target_defs[0], "roster_target": True}

    base_state_health: dict[str, Fraction] = {}
    base_state_reduction: dict[str, Fraction] = {}
    state_definitions: dict[str, dict[str, Any]] = {}
    for target_def in target_defs:
        state_id = str(target_def.get("id") or target_def.get("state_id") or "").strip()
        if not state_id:
            continue
        try:
            is_primary = bool(target_def.get("roster_target"))
            if is_primary:
                health = base_health
            elif (brawler, state_id) in world.state_health:
                health = world.state_health[(brawler, state_id)]
            elif target_def.get("health") is not None:
                health = scaled_amount(target_def["health"], output_power=output_power)
            else:
                raise ValueError("alternate target state is missing health")
            base_state_health[state_id] = health
            intrinsic_reduction = defense_value(
                {"old": target_def.get("intrinsic_damage_reduction", 0)}, "old"
            )
            base_state_reduction[state_id] = intrinsic_reduction
            state_definitions[state_id] = dict(target_def)
            entity_class = str(target_def.get("entity_class") or ("brawler_body" if is_primary else "brawler_alternate_form"))
            state_conditions = list(
                dict.fromkeys(
                    text_list(target_def.get("active_when"))
                    + text_list(target_def.get("state_rule"))
                )
            )
            intrinsic_id = target_def.get("intrinsic_modifier_id")
            intrinsic_sources = [str(intrinsic_id)] if intrinsic_id else []
            add_state(
                state_id,
                health,
                Fraction(0),
                intrinsic_reduction,
                [],
                state_conditions,
                entity_class=entity_class,
                roster_target=is_primary,
                source_modifiers=intrinsic_sources,
            )
            add_state(
                f"{state_id}+shield_gear_full",
                health,
                SHIELD_GEAR_P11,
                intrinsic_reduction,
                ["Shield gear at full charge"],
                state_conditions,
                entity_class=entity_class,
                roster_target=False,
                source_modifiers=intrinsic_sources + ["shield_gear_full"],
            )
        except (TypeError, ValueError, ZeroDivisionError) as exc:
            exclusions.append(
                {
                    "scope": "target_state",
                    "brawler": brawler,
                    "target_state": state_id,
                    "reason": "invalid_profile_target_state",
                    "detail": str(exc),
                }
            )

    # Formal defense modifiers are combined only when their loadout groups are
    # distinct.  This creates Bibi's legal Star Power + Star Buffie state while
    # preventing two Star Powers from being combined.
    formal_modifiers = [
        item
        for item in profile_lists(profile or {}, "defense_modifiers")
        if isinstance(item.get("effect"), Mapping)
    ]
    for state_id, health in base_state_health.items():
        applicable = [
            item
            for item in formal_modifiers
            if state_id in text_list(item.get("applies_to_states", [state_id]))
        ]
        for subset in legal_modifier_sets(applicable):
            modifier_ids = [str(item.get("id") or item.get("modifier_id")) for item in subset]
            try:
                replaces_intrinsic = any(
                    bool(item.get("replaces_intrinsic_damage_reduction")) for item in subset
                )
                reduction = Fraction(0) if replaces_intrinsic else base_state_reduction[state_id]
                barrier_hp = Fraction(0)
                max_health_add = Fraction(0)
                requirements: list[str] = []
                conditions: list[str] = []
                for modifier, modifier_id in zip(subset, modifier_ids):
                    dr, barrier, max_add = formal_modifier_effect(
                        modifier,
                        world.defense_overrides.get((brawler, modifier_id)),
                        output_power=output_power,
                    )
                    reduction += dr
                    barrier_hp += barrier
                    max_health_add += max_add
                    requirements.append(modifier_id)
                    conditions.extend(text_list(modifier.get("active_when")))
                    conditions.extend(text_list(modifier.get("sequence_validity")))
                modifier_state_id = "+".join([state_id, *modifier_ids])
                target_def = state_definitions[state_id]
                entity_class = str(target_def.get("entity_class") or "brawler_body")
                intrinsic_id = target_def.get("intrinsic_modifier_id")
                source_modifiers = ([] if replaces_intrinsic or not intrinsic_id else [str(intrinsic_id)]) + modifier_ids
                add_state(
                    modifier_state_id,
                    health,
                    barrier_hp,
                    reduction,
                    requirements,
                    list(dict.fromkeys(conditions)),
                    max_health_add=max_health_add,
                    entity_class=entity_class,
                    source_modifiers=source_modifiers,
                )
                add_state(
                    f"{modifier_state_id}+shield_gear_full",
                    health,
                    barrier_hp + SHIELD_GEAR_P11,
                    reduction,
                    requirements + ["Shield gear at full charge"],
                    list(dict.fromkeys(conditions)),
                    max_health_add=max_health_add,
                    entity_class=entity_class,
                    source_modifiers=source_modifiers + ["shield_gear_full"],
                )
            except (TypeError, ValueError, ZeroDivisionError) as exc:
                exclusions.append(
                    {
                        "scope": "target_state",
                        "brawler": brawler,
                        "target_state": "+".join([state_id, *modifier_ids]),
                        "reason": "invalid_defense_modifier_combination",
                        "detail": str(exc),
                    }
                )

    # Compatibility for early hand-authored variant fixtures.  Canonical
    # repository pages use the formal target_states/defense_modifiers model.
    modifier_items = profile_lists(profile or {}, "modifiers")
    modifier_defs = {
        str(item.get("id") or item.get("modifier_id")): item
        for item in modifier_items
        if item.get("id") or item.get("modifier_id")
    }
    variants = profile_lists(profile or {}, "variants", "defense_variants", "states")
    if not variants and modifier_defs:
        variants = [{"id": key, "modifier_ids": [key]} for key in modifier_defs]
    primary_health = next(
        (base_state_health[state_id] for state_id, item in state_definitions.items() if item.get("roster_target")),
        base_health,
    )
    for variant in variants:
        state_id = str(variant.get("id") or variant.get("state_id") or "").strip()
        if not state_id:
            continue
        try:
            reduction, flat_shield, requirements = resolve_variant(
                variant, modifier_defs, world.defense_overrides, brawler
            )
            if (brawler, state_id) in world.state_health:
                health = world.state_health[(brawler, state_id)]
            elif variant.get("health") is not None or variant.get("base_health") is not None:
                raw_health = variant.get("health", variant.get("base_health"))
                source_power = int(variant.get("power_level", variant.get("source_power_level", 1)))
                health = scale_between_powers(raw_health, source_power, output_power)
            else:
                health = primary_health
            conditions = text_list(variant.get("conditions"))
            add_state(state_id, health, flat_shield, reduction, requirements, conditions)
            if variant.get("shield_gear_compatible", True) is not False:
                add_state(
                    f"{state_id}+shield_gear_full",
                    health,
                    flat_shield + SHIELD_GEAR_P11,
                    reduction,
                    requirements + ["Shield gear at full charge"],
                    conditions,
                )
        except (TypeError, ValueError, ZeroDivisionError) as exc:
            exclusions.append(
                {
                    "scope": "target_state",
                    "brawler": brawler,
                    "target_state": state_id,
                    "reason": "invalid_profile_variant",
                    "detail": str(exc),
                }
            )

    # A manifest may carry an alternate-form HP state before the profile is
    # curated.  Keep it auditable, but label it as manifest-only.
    for (name, state_id), health in world.state_health.items():
        if name == brawler and state_id not in states:
            add_state(state_id, health, Fraction(0), Fraction(0), ["manifest-defined target state"], [])
            add_state(
                f"{state_id}+shield_gear_full",
                health,
                SHIELD_GEAR_P11,
                Fraction(0),
                ["manifest-defined target state", "Shield gear at full charge"],
                [],
            )
    return states, exclusions


def build_all_target_states(
    targets: Sequence[BaseTarget],
    profiles: Mapping[str, dict[str, Any]],
    world: WorldState,
    output_power: int,
) -> tuple[dict[str, dict[str, dict[str, Any]]], list[dict[str, Any]]]:
    result: dict[str, dict[str, dict[str, Any]]] = {}
    exclusions: list[dict[str, Any]] = []
    for target in targets:
        states, problems = build_target_states(
            target.name,
            world.base_health[target.name],
            profiles.get(target.name),
            world,
            output_power=output_power,
        )
        result[target.name] = states
        exclusions.extend(problems)
    return result, exclusions


def apply_change(world: WorldState, change: Mapping[str, Any], side: str = "new") -> None:
    value = change[side]
    kind = change["type"]
    key = change["key"]
    if kind == "damage_packet":
        world.packet_damage[key] = value
    elif kind == "target_state":
        if key[1] in {"base", "body"}:
            world.base_health[key[0]] = value
        else:
            world.state_health[key] = value
    elif kind == "defense_modifier":
        world.defense_overrides[key] = value


def initialize_world(
    targets: Sequence[BaseTarget],
    patches: Sequence[Patch],
    changes_by_patch: Mapping[str, list[dict[str, Any]]],
    output_power: int,
    current_profile_packets: Mapping[tuple[str, str], Fraction] | None = None,
    current_profile_states: Mapping[tuple[str, str], Fraction] | None = None,
    current_profile_defenses: Mapping[tuple[str, str], Fraction] | None = None,
) -> tuple[WorldState, list[dict[str, Any]]]:
    current_health = {
        target.name: scale_between_powers(target.health_p1, 1, output_power) for target in targets
    }
    world = WorldState(current_health, {}, dict(current_profile_packets or {}), {})
    exclusions: list[dict[str, Any]] = []

    current_non_packet_values: dict[str, Mapping[tuple[str, str], Fraction]] = {
        "target_state": current_profile_states or {},
        "defense_modifier": current_profile_defenses or {},
    }
    for kind, current_values in current_non_packet_values.items():
        previous_new: dict[tuple[str, str], Fraction] = {}
        latest_value: dict[tuple[str, str], Fraction] = {}
        latest_patch: dict[tuple[str, str], str] = {}
        for patch in patches:
            for change in changes_by_patch.get(patch.patch_id, []):
                if change["type"] != kind:
                    continue
                key = change["key"]
                if key in previous_new and previous_new[key] != change["old"]:
                    exclusions.append(
                        {
                            "scope": f"{kind}_chain",
                            "patch_id": patch.patch_id,
                            "brawler": key[0],
                            "input_id": key[1],
                            "reason": "old_value_does_not_match_previous_new_value",
                            "previous_new": json_number(previous_new[key]),
                            "observed_old": json_number(change["old"]),
                        }
                    )
                previous_new[key] = change["new"]
                latest_value[key] = change["new"]
                latest_patch[key] = patch.patch_id
        for key, manifest_new in latest_value.items():
            current = current_values.get(key)
            if current is None:
                exclusions.append(
                    {
                        "scope": f"{kind}_current_value",
                        "patch_id": latest_patch[key],
                        "brawler": key[0],
                        "input_id": key[1],
                        "reason": "latest_manifest_input_missing_from_current_stable_profile",
                        "manifest_new": json_number(manifest_new),
                    }
                )
            elif current != manifest_new:
                exclusions.append(
                    {
                        "scope": f"{kind}_current_value",
                        "patch_id": latest_patch[key],
                        "brawler": key[0],
                        "input_id": key[1],
                        "reason": "latest_manifest_new_does_not_match_current_stable_input",
                        "manifest_new": json_number(manifest_new),
                        "stable_current": json_number(current),
                    }
                )

    # Latest direct raw/profile values represent the current world. Reverse the
    # ordered patch chain to reach the snapshot immediately before the first
    # manifest. Packet values are sourced from the first old value because raw
    # infobox attack fields cannot safely identify a semantic packet.
    for patch in reversed(patches):
        for change in reversed(changes_by_patch.get(patch.patch_id, [])):
            if change["type"] in {"target_state", "defense_modifier"}:
                apply_change(world, change, "old")

    first_packet_value: dict[tuple[str, str], Fraction] = {}
    latest_packet_value: dict[tuple[str, str], Fraction] = {}
    previous_new: dict[tuple[str, str], Fraction] = {}
    for patch in patches:
        for change in changes_by_patch.get(patch.patch_id, []):
            if change["type"] != "damage_packet":
                continue
            key = change["key"]
            first_packet_value.setdefault(key, change["old"])
            if key in previous_new and previous_new[key] != change["old"]:
                exclusions.append(
                    {
                        "scope": "damage_packet_chain",
                        "patch_id": patch.patch_id,
                        "attacker": key[0],
                        "packet_id": key[1],
                        "reason": "old_value_does_not_match_previous_new_value",
                        "previous_new": json_number(previous_new[key]),
                        "observed_old": json_number(change["old"]),
                    }
                )
            previous_new[key] = change["new"]
            latest_packet_value[key] = change["new"]

    for key, latest_value in latest_packet_value.items():
        profile_value = world.packet_damage.get(key)
        if profile_value is not None and profile_value != latest_value:
            exclusions.append(
                {
                    "scope": "damage_packet_current_value",
                    "attacker": key[0],
                    "packet_id": key[1],
                    "reason": "latest_manifest_new_does_not_match_current_profile",
                    "manifest_new": json_number(latest_value),
                    "profile_current": json_number(profile_value),
                }
            )
        world.packet_damage.setdefault(key, latest_value)

    # Reverse all packet changes from the current reviewed snapshot.  This is
    # what makes Crow's 320 -> 420 -> 380 chain reconstruct both patches.
    for patch in reversed(patches):
        for change in reversed(changes_by_patch.get(patch.patch_id, [])):
            if change["type"] == "damage_packet":
                world.packet_damage[change["key"]] = change["old"]

    # A manifest-only packet has no current profile but still enters the audit
    # with its earliest declared value.
    for key, value in first_packet_value.items():
        world.packet_damage.setdefault(key, value)
    return world, exclusions


def serialized_state(state: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "health": json_number(state["health"]),
        "max_health_add": json_number(state.get("max_health_add", Fraction(0))),
        "barrier_hp": json_number(state.get("barrier_hp", state["flat_shield"])),
        "flat_shield": json_number(state["flat_shield"]),
        "damage_reduction": json_number(state["damage_reduction"]),
        "effective_health": json_number(state["effective_health"]),
        "requirements": state["requirements"],
        "conditions": state["conditions"],
        "entity_class": state.get("entity_class"),
        "roster_target": bool(state.get("roster_target")),
        "source_modifiers": state.get("source_modifiers", []),
    }


def primary_state_id(states: Mapping[str, Mapping[str, Any]]) -> str:
    for state_id, state in states.items():
        if state.get("roster_target"):
            return state_id
    if "body" in states:
        return "body"
    if "base" in states:
        return "base"
    raise ValueError("target has no primary roster state")


def threshold_summary(
    patch_id: str,
    packet_key_value: tuple[str, str],
    before_world: WorldState,
    after_world: WorldState,
    before_targets: Mapping[str, Mapping[str, Mapping[str, Any]]],
    after_targets: Mapping[str, Mapping[str, Mapping[str, Any]]],
    repeat_model: str = "identical",
) -> dict[str, Any]:
    before_damage = before_world.packet_damage[packet_key_value]
    after_damage = after_world.packet_damage[packet_key_value]
    before_hits: dict[str, int] = {}
    after_hits: dict[str, int] = {}
    for name in sorted(set(before_targets) & set(after_targets), key=str.casefold):
        before_primary = primary_state_id(before_targets[name])
        after_primary = primary_state_id(after_targets[name])
        before_hits[name] = hits_to_kill(before_targets[name][before_primary]["effective_health"], before_damage)
        after_hits[name] = hits_to_kill(after_targets[name][after_primary]["effective_health"], after_damage)

    def histogram(values: Mapping[str, int]) -> dict[str, int]:
        result: dict[str, int] = {}
        for hits in values.values():
            result[str(hits)] = result.get(str(hits), 0) + 1
        return dict(sorted(result.items(), key=lambda item: int(item[0])))

    exact_before = sorted((name for name, hits in before_hits.items() if hits == 3), key=str.casefold)
    exact_after = sorted((name for name, hits in after_hits.items() if hits == 3), key=str.casefold)
    at_most_before = sorted((name for name, hits in before_hits.items() if hits <= 3), key=str.casefold)
    at_most_after = sorted((name for name, hits in after_hits.items() if hits <= 3), key=str.casefold)
    result = {
        "patch_id": patch_id,
        "attacker": packet_key_value[0],
        "packet_id": packet_key_value[1],
        "packet_damage_before": json_number(before_damage),
        "packet_damage_after": json_number(after_damage),
        "base_target_count": len(before_hits),
        "comparison_kind": "repeated_identical_packets" if repeat_model == "identical" else "one_packet_threshold_only",
        "repeat_model": repeat_model,
    }
    if repeat_model != "identical":
        one_before = sorted((name for name, hits in before_hits.items() if hits <= 1), key=str.casefold)
        one_after = sorted((name for name, hits in after_hits.items() if hits <= 1), key=str.casefold)
        result.update(
            {
                "one_packet_kill_before": one_before,
                "one_packet_kill_after": one_after,
                "one_packet_kill_count_change": len(one_after) - len(one_before),
            }
        )
        return result
    result.update({
        "hits_to_kill_histogram_before": histogram(before_hits),
        "hits_to_kill_histogram_after": histogram(after_hits),
        "exactly_3_packets_before": exact_before,
        "exactly_3_packets_after": exact_after,
        "exactly_3_count_change": len(exact_after) - len(exact_before),
        "at_most_3_packets_before": at_most_before,
        "at_most_3_packets_after": at_most_after,
        "at_most_3_count_change": len(at_most_after) - len(at_most_before),
    })
    return result


def make_pair_delta(
    patch_id: str,
    packet_key_value: tuple[str, str],
    target: str,
    target_state: str,
    before_world: WorldState,
    after_world: WorldState,
    before_state: Mapping[str, Any],
    after_state: Mapping[str, Any],
    drivers: list[str],
    repeat_model: str = "identical",
) -> dict[str, Any] | None:
    before_damage = before_world.packet_damage[packet_key_value]
    after_damage = after_world.packet_damage[packet_key_value]
    before_hits = hits_to_kill(before_state["effective_health"], before_damage)
    after_hits = hits_to_kill(after_state["effective_health"], after_damage)
    if repeat_model != "identical":
        before_one = before_hits <= 1
        after_one = after_hits <= 1
        if before_one == after_one:
            return None
        return {
            "patch_id": patch_id,
            "attacker": packet_key_value[0],
            "packet_id": packet_key_value[1],
            "target": target,
            "target_state": target_state,
            "comparison_kind": "one_packet_threshold_only",
            "repeat_model": repeat_model,
            "change_drivers": drivers,
            "packet_damage_before": json_number(before_damage),
            "packet_damage_after": json_number(after_damage),
            "effective_health_before": json_number(before_state["effective_health"]),
            "effective_health_after": json_number(after_state["effective_health"]),
            "kills_in_one_packet_before": before_one,
            "kills_in_one_packet_after": after_one,
            "requirements": after_state["requirements"],
            "conditions": after_state["conditions"],
            "rounding_review_required": bool(
                (before_state["effective_health"] / before_damage).denominator == 1
                or (after_state["effective_health"] / after_damage).denominator == 1
            ),
        }
    if before_hits == after_hits:
        return None
    return {
        "patch_id": patch_id,
        "attacker": packet_key_value[0],
        "packet_id": packet_key_value[1],
        "target": target,
        "target_state": target_state,
        "comparison_kind": "repeated_identical_packets",
        "repeat_model": repeat_model,
        "change_drivers": drivers,
        "packet_damage_before": json_number(before_damage),
        "packet_damage_after": json_number(after_damage),
        "effective_health_before": json_number(before_state["effective_health"]),
        "effective_health_after": json_number(after_state["effective_health"]),
        "hits_to_kill_before": before_hits,
        "hits_to_kill_after": after_hits,
        "hit_count_change": after_hits - before_hits,
        "requirements": after_state["requirements"],
        "conditions": after_state["conditions"],
        "rounding_review_required": bool(
            (before_state["effective_health"] / before_damage).denominator == 1
            or (after_state["effective_health"] / after_damage).denominator == 1
        ),
    }


def build_pressure_for_pair(
    patch_id: str,
    packet_key_value: tuple[str, str],
    target: str,
    before_world: WorldState,
    after_world: WorldState,
    before_states: Mapping[str, Mapping[str, Any]],
    after_states: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    try:
        before_primary_id = primary_state_id(before_states)
        after_primary_id = primary_state_id(after_states)
    except ValueError:
        return []
    before_damage = before_world.packet_damage[packet_key_value]
    after_damage = after_world.packet_damage[packet_key_value]
    base_before = hits_to_kill(before_states[before_primary_id]["effective_health"], before_damage)
    base_after = hits_to_kill(after_states[after_primary_id]["effective_health"], after_damage)
    result: list[dict[str, Any]] = []
    for state_id in sorted((set(before_states) & set(after_states)) - {before_primary_id, after_primary_id}):
        if not state_id.startswith(f"{before_primary_id}+"):
            # Alternate/split forms are separate target states, not a build
            # layered on top of the primary body denominator.
            continue
        state_before = hits_to_kill(before_states[state_id]["effective_health"], before_damage)
        state_after = hits_to_kill(after_states[state_id]["effective_health"], after_damage)
        direction: str | None = None
        preserved = None
        if base_after < base_before:
            preserved = base_before
            if state_after >= base_before:
                direction = "defense_state_now_required_to_preserve_previous_base_breakpoint"
            elif state_id.endswith("+shield_gear_full") and state_after < base_before:
                direction = "shield_gear_cannot_preserve_previous_base_breakpoint"
        elif base_after > base_before and state_before > base_before and base_after >= state_before:
            preserved = state_before
            direction = "defense_state_requirement_relieved"
        if direction is None:
            continue
        result.append(
            {
                "patch_id": patch_id,
                "attacker": packet_key_value[0],
                "packet_id": packet_key_value[1],
                "target": target,
                "target_state": state_id,
                "direction": direction,
                "breakpoint_to_preserve": preserved,
                "survival_packet_count_to_preserve": (preserved - 1) if preserved is not None else None,
                "base_hits_to_kill_before": base_before,
                "base_hits_to_kill_after": base_after,
                "base_survives_packet_count_before": max(base_before - 1, 0),
                "base_survives_packet_count_after": max(base_after - 1, 0),
                "defense_state_hits_to_kill_before": state_before,
                "defense_state_hits_to_kill_after": state_after,
                "defense_state_survives_packet_count_before": max(state_before - 1, 0),
                "defense_state_survives_packet_count_after": max(state_after - 1, 0),
                "requirements": after_states[state_id]["requirements"],
                "conditions": after_states[state_id]["conditions"],
            }
        )
    return result


def build_audit(
    *,
    roster_path: Path,
    fandom_dir: Path,
    entity_dir: Path,
    patch_sources: Sequence[Path],
    output_power: int = 11,
) -> dict[str, Any]:
    roster_entries = parse_roster(roster_path)
    roster_names = {entry.name for entry in roster_entries}
    targets, exclusions, manifest_roster_count = load_base_targets(roster_path, fandom_dir)
    profiles, profile_exclusions = load_profiles(entity_dir)
    exclusions.extend(profile_exclusions)
    patches, patch_exclusions = load_patches(patch_sources)
    exclusions.extend(patch_exclusions)

    names = [target.name for target in targets]
    lookup = canonical_map(names)
    changes_by_patch, change_exclusions = normalize_changes(patches, lookup, output_power)
    exclusions.extend(change_exclusions)
    profile_packet_values, profile_packet_meta, packet_profile_exclusions = load_profile_packets(
        profiles, lookup, output_power
    )
    exclusions.extend(packet_profile_exclusions)
    profile_state_values, profile_defense_values, current_input_exclusions = load_profile_current_inputs(
        targets, profiles, lookup, output_power
    )
    exclusions.extend(current_input_exclusions)
    world, chain_exclusions = initialize_world(
        targets,
        patches,
        changes_by_patch,
        output_power,
        current_profile_packets=profile_packet_values,
        current_profile_states=profile_state_values,
        current_profile_defenses=profile_defense_values,
    )
    exclusions.extend(chain_exclusions)

    packet_meta: dict[tuple[str, str], dict[str, Any]] = dict(profile_packet_meta)
    for patch in patches:
        for change in changes_by_patch.get(patch.patch_id, []):
            if change["type"] == "damage_packet":
                packet_meta[change["key"]] = {
                    "label": change["label"],
                    "conditions": change["conditions"],
                    "repeat_model": change["repeat_model"],
                    "packet_unit": change["packet_unit"],
                    "source": "balance_patch_manifest",
                }

    threshold_summaries: list[dict[str, Any]] = []
    pair_deltas: list[dict[str, Any]] = []
    build_pressure_deltas: list[dict[str, Any]] = []
    patch_summaries: list[dict[str, Any]] = []
    profile_state_exclusions: list[dict[str, Any]] = []

    for patch in patches:
        before_world = world.clone()
        patch_changes = changes_by_patch.get(patch.patch_id, [])
        changed_packets = {change["key"] for change in patch_changes if change["type"] == "damage_packet"}
        changed_target_names = {
            change["key"][0]
            for change in patch_changes
            if change["type"] in {"target_state", "defense_modifier"}
        }
        changed_defense_states = {
            change["key"] for change in patch_changes if change["type"] == "defense_modifier"
        }
        changed_health_targets = {
            change["key"] for change in patch_changes if change["type"] == "target_state"
        }

        for change in patch_changes:
            apply_change(world, change, "new")
        after_world = world.clone()
        before_targets, before_problems = build_all_target_states(targets, profiles, before_world, output_power)
        after_targets, after_problems = build_all_target_states(targets, profiles, after_world, output_power)
        profile_state_exclusions.extend(before_problems)
        profile_state_exclusions.extend(after_problems)

        for key in sorted(changed_packets):
            repeat_model = str(packet_meta.get(key, {}).get("repeat_model", "identical"))
            threshold_summaries.append(
                threshold_summary(
                    patch.patch_id,
                    key,
                    before_world,
                    after_world,
                    before_targets,
                    after_targets,
                    repeat_model,
                )
            )

        comparison_packets = sorted(before_world.packet_damage)
        for key in comparison_packets:
            packet_changed = key in changed_packets
            repeat_model = str(packet_meta.get(key, {}).get("repeat_model", "non_independent"))
            if not packet_changed and repeat_model != "identical":
                continue
            for target in sorted(before_targets, key=str.casefold):
                if not packet_changed and target not in changed_target_names:
                    continue
                before_states = before_targets[target]
                after_states = after_targets[target]
                for state_id in sorted(set(before_states) & set(after_states)):
                    drivers: list[str] = []
                    if packet_changed:
                        drivers.append("damage_packet")
                    if any(
                        changed_target == target
                        and (
                            changed_state in {"base", "body"}
                            and state_id.startswith("body")
                            or state_id == changed_state
                            or state_id.startswith(f"{changed_state}+")
                        )
                        for changed_target, changed_state in changed_health_targets
                    ):
                        drivers.append("target_health")
                    state_modifiers = set(after_states[state_id].get("source_modifiers", []))
                    if any(
                        changed_target == target and modifier_id in state_modifiers
                        for changed_target, modifier_id in changed_defense_states
                    ):
                        drivers.append("damage_reduction")
                    delta = make_pair_delta(
                        patch.patch_id,
                        key,
                        target,
                        state_id,
                        before_world,
                        after_world,
                        before_states[state_id],
                        after_states[state_id],
                        drivers,
                        repeat_model,
                    )
                    if delta:
                        pair_deltas.append(delta)
                if repeat_model == "identical":
                    build_pressure_deltas.extend(
                        build_pressure_for_pair(
                            patch.patch_id,
                            key,
                            target,
                            before_world,
                            after_world,
                            before_states,
                            after_states,
                        )
                    )

        patch_summaries.append(
            {
                "patch_id": patch.patch_id,
                "source": str(patch.source_path),
                "effective_date": patch.payload.get(
                    "effective_at", patch.payload.get("effective_date", patch.payload.get("date"))
                ),
                "supported_change_count": len(patch_changes),
                "changed_damage_packet_count": len(changed_packets),
                "changed_target_count": len(changed_target_names),
            }
        )

    # Materialize the current index after every manifest.  This is both a
    # coverage artifact and the reusable durability input for human review.
    current_targets, current_problems = build_all_target_states(targets, profiles, world, output_power)
    profile_state_exclusions.extend(current_problems)
    # State validation can repeat for before/after snapshots; keep exclusions
    # deterministic and compact.
    seen_exclusion: set[str] = set()
    for item in [*exclusions, *profile_state_exclusions]:
        signature = json.dumps(item, ensure_ascii=False, sort_keys=True, default=str)
        if signature not in seen_exclusion:
            seen_exclusion.add(signature)
        else:
            continue
    all_exclusions = [json.loads(value) for value in sorted(seen_exclusion)]

    target_index: list[dict[str, Any]] = []
    raw_by_name = {target.name: target for target in targets}
    for name in sorted(current_targets, key=str.casefold):
        target = raw_by_name[name]
        target_index.append(
            {
                "brawler": name,
                "source": str(target.raw_path),
                "base_health_power_1": json_number(target.health_p1),
                f"base_health_power_{output_power}": json_number(world.base_health[name]),
                "states": {
                    state_id: serialized_state(state)
                    for state_id, state in sorted(current_targets[name].items())
                },
            }
        )

    target_state_count = sum(len(item["states"]) for item in target_index)
    indexed_target_form_count = sum(
        1
        for item in target_index
        for state in item["states"].values()
        if not state.get("source_modifiers") and state["barrier_hp"] == 0 and state["max_health_add"] == 0
    )
    manifest_packet_keys = {
        change["key"]
        for patch in patches
        for change in changes_by_patch.get(patch.patch_id, [])
        if change["type"] == "damage_packet"
    }
    health_index: list[dict[str, Any]] = []
    for item in target_index:
        if item["brawler"] not in roster_names:
            continue
        state_rows: list[dict[str, Any]] = []
        primary: dict[str, Any] | None = None
        for state_id, state in item["states"].items():
            if state.get("source_modifiers") or state["barrier_hp"] != 0 or state["max_health_add"] != 0:
                continue
            row = {
                "state_id": state_id,
                "entity_class": state.get("entity_class"),
                "roster_target": bool(state.get("roster_target")),
                "health_power_1_equivalent": json_number(
                    parse_fraction(state["health"]) / power_multiplier(output_power)
                ),
                f"health_power_{output_power}": state["health"],
            }
            state_rows.append(row)
            if row["roster_target"]:
                primary = row
        if primary is None:
            continue
        health_index.append(
            {
                "brawler": item["brawler"],
                "source_raw": item["source"],
                "primary_body": primary,
                "target_states": state_rows,
            }
        )
    health_change_count = sum(
        1
        for patch in patches
        for change in changes_by_patch.get(patch.patch_id, [])
        if change["type"] in {"target_state", "defense_modifier"}
    )
    audit = {
        "schema": OUTPUT_SCHEMA,
        "power_level": output_power,
        "provenance": {
            "roster_manifest": str(roster_path),
            "fandom_raw_directory": str(fandom_dir),
            "brawler_entity_directory": str(entity_dir),
            "patch_sources": [str(patch.source_path) for patch in patches],
        },
        "roster": {
            "manifest_brawler_count": manifest_roster_count,
            "indexed_manifest_brawler_count": len(health_index),
            "active_direct_raw_target_count": len(targets),
            "active_raw_additions_not_in_manifest": sorted(
                set(names) - roster_names, key=str.casefold
            ),
        },
        "ruleset": {
            "power_scaling": "standard_stat_multiplier_equals_one_plus_0.10_times_power_level_minus_1",
            "shield_gear_full_power_11": json_number(SHIELD_GEAR_P11),
            "shield_gear_level_scaling": "none",
            "damage_reduction_combination": "distinct_simultaneously_active_components_add;same_loadout_group_is_mutually_exclusive",
            "effective_health_formula": "(health+max_health_add+barrier_hp)/(1-total_damage_reduction)",
            "packet_rounding": "exact_fraction_then_mathematical_ceil",
            "exact_boundary_policy": "pair_delta_marks_rounding_review_required",
        },
        "shield_gear_flat_health": json_number(SHIELD_GEAR_P11),
        "damage_reduction_stack_rule": "distinct_components_additive_then_ehp_equals_hp_plus_flat_shield_over_one_minus_total_reduction",
        "coverage": {
            "roster_manifest_row_count": manifest_roster_count,
            "roster_brawler_count": manifest_roster_count,
            "roster_base_health_covered_count": len(health_index),
            "active_target_count": len(targets),
            "base_health_covered_count": len(targets),
            "combat_profile_count": len(profiles),
            "reviewed_defense_modifier_profile_count": sum(
                1 for profile in profiles.values() if profile_lists(profile, "defense_modifiers")
            ),
            "reviewed_defense_modifier_count": sum(
                len(profile_lists(profile, "defense_modifiers")) for profile in profiles.values()
            ),
            "reviewed_damage_packet_profile_count": sum(
                1 for profile in profiles.values() if profile_lists(profile, "damage_packets")
            ),
            "indexed_target_form_count": indexed_target_form_count,
            "materialized_target_state_count": target_state_count,
            "manifest_damage_packet_count": len(manifest_packet_keys),
            "reviewed_damage_packet_count": len(world.packet_damage),
            "reviewed_identical_damage_packet_count": sum(
                1 for key in world.packet_damage if packet_meta.get(key, {}).get("repeat_model") == "identical"
            ),
            "manifest_health_or_defense_change_count": health_change_count,
            "health_change_comparison_scope": "all_reviewed_identical_damage_packets_from_profiles_and_loaded_manifests",
            "health_change_comparison_limitation": "reviewed_packets_are_not_a_complete_attack_packet_index_for_every_active_brawler",
        },
        "patches": patch_summaries,
        "health_index": health_index,
        "target_index": target_index,
        "damage_packet_index": [
            {
                "attacker": key[0],
                "packet_id": key[1],
                "current_damage": json_number(world.packet_damage[key]),
                "label": packet_meta.get(key, {}).get("label", key[1]),
                "conditions": packet_meta.get(key, {}).get("conditions", []),
                "repeat_model": packet_meta.get(key, {}).get("repeat_model", "non_independent"),
                "packet_unit": packet_meta.get(key, {}).get("packet_unit", "unspecified"),
            }
            for key in sorted(world.packet_damage)
        ],
        "threshold_summaries": threshold_summaries,
        "pair_deltas": sorted(
            pair_deltas,
            key=lambda item: (
                item["patch_id"],
                item["attacker"].casefold(),
                item["packet_id"],
                item["target"].casefold(),
                item["target_state"],
            ),
        ),
        "build_pressure_deltas": sorted(
            build_pressure_deltas,
            key=lambda item: (
                item["patch_id"],
                item["attacker"].casefold(),
                item["packet_id"],
                item["target"].casefold(),
                item["target_state"],
            ),
        ),
        "exclusions": all_exclusions,
    }
    return audit


def render_markdown(audit: Mapping[str, Any]) -> str:
    coverage = audit["coverage"]
    lines = [
        "# Balance Breakpoint Audit",
        "",
        f"- Schema: `{audit['schema']}`",
        f"- Power level: `{audit['power_level']}`",
        f"- Active targets with base health: `{coverage['base_health_covered_count']}`",
        f"- Defensive states materialized: `{coverage['materialized_target_state_count']}`",
        f"- Reviewed hero-specific defenses: `{coverage['reviewed_defense_modifier_profile_count']}` profiles / "
        f"`{coverage['reviewed_defense_modifier_count']}` modifiers (partial coverage)",
        f"- Reviewed damage packets: `{coverage['reviewed_damage_packet_count']}` "
        f"(`{coverage['manifest_damage_packet_count']}` appear in loaded patch manifests)",
        f"- Shield gear: `+{audit['shield_gear_flat_health']}` flat health at Power 11 (not level-scaled)",
        "- Damage reduction: distinct components add, then EHP = (health + flat shield) / (1 - total reduction)",
        "- Health/defense reverse comparisons cover reviewed identical packets from Brawler profiles and loaded patch manifests; this is not a complete attack-packet catalog.",
        "",
        "## Patch Coverage",
        "",
        "| Patch | Supported changes | Damage packets changed | Targets changed |",
        "| --- | ---: | ---: | ---: |",
    ]
    for patch in audit["patches"]:
        lines.append(
            f"| {patch['patch_id']} | {patch['supported_change_count']} | "
            f"{patch['changed_damage_packet_count']} | {patch['changed_target_count']} |"
        )

    lines.extend(
        [
            "",
            "## Three-Packet Threshold Summaries",
            "",
            "| Patch | Packet | Damage before -> after | Exactly 3 before -> after | At most 3 before -> after |",
            "| --- | --- | --- | ---: | ---: |",
        ]
    )
    for summary in audit["threshold_summaries"]:
        if summary["comparison_kind"] == "one_packet_threshold_only":
            exact_counts = "one-packet only"
            at_most_counts = (
                f"{len(summary['one_packet_kill_before'])} -> "
                f"{len(summary['one_packet_kill_after'])}"
            )
        else:
            exact_counts = (
                f"{len(summary['exactly_3_packets_before'])} -> "
                f"{len(summary['exactly_3_packets_after'])}"
            )
            at_most_counts = (
                f"{len(summary['at_most_3_packets_before'])} -> "
                f"{len(summary['at_most_3_packets_after'])}"
            )
        lines.append(
            f"| {summary['patch_id']} | {summary['attacker']} / {summary['packet_id']} | "
            f"{summary['packet_damage_before']} -> {summary['packet_damage_after']} | "
            f"{exact_counts} | {at_most_counts} |"
        )

    lines.extend(
        [
            "",
            "## Pair Breakpoint Deltas",
            "",
            "The Markdown view keeps repeated-packet transitions whose smaller kill count is at most 4; the JSON retains every transition.",
            "",
            "| Patch | Attacker packet | Target state | Hits before -> after | Drivers |",
            "| --- | --- | --- | ---: | --- |",
        ]
    )
    visible_pair_deltas = [
        delta
        for delta in audit["pair_deltas"]
        if delta["comparison_kind"] == "one_packet_threshold_only"
        or min(delta["hits_to_kill_before"], delta["hits_to_kill_after"]) <= 4
    ]
    for delta in visible_pair_deltas:
        if delta["comparison_kind"] == "one_packet_threshold_only":
            transition = f"one-packet {delta['kills_in_one_packet_before']} -> {delta['kills_in_one_packet_after']}"
        else:
            transition = f"{delta['hits_to_kill_before']} -> {delta['hits_to_kill_after']}"
        lines.append(
            f"| {delta['patch_id']} | {delta['attacker']} / {delta['packet_id']} | "
            f"{delta['target']} / {delta['target_state']} | "
            f"{transition} | "
            f"{', '.join(delta['change_drivers']) or 'simultaneous patch state'} |"
        )
    suppressed_pair_count = len(audit["pair_deltas"]) - len(visible_pair_deltas)
    lines.extend(["", f"- Suppressed higher-count pair transitions in Markdown: `{suppressed_pair_count}`"])

    lines.extend(
        [
            "",
            "## Defensive Build Pressure",
            "",
            "The Markdown view keeps pressure whose preserved kill breakpoint is at most 4; the JSON retains every pressure delta.",
            "",
            "| Patch | Attacker packet | Target state | Direction | Base hits before -> after | State hits before -> after |",
            "| --- | --- | --- | --- | ---: | ---: |",
        ]
    )
    visible_pressure_deltas = [
        delta
        for delta in audit["build_pressure_deltas"]
        if delta.get("breakpoint_to_preserve") is not None and delta["breakpoint_to_preserve"] <= 4
    ]
    for delta in visible_pressure_deltas:
        lines.append(
            f"| {delta['patch_id']} | {delta['attacker']} / {delta['packet_id']} | "
            f"{delta['target']} / {delta['target_state']} | {delta['direction']} | "
            f"{delta['base_hits_to_kill_before']} -> {delta['base_hits_to_kill_after']} | "
            f"{delta['defense_state_hits_to_kill_before']} -> {delta['defense_state_hits_to_kill_after']} |"
        )
    suppressed_pressure_count = len(audit["build_pressure_deltas"]) - len(visible_pressure_deltas)
    lines.extend(["", f"- Suppressed higher-count build-pressure transitions in Markdown: `{suppressed_pressure_count}`"])

    lines.extend(
        [
            "",
            "## Current Base Health Index",
            "",
            f"| Brawler | Power 1 | Power {audit['power_level']} | Defensive states |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    p_level_key = f"base_health_power_{audit['power_level']}"
    for target in audit["target_index"]:
        lines.append(
            f"| {target['brawler']} | {target['base_health_power_1']} | "
            f"{target[p_level_key]} | {len(target['states'])} |"
        )

    lines.extend(["", "## Exclusions", ""])
    if not audit["exclusions"]:
        lines.append("- None")
    else:
        for item in audit["exclusions"]:
            change = item.get("change") if isinstance(item.get("change"), Mapping) else {}
            subject = (
                item.get("brawler")
                or change.get("brawler")
                or item.get("patch_id")
                or item.get("source")
                or "unknown"
            )
            change_id = change.get("id")
            label = f"{subject} / {change_id}" if change_id else str(subject)
            detail = item.get("detail")
            detail_text = f" ({detail})" if detail else ""
            lines.append(f"- `{label}`: {item.get('reason', 'unspecified')}{detail_text}")
    lines.append("")
    return "\n".join(lines)


def select_report_patches(audit: Mapping[str, Any], patch_ids: Sequence[str]) -> dict[str, Any]:
    if not patch_ids:
        return dict(audit)
    selected = set(patch_ids)
    result = copy.deepcopy(dict(audit))
    available = {item["patch_id"] for item in result["patches"]}
    missing = sorted(selected - available)
    if missing:
        raise ValueError(f"unknown --patch-id value(s): {', '.join(missing)}")
    result["selected_patch_ids"] = list(dict.fromkeys(patch_ids))
    result["patches"] = [item for item in result["patches"] if item["patch_id"] in selected]
    for key in ("threshold_summaries", "pair_deltas", "build_pressure_deltas"):
        result[key] = [item for item in result[key] if item["patch_id"] in selected]
    return result


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    patch_sources = list(args.patch_source) or discover_patch_sources(args.source_dir)
    audit = build_audit(
        roster_path=args.roster,
        fandom_dir=args.fandom_dir,
        entity_dir=args.entity_dir,
        patch_sources=patch_sources,
        output_power=args.power_level,
    )
    audit = select_report_patches(audit, args.patch_id)
    json_path = args.json_output or args.output_dir / "balance_breakpoint_audit.v1.json"
    markdown_path = args.markdown_output or args.output_dir / "balance_breakpoint_audit.v1.md"
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(audit), encoding="utf-8")
    print(
        json.dumps(
            {
                "schema": OUTPUT_SCHEMA,
                "json_output": str(json_path),
                "markdown_output": str(markdown_path),
                "active_target_count": audit["coverage"]["active_target_count"],
                "pair_delta_count": len(audit["pair_deltas"]),
                "build_pressure_delta_count": len(audit["build_pressure_deltas"]),
                "exclusion_count": len(audit["exclusions"]),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
