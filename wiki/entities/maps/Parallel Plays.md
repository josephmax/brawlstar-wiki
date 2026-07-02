# Parallel Plays

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Hot Zone`
- Fandom URL：https://brawlstars.fandom.com/wiki/Parallel_Plays
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Parallel Plays
  mode: Hot Zone
  summary: 双圈距离远，分兵、远圈速度、本方圈锚点、水域/特殊路线和轮转惩罚决定 BP。
  topology:
    key_points:
      - 两个热区相距较远，单一抱团难以同时计分。
      - 本方近圈与敌方远圈职责不同，需要分兵。
      - 水域/障碍可能让特定英雄更快触达远圈或形成安全角度。
  objective_access:
    objective_type: zone
    stable_goal: Hot Zone 双圈要求同时能守本方圈、压远圈和轮转；缺少分兵能力会被计分拉开。
  tactical_features:
    - id: two_zone_split_map
      type: split_objective
      location: two_hot_zones
      condition: 双圈分离迫使队伍分兵
      combat_effect:
        rewards_capabilities: [split_pressure, home_zone_anchor, far_zone_dive, independent_lane_hold]
        punishes_capabilities: [single_anchor_no_rotation, three_player_stack]
        false_positive_capabilities: [carry_that_only_works_with_team_ball]
      objective_effect:
        payoff: 可以同时争两边计分
      draft_implication:
        bp_use: BP 要评估每个英雄是否能独立执行一边任务
    - id: far_zone_speed_requirement
      type: rotation_check
      location: far_enemy_zone_route
      condition: 远圈争夺要求速度、位移或强线权
      combat_effect:
        rewards_capabilities: [speed_rotation, mobility_engage, fast_zone_entry, sustain_under_focus]
        punishes_capabilities: [slow_rotation_without_range]
        false_positive_capabilities: [fast_brawler_without_zone_presence]
      objective_effect:
        payoff: 决定能否打断敌方远圈计分
      draft_implication:
        bp_use: 速度和机动是目标能力，不只是逃生能力
    - id: water_crossing_safe_angle
      type: river_crossing
      location: water_edges_between_zones
      condition: 水域路线/角度可让特定英雄绕开普通路径
      combat_effect:
        rewards_capabilities: [water_crossing_angle, range_over_water, safe_poke_to_zone]
        punishes_capabilities: [normal_walk_short_range]
        false_positive_capabilities: [water_crossing_without_zone_pressure]
      objective_effect:
        payoff: 提高跨水或隔水控圈价值
      draft_implication:
        bp_use: 需要验证能否实际赶人/站圈
  lane_dynamics:
    notes:
      - 至少一人稳守近圈，一人能打远圈，一人能支援或轮转。
      - 抱团会输双圈计分。
      - 远圈英雄必须能独立生存，不只是高伤害。
  map_rules:
    - if: 我方阵容只能抱团
      then: 不适合这张图
      because: 双圈会让抱团失去另一边计分
      bp_use: 补 split pressure
    - if: 敌方远圈英雄慢且无机动
      then: 速度/突进可惩罚
      because: 远圈支援距离长，落单容易被打断
      bp_use: 选 far_zone_dive 或 speed
    - if: 候选能过水但不能站圈/赶人
      then: 只能算条件适配
      because: Hot Zone 目标是计分，不是绕路本身
      bp_use: 要求 zone pressure
  false_positive:
    - 单核心站圈很强但无法轮转，可能在另一圈输分。
    - 水域能力如果不能转化为赶人或计分，就是假阳性。
```

## BP 用法

- 如果 `我方阵容只能抱团`，则 `不适合这张图`；BP 上用于：补 split pressure。
- 如果 `敌方远圈英雄慢且无机动`，则 `速度/突进可惩罚`；BP 上用于：选 far_zone_dive 或 speed。
- 如果 `候选能过水但不能站圈/赶人`，则 `只能算条件适配`；BP 上用于：要求 zone pressure。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
