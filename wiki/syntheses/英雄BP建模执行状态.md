# 英雄 BP 建模执行状态

本页记录 [[syntheses/英雄BP建模升级任务计划|英雄 BP 建模升级任务计划]] 的实际执行进度。计划页保持为方法与验收标准，本页用于交接当前完成度和下一步。

状态日期：2026-06-30。

## Scope

- 上游 roster manifest 保留 Fandom 105 行事实：[[sources/Brawler-Roster-2026-06-29|Brawler Roster 2026-06-29]]。
- 当前 BP-active scope 为 104 个非临时英雄。
- `Buzz Lightyear` 已按 [[sources/User-Note-Buzz-Lightyear-Out-of-Scope|维护者说明]] 排除，不进入 raw 补抓、PLP 缺口、英雄实体、对位边或地图适配索引。

## Phase 0: roster manifest

状态：已完成。

- raw manifest：[[../../raw/sources/roster/brawlers-roster-2026-06-29.md]]
- 来源摘要：[[sources/Brawler-Roster-2026-06-29|Brawler Roster 2026-06-29]]
- Fandom `Category:Brawlers` 返回 105 个 Brawler 页面。
- PLP sitemap 返回 104 个英雄 guide URL。
- 原本地英雄实体页 72 个；BP-active 缺失实体页 32 个。

## Phase 1: 全量 raw capture

状态：104 个 BP-active 英雄两站 raw 均已完成。

- Fandom：104/104 有 corrected direct raw capture。
  - 2026-06-30 首轮补抓中发现单行 infobox 模板解析漂移。
  - 已用 `2026-06-30-v2` 为 104 个 BP-active 英雄补抓 corrected Fandom raw。
  - `Chester` 与 `Kaze` 使用专属 `Chester Infobox` / `Kaze Infobox`，已用 `2026-06-30-v3` 定点修正。
- PLP：104/104 有 direct raw capture。
  - `Meeple` 首次 PLP 请求出现 SSL 抖动，定点重试后成功。
- 旧 raw 未覆盖；漂移修正均以新 dated raw 文件保留。

## Phase 2: 全量 source summaries

状态：104 个 BP-active 英雄两站 source 摘要均已完成。

- Fandom source：104/104。
- PLP source：104/104。
- 所有 PLP `countersThese` / `counteredBy` 均只作为 `conditional_matchup_seed`，不写成无条件克制。
- Source 层统一标注 `usable_for` / `not_usable_for`，区分 Fandom 稳定机制事实与 PLP 第三方竞技信号。

## Phase 3: 英雄实体与 BP draft profile

状态：104 个 BP-active 英雄均已有实体页与 `bp_brawler_profile`。

- 新建 32 个缺失 BP-active 英雄实体页。
- 69 个既有英雄页追加 `profile_status: draft_from_raw_signals` 草案。
- `Brock`、`Gene`、`Otis` 三个已有人工草案已复核为 `profile_status: reviewed`，并同步 corrected Fandom raw 日期。
- `8-Bit`、`Alli`、`Amber`、`Angelo`、`Ash`、`Barley`、`Bea`、`Belle`、`Bibi`、`Bo`、`Bolt`、`Bonnie`、`Buster`、`Buzz`、`Carl`、`Charlie`、`Chuck`、`Clancy`、`Colette`、`Colt`、`Cordelius`、`Crow`、`Darryl`、`Doug`、`Draco`、`Emz`、`Finx`、`Gale`、`Gigi`、`Gus`、`Hank`、`Jae-yong`、`Janet`、`Jessie`、`Kaze`、`Kenji`、`Lily`、`Lola`、`Lou`、`Lumi`、`Maisie`、`Mandy`、`Max`、`Meg`、`Melodie`、`Mico`、`Mina`、`Mortis`、`Mr. P`、`Nita`、`Ollie`、`Pam`、`Pearl`、`Penny`、`Poco`、`Rico`、`Rosa`、`Sam`、`Sandy`、`Shade`、`Shelly`、`Squeak`、`Starr Nova`、`Stu`、`Willow`、`Ziggy` 已完成 reviewed profile、reviewed 条件化对位边和 Ranked 地图 hook，升级为 `profile_status: bp_ready`。

草案边界：

- 自动草案用于把 Fandom 机制事实、PLP build/mode/matchup seed、失败条件和 slot notes 接入统一 schema。
- 自动草案不是最终 BP 判断；仍需逐英雄复核机制、地图因素、条件化对位和 build 失效条件。

## Phase 4: 全局 seed 索引

状态：draft seed 索引已建立。

- 新增 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]。
  - 覆盖 104 个 BP-active 英雄。
  - 收录 PLP matchup seed 方向信号 1664 条。
  - 状态为 `draft_seed_index_from_plp_payload`，不是最终 counter 表。
  - 已追加 `reviewed_from_brawler_profiles` 区，当前有 244 组 reviewed 条件化对位边。
- 新增 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]。
  - 覆盖 104 个 BP-active 英雄。
  - 汇总英雄页 map hook seed 271 条。
  - 状态为 `draft_seed_index_from_brawler_profiles`，不是最终地图适配结论。
  - 已追加 `reviewed_from_brawler_profiles` 区，当前有 240 条 reviewed Ranked 地图 hook。

## Phase 5: reviewed / bp_ready 质量升级

状态：进行中。

- `bp_ready`：66 个，分别为 `8-Bit`、`Alli`、`Amber`、`Angelo`、`Ash`、`Barley`、`Bea`、`Belle`、`Bibi`、`Bo`、`Bolt`、`Bonnie`、`Buster`、`Buzz`、`Carl`、`Charlie`、`Chuck`、`Clancy`、`Colette`、`Colt`、`Cordelius`、`Crow`、`Darryl`、`Doug`、`Draco`、`Emz`、`Finx`、`Gale`、`Gigi`、`Gus`、`Hank`、`Jae-yong`、`Janet`、`Jessie`、`Kaze`、`Kenji`、`Lily`、`Lola`、`Lou`、`Lumi`、`Maisie`、`Mandy`、`Max`、`Meg`、`Melodie`、`Mico`、`Mina`、`Mortis`、`Mr. P`、`Nita`、`Ollie`、`Pam`、`Pearl`、`Penny`、`Poco`、`Rico`、`Rosa`、`Sam`、`Sandy`、`Shade`、`Shelly`、`Squeak`、`Starr Nova`、`Stu`、`Willow`、`Ziggy`。
- `reviewed`：3 个，分别为 `Brock`、`Gene`、`Otis`；这三页已过单英雄 reviewed 门槛，但仍缺至少 3 条 reviewed 条件化对位边和 3 条接入 Ranked 地图的 hook，暂不标 `bp_ready`。
- `draft_from_raw_signals`：35 个，仍含自动占位、空地图示例或未复核 matchup seed。
- 质量审计页：[[syntheses/英雄BP建模质量审计|英雄 BP 建模质量审计]]。

## 剩余质量门槛

下一步不再是“抓取缺口”，而是“把 draft seed 升级为可消费 BP 知识”：

1. 逐批把剩余 35 个 `draft_from_raw_signals` 英雄提升为 reviewed：先复核 Fandom 机制抽取，再修正自动能力向量误判。
2. 对 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]] 中的高频边补 `mechanism / active_when / fails_when / bp_use`。
3. 对 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]] 中的 hook 接入具体 Ranked Season 46 地图、路线/位置、目标收益和失效条件。
4. 只有完成上述复核的英雄或边，才能从 `draft` 升级为 `reviewed` 或 `bp_ready`；不要直接批量标记 `bp_ready`。

## 当前验收快照

- BP-active 英雄：104。
- 英雄实体页：104。
- 含 `bp_brawler_profile`：104。
- `profile_status: bp_ready`：66。
- `profile_status: reviewed`：3。
- `profile_status: draft_from_raw_signals`：35。
- Fandom source：104。
- PLP source：104。
- Buzz Lightyear 实体页：0。

## 关联页面

- [[syntheses/英雄BP建模升级任务计划|英雄 BP 建模升级任务计划]]
- [[syntheses/英雄BP建模质量门槛|英雄 BP 建模质量门槛]]
- [[syntheses/英雄BP建模质量审计|英雄 BP 建模质量审计]]
- [[syntheses/英雄BP建模覆盖审计|英雄 BP 建模覆盖审计]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]
- [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
- [[sources/User-Note-Buzz-Lightyear-Out-of-Scope|用户经验来源摘要: Buzz Lightyear 不进入 BP 建模]]
