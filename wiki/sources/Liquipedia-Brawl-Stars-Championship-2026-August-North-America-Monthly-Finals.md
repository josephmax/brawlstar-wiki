# Liquipedia 来源摘要: Brawl Stars Championship 2026: August North America Monthly Finals

## 来源信息

- 来源：[Brawl Stars Championship 2026: August North America Monthly Finals](https://liquipedia.net/brawlstars/Brawl_Stars_Championship/2026/Season_6/North_America/Monthly_Finals)
- 页面：`Brawl Stars Championship/2026/Season 6/North America/Monthly Finals`
- 抓取 revision：`269180`（2026-08-17T17:48:25Z）
- 上游 raw：[[../../raw/sources/liquipedia/events/brawl-stars-championship-2026-season-6-north-america-monthly-finals-2026-08-24.md]]
- 许可：CC BY-SA 3.0；归属 Liquipedia contributors
- source_quality：structured_mediawiki_capture
- source_type：competitive_event_result_and_draft_observation
- 对应赛事实体：[[../entities/events/Brawl-Stars-Championship-2026-August-North-America-Monthly-Finals|Brawl Stars Championship 2026: August North America Monthly Finals]]

## 可用范围

- usable_for: event_result, played_set_count, map_mode_occurrence, observed_pick, observed_local_ban, observed_global_ban, set_result, mvp_record
- not_usable_for: causal_win_claim, automatic_tier, unconditional_counter_edge, stable_map_fit_without_vod_review, brawler_draft_order_when_map_firstpick_is_empty

## 赛事事实

- 日期：2026-08-16
- 赛区：North America
- 赛制：Single-elimination
- 冠军：Tribe
- 亚军：Team Elektros
- 系列赛：7（实际进行 7，弃权 0）
- 实际进行的 sets：29

## 对阵结果

| 阶段 | 对阵 | 比分 | 状态 | MVP |
| --- | --- | --- | --- | --- |
| R1M1 | Team Elektros vs Utopia | 3-0 | played | Memen |
| R1M2 | Vatic vs Legacy Esports | 3-2 | played | Duckie |
| R1M3 | Tribe vs Momo | 3-1 | played | RBM |
| R1M4 | KDS Esports vs F/A Homeless | 3-2 | played | sans |
| R2M1 | team elektros vs vatic | 3-1 | played | Duckie |
| R2M2 | Tribe vs KDS Esports | 3-1 | played | Lxffy |
| R3M1 | Team Elektros vs Tribe | 1-3 | played | Lxffy |

## 选用观察（按 set）

| 英雄 | 选用 sets | set 胜场 | 选用覆盖 |
| --- | ---: | ---: | ---: |
| Meeple | 9 | 5 | 31.0% |
| Griff | 8 | 4 | 27.6% |
| Meg | 7 | 2 | 24.1% |
| Mina | 6 | 3 | 20.7% |
| Sirius | 6 | 3 | 20.7% |
| Ash | 6 | 2 | 20.7% |
| Surge | 5 | 3 | 17.2% |
| Rico | 5 | 2 | 17.2% |
| Byron | 4 | 4 | 13.8% |
| Edgar | 4 | 4 | 13.8% |

以上是描述性样本。选用覆盖率分母为实际进行的 sets；`set 胜场` 不是个人因果胜率，也不能自动生成强度 tier。

## Local ban 观察（按 set）

| 英雄 | set 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| 8-Bit | 14 | 14 | 48.3% |
| Stu | 9 | 9 | 31.0% |
| Emz | 8 | 9 | 27.6% |
| Griff | 8 | 9 | 27.6% |
| Kit | 8 | 9 | 27.6% |
| Lou | 8 | 9 | 27.6% |
| Brock | 7 | 9 | 24.1% |
| Meeple | 7 | 7 | 24.1% |
| Shade | 6 | 6 | 20.7% |
| Surge | 6 | 6 | 20.7% |

同一 set 内双方重复提名同一英雄时，`nominations` 计 2，`set 覆盖` 只计 1。

## Global ban 观察（按实际 series）

| 英雄 | series 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Max | 5 | 5 | 71.4% |
| Lumi | 4 | 4 | 57.1% |
| Ash | 3 | 3 | 42.9% |
| Bolt | 3 | 3 | 42.9% |
| Starr Nova | 3 | 3 | 42.9% |
| 8-Bit | 2 | 2 | 28.6% |
| Damian | 2 | 2 | 28.6% |
| Meg | 2 | 2 | 28.6% |
| Berry | 1 | 1 | 14.3% |
| Crow | 1 | 1 | 14.3% |

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
