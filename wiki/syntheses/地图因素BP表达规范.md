# 地图因素 BP 表达规范

这页定义地图因素如何进入 Ban Pick 决策。它建立在 [[syntheses/地图特征建模Schema|地图特征建模 Schema]] 和 26 张 `bp_map_profile_v2` 地图实体页之上。

核心判断：BP 不直接消费“这张图有水 / 有草 / 有墙”。BP 消费的是地图制造出的职责、路线、目标访问、地形状态、反制窗口和假阳性陷阱。

## 从地图特征到 BP 因素

`map_feature` 是稳定地形事实，`map_bp_factor` 是当前 BP 会用到的决策信号。

```yaml
map_bp_factor:
  id:
  source_map_feature_id:
  factor_class:
    - objective_access
    - route_gate
    - space_control
    - terrain_transform
    - vision_tax
    - congestion_punish
    - scoring_window
    - survival_space
    - split_duty
    - last_pick_trap

  active_when:
    map_state:
    draft_state:
    enemy_plan:
    own_plan:

  creates_draft_obligation:
    must_cover_duty:
    must_answer_if_enemy_uses:
    must_avoid_exposing:

  rewards_capabilities:
  punishes_capabilities:
  false_positive_capabilities:

  slot_sensitivity:
    slot_1:
    slot_2_3:
    slot_4_5:
    slot_6:

  bp_output_use:
    required_capabilities:
    candidate_eval_questions:
    ban_reason:
    pick_reason:
    avoid_reason:
```

也就是说，地图页里的 `tactical_features` 不应直接等于“推荐英雄”。它们应先转成当前局面的 BP 因素，再进入候选评估。

## 五层地图决策模型

完整 BP 中，地图因素应按五层读取。

```yaml
map_decision_model:
  1_objective_contract:
    asks:
      - 这张图如何把模式目标转成具体赢法？
      - 哪些职责是非做不可？
      - 哪些优势可以直接转成得分、金库伤害、宝石安全、星差或站圈时间？

  2_route_and_position_graph:
    asks:
      - 哪些路线能进入目标区？
      - 哪些路线被墙、草、水、窄口或长线火力限制？
      - 哪些能力能绕过路线成本？
      - 哪些位置是低承诺输出点或持续生存锚点？

  3_terrain_state_and_transform:
    asks:
      - 墙体、草丛、球门、热区入口、金库屏障当前是 intact 还是 opened / cleared？
      - 开墙、烧草、探草、破门会让地图转向哪类英雄？
      - 这个变化更利于我方还是敌方？

  4_duty_coverage:
    asks:
      - 我方已覆盖哪些地图职责？
      - 敌方已暴露哪些地图计划？
      - 当前 slot 最需要补职责、抢路线、保护核心，还是惩罚敌方结构？

  5_false_positive_filter:
    asks:
      - 候选看似命中地图标签，是否真的能把能力转成目标收益？
      - 是否需要队友前置条件？
      - 是否会被敌方剩余 slot 低成本回答？
```

这五层比 `open / closed / water` 更适合 BP，因为它们能直接变成 `required_capabilities`、`must_answer`、`must_avoid` 和 `candidate_eval`。

## 模式化的地图职责

从 26 张地图抽象后，地图职责可以按模式分组表达。

```yaml
map_duties_by_mode:
  Heist:
    objective_contract:
      - safe_access
      - sustained_safe_dps
      - route_to_safe_or_remote_angle
      - defend_enemy_entry_route
    recurring_factors:
      - long_range_safe_damage
      - wall_break_to_create_safe_angle
      - throw_arc_safe_damage
      - water_or_jump_entry
      - base_corner_anchor
      - lane_duel_into_safe_pressure

  Brawl_Ball:
    objective_contract:
      - ball_control
      - scoring_window
      - goal_geometry_management
      - anti_scorer_defense
    recurring_factors:
      - wall_break_for_goal
      - trickshot_wall_value
      - grass_control_for_ball
      - dash_or_knockback_score
      - overtime_or_open_field_transition

  Hot_Zone:
    objective_contract:
      - zone_presence
      - zone_clear
      - zone_sustain
      - split_zone_duty_if_two_zones
    recurring_factors:
      - area_denial
      - body_on_zone
      - protected_turret_or_support_anchor
      - far_zone_rotation
      - anti_thrower_or_wallbreak_clear

  Gem_Grab:
    objective_contract:
      - gem_mine_access
      - gem_carrier_safety
      - side_pressure_to_protect_mid
      - countdown_retreat_or_comeback_route
    recurring_factors:
      - bush_scouting
      - mid_survivability
      - entrance_blocking
      - flank_pressure
      - retreat_anchor_break

  Bounty:
    objective_contract:
      - low_commitment_star_gain
      - survival_after_lead
      - break_lead_when_behind
      - deny_thrower_or_short_range_cover
    recurring_factors:
      - long_sightline
      - wall_break_snowball
      - thrower_pocket_if_walls_intact
      - retreat_layer
      - forced_engage_only_as_last_pick

  Knockout:
    objective_contract:
      - space_control
      - survival_space
      - final_engage_window
      - answer_wall_or_thrower_control
    recurring_factors:
      - thrower_pocket
      - wall_break_transform
      - route_based_assassin
      - water_or_jump_reposition
      - last_pick_no_peel_punish
```

模式职责是 BP 的第一层过滤。某英雄即使对线很强，如果不能参与本模式的地图职责，也不能被判为地图强适配。

## 地形状态要显式建模

许多地图不是固定形态，而是会在局内或 BP 中被某些能力改写。

```yaml
terrain_state:
  walls:
    state: intact | opened | selectively_opened | overbroken
    favors_when_intact:
      - thrower_pocket
      - bounce_wall
      - short_range_approach
      - retreat_layer
    favors_when_opened:
      - marksman_range
      - long_range_safe_damage
      - anti_thrower_angle
    bp_question: 我方是需要保墙，还是需要主动开墙？

  grass:
    state: intact | swept | burned | controlled_by_us | controlled_by_enemy
    favors_when_intact:
      - bush_flank
      - speed_gear
      - ambush
      - gem_carrier_hide
    favors_when_removed:
      - pure_range
      - safe_carrier_visibility
      - anti_tank_control
    bp_question: 当前阵容有没有支付视野税？

  goal_geometry:
    state: closed | opened | trickshot_enabled | overopened
    bp_question: 破门会创造我方进球窗口，还是帮敌方远程接管？

  zone_control:
    state: neutral | controlled_by_us | controlled_by_enemy
    bp_question: 我方缺站圈身体、清圈能力，还是缺翻圈工具？

  objective_route:
    state: open | gated | bypassable | denied
    bp_question: 候选能否真实接触目标，而不是只“看起来适配”？
```

这层能解释为什么同一张图上“开墙”有时是答案，有时是自杀；为什么草丛图不等于无脑坦克；为什么水图不等于所有过水英雄都强。

## 地图硬门槛

地图因素进入 `hard_gate_result` 的规则：

```yaml
map_hard_gate_rules:
  must_pick:
    trigger:
      - 某英雄低成本覆盖地图非做不可职责
      - 该职责在当前可用池中稀缺
      - 放给对手后没有稳定 answer
    examples:
      - Heist 图上的稳定 safe_access + safe_dps
      - Brawl Ball 图上的破门 + 得分窗口
      - Hot Zone 图上的站圈 + 区域清除

  must_answer:
    trigger:
      - 敌方已选英雄激活关键地图路线或地形锚点
      - 如果不回答，会直接转化为目标收益
    examples:
      - 投掷占住墙后口袋
      - 远程 safe angle 无人处理
      - 双圈图远圈无人能打断

  must_ban:
    trigger:
      - 某英雄会低成本拆毁我方地图主计划
      - 或某英雄能独占地图关键职责且我方无 answer
    examples:
      - 我方计划依赖墙体，敌方开墙英雄会直接改图
      - 我方缺探草，敌方草丛进攻能持续威胁核心

  must_avoid:
    trigger:
      - 候选命中粗标签，但无法完成目标转换
      - 或会被敌方剩余 slot 通过地图因素一手惩罚
    examples:
      - water_crossing_without_range_or_anchor
      - sniper_that_cannot_step_on_zone
      - thrower_without_peel_or_safe_angle
      - wall_break_without_followup
```

## Slot 视角下的地图任务

地图因素必须随 pick 顺位改变权重。

```yaml
map_slot_policy:
  slot_1:
    map_job:
      - 抢稳定、可延展、低假阳性的地图职责
      - 覆盖至少一个非做不可职责
      - 不把阵容锁死在容易被 2-3 位回答的单一地形状态
    prefer:
      - 跨地形状态仍有价值
      - 能打目标，也能保基本面
      - 被反制条件窄

  slot_2_3:
    map_job:
      - 一手回答敌方 1 位激活的地图因素
      - 一手建立己方地图胜利路线
      - 制造 4-5 位同时处理多个地图职责的压力
    avoid:
      - 两手共享同一个地图弱点
      - 只防守但没有目标转换

  slot_4_5:
    map_job:
      - 补完己方地图职责覆盖
      - 回答敌方 2-3 位成组激活的路线或地形状态
      - 不把不可修复的地图破口留给 6 位
    check:
      - 是否缺 vision / wallbreak / zone body / scoring window / safe DPS
      - 是否会被最后手刺客、投掷、开墙或高机动一手贯穿

  slot_6:
    map_job:
      - 惩罚敌方无法再修复的地图职责缺口
      - 利用已锁定的地形状态做高上限选择
      - 选择 aggressive pick 只在敌方没有后续 answer 时成立
    examples:
      - 敌方无探草，选草丛绕后或伏击
      - 敌方无开墙，选投掷口袋
      - 敌方无 anti-aggro，选路线明确的突进
      - 敌方无基地清理，选持续入侵 / 角落锚点英雄
```

## 候选地图适配评估

每个候选都应被问一组固定问题。

```yaml
candidate_map_factor_eval:
  candidate:
  map_duties_covered:
    - duty:
      quality: primary | secondary | emergency
      proof:

  activated_map_bp_factors:
    - factor_id:
      how_candidate_uses_it:
      required_build:
      required_teammate_support:
      enemy_counterplay:

  objective_conversion:
    can_convert_to:
      - safe_damage
      - goal_window
      - zone_time
      - gem_security
      - star_lead
      - knockout_space
    required_commitment:
    failure_if:

  terrain_state_dependency:
    strong_when:
    weak_when:
    can_transform_state:

  false_positive_check:
    looks_good_because:
    actually_fails_if:
    verdict: real_fit | conditional_fit | false_positive

  slot_fit:
    safe_as_slot_1:
    good_as_response:
    good_as_last_pick:
    exposure_risk:
```

这个结构能直接回答用户前面提出的 Brock / Mortis / Cordelius 问题：静态 counter 必须被地图路线、接近成本、地形状态和 slot 信息重新过滤。

## 常见假阳性库

这些是 26 张地图里反复出现的陷阱。

```yaml
map_false_positive_library:
  water_crossing:
    false_if:
      - crossing_without_range
      - crossing_without_anchor
      - crossing_without_objective_pressure
    question: 过水后能否打到目标、站住或迫使回防？

  wall_break:
    false_if:
      - overbreak_helps_enemy_range
      - no_followup_after_opening
      - our_comp_needs_walls
    question: 开墙后谁更受益？

  thrower_pocket:
    false_if:
      - no_peel
      - enemy_has_easy_dive
      - walls_can_be_broken
      - cannot_touch_objective
    question: 投掷能否低风险影响目标，而不只是打墙后伤害？

  grass_aggro:
    false_if:
      - enemy_has_constant_sweep
      - grass_can_be_burned
      - no_exit_after_failed_flank
      - no_ball_or_objective_followup
    question: 草丛路线是否能转成击杀、进球、宝石安全或站圈？

  sniper_range:
    false_if:
      - cannot_step_zone
      - cannot_check_bush
      - projectile_unreliable_into_mobility
      - side_wall_or_thrower_unanswered
    question: 长手是否能服务当前模式目标？

  assassin_counter:
    false_if:
      - no_route
      - single_predictable_choke
      - target_has_peel
      - map_is_long_open
    question: 贴脸是否是地图给出的路线，而不是名字上的 counter？
```

## BP 输出中的地图因素写法

推荐在每轮 BP 输出里新增 `map_factor_summary`。

```yaml
map_factor_summary:
  active_objective_contract:
    - 当前地图把模式目标转成什么赢法

  active_map_bp_factors:
    - id:
      source_feature:
      bp_relevance:
      current_owner: us | enemy | neutral | unknown
      urgency: hard_gate | core_duty | must_answer_route | plan_protection | slot_trap | conditional_opportunity | low_relevance

  duty_coverage:
    covered:
    missing:
    overexposed:

  terrain_state_plan:
    keep:
    transform:
    deny_enemy_transform:

  false_positive_alerts:
    - candidate_or_plan:
      why_it_looks_good:
      why_it_may_fail:
```

如果一个 BP 回答没有这一层，它很容易退化成“地图强势英雄列表”，而不是高水平 draft 推理。

## 关联页面

- [[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- [[syntheses/地图知识分层治理|地图知识分层治理]]
- [[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- [[sources/User-Note-Map-Factor-BP-Expression|用户经验来源摘要: 地图因素需要 BP 决策表达]]
