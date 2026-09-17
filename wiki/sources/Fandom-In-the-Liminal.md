# Fandom 来源摘要: In the Liminal

## 来源信息

- 标题：In the Liminal
- 来源：[In the Liminal | Brawl Stars Wiki | Fandom](https://brawlstars.fandom.com/wiki/In_the_Liminal)
- 抓取日期：2026-09-17（revid 213034，2026-05-20T15:13:56Z）
- 类型：地图来源 / Hot Zone 地图页 / 社区攻略来源
- 上游 raw：[[../../raw/sources/fandom/maps/in-the-liminal-2026-09-17.md]]
- 关联地图实体：[[entities/maps/In the Liminal|In the Liminal]]

## 范围

本页覆盖 Fandom `In the Liminal` 地图页中的：

- 模式与环境：`Hot Zone`，`Hub`（2026-02-25 起）。
- 障碍概况：Infobox `Block1=38`、`Box=12`、`Fence=6`、`Bush=112`。
- Layout：**源页面该章节为空**，无布局描述。
- Tips：**源页面该章节为空**。
- History：2025-04-23 加入；环境 Arcade → Enchanted Forest（2025-06-24）→ Circus（2025-10-28）→ Starr Force（2025-12-16）→ Hub（2026-02-25）；曾入 Ranked 的记录为地图页编号 Season 21 / Season 26（本库编号体系不同）；2026-09-17 起进入本库 Season 49 池（证据为 Ranked 页 Active maps 表）。

## 可用范围

- `usable_for`:
  - `stable_map_structure`（仅 infobox 数值层面：墙体/木箱/围栏/草丛数量与比例）
  - `hot_zone_mode_binding`
  - `ranked_or_event_history_reference`
- `not_usable_for`:
  - 任何路线、草簇连接、掩体口袋、区域相邻关系级结论（源页面无 Layout/Tips 证据，禁止脑补）。
  - 当前版本强势英雄 tier、ban 优先级。
  - 英雄当前数值或补丁后胜率。

## BP 建模要点

- 本图是"infobox 可证、布局不可证"的典型：实体页只建模tile 计数能支撑的事实（草丛 112 对 38 墙体的比例偏高，属于草丛占比显著的结构信号），并在 `map_bp_factors` 与 false_positive 中显式标注"路线级结论缺源、待补抓"。
- Bush=112 属于全池偏高的草丛量级（对比 Ring of Fire / Dueling Beetles 等同模式图），只能得出"草丛资源显著"这一方向性事实，不能推出"草路连接区域"或"伏击 endpoint"。
- 2026-09-17 入池状态属于赛季索引层（Ranked Season 49 总览），不入本图稳定结构。

## 关联页面

- [[entities/maps/In the Liminal|In the Liminal]]
- [[concepts/Hot Zone|Hot Zone]]
- [[syntheses/Ranked-Season-49-地图Map-Profile总览|Ranked Season 49 地图 Map Profile 总览]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
