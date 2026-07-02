# BP 英雄建模标准流程

状态：`maintenance_standard`。整理日期：2026-07-02。

本页定义新增英雄、重建英雄 BP profile、或批量修复英雄页时的标准流程。它替代已经完成的执行状态页、质量门槛页和质量审计页；这些页面不再作为长期 syntheses 维护。

## 适用场景

- 新增常驻英雄，需要进入 BP-active 英雄集合。
- 英雄机制、build、Hypercharge、Buffies 或关键能力发生定性变化。
- 批量重建 `wiki/entities/brawlers/` 下的 `bp_brawler_profile`。
- 审计发现英雄页含自动占位、未复核对位、地图 hook 假阳性或 slot notes 不足。

不适用：

- 只做当前版本强度榜或临时 tier list。
- 只记录普通数值微调且无法判断定性 BP 影响。
- 为临时、已下架或无有效来源覆盖的 roster 行创建 BP 概念。

## 输入边界

```text
raw/
  原始抓取事实，只读不改

wiki/sources/
  单来源摘要，保留 Fandom / PLP / 用户说明 / 版本公告的边界

wiki/entities/brawlers/
  英雄稳定 BP 字段，承载当前可消费模型

wiki/syntheses/
  只保留标准流程、schema、架构和跨来源结论，不保留批次进度看板
```

BP-active 英雄集合由当前有效来源覆盖和维护者确认的常驻范围决定，不通过命名排除维护。历史 roster 差异只保留在 raw/source 溯源中，不进入候选池、对位边、地图 hook 或运行时编译索引。

## 标准流程

1. 读取 `AGENTS.md`、[[index|Wiki Index]]、本页、[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/条件化对位模型|条件化对位模型]] 和 [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]。
2. 先保留 raw：Fandom 机制页、PLP 竞技页、版本公告、用户经验或赛事复盘都必须先进入 `raw/` 或已有 raw。
3. 写 source 摘要：Fandom 只作为稳定机制事实，PLP 只作为 build / mode / matchup 竞技信号，用户经验用于修正模型边界。
4. 更新英雄页稳定字段：只把能进入 BP 决策的内容写入 `capability_vector`、`build_switches`、`map_feature_hooks`、`objective_contracts`、`failure_modes`、`conditional_matchups` 和 `slot_notes`。
5. 接入地图事实：地图适配必须落到具体路线、位置、目标收益、失效条件和 slot 任务，不能只写 `open`、`closed`、`grass`、`water` 等粗标签。
6. 跑质量审计：用 `tools/audit_bp_profile_quality.py` 检查明显占位符、缺字段、来源追溯和 slot notes。审计结果默认输出到终端；需要落盘时写入 `outputs/bp-profile-quality-audit.md`，不要写回 `wiki/syntheses/`。
7. 人工/LLM 复核：脚本只能发现结构风险，不能替代机制判断。升级 `profile_status` 必须基于当前英雄页内容。
8. 更新导航和日志：只有新增长期页面或入口变化时更新 [[index|Wiki Index]]；每次批量维护都追加 [[log|Wiki Log]]。

## 质量状态

### draft_from_raw_signals

含义：从 Fandom / PLP raw 自动或半自动抽取出的候选结构。

允许：

- 存在 `pending`、`unknown`、`needs_review`。
- PLP matchup 只保留为原始候选信号。
- map hook 只有特征类型，尚未接入具体地图路线。

禁止：

- 被 BP 查询当作最终 counter、最终地图适配或稳定 pick 顺位依据。
- 被标记为 `bp_ready`。

### reviewed

含义：单英雄资料已经过人工/LLM 复核，可作为 BP 候选生成和初步 candidate_eval 的可靠输入。

验收：

- `capability_vector` 已复核，不能含自动抽取残留语句。
- 每个关键能力必须能追溯到 `wiki/sources/Fandom-*`、`wiki/sources/PLP-*` 或明确的用户/复盘来源。
- `build_switches` 至少有一个可用 build，并说明改变哪些能力、缓解哪些失败条件、何时差。
- `map_feature_hooks` 至少有两个可用 hook；每个 hook 必须说明路线/位置、目标收益、失效条件和 BP 用途。
- `objective_contracts` 不能只复制 PLP modes；必须说明在模式中能履行什么职责、不能履行什么职责、需要队友补什么。
- `failure_modes` 至少 3 条，且每条能进入 `must_avoid`、`false_positive_filter`、`needs_protection` 或 `terrain_state_plan_check`。
- `conditional_matchup_candidates` 可以仍是候选，但每组候选至少要写出机制类和激活/失效条件。
- `slot_notes` 必须区分 1、2-3、4-5、6 位任务与风险。

### bp_ready

含义：该英雄已经能进入高水平 BP 推理的可消费知识层。

验收：

- 满足 `reviewed` 的全部要求。
- 至少 3 条条件化对位边已进入英雄页 `conditional_matchups`，每条边都有 `mechanism / active_when / fails_when / bp_use`。
- 至少 3 条地图适配 hook 已接入英雄页 `map_feature_hooks` 或 Ranked 单地图实体页，必须包含具体地图、路线/位置、目标收益和失效条件。
- 至少一个模式目标契约能进入 `candidate_eval.mode_fit`。
- 至少一个失败条件能进入 `must_avoid` 或 `false_positive_check`。
- 不含自动草案占位词：`pending`、`unknown_pending`、`needs_review`、`candidate_only_not_final`、`not_inferred_from_source` 等。

`bp_ready` 不是“永远强”或“无条件推荐”。它只表示资料结构足以让 BP DSL 在具体局面中判断是否选、禁、规避或要求队友保护。

## 审计输出

质量审计建议输出为临时报告：

```yaml
bp_profile_quality_audit:
  brawler:
  current_status:
  target_status:
  blockers:
    - blocker_type:
      evidence:
      required_fix:
  can_upgrade_to_reviewed:
  can_upgrade_to_bp_ready:
```

常见 blocker：

- `auto_placeholder`
- `missing_mechanism`
- `missing_map_route_or_objective`
- `missing_failure_modes`
- `missing_slot_specificity`
- `unreviewed_matchup_candidate`
- `unreviewed_build_delta`
- `source_traceability_gap`

## 产物治理

- 不在 `wiki/syntheses/` 新建批次进度页、执行状态页或一次性质量审计页。
- 完成态数字写入 `wiki/log.md`；可复用规则更新本页；历史经验归入 [[syntheses/BP-维护归档|BP 维护归档]]。
- 不恢复手写运行时对位索引或地图 hook 索引；这些应由 future `bp compile` 生成临时产物。
- 版本强度和临时 meta 不写入英雄页；只有定性改变能力语义、对位成立条件、地图 hook 或 slot 策略时，才更新稳定字段。

## 关联页面

- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- [[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]]
- [[syntheses/BP-维护归档|BP 维护归档]]
