# Ranked Season 49 地图 Map Profile 总览

这页作为 `Ranked Season 49` 的赛季地图池索引。稳定地图结构、`map_feature`、地图特征对英雄能力的稳定影响和 `false_positive` 拆入单地图实体页。

治理原则见 [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]：

- 地图实体页：长期稳定，放在 `wiki/entities/maps/`。
- 本页：赛季轮换索引，只记录当前 Ranked Season 49 地图池和入口。
- 版本 / meta 审计：记录来源摘要、观察项和是否足以改写稳定 BP 字段的判断，不作为运行时叠加层。
- 英雄页 map-fit：记录英雄在具体地图特征上能做什么；若版本资料形成定性变化，直接内联改写稳定字段。

## 来源与时间语境

- 来源：Fandom Ranked 页 `https://brawlstars.fandom.com/wiki/Ranked`，"Active maps (Season 49)" 表（MediaWiki API 抓取，revid 219103，2026-09-17）
- Trial Brawlers 表锚点：`#49 | September 17, 2026 | Ash, Mortis, Pierce | Hot Zone (featured)`
- 抓取日期：2026-09-17
- 状态：`ranked_rotation_index`
- 说明：Season 49 于 2026-09-17 开始（页面原文规则：赛季于每月第三个周四开始，2026 年 9 月第三个周四即当日），featured 模式从 Season 48 的 Brawl Ball 切换为 **Hot Zone**。
- 编号说明：单地图页 History 使用另一套赛季编号（Quick Travel 2026-09-17 条目写作 "Season 31 Ranked"），与本库 Season 49 并存；本库以 Ranked 页编号为准。

## 与 Season 48 的差异

| 模式 | S48 图数 | S49 图数 | 变化 | 新增 | 移除 |
| --- | --- | --- | --- | --- | --- |
| Hot Zone (featured) | 4 | 6 | +2 | In the Liminal, Quick Travel | 无 |
| Gem Grab | 6 | 4 | −2（失去 featured，本轮缩池） | — | Crystal Arcade, Rustic Arcade |
| Heist | 6 | 4 | −2 | — | Pit Stop, Safe(r) Zone |
| Brawl Ball | 6 | 4 | −2（失去 featured） | — | Beach Ball, Spiraling Out |
| Bounty | 4 | 4 | 0 | — | — |
| Knockout | 4 | 4 | 0 | — | — |

- 总图数：30 → 26。
- 两张新增图（In the Liminal、Quick Travel）均为 Hot Zone，随 featured 机制进入池内；Quick Travel 为回归图（曾入本库编号 S21/S26 对应期），In the Liminal 同为回归图。
- `Beach Ball`、`Spiraling Out` 完成一个赛季生命周期：S48 随 featured 入池、S49 随 featured 切换出池。
- Trial Brawlers 锚点变化：`Trunk, Willow, Kaze` → `Ash, Mortis, Pierce`。

## Hot Zone（featured）

- [[entities/maps/Dueling Beetles|Dueling Beetles]]
- [[entities/maps/In the Liminal|In the Liminal]]（S49 新增，`layout_coverage_gap`）
- [[entities/maps/Open Business|Open Business]]
- [[entities/maps/Quick Travel|Quick Travel]]（S49 新增）
- [[entities/maps/Parallel Plays|Parallel Plays]]
- [[entities/maps/Ring of Fire|Ring of Fire]]

## Gem Grab

- [[entities/maps/Double Swoosh|Double Swoosh]]
- [[entities/maps/Gem Fort|Gem Fort]]
- [[entities/maps/Hard Rock Mine|Hard Rock Mine]]
- [[entities/maps/Undermine|Undermine]]

## Heist

- [[entities/maps/Bridge Too Far|Bridge Too Far]]
- [[entities/maps/Hot Potato|Hot Potato]]
- [[entities/maps/Kaboom Canyon|Kaboom Canyon]]
- [[entities/maps/Safe Zone|Safe Zone]]

## Bounty

- [[entities/maps/Dry Season|Dry Season]]
- [[entities/maps/Hideout|Hideout]]
- [[entities/maps/Layer Cake|Layer Cake]]
- [[entities/maps/Shooting Star|Shooting Star]]

## Brawl Ball

- [[entities/maps/Center Stage|Center Stage]]
- [[entities/maps/Pinball Dreams|Pinball Dreams]]
- [[entities/maps/Sneaky Fields|Sneaky Fields]]
- [[entities/maps/Triple Dribble|Triple Dribble]]

## Knockout

- [[entities/maps/Belle's Rock|Belle's Rock]]
- [[entities/maps/Flaring Phoenix|Flaring Phoenix]]
- [[entities/maps/New Horizons|New Horizons]]
- [[entities/maps/Out in the Open|Out in the Open]]

## 待 ingest 缺口

- `In the Liminal`：源页面 Layout/Tips 为空，实体页已按可证结构建模并标注 `layout_coverage_gap`；布局级证据待补，此前 BP 消费仅限"扫草/探草保底价值"。
- 其余 25 张池内图均有 `raw/sources/fandom/maps/` 覆盖、source 摘要和地图实体页。
- 移出池的 6 张图（Crystal Arcade、Rustic Arcade、Pit Stop、Safe(r) Zone、Beach Ball、Spiraling Out）实体页保留为稳定结构知识，仅离开当前赛季索引。

## BP 查询用法

```text
当前 Ranked BP 问题
-> 读 BP DSL
-> 读本页确定地图是否在 Season 49 池内
-> 进入对应地图实体页读取稳定 map_profile
-> 再读相关英雄页；若已有 runtime_bp_index，则读取编译产物
```

## 关联页面

- [[syntheses/Ranked-Season-48-地图Map-Profile总览|Ranked Season 48 地图 Map Profile 总览]]（已过期，保留作历史索引）
- [[syntheses/Ranked-Season-47-地图Map-Profile总览|Ranked Season 47 地图 Map Profile 总览]]（已过期，保留作历史索引）
- [[sources/Fandom-Ranked-Season-49-Map-Pages|Fandom 来源摘要: Ranked Season 49 地图池]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
