# Ring of Fire

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Hot Zone`
- Fandom URL：https://brawlstars.fandom.com/wiki/Ring_of_Fire
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Ring of Fire
  mode: Hot Zone
  summary: 单圈、大草、L 墙支援口袋和侧路长角度让中心争夺、草控、支援站位与反伏击成为核心。
  topology:
    key_points:
      - 单一热区周围有大草区，隐藏接近和站圈都很重要。
      - L 墙给支援/投掷/炮台提供安全口袋。
      - 侧路长角度可以压圈，但会被草丛伏击威胁。
  objective_access:
    objective_type: zone
    stable_goal: 目标是持续站圈并控制草丛视野；缺探草会让任何圈外压制都不稳定。
  tactical_features:
    - id: large_center_bush_mass
      type: grass_anchor
      location: center_zone_bushes
      condition: 大草区覆盖热区附近接近路线
      combat_effect:
        rewards_capabilities: [bush_control, bush_reveal, wide_spread, zone_sustain, area_super]
        punishes_capabilities: [isolated_marksman, heavyweight_without_connected_cover]
        false_positive_capabilities: [tank_after_bush_burned]
      objective_effect:
        payoff: 控制草就控制进圈安全
      draft_implication:
        bp_use: 探草/扫草是硬需求
    - id: l_wall_support_pocket
      type: support_pocket
      location: l_wall_near_zone
      condition: L 墙允许支援、投掷或炮台安全影响热区
      combat_effect:
        rewards_capabilities: [support_anchor, thrower_control, protected_turret, healing_station]
        punishes_capabilities: [linear_shooter_if_walls_intact]
        false_positive_capabilities: [support_pocket_if_enemy_has_wallbreak]
      objective_effect:
        payoff: 低风险给站圈者续航或压制
      draft_implication:
        bp_use: 后手要看是否需要开墙/突进清点
    - id: right_lane_long_angle_ambush_risk
      type: long_sightline
      location: side_long_lane
      condition: 侧路长线可压圈，但旁边草丛有伏击风险
      combat_effect:
        rewards_capabilities: [long_range_zone_pressure, vision_gear, anti_aggro_peel]
        punishes_capabilities: [sniper_without_bush_check]
        false_positive_capabilities: [long_angle_when_enemy_controls_bush]
      objective_effect:
        payoff: 提供圈外火力，但需要视野保护
      draft_implication:
        bp_use: 长手不是无条件强，必须配探草
  lane_dynamics:
    notes:
      - 中心草控优先，侧路长线作为支援而不是主目标。
      - 拿圈方应守草和 L 墙；丢圈方需要清草/开墙/范围技能。
      - 孤立长手容易被草丛绕后。
  map_rules:
    - if: 我方无探草
      then: 所有圈外远程都不稳定
      because: 大草区让敌方可以无声接近
      bp_use: 优先补 vision/sweep
    - if: 敌方用 L 墙支援口袋
      then: 开墙或突进价值上升
      because: 不清点会让敌方持续站圈
      bp_use: must_answer support pocket
    - if: 我方拥有强区域 Super
      then: 开局控圈后滚雪球能力高
      because: 单圈图控制时间直接等于胜利进度
      bp_use: 可作为先手计划
  false_positive:
    - 把它当纯草丛坦克图不够；L 墙和长线支援同样重要。
    - 把它当纯长线图也错；没有草控的远程会被伏击。
```

## BP 用法

- 如果 `我方无探草`，则 `所有圈外远程都不稳定`；BP 上用于：优先补 vision/sweep。
- 如果 `敌方用 L 墙支援口袋`，则 `开墙或突进价值上升`；BP 上用于：must_answer support pocket。
- 如果 `我方拥有强区域 Super`，则 `开局控圈后滚雪球能力高`；BP 上用于：可作为先手计划。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
