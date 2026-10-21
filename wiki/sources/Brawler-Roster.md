# Brawler Roster

## 来源信息

- 基线 raw：[[../../raw/sources/roster/brawlers-roster-2026-06-29|brawlers-roster-2026-06-29]]
- 中期基线 raw（含 Nori）：[[../../raw/sources/roster/brawlers-roster-2026-08-11|brawlers-roster-2026-08-11]]
- 最新覆盖 manifest：[[../../raw/sources/roster/brawlers-roster-2026-10-21|2026-10-21 108 位英雄覆盖清单]]；旧 2026-09-03 raw 链接已失效，本次用实际留存的当前来源修复。
- 历史审计 raw：[[../../raw/sources/roster/brawlers-roster-audit-2026-07-10|brawlers-roster-audit-2026-07-10]]
- 英雄状态复核 raw：[[../../raw/sources/fandom/heroes/wendy.md|Wendy 当前抓取]]、[[../../raw/sources/fandom/heroes/nori.md|Nori 2026-10-21 补抓]]；Nori 原缺失的 canonical raw 已从现页恢复，[[../../raw/sources/fandom/heroes/nori-2026-07-11|7 月历史抓取]]仍保留。Cosmo / Vince 原文见各自 canonical source 页面。
- Fandom：[`Category:Brawlers`](https://brawlstars.fandom.com/wiki/Category:Brawlers) 与 MediaWiki category API（2026-09-03 API 直连成功，无 403）
- Power League Prodigy：[`sitemap.xml`](https://powerleagueprodigy.com/sitemap.xml) 与 [`guides`](https://powerleagueprodigy.com/guides)
- 基线读取日期：2026-06-29
- 最新复核日期：2026-10-21
- 类型：roster manifest / release-state audit / guide-coverage audit

## 当前结论

- 当前可识别且已开放获取的英雄为 `108` 位（含提前获取）；Cosmo 2026-09-10 提前获取、10-01 常规获取，Vince 2026-10-19 提前获取。8 月公告只预告二人，不能把公告日期当作已发布日期。见 [[sources/新英雄头像与发布状态复核-2026-10|发布状态复核]]。
- `Wendy` 已于 2026-08 转正（页面不再携带 `FutureUpdate`），PLP `/wendy` guide 2026-09-03 已上线，Fandom + PLP 双源闭环，本地已建 [[entities/brawlers/Wendy|Wendy]] `bp_ready` profile；其极限充能为 `GREEN ENERGY`。
- `Nori` 的 PLP guide 与 Fandom 页面 2026-09-03 双源刷新；其极限充能为 `MASTER FISHERMAN`，并带入 8 月补丁的数值削弱，实体页已按当前数值更新。
- `Cosmo`、`Vince` 的 Fandom / PLP direct raw 与四份 canonical source 页面在远端 2026-10-16 已建立，本地 2026-10-21 抓取补充最新状态；两期 raw 分别保留，source 合并。PLP 已有真实 guideRecord，旧 404 结论失效。
- 本地稳定运行层现有 `106` 个 `bp_ready` 英雄；Cosmo / Vince 目前缺完整六模式、地图路线与条件对位的人工复核 profile，尚未因双源可用而自动升级。

## 数量口径

| 口径 | 数量 | 说明 |
| --- | ---: | --- |
| 已开放获取（含提前获取） | 108 | 104 基线 + Nori / Wendy / Cosmo / Vince；不推定赛事可选资格 |
| Brawl API 清单行数 | 109 | 含已移除 Buzz Lightyear；并非当前英雄分母 |
| 双源 URL 覆盖 | 108 | 104 基线及四个新增身份；本次直接复核新增 Cosmo / Vince，未重抓全部旧攻略 |
| 本地 `bp_ready` 实体 | 106 | Wendy 已闭环双源 + bp_ready profile |
| 当前 reviewed profile 缺口 | 2 | Cosmo、Vince 来源齐备，仍需完整 BP 模型复核 |

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
