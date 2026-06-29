# Fandom 来源摘要: Ranked Season 46 全量地图页

## 来源信息

- 标题：Ranked Season 46 Map Page Extracts
- 来源：Brawl Stars Wiki / Fandom 地图页
- 抓取日期：2026-06-29
- 类型：地图来源 / 排位地图池 / 社区攻略来源
- 上游 raw：[[../../raw/sources/fandom/maps/ranked-season-46-map-extracts-2026-06-29.md]]
- 前置评估：[[sources/Fandom-Ranked-Map-Source-Assessment|Fandom 来源摘要: Ranked 地图页建模价值评估]]
- raw 状态：已按维护者要求压缩为 compact manifest；详细整理结果在单地图实体页与本来源摘要中。
- 二次 ingest 状态：26 张地图实体页已升级为 `bp_map_profile_v2`，每页包含 `summary`、`topology`、`objective_access`、`tactical_features`、`lane_dynamics`、`map_rules` 和 `false_positive`；`summary_tags` 已从 BP 可消费结构中移除。

## 范围

本次覆盖 Fandom `Ranked` 页面显示的 Season 46 active maps：

- `Gem Grab`：`Double Swoosh`、`Gem Fort`、`Hard Rock Mine`、`Undermine`
- `Heist`：`Bridge Too Far`、`Hot Potato`、`Kaboom Canyon`、`Pit Stop`、`Safe Zone`、`Safe(r) Zone`
- `Bounty`：`Dry Season`、`Hideout`、`Layer Cake`、`Shooting Star`
- `Brawl Ball`：`Center Stage`、`Pinball Dreams`、`Sneaky Fields`、`Triple Dribble`
- `Hot Zone`：`Dueling Beetles`、`Open Business`、`Parallel Plays`、`Ring of Fire`
- `Knockout`：`Belle's Rock`、`Flaring Phoenix`、`New Horizons`、`Out in the Open`

## 来源价值

Fandom 地图页适合抽取第一版 `map_profile`，原因是多数页面提供：

- `Obstacles`：墙体、草丛、水域、不可破墙等粗几何信号
- `Layout`：地图结构、分路、中心区、目标位置和障碍分布
- `Tips`：英雄与地形的具体互动，例如过墙、跳板、投掷口袋、远程角度、草丛扫描、破墙收益
- `History`：地图加入、移除、排位或赛事出现记录

这些信息已经足够把地图从粗标签转成 [[syntheses/地图特征建模Schema|地图特征建模 Schema]] 中的 `map_feature` 候选。2026-06-29 的二次 ingest 已进一步把 26 张地图页从 `first_pass_from_fandom_text` 升级为 `bp_map_profile_v2`，重点补充“能力 -> 路线 / 位置 -> 目标收益 -> 失效条件 -> BP 用途”的中间表达。

## 使用边界

Fandom 地图页不能直接变成 BP 推荐：

- 它提供的是地图互动候选，不提供当前版本强度。
- 部分 Tips 可能过时，英雄名和机制需要与当前实体页校验。
- 地图文字描述不能替代地图图片坐标级校验。
- `map_feature` 必须继续进入 [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]，再结合顺位、ban、前序 pick 和敌方反制权。

## 已沉淀结论

本次来源已经分层沉淀：

- [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]：只作为当前赛季地图池索引。
- `wiki/entities/maps/` 下的 26 张单地图实体页：保存每张图的 `bp_map_profile_v2`，包括稳定 map profile、具体 tactical features、lane dynamics、map rules、BP 用法和 false positive。
- [[syntheses/地图知识分层治理|地图知识分层治理]]：说明地图实体、赛季索引、版本 meta 和英雄 map-fit 的更新边界。

## 关联页面

- [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- [[syntheses/地图知识分层治理|地图知识分层治理]]
- [[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[sources/Fandom-Ranked-Map-Source-Assessment|Fandom 来源摘要: Ranked 地图页建模价值评估]]
