# Environment Signal Ingest

Use this reference when maintaining the BP environment signal: the high-rank pick/use-rate layer and the monthly ban layer. The environment signal is the successor of the retired strength layer (see `wiki/syntheses/BP-强度层语义回归与高分选取率估计器.md`); it is a descriptive draft, not a runtime input until separately reviewed and promoted.

## Signal Structure

The environment signal has two layers with different windows:

| Layer | Source | Window | Rank floor | Rate |
| --- | --- | --- | --- | --- |
| pick / use rate | Brawl Planet `pl-l1-results.json.gz` | rolling 10 weeks | Legendary+ | `use_rate` (ur %) |
| ban rate | Liquipedia Monthly Finals aggregation | monthly | pro (legendary+ approximation) | `ban_rate` |

- `manifest.pickrate_source` / `manifest.pickrate_status` in the compiler currently record the empty slot; the aggregated signal is the candidate payload for `pickrate_status: ready` after reviewed promotion.
- The two layers have different windows; when merging, keep them as separate fields with explicit `window` labels, never average them into one number.

## Monthly Workflow

1. **Pick layer**: run `fetch_brawlplanet_pickrate.py --tier l1` (Legendary+) and write to `outputs/runtime-bp-index/environment-signal-pickrate-legendary-plus.json`.
2. **Ban layer**: capture each region's Monthly Finals with `capture_liquipedia_event.py`, analyze with `analyze_esports_event.py`, then aggregate with `aggregate_environment_signal.py` (paired pick/ban per brawler, set-level denominator).
3. Merge into a single `brawlstar.environment_signal.v1` with both layers labeled, plus `summary` (sample sizes), `fetched_at`, and `policy`.
4. Only after maintainer review, promote the signal into the compiler's pickrate slot and flip `manifest.pickrate_status` from `empty` to the source id.

## Rules

- Do not write tournament or ladder pick/ban rates into `wiki/entities/brawlers/`. Event entities keep event facts; brawler entities keep stable mechanisms and BP contracts.
- Do not auto-generate tiers, hard gates, map fit, slot eligibility, or matchup edges from the signal.
- Do not consume the signal directly in `decide`; it is a draft until reviewed promotion.
- Normalize all brawler names through `wiki/concepts/英雄名称归一化.md` / canonical entity names; drop and log unmatched names.
- Filter future-only brawlers (e.g., Wendy) out of the signal.
- Brawl Planet GCS filenames or bucket layout may change; keep the fetcher's file map maintainable and record the capture date in the output.
- Liquipedia access follows `esports-event-ingest.md` (MediaWiki API, gzip, one request per 2s, custom UA, revision provenance).

## Related

- `wiki/sources/Brawl-Planet-站点与数据接口.md`
- `scripts/fetch_brawlplanet_pickrate.py`
- `scripts/aggregate_environment_signal.py`
- `scripts/capture_liquipedia_event.py` / `scripts/analyze_esports_event.py`
- `wiki/syntheses/BP-强度层语义回归与高分选取率估计器.md`
