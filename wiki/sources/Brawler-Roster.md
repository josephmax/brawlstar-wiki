# Brawler Roster

## 来源信息

- 基线 raw：[[../../raw/sources/roster/brawlers-roster-2026-06-29|brawlers-roster-2026-06-29]]
- 中期基线 raw（含 Nori）：[[../../raw/sources/roster/brawlers-roster-2026-08-11|brawlers-roster-2026-08-11]]
- 最新基线 raw（含 Wendy / Cosmo / Vince）：[[../../raw/sources/roster/brawlers-roster-2026-09-03|brawlers-roster-2026-09-03]]
- 历史审计 raw：[[../../raw/sources/roster/brawlers-roster-audit-2026-07-10|brawlers-roster-audit-2026-07-10]]
- 英雄状态复核 raw：[[../../raw/sources/fandom/heroes/wendy-2026-09-03|wendy-2026-09-03]]、[[../../raw/sources/fandom/heroes/nori-2026-09-03|nori-2026-09-03]] 与更早的 wendy/nori 日期版
- Fandom：[`Category:Brawlers`](https://brawlstars.fandom.com/wiki/Category:Brawlers) 与 MediaWiki category API（2026-09-03 API 直连成功，无 403）
- Power League Prodigy：[`sitemap.xml`](https://powerleagueprodigy.com/sitemap.xml) 与 [`guides`](https://powerleagueprodigy.com/guides)
- 基线读取日期：2026-06-29
- 最新复核日期：2026-09-03
- 类型：roster manifest / release-state audit / guide-coverage audit

## 当前结论

- 游戏当前已有 `108` 位已发布英雄；相对 2026-08-11 的 `105` 位新增 `Wendy`、`Cosmo`、`Vince`（见 [[sources/Fandom-Release-Notes-August-2026|Release Notes August 2026]]）。
- `Wendy` 已于 2026-08 转正（页面不再携带 `FutureUpdate`），PLP `/wendy` guide 2026-09-03 已上线，Fandom + PLP 双源闭环，本地已建 [[entities/brawlers/Wendy|Wendy]] `bp_ready` profile；其极限充能为 `GREEN ENERGY`。
- `Nori` 的 PLP guide 与 Fandom 页面 2026-09-03 双源刷新；其极限充能为 `MASTER FISHERMAN`，并带入 8 月补丁的数值削弱，实体页已按当前数值更新。
- `Cosmo`、`Vince` 为 2026-08 新发布的 Mythic 英雄；PLP guide 仍 404，按 roster 规则不进入 BP 英雄集合，处于 ingest 队列。
- PLP guide coverage：`nori`、`wendy` 已上线；`cosmo`、`vince` 缺失。
- 本地稳定运行层现有 `106` 个 `bp_ready` 英雄（Wendy 本次闭环；Cosmo / Vince 有意不入，直至竞技来源闭环）。

## 数量口径

| 口径 | 数量 | 说明 |
| --- | ---: | --- |
| 游戏已发布英雄 | 108 | Fandom category 正文口径；105 基线 + Wendy + Cosmo + Vince |
| Fandom namespace-0 category pages | 109 | 另含已移除的限时 Buzz Lightyear 页面（future Wendy 已转正） |
| PLP guide coverage | 107 | nori/wendy 已上线；cosmo/vince 404 |
| 本地 `bp_ready` 实体 | 106 | Wendy 已闭环双源 + bp_ready profile |
| 当前 roster ingest 缺口 | 2 | Cosmo、Vince 等待 PLP（或等效竞技来源）闭环 |

## 证据边界

- 本页只用于确认英雄数量、发布状态、URL 可用性和本地覆盖缺口。
- Fandom category membership 不能证明竞技强度、build 或 matchup。
- PLP guide 缺失不等于英雄未发布，只表示竞技来源覆盖尚未闭环。
- `Wendy` 的预发布数值冲突（官方预告 vs Fandom future 页）已随发布闭合：当前稳定事实以 2026-09-03 direct raw 为准，预发布差异保留在 [[sources/Supercell-Wendy-Announcement-June-2026|Wendy Announcement]] 与历史 raw 中。
- 英雄能力必须继续读取对应 Fandom / 官方 raw；竞技 build、模式适配和对位候选应等 PLP 或其他明确竞技来源。

## 关联页面

- [[sources/Fandom-Release-Notes-June-2026|Fandom 来源摘要: Release Notes June 2026]]
- [[sources/Fandom-Release-Notes-August-2026|Fandom 来源摘要: Release Notes August 2026]]
- [[sources/Fandom-Nori|Fandom 来源摘要: Nori]]
- [[sources/Fandom-Wendy|Fandom 来源摘要: Wendy]]
- [[sources/Supercell-Wendy-Announcement-June-2026|Supercell 来源摘要: Wendy Announcement]]
- [[sources/Fandom-Maintenance-July-8-2026|Fandom 来源摘要: Maintenance - July 8, 2026]]
