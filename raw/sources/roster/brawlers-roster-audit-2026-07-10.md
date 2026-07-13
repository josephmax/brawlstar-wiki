# Raw Capture: Brawlers Roster Audit (2026-07-10)

- Source 1: Fandom `Category:Brawlers` page and MediaWiki category API
- Source 1 page: https://brawlstars.fandom.com/wiki/Category:Brawlers
- Source 1 API: https://brawlstars.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category%3ABrawlers&cmlimit=500&cmnamespace=0&format=json
- Source 2: Power League Prodigy sitemap and guide index
- Source 2 sitemap: https://powerleagueprodigy.com/sitemap.xml
- Source 2 guide index: https://powerleagueprodigy.com/guides
- Capture date: 2026-07-10
- Capture boundary: roster membership, release state, and public guide URL availability only; hero mechanics and competitive recommendations require per-hero raw captures.
- Previous manifest: [[brawlers-roster-2026-06-29]]

## Fandom Observation

- The rendered category page states that there are currently `105` Brawlers in the game.
- The namespace-0 category API returned `107` page titles.
- Relative to the previous 104-Brawler persistent set, the newly observed titles are `Nori` and `Wendy`; the remaining extra category member is the removed limited-time `Buzz Lightyear` page.
- `Nori` page revision observed: `2026-07-09T13:55:36Z` (`revid 215901`). Its History states that Nori became playable in the Training Cave and available for early unlock on 2026-07-09.
- `Wendy` page revision observed: `2026-07-04T19:19:42Z` (`revid 215616`). It still carries `FutureUpdate`, calls Wendy the future 106th Brawler, and has no release History entry.

## PLP Observation

- The sitemap and guide index still expose `104` Brawler guide URLs, with no additions or removals relative to the 2026-06-29 manifest.
- `https://powerleagueprodigy.com/nori` returned HTTP `404`.
- `https://powerleagueprodigy.com/wendy` returned HTTP `404`.
- The PLP blog had no July balance article at capture time; its newest listed post was dated 2026-06-30.

## Captured Scope Decision

- Current released Brawler count: `105` (`Nori` added to the prior 104).
- Current PLP guide coverage: `104`.
- `Nori` is active but lacks PLP guide coverage and a reviewed BP profile.
- `Wendy` remains future-only and is not part of the active catalog.
- This raw audit does not promote either page into runtime BP evidence by itself.
