# Safe(r) Zone

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Heist`
- Fandom URL：https://brawlstars.fandom.com/wiki/Safe%28r%29_Zone
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Safe(r) Zone
  mode: Heist
  summary: 直线金库路径、水域跨越、左路远程角度和中路投掷封锁构成更强调路线选择的 Heist 图。
  topology:
    key_points:
      - 通向金库的路线更直观，但会被中路和侧路地形分割。
      - 水域/障碍让部分英雄能走普通英雄不能走的进库路线。
      - 左路长线和中路投掷都能改变防守站位。
  objective_access:
    objective_type: safe
    stable_goal: 目标访问取决于候选能否沿路线持续推进、跨越水域或从远程角度低承诺打库。
  tactical_features:
    - id: straight_path_to_safe
      type: objective_route
      location: main_safe_lane
      condition: 存在较直接的金库推进路径
      combat_effect:
        rewards_capabilities: [route_based_safe_damage, lane_duel_consistency, sustained_dps]
        punishes_capabilities: [slow_rotation_without_range]
        false_positive_capabilities: [glass_cannon_if_lane_lost]
      objective_effect:
        payoff: 赢线后能快速转化为金库伤害
      draft_implication:
        bp_use: 先手要兼顾打线和打库
    - id: water_traverse_to_safe
      type: river_crossing
      location: water_route_to_safe
      condition: 水域路线允许特定英雄绕过普通防线
      combat_effect:
        rewards_capabilities: [water_traverse, water_crossing_with_range, mobile_objective_pressure]
        punishes_capabilities: [normal_walk_melee]
        false_positive_capabilities: [water_crossing_without_damage_window]
      objective_effect:
        payoff: 提高可跨水英雄的路线价值
      draft_implication:
        bp_use: 但必须验证跨水后的输出/生存
    - id: left_lane_long_range_safe_angle
      type: long_sightline
      location: left_lane
      condition: 左路远程角度可低承诺打库或牵制防守
      combat_effect:
        rewards_capabilities: [long_range_safe_angle, wall_break_followup, projectile_reliability]
        punishes_capabilities: [short_range_lane_into_open]
        false_positive_capabilities: [long_range_without_anti_dive]
      objective_effect:
        payoff: 让远程可作为稳定 DPS 路线
      draft_implication:
        bp_use: 敌方可用机动/开墙/压线回答
    - id: mid_lane_thrower_block
      type: thrower_pocket
      location: mid_lane_walls
      condition: 中路墙体给投掷封锁推进路线的机会
      combat_effect:
        rewards_capabilities: [thrower_space_creation, choke_blocking, arc_control]
        punishes_capabilities: [linear_push_through_wall]
        false_positive_capabilities: [thrower_if_flanked_from_side]
      objective_effect:
        payoff: 阻断敌方进库路线并磨金库
      draft_implication:
        bp_use: 需要队友边路线权保护
  lane_dynamics:
    notes:
      - 直线推进、跨水路线和远程角度同时存在，不能只按一种 Heist 模型评价。
      - 中路投掷能拖节奏，但边路被破会失去保护。
      - 水域能力必须和目标输出绑定。
  map_rules:
    - if: 敌方缺远程左路答案
      then: 长线打库可以成为主计划
      because: 低承诺 DPS 会迫使敌方回防
      bp_use: 优先 long_range_safe_angle
    - if: 敌方选中路投掷封路
      then: 侧路压力或开墙成为必需
      because: 否则推进路线会被反复阻断
      bp_use: response pick anti_thrower
    - if: 候选只能跨水不能持续输出
      then: 不要当作强 map-fit
      because: 跨水只是路线，不是胜利条件
      bp_use: 标记为条件适配
  false_positive:
    - 水域路线会制造假阳性，尤其是手短或过水后不能持续打库的英雄。
    - 投掷若边路失控，会从封路者变成被包夹目标。
```

## BP 用法

- 如果 `敌方缺远程左路答案`，则 `长线打库可以成为主计划`；BP 上用于：优先 long_range_safe_angle。
- 如果 `敌方选中路投掷封路`，则 `侧路压力或开墙成为必需`；BP 上用于：response pick anti_thrower。
- 如果 `候选只能跨水不能持续输出`，则 `不要当作强 map-fit`；BP 上用于：标记为条件适配。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
