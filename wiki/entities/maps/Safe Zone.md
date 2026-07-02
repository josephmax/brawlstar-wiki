# Safe Zone

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Heist`
- Fandom URL：https://brawlstars.fandom.com/wiki/Safe_Zone
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Safe Zone
  mode: Heist
  summary: 河道、水域路线、远程金库角度、中路拥挤和金库角落锚点共同决定英雄价值。
  topology:
    key_points:
      - 河道限制普通英雄直接进入敌方基地附近。
      - 中路可拥挤，也可由分路和远程角度拉开。
      - 敌方金库附近墙角/地形能让少数英雄持续存活。
  objective_access:
    objective_type: safe
    stable_goal: Heist 目标访问有两条主线：可过水/越墙进入敌方半场，或远程/抛物线不进半场也能打库。
  tactical_features:
    - id: river_barrier_to_enemy_base
      type: river_crossing
      location: mid_to_enemy_base
      condition: 河道阻断普通步行进库路线
      combat_effect:
        rewards_capabilities: [water_crossing_with_range, water_crossing_with_survivability, jump_or_wall_bypass, objective_pressure_after_crossing]
        punishes_capabilities: [normal_walk_short_range_without_control]
        false_positive_capabilities: [water_crossing_short_range_without_base_anchor]
      objective_effect:
        payoff: 能过河且能打库/站住才有价值
      draft_implication:
        bp_use: 不要把“会过水”单独当加分项
    - id: remote_safe_damage_angles
      type: long_sightline
      location: mid_to_enemy_safe
      condition: 部分远程或特殊弹道不用过河也能打到金库
      combat_effect:
        rewards_capabilities: [long_range_safe_damage, throw_arc_safe_damage, low_commitment_safe_pressure]
        punishes_capabilities: [short_range_no_objective_access]
        false_positive_capabilities: [long_range_with_unreliable_projectile_into_dive]
      objective_effect:
        payoff: 绕过河道问题制造稳定 DPS
      draft_implication:
        bp_use: 可作为先手基本面或回答敌方进库路线
    - id: mid_congestion_if_no_split
      type: central_congestion
      location: mid_lane
      condition: 敌方不分路会让中路人数密度升高
      combat_effect:
        rewards_capabilities: [chain_damage, line_pierce, turret_or_pet_pressure, long_linear_control, bounce_or_mark_value]
        punishes_capabilities: [single_target_low_area_pressure]
        false_positive_capabilities: [clump_punish_when_enemy_actually_splits]
      objective_effect:
        payoff: 放大连锁/穿透/召唤物收益
      draft_implication:
        bp_use: 评估前序 pick 是否会导致敌方聚中
    - id: enemy_safe_corner_anchor
      type: base_corner
      location: near_enemy_safe
      condition: 金库附近角落能让部分英雄反复存活
      combat_effect:
        rewards_capabilities: [wall_bounce_damage, jump_cycle, area_sustain, close_range_survival_with_escape]
        punishes_capabilities: [one_way_dive_no_sustain]
        false_positive_capabilities: [crossing_short_range_without_corner_use]
      objective_effect:
        payoff: 把一次入侵变成持续牵制或输出
      draft_implication:
        bp_use: 适合最后手惩罚缺少基地清理的阵容
  lane_dynamics:
    notes:
      - 分路能降低中路拥挤；敌方不分路会被连锁/穿透惩罚。
      - 远程打库和过河打库是两种不同能力，不应合并。
      - 可过水英雄必须证明过河后能打到目标或活下来。
  map_rules:
    - if: 候选只有 water_crossing 但手短
      then: 标记为 false_positive
      because: 路线打开不等于目标访问成立
      bp_use: 要求额外战术价值或队友压制
    - if: 敌方无基地清理/反入侵
      then: 金库角落锚点升值
      because: 入侵英雄能反复牵制和打库
      bp_use: 后手可选持续入侵型英雄
    - if: 敌方三人聚中防守
      then: 连锁、穿透、炮台和长线控制升值
      because: 中路拥挤放大多目标收益
      bp_use: 可作为 response pick
  false_positive:
    - 能过水但打不到金库、站不住或无法迫使回防的英雄是典型假阳性。
    - 远程角度必须看弹道可靠性和敌方 dive 威胁，不是所有长手都稳定。
```

## BP 用法

- 如果 `候选只有 water_crossing 但手短`，则 `标记为 false_positive`；BP 上用于：要求额外战术价值或队友压制。
- 如果 `敌方无基地清理/反入侵`，则 `金库角落锚点升值`；BP 上用于：后手可选持续入侵型英雄。
- 如果 `敌方三人聚中防守`，则 `连锁、穿透、炮台和长线控制升值`；BP 上用于：可作为 response pick。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
