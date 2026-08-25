# Fandom 来源摘要: Ranked Season 48 地图池

## 来源信息

- 标题：Ranked Season 48 Map Pool Extracts
- 来源：Brawl Stars Wiki / Fandom `Ranked` 页，"Active maps (Season 48)" 表
- 来源 URL：https://brawlstars.fandom.com/wiki/Ranked
- 抓取日期：2026-08-21（revid 217144，2026-08-21T00:23:29Z）
- 类型：地图来源 / 排位地图池 / 社区攻略来源
- 上游 raw：[[../../raw/sources/fandom/maps/ranked-season-48-map-extracts-2026-08-21.md]]
- 前置来源：[[sources/Fandom-Ranked|Fandom 来源摘要: Ranked]]、[[sources/Fandom-Ranked-Map-Source-Assessment|Fandom 来源摘要: Ranked 地图页建模价值评估]]

## 范围

本页覆盖 Season 48 完整 active map pool（6 模式 30 张图）：

- `Gem Grab`（6）：`Crystal Arcade`、`Double Swoosh`、`Gem Fort`、`Hard Rock Mine`、`Rustic Arcade`、`Undermine`
- `Heist`（6）：`Bridge Too Far`、`Hot Potato`、`Kaboom Canyon`、`Pit Stop`、`Safe Zone`、`Safe(r) Zone`
- `Bounty`（4）：`Dry Season`、`Hideout`、`Layer Cake`、`Shooting Star`
- `Brawl Ball`（featured，6）：`Beach Ball`、`Center Stage`、`Pinball Dreams`、`Sneaky Fields`、`Spiraling Out`、`Triple Dribble`
- `Hot Zone`（4）：`Dueling Beetles`、`Open Business`、`Parallel Plays`、`Ring of Fire`
- `Knockout`（4）：`Belle's Rock`、`Flaring Phoenix`、`New Horizons`、`Out in the Open`

Trial Brawlers 锚点：`#48 | August 20, 2026 | Trunk, Willow, Kaze | Brawl Ball (featured)`。

## S48 vs S47 变化

- 总图数 28 -> 30；featured 模式从 Gem Grab 切到 Brawl Ball。
- Brawl Ball +2（`Beach Ball`、`Spiraling Out`），其余模式图数不变。
- Gem Grab 失去 featured 后保留 6 张图（与 Heist S46->S47 行为一致）；`Rustic Arcade` 为 S47 已存在、S48 继续保留的图，本轮补齐其 raw/source/entity 缺口。

## 来源价值

`Ranked` 页的 Active maps 表提供当前赛季每模式的地图名单，是本库赛季编号（Season 46/47/48）的权威基准，用于赛季轮换索引；不承载单图结构细节。

单图结构与 BP 因素来自对应 Fandom 地图页，本轮为三张缺图（Beach Ball、Spiraling Out、Rustic Arcade）分别建立 raw capture 与本来源页的下游地图页。

## 使用边界

- Active maps 表只回答"某图是否在当前赛季池内"，不回答地图结构或英雄适配。
- 单地图页 History 使用另一套赛季编号（2026-08-20 的条目写作 "Season 30 Ranked"），与本库编号（Season 48）并存；本库以 Ranked 页编号为准，地图 History 仅作为"曾进入 Ranked"历史证据。
- 不据此生成强度、ban 优先级或一选优先级。

## 已沉淀结论

- [[syntheses/Ranked-Season-48-地图Map-Profile总览|Ranked Season 48 地图 Map Profile 总览]]：当前赛季地图池索引。
- `wiki/entities/maps/`：`Beach Ball`、`Spiraling Out`、`Rustic Arcade` 三张新增实体页补齐后，`bp_map_profile_v2` 覆盖全部池内地图。
- `outputs/runtime-bp-index/`：Season 48 地图池落盘后重新编译 runtime index，使新图进入可查询稳定层。

## 关联页面

- [[syntheses/Ranked-Season-48-地图Map-Profile总览|Ranked Season 48 地图 Map Profile 总览]]
- [[syntheses/Ranked-Season-47-地图Map-Profile总览|Ranked Season 47 地图 Map Profile 总览]]（已过期）
- [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]（历史索引）
- [[sources/Fandom-Ranked|Fandom 来源摘要: Ranked]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
