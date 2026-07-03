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
