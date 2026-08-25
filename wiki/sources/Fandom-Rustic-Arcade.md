# Fandom 来源摘要: Rustic Arcade

## 来源信息

- 标题：Rustic Arcade
- 来源：[Rustic Arcade | Brawl Stars Wiki | Fandom](https://brawlstars.fandom.com/wiki/Rustic_Arcade)
- 抓取日期：2026-08-21（revid 217096，2026-08-19T18:58:05Z）
- 类型：地图来源 / Gem Grab 地图页 / 社区攻略来源
- 上游 raw：[[../../raw/sources/fandom/maps/rustic-arcade-2026-08-21.md]]
- 关联地图实体：[[entities/maps/Rustic Arcade|Rustic Arcade]]
- 背景：Season 47 索引（2026-08-12）标记的"待 ingest 缺口"；本页与 raw/entity 一并补齐，S47/S48 均为 Gem Grab 池内图。

## 范围

本页覆盖 Fandom `Rustic Arcade` 地图页中的：

- 模式与环境：`Gem Grab`，`Arcade`（2026-02-25 起）。
- 障碍概况：Infobox `Block2=12`、`Barrel=4`、`Breakable=2`、`Bush=50`、`Lake=2`、`LaunchPad=2`、`IndestructibleWall=18`。
- Layout：中央六边形墙区（墙朝中心、草贴外墙，墙草与宝石矿之间留空）；靠出生点六处带草 enclave + 两个跳板（Launch Pad）把英雄送到中心；对角对称。
- Tips：高展开中距离英雄控中/封路（Pam/Emz/Frank/Poco 示例）；短手与纯投掷在开阔空间挣扎；长手单发射手护 carrier / 破六面墙扩线；Tara/Bo/Griff/Carl 可在中上墙后激进并夹击角草撤退。
- History：2026-08-20 与 2026-07-16 均进入 Ranked（地图页编号 "Season 30/29"，对应本库 Season 48/47）；2026-02 ~ 03 与 2024 早期（"Season 1/2"）也曾作为 Ranked Gem Grab 图。

## 可用范围

- `usable_for`:
  - `stable_map_structure`
  - `gem_grab_mine_and_carrier_factors`
  - `launch_pad_routes`
  - `wall_break_extends_sightline_candidates`
  - `thrower_and_short_range_false_positive_filter`
  - `ranked_or_event_history_reference`
- `not_usable_for`:
  - 当前版本强势英雄 tier。
  - ban 优先级或一选优先级。
  - 地图图片级坐标校验。
  - 英雄当前数值、构筑强度或补丁后胜率。

## BP 建模要点

- 中央六边形墙 + 贴墙草是核心控制结构：高展开、穿墙/越墙、范围压制的机制候选；同时两湖（`Lake=2`）与两跳板会改变接近路线的几何。
- 跳板是明确的路线因子：跳板把英雄送到中心，进入/离开中心的方式与常规地图不同，涉及 carrier 逃生与抢矿的时机成本。
- "开阔空间"提示投掷与短手挣扎，这与 Crystal Arcade 的中央 2x2 墙结构形成对照（Crystal Arcade 页 Tips 也反向引用 Rustic Arcade）；两图可互为 false-positive 对照样本。
- 破墙（六面墙）延长长手射程是明确机制候选，但破墙同样会改变中央控制结构的收益，需要双向评估。
- Fandom 英雄 Tips 只作为 map-feature 候选；具体英雄适配回到英雄实体页与当前稳定事实层，不写入本地图实体的强度结论。

## 关联页面

- [[entities/maps/Rustic Arcade|Rustic Arcade]]
- [[entities/maps/Crystal Arcade|Crystal Arcade]]（结构对照）
- [[concepts/Gem Grab|Gem Grab]]
- [[sources/Fandom-Gem-Grab|Fandom 来源摘要: Gem Grab]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
