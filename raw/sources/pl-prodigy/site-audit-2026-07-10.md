# Raw Capture: Power League Prodigy Live-Site Audit (2026-07-10)

- Source: https://powerleagueprodigy.com/
- Sitemap: https://powerleagueprodigy.com/sitemap.xml
- Guide index: https://powerleagueprodigy.com/guides
- Blog index: https://powerleagueprodigy.com/blog
- Draft dataset surface: https://powerleagueprodigy.com/plprodigy
- Capture date: 2026-07-10
- Capture method: public sitemap/index inspection plus current public guide payload comparison against the local 2026-06-29/30 captures
- Capture boundary: current URL coverage, visible build fields, payload timestamps, blog recency, and dynamic-dataset metadata only; this is not a replacement for per-Brawler direct raw.

## URL and Publication State

- Public Brawler guide URLs: `104`; no additions or removals relative to the local 2026-06-29 roster manifest.
- `https://powerleagueprodigy.com/nori`: HTTP `404`.
- `https://powerleagueprodigy.com/wendy`: HTTP `404`.
- No July balance-analysis article was listed. The newest visible blog post was dated 2026-06-30.

## Current Guide Fields Observed

| Guide | Gadget | Star Power | Gears |
| --- | --- | --- | --- |
| https://powerleagueprodigy.com/8bit | Extra Credits | Boosted Booster | Damage, Health |
| https://powerleagueprodigy.com/brock | Rocket Laces | More Rockets | Damage, Shield |
| https://powerleagueprodigy.com/max | Sneaky Sneakers | Super Charged | Shield, Damage |

These fields differ from the corresponding local 2026-06-29/30 direct captures. They are retained as live-site audit observations until per-Brawler canonical raw can be recaptured.

## Dynamic Matchup and Dataset State

- Comparison against the 104 local captures found changed `countersThese` and/or `counteredBy` lists on `67` guides.
- Example current 8-Bit lists:
  - `countersThese`: Poco, Jae-Yong, Fang, Hank, Glowy, Rosa, Cordelius, Kit
  - `counteredBy`: Bolt, Sprout, Damian, Maisie, Ash, R-T, Brock, Buster
- The public draft dataset surface reported an update date of `2026-07-07` and `2,354,811` Masters+ games at capture time.

## Timestamp Caveat

- Sitemap `lastmod` remained `2026-05-23` for the guide URLs.
- Public guide payload `sourceUpdatedAt` remained `2026-05-25` for 103 guides and `2026-06-06` for Bolt.
- Therefore the live differences cannot be attributed specifically to July from PLP's exposed per-guide timestamps.
- Dynamic matchup lists are audit seeds only. They must not overwrite stable build facts or become unconditional matchup edges without a direct recapture and mechanism review.
