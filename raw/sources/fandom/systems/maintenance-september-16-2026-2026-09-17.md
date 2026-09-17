# Direct Raw Capture: Fandom Maintenance - September 16, 2026

- Title: Version History/2026 - Maintenance - September 16th
- Source URL: https://brawlstars.fandom.com/wiki/Version_History/2026
- API URL: https://brawlstars.fandom.com/api.php?action=query&prop=revisions&titles=Version%20History%2F2026&rvslots=main&rvprop=ids%7Ctimestamp%7Ccontent&format=json
- Capture date: 2026-09-17
- Fandom revision at capture: revid 219043, 2026-09-16T09:12:51Z
- Capture boundary: September 16 maintenance balance inventory and bug-fix observations. Client/cosmetic fixes are recorded only when they touch combat-relevant behavior.
- Processing note: numeric values and affected abilities are preserved verbatim from the wikitext; surrounding prose is normalized into compact records.

## Balance Changes

### Nerfs

- Shade:
  - Super Charge when near enemies reduced by `15%`.
  - Gadget 'Long arms' cooldown `18s -> 20s`.
  - Gadget 'Jump scare' fear radius `1000 -> 600`.
  - Hypercharge Buffie bonus damage `75% -> 30%`.
- Gus:
  - Gadget 'Knockback spirit' cooldown increased to `18s` (no `from` value stated in the source).
  - Star Power 'Health Bonanza' healing increase `100% -> 75%`.
- El Primo:
  - Gadget 'Asteroid Belt' cooldown `16s -> 20s`.
  - Gadget 'Asteroid Belt' Super gained from projectiles reduced by `50%`.
  - Star Power 'Meteor Rush' speedboost duration `4s -> 3s`.
  - Star Power 'Meteor Rush' shield `20% -> 15%`.
- Amber:
  - Gadget 'Fire Starters' health `1750 -> 1300`.
  - Star Power 'Wild Flames' oil trail duration `3s -> 1s`.
  - Hypercharge Buffie burn damage `500 -> 240`.
- Nori:
  - Main Attack max charge time increased by `25%`.
  - Hypercharge rate `50 -> 28`.
- Wendy:
  - Health `2000 -> 2500`.
  - Shield on spawn `100% max health -> 40% max health`.
  - Shield gained from main attack `580 -> 300`.
  - Star Power 'Solar Shield' bonus health `1000 -> 600`.
  - Hypercharge turret health `4500 -> 3500`.
  - Gadget 'Wind-Powered' can now jump on water (behavior change, no number).
- Meg:
  - Gadget 'Repurpose' knockback on projectile removed (now only on the explosion).
- Colette:
  - Hypercharge Buffie second projectile damage `50% -> 35%`.
- Brock:
  - Gadget 'Rocket Laces' cooldown `20s -> 22s`.
  - Super Charge from Super `80 -> 70`.

### Buffs

- Poco:
  - Gadget 'Tuning Fork' healing `500 -> 700`.
  - Star Power 'Da Capo' healing `320 -> 400`.
- Chuck:
  - Star Power 'Pit Stop' slow duration `1s -> 2s`.
  - Star Power 'Pit Stop' slow potency `20% -> 30%`.
  - Star Power 'Pit Stop' Buffie area damage `100 -> 400`.
- Ollie:
  - Main attack damage `900 -> 1000`.
- Trunk:
  - Main attack movement speed on ants `25% -> 30%`.
  - Super Charge rate `70 -> 75`.
- Willow:
  - Main Attack reload speed `2000 -> 1800`.
  - Health `3300 -> 3600`.
- Juju:
  - Health `3100 -> 3500`.
  - Super Charge rate `65 -> 75`.
- Pam:
  - Super turret health `3040 -> 3300`.
  - Super healing `500 -> 600`.
  - Hypercharge turret health `4200 -> 4500`.
- Belle:
  - Main attack damage `1040 -> 1140`.
- R-T:
  - Star Power 'Recording' damage resistance `20% -> 25%`.

## Bug Fixes

- Respawn shields are now removed when using a dash or jump ability (combat-relevant survival-window change; no static number).
- Kaze, Moe, Meg, and Bonnie no longer receive an unintended respawn shield when changing forms in Showdown (Showdown-scoped form-change shield fix).
- Colt's Star Power 'Magnum Special' now increases bullet speed correctly when using a Skin.
- Bea's Gadget 'Rattled Hive' and Cosmo's main attack now end in the same position on mirrored maps.
- Cosmo's main attack now follows the same path on both the True Blue and True Red sides.
- Eve's Hypercharged Super now spawns 4 hatchlings when it explodes (as it should; aligns with the August change `hatchling count 3 -> 4`).
- Players are no longer charged multiple times the 1000 Coins for the Club creation fee.
- The goal line is now clearly visible on Brawl Ball 5v5 maps using the Duolingo environment.
- Jump pads are no longer blocked by invisible walls on the Crescendo and Brawlerverse 5v5 Knockout maps.
- Brawl Ball matches now end correctly at 0:00 when a ball is stuck inside the walls.
- Mega Boxes no longer grant the full Credit amount twice when the final reward from multiple Credit drops unlocks a new Brawler on Starr Road.

## Raw Use Boundary

- Use the maintenance page as the affected-Brawler index; resolve present ability behavior on current individual Fandom pages.
- Amber 'Fire Starters' health is stated here as `1750 -> 1300`; the August release-notes layer recorded the reworked barrel as `3500` durability. The two figures are consistent under Power Level 1 vs Power Level 11 standard scaling (1750 x 2 = 3500); keep the Power Level explicit on any derived row.
- Gus 'Knockback spirit' cooldown has no explicit `from` value in the source; the August rework introduced the gadget, so the `from` side must be resolved against the current page before any continuous-chain claim.
