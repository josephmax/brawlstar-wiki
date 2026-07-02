# Fandom 来源摘要: Ranked 地图页建模价值评估

## 来源信息

- 标题：Fandom Ranked Map Source Assessment
- 来源：Brawl Stars Wiki / Fandom 地图与 Ranked 页面
- 抓取日期：2026-06-29
- 类型：地图来源评估 / 排位地图池 / 社区攻略来源
- 上游 raw：[[../../raw/sources/fandom/maps/ranked-map-source-assessment-2026-06-29.md]]
- raw 状态：已按维护者要求压缩为 compact manifest；详细评估保留在本来源摘要中。

## 调研问题

本次调研回答一个具体问题：Fandom 的地图页能否提供足够细的地图信息，用来支持 [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]，而不是只给出 `open`、`water_value`、`wall_density` 这类粗标签。

结论：可以作为第一批地图建模的主来源，但不能直接作为最终 BP 结论。

## 当前 Ranked 地图池快照

Fandom 的 `Ranked` 页面在 `Active maps (Season 46)` 下列出了当前排位地图池。按页面快照整理：

- `Gem Grab`：`Double Swoosh`、`Gem Fort`、`Hard Rock Mine`、`Undermine`
- `Heist`，featured：`Bridge Too Far`、`Hot Potato`、`Kaboom Canyon`、`Pit Stop`、`Safe Zone`、`Safe(r) Zone`
- `Bounty`：`Dry Season`、`Hideout`、`Layer Cake`、`Shooting Star`
- `Brawl Ball`：`Center Stage`、`Pinball Dreams`、`Sneaky Fields`、`Triple Dribble`
- `Hot Zone`：`Dueling Beetles`、`Open Business`、`Parallel Plays`、`Ring of Fire`
- `Knockout`：`Belle's Rock`、`Flaring Phoenix`、`New Horizons`、`Out in the Open`

这个列表具有时间语境：它是 2026-06-29 调研时 Fandom 页面显示的 Season 46 快照。后续排位轮换变化时必须重抓。

## 页面结构价值

抽检到的 Fandom 地图页通常包含：

- 地图模式和环境
- 障碍物数量
- 地图图片链接
- `Layout`：地图几何、路线、草丛、墙体、水域、目标位置等描述
- `Tips`：具体英雄如何利用地形、哪些英雄或打法受限
- `History`：加入、移除、改动、赛事或排位出现记录

其中 `Layout` 和 `Tips` 最适合转译为本地 `map_feature`：

- `route_effect`
- `objective_effect`
- `combat_effect`
- `false_positive_capabilities`
- `draft_implication`

## 抽检判断

`Safe Zone` 页面足够支持第一版 Heist 地图拆解。它包含金库暴露、远程角度、侧路水域、中路主要通道、中心控制和多个英雄互动提示，可转译为 `direct_damage_lanes`、`central_route_to_safe`、`river_barrier`、`central_congestion` 等特征。

`Bridge Too Far` 页面明确三路进攻路线、垂直水域分割和远程跨线射击价值，同时指出投掷在接近金库时存在限制，适合抽取 `lane_isolation`、`long_sightline_across_lanes` 和 `false_positive_thrower`。

`Hard Rock Mine` 页面提供开放中场、H 形草丛、狭窄横向通路、边路短手潜入、投掷站位口袋和 Rosa 改造草丛路线的信息，适合抽取 `grass_network`、`side_flank`、`thrower_pocket` 和 `terrain_modification`。

`Double Swoosh` 页面提供旋涡状草丛、侧路埋伏、破墙削弱绕后、中心扩散攻击、Tara 探草和 Rosa 连草等信息，适合抽取 `bush_spiral_route`、`flank_pressure`、`scouting_value` 和 `terrain_denial`。

`Center Stage` 页面提供足球图中的中心草丛边界、边路草带、球门入口、Speed Gear 价值、Rosa 和扩散攻击价值、狙击风险等信息，适合与本地 `Brawl Ball` 模式框架结合。

`Ring of Fire` 页面提供单圈争夺、中心大草、L 形水域、右路长射线与埋伏风险、墙后炮台和支援口袋等信息，适合抽取 `single_zone_anchor`、`bush_entry_rule`、`support_pocket` 和 `turret_anchor`。

`Belle's Rock` 页面提供三路、棋盘墙体、投掷掩体、Sprout 封路、破墙反投掷、Rico/Ruffs 弹墙等信息，适合抽取 `thrower_pocket`、`wall_break_counterplay`、`bounce_wall` 和 `path_blocking`。

`Out in the Open` 页面提供开阔中路、跳板、水域角度、狙击价值、Brock 开墙制造多方向进攻、Eve/Juju/Angelo 利用水域进退等信息，适合抽取 `open_mid_marksman`、`wall_break_route_creation`、`water_angle` 和 `launch_pad_route`。

## 使用边界

Fandom 适合做地图建模的“第一层证据”，不适合直接输出 BP：

- 地图 tips 是社区攻略，更新速度和质量不稳定。
- 英雄推荐可能落后版本强度。
- 页面能描述地形和英雄互动，但不天然提供 ban 位、顺位、阵容前缀和对手反制权。
- 页面图片能辅助几何判断，但文字本身不提供结构化坐标。

因此，后续 ingest 应采用这个转换流程：

```text
Fandom map page
-> raw capture
-> map_feature candidates
-> local map entity page
-> conditional matchup activation
-> candidate_eval.map_fit
-> BP DSL 输出
```

## 后续建议

值得抓取当前 Ranked Season 46 全部地图页，但应该按模式分批，不要一次把所有地图混在一起：

1. 先抓 `Heist`，因为当前 Season 46 是 featured mode，且地图特征最直接影响 safe damage、远程角度、过河、开墙和 base entry。
2. 再抓 `Knockout` 与 `Bounty`，因为长线、掩体、投掷、破墙和生存空间对 BP 影响很大。
3. 再抓 `Gem Grab` 与 `Hot Zone`，重点抽取中线控制、草丛网络、站位锚点和翻盘路径。
4. 最后抓 `Brawl Ball`，需要与本地得分手、推进、破门、持球和抢球框架结合。

## 关联页面

- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/Ban-Pick-问题拆分|Ban Pick 问题拆分]]
- [[sources/User-Note-Map-Profile-Schema|用户经验来源摘要: 地图特征建模需要战术特征 Schema]]
