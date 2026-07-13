# Brawler Roster

## 来源信息

- 基线 raw：[[../../raw/sources/roster/brawlers-roster-2026-06-29|brawlers-roster-2026-06-29]]
- 最新审计 raw：[[../../raw/sources/roster/brawlers-roster-audit-2026-07-10|brawlers-roster-audit-2026-07-10]]
- 英雄状态复核 raw：[[../../raw/sources/fandom/heroes/nori-2026-07-11|nori-2026-07-11]]、[[../../raw/sources/fandom/heroes/wendy-2026-07-11|wendy-2026-07-11]]
- Fandom：[`Category:Brawlers`](https://brawlstars.fandom.com/wiki/Category:Brawlers) 与 MediaWiki category API
- Power League Prodigy：[`sitemap.xml`](https://powerleagueprodigy.com/sitemap.xml) 与 [`guides`](https://powerleagueprodigy.com/guides)
- 基线读取日期：2026-06-29
- 最新复核日期：2026-07-11
- 类型：roster manifest / release-state audit / guide-coverage audit

## 当前结论

- 游戏当前已有 `105` 位已发布英雄；相对 2026-06-29 的 `104` 位基线新增 `Nori`。
- `Nori` 在 2026-07-09 已开放 Training Cave 与早期解锁，因此属于已发布英雄；2026-07-11 已补齐 Fandom direct raw 与 [[sources/Fandom-Nori|Fandom-Nori]] 来源摘要，但 PLP 尚无 guide，本地也尚无经过复核的 BP profile。
- `Wendy` 已有 2026-07-11 Fandom direct raw 与官方预告交叉核验，但当前页仍标记 `FutureUpdate`，不进入当前已发布英雄集合；预发布数值冲突见 [[sources/Fandom-Wendy|Fandom-Wendy]]。
- PLP sitemap 与 guide index 仍为 `104` 个英雄，集合与 2026-06-29 基线相同；`/nori`、`/wendy` 均返回 404。
- 本地稳定运行层仍有 `104` 个 `bp_ready` 英雄。`Nori` 在补齐 PLP 竞技来源或等价高质量竞技证据、strength 输入与 reviewed BP profile 之前，不进入 runtime 编译默认池。

## 数量口径

| 口径 | 数量 | 说明 |
| --- | ---: | --- |
| 游戏已发布英雄 | 105 | Fandom category 正文口径；包含新发布的 Nori |
| Fandom namespace-0 category pages | 107 | 另含 future Wendy 与已移除的限时 Buzz Lightyear 页面 |
| PLP guide coverage | 104 | 未覆盖 Nori / Wendy |
| 本地 `bp_ready` 实体 | 104 | 与旧双源 roster 一致 |
| 当前 roster ingest 缺口 | 1 | Nori：Fandom 机制已 ingest，竞技来源 / strength / profile 未闭环 |

## 证据边界

- 本页只用于确认英雄数量、发布状态、URL 可用性和本地覆盖缺口。
- Fandom category membership 不能证明竞技强度、build 或 matchup。
- PLP guide 缺失不等于英雄未发布，只表示竞技来源覆盖尚未闭环。
- `Wendy` 的预发布数值在 Fandom 与 Supercell 之间存在差异；发布前不得写成稳定实体事实。
- 英雄能力必须继续读取对应 Fandom / 官方 raw；竞技 build、模式适配和对位候选应等 PLP 或其他明确竞技来源。

## 关联页面

- [[sources/Fandom-Release-Notes-June-2026|Fandom 来源摘要: Release Notes June 2026]]
- [[sources/Fandom-Nori|Fandom 来源摘要: Nori]]
- [[sources/Fandom-Wendy|Fandom 来源摘要: Wendy]]
- [[sources/Supercell-Wendy-Announcement-June-2026|Supercell 来源摘要: Wendy Announcement]]
- [[sources/Fandom-Maintenance-July-8-2026|Fandom 来源摘要: Maintenance - July 8, 2026]]
- [[sources/iKaoss11-July-2026-Strength-Profile|iKaoss11 July 2026 Strength Profile]]
