# Brawler Modeling

Use this reference when creating, repairing, or auditing `wiki/entities/brawlers/` BP profiles.

## Scope

Brawler pages hold current stable BP modeling fields. They do not hold version history, temporary tier lists, or batch-progress notes.

Only write fields that can be consumed by compile/decide:

- `capability_vector`
- `build_switches`
- `map_feature_hooks`
- `objective_contracts`
- `failure_modes`
- `conditional_matchups`
- `slot_notes`

## Modeling Flow

1. Start from both `wiki/sources/Fandom-*` and `wiki/sources/PLP-*` pages and their raw provenance.
2. Convert Fandom mechanics into capability facts with source links.
3. Convert PLP matchup/build/mode signals into candidates, then review them against mechanism, map, build, and failure conditions.
4. Read relevant `wiki/entities/maps/` pages before finalizing `map_feature_hooks` or objective contracts.
5. Connect map hooks to route, position, objective payoff, active condition, failure condition, and BP use.
6. Update existing brawler pages by replacing or tightening stable BP fields, not by appending version history or batch-progress notes.
7. Write slot notes for slot 1, slots 2-3, slots 4-5, and slot 6.
8. Run `scripts/audit_bp_profile_quality.py`.

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
- Contains no automatic placeholders such as `unknown_pending`, `needs_review`, `not_inferred_from_source`, or `candidate_only_not_final`.

## Common Mistakes

- Copying PLP `countersThese` into unconditional `conditional_matchups`.
- Writing "good on open maps" without route and objective conversion.
- Treating a version strength bump as a permanent ability change.
- Marking a generated draft `bp_ready` because required sections exist.
