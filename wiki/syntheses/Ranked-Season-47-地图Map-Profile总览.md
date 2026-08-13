# Ranked Season 47 地图 Map Profile 总览

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

- `Rustic Arcade`：Season 47 Gem Grab featured 新增图，仓库尚无 `raw/sources/fandom/maps/` raw capture、source 摘要或地图实体页。Fandom 页有效（`https://brawlstars.fandom.com/wiki/Rustic_Arcade`，地图图 `Rustic_Arcade-Map.png` revision `20260225223748`）。需要按正常地图 ingest 流程补齐后才能进入 BP 稳定层。

## BP 查询用法

```text
当前 Ranked BP 问题
-> 读 BP DSL
-> 读本页确定地图是否在 Season 47 池内
-> 进入对应地图实体页读取稳定 map_profile
-> 再读相关英雄页；若已有 runtime_bp_index，则读取编译产物
```

## 关联页面

- [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]（已过期，保留作历史索引）
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
