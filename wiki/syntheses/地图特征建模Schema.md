# 地图特征建模 Schema

这页定义 BP 推理中更细粒度的地图表达。它补充 [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]] 中的 `map_profile`，用于把地图从粗略标签升级为“地形模块、行动路线、目标访问和英雄能力交互规则”。

核心原则：地图不是 `open` 或 `closed`，而是会把某些英雄能力转化为路线、站位、目标输出、局部生存或反制压力的一组条件。

2026-06-29 二次升级后，本页负责定义“地图如何结构化”；地图因素如何进一步进入每一手 BP 决策，见 [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]。

## 为什么粗分档不够

`openness: mixed`、`water_value: high` 这类字段只能提示方向，不能支持 BP 判断。

真正影响 draft 的问题通常更具体：

- 这条河道是阻止普通英雄出家门，还是给可过水英雄打开绕后路线？
- 远程英雄能否不越过危险区就打到目标？
- 可过水但手短的英雄过河后有没有持续站住的位置？
- 中路拥挤时，哪些弹道、召唤物、连锁、穿透或直线压制机制会升值？
- 金库旁的墙角、弹墙、草丛或障碍，是否能让某类英雄反复存活并制造目标压力？

因此地图 schema 应表达“能力 -> 路线 -> 收益 -> 失效条件”，而不是只表达地图整体长什么样。

2026-06-29 修正：`summary_tags` 不再属于 BP 可消费的 `map_profile`。如果未来需要搜索或 UI 筛选索引，也必须放在 BP 输入之外，且不能参与候选排序、理由生成或 hard gate 判断。字段进入 schema 前必须有明确消费方；否则按奥卡姆剃刀原则删除，避免给 LLM 增加噪声。

## map_profile 总体结构

```yaml
map_profile:
  name:
  mode:

  topology:
    zones:
      - id:
        owner_at_start: our_side | enemy_side | neutral | contested
        strategic_value:
    lanes:
      - id:
        connects:
        default_role:
        pressure_direction:
        rotation_cost:
    barriers:
      - id:
        type: river | wall | unbreakable_wall | choke | grass | open_gap
        separates:
        bypassed_by_capabilities:
    routes:
      - id:
        from:
        to:
        requires_capabilities:
        denies_capabilities:
        risk:
        payoff:

  objective_access:
    objective_type: safe | gem_mine | goal | zone | bounty_star | knockout_space
    direct_damage_lanes:
      - id:
        from_zone:
        requires_capabilities:
        example_brawlers:
        risk:
        counterplay:
    base_entry_routes:
      - id:
        route_ref:
        requires_capabilities:
        required_survival_after_entry:
        payoff:
        failure_modes:

  tactical_features:
    - id:
      type: river_crossing | long_sightline | lane_funnel | central_congestion | base_corner | bounce_wall | grass_anchor | thrower_pocket
      location:
      condition:
      enables:
      rewards_capabilities:
      punishes_capabilities:
      false_positive_capabilities:
      example_brawlers:
      draft_implication:

  lane_dynamics:
    default_lane_assignment:
    congestion_triggers:
    split_pressure_value:
    rotation_punishers:
    grouping_punishers:

  map_rules:
    - if:
      then:
      because:
      bp_use:
```

真正参与 BP 的是 `topology`、`objective_access`、`tactical_features`、`lane_dynamics` 和 `map_rules`。粗粒度摘要不进入 `map_profile`，因为它既不能直接回答“当前 draft 缺什么”，也不能证明某个英雄能把地形转化为目标收益。

## 从 map_feature 到 map_bp_factor

26 张 Ranked Season 46 地图升级为 `bp_map_profile_v2` 后，可以看到一个稳定规律：`map_feature` 仍然偏“地图事实”，而 BP 需要的是“地图事实在当前 draft 中制造了什么义务或机会”。

因此，本 schema 后续应区分两层：

```yaml
map_feature:
  purpose: 记录稳定地图结构
  example:
    - river_crossing
    - thrower_pocket
    - goal_barrier
    - lane_funnel
    - wall_break_transform

map_bp_factor:
  purpose: 记录当前 BP 可直接消费的地图决策信号
  derived_from:
    - map_feature
    - mode_objective_profile
    - draft_state
    - terrain_state
  outputs:
    - required_capabilities
    - map_duties
    - must_answer
    - must_avoid
    - candidate_map_factor_eval
```

完整表达见 [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]。最小转换规则是：

```yaml
map_feature_to_bp_factor:
  map_feature:
    id:
    route_or_position:
    objective_payoff:
    failure_condition:
  map_bp_factor:
    active_when:
    creates_draft_obligation:
    slot_sensitivity:
    false_positive_filter:
    bp_output_use:
```

例如 `wall_break_transform` 作为地图特征，只说明“开墙会改变地图”。进入 BP 时必须继续问：

- 我方需要保墙，还是需要开墙？
- 开墙后谁的射程、目标访问或生存更受益？
- 当前 slot 是否还允许对手补远程或突进来利用开墙结果？
- 候选开墙是否有后续目标转换，否则是不是 `wall_break_without_followup`？

## map_feature 对象

每个具体地形都应写成可激活的 `map_feature`。

```yaml
map_feature:
  id:
  type:
  location:
  condition:
  route_effect:
    opens_routes_for:
    closes_routes_for:
    bypass_capabilities:
    rotation_cost_change:
  combat_effect:
    rewards_capabilities:
    punishes_capabilities:
    false_positive_capabilities:
  objective_effect:
    enables_objective_pressure:
    enables_safe_positioning:
    required_followup:
  draft_implication:
    raises_pick_value:
    lowers_pick_value:
    creates_must_answer:
    creates_ban_reason:
  examples:
    works_well:
    conditional:
    traps:
```

这里最关键的是 `false_positive_capabilities`。它用来记录“看似满足地图条件，但实际收益不足”的能力组合。例如“可过水”在某些图上很有价值，但如果英雄手短、过河后没有生存锚点，也可能只是把自己送进敌方基地附近坐牢。

## Safe Zone 示例

下面不是完整地图数据，而是说明这类信息应如何被抽象。

```yaml
map_profile:
  name: Safe Zone
  mode: Heist

  tactical_features:
    - id: river_barrier_to_enemy_base
      type: river_crossing
      location: between_mid_and_enemy_base
      condition: 河道会限制普通英雄直接进入敌方基地附近
      route_effect:
        opens_routes_for:
          - water_crossing
          - long_jump_or_wall_bypass
        closes_routes_for:
          - normal_walk_short_range_without_control
        bypass_capabilities:
          - water_crossing
          - jump
          - teleport_or_dash_if_route_exists
      combat_effect:
        rewards_capabilities:
          - water_crossing_with_range
          - water_crossing_with_survivability
          - water_crossing_with_objective_pressure
        false_positive_capabilities:
          - water_crossing_short_range_without_base_anchor
      objective_effect:
        enables_objective_pressure: 过河后可直接威胁金库或牵制防守
        required_followup: 需要能站住、能打到目标，或能迫使敌方回防
      draft_implication:
        raises_pick_value:
          - Angelo
          - Eve
        lowers_pick_value:
          - 只有过水但缺少射程、生存或目标压力的候选

    - id: remote_safe_damage_angles
      type: long_sightline
      location: mid_to_enemy_safe
      condition: 部分远程或特殊弹道英雄不必过河也能对金库施压
      combat_effect:
        rewards_capabilities:
          - long_range_safe_damage
          - throw_arc_safe_damage
          - safe_pressure_from_low_commitment_position
      objective_effect:
        enables_objective_pressure: 不进入敌方基地也能造成金库伤害
        required_followup: 需要弹道能稳定命中或迫使敌方离开中路
      draft_implication:
        raises_pick_value:
          - Grom

    - id: mid_congestion_if_enemy_does_not_split
      type: central_congestion
      location: mid_lane
      condition: 敌方没有进行有效分路，导致中路人数密度提高
      combat_effect:
        rewards_capabilities:
          - chain_damage
          - line_pierce
          - turret_or_pet_pressure
          - long_linear_control
          - mark_or_bounce_value
        punishes_capabilities:
          - single_target_low_area_pressure
      draft_implication:
        raises_pick_value:
          - Jessie
          - Belle
          - Mandy
          - 用户例子: 皮尔斯

    - id: enemy_safe_corner_anchor
      type: base_corner
      location: near_enemy_safe
      condition: 过河后可利用墙角或基地附近地形反复生存
      combat_effect:
        rewards_capabilities:
          - wall_bounce_damage
          - jump_cycle
          - area_sustain
          - close_range_survival_with_escape_pattern
      objective_effect:
        enables_safe_positioning: 能在敌方基地附近持续牵制或输出
      draft_implication:
        raises_pick_value:
          - Mico
          - Rico
          - Berry
```

这个例子表达的不是“Safe Zone 等于水图，所以选所有会过水的英雄”，而是：

- 可过水打开的是路线，不自动等于高价值。
- 远程目标访问可以绕过路线问题。
- 中路拥挤会让惩罚密集站位的机制升值。
- 基地角落能把某些英雄的入侵从一次性突进变成持续压力。

## 候选地图适配输出

评估某个英雄时，`map_fit` 不应只写 `good` 或 `bad`，而应拆成：

```yaml
map_fit:
  activated_features:
    - map_feature_id:
      how_candidate_uses_it:
  enabled_routes:
    - route_id:
      required_capability:
      payoff:
  objective_access:
    can_pressure_objective_from:
    required_commitment:
    counterplay:
  false_positive_risks:
    - looks_good_because:
      actually_fails_if:
  required_support:
    - teammate_pressure
    - wall_break
    - anti_aggro
    - lane_control
  verdict: strong_fit | conditional_fit | false_positive | poor_fit
```

这能直接处理用户指出的问题：`Shade` 或 `阿尔缇` 这类“能过河但手短”的候选，不能因为命中 `water_crossing` 就被判定为强适配。它们需要进一步证明自己能在过河后站住、打到目标、制造击杀窗口，或在当前 draft 中承担不可替代的战术价值。

## 与 BP DSL 的连接

在 [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]] 中，`map_profile` 应先提供上述地图对象；随后：

1. `conditional_matchup.active_when.map_conditions` 引用具体 `map_feature_id`，而不是只写“水多”或“墙多”。
2. `candidate_eval.map_fit` 写明候选激活了哪些地图特征，哪些只是表面适配。
3. `map_bp_factors` 将地图特征转成当前局面的职责、硬门槛、地形状态计划和 slot 风险。
4. `hard_gate_result.must_answer` 可以来自地图因素，例如远程金库角度无人处理、敌方中路拥挤惩罚过强、敌方可过河入侵无人能回防。
5. `ban_state` 可根据地图因素拆路线，例如 ban 掉低成本利用远程金库角度、投掷口袋或基地角落锚点的英雄。

## Fandom 地图页的接入方式

Fandom 地图页可以作为第一批 `map_feature` 候选来源。抽检见 [[sources/Fandom-Ranked-Map-Source-Assessment|Fandom 来源摘要: Ranked 地图页建模价值评估]]。

当前 Ranked Season 46 的地图池索引见 [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]。稳定地图结论应进入 `wiki/entities/maps/` 下的单地图实体页；分层规则见 [[syntheses/地图知识分层治理|地图知识分层治理]]。

典型转换关系：

```yaml
fandom_map_page_to_schema:
  event: map_profile.mode
  obstacle_counts: topology.barriers 的辅助校验来源，不进入 BP 判断
  map_image: topology + tactical_features 的视觉校验来源
  layout_section: topology + objective_access + lane_dynamics
  tips_section: tactical_features + map_rules + example_brawlers
  history_section: source_context + map_rotation_context
```

使用边界：

- `Layout` 适合抽取稳定地形事实。
- `Tips` 适合抽取英雄与地形互动候选，但必须经过本地 BP DSL 校验。
- 英雄推荐不能直接转成 BP 推荐，必须先转为能力、路线、目标收益和失效条件。
- 当前排位地图池必须从 `Ranked` 页面单独记录抓取日期和赛季，避免轮换后误用。

## 关联页面

- [[sources/Fandom-Ranked-Map-Source-Assessment|Fandom 来源摘要: Ranked 地图页建模价值评估]]
- [[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- [[sources/User-Note-Map-Profile-Schema|用户经验来源摘要: 地图特征建模需要战术特征 Schema]]
- [[sources/User-Note-Map-Factor-BP-Expression|用户经验来源摘要: 地图因素需要 BP 决策表达]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
- [[syntheses/地图知识分层治理|地图知识分层治理]]
- [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/Ban-Pick-问题拆分|Ban Pick 问题拆分]]
