# Ranked Season 47 地图 Map Profile 总览

> **已过期**：当前 Ranked 赛季为 Season 48（2026-08-20 起，featured = Brawl Ball）。本页保留作历史索引，当前地图池见 [[syntheses/Ranked-Season-48-地图Map-Profile总览|Ranked Season 48 地图 Map Profile 总览]]。

这页作为 `Ranked Season 47` 的赛季地图池索引。稳定地图结构、`map_feature`、地图特征对英雄能力的稳定影响和 `false_positive` 拆入单地图实体页。

治理原则见 [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]：

- 地图实体页：长期稳定，放在 `wiki/entities/maps/`。
- 本页：赛季轮换索引，只记录当前 Ranked Season 47 地图池和入口。
- 版本 / meta 审计：记录来源摘要、观察项和是否足以改写稳定 BP 字段的判断，不作为运行时叠加层。
- 英雄页 map-fit：记录英雄在具体地图特征上能做什么；若版本资料形成定性变化，直接内联改写稳定字段。

## 来源与时间语境

- 来源：Fandom Ranked 页 `https://brawlstars.fandom.com/wiki/Ranked`，"Active maps (Season 47)" 表（浏览器直读，2026-08-12）
- Trial Brawlers 表锚点：`#47 | July 16, 2026 | Berry, Tara, Meg | Gem Grab (featured)`；`#48 | August 20, 2026 | Trunk, Willow, Kaze | Brawl Ball (featured)`
- 抓取日期：2026-08-12
- 状态：`ranked_rotation_index`
- 说明：Featured 模式从 Season 46 的 Heist 切换为 Season 47 的 Gem Grab。Featured 机制不是"从别的模式抢图"，而是 featured 模式在原有基数上额外增加图；因此 Gem Grab 从 Season 46 的 4 张扩到 6 张，其余模式图数不变。

## 与 Season 46 的差异

| 模式 | S46 图数 | S47 图数 | 变化 | 新增 | 移除 |
| --- | --- | --- | --- | --- | --- |
| Gem Grab (featured) | 4 | 6 | +2 | Crystal Arcade, Rustic Arcade | 无 |
| Heist | 6 | 6 | 0 | — | — |
| Bounty | 4 | 4 | 0 | — | — |
| Brawl Ball | 4 | 4 | 0 | — | — |
| Hot Zone | 4 | 4 | 0 | — | — |
| Knockout | 4 | 4 | 0 | — | — |

- 总图数：26 → 28。
- Heist 在 S46 做 featured 时已有 6 张，S47 降回常规仍保持 6 张，无图被移除。
- Season 46 的 4 张 Gem Grab 图（Double Swoosh / Gem Fort / Hard Rock Mine / Undermine）全部保留。

## Gem Grab（featured）

- [[entities/maps/Crystal Arcade|Crystal Arcade]]（S47 新增）
- [[entities/maps/Double Swoosh|Double Swoosh]]
- [[entities/maps/Gem Fort|Gem Fort]]
- [[entities/maps/Hard Rock Mine|Hard Rock Mine]]
- Rustic Arcade（S47 新增；**缺实体页**，Fandom URL `https://brawlstars.fandom.com/wiki/Rustic_Arcade`，待 ingest）
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

## Brawl Ball

- [[entities/maps/Center Stage|Center Stage]]
- [[entities/maps/Pinball Dreams|Pinball Dreams]]
- [[entities/maps/Sneaky Fields|Sneaky Fields]]
- [[entities/maps/Triple Dribble|Triple Dribble]]

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

- ~~`Rustic Arcade`~~：Season 47 Gem Grab featured 新增图，当时仓库尚无 raw capture、source 摘要或地图实体页。已于 2026-08-21（Season 48 落盘）补齐：`raw/sources/fandom/maps/rustic-arcade-2026-08-21.md`、[[sources/Fandom-Rustic-Arcade|Fandom 来源摘要: Rustic Arcade]]、[[entities/maps/Rustic Arcade|Rustic Arcade]]（`bp_map_profile_v2`）。S48 中仍为 Gem Grab 池内图。

## BP 查询用法

```text
历史赛季（S47）地图池查询
-> 读本页确认某图曾在 Season 47 池内
-> 当前赛季 BP 请使用 Season 48 索引与对应地图实体页
```

## 关联页面

- [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]（已过期，保留作历史索引）
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
