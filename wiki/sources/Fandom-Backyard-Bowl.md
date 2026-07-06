# Fandom 来源摘要: Backyard Bowl

## 来源信息

- 标题：Backyard Bowl
- 来源：[Backyard Bowl | Brawl Stars Wiki | Fandom](https://brawlstars.fandom.com/wiki/Backyard_Bowl)
- 抓取日期：2026-07-06
- 类型：地图来源 / Brawl Ball 地图页 / 社区攻略来源
- 上游 raw：[[../../raw/sources/fandom/maps/backyard-bowl-2026-07-06.md]]
- 关联地图实体：[[entities/maps/Backyard Bowl|Backyard Bowl]]

## 范围

本页覆盖 Fandom `Backyard Bowl` 地图页中的：

- 模式与环境：`Brawl Ball`，`Grassfield`。
- 障碍概况：箱子、桶、栅栏、草丛、不可破墙等 Infobox 数量。
- Layout：开阔结构、小草块、球门前长条障碍、右侧 L 形草、中心入口附近墙草簇、可被破墙扩大的球门开口、对角对称。
- Tips：长手 / 宽弹道收益、投掷劣势、有限中场墙位、破墙得分价值、门前 / 边路封锁窗口。
- History：加入、改图、环境变化和曾经进入 Power League / Ranked / 赛事的历史。

## 可用范围

- `usable_for`:
  - `stable_map_structure`
  - `brawl_ball_goal_structure`
  - `wall_break_score_window_candidates`
  - `open_lane_and_small_bush_map_factors`
  - `thrower_false_positive_filter`
  - `ranked_or_event_history_reference`
- `not_usable_for`:
  - 当前版本强势英雄 tier。
  - ban 优先级或一选优先级。
  - 地图图片级坐标校验。
  - 英雄当前数值、构筑强度或补丁后胜率。

## BP 建模要点

- `Backyard Bowl` 是开阔 Brawl Ball 图，长线和宽弹道更容易在中远距离控制球权；投掷只有极少数中场墙位可用，不能因“Brawl Ball 有墙”而默认升值。
- 球门前长条障碍让默认进球窗口受限；破墙可以把球门开口从窄门扩成更宽的射门/推进窗口，但开墙后也会让双方进入更纯粹的开阔长线对抗。
- 小草块与中心入口墙草簇提供局部伏击、拿球和短暂充能点，但不构成连续安全草路；短手或中程必须说明如何穿过长线火力。
- Fandom 的英雄 Tips 可以作为 map-feature 候选，但具体英雄适配仍需回到英雄实体页与当前 strength profile，不写入本地图实体的稳定结论。

## 辅助来源

- [[sources/Fandom-Brock|Fandom 来源摘要: Brock]]：Brock 页面明确把 Backyard Bowl 作为 Rocket Fuel 开关键墙示例，支持“破门/破掩体是稳定地图因子”。
- [[sources/Fandom-Otis|Fandom 来源摘要: Otis]]：Otis 页面把 Backyard Bowl 作为 Brawl Ball 门前 choke / 防冲门控制示例。
- [[entities/brawlers/Bea|Bea]]：已有 `brawl_ball_super_slow_and_supercharge_hold` map hook 引用 Backyard Bowl，支持“开阔球路 + 长单发威胁 + slow 防守”的英雄侧消费方式。

## 关联页面

- [[entities/maps/Backyard Bowl|Backyard Bowl]]
- [[concepts/Brawl Ball|Brawl Ball]]
- [[sources/Fandom-Brawl-Ball|Fandom 来源摘要: Brawl Ball]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
