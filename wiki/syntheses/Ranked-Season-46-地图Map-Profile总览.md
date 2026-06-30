# Ranked Season 46 地图 Map Profile 总览

这页现在只作为 `Ranked Season 46` 的赛季地图池索引。稳定地图结构、`map_feature`、地图特征对英雄能力的稳定影响和 `false_positive` 已拆入单地图实体页。

治理原则见 [[syntheses/地图知识分层治理|地图知识分层治理]]：

- 地图实体页：长期稳定，放在 `wiki/entities/maps/`。
- 本页：赛季轮换索引，只记录当前 Ranked Season 46 地图池和入口。
- 版本 / meta 审计：记录来源摘要、观察项和是否足以改写稳定 BP 字段的判断，不作为运行时叠加层。
- 英雄页 map-fit：记录英雄在具体地图特征上能做什么；若版本资料形成定性变化，直接内联改写稳定字段。

## 来源与时间语境

- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 抓取日期：2026-06-29
- 状态：`ranked_rotation_index`
- 说明：如果 Ranked 地图池变化，只更新本页或新增新赛季索引；不要重写稳定地图实体页。

## Gem Grab

- [[entities/maps/Double Swoosh|Double Swoosh]]
- [[entities/maps/Gem Fort|Gem Fort]]
- [[entities/maps/Hard Rock Mine|Hard Rock Mine]]
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

## BP 查询用法

```text
当前 Ranked BP 问题
-> 读 BP DSL
-> 读本页确定地图是否在 Season 46 池内
-> 进入对应地图实体页读取稳定 map_profile
-> 再读相关英雄页、条件化对位边索引和地图 hook 索引
```

## 关联页面

- [[syntheses/地图知识分层治理|地图知识分层治理]]
- [[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
