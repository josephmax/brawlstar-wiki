# Source Ingest

Use this reference when adding or refreshing Fandom, Power League Prodigy, roster, patch, user-note, map, or mode sources.

## Standard Flow

1. Read `AGENTS.md`, `wiki/index.md`, and `references/repo-layering.md`.
2. Identify source type, URL/path, capture date, and reliability.
3. Preserve raw material in `raw/` or confirm an existing raw capture.
4. Create or update a document-scoped page in `wiki/sources/`.
5. State `usable_for` and `not_usable_for`.
6. Update affected stable brawler/map/concept pages only when the source proves stable facts.
7. Update `wiki/index.md` if navigation changes.
8. Append `wiki/log.md`.

## Artifact Policy

`raw/`, `wiki/sources/`, `wiki/entities/brawlers/`, and `wiki/entities/maps/` are canonical knowledge writes, not temporary outputs.

Generated audit reports and runtime indexes go to `outputs/` or a caller-provided path. Do not write generated reports, handoff scratchpads, or runtime indexes back into `wiki/syntheses/`.

## Hero Fandom and PLP Ingest

Hero BP maintenance uses two default source families:

- Fandom brawler pages: stable mechanics, ability candidates, build/tip seeds, mode and map-feature hints.
- Power League Prodigy pages: third-party build, mode-fit, matchup, and slot-note candidates.

Fandom and PLP are complementary. PLP does not replace Fandom for mechanics, stats, attack/Super behavior, or stable ability facts. Fandom does not replace PLP for competitive build, mode-fit, matchup, or slot-note candidates.

Use these scripts for repeatable hero source work:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/capture_brawler_sources.py --dry-run --names Brock --sites fandom plp
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/ingest_brawler_sources.py --dry-run --names Brock
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/ingest_brawler_bp_profiles.py --dry-run --names Brock
```

`scripts/capture_brawler_sources.py` is hero-only. It reads `raw/sources/roster/brawlers-roster-2026-06-29.md`, accepts `--sites fandom`, `--sites plp`, or `--sites fandom plp`, and writes direct raw captures under `raw/sources/fandom/heroes/` and `raw/sources/pl-prodigy/brawlers/`.

`scripts/ingest_brawler_sources.py` reads those raw captures and writes `wiki/sources/Fandom-*` and `wiki/sources/PLP-*`. `scripts/ingest_brawler_bp_profiles.py` initializes or explicitly overwrites draft brawler profiles in `wiki/entities/brawlers/`; it does not make them reviewed or `bp_ready`.

Use `--force` or `--overwrite-existing-profile` only when the replacement scope is explicit and logged.

## Map Fandom ingest

Map source acquisition is from Brawl Stars Fandom map pages and Ranked map pool pages. Preserve map raw captures under `raw/sources/fandom/maps/`.

The current brawler capture scripts do not automate map capture. For map work, create or refresh a Fandom raw capture in `raw/sources/fandom/maps/`, then create or update a matching document-scoped source summary such as `wiki/sources/Fandom-Ranked-Season-46-Map-Pages.md`. That source summary should identify:

- source URL or page set
- capture date and source type
- included maps and missing maps
- map-mode pairing evidence
- what can be used for stable map structure
- what must remain season-only pool metadata

After the source summary exists, update `wiki/entities/maps/<Map Name>.md` only with stable map structure, routes, objective facts, terrain state, and BP factors. A Ranked season page may index which maps are active in that season, but it must not become the stable map fact layer.

## Raw Coverage Rules

Same-source raw may cover older raw only when the new capture fully contains the old capture's relevant evidence, or the old file is a correction-stage duplicate. Otherwise keep both captures.

Keep separate sources when they provide different evidence fields, different time points, different page states, or different source perspectives. For hero ingest, Fandom and PLP are normally kept together because their evidence roles are different. For map ingest, a Ranked map pool capture and an individual map page capture are kept together unless one demonstrably fully covers the other's map set and fields.
