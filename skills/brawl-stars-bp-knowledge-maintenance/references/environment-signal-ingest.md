# Environment Signal Ingest

Use this reference when maintaining the BP environment signal: the high-rank pick/use-rate layer and the monthly ban layer. The environment signal is the successor of the retired strength layer (see `wiki/syntheses/BP-强度层语义回归与高分选取率估计器.md`); it is the evidence layer for the three-dimension decision framework: mechanism constraints (highest weight) + Legendary+ ladder anchor (high, with lag label) + monthly ban hint (low). The mechanism layer is complete and authoritative; the environment signal updates and corroborates it, never overrides it.

## Signal Structure

The environment signal has two layers with different windows:

| Layer | Source | Window | Rank floor | Rate |
| --- | --- | --- | --- | --- |
| pick / use rate | Brawl Planet `pl-l1-results.json.gz` | rolling 10 weeks | Legendary+ | `use_rate` (ur %) |
| ban rate | Liquipedia Monthly Finals aggregation | monthly | pro (legendary+ approximation) | `ban_rate` |

- **Current status (2026-08-14 architecture turn): compile-folded evidence.** Maintenance archives the signals under `wiki/environment/`; `compile` is the only aggregator and folds them into the `runtime_bp_index` as per-brawler `environment_evidence` (`ladder_anchor` / `monthly_finals`) plus `environment_ladder_per_map`, with window / rank_floor / fetch-or-capture labels. `decide` reads the embedded evidence through `hydrate_runtime_facts.py` for `evidence_roles`; it never reads signal files directly. The evidence never becomes fit/eligibility and never generates tiers. It is corroboration for the decision, not a replacement for mechanism reasoning. Evidence strength changes with each update (new month, refreshed 10-week window) without changing the three-dimension framework itself.
- Keep the two layers as separate fields with explicit `window` labels; never average them into one number.

## Archive Layout

```text
wiki/environment/
  current.json                        # environment_archive_pointer.v1：compile 只读此指针
  <YYYY-MM>/archive.sqlite3           # SQLite 行列归档（event/series/set/pick/ban + metric_* + signal_brawler 表）
  pickrate.sqlite3                    # brawlstar.environment_signal_pickrate.v1（Legendary+ 滚动快照，行列表）
  index.md                            # 归档索引与 provenance 表格
```

- 归档存储为单文件 SQLite（标准库 `sqlite3`，可迁移、外部应用可 SQL 查询）；脚本读取时展开为结构数据（`_environment_sqlite.py` 的 `load_profile` / `load_signal` / `load_pickrate`，同样接受 `.json` 路径）。需要人类可读/审计导出时用 `--output` 生成 JSON。

- 归档是持久知识库层（git 跟踪），不在 gitignored `outputs/`；`outputs/esports/` 只保留审计报告等临时产物。
- 每次归档变更后必须同步更新 `current.json` 指针与 `index.md`，并在 `wiki/log.md` 追加记录。

## Monthly Workflow

1. **Pick layer**: run `fetch_brawlplanet_pickrate.py --tier l1` (Legendary+) and write to `wiki/environment/pickrate.sqlite3` (`--db`；`--output` 为可选 JSON 导出).
2. **Ban layer**: after the monthly finals of the month are fully played, capture each region with `capture_liquipedia_event.py`, analyze with `analyze_esports_event.py --db wiki/environment/<YYYY-MM>/archive.sqlite3`（内含逐 set 行列表），then aggregate with `aggregate_environment_signal.py --profile wiki/environment/<YYYY-MM>/archive.sqlite3 --db wiki/environment/<YYYY-MM>/archive.sqlite3` (paired pick/ban per brawler, set-level denominator). Do not aggregate an unfinished month.
3. Update `current.json` to point at the new month's signal, refresh `wiki/environment/index.md`, append `wiki/log.md`.
4. Recompile the runtime index (default `--environment-manifest wiki/environment/current.json`) so the next `decide` consumes the new evidence; `manifest.environment_provenance` records which archive snapshot was folded.
5. The archived signals also serve as a human-readable reference (meta trend, monthly pick/ban report, cross-check of patch impact).

## Rules

- The signal enters the runtime index **only through compile folding**. `decide` never queries signal files; `query_environment_evidence.py` is retired. It cannot override a mechanism constraint, cannot create fit/eligibility, and cannot generate tiers.
- `manifest.pickrate_status` records `"loaded"` when the archive pointer resolves and `"empty"` otherwise; `manifest.environment_provenance` keeps the exact pointer, archive id, windows, and sample denominators.
- Do not write tournament or ladder pick/ban rates into `wiki/entities/brawlers/`. Event entities keep event facts; brawler entities keep stable mechanisms and BP contracts.
- Do not auto-generate tiers, hard gates, map fit, slot eligibility, or matchup edges from the signal.
- Normalize all brawler names through `wiki/concepts/英雄名称归一化.md` / canonical entity names; drop and log unmatched names.
- Filter future-only brawlers (e.g., Wendy) out of the signal.
- Do not aggregate a month whose monthly finals are not fully played.
- Brawl Planet GCS filenames or bucket layout may change; keep the fetcher's file map maintainable and record the capture date in the output.
- Liquipedia access follows `esports-event-ingest.md` (MediaWiki API, gzip, one request per 2s, custom UA, revision provenance).

## Related

- `wiki/environment/index.md`
- `wiki/sources/Brawl-Planet-站点与数据接口.md`
- `scripts/fetch_brawlplanet_pickrate.py`
- `scripts/aggregate_environment_signal.py`
- `scripts/capture_liquipedia_event.py` / `scripts/analyze_esports_event.py`
- `wiki/syntheses/BP-强度层语义回归与高分选取率估计器.md`
