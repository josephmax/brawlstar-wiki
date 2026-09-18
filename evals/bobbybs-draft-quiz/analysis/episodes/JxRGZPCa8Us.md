# Draft Quiz VIEWER EDITION

[题库索引](../QUESTION-BANK.md) · [本轮核源记录](../SOURCE-VERIFICATION.md)

评分侧材料，禁止交给被测模型。

<a id="q01"></a>

## 01 · 双边路后的中路补位

[题面](https://www.youtube.com/watch?v=JxRGZPCa8Us&t=13s) · `bobby-JxRGZPCa8Us-q1`

**局面**：Gem Grab / Hard Rock Mine；位次 6。己方 Griff、Starr Nova；敌方 Amber、Carl、Otis；已知禁用 Gus、Shade、Rico。其余禁用未知，已选数组不代表历史顺序。

**作者参考**：Pierce、Byron、Janet；条件答案：[]。

**源中理由摘要**：补足远程中路位；两名现有队友承担边路

**当前待核项**：本轮目标字段疑点已解除／无单列冲突；这不表示全题视听、完整 bans、补丁与构筑已验收。

**本轮直接画面证据**：

- `input.enemies`：[] → ['Amber', 'Carl', 'Otis']。[20s 截图](../../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-20-q1.png)。题面上方 Amber / Carl / Otis，下方 Griff / Starr Nova；五个已选头像。

- `input.pick_slot_basis`：explicit_or_inferred_from_visible_caption_counts; see context → inferred_from_complete_visible_five_pick_state。[20s 截图](../../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-20-q1.png)。二友三敌完整，下一手为第六手；不声称看到原始历史选人顺序。

- `input.bans`：['Gus'] → ['Gus', 'Shade', 'Rico']。[20s 截图](../../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-20-q1.png)。确认可辨识的 Gus、Shade、Rico；另一个橙色护目镜小 pin 暂不强行命名，完整 bans 仍为 partial。

**考点与机制链（分析推断）**：

1. Griff 与 Starr Nova 已承担边路和接触压力；敌方 Amber、Carl、Otis 现已还原，第三人需补矿区长线与携宝安全。

2. Byron 的治疗与远程压线、Janet 的探草及空中撤退、Pierce 的长线输出提供不同补位路径；必须检查 Otis 沉默与 Carl 接近是否能覆盖该角色的位置。

3. Gus、Shade、Rico 为已辨认禁用，另一个小 pin 未确认；不能推荐已知被 ban 的 Gus，也不能把未辨认禁用当作不存在。

**逐题评分检查**：

- 识别己方缺中路而非继续补边路

- 结合 Amber 清草、Carl 接近与 Otis 沉默解释射程和携宝安全取舍

- 说明首选如何与 Griff / Starr Nova 分工，并遵守已知 bans

**典型失误**：只说己方缺中路就比较射程，忽略 Carl 接近、Otis 沉默和宝石丢失风险。

**反事实追问（待专家验证）**：若对方补出有路线的刺客，重新检查携宝安全和 peel，原远程排序可能改变

**结论边界**：敌方三人及第六手已确认；仍有一个禁用小 pin 未可靠命名，补丁和构筑未知。

**知识依据**：[Griff · capability_vector:](../../../../wiki/entities/brawlers/Griff.md)；[Griff · failure_modes:](../../../../wiki/entities/brawlers/Griff.md)；[Starr Nova · capability_vector:](../../../../wiki/entities/brawlers/Starr Nova.md)；[Starr Nova · failure_modes:](../../../../wiki/entities/brawlers/Starr Nova.md)；[Byron · capability_vector:](../../../../wiki/entities/brawlers/Byron.md)；[Byron · failure_modes:](../../../../wiki/entities/brawlers/Byron.md)；[Janet · capability_vector:](../../../../wiki/entities/brawlers/Janet.md)；[Janet · failure_modes:](../../../../wiki/entities/brawlers/Janet.md)；[Pierce · capability_vector:](../../../../wiki/entities/brawlers/Pierce.md)；[Pierce · failure_modes:](../../../../wiki/entities/brawlers/Pierce.md)；[Gus · capability_vector:](../../../../wiki/entities/brawlers/Gus.md)；[Gus · failure_modes:](../../../../wiki/entities/brawlers/Gus.md)；[Hard Rock Mine · map_profile:](../../../../wiki/entities/maps/Hard Rock Mine.md)；[Amber · capability_vector:](../../../../wiki/entities/brawlers/Amber.md)；[Amber · failure_modes:](../../../../wiki/entities/brawlers/Amber.md)；[Carl · capability_vector:](../../../../wiki/entities/brawlers/Carl.md)；[Carl · failure_modes:](../../../../wiki/entities/brawlers/Carl.md)；[Otis · capability_vector:](../../../../wiki/entities/brawlers/Otis.md)；[Otis · failure_modes:](../../../../wiki/entities/brawlers/Otis.md)

---

<a id="q02"></a>

## 02 · 投掷＋保镖双选与拆墙反制

[题面](https://www.youtube.com/watch?v=JxRGZPCa8Us&t=39s) · `bobby-JxRGZPCa8Us-q2`

**局面**：Knockout / Belle's Rock；位次 4。己方 Gus；敌方 Piper、Wendy；已知禁用 Shade。其余禁用未知，已选数组不代表历史顺序。

**作者参考**：Sprout；条件答案：[]。

**源中理由摘要**：投掷压制 Piper 与 Wendy；后续搭配 R-T 或 Pearl；Edgar+Rico 有压制与阻止投掷的价值，但对方 Griff 拆墙后 Piper 获益

**组合评分**：Sprout + R-T 或 Sprout + Pearl；不按单手 accepted 计算命中率。两手顺序不作要求。

**当前待核项**：阵容与双选语义已确认；须使用组合评分，不能继续按单手 Sprout 命中评分。禁用栏另三个小 pin 尚未逐一可靠归一化。

**本轮直接画面证据**：

- `input.decision_scope`：None → paired_4_5。[51s 截图](../../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-51-q2.png)。一名己方 Gus、两名敌方 Piper / Wendy；这是 4/5 连选阶段。

- `input.pick_slots`：None → [4, 5]。[51s 截图](../../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-51-q2.png)。位次由完整可见人数推定；两手之间没有对手插入。

- `reference.accepted_pairs`：None → [['Sprout', 'R-T'], ['Sprout', 'Pearl']]。[65s 截图](../../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-65-q2-pair.png)。65s Sprout 头像；字幕49—64s为 thrower + R-T/Pearl，具体 thrower 为 Sprout。组合两手顺序不参与评分。

- `input.bans`：[] → ['Shade']。[51s 截图](../../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-51-q2.png)。仅将明确可辨认的 Shade 写为已知 ban；另三个不同小 pin 留待实体对照，重复禁用不当成六个不同英雄。

- `input.ban_status`：not_provided → partial。[51s 截图](../../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-51-q2.png)。画面展示完整禁用栏，但本次只可靠归一化其中部分名字。

**考点与机制链（分析推断）**：

1. Gus 已提供护盾/反突资源；Sprout 借墙压 Piper 和 Wendy 的直线输出位置

2. 投掷后的第五手 R-T/Pearl 应承担入口防守，避免两名脆后排共同暴露

3. 对方第六手 Griff 可以开墙：Piper 获得长线，而己方依赖墙的角色失去安全位

**逐题评分检查**：

- 把两手当互补组合而非分别选两个 counter

- 明确完整墙与开墙两个状态

- 区分作者偏好的 Sprout 路线与玩家实际 Edgar＋Rico

**典型失误**：说投掷天然克 Wendy；忽略其护盾、炮台区域、跳跃逃生和剩余拆墙

**反事实追问（待专家验证）**：若 Griff/其他廉价开墙不可用，Edgar＋Rico 的反制风险会下降，但不能自动超过投掷组合

**结论边界**：题面与字幕已确认 Sprout + R-T/Pearl 双选建议；两手顺序不计对错。额外 ban 小 pin 未全部识别；独立导出组合输入，暂不混入单手命中率。

**知识依据**：[Gus · capability_vector:](../../../../wiki/entities/brawlers/Gus.md)；[Gus · failure_modes:](../../../../wiki/entities/brawlers/Gus.md)；[Sprout · capability_vector:](../../../../wiki/entities/brawlers/Sprout.md)；[Sprout · failure_modes:](../../../../wiki/entities/brawlers/Sprout.md)；[Piper · capability_vector:](../../../../wiki/entities/brawlers/Piper.md)；[Piper · failure_modes:](../../../../wiki/entities/brawlers/Piper.md)；[Wendy · capability_vector:](../../../../wiki/entities/brawlers/Wendy.md)；[Wendy · failure_modes:](../../../../wiki/entities/brawlers/Wendy.md)；[R-T · capability_vector:](../../../../wiki/entities/brawlers/R-T.md)；[R-T · failure_modes:](../../../../wiki/entities/brawlers/R-T.md)；[Pearl · capability_vector:](../../../../wiki/entities/brawlers/Pearl.md)；[Pearl · failure_modes:](../../../../wiki/entities/brawlers/Pearl.md)；[Griff · capability_vector:](../../../../wiki/entities/brawlers/Griff.md)；[Griff · failure_modes:](../../../../wiki/entities/brawlers/Griff.md)；[Edgar · capability_vector:](../../../../wiki/entities/brawlers/Edgar.md)；[Edgar · failure_modes:](../../../../wiki/entities/brawlers/Edgar.md)；[Rico · capability_vector:](../../../../wiki/entities/brawlers/Rico.md)；[Rico · failure_modes:](../../../../wiki/entities/brawlers/Rico.md)；[Belle's Rock · map_profile:](../../../../wiki/entities/maps/Belle's Rock.md)
