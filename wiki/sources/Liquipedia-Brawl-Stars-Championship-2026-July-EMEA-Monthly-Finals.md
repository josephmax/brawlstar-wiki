# Liquipedia 来源摘要: Brawl Stars Championship 2026: July EMEA Monthly Finals

## 来源信息

- 来源：[Brawl Stars Championship 2026: July EMEA Monthly Finals](https://liquipedia.net/brawlstars/Brawl_Stars_Championship/2026/Season_5/EMEA/Monthly_Finals)
- 页面：`Brawl Stars Championship/2026/Season 5/EMEA/Monthly Finals`
- 抓取 revision：`263360`（2026-07-13T04:14:39Z）
- 上游 raw：[[../../raw/sources/liquipedia/events/brawl-stars-championship-2026-season-5-emea-monthly-finals-2026-07-13.md]]
- 许可：CC BY-SA 3.0；归属 Liquipedia contributors
- source_quality：structured_mediawiki_capture
- source_type：competitive_event_result_and_draft_observation
- 对应赛事实体：[[../entities/events/Brawl-Stars-Championship-2026-July-EMEA-Monthly-Finals|Brawl Stars Championship 2026: July EMEA Monthly Finals]]

## 可用范围

- usable_for: event_result, played_set_count, map_mode_occurrence, observed_pick, observed_local_ban, observed_global_ban, set_result, mvp_record
- not_usable_for: causal_win_claim, automatic_tier, unconditional_counter_edge, stable_map_fit_without_vod_review, brawler_draft_order_when_map_firstpick_is_empty

## 赛事事实

- 日期：2026-07-12
- 赛区：EMEA
- 赛制：Single-elimination
- 冠军：FUT Esports
- 亚军：NOVO Esports
- 系列赛：7（实际进行 7，弃权 0）
- 实际进行的 sets：24

## 对阵结果

| 阶段 | 对阵 | 比分 | 状态 | MVP |
| --- | --- | --- | --- | --- |
| R1M1 | HMBLE vs FUT Esports Academy | 3-0 | played | Lukii |
| R1M2 | Kozaki vs FUT Esports | 0-3 | played | Angelboy |
| R1M3 | NOVO Esports vs Team Heretics | 3-0 | played | MeOw |
| R1M4 | BIG vs Totem | 0-3 | played | Joker |
| R2M1 | HMBLE vs FUT Esports | 0-3 | played | Angelboy |
| R2M2 | NOVO Esports vs Totem | 3-2 | played | MeOw |
| R3M1 | FUT Esports vs NOVO Esports | 3-1 | played | Angelboy |

## 选用观察（按 set）

| 英雄 | 选用 sets | set 胜场 | 选用覆盖 |
| --- | ---: | ---: | ---: |
| Meeple | 9 | 7 | 37.5% |
| Max | 8 | 4 | 33.3% |
| Lumi | 7 | 4 | 29.2% |
| Brock | 6 | 4 | 25.0% |
| Edgar | 6 | 3 | 25.0% |
| Pearl | 6 | 2 | 25.0% |
| Ruffs | 5 | 4 | 20.8% |
| Damian | 5 | 3 | 20.8% |
| Lola | 5 | 3 | 20.8% |
| Charlie | 4 | 4 | 16.7% |

以上是描述性样本。选用覆盖率分母为实际进行的 sets；`set 胜场` 不是个人因果胜率，也不能自动生成强度 tier。

## Local ban 观察（按 set）

| 英雄 | set 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Surge | 17 | 17 | 70.8% |
| 8-Bit | 16 | 17 | 66.7% |
| Starr Nova | 10 | 10 | 41.7% |
| Crow | 8 | 8 | 33.3% |
| Glowy | 7 | 7 | 29.2% |
| Kit | 7 | 7 | 29.2% |
| Lumi | 6 | 6 | 25.0% |
| Ruffs | 5 | 5 | 20.8% |
| Gene | 4 | 5 | 16.7% |
| Lou | 4 | 5 | 16.7% |

同一 set 内双方重复提名同一英雄时，`nominations` 计 2，`set 覆盖` 只计 1。

## Global ban 观察（按实际 series）

| 英雄 | series 覆盖 | nominations | 覆盖率 |
| --- | ---: | ---: | ---: |
| Griff | 5 | 5 | 71.4% |
| Damian | 4 | 4 | 57.1% |
| Meg | 4 | 4 | 57.1% |
| Starr Nova | 4 | 4 | 57.1% |
| Max | 2 | 2 | 28.6% |
| Ruffs | 2 | 2 | 28.6% |
| 8-Bit | 1 | 1 | 14.3% |
| Berry | 1 | 1 | 14.3% |
| Edgar | 1 | 1 | 14.3% |
| Leon | 1 | 1 | 14.3% |

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
