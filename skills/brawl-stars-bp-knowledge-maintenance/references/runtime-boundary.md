# Runtime Boundary

Use this reference when updating maintenance rules, runtime skill references, or `runtime_bp_index` architecture.

## Separation

Maintenance may read broad context. Runtime must be narrow.

Maintenance skill may read:

- `raw/`
- `wiki/sources/`
- `wiki/syntheses/`
- `wiki/entities/`
- `skills/`
- `outputs/`

Runtime slot decision may read:

- `skills/brawl-stars-bp-slot-decision/references/compile-knowledge.md`
- `skills/brawl-stars-bp-slot-decision/references/runtime-decision-knowledge.md`
- relevant `wiki/entities/maps/`
- relevant `wiki/entities/brawlers/`
- supplied strength profile
- compiled `runtime_bp_index`

`tournament_observation_profile.v1` is a maintainer output in Phase 1, not an allowed runtime input. Tournament observations must not auto-generate strength tiers, hard gates, map fit, slot eligibility, or matchup edges. A separately reviewed maintainer interpretation may later be supplied through the existing strength-profile boundary.

`combat_breakpoint_profile` and `balance_breakpoint_audit.v1` are also maintainer-only inputs/outputs in v1. Runtime compile reads the first `bp_brawler_profile` block and must ignore the second combat block and every `outputs/balance-breakpoints/` report. A numeric transition reaches runtime only after a maintainer validates its packet/form/build/map assumptions and rewrites the durable qualitative consequence into an existing `build_switches`, `failure_modes`, `conditional_matchups`, or `map_feature_hooks` field.

## Rule Promotion

If a maintainer conclusion becomes an operational runtime rule:

1. Copy the rule into the appropriate runtime skill reference.
2. Add or update `scripts/test_bp_skill_contract.py`.
3. Keep the synthesis page as explanation/archive only.

Do not expect runtime skills to read `wiki/syntheses/` for missing operational rules.

## runtime_bp_index

The `runtime_bp_index` is a generated session artifact, not a long-term wiki page.

It should compile:

- map duties
- brawler cards
- map-brawler edges
- draft edges
- strength context
- source hashes or stable refs

Write generated indexes to `outputs/` or a caller-provided path. Do not write hand-maintained decision indexes back into `wiki/syntheses/`.

## Boundary Failure Modes

- Runtime decision cites a maintainer synthesis page as pick evidence.
- A brawler page stores temporary tier strength instead of stable capability.
- A map page stores current strong heroes instead of route/objective facts.
- A source summary becomes the only copy of raw evidence.
- An audit report becomes a long-term synthesis page.
- Runtime reads a pairwise breakpoint matrix or treats a Shield-gear pressure seed as an automatic matchup edge.
