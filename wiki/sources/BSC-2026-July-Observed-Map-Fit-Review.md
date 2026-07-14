# BSC 2026 July 三张补充地图的适配复核

## 来源信息

- 上游赛事 raw：[[../../raw/sources/liquipedia/events/brawl-stars-championship-2026-season-5-emea-monthly-finals-2026-07-13.md|EMEA Monthly Finals raw]]、[[../../raw/sources/liquipedia/events/brawl-stars-championship-2026-season-5-south-america-monthly-finals-2026-07-13.md|South America Monthly Finals raw]]
- 赛事来源摘要：[[Liquipedia-Brawl-Stars-Championship-2026-July-EMEA-Monthly-Finals|EMEA]]、[[Liquipedia-Brawl-Stars-Championship-2026-July-South-America-Monthly-Finals|South America]]
- 地图结构来源：[[Fandom-BSC-July-2026-Observed-Map-Pages|Fandom 三张地图页摘要]]
- 复核日期：2026-07-14
- source_type：`cross_event_map_fit_review`

## 语义边界

- 本页把逐 set 选择当作“需要解释的观察”，不是因果胜率、tier 或无条件地图推荐。
- 只有能同时连接到稳定地图结构、英雄机制、目标转化和失效条件的观察，才提升到英雄页 `map_feature_hooks.example_maps`。
- `set 胜场` 只描述该英雄所在阵容的 set 结果；提升决定不以胜率阈值自动触发。
- 本页不进入 BP runtime。`compile` 只从地图实体、英雄实体和显式 strength profile 生成 runtime index。

## 地图样本范围

| 地图 | 模式 | 实际进行 sets | 复核结果 |
| --- | --- | ---: | --- |
| Crystal Arcade | Gem Grab | 6 | 4 个机制成立的英雄 map-fit 被提升；2 个观察保留但不提升 |
| Goldarm Gulch | Knockout | 3 | Charlie 的条件化隔离职责被提升；Damian 保留但不提升 |
| Pinhole Punt | Brawl Ball | 2 | 单英雄均只有 1 set；稳定地图职责与既有英雄 hooks 已覆盖，不新增英雄特例 |

## 已提升的稳定 map-fit

| 地图 | 英雄 | 选用 sets | 所在阵容 set 胜场 | 提升到的稳定机制 | 关键失效条件 |
| --- | --- | ---: | ---: | --- | --- |
| Crystal Arcade | Griff | 5 | 2 | `gem_mid_super_area_and_anti_body`：中央墙边宽 Super、近中距离反身体与 carrier 退线保护 | 对方极远长手或墙后投掷能迫使 Griff 离开有效距离时失效 |
| Crystal Arcade | Stu | 3 | 2 | `dash_chain_lane_pressure`：半开放侧路命中后连续位移，形成 Gem side lane 节奏 | 召唤物挡弹、硬控覆盖 dash 终点或中央墙让首发无法命中时失效 |
| Crystal Arcade | Pearl | 2 | 2 | `gem_heat_shield_mid_anchor`：利用中央墙边蓄 Heat，保护矿区和 carrier 退线 | 被投掷或开阔长线逼迫频繁开火、无法维持 Heat 时失效 |
| Crystal Arcade | Meeple | 2 | 1 | `gem_mid_rule_area_carrier_pressure`：Critical Success 改写中央墙体，保护撤退或压矿区入口 | 规则区无法覆盖关键墙、队友不能利用穿墙投射或 Meeple 被多角度切入时失效 |
| Goldarm Gulch | Charlie | 2 | 2 | `knockout_cocoon_first_pick_and_spider_route_tax`：Cocoon 隔离墙袋关键目标，Spiders 探侧草并收取弹药税 | 缺 follow-up、范围伤害免费清资源或双侧线权丢失时失效 |

以上提升只让编译器在对应地图激活已有或新增的条件化 hook，不改变英雄全局强度 tier。

## 已观察但未提升

| 地图 | 英雄 | 选用 sets | 所在阵容 set 胜场 | 不提升原因 |
| --- | --- | ---: | ---: | --- |
| Crystal Arcade | Glowy | 2 | 0 | 牵线支援可能与矿区换血有关，但两次样本都未转成 set 胜利，且现有资料不足以确认她在中央墙体与多角度侧夹下如何稳定维持视线。 |
| Goldarm Gulch | Damian | 2 | 0 | 两次选择都未获胜；跳入墙袋或毒圈阶段的职责有解释空间，但缺少落点、资源和反控制上下文，不能提升为稳定 Knockout map-fit。 |
| Pinhole Punt | 所有单次选择 | 1 / 英雄 | - | 每个英雄只出现 1 个 set；地图的探草、控球、门前 reset 与选择性破门职责已能由稳定地图实体和既有 hooks 编译，无需为单场阵容复制特例。 |

## Runtime 连接点

- `Crystal Arcade`：地图实体提供中央墙、侧草、carrier 退线和地形保留任务；Griff、Stu、Pearl、Meeple 的 exact example map 使相应 hook 在 compile 阶段进入候选解释。
- `Goldarm Gulch`：地图实体提供侧草、墙袋、毒圈退出与双侧 collapse 任务；Charlie 的新 hook 只在队伍有侧路线权和收割 follow-up 时成立。
- `Pinhole Punt`：地图实体提供草环探测、墙封推进与窄门转换任务；runtime 继续通过能力需求和既有 Brawl Ball hooks 组合候选，不使用赛事频率做加权。

## 关联页面

- [[../entities/maps/Crystal Arcade|Crystal Arcade]]
- [[../entities/maps/Goldarm Gulch|Goldarm Gulch]]
- [[../entities/maps/Pinhole Punt|Pinhole Punt]]
- [[../entities/brawlers/Griff|Griff]]
- [[../entities/brawlers/Stu|Stu]]
- [[../entities/brawlers/Pearl|Pearl]]
- [[../entities/brawlers/Meeple|Meeple]]
- [[../entities/brawlers/Charlie|Charlie]]
