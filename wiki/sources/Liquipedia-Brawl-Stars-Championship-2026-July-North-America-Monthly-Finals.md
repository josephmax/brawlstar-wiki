# Liquipedia 来源摘要: Brawl Stars Championship 2026: July North America Monthly Finals

## 来源信息

- 来源：[Brawl Stars Championship 2026: July North America Monthly Finals](https://liquipedia.net/brawlstars/Brawl_Stars_Championship/2026/Season_5/North_America/Monthly_Finals)
- 页面：`Brawl Stars Championship/2026/Season 5/North America/Monthly Finals`
- 抓取 revision：`264554`（2026-07-20T21:09:11Z）
- 上游 raw：[[../../raw/sources/liquipedia/events/brawl-stars-championship-2026-season-5-north-america-monthly-finals-2026-07-21.md]]
- 许可：CC BY-SA 3.0；归属 Liquipedia contributors
- source_quality：structured_mediawiki_capture
- source_type：competitive_event_result_and_draft_observation
- 对应赛事实体：[[../entities/events/Brawl-Stars-Championship-2026-July-North-America-Monthly-Finals|Brawl Stars Championship 2026: July North America Monthly Finals]]

## 可用范围

- usable_for: event_result, played_set_count, map_mode_occurrence, observed_pick, observed_local_ban, observed_global_ban, set_result, mvp_record
- not_usable_for: causal_win_claim, automatic_tier, unconditional_counter_edge, stable_map_fit_without_vod_review, brawler_draft_order_when_map_firstpick_is_empty

## 赛事事实

- 日期：2026-07-19
- 赛区：North America
- 赛制：Single-elimination
- 冠军：Team Elektros
- 亚军：Tribe
- 系列赛：7（实际进行 7，弃权 0）
- 实际进行的 sets：24

## 对阵结果

| 阶段 | 对阵 | 比分 | 状态 | MVP |
| --- | --- | --- | --- | --- |
| R1M1 | Tribe vs Momo | 3-0 | played | Lxffy |
| R1M2 | F/A Homeless vs Vic Day | 3-1 | played | Rafiki |
| R1M3 | Team Elektros vs David's Aura | 3-0 | played | Memen |
| R1M4 | Vatic Esports vs Legacy Esports | 3-0 | played | Duckie |
| R2M1 | Tribe vs F/A Homeless | 3-0 | played | Diegogamer |
| R2M2 | Team Elektros vs Vatic | 3-2 | played | Duckie |
| R3M1 | Tribe vs Team Elektros | 0-3 | played | Snoiy |

## 选用观察（按 set）

| 英雄 | 选用 sets | set 胜场 | 选用覆盖 |
| --- | ---: | ---: | ---: |
| Ash | 8 | 3 | 33.3% |
| Stu | 6 | 6 | 25.0% |
| Griff | 6 | 4 | 25.0% |
| Lou | 5 | 3 | 20.8% |
| Pearl | 5 | 3 | 20.8% |
| Kaze | 5 | 1 | 20.8% |
| Gray | 4 | 4 | 16.7% |
| Leon | 4 | 3 | 16.7% |
| Brock | 4 | 2 | 16.7% |
| Charlie | 4 | 2 | 16.7% |

以上是描述性样本。选用覆盖率分母为实际进行的 sets；`set 胜场` 不是个人因果胜率，也不能自动生成强度 tier。

## Local ban 观察（按 set）

| 英雄 | set 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| 8-Bit | 13 | 13 | 54.2% |
| Surge | 12 | 13 | 50.0% |
| Ruffs | 8 | 10 | 33.3% |
| Starr Nova | 7 | 7 | 29.2% |
| Crow | 6 | 8 | 25.0% |
| Brock | 6 | 7 | 25.0% |
| Lou | 6 | 7 | 25.0% |
| Meeple | 6 | 6 | 25.0% |
| Stu | 5 | 5 | 20.8% |
| Emz | 4 | 5 | 16.7% |

同一 set 内双方重复提名同一英雄时，`nominations` 计 2，`set 覆盖` 只计 1。

## Global ban 观察（按实际 series）

| 英雄 | series 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Lumi | 4 | 4 | 57.1% |
| Max | 4 | 4 | 57.1% |
| Starr Nova | 4 | 4 | 57.1% |
| Crow | 3 | 3 | 42.9% |
| Surge | 3 | 3 | 42.9% |
| 8-Bit | 2 | 2 | 28.6% |
| Griff | 2 | 2 | 28.6% |
| Lou | 2 | 2 | 28.6% |
| Damian | 1 | 1 | 14.3% |
| Kit | 1 | 1 | 14.3% |

弃权 series 的页面字段保留在 raw，但不进入以上 global-ban 实战聚合。

## 语义边界

- 一次 series 为双方一次交锋；本页赛制是先赢 3 个 set 的 Bo5 sets。
- 每个 set 固定一个地图 / 模式，并以局内小局比分决定 set 胜负。
- `Match.t1b* / t2b*` 是 series 级 global bans；`Map.t1b* / t2b*` 是 set 级 local ban nominations。
- `MapVeto.firstpick` 只表示地图 veto 的先选方，不是英雄 draft first pick。
- `winner=skip` 与弃权对阵不进入 played-set 分母。

## 关联页面

- [[../index|Wiki Index]]
- [[../concepts/英雄名称归一化|英雄名称归一化]]
