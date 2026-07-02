# 用户经验来源摘要: BP Schema 奥卡姆剃刀

## 来源信息

- 类型：用户经验 / schema 治理原则
- 日期：2026-06-29
- 上游 raw：[[../../raw/inbox/2026-06-29-user-note-bp-schema-occam.md]]
- 关联：[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]

## 核心观点

用户强调：BP schema 中的任何新增信息都可能帮助 LLM，也可能成为噪声。既然当前决策层已经拆成地图因素、能力、路线、目标收益、假阳性和 slot 任务，粗粒度 `summary_tags` 不能提供可靠判断，反而可能干扰决策质量。

因此，schema 字段必须有明确消费方。不能说明自己如何进入 `hard_gate`、`required_capabilities`、`map_bp_factors`、`candidate_eval` 或输出解释的字段，不应进入 Canonical Input。

## 已采纳规则

- `summary_tags` 从 BP 可消费的 `map_profile` 中移除。
- `high | medium | low` 不再用于 `map_bp_factors.urgency` 这类决策层字段。
- 若未来需要检索或 UI 筛选索引，应放在 BP 输入之外，并明确不得参与候选排序、理由生成或 hard gate 判断。

## 对 BP 建模的影响

地图因素应继续落到：

- 具体路线或站位
- 目标收益
- 失效条件
- 需要承担的模式职责
- 当前 slot 的风险与机会
- 对候选英雄的假阳性过滤

粗标签只能作为被淘汰的过渡表达，不应成为另一个 LLM 的推理依据。
