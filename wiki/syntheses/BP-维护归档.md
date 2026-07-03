# BP 维护归档

状态：`maintenance_archive`。整理日期：2026-07-02。

本页归并已经完成、被标准流程吸收、或被新架构取代的 BP 维护任务页。它不是 BP 运行时入口；正式 BP 推演仍应读取 [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/条件化对位模型|条件化对位模型]]、[[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]]、地图页和英雄页。

## 本次整理结论

本次在 `wiki/syntheses/` 中识别出的已完成维护任务页均已归并，原文件已删除：

| 原页面 | 原作用 | 归并判断 | 当前替代入口 |
| --- | --- | --- | --- |
| 英雄 BP 建模覆盖审计 | 2026-06-29 审计 72 个旧英雄页是否能支撑 BP DSL。 | 旧缺口已被 104 个 BP-active 英雄全量 `bp_ready` 结果取代。 | [[syntheses/BP-英雄建模标准流程|BP 英雄建模标准流程]] |
| 英雄 BP 建模升级任务计划 | 2026-06-29 的批量抓取、source 摘要和 BP profile 升级交接计划。 | 批量任务已完成；可复用规则已沉淀到标准流程。 | [[syntheses/BP-英雄建模标准流程|BP 英雄建模标准流程]] |
| 英雄 BP 建模进度审计 2026-06-30 | 记录批次推进和旧索引进度。 | 进度已经收敛为 104 个 `bp_ready`、无 draft 队列；旧手写索引也已删除。 | [[syntheses/BP-英雄建模标准流程|BP 英雄建模标准流程]] |
| BP 实战查询速度与模型形态评估 | 评估 skill / 检索 / 微调的运行形态。 | 核心结论已被 compile-first 架构吸收；旧手写索引假设已失效。 | [[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]] |
| 英雄 BP 建模执行状态 | 记录 104 个 BP-active 英雄完成状态、旧索引快照和最终批次。 | 是完成态看板，不应长期作为 syntheses 入口。 | [[syntheses/BP-英雄建模标准流程|BP 英雄建模标准流程]] |
| 英雄 BP 建模质量门槛 | 定义 `draft_from_raw_signals` / `reviewed` / `bp_ready` 质量标准。 | 可复用内容已合入标准流程。 | [[syntheses/BP-英雄建模标准流程|BP 英雄建模标准流程]] |
| 英雄 BP 建模质量审计 | 由脚本生成的一次性结构审计报告。 | 应作为临时输出而不是长期 wiki 页面。 | `outputs/bp-profile-quality-audit.md` |

另外 2 个非运行时页面保留为独立归档，而不是本次删除：

- [[syntheses/2026-06-30版本BP影响评估|2026-06-30 版本 BP 影响评估]]：来源驱动的版本审计，仍可解释 June 2026 patch 哪些内容只是观察项，哪些可能改变稳定 BP 字段。
- [[syntheses/BP-模拟样本关键结论汇总|BP 模拟样本关键结论汇总]]：模拟样本 digest，不是运行时事实源，但可用于回看裁判 / 选手 skill 的输出问题。

## 保留的关键结论

- 当前 BP-active scope 是 104 个有有效来源覆盖的常驻英雄；历史临时或无有效来源覆盖的 roster 行只保留在 raw/source 溯源中，不进入 BP 概念集合。
- 104 个 BP-active 英雄均已有 Fandom / PLP source 摘要与 `bp_brawler_profile`，当前结构状态为 `profile_status: bp_ready`。
- 批量建模流程的有效部分是：先保留 raw，再写 source 摘要，再更新英雄页稳定 BP 字段，最后跑质量审计和更新日志。
- `bp_ready` 只表示结构可被 BP DSL 消费，不表示英雄在当前版本强。
- 版本强度、临时 meta、赛事观察和补丁影响必须先进入来源页、审计页或日志；只有产生定性 BP 影响时，才直接更新英雄页或地图页的稳定字段。
- 实战 BP 不应把可变事实微调进模型；更合适的形态是 `skill + 本地检索 / 编译索引 + 小范围候选评估`。

## 后续维护规则

- 新增英雄或大批量重建时，不恢复旧任务页；直接按 [[syntheses/BP-英雄建模标准流程|BP 英雄建模标准流程]] 执行。
- 质量检查继续通过 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py` 运行；需要落盘时生成 `outputs/bp-profile-quality-audit.md`，不写入 `wiki/syntheses/`。
- 如果未来实现 `bp compile`，编译产物应写到运行输出或 debug artifact，不写回长期 `wiki/syntheses/` 手写索引页。

## 关联页面

- [[syntheses/BP-英雄建模标准流程|BP 英雄建模标准流程]]
- [[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]]
- [[sources/User-Note-Hero-BP-Ingest-Plan|用户经验来源摘要: 英雄 BP 建模 ingest 计划要求]]
