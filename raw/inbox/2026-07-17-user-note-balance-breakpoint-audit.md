# User Note: Balance Breakpoint Audit

- Capture date: 2026-07-17
- Source type: maintainer-provided domain rule and audit request
- Status: captured verbatim in meaning; formulas require implementation-level validation

## 原始要求

每次平衡性调整除了检查能力类型、地图适配和 BP 职责，还要审计伤害与生存数值跨过了哪些实战阈值：

- 索引每个英雄当前血量。
- 满值 Shield gear 作为 `+900` 可消耗护盾。
- 英雄专属护盾、Gadget、Star Power、Buffie 及其合法叠加需要形成条件化生存变体；例如 Bibi、Pearl 等减伤护盾。
- 本项目按维护者提供的游戏规则，将同时生效的不同减伤 buff 先做加法，再换算有效血量：`EHP = (HP + flat shield) / (1 - sum(DR))`。例如 30% 减伤对应 `HP / 0.7`。
- 对每次直接伤害或英雄血量的增加/减少，比较补丁前后击杀所需的命中次数。重点找出：原先三下不能击杀、现在三下能击杀；原先无需 Shield gear 可以多抗一下、现在必须带 Shield gear；或反向变化。
- 这类变化应作为平衡补丁审计的高价值对位证据，但不能脱离攻击形态、距离、命中数、构筑条件和地图职责直接写成强度结论。

## 本轮试验范围

- 先针对 2026 年 6 月底大版本和平衡调整，以及 2026-07-08 maintenance 做一次端到端试验。
- 如果缺少可复用基础索引，可以为英雄稳定事实增加新的、具有明确审计消费方的维度。
