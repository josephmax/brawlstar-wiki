# Balance Breakpoint Audit

Use this reference for every patch that changes brawler health, a discrete damage packet, a flat barrier, or a damage-reduction modifier.

## Purpose and Boundary

The audit answers deterministic questions such as “which target states moved from four to three identical packets?” and “which target now needs full Shield gear to survive the second packet?” It does not answer whether a brawler is strong.

`balance_breakpoint_audit.v1` must not auto-generate a strength tier, favored matchup, pick/ban priority, map fit, hard gate, slot eligibility, or runtime recommendation. Generated matrices and review seeds belong in `outputs/balance-breakpoints/`.

## Input Ownership

| Input | Canonical location | Rule |
| --- | --- | --- |
| Patch before/after values | corresponding `wiki/sources/` patch page | fenced JSON `balance_patch_manifest` ledger; never brawler history |
| Current body health | latest direct Fandom raw, indexed by roster | Power Level and form must be explicit |
| Reviewed alternate forms, damage packets, and hero-specific defenses | second fenced JSON block on `wiki/entities/brawlers/*.md` | top-level key `combat_breakpoint_profile`; current stable fact only |
| Power scaling, Shield gear, stacking, and rounding semantics | `wiki/concepts/伤害与生存断点.md` | shared rules are not copied into every brawler page |
| Pairwise differences | `outputs/balance-breakpoints/` | generated, reproducible, and excluded from canonical wiki/runtime |

The current roster fallback may seed a primary `body` state from the latest direct Fandom `Health` or `Health1`. It must report coverage and may not invent an attack packet from a bare `Attack` field. Multi-projectile, distance-scaled, form-dependent, staged, percentage-health, DoT, or resource-dependent attacks need a reviewed packet.

## Power-Level Normalization

Ranked audits use Power Level 11. A standard scalar recorded at any source Power Level is normalized with the ratio between the target and source multipliers:

```text
multiplier(power) = 1 + 0.10 * (power - 1)
amount_at_11 = amount_at_source_level * multiplier(11) / multiplier(source_level)
```

Therefore a Power Level 1 scalar is multiplied by `2.0`. A flat Power Level 11 equipment value such as full Shield gear `+900` is already absolute and is not scaled again.

## Target and Defense Model

Supported target classes are `brawler_body`, `brawler_alternate_form`, and `brawler_split_part`. `summon` and `deployable` states are reported separately and do not increase the “number of brawlers” denominator.

If a form has always-on mitigation, declare `intrinsic_damage_reduction` and an `intrinsic_modifier_id` on that `target_state`; the unmitigated form must not be materialized. A conditional modifier that replaces rather than adds to that baseline declares `replaces_intrinsic_damage_reduction: true`. R-T's split legs (29% normally, 50% with Recording) are the regression case.

The v1 defense effects are:

- `barrier_hp`
- `max_health_add`
- `damage_reduction`

The project-level `damage_reduction_stack_rule` is: distinct simultaneously active damage reductions add, while mutually exclusive loadout choices do not combine. Full Shield gear is a `barrier_hp` modifier. The audit arithmetic is:

```text
raw_hp_pool = health + max_health_add + barrier_hp
total_dr = sum(distinct_legal_damage_reductions)
effective_hp = raw_hp_pool / (1 - total_dr)
packets_to_kill = ceil(effective_hp / packet_damage)
```

Use exact rational arithmetic. Equality means the target dies on that packet. Because the engine's internal stepwise rounding is not proven here, exact-boundary results must carry `rounding_review_required`.

Do not flatten healing, resurrection, invulnerability, a cap on one incoming hit, or a time-decaying barrier into static EHP. Record them as exclusions until the packet/time sequence is modeled.

## `combat_breakpoint_profile`

Append a second fenced JSON block to a brawler page only for reviewed current inputs. The existing first `bp_brawler_profile` YAML block remains the runtime compiler input.

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "Bibi",
    "target_states": [
      {
        "id": "body",
        "entity_class": "brawler_body",
        "roster_target": true,
        "health": {"amount": 5000, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-Bibi|Fandom-Bibi]]"
      }
    ],
    "damage_packets": [],
    "defense_modifiers": [
      {
        "id": "batting_stance",
        "source_kind": "star_power",
        "loadout_group": "star_power",
        "applies_to_states": ["body"],
        "effect": {"type": "damage_reduction", "ratio": 0.20},
        "active_when": "Home Run bar is full",
        "sequence_validity": "ends when Bibi uses the charged swing",
        "source_ref": "[[sources/Fandom-Bibi|Fandom-Bibi]]"
      }
    ]
  }
}
```

For damage packets, always declare:

- `id`, `ability_kind`, and `packet_unit`
- `delivery_variant` such as `impact`, `full_connect`, `max_range`, `sequence_step`, or `full_resolution`
- `repeat_model`: `identical`, `cycle`, `resource_gated`, `non_independent`, or `one_off`
- numeric components at a stated Power Level
- `active_when`, exclusions, target classes, provenance, and conflict status

Only `identical` packets may use simple packets-to-kill division. `cycle` needs ordered simulation. `resource_gated` and `one_off` may report one-packet thresholds but not repeated-shot claims. `non_independent` packets such as poison refresh must not fall back to division.

## `balance_patch_manifest`

Each patch source summary stores a fenced JSON ledger with schema `balance_breakpoint_manifest.v1`. Every item must have a `type`. A calculable row uses `damage_packet`, `target_state`, or `defense_modifier`; this tells the script which stable input is changing.

Every new item should also have a `change_class` support disposition:

- `breakpoint_supported`
- `temporal_survival_excluded`
- `non_breakpoint`
- `unsupported_mechanic`
- `source_conflict`

`breakpoint_supported` is valid only when `type` is one of the three calculable input types. Excluded rows may use `type: other` plus a non-supported `change_class`. Existing v1 trial manifests that use `type: unsupported`, `type: source_conflict`, or omit `change_class` remain backward-compatible, but new manifests should write both fields explicitly.

Supported changes point to an input id and field. Before/after values must include their Power Level when relevant. Consecutive changes to every input kind must be continuous: an earlier `after` must equal the next `before`. The latest supported `after` is checked against current direct body health, reviewed alternate-form health, current damage packet, or current defense modifier; any mismatch or missing current input must remain an explicit exclusion and blocks promotion.

Crow's `320 -> 420 -> 380` main-dagger chain is the regression case: June must compare `320` with `420`, while July compares `420` with `380`; neither patch may be reconstructed directly from only the current `380`.

## Output Semantics

The JSON schema `balance_breakpoint_audit.v1` includes:

- provenance, ruleset, roster, and Power Level
- coverage of roster targets, reviewed packets, supported changes, and exclusions
- `threshold_summaries`, where counts mean `packets_to_kill <= N`
- only integer-changing `pair_deltas`, not the entire unchanged matrix
- `build_pressure_deltas` for base-versus-defense-option survival changes
- review seeds with assumptions and evidence refs

Coverage must distinguish:

- damage changes checked against every indexed target state
- HP/defense changes checked against the reviewed attacker packet set

If attacker packet coverage is incomplete, the report must not say “no other matchup changed.”

## Promotion Gate

A generated transition may enter an existing BP field only when all are true:

1. The patch before/after values and current state are source-consistent.
2. Packet, target form, legal loadout stack, and Power Level are reviewed.
3. An integer packet-count or defense-option requirement actually changed.
4. Distance, full-connect, form, resource, time-window, and map-route assumptions are realistic and written down.
5. The result maps to an existing consumer: build pressure to `build_switches`/`failure_modes`, a bilateral relation to `conditional_matchups`, or a route-specific realization to `map_feature_hooks`.
6. The promoted fact states mechanism, `active_when`, `fails_when`, and `bp_use`.

Tournament picks may corroborate that a state or build occurred. Frequency and results never enter the formula or promotion score.

## Commands

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/test_balance_breakpoints.py
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_balance_breakpoints.py \
  --manifest-source wiki/sources/Fandom-Release-Notes-June-2026.md \
  --manifest-source wiki/sources/Fandom-Maintenance-July-8-2026.md \
  --output outputs/balance-breakpoints/2026-june-july-balance-breakpoints.json \
  --report outputs/balance-breakpoints/2026-june-july-balance-breakpoints.md
```

To render only one patch's sections, add `--patch-id <id>` while still loading the complete ordered manifest chain so before/after continuity remains valid.
