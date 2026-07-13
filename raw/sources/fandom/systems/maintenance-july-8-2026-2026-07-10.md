# Direct Raw Capture: Fandom Maintenance - July 8, 2026

- Title: Version History/2026 - Maintenance - July 8
- Source URL: https://brawlstars.fandom.com/wiki/Version_History/2026
- Section API: https://brawlstars.fandom.com/api.php?action=parse&page=Version%20History%2F2026&prop=wikitext&section=1&format=json&formatversion=2
- Capture date: 2026-07-10
- Fandom page last edited at capture: 2026-07-10T08:18:04Z
- Cross-check: https://supercell.com/en/games/brawlstars/blog/release-notes/release-notes-june-2026/
- Capture boundary: July 8 maintenance balance inventory and BP-relevant bug-fix observations. Cosmetic and client-only fixes are omitted.
- Processing note: numeric values and affected abilities are preserved; surrounding prose is normalized into compact records.

## Balance Changes

### Buffs

- Jacky: health `5000 -> 5200`.
- Bonnie: main attack damage `1120 -> 1220`.
- Jessie: main attack projectile speed `2870 -> 3050`.

### Nerfs

- 8-Bit:
  - Buffied Extra Credits bounce damage `75% -> 60%`.
  - Buffied Boosted Booster ammo spawn interval `3s -> 5s`.
  - Hypercharge rate reduced by `15%`.
- Surge:
  - Power Shield cooldown `18s -> 22s`.
  - Hypercharge range `20 -> 16`.
  - Buffied Hypercharge second-shot damage `70% -> 50%`.
  - Hypercharge projectile damage `1000 -> 800`.
- Brock:
  - Buffied Rocket No. 4 extra-range interval `4s -> 6s`.
  - The patch text says a Gadget knockback was removed; source naming is inconsistent with current individual-page ability names and requires per-page resolution.
- Meg:
  - Toolbox Super-charge duration `4s -> 6s`.
  - Buffied Jolting Volts extra duration `2s -> 1s`.
  - Mecha main-attack Super-charge rate reduced by `60%`.
  - Buffied Hypercharge main-attack Super-charge rate reduced by `60%`.
- Crow: main attack damage `420 -> 380`.
- Colette: charm duration `1s -> 0.5s`; the patch labels it `Gotcha!`, while the current individual page assigns the charm to `Na-ah!`.
- Starr Nova:
  - main attack damage `540 -> 480`.
  - Super charge rate increased by `11%`.
  - official note says the attack count remains `10 hits`; Fandom individual History has conflicting wording.
- Max: Buffied Hypercharge main-attack Super charge `8% -> 7%`.

## BP-Relevant Bug-Fix Observations

- Rico can no longer use Bouncy Castle in the Shadow Realm or charge Super by bouncing Super Bouncy shots from walls into Power Cube boxes.
- Mortis Hypercharge damage with Buffie was corrected upward to intended behavior.
- Sirius Shadow stats now scale from the copied Brawler rather than from Sirius' health.
- Starr Nova can no longer chain a second Hypercharged Super and nearly refill Hypercharge through the prior bug.
- Crow Hypercharge poison damage with Buffies and Star Power 2 was corrected.
- Carl and Charlie no longer fire duplicate returning projectiles after collecting 8-Bit's ammo clips.
- Byron Hypercharged attack damage was corrected.
- Larry & Lawrie, Jacky/Sprout, and Emz fixes are Nano-event interactions and are not general Ranked mechanics.

## Source Conflicts To Preserve

- Colette: patch index says `Gotcha!`; current Fandom mechanics place the 0.5-second charm under `Na-ah!`.
- Brock: patch index says `Rocket Barrage Gadget`; current Fandom page has Rocket Laces / Rocket Fuel Gadgets and Rocket Barrage Hypercharge.
- Starr Nova: official note says the Super remains a 10-hit charge; Fandom History reports a different hit-count transition.
- Surge individual History omits several Hypercharge nerfs listed in the maintenance index.
- Meg individual History expresses some charge changes as hit-count / 99% details not stated verbatim in the maintenance index.

## Raw Use Boundary

- Use the maintenance page as the affected-Brawler index.
- Use current individual Fandom pages to resolve present ability behavior.
- Do not promote conflicting labels or purely numeric changes into stable BP facts without a clear consumer and qualitative consequence.
