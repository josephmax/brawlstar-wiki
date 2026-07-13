# Esports Event Ingest

Use this reference when capturing, parsing, ingesting, analyzing, or auditing Brawl Stars competitive events. Phase 1 supports Liquipedia Brawl Stars event pages through their MediaWiki API.

## Domain Terms

- `event`: a trackable tournament instance, such as one region's Monthly Finals.
- `series`: one team-versus-team match. In the current BSC Monthly Finals format, a series is Bo5 sets and the first team to 3 set wins advances.
- `set`: one map/mode draft played as a Bo3 of games. A 3-1 series therefore contains 4 played sets, not 4 separate series.
- `game`: one in-client round inside a set.
- `global ban`: match-level `Match.t1b* / t2b*` data that applies to a series. Generated observation metrics include played series only; forfeit fields remain in raw provenance.
- `local ban nomination`: set-level `Map.t1b* / t2b*` data. If both teams nominate the same brawler, count two nominations but one unique set coverage.
- `map_veto_first_pick_team`: `MapVeto.firstpick`; this is map-veto initiative, not brawler draft order.
- `draft_first_pick_team`: `Map.firstpick` only when explicitly populated. An empty field means draft order is unknown.
- `tournament_observation_profile.v1`: generated descriptive evidence over actually played sets. It is neither a tier list nor a runtime BP input.

## Liquipedia Access Contract

Follow [Liquipedia API terms](https://liquipedia.net/api-terms-of-use):

- Use `https://liquipedia.net/brawlstars/api.php` and MediaWiki `action=query&prop=revisions&rvslots=main&rvprop=ids|timestamp|content`.
- Do not automate normal HTML pages. Use the API endpoint.
- Send a custom User-Agent that identifies the project/use and includes contact information.
- Send `Accept-Encoding: gzip` and reuse one HTTP connection for a batch.
- Keep MediaWiki API traffic at no more than one request per two seconds. `action=parse` has a stricter one-request-per-30-seconds limit and is not used by the capture script.
- Reuse cached raw captures. If the same dated target exists, skip it unless `--force` is explicit.
- Preserve revision ID, revision timestamp, capture timestamp, source URL, API URL, and full source wikitext.
- Liquipedia content is CC BY-SA 3.0. Raw and source pages must attribute Liquipedia contributors and retain the source link.

Fresh event pages can receive corrections. A capture is a revision-specific observation, not an assertion that the page can never change. Recapture to a new dated raw file or explicitly overwrite the same-date target with `--force`; do not silently mutate old revision provenance.

## Layering

| Artifact | Path | Responsibility |
| --- | --- | --- |
| Direct raw capture | `raw/sources/liquipedia/events/` | Full wikitext, revision provenance, and deterministic parsed event JSON |
| Source summary | `wiki/sources/Liquipedia-*` | Document-scoped results, data coverage, semantics, attribution, usable/not-usable boundaries |
| Event entity | `wiki/entities/events/` | Stable identity, date, region, format, champion, runner-up, played series/sets, map-mode occurrence |
| Observation profile | `outputs/esports/*.json` | Generated pick/ban/set-win counts at event/global/mode/map scopes |
| Knowledge-gap audit | `outputs/esports/*.md` | Missing entity/map coverage and optional runtime-fit review seeds |

Do not write tournament pick rates, win rates, or ban rates directly into `wiki/entities/brawlers/`. Event entities keep event facts; brawler entities keep stable mechanisms and BP contracts.

## Capture and Ingest Workflow

Dry-run the capture targets:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/capture_liquipedia_event.py \
  --event Brawl_Stars_Championship/2026/Season_5/EMEA/Monthly_Finals \
  --dry-run
```

Capture one or more pages. Repeated requests share a connection and are spaced by at least two seconds:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/capture_liquipedia_event.py \
  --event Brawl_Stars_Championship/2026/Season_5/EMEA/Monthly_Finals \
  --event Brawl_Stars_Championship/2026/Season_5/South_America/Monthly_Finals
```

Then create or refresh the document-scoped source summary and event entity:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/ingest_liquipedia_event.py \
  --raw raw/sources/liquipedia/events/<capture>.md \
  --dry-run
```

After canonical writes, update `wiki/index.md` for new event/source navigation and append `wiki/log.md`.

## Parsing and Metric Semantics

The parser must remain deterministic and source-shaped:

- Exclude `winner=skip` placeholders.
- Exclude forfeited series from played-series and played-set denominators; keep the forfeit as an event result.
- Determine a set winner from its `score1` / `score2`. These are game scores inside the set.
- Preserve team picks as team rosters. `t1c1..3` and `t2c1..3` must not be presented as chronological pick order unless `Map.firstpick` is populated and a separate draft-order parser is proven.
- Normalize brawler names using `wiki/concepts/英雄名称归一化.md`; do not add a script-local alias table.
- `pick_sets` uses played sets as denominator.
- `set_wins_when_picked` is a descriptive set result, not individual-game wins and not causal credit.
- Keep local ban nominations, local unique-set coverage, global ban nominations, and global unique-series coverage as separate atomic metrics.
- Do not produce a composite meta score.

Generate a neutral observation profile:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/analyze_esports_event.py \
  --raw raw/sources/liquipedia/events/<capture-a>.md \
  --raw raw/sources/liquipedia/events/<capture-b>.md \
  --output outputs/esports/tournament-observation-profile.json
```

## Wiki and BP Connection

The connection is a gated evidence flow:

```text
event raw -> event source/entity -> tournament_observation_profile.v1
                                      |
                                      +-> knowledge-gap audit -> VOD/draft-context review
                                      |
                                      +-> separate maintainer interpretation -> optional supplied strength profile
```

The observation profile must not auto-generate a strength tier. It also must not create:

- `hard_gate`
- `required_capabilities`
- map fit or slot eligibility
- unconditional matchup edges
- early/response/late pick recommendations

There are three valid downstream connections:

1. `coverage-gap review`: use observed map-brawler pairs to find missing map entities, missing brawler entities, or compiled weak-fit cases that deserve VOD and draft-context review.
2. `stable fact promotion`: after replay/mechanism review proves why a choice worked and when it fails, update the corresponding stable map route, brawler `map_feature_hook`, `objective_contract`, `failure_mode`, or conditional matchup. The event frequency alone is insufficient.
3. `strength interpretation`: a maintainer may separately create a reviewed, version-scoped `strength_profile` using tournament observations as one cited input. This remains an explicit human/maintainer judgment step; Phase 1 does not wire the observation profile into the BP compiler.

Tournament drafts may later become replay/evaluation cases for BP quality, but a professional pick is evidence of a realized choice, not the unique correct answer. Team scouting is also a later entity/profile layer and must not be mixed into general brawler strength.

## Knowledge-Gap Audit

Run structural coverage checks after generating the profile:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_tournament_observations.py \
  --observation-profile outputs/esports/tournament-observation-profile.json \
  --runtime-index outputs/runtime-bp-index/<index>.json \
  --output outputs/esports/tournament-knowledge-gap-audit.md
```

Without `--runtime-index`, the audit checks missing brawler and map entities. With a compiled index, repeated observed picks whose `map_floor_fit` is weak become `needs_vod_and_draft_context_review` seeds. They are not automatic proof that the compiler or wiki is wrong.
