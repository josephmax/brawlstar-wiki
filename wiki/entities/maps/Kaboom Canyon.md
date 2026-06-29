# Kaboom Canyon

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Heist`
- Fandom URL：https://brawlstars.fandom.com/wiki/Kaboom_Canyon
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Kaboom Canyon
  mode: Heist
  summary: 开阔长线、中心草接近和局部投掷口袋共同决定金库 race，远程 safe DPS、反坦与选择性开墙价值高。
  topology:
    key_points:
      - 地图整体较开阔，长射程能直接影响边路和金库。
      - 中心草丛为短中程提供接近路线，但被探草后风险高。
      - 水域/墙体附近存在投掷或控制口袋。
  objective_access:
    objective_type: safe
    stable_goal: 主要目标是建立长线 safe DPS，同时防止敌方从中心草或局部墙体绕开正面对枪。
  tactical_features:
    - id: open_long_range_heist
      type: long_sightline
      location: main_lanes_to_safe
      condition: 长线视野让远程输出能直接参与金库 race
      combat_effect:
        rewards_capabilities: [long_range_safe_damage, projectile_reliability, wall_break_snowball, anti_tank_range]
        punishes_capabilities: [short_range_without_exit_route]
        false_positive_capabilities: [slow_projectile_into_high_mobility_lane]
      objective_effect:
        payoff: 低承诺位置即可制造金库伤害
      draft_implication:
        bp_use: 优先考虑可靠远程 DPS 和能拆掩体的英雄
    - id: center_bush_approach
      type: grass_route
      location: center_bush
      condition: 中心草允许短中程进入威胁半场
      combat_effect:
        rewards_capabilities: [bush_ambush, anti_marksman_pressure, wide_sweep]
        punishes_capabilities: [isolated_marksman_no_scan]
        false_positive_capabilities: [tank_when_grass_is_denied]
      objective_effect:
        payoff: 让敌方后排不能只看长线
      draft_implication:
        bp_use: 需要探草或范围压制保护远程
    - id: pond_thrower_pocket
      type: thrower_pocket
      location: water_wall_edges
      condition: 水域/墙体边缘给投掷和绕射提供局部安全角度
      combat_effect:
        rewards_capabilities: [thrower_pocket, arc_control, selective_wall_break]
        punishes_capabilities: [linear_shooter_if_walls_intact]
        false_positive_capabilities: [thrower_without_team_lane_control]
      objective_effect:
        payoff: 可干扰防守站位或保护金库入口
      draft_implication:
        bp_use: 中后手用开墙/突进回答
  lane_dynamics:
    notes:
      - 默认长线对枪，但中心草会打破纯远程格局。
      - 如果敌方无反坦，中心草短中程推进可改变 race。
      - 开墙会提高远程收益，但可能也暴露己方金库防守。
  map_rules:
    - if: 敌方选纯短手打长线
      then: 先检查草丛是否还能提供进入路线
      because: 没有草/墙掩护时短手难以持续打库
      bp_use: 用探草和远程维持距离
    - if: 敌方远程 safe DPS 占优
      then: 需要中心草压迫或开墙反打
      because: 单纯防守会输 race
      bp_use: 补 anti-marksman pressure 或更高 DPS
    - if: 己方投掷想打防守
      then: 必须证明有口袋和线权
      because: 开阔图投掷若无保护会被远程赶走
      bp_use: 只作为条件 pick
  false_positive:
    - 短手看到中心草不等于强；草被清后可能没有撤退路线。
    - 开墙如果没有远程压制跟进，可能只是削弱己方防守。
```

## BP 用法

- 如果 `敌方选纯短手打长线`，则 `先检查草丛是否还能提供进入路线`；BP 上用于：用探草和远程维持距离。
- 如果 `敌方远程 safe DPS 占优`，则 `需要中心草压迫或开墙反打`；BP 上用于：补 anti-marksman pressure 或更高 DPS。
- 如果 `己方投掷想打防守`，则 `必须证明有口袋和线权`；BP 上用于：只作为条件 pick。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
