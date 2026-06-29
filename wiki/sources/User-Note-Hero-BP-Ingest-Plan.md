# 用户经验来源摘要: 英雄 BP 建模 ingest 计划要求

## 来源信息

- 类型：用户经验 / 任务计划要求
- 日期：2026-06-29
- 上游 raw：[[../../raw/inbox/2026-06-29-user-note-hero-bp-ingest-plan.md]]
- 关联：[[syntheses/英雄BP建模覆盖审计|英雄 BP 建模覆盖审计]]、[[syntheses/英雄BP建模升级任务计划|英雄 BP 建模升级任务计划]]

## 核心要求

用户要求在当前会话只准备交接计划，不执行抓取或批量 ingest。计划必须覆盖当前 105 位英雄，而不是停留在本地已有的 72 个英雄页。

任务原则：

- 先保留原始信息，再做抽象和 ingest。
- Fandom 与 Power League Prodigy 的英雄详情页都应尽量各自摘录到 `raw/`。
- 英雄信息进入 BP 知识库时，必须说明它如何影响 BP 决策。
- 抽象层应沿用已有中间层：能力向量、build switch、map feature hook、objective contract、failure mode、conditional matchup seed、slot notes 和 candidate eval。
- 不新增没有明确消费方的粗字段，避免干扰 LLM 决策质量。

## 对计划文件的约束

- 必须能交接给另一个会话直接执行。
- 必须明确原始抓取、source 摘要、英雄实体页和跨页综合层的职责边界。
- 必须把 105 英雄 scope、缺口、执行批次和验收标准写清楚。
