# Direct Raw Capture: Power Points stat scaling

- Title: Power Points | Brawl Stars Wiki | Fandom
- URL: https://brawlstars.fandom.com/wiki/Power_Points
- Capture date: 2026-07-17
- Capture method: web search result excerpt; direct page semantics retained
- Topic bucket: gameplay

## Relevant visible content

- Brawlers can be upgraded through Power Level 11.
- Each Power Level linearly increases a Brawler's health and damage by 10% relative to the Power Level 1 value.
- The page's example states that Power Level 5 has 40% more health and damage than Power Level 1.
- History records that on 2023-09-05, per-level health and damage growth changed from 5% to 10%.
- Gear slots unlock before Power Level 11, while Hypercharge unlocks at Power Level 11.

## Breakpoint implication

For current Ranked / maxed-brawler audits, a Power Level 1 infobox health or damage scalar is normalized to Power Level 11 with factor `1 + 10 * 0.10 = 2.0`. Flat Gear values such as a `+900` consumable Shield are already absolute equipment values and must not be multiplied by this factor.
