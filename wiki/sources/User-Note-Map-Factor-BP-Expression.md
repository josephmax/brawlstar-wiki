# 用户经验来源摘要: 地图因素需要 BP 决策表达

## 来源信息

- 类型：用户经验 / 建模需求
- 日期：2026-06-29
- 上游 raw：[[../../raw/inbox/2026-06-29-user-note-map-factor-bp-expression.md]]
- 关联专题：[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]

## 摘要

在 26 张 Ranked Season 46 地图实体页已经升级为 `bp_map_profile_v2` 后，维护者提出下一层要求：地图知识不能只记录“这张图有什么特征”，还要明确这些特征如何进入 BP 决策。

核心问题是：

- 地图特征如何变成当前 draft 的职责缺口？
- 哪些地图因素会触发 `must_pick`、`must_ban`、`must_answer` 或 `must_avoid`？
- 某个英雄看似适配地图时，哪些条件会让它变成假阳性？
- 不同 pick slot 应该如何承担地图任务或避免留下 last pick 破口？

## 本地 wiki 的处理

本条经验沉淀到 [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]，并反向接入：

- [[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]

## 使用边界

这不是单张地图事实，也不是版本 meta 结论；它是地图因素进入 BP 推理的表达规范。
