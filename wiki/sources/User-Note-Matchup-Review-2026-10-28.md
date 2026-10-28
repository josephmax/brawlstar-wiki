# 用户来源：13 组克制关系复核（2026-10-28）

## 来源与边界

- 原文：[[../../raw/inbox/2026-10-28-matchup-review-user.md|用户逐项回复]]。
- source_type: maintainer_gameplay_review；source_quality: direct_user_statement。
- usable_for: reviewed_conditional_matchups, disputed_candidate_withdrawal, mechanism_attribution。
- not_usable_for: official_mechanics, measured_win_rate, unconditional_counter, numerical_kill_guarantee。
- 用户已明确给出策略判断；能力与配装前提再对照本地 Fandom/实体。这里不冒称独立实战测评，也不把“五五开”转成实测 50% 胜率。
- “成立”仍需接近、资源、配装与队友条件；原文的“必死”不转换成无条件数值斩杀保证。“半成立”必须收窄条件，不记作普遍克制。

## 逐项采纳

| 编号 | 当前判断与处理 | 机制/边界 |
| --- | --- | --- |
| 1 | Edgar→Squeak 保留，独立机制 | Squeak 延迟出伤、缺直接自保；Edgar 跳中后贴身吸血持续输出。保留跳空、无法持续接触及队友保护的失效条件。 |
| 2 | Finx→Gigi 撤回 | 用户否定；PLP 候选不等于机制，禁止套用远程弹道解释。历史溯源见下。 |
| 3 | Finx→Shade 撤回 | 地形决定优劣，无普遍方向；不替换成反向克制。 |
| 4 | Bolt→Nori 保留，Starr Nova 原因暂缺 | Bolt 需 Toss Up 星徽和满速接触，击退/击飞干扰 Nori；Starr Nova 的长线爆发理由撤回，新的真实原因未提供，暂留来源候选。 |
| 5 | Wendy→Bolt 收窄为区域减速窗口 | Slowing Shield 发生器区域或 Green Grenade 命中；不把减速写成所有构筑常驻。 |
| 6 | Rosa→Bolt 条件性保留 | 身体/护盾使 Bolt 难以完成击杀；Unfriendly Bushes 对草内目标或极限充能减速进一步限制速度。无资源或无法接触时不保证反杀。 |
| 7 | Jacky→Doug/Hank 分开保留 | Pneumatic Booster 接近、Super 拉扯打断，极限充能提供额外减速；Doug/Hank 不是低中血脆皮。 |
| 8 | Wendy→Pierce 撤回 | Pierce 射程与连续拾壳爆发，Wendy 防御承受能力，各有窗口。 |
| 9 | Grom→Eve 收窄 | 地形允许保持射程压制；水路缩短有效距离时优势失效。没有“Eve 站定蓄力”的前提。 |
| 10 | Bea→Gene 撤回 | 多数情况各有胜负手；不把 Honeycomb 条件补齐后就继续当普遍克制。 |
| 11 | Tara→Rico 撤回 | 射程劣势下需攒出 Super 才有击杀窗口；有大招威胁不等于普遍对位优势。 |
| 12a | Juju→Berry 收窄 | 射程/输出压制的站位窗口；Berry 有位移和击退反制。两个英雄页同步。 |
| 12b | Gray→Berry 保留，单独机制 | Walking Cane 拉出掩体与传送切入斩杀；不能把这推广为所有妙具同一效果。 |
| 12c | Sirius→Berry 撤回 | 优势方向不明确，不编造替代机制。 |
| 12d | 8-Bit/Berry 拆为地形条件边 | 开阔长线 8-Bit 压制；有墙且 Berry 可安全覆盖增伤器/目标点时，Berry 可反制。互不推广到另一地形。 |
| 13a | Stu→Gigi 保留，单独机制 | 连续位移风筝，使 Gigi 第一轮未斩杀后难以持续接触。 |
| 13b | Stu→Squeak 保留，单独机制 | 位移躲延迟爆炸、利用射程窗口压制；Breakthrough 可破可破坏墙，钢墙不适用。没有宣称 Stu 基础射程数值一定更长。 |

## Finx/Gigi 历史溯源

- [[../../raw/sources/pl-prodigy/brawlers/finx-2026-06-30.md|2026-06-30 PLP Finx 抓取件]] 的 `Matchup Fields.countersThese` 确实包含 Gigi：`source=data`、`matchupTier=global-best-modes`、`winRate=0.628`。不是回答模型临时创造名字，也不是本次优化把方向翻转。
- 原始抓取的 `payload sourceUpdatedAt` 为 2026-05-25；没有足够样本数、筛选口径与地图拆分，也没有逐目标机制说明。62.8% 仅是该抓取字段，不能宣称普遍单挑胜率或当前真值；上游为何得出候选尚无法由保存内容解释。
- Git `66d834ad789d82573dedeed435826b77f581b55b`（2026-06-30，upgrade BP-ready brawler profiles）把 Finx 草稿从 `draft_from_raw_signals` 提升为 `bp_ready`，将 Gigi 与 Piper/Nani/Byron/Mandy 归组，并将 pending 机制替换为 Time Warp 减慢敌方弹道。
- 可确定的本地错误：统计候选未经逐目标机制复核即升级为已审核条件边，并为 Gigi 配上不适用的长线弹道理由。用户本轮否定该关系，撤回实体及编译边，原始抓取不变。
- 同时修复 [[sources/PLP-Finx|PLP Finx 摘要]] 指向不存在的 `finx.md` 的链接，改为现存 dated capture；这是来源导航错误，不是方向生成的根因。

## 机制交叉核对

- [[sources/Fandom-Bolt|Bolt]]：Toss Up 满速接触击飞；Unstoppaball 开启 Super 的短免控窗口不能被减速解释忽略。
- [[sources/Fandom-Wendy|Wendy]]：Slowing Shield 星徽使发生器区域减速；Green Grenade 另有命中前提。
- [[sources/Fandom-Rosa|Rosa]]：Unfriendly Bushes 对草内目标、极限充能随身减速，均非普攻常驻减速。
- [[sources/Fandom-Jacky|Jacky]]：Pneumatic Booster 加速、Super 拉扯取消攻击、极限充能减速。
- [[sources/Fandom-Stu|Stu]]：Breakthrough 是破墙前提；保留钢墙例外。
- [[sources/Fandom-Gray|Gray]]、[[sources/Fandom-Edgar|Edgar]]、[[sources/Fandom-Berry|Berry]]：相应拉人/传送、攻击回血、位移/击退事实；用户补足逐目标实战判断。

## 后续缺口

Starr Nova→Nori 的真实原因仍待补充；撤回旧理由不表示已证明方向相反。当前批次是维护者复核后的知识修正，真实回答回放和 NAS 现场效果尚需另外验证。
