# Draft Quiz Heist Edition

[题库索引](../QUESTION-BANK.md) · [本轮核源记录](../SOURCE-VERIFICATION.md)

评分侧材料，禁止交给被测模型。

<a id="q33"></a>

## 33 · 抢劫首选的射线、百分比与资源角色

[题面](https://www.youtube.com/watch?v=m4P2v_NfmlY&t=2s) · `bobby-m4P2v_NfmlY-q1`

**局面**：Heist / Kaboom Canyon；位次 1。己方 尚未选择／未提供；敌方 尚未选择／未提供；已知禁用 Damian。其余禁用未知，已选数组不代表历史顺序。

**作者参考**：Colt、Colette、Crow；条件答案：[]。

**源中理由摘要**：原字幕未充分解释，以下机制为分析推断。

**当前待核项**：本轮目标字段疑点已解除／无单列冲突；这不表示全题视听、完整 bans、补丁与构筑已验收。

**考点与机制链（分析推断）**：

1. Colt 能开线并持续打库；Colette 对特殊目标有强转化；Crow 的历史选项强调线权/反治疗，具体打库强度仍依版本

2. Kaboom Canyon 的中心草与长线要求同时解释守库与输出访问

3. 首选的后两手要能补齐其命中、接近或防突短板

**逐题评分检查**：

- 逐个描述谁开线谁打库谁守库

- 承认 Crow 当前库的 race 定位有限

- 不把金库伤害数字脱离到达时间

**典型失误**：看到作者三个答案就给三者相同职责说明

**反事实追问（待专家验证）**：如果己方没有稳定命中/开墙执行能力，Colt 的理论输出未必兑现

**结论边界**：历史候选集，不作为目前三大最强首选。

**知识依据**：[Colt · capability_vector:](../../../../wiki/entities/brawlers/Colt.md)；[Colt · failure_modes:](../../../../wiki/entities/brawlers/Colt.md)；[Colette · capability_vector:](../../../../wiki/entities/brawlers/Colette.md)；[Colette · failure_modes:](../../../../wiki/entities/brawlers/Colette.md)；[Crow · capability_vector:](../../../../wiki/entities/brawlers/Crow.md)；[Crow · failure_modes:](../../../../wiki/entities/brawlers/Crow.md)；[Kaboom Canyon · map_profile:](../../../../wiki/entities/maps/Kaboom Canyon.md)

---

<a id="q34"></a>

## 34 · 用不可忽视的目标路线绕过狙击对枪

[题面](https://www.youtube.com/watch?v=m4P2v_NfmlY&t=10s) · `bobby-m4P2v_NfmlY-q2`

**局面**：Heist / Safe Zone；位次 2。己方 尚未选择／未提供；敌方 Angelo；已知禁用 Damian。其余禁用未知，已选数组不代表历史顺序。

**作者参考**：Chuck；条件答案：[]。

**源中理由摘要**：原字幕未充分解释，以下机制为分析推断。

**当前待核项**：本轮目标字段疑点已解除／无单列冲突；这不表示全题视听、完整 bans、补丁与构筑已验收。

**考点与机制链（分析推断）**：

1. Angelo 擅长长线交换；Chuck 通过布站路线制造对金库的重复压力，改变对手必须处理的任务

2. Safe Zone 水路/障碍使路线构筑与打库终点安全比单纯射程更关键

3. Chuck 的启动、补充充能和终点被蹲风险必须按版本区分

**逐题评分检查**：

- 画出抽象布站→访问金库→迫使回防链

- 检查早期建线时的防守代价

- 不沿用过时自动充能假设

**典型失误**：解释为 Chuck 单挑天然克 Angelo

**反事实追问（待专家验证）**：若对方补能守终点的硬控/爆发，重复路线可能亏损，需改站或换计划

**结论边界**：知识库当前 Chuck 充能模型与历史可能不同；不可用当前数值“证明”旧局面。

**知识依据**：[Chuck · capability_vector:](../../../../wiki/entities/brawlers/Chuck.md)；[Chuck · failure_modes:](../../../../wiki/entities/brawlers/Chuck.md)；[Angelo · capability_vector:](../../../../wiki/entities/brawlers/Angelo.md)；[Angelo · failure_modes:](../../../../wiki/entities/brawlers/Angelo.md)；[Safe Zone · map_profile:](../../../../wiki/entities/maps/Safe Zone.md)

---

<a id="q35"></a>

## 35 · 末手穿墙刺客把队伍防守转成入库威胁

[题面](https://www.youtube.com/watch?v=m4P2v_NfmlY&t=22s) · `bobby-m4P2v_NfmlY-q3`

**局面**：Heist / Hot Potato；位次 6。己方 Spike、Otis；敌方 Rico、Nita、Carl；已知禁用 Damian。其余禁用未知，已选数组不代表历史顺序。

**作者参考**：Shade；条件答案：[]。

**源中理由摘要**：原字幕未充分解释，以下机制为分析推断。

**当前待核项**：本轮目标字段疑点已解除／无单列冲突；这不表示全题视听、完整 bans、补丁与构筑已验收。

**本轮直接画面证据**：

- `input.enemies`：['Rico', 'Nita', 'Carl'] → ['Rico', 'Nita', 'Carl']。[28.93s 截图](../../../../raw/sources/bobbybs-draft-quiz/visual-evidence/m4P2v_NfmlY-29-q3.png)。敌方中间为红熊帽 Nita，左右 Rico / Carl。保留 Nita。

**考点与机制链（分析推断）**：

1. Spike＋Otis 已能拖延对方近身路线，Shade 可利用 Hot Potato 的墙草建立进库或清守卫路径

2. 对方 Rico/Nita/Carl 的投射/召唤/回旋并非绝对不能打 Shade，要检查其虚体和近身窗口

3. Shade 到达目标后的存活、恐惧工具和超级技能持续时间决定真正收益

**逐题评分检查**：

- 把守库底座与 Shade 的进攻分工连接

- 明确穿墙不等于永远免伤

- 核对第一轮充能与进库路径

**典型失误**：只写 Shade 克制三个英雄，不解释金库收益

**反事实追问（待专家验证）**：若关键墙被拆或对方可覆盖虚体结束点，入库收益大幅下降

**结论边界**：本轮完整题面确认敌方 Nita；仍需按当前/历史构筑分别检查 Shade 充能与进库路线。

**知识依据**：[Shade · capability_vector:](../../../../wiki/entities/brawlers/Shade.md)；[Shade · failure_modes:](../../../../wiki/entities/brawlers/Shade.md)；[Spike · capability_vector:](../../../../wiki/entities/brawlers/Spike.md)；[Spike · failure_modes:](../../../../wiki/entities/brawlers/Spike.md)；[Otis · capability_vector:](../../../../wiki/entities/brawlers/Otis.md)；[Otis · failure_modes:](../../../../wiki/entities/brawlers/Otis.md)；[Rico · capability_vector:](../../../../wiki/entities/brawlers/Rico.md)；[Rico · failure_modes:](../../../../wiki/entities/brawlers/Rico.md)；[Nita · capability_vector:](../../../../wiki/entities/brawlers/Nita.md)；[Nita · failure_modes:](../../../../wiki/entities/brawlers/Nita.md)；[Carl · capability_vector:](../../../../wiki/entities/brawlers/Carl.md)；[Carl · failure_modes:](../../../../wiki/entities/brawlers/Carl.md)；[Hot Potato · map_profile:](../../../../wiki/entities/maps/Hot Potato.md)
