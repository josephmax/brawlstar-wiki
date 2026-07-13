# Power League Prodigy 站点与抽检

## 来源信息

- 标题：Power League Prodigy public site and sample guide capture
- 来源：[Power League Prodigy](https://powerleagueprodigy.com/)
- Sitemap：[powerleagueprodigy.com/sitemap.xml](https://powerleagueprodigy.com/sitemap.xml)
- 基线读取日期：2026-06-29
- 最新复核日期：2026-07-11
- 类型：第三方竞技工具 / Draft simulator / Draft practice / 角色攻略 / Blog
- 基线上游 raw：[[../../raw/sources/pl-prodigy/site-and-sample-2026-06-29.md]]
- 最新审计 raw：[[../../raw/sources/pl-prodigy/site-audit-2026-07-10.md]]
- raw 状态：已按维护者要求压缩为 compact manifest；抽检字段和可复用结论保留在本页与相关 BP 综合页。

## 站点覆盖

PL Prodigy 公开站点包含几类与本地 BP 知识库高度相关的内容：

- Draft simulator：用于模拟 pick / ban 局面
- Draft practice：用于生成练习场景并给出反馈
- Draft rush：用于限时训练快速选角判断
- Tier lists：提供版本与数据驱动的强度入口
- Brawler guides：提供角色 build、适合模式、counter 关系
- Blog：包含赛事 draft study、版本变化、新英雄早期判断和访谈

公开产品入口：

| 类型 | URL |
| --- | --- |
| Draft simulator | https://powerleagueprodigy.com/plprodigy |
| Draft practice | https://powerleagueprodigy.com/draftpractice |
| Draft rush | https://powerleagueprodigy.com/draftrush |
| Tier lists | https://powerleagueprodigy.com/tierlists |
| Brawler guides index | https://powerleagueprodigy.com/guides |
| Blog index | https://powerleagueprodigy.com/blog |

## 2026-07-10 复核

- Sitemap 与 guide index 仍只有 `104` 位英雄；`Nori`、`Wendy` 的 guide URL 均为 404。PLP 因此尚未覆盖刚进入正式 roster 的 Nori。
- Blog index 没有 7 月平衡分析；最新可见文章日期为 2026-06-30。
- 当前公开 payload 与本地 2026-06-29/30 direct raw 对比，至少能确认三项 build 字段变化：
  - `8-Bit`：`Extra Credits / Boosted Booster / Damage + Health`
  - `Brock`：`Rocket Laces / More Rockets / Damage + Shield`
  - `Max`：`Sneaky Sneakers / Super Charged / Shield + Damage`
- 104 份 guide 中有 67 份动态 matchup 列表发生变化；这些只进入待机制复核的 audit seed，不覆盖 canonical PLP 英雄来源页，也不直接形成稳定 counter 边。
- PLP 的 guide sitemap `lastmod` 和 payload `sourceUpdatedAt` 没有随这些内容变化而更新，无法证明变化发生于 7 月。公开 draft 数据面虽显示 2026-07-07 更新，但它属于动态强度输入，不是稳定英雄事实。
- 2026-07-11 已用仓库维护脚本补抓 8-Bit、Brock、Max 的 per-Brawler canonical PLP raw，并刷新对应来源摘要；三项 build 变化现已可复现追溯。
- 其余动态 matchup 变化继续只保留为站点审计种子，未全量重抓、未直接形成稳定 counter 边。

## 2026-06-29 基线抽检结论

这次没有全量抓取 100+ 个角色页，只抽检了 `Brock`、`Gene`、`Otis`、`Shade`、`Belle`、`Kaze`、`Colt`、`Angelo` 等代表样本。

角色页公开 payload 中确实能提取以下结构化字段：

- 推荐 Gadget
- 推荐 Star Power
- 推荐 Gears
- 适合 Modes
- 备注 Notes
- 避免项 Avoid
- `countersThese`
- `counteredBy`

这些字段对本地 wiki 有价值，尤其适合补充英雄实体页中的：

- 不同 build 的战术取向
- 适合地图 / 模式的初筛
- 经典对位关系
- BP 中的先手、反手、补位、保护性选择

## 2026-06-29 基线抽检样例

| 英雄 | PLP 推荐 build | 适合模式 | 对位价值 |
| --- | --- | --- | --- |
| `Brock` | Rocket Laces / More Rockets / Shield + Reload | Heist, Bounty, Knockout | 克制部分低机动或站位笨重目标；被 Stu、Crow、Max、刺客类切入压制 |
| `Gene` | Vengeful Spirits / Magic Puffs / Shield + Vision + Talk to the Hand | Bounty, Knockout | 克制部分短手、投掷和中距离目标；被长射程、召唤压制和高机动突进干扰 |
| `Otis` | Phat Splatter / Ink Refills / Shield + Speed + Damage + Vision + Super Charge | Gem Grab, Brawl Ball, Heist, Hot Zone | 对 Chuck、Sam、Rosa、Bibi 等进场或节奏型英雄有针对价值 |
| `Shade` | Longarms / Hardened Hoodie / Shield + Damage | Gem Grab, Brawl Ball, Heist, Hot Zone | 能压迫 Brock、Sprout、Nani 等依赖距离或地形舒适区的英雄 |
| `Belle` | Nest Egg / Positive Feedback / Shield + Reload | Heist, Hot Zone, Bounty, Knockout | 适合反制进场和聚集站位，是反 aggro 的稳定功能位 |
| `Kaze` | Gracious Host / Gratuity Included / Shield + Damage + Health | 多模式覆盖 | 是高威胁 aggro / safe pressure 样本，但先手会暴露反制目标 |
| `Colt` | Speedloader / Slick Boots / Shield + Damage | Heist, Brawl Ball, Gem Grab | 在 Heist / Safe Zone 类局面中提供直接 DPS 和开图压力 |
| `Angelo` | Stinging Flight / Empower / Damage + Shield + Gadget Cooldown | Heist, Bounty, Knockout | 水域图和长线对枪价值高，但需要防被投掷、长狙或贴脸处理 |

2026-06-29 基线 payload 中保留的精确字段如下。这里的 `countersThese` / `counteredBy` 只作为条件化对位建模的候选边，不能直接当作无条件克制；与上方 2026-07-10 现场审计不一致时，以日期区分，不把旧值误读为当前推荐。

| 英雄 | URL | Build | Modes | Notes | countersThese | counteredBy |
| --- | --- | --- | --- | --- | --- | --- |
| Brock | https://powerleagueprodigy.com/brock | Rocket Laces / More Rockets / Shield, Reload | Heist, Bounty, Knockout | Gadget 1 into aggro | 8-Bit, Nita, Pam, Shelly, Mr. P, Hank, Spike, Emz | Stu, Crow, Max, Cordelius, Leon, Mortis, Bibi, Edgar |
| Gene | https://powerleagueprodigy.com/gene | Vengeful Spirits / Magic Puffs / Shield, Vision, Talk to the Hand | Bounty, Knockout | none observed | Fang, Emz, Squeak, Barley, Carl, Sprout, Rico, Buzz | Mico, Bea, Stu, Eve, Mr. P, Brock, Piper, Mandy |
| Otis | https://powerleagueprodigy.com/otis | Phat Splatter / Ink Refills / Shield, Speed, Damage, Vision, Super Charge | Gem Grab, Brawl Ball, Heist, Hot Zone | none observed | Chuck, Sam, Rosa, Trunk, Ash, Bibi, Damian, Mandy | Ollie, Barley, Ziggy, Glowy, Larry & Lawrie, Shade, Lola, Willow |
| Shade | https://powerleagueprodigy.com/shade | Longarms / Hardened Hoodie / Shield, Damage | Gem Grab, Brawl Ball, Heist, Hot Zone | none observed | Mr. P, Jessie, Gale, Sprout, Brock, Jae-Yong, Squeak, Nani | Doug, Jacky, Trunk, Frank, Finx, Bibi, Ash, Hank |
| Belle | https://powerleagueprodigy.com/belle | Nest Egg / Positive Feedback / Shield, Reload | Heist, Hot Zone, Bounty, Knockout | Gadget 1 into aggro | El Primo, Jacky, Shelly, Buzz, Hank, Stu, Griff, Frank | Sprout, Chuck, Rosa, Barley, Willow, Bibi, Larry & Lawrie, Sandy |
| Kaze | https://powerleagueprodigy.com/kaze | Gracious Host / Gratuity Included / Shield, Damage, Health | Gem Grab, Brawl Ball, Heist, Hot Zone, Bounty, Knockout | preference; Gadget 1 pro | Mr. P, Jessie, Sprout, Ziggy, Dynamike, Grom, Piper, Brock | Chester, Bull, Sandy, Trunk, Sam, Rosa, Doug, Bibi |
| Colt | https://powerleagueprodigy.com/colt | Speedloader / Slick Boots / Shield, Damage | Heist, Brawl Ball, Gem Grab | preference; Star Power 1 pro | R-T, Sprout, Mandy, Tick, Ziggy, El Primo, Piper, Brock | Angelo, Damian, Moe, Bibi, Meeple, Stu, Starr Nova, Chester |
| Angelo | https://powerleagueprodigy.com/angelo | Stinging Flight / Empower / Damage, Shield, Gadget Cooldown | Heist, Bounty, Knockout | avoid Kit | Belle, Colette, Brock, Bea, Gene, Pearl, Colt, Byron | Mandy, Grom, Larry & Lawrie, Tara, Nani, Ruffs, Lola, Mr. P |

## 2026-06-29 基线 Blog 清单

RSS feed 在 2026-06-29 公开列出 9 篇 blog：

| 日期 | 标题 | URL | 分类 | feed 摘要 |
| --- | --- | --- | --- | --- |
| 2026-06-15 | Code: Prodigy, and Everything You Helped Build | https://powerleagueprodigy.com/blog/code-prodigy-and-everything-you-helped-build | Prodigy, Community, Creator Code | 工具、支持、合作与 Code: Prodigy 的社区信。 |
| 2026-06-12 | Bolt Action Rolling Ball: Our Early Thoughts on Bolt | https://powerleagueprodigy.com/blog/bolt-action-rolling-ball-early-thoughts-on-bolt | Bolt, Brawler Guide, Meta | Bolt 的 build、玩法、对位、模式、地图和早期 meta 预测。 |
| 2026-06-05 | Caster Spotlight: Ark! | https://powerleagueprodigy.com/blog/caster-spotlight-ark | Interview, Esports, Drafting | Ark 讨论高光局面、draft 错误和解说准备。 |
| 2026-05-31 | May 30 Balance Changes: Winners, Losers, and Biggest Question Marks | https://powerleagueprodigy.com/blog/may-30-balance-changes-winners-losers-question-marks | Balance Changes, Meta | 5 月 30 日平衡改动后的赢家、输家和疑问点。 |
| 2026-05-22 | Starr Nova First Thoughts: Best Build, Modes, and Early Meta Predictions | https://powerleagueprodigy.com/blog/starr-nova-first-thoughts-best-loadout-modes | Starr Nova, Brawler Guide, Meta | Starr Nova 的早期 build、模式、地图和 meta 判断。 |
| 2026-05-18 | Brawl Cup Draft Study: Crazy Raccoon vs Eternal (Safe Zone) | https://powerleagueprodigy.com/blog/crazy-raccoon-vs-eternal-safe-zone-draft-study | Draft Study, Esports | Safe Zone 的赛事 BP 复盘，涉及 Kaze、Belle、Otis、Shade。 |
| 2026-05-17 | Brawl Stars World Finals 2026 Is Coming to Tokyo | https://powerleagueprodigy.com/blog/brawl-stars-world-finals-2026-tokyo | Esports, World Finals, Tokyo | 东京 World Finals 公告。 |
| 2026-05-15 | Brawl Stars Balance Changes: Damian Got Nerfed, But Let's Not Pretend He's Fixed | https://powerleagueprodigy.com/blog/may-13-balance-changes-damian-nerfed | Balance Changes | Damian、Sirius、Griff 相关改动判断。 |
| 2025-04-13 | A Letter to the Prodigy Community | https://powerleagueprodigy.com/blog/a-letter-to-the-prodigy-community | Prodigy, Community, Announcement | Prodigy Esports LLC 成长与社区感谢信。 |

## Blog 的 BP 价值

RSS feed 公开列出 9 篇 blog，可分成四类：

- BP / Draft：`Brawl Cup Draft Study: Crazy Raccoon vs Eternal (Safe Zone)`、`Caster Spotlight: Ark`
- 新英雄早期攻略：`Bolt Action Rolling Ball`、`Starr Nova First Thoughts`
- 版本变化：`May 30 Balance Changes`、`Damian Got Nerfed`
- 社区 / 赛事资讯：`Code: Prodigy`、`World Finals 2026 Tokyo`、`A Letter to the Prodigy Community`

抽检正文证明其中部分不只是资讯：

- `Crazy Raccoon vs Eternal (Safe Zone)` 是直接可复用的 BP 复盘样本：ban 被解释为封掉简单成型路线，last pick 被解释为同时破坏多个敌方胜利条件。
- `Caster Spotlight: Ark` 强调 draft 准备、ban 数据缺失、以及 draft assistant 不应只告诉玩家“选谁”，还要教“为什么”。
- `May 30 Balance Changes` 适合跟踪版本强度变化，帮助区分短期 patch 强势和长期角色机制。
- `Starr Nova First Thoughts` 适合记录新英雄早期 build、模式和地图判断，但应标注为早期预测。

## 可靠性与边界

- PLP 是第三方竞技工具，不是官方 Supercell 数据源。
- 角色攻略字段公开可见，但来源自身可能随版本更新而变。
- 抽检中的部分 matchup 来源在公开 payload 里标为 legacy / manual，应作为专家经验信号，而不是绝对结论。
- 本地 wiki 使用这类资料时，应保留读取日期与版本语境，避免把短期 meta 或旧 matchup 当作长期事实。

## 对本地 wiki 的意义

PLP 适合作为本地 BP 知识体系的“竞技攻略层”来源：

- Fandom 页面提供稳定事实和技能说明
- 用户经验页提供本地维护者验证过的模式判断
- PLP 可补充 build、counter、mode fit 和 draft study

本地 wiki 不直接复制 PLP 的推荐排序，而是把它拆成可解释维度，接入 [[syntheses/Ban-Pick-问题拆分|Ban Pick 问题拆分]]。
