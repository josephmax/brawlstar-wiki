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
| Pairwise differences | `outputs/balance-breakpoints/` | generated, reproducible, ephemeral ledger — see durability rule below |

**Durability rule (`outputs` is never persistent)**: everything under `outputs/` — including this audit and `runtime_bp_index` — is a gitignored, regenerable computation artifact: compile-or-generate on demand, use, discard. It is never part of the knowledge base and never a dependency of any page. Wiki pages must not link to or cite `outputs/` paths; a synthesis page digesting an audit must be self-contained (carry its own conclusions, tables, and reliability notes) and only record valuable audit conclusions. When the machine ledger is needed again, regenerate it deterministically from the `balance_patch_manifest` ledgers and stable profiles with the audit command in this reference.

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

### Numerically-grounded matchup review scope (2026-09-17 maintainer decision)

Breakpoint digestion into `conditional_matchups` is scoped to **numerically-grounded edges only** — edges whose `mechanism`/`active_when`/`fails_when` text carries a survival or kill-time premise that the breakpoint math can prove or falsify (burst windows, shot counts, outlast claims, "clears effective spawn health", low-HP finish ranges, shield-line requirements). For each patch:

- **Premise-class sub-test first**: before an integer transition fires a review, classify the premise as static-EHP class or sustain/healing class. Sustain premises (healing loops, regen, shield replenishment cycles, "回血/耐杀/outlast by healing") belong to the temporal-survival exclusion class — the static matrix cannot falsify them, so they never trigger direction review; they queue for packet/time-sequence modeling instead. Only static-EHP premises (fixed pools, non-regenerating barriers, flat DR windows) are auditable.
- Review only edges involving patch-involved parties (attacker packet changed, or target state/defense changed) whose premise text is numerically-grounded AND passed the sub-test.
- An integer transition that falsifies such a premise triggers rewrite, bundle-split, or demotion of that edge; a non-integer EHP drift never does.
- Edges that are positional or utility-based (body-block, wall control, scouting, routing, objective conversion) are out of scope even when both parties are patch-involved; their premises are not functions of the EHP matrix.
- Direction calls (favored side) still come from mechanism and source review, never from the audit matrix; the audit only fires the review, and a burst-window line at most annotates `fails_when` (e.g., "inside an anti-heal/focus window"), never flips a direction.
- Build-pressure findings route to `build_switches`/`failure_modes` regardless of this scope, since those fields are their named consumers.

### Capability-grounded matchup review (behavior reworks)

Behavior reworks — gadget/star-power/hypercharge reworks and new mechanics such as knockback, ammo steal, homing, purge — are not breakpoint quantities, so the numeric scope above is blind to them. But they change which matchup stories an edge can truthfully tell. Known regression case (2026-08 wave): Gus's Knockback Spirit rework reached `capability_vector`/`crowd_control` yet his dive-bundle edge kept telling the pre-rework Super-shield-only story.

For every patch that carries behavior-rework rows for a Brawler:

1. Curate the rework-atom list (ability atom plus keyword group) from the manifest's behavior rows and the brawler's reviewed stable fields. This list is maintainer knowledge, not script output.
2. Pair the curation with the community-evidence recheck required by `references/source-ingest.md` ("Rework- and Buffie-flavored changes"): re-check the current Fandom and PLP pages for new match-up evidence instead of inferring stories from the literal patch text, and use that evidence as the source for any edge a seed grows into.
3. Run `audit_capability_edge_coverage.py`: for each atom, check coverage in (a) the brawler's stable fact fields (`capability_vector`, `build_switches`, `map_feature_hooks`, `objective_contracts`) and (b) its `conditional_matchups` mechanism/active_when/fails_when text.
4. Missing capability coverage means the ingest fold itself was incomplete — fix the entity fields first. Missing edge coverage produces a **review seed**, never an edge: a maintainer decides whether the atom actually changes an edge story, using mechanism and source knowledge; direction is never set by the script. Many atoms are legitimately sub-edge loadout detail; an accepted seed is a closed review, not an open gap — record the maintainer rationale (e.g., "post-nerf the Brawler returned to the passive-peel positioning").
5. New or rewritten edge text follows the standard promotion discipline: mechanism, `active_when`, `fails_when`, `bp_use`, and a source ref; sustain-class caveats from the premise-class sub-test still apply (e.g., chase-down claims about healing Brawlers cannot lean on the static matrix).
6. Re-run the audit after ingest waves touching multiple Brawlers (full regression), not only for the single patch that triggered it.

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
