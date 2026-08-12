# Liquipedia 来源摘要: Brawl Stars Championship 2026: July East Asia Monthly Finals

## 来源信息

- 来源：[Brawl Stars Championship 2026: July East Asia Monthly Finals](https://liquipedia.net/brawlstars/Brawl_Stars_Championship/2026/Season_5/East_Asia/Monthly_Finals)
- 页面：`Brawl Stars Championship/2026/Season 5/East Asia/Monthly Finals`
- 抓取 revision：`264095`（2026-07-18T17:11:13Z）
- 上游 raw：[[../../raw/sources/liquipedia/events/brawl-stars-championship-2026-season-5-east-asia-monthly-finals-2026-07-21.md]]
- 许可：CC BY-SA 3.0；归属 Liquipedia contributors
- source_quality：structured_mediawiki_capture
- source_type：competitive_event_result_and_draft_observation
- 对应赛事实体：[[../entities/events/Brawl-Stars-Championship-2026-July-East-Asia-Monthly-Finals|Brawl Stars Championship 2026: July East Asia Monthly Finals]]

## 可用范围

- usable_for: event_result, played_set_count, map_mode_occurrence, observed_pick, observed_local_ban, observed_global_ban, set_result, mvp_record
- not_usable_for: causal_win_claim, automatic_tier, unconditional_counter_edge, stable_map_fit_without_vod_review, brawler_draft_order_when_map_firstpick_is_empty

## 赛事事实

- 日期：2026-07-18
- 赛区：East Asia
- 赛制：Single-elimination
- 冠军：ZETA DIVISION
- 亚军：Crazy Raccoon
- 系列赛：7（实际进行 7，弃权 0）
- 实际进行的 sets：26

## 对阵结果

| 阶段 | 对阵 | 比分 | 状态 | MVP |
| --- | --- | --- | --- | --- |
| R1M1 | ZETA DIVISION vs T5S | 3-0 | played | Sitetampo |
| R1M2 | AXIS e-sports vs REJECT | 1-3 | played | Levi |
| R1M3 | Rival Esports vs Siesta | 3-0 | played | Ryohei |
| R1M4 | SKCalalas EA vs Crazy Raccoon | 1-3 | played | Tensai |
| R2M1 | ZETA DIVISION vs REJECT | 3-1 | played | Sitetampo |
| R2M2 | Rival Esports vs Crazy Raccoon | 1-3 | played | Tensai |
| R3M1 | ZETA DIVISION vs Crazy Raccoon | 3-1 | played | Sitetampo |

## 选用观察（按 set）

| 英雄 | 选用 sets | set 胜场 | 选用覆盖 |
| --- | ---: | ---: | ---: |
| Max | 9 | 5 | 34.6% |
| Pearl | 8 | 3 | 30.8% |
| Brock | 6 | 5 | 23.1% |
| Meg | 6 | 5 | 23.1% |
| Griff | 6 | 4 | 23.1% |
| Shade | 6 | 4 | 23.1% |
| Pierce | 6 | 3 | 23.1% |
| Rico | 6 | 1 | 23.1% |
| Mortis | 5 | 3 | 19.2% |
| Belle | 5 | 2 | 19.2% |

以上是描述性样本。选用覆盖率分母为实际进行的 sets；`set 胜场` 不是个人因果胜率，也不能自动生成强度 tier。

## Local ban 观察（按 set）

| 英雄 | set 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Starr Nova | 13 | 13 | 50.0% |
| 8-Bit | 12 | 12 | 46.2% |
| Griff | 10 | 10 | 38.5% |
| Surge | 10 | 10 | 38.5% |
| Crow | 9 | 9 | 34.6% |
| Stu | 6 | 9 | 23.1% |
| Max | 5 | 7 | 19.2% |
| Cordelius | 5 | 5 | 19.2% |
| Damian | 5 | 5 | 19.2% |
| Lou | 4 | 5 | 15.4% |

同一 set 内双方重复提名同一英雄时，`nominations` 计 2，`set 覆盖` 只计 1。

## Global ban 观察（按实际 series）

| 英雄 | series 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Damian | 5 | 5 | 71.4% |
| Surge | 4 | 4 | 57.1% |
| 8-Bit | 3 | 3 | 42.9% |
| Lumi | 2 | 2 | 28.6% |
| Max | 2 | 2 | 28.6% |
| Meg | 2 | 2 | 28.6% |
| Rico | 2 | 2 | 28.6% |
| Starr Nova | 2 | 2 | 28.6% |
| Stu | 2 | 2 | 28.6% |
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
