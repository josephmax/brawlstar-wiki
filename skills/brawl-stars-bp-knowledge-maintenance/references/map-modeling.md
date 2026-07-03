# Map Modeling

Use this reference when creating or repairing `wiki/entities/maps/` pages, Ranked map-pool indexes, or map-related BP factors.

## Source Route

Map data starts from Fandom ingest, not from draft-time intuition:

1. Capture or confirm Brawl Stars Fandom map pages under `raw/sources/fandom/maps/`.
2. Create or update the matching `wiki/sources/Fandom-*Map*` source summary.
3. Use the source summary plus raw provenance to update stable map entity pages in `wiki/entities/maps/`.
4. Keep season map-pool status in a season index page; do not merge season membership into stable map structure.

If map raw is missing, do not invent route, wall, bush, water, or objective facts. Capture the source first or mark the map page as needing source coverage.

## Stable Map Entity

Map entity pages should describe structure and BP-consumable map facts:

- `map_profile`
- topology, walls, bushes, water/void, routes, objectives
- tactical features
- lane dynamics
- `map_bp_factors`
- hard gates, false-positive filters, terrain state plans

Do not store current strong heroes, temporary counter claims, or season-only entry status in the map entity page.

## Three-Step Consumption

1. Stable facts: what the map contains.
2. BP factors: what duties, gates, routes, rewards, and failure conditions the facts create.
3. Decision index: how those factors combine with brawler facts and strength profile into `runtime_bp_index`.

Use the Fandom source for terrain and map-mode evidence. Use maintainer synthesis only to understand schema or modeling policy; do not cite synthesis pages as the provenance for a map's concrete structure.

## Five-Layer Check

Every map factor or candidate map-fit claim should trace to at least one layer:

1. Objective contract.
2. Lane and route contract.
3. Terrain state.
4. Draft slot pressure.
5. Counter and failure audit.

## Required Specificity

Avoid coarse direct signals. Convert them first:

- `open` -> named sightline, target, exposure, and objective payoff.
- `wall density` -> specific wall block, protected route, break target, or pocket.
- `grass` -> connected path, scout tax, ambush endpoint, and retreat condition.
- `water` -> actual shortcut, projectile block, objective barrier, or mobility-only route.

## Mode Duties

- Heist: safe access, objective damage, defense, race conversion, wall state.
- Brawl Ball: goal structure, wall/grass routes, scoring windows, reset tools.
- Hot Zone: zone time, clear/stand/deny cycles, wall-protected or open-zone state.
- Gem Grab: mine control, carrier safety, flank access, scout tax.
- Bounty: low-risk pressure, star safety, vision, comeback routes.
- Knockout: first-kill pressure, collapse, late-circle terrain, anti-engage.

## False-Positive Filters

Reject or demote claims like:

- "walls mean thrower" when walls do not protect objective pressure.
- "grass means assassin" when grass does not connect to a target or exit.
- "open means sniper" when the mode requires standing, scoring, or safe damage access.
- "Heist only needs DPS" when the candidate cannot reach safe or defend the race.
