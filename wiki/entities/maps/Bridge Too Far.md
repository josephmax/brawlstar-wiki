# Bridge Too Far

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Heist`
- Fandom URL：https://brawlstars.fandom.com/wiki/Bridge_Too_Far
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Bridge Too Far
  mode: Heist
  summary: 三条纵向水域隔离的 Heist 路线让单路线权、跨线远程和稳定金库输出成为核心。
  topology:
    key_points:
      - 三条路线被纵向水域切开，横向支援成本高。
      - 每路都更像独立 duel，失线后容易变成金库直压。
      - 水域让普通短手难以随意换线或绕后。
  objective_access:
    objective_type: safe
    stable_goal: 目标是赢下至少一路并持续打金库；跨线远程能同时支援队友和压金库。
  tactical_features:
    - id: three_isolated_heist_lanes
      type: lane_split
      location: three_vertical_lanes
      condition: 三路隔离导致每路单挑质量极高
      combat_effect:
        rewards_capabilities: [lane_duel_consistency, long_range_safe_damage, sustained_dps, cross_lane_pressure]
        punishes_capabilities: [slow_rotation, short_range_flank_without_route]
        false_positive_capabilities: [team_comp_with_no_individual_lane_winner]
      objective_effect:
        payoff: 赢一路即可转化为金库压力
      draft_implication:
        bp_use: BP 先看三路是否都有可接受对位，而不是只看团战强度
    - id: vertical_water_barriers
      type: river_barrier
      location: between_lanes
      condition: 水域限制普通英雄横向支援和短手绕后
      combat_effect:
        rewards_capabilities: [range_over_water, water_crossing_with_range, projectile_width, safe_dps_from_lane]
        punishes_capabilities: [melee_no_route, thrower_without_angle]
        false_positive_capabilities: [water_crossing_short_range_without_safe_pressure]
      objective_effect:
        payoff: 让远程和可隔水输出的英雄更稳定
      draft_implication:
        bp_use: 短手 counter 必须证明有进场路线
    - id: thrower_access_false_positive
      type: false_positive_feature
      location: lane_edges_and_safe_angles
      condition: 投掷不一定能稳定接触金库或保护自身
      combat_effect:
        rewards_capabilities: [thrower_only_with_safe_angle, wall_break_to_create_angle]
        punishes_capabilities: [generic_lobber_without_safe_access]
        false_positive_capabilities: [drafting_thrower_because_heist_has_walls]
      objective_effect:
        payoff: 只有安全角度存在时才转化为金库收益
      draft_implication:
        bp_use: 投掷候选应被标记为条件适配
  lane_dynamics:
    notes:
      - 默认三路平行分配，换线和救援慢。
      - 强路线权可以转化成直接 safe DPS，而不是只转化为击杀。
      - 组合需要至少一个跨线支援点，避免某一路崩盘不可救。
  map_rules:
    - if: 候选英雄无法独立守一路
      then: 不要当稳定 pick
      because: 三路隔离放大单路劣势
      bp_use: 优先 lane_duel_consistency
    - if: 敌方选短手刺客反远程
      then: 评估地图是否给了接近路线
      because: 水域和长直线会让许多短手 counter 失效
      bp_use: 不能无条件承认 counter
    - if: 我方有长射程跨线输出
      then: 可以保护弱侧并加速金库 race
      because: 跨线火力降低换线成本
      bp_use: 作为先手或保护位都很有价值
  false_positive:
    - “某刺客克制某射手”在这张图常常失效，因为接近路线过于明确。
    - 投掷不是天然 Heist 解法；没有安全角度就无法稳定打金库。
```

## BP 用法

- 如果 `候选英雄无法独立守一路`，则 `不要当稳定 pick`；BP 上用于：优先 lane_duel_consistency。
- 如果 `敌方选短手刺客反远程`，则 `评估地图是否给了接近路线`；BP 上用于：不能无条件承认 counter。
- 如果 `我方有长射程跨线输出`，则 `可以保护弱侧并加速金库 race`；BP 上用于：作为先手或保护位都很有价值。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
