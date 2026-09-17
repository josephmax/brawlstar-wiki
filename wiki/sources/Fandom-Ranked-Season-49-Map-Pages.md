# Fandom 来源摘要: Ranked Season 49 地图池

## 来源信息

- 标题：Ranked Season 49 Map Pool Extracts
- 来源：Brawl Stars Wiki / Fandom `Ranked` 页，"Active maps (Season 49)" 表 + Seasons 表 `#49` 行
- 来源 URL：https://brawlstars.fandom.com/wiki/Ranked
- 抓取日期：2026-09-17（revid 219103，2026-09-17T06:56:45Z）
- 类型：地图来源 / 排位地图池 / 社区攻略来源
- 上游 raw：[[../../raw/sources/fandom/maps/ranked-season-49-map-extracts-2026-09-17.md]]
- 前置来源：[[sources/Fandom-Ranked|Fandom 来源摘要: Ranked]]、[[sources/Fandom-Ranked-Season-48-Map-Pages|Fandom 来源摘要: Ranked Season 48 地图池]]

## 范围

本页覆盖 Season 49 完整 active map pool（6 模式 26 张图）：

- `Gem Grab`（4）：`Double Swoosh`、`Gem Fort`、`Hard Rock Mine`、`Undermine`
- `Heist`（4）：`Bridge Too Far`、`Hot Potato`、`Kaboom Canyon`、`Safe Zone`
- `Bounty`（4）：`Dry Season`、`Hideout`、`Layer Cake`、`Shooting Star`
- `Brawl Ball`（4）：`Center Stage`、`Pinball Dreams`、`Sneaky Fields`、`Triple Dribble`
- `Hot Zone`（featured，6）：`Dueling Beetles`、`In the Liminal`、`Open Business`、`Quick Travel`、`Parallel Plays`、`Ring of Fire`
- `Knockout`（4）：`Belle's Rock`、`Flaring Phoenix`、`New Horizons`、`Out in the Open`

赛季锚点：`#49 | September 17, 2026 | Ash, Mortis, Pierce | Hot Zone (featured)`。赛季节奏规则（页面原文）：Ranked 赛季于每月第三个周三结束、第三个周四开始——2026 年 9 月第三个周四即 2026-09-17，与锚点及抓取当日页面状态一致。

## S49 vs S48 变化

- 总图数 30 → 26（−4）；featured 模式从 Brawl Ball 切到 **Hot Zone**。
- `Hot Zone` 4 → 6（+2）：新增 `In the Liminal`、`Quick Travel`，配合 featured 机制进入池内。
- 失去 featured 的三个模式各缩 2 张：
  - `Gem Grab` 6 → 4：移出 `Crystal Arcade`、`Rustic Arcade`（与 S46→S47 Heist、S47→S48 Gem Grab 的"失去 featured 后缩池"行为一致，本轮不再整模式保留）。
  - `Heist` 6 → 4：移出 `Pit Stop`、`Safe(r) Zone`。
  - `Brawl Ball` 6 → 4：移出 `Beach Ball`、`Spiraling Out`（两图均为 S48 随 featured 入池、S49 即随 featured 切换出池，一个赛季生命周期）。
- `Bounty`、`Knockout` 图名单不变。
- Trial Brawlers 锚点变化：`Trunk, Willow, Kaze` → `Ash, Mortis, Pierce`。

## 新增图来源覆盖

- `In the Liminal`：[[sources/Fandom-In-the-Liminal|Fandom 来源摘要: In the Liminal]]（源页面稀疏：仅 infobox 数值，Layout/Tips 为空，实体页按"可证结构"建模并标注覆盖缺口）。
- `Quick Travel`：[[sources/Fandom-Quick-Travel|Fandom 来源摘要: Quick Travel]]（Layout/Tips 完整，绳网分割双区 + S 形草簇 + 弹射垫结构可建模）。

## 来源价值与使用边界

- Active maps 表只回答"某图是否在当前赛季池内"，是本库赛季编号（Season 49）的权威基准；不承载单图结构细节。
- 单地图页 History 使用另一套编号（Quick Travel 2026-09-17 条目写作 "Season 31 Ranked"），与本库编号并存；以 Ranked 页编号为准。
- 移出池的 6 张图（`Crystal Arcade`、`Rustic Arcade`、`Pit Stop`、`Safe(r) Zone`、`Beach Ball`、`Spiraling Out`）实体页保留为稳定结构知识，只是不再进入当前赛季索引。
- 不据此生成强度、ban 优先级或一选优先级。

## 关联页面

- [[syntheses/Ranked-Season-49-地图Map-Profile总览|Ranked Season 49 地图 Map Profile 总览]]
- [[syntheses/Ranked-Season-48-地图Map-Profile总览|Ranked Season 48 地图 Map Profile 总览]]（已过期）
- [[sources/Fandom-In-the-Liminal|Fandom 来源摘要: In the Liminal]]
- [[sources/Fandom-Quick-Travel|Fandom 来源摘要: Quick Travel]]
- [[sources/Fandom-Ranked|Fandom 来源摘要: Ranked]]

## 机器消费清单

`wiki/environment/ranked_pool.json` 已按本页对应 raw 的 26 张地图同步到 S49，供应用实时排位数据过滤使用；不将旧归档标为 S49 实时统计。
