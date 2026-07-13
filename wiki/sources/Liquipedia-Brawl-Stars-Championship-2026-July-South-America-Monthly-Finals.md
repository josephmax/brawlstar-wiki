# Liquipedia 来源摘要: Brawl Stars Championship 2026: July South America Monthly Finals

## 来源信息

- 来源：[Brawl Stars Championship 2026: July South America Monthly Finals](https://liquipedia.net/brawlstars/Brawl_Stars_Championship/2026/Season_5/South_America/Monthly_Finals)
- 页面：`Brawl Stars Championship/2026/Season 5/South America/Monthly Finals`
- 抓取 revision：`263153`（2026-07-12T01:25:18Z）
- 上游 raw：[[../../raw/sources/liquipedia/events/brawl-stars-championship-2026-season-5-south-america-monthly-finals-2026-07-13.md]]
- 许可：CC BY-SA 3.0；归属 Liquipedia contributors
- source_quality：structured_mediawiki_capture
- source_type：competitive_event_result_and_draft_observation
- 对应赛事实体：[[../entities/events/Brawl-Stars-Championship-2026-July-South-America-Monthly-Finals|Brawl Stars Championship 2026: July South America Monthly Finals]]

## 可用范围

- usable_for: event_result, played_set_count, map_mode_occurrence, observed_pick, observed_local_ban, observed_global_ban, set_result, mvp_record
- not_usable_for: causal_win_claim, automatic_tier, unconditional_counter_edge, stable_map_fit_without_vod_review, brawler_draft_order_when_map_firstpick_is_empty

## 赛事事实

- 日期：2026-07-11
- 赛区：South America
- 赛制：Single-elimination
- 冠军：RED Canids
- 亚军：LOUD
- 系列赛：7（实际进行 6，弃权 1）
- 实际进行的 sets：24

## 对阵结果

| 阶段 | 对阵 | 比分 | 状态 | MVP |
| --- | --- | --- | --- | --- |
| R1M1 | Bounty Hunters Esports vs SKCalalas | 2-3 | played | Juan Carlos |
| R1M2 | OCX Division vs LOUD | 1-3 | played | FireCrow |
| R1M3 | olimpo squad vs quieroqueque | FF | forfeit | - |
| R1M4 | glxy gaming vs RED Canids | 0-3 | played | Mohtep |
| R2M1 | SKCalalas vs LOUD | 2-3 | played | FireCrow |
| R2M2 | olimpo squad vs RED Canids | 1-3 | played | Mohtep |
| R3M1 | LOUD vs RED Canids | 0-3 | played | Mohtep |

## 选用观察（按 set）

| 英雄 | 选用 sets | set 胜场 | 选用覆盖 |
| --- | ---: | ---: | ---: |
| Griff | 7 | 2 | 29.2% |
| Lou | 6 | 4 | 25.0% |
| Ruffs | 6 | 1 | 25.0% |
| Ash | 5 | 4 | 20.8% |
| Meg | 5 | 3 | 20.8% |
| Stu | 5 | 3 | 20.8% |
| Buzz | 4 | 2 | 16.7% |
| Crow | 4 | 2 | 16.7% |
| Emz | 4 | 2 | 16.7% |
| Mortis | 4 | 2 | 16.7% |

以上是描述性样本。选用覆盖率分母为实际进行的 sets；`set 胜场` 不是个人因果胜率，也不能自动生成强度 tier。

## Local ban 观察（按 set）

| 英雄 | set 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Surge | 21 | 22 | 87.5% |
| Lumi | 9 | 10 | 37.5% |
| Meg | 9 | 10 | 37.5% |
| Max | 6 | 6 | 25.0% |
| 8-Bit | 5 | 6 | 20.8% |
| Crow | 5 | 5 | 20.8% |
| Kit | 5 | 5 | 20.8% |
| Brock | 4 | 5 | 16.7% |
| Ash | 4 | 4 | 16.7% |
| Cordelius | 4 | 4 | 16.7% |

同一 set 内双方重复提名同一英雄时，`nominations` 计 2，`set 覆盖` 只计 1。

## Global ban 观察（按实际 series）

| 英雄 | series 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Starr Nova | 5 | 5 | 83.3% |
| Damian | 4 | 4 | 66.7% |
| Max | 4 | 4 | 66.7% |
| 8-Bit | 3 | 3 | 50.0% |
| Otis | 3 | 3 | 50.0% |
| Crow | 2 | 2 | 33.3% |
| Alli | 1 | 1 | 16.7% |
| Meg | 1 | 1 | 16.7% |
| Ruffs | 1 | 1 | 16.7% |

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
