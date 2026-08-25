# Liquipedia 来源摘要: Brawl Stars Championship 2026: August East Asia Monthly Finals

## 来源信息

- 来源：[Brawl Stars Championship 2026: August East Asia Monthly Finals](https://liquipedia.net/brawlstars/Brawl_Stars_Championship/2026/Season_6/East_Asia/Monthly_Finals)
- 页面：`Brawl Stars Championship/2026/Season 6/East Asia/Monthly Finals`
- 抓取 revision：`269178`（2026-08-17T17:46:53Z）
- 上游 raw：[[../../raw/sources/liquipedia/events/brawl-stars-championship-2026-season-6-east-asia-monthly-finals-2026-08-24.md]]
- 许可：CC BY-SA 3.0；归属 Liquipedia contributors
- source_quality：structured_mediawiki_capture
- source_type：competitive_event_result_and_draft_observation
- 对应赛事实体：[[../entities/events/Brawl-Stars-Championship-2026-August-East-Asia-Monthly-Finals|Brawl Stars Championship 2026: August East Asia Monthly Finals]]

## 可用范围

- usable_for: event_result, played_set_count, map_mode_occurrence, observed_pick, observed_local_ban, observed_global_ban, set_result, mvp_record
- not_usable_for: causal_win_claim, automatic_tier, unconditional_counter_edge, stable_map_fit_without_vod_review, brawler_draft_order_when_map_firstpick_is_empty

## 赛事事实

- 日期：2026-08-08
- 赛区：East Asia
- 赛制：Single-elimination
- 冠军：Crazy Raccoon
- 亚军：ZETA Division
- 系列赛：7（实际进行 7，弃权 0）
- 实际进行的 sets：27

## 对阵结果

| 阶段 | 对阵 | 比分 | 状态 | MVP |
| --- | --- | --- | --- | --- |
| R1M1 | ZETA DIVISION vs F/A Zero Mercy | 3-0 | played | Sitetampo |
| R1M2 | IGNUM vs FENNEL | 0-3 | played | Achapi |
| R1M3 | Crazy Raccoon vs T5S | 3-1 | played | Tensai |
| R1M4 | SKCalalas EA vs Frenzy Esports | 2-3 | played | Toridesu |
| R2M1 | ZETA DIVISION vs FENNEL | 3-1 | played | Sitetampo |
| R2M2 | Crazy Raccoon vs Frenzy Esports | 3-1 | played | Tensai |
| R3M1 | ZETA Division vs Crazy Raccoon | 1-3 | played | Tensai |

## 选用观察（按 set）

| 英雄 | 选用 sets | set 胜场 | 选用覆盖 |
| --- | ---: | ---: | ---: |
| 8-Bit | 7 | 5 | 25.9% |
| Max | 7 | 1 | 25.9% |
| Emz | 6 | 4 | 22.2% |
| Kaze | 6 | 3 | 22.2% |
| Pierce | 6 | 1 | 22.2% |
| Meeple | 5 | 5 | 18.5% |
| Surge | 5 | 4 | 18.5% |
| Damian | 5 | 3 | 18.5% |
| Griff | 5 | 3 | 18.5% |
| Stu | 5 | 3 | 18.5% |

以上是描述性样本。选用覆盖率分母为实际进行的 sets；`set 胜场` 不是个人因果胜率，也不能自动生成强度 tier。

## Local ban 观察（按 set）

| 英雄 | set 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Starr Nova | 17 | 17 | 63.0% |
| 8-Bit | 15 | 16 | 55.6% |
| Surge | 14 | 14 | 51.9% |
| Lou | 7 | 7 | 25.9% |
| Max | 7 | 7 | 25.9% |
| Najia | 7 | 7 | 25.9% |
| Brock | 6 | 7 | 22.2% |
| Kit | 6 | 6 | 22.2% |
| Shade | 5 | 7 | 18.5% |
| Emz | 5 | 6 | 18.5% |

同一 set 内双方重复提名同一英雄时，`nominations` 计 2，`set 覆盖` 只计 1。

## Global ban 观察（按实际 series）

| 英雄 | series 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Bolt | 6 | 6 | 85.7% |
| Lumi | 4 | 4 | 57.1% |
| Rico | 3 | 3 | 42.9% |
| Starr Nova | 3 | 3 | 42.9% |
| Edgar | 2 | 2 | 28.6% |
| Max | 2 | 2 | 28.6% |
| Meg | 2 | 2 | 28.6% |
| Surge | 2 | 2 | 28.6% |
| Emz | 1 | 1 | 14.3% |
| Griff | 1 | 1 | 14.3% |

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
