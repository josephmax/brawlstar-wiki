# Brawler Modeling

Use this reference when creating, repairing, or auditing `wiki/entities/brawlers/` BP profiles.

## Scope

Brawler pages hold current stable BP modeling fields. They do not hold version history, temporary tier lists, or batch-progress notes.

The first `bp_brawler_profile` block only contains fields consumed by compile/decide:

- `capability_vector`
- `build_switches`
- `map_feature_hooks`
- `objective_contracts`
- `failure_modes`
- `conditional_matchups`
- `slot_notes`

A brawler page may contain a second fenced JSON `combat_breakpoint_profile` block for current stable numerical mechanics consumed only by the maintainer breakpoint audit. It is not a runtime field. Allowed contents are reviewed `target_states`, discrete `damage_packets`, `defense_modifiers`/`defense_variants`, and explicit temporal or source-conflict exclusions. Do not store patch history, generated pairwise matrices, tiers, or review seeds in this block.

The audit may fall back to the latest direct Fandom `Health`/`Health1` for a primary body so every roster brawler can enter the health index. Alternate forms, split bodies, summons, multi-hit packets, distance scaling, cycles, DoT, and hero-specific defenses require explicit reviewed semantics; a bare infobox scalar is not enough.

## Modeling Flow

1. Start from both `wiki/sources/Fandom-*` and `wiki/sources/PLP-*` pages and their raw provenance.
2. Convert Fandom mechanics into capability facts with source links.
3. Convert PLP matchup/build/mode signals into candidates, then review them against mechanism, map, build, and failure conditions. PLP mode recommendations are reverse-validation evidence, not the scope of evaluation — every Ranked mode must be independently evaluated regardless of whether PLP recommends it.
4. Read relevant `wiki/entities/maps/` pages before finalizing `map_feature_hooks` or objective contracts. Evaluate the brawler's capability-to-map fit for all six Ranked modes, not only PLP-recommended ones.
5. Connect map hooks to route, position, objective payoff, active condition, failure condition, and BP use.
6. Update existing brawler pages by replacing or tightening stable BP fields, not by appending version history or batch-progress notes.
7. Write slot notes for slot 1, slots 2-3, slots 4-5, and slot 6.
8. Run `scripts/audit_bp_profile_quality.py`.
9. If health, damage, barrier, or damage reduction changed, update `combat_breakpoint_profile`, run `scripts/audit_balance_breakpoints.py`, and review its coverage/exclusions without auto-promoting results.

Fandom and PLP are complementary here. PLP does not replace Fandom mechanics, and Fandom does not replace PLP competitive candidates. If they conflict, preserve the difference in source summaries and only promote the claim that survives mechanism, map, build, and failure review.

## Status Rules

`draft_from_raw_signals`:

- May contain `pending`, `unknown`, or `needs_review`.
- May keep PLP matchup seeds as unreviewed candidates.
- Must not be used as final counter, map-fit, or pick-order evidence.

`reviewed`:

- Removes automatic extraction residue.
- Explains build deltas, objective duties, at least three failure modes, and slot-specific jobs.
- Keeps matchup candidates conditional.

`bp_ready`:

- Meets reviewed requirements.
- Has reviewed conditional matchups with `mechanism`, `active_when`, `fails_when`, and `bp_use`.
- Has map hooks tied to concrete routes, maps, positions, objectives, and failure cases.
- Has an `objective_contract` for every mode in the current Ranked mode pool (Gem Grab, Brawl Ball, Heist, Bounty, Hot Zone, Knockout). A contract that concludes the brawler is a false positive or poor fit for a mode counts as valid coverage — the requirement is that the evaluation exists, not that it is positive. Missing contracts produce silent false negatives in compile (`fit=weak` indistinguishable from genuine weakness).
- Contains no automatic placeholders such as `unknown_pending`, `needs_review`, `not_inferred_from_source`, or `candidate_only_not_final`.
- All health, damage, and EHP numbers cited in `capability_vector`, `objective_contracts`, `failure_modes`, `map_feature_hooks`, `build_switches`, `conditional_matchups`, and `slot_notes` must be Power Level 11 values. Fandom infobox values are Power Level 1; multiply by `2.0` before writing them into any BP evaluation field. Label the value as "Power 11" on first use in a field. The `combat_breakpoint_profile` JSON block continues to record raw `at_power_level: 1` source values for the maintainer breakpoint audit; that block is not a BP evaluation field and is exempt.

## Common Mistakes

- Copying PLP `countersThese` into unconditional `conditional_matchups`.
- Writing "good on open maps" without route and objective conversion.
- Treating a version strength bump as a permanent ability change.
- Marking a generated draft `bp_ready` because required sections exist.
- Multiplying a bare `Attack` field by `AttackBullets` without reviewing whether it means projectile, tick, range endpoint, sequence step, form, or full ammo.
- Combining alternate-form health pools or summon/deployable health into the roster brawler denominator.
- Copying a generated integer breakpoint directly into `conditional_matchups` without mechanism, conditions, map route, failure case, and `bp_use`.
- Citing Power Level 1 health or damage values (raw Fandom infobox numbers) in BP evaluation fields without multiplying by `2.0` to get Power Level 11. Power Level is a progression artifact, not a BP factor — all strength comparisons must use a single normalized level so brawlers are never judged weaker or stronger based on an irrelevant growth scalar.
