# Fandom 来源摘要: Beach Ball

## 来源信息

- 标题：Beach Ball
- 来源：[Beach Ball | Brawl Stars Wiki | Fandom](https://brawlstars.fandom.com/wiki/Beach_Ball)
- 抓取日期：2026-08-21（revid 217108，2026-08-19T19:02:52Z）
- 类型：地图来源 / Brawl Ball 地图页 / 社区攻略来源
- 上游 raw：[[../../raw/sources/fandom/maps/beach-ball-2026-08-21.md]]
- 关联地图实体：[[entities/maps/Beach Ball|Beach Ball]]

## 范围

本页覆盖 Fandom `Beach Ball` 地图页中的：

- 模式与环境：`Brawl Ball`，`Grassfield`（2026-04-22 起）。
- 障碍概况：Infobox `Box=42`、`Barrel=24`、`Bush=82`。
- Layout：长窄墙分布 + 大草簇；左右两侧各三组草簇与两排墙；中路两处小墙草块，近中心两大墙草簇、球置正中；球门三格开口、破墙可扩到七格；对角对称。
- Tips：中距离血量英雄泛用（Nita/Frank/Carl 示例）、短手借两侧草推进与伏击、墙体价值低且易被破、宽弹道压制草路、三路职责（重装左 / 斗士中 / 射手支援右）、Sprout 封草、投掷逼草、Squeak 减速、草内狙、高血量带球/护盾打法。
- History：2026-08-20 进入 Ranked（地图页编号 "Season 30"，对应本库 Season 48）。

## 可用范围

- `usable_for`:
  - `stable_map_structure`
  - `brawl_ball_goal_structure`（窄门开口 + 破墙扩大窗口）
  - `grass_route_and_ambush_candidates`
  - `bush_sweep_and_area_denial_factors`
  - `wall_break_score_window_candidates`
  - `ranked_or_event_history_reference`
- `not_usable_for`:
  - 当前版本强势英雄 tier。
  - ban 优先级或一选优先级。
  - 地图图片级坐标校验。
  - 英雄当前数值、构筑强度或补丁后胜率。

## BP 建模要点

- 草是主要路径资源：两侧大草簇支撑短手推进/伏击，但"草多"不等于短手自动成立——草路需要连接到球门方向并有出口，否则会被宽弹道和扫草英雄清空。
- 球门窄口（三格）使破墙成为明确得分窗口工具；但 Fandom 同时提示墙体本身价值低、易被拆，因此破墙收益与开墙后的开阔对抗要双向评估。
- 中距离高血量英雄（Nita/Frank/Carl 类）在本页被描述为同时压短手和长手，可作为"草路 + 窄口 + 开阔混合"的机制候选，不代表强度结论。
- Fandom 英雄 Tips 只作为 map-feature 候选；具体英雄适配回到英雄实体页与当前稳定事实层，不写入本地图实体的强度结论。

## 关联页面

- [[entities/maps/Beach Ball|Beach Ball]]
- [[concepts/Brawl Ball|Brawl Ball]]
- [[sources/Fandom-Brawl-Ball|Fandom 来源摘要: Brawl Ball]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
