# 用户经验来源摘要: BP 运行时索引应按版本语境编译

## 来源信息

- 类型：用户经验 / BP runtime 架构原则
- 日期：2026-07-02
- 上游 raw：[[../../raw/inbox/2026-07-02-user-note-bp-runtime-index-compilation.md]]
- 关联：[[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]]、[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/条件化对位模型|条件化对位模型]]、[[syntheses/BP-维护归档|BP 维护归档]]

## 核心观点

维护者认为，当前 BP skill 的运行结构不应长期依赖手写的“决策索引”页面。稳定 wiki 应只长期维护底层 BP 事实：英雄能力、build 条件、常见条件化对位、地图 hook、目标契约、失败条件、slot notes、地图结构和地图 BP 因素。

强度理解会随用户、社区、选手、赛季和补丁变化，不应写入英雄百科或稳定地图页。它应作为运行时输入或 profile，由 BP skill 与底层事实结合，临时编译出本次使用的 runtime BP index。

## 对 BP skill 的影响

BP skill 应拆成两个领域：

- `compile / understand-version`：读取稳定 wiki 事实和当前 strength profile，生成本次地图池 / 版本理解下的 runtime BP index。
- `decide`：只消费 runtime BP index，根据地图、ban/pick、slot 和 strategy bias 做 ban 或 pick 决策。

## 对现有索引页的影响

旧 `BP-条件化对位边索引` 与 `BP-英雄地图特征适配索引` 暴露了真正需要检索的关系，但它们混合了结构事实、slot 用途、候选提示和部分版本语境，不适合作为长期手写事实源。

后续更合理的形态是：这些关系从英雄页和地图页自动抽取，在 `compile` 阶段与 strength profile 结合，生成可丢弃、可重建的 runtime index。旧 Markdown 索引已按维护者确认删除；若需要审计，只能由脚本生成调试产物。
