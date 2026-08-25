# Ranked Season 48 地图 Map Profile 总览

这页作为 `Ranked Season 48` 的赛季地图池索引。稳定地图结构、`map_feature`、地图特征对英雄能力的稳定影响和 `false_positive` 拆入单地图实体页。

治理原则见 [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]：

- 地图实体页：长期稳定，放在 `wiki/entities/maps/`。
- 本页：赛季轮换索引，只记录当前 Ranked Season 48 地图池和入口。
- 版本 / meta 审计：记录来源摘要、观察项和是否足以改写稳定 BP 字段的判断，不作为运行时叠加层。
- 英雄页 map-fit：记录英雄在具体地图特征上能做什么；若版本资料形成定性变化，直接内联改写稳定字段。

## 来源与时间语境

- 来源：Fandom Ranked 页 `https://brawlstars.fandom.com/wiki/Ranked`，"Active maps (Season 48)" 表（MediaWiki API 抓取，revid 217144，2026-08-21）
- Trial Brawlers 表锚点：`#48 | August 20, 2026 | Trunk, Willow, Kaze | Brawl Ball (featured)`
- 抓取日期：2026-08-21
- 状态：`ranked_rotation_index`
- 说明：Season 48 于 2026-08-20 开始，featured 模式从 Season 47 的 Gem Grab 切换为 Brawl Ball。与 Heist（S46 featured -> S47 保留 6 张）一致，Gem Grab 失去 featured 后保留其 6 张图。
- 编号说明：单地图页 History 使用另一套赛季编号（2026-08-20 条目写作 "Season 30 Ranked"），与本库 Season 48 并存；本库以 Ranked 页编号为准。

## 与 Season 47 的差异

| 模式 | S47 图数 | S48 图数 | 变化 | 新增 | 移除 |
| --- | --- | --- | --- | --- | --- |
| Brawl Ball (featured) | 4 | 6 | +2 | Beach Ball, Spiraling Out | 无 |
| Gem Grab | 6 | 6 | 0（失去 featured，图数保留） | — | — |
| Heist | 6 | 6 | 0 | — | — |
| Bounty | 4 | 4 | 0 | — | — |
| Hot Zone | 4 | 4 | 0 | — | — |
| Knockout | 4 | 4 | 0 | — | — |

- 总图数：28 → 30。
- 两张新增图（Beach Ball、Spiraling Out）均为 Brawl Ball，随 featured 机制进入池内。
- Season 47 遗留缺口 `Rustic Arcade`（Gem Grab，S47 已存在、S48 继续保留）本轮已补齐 raw/source/entity 三层。

## Brawl Ball（featured）

- [[entities/maps/Beach Ball|Beach Ball]]（S48 新增）
- [[entities/maps/Center Stage|Center Stage]]
- [[entities/maps/Pinball Dreams|Pinball Dreams]]
- [[entities/maps/Sneaky Fields|Sneaky Fields]]
- [[entities/maps/Spiraling Out|Spiraling Out]]（S48 新增）
- [[entities/maps/Triple Dribble|Triple Dribble]]

## Gem Grab

- [[entities/maps/Crystal Arcade|Crystal Arcade]]
- [[entities/maps/Double Swoosh|Double Swoosh]]
- [[entities/maps/Gem Fort|Gem Fort]]
- [[entities/maps/Hard Rock Mine|Hard Rock Mine]]
- [[entities/maps/Rustic Arcade|Rustic Arcade]]（S47 待 ingest 缺口，本轮补齐）
- [[entities/maps/Undermine|Undermine]]

## Heist

- [[entities/maps/Bridge Too Far|Bridge Too Far]]
- [[entities/maps/Hot Potato|Hot Potato]]
- [[entities/maps/Kaboom Canyon|Kaboom Canyon]]
- [[entities/maps/Pit Stop|Pit Stop]]
- [[entities/maps/Safe Zone|Safe Zone]]
- [[entities/maps/Safe(r) Zone|Safe(r) Zone]]

## Bounty

- [[entities/maps/Dry Season|Dry Season]]
- [[entities/maps/Hideout|Hideout]]
- [[entities/maps/Layer Cake|Layer Cake]]
- [[entities/maps/Shooting Star|Shooting Star]]

## Hot Zone

- [[entities/maps/Dueling Beetles|Dueling Beetles]]
- [[entities/maps/Open Business|Open Business]]
- [[entities/maps/Parallel Plays|Parallel Plays]]
- [[entities/maps/Ring of Fire|Ring of Fire]]

## Knockout

- [[entities/maps/Belle's Rock|Belle's Rock]]
- [[entities/maps/Flaring Phoenix|Flaring Phoenix]]
- [[entities/maps/New Horizons|New Horizons]]
- [[entities/maps/Out in the Open|Out in the Open]]

## 待 ingest 缺口

- 无。全部 30 张池内图均有 `raw/sources/fandom/maps/` 覆盖、source 摘要和地图实体页。

## BP 查询用法

```text
当前 Ranked BP 问题
-> 读 BP DSL
-> 读本页确定地图是否在 Season 48 池内
-> 进入对应地图实体页读取稳定 map_profile
-> 再读相关英雄页；若已有 runtime_bp_index，则读取编译产物
```

## 关联页面

- [[syntheses/Ranked-Season-47-地图Map-Profile总览|Ranked Season 47 地图 Map Profile 总览]]（已过期，保留作历史索引）
- [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]（历史索引）
- [[sources/Fandom-Ranked-Season-48-Map-Pages|Fandom 来源摘要: Ranked Season 48 地图池]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
