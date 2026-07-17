# 用户维护规则：平衡调整伤害—生存断点审计

## 来源信息

- 来源：知识库维护者在 2026-07-17 提供的审计规则与本轮执行要求
- 上游 raw：[[../../raw/inbox/2026-07-17-user-note-balance-breakpoint-audit|2026-07-17 user note]]
- source_quality：maintainer_provided_domain_rule
- source_type：calculation_semantics / maintenance_requirement

## 可用范围

- usable_for: Shield gear 满值 `+900`、不同减伤 buff 加法叠加、EHP 换算、平衡补丁前后击杀线差分、维护流程设计
- not_usable_for: 单独证明某英雄强弱、无条件 counter、实际命中率、距离与散射条件、游戏内部整数舍入顺序、未核验的技能数值

## 已采纳的计算语义

- 基础目标状态使用英雄当前本体血量。
- 通用 Shield gear 的满值状态作为 `flat_shield = 900`；它是条件化满盾状态，不代表交战中始终存在。
- 同时生效且允许叠加的不同减伤 buff 按维护者规则加法合并：`total_damage_reduction = sum(reductions)`。
- 用于比较离散击杀线的有效血量为：`EHP = (base_health + flat_shield) / (1 - total_damage_reduction)`。
- 伤害包所需命中次数使用精确分数比较；只有攻击包已明确伤害单位、命中数、形态、距离或构筑条件时才可计算。

## 证据边界

- 本规则定义“怎么算”，不替 Fandom、官方补丁或英雄机制页证明“技能当前是多少”。
- `+900`、加法叠加与 EHP 公式后续仍可用官方或可复核游戏机制来源交叉核验；发现冲突时必须保留冲突，不能静默改公式。
- 下一击减伤、随时间衰减护盾、治疗、复活、百分比生命伤害、距离连续缩放、多弹散射和持续伤害不能自动压成普通单发。
- 断点变化只能生成 maintainer review evidence；不能自动生成 strength tier、地图适配、稳定对位边或 runtime 推荐。

## 本轮关联来源

- [[sources/Fandom-Release-Notes-June-2026|Release Notes June 2026]]
- [[sources/Fandom-Maintenance-July-8-2026|Maintenance - July 8, 2026]]
- [[concepts/伤害与生存断点|伤害与生存断点]]
