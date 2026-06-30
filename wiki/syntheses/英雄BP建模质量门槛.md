# 英雄 BP 建模质量门槛

本页定义 `bp_brawler_profile.profile_status` 从 `draft_from_raw_signals` 升级到 `reviewed` / `bp_ready` 的验收标准。它是 [[syntheses/英雄BP建模升级任务计划|英雄 BP 建模升级任务计划]] 的执行质量门槛。

## 状态定义

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

- `capability_vector` 已复核，不能含自动抽取残留语句，例如 `needs_review`、`unknown_pending_review`、`not_observed_in_selected_raw` 作为主要结论。
- 每个关键能力必须能追溯到 [[sources/Fandom-*]] 或明确的用户/复盘来源。
- `build_switches` 至少有一个可用 build，并说明改变哪些能力、缓解哪些失败条件、何时差。
- `map_feature_hooks` 至少有两个可用 hook；每个 hook 必须说明路线/位置、目标收益、失效条件和 BP 用途。
- `objective_contracts` 不能只复制 PLP modes；必须说明在模式中能履行什么职责、不能履行什么职责、需要队友补什么。
- `failure_modes` 至少 3 条，且每条能进入 `must_avoid`、`false_positive_filter`、`needs_protection` 或 `terrain_state_plan_check`。
- `conditional_matchup_candidates` 可以仍是候选，但每组候选至少要写出机制类和激活/失效条件，不得停留在 `mechanism: pending`。
- `slot_notes` 必须区分 1、2-3、4-5、6 位任务与风险，不能只写通用模板句。

reviewed 仍不是最终 BP 结论。它表示英雄页能被 BP DSL 安全读取，但具体对局仍必须结合地图、模式、ban/pick 和 slot。

### bp_ready

含义：该英雄已经能进入高水平 BP 推理的可消费知识层。

验收：

- 满足 `reviewed` 的全部要求。
- 至少 3 条条件化对位边已进入 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]] 的 reviewed 区或英雄页内等价结构，每条边都有 `mechanism / active_when / fails_when / bp_use`。
- 至少 3 条地图适配 hook 已接入 Ranked Season 46 单地图实体或 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]] 的 reviewed 区，必须包含具体地图、路线/位置、目标收益和失效条件。
- 该英雄至少有一个模式目标契约能进入 `candidate_eval.mode_fit`，且至少一个失败条件能进入 `must_avoid` 或 `false_positive_check`。
- 不含自动草案占位词：`pending`、`unknown_pending`、`needs_review`、`candidate_only_not_final`、`PLP mode fit is only a candidate`、`not_inferred_from_source`。

bp_ready 不是“永远强”或“无条件推荐”。它只表示资料结构足以让 BP DSL 在具体局面中判断是否选、禁、规避或要求队友保护。

## 批量升级原则

- 可以批量审计，不能批量宣称 `bp_ready`。
- 可以用脚本发现占位词、缺字段和断链；升级状态必须依据当前页面内容。
- 自动抽取产生的 map hook 必须复核。例如 `water_crossing_or_obstacle_bypass` 不能只因为 Fandom raw 出现 `water` 就成立。
- PLP `countersThese` / `counteredBy` 只能提供边候选，不能直接升级为 reviewed 对位边。
- 版本强度、临时 meta 和赛事复盘应先进入来源页、审计页或日志；只有产生定性 BP 影响时，才内联更新稳定字段。

## 审计输出

质量审计应输出：

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

阻塞类型建议：

- `auto_placeholder`
- `missing_mechanism`
- `missing_map_route_or_objective`
- `missing_failure_modes`
- `missing_slot_specificity`
- `unreviewed_matchup_candidate`
- `unreviewed_build_delta`
- `source_traceability_gap`

## 关联页面

- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/英雄BP建模覆盖审计|英雄 BP 建模覆盖审计]]
- [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]
- [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]
- [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]
