# Hot Potato

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Heist`
- Fandom URL：https://brawlstars.fandom.com/wiki/Hot_Potato
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Hot Potato
  mode: Heist
  summary: 斜向中草、分割侧路和投掷角度让 Heist 同时奖励伏击、远程边路、穿透和低风险金库压力。
  topology:
    key_points:
      - 中部斜向草带提供伏击和过渡路线。
      - 两侧路线被墙体/草丛分割，边路赢线能切入金库。
      - 部分墙体给投掷和弹道绕射创造角度。
  objective_access:
    objective_type: safe
    stable_goal: Heist race 不只看 DPS，还看谁能从草丛或侧路安全转入金库输出。
  tactical_features:
    - id: diagonal_center_bush_band
      type: grass_route
      location: center_diagonal_bush
      condition: 斜草带允许伏击、换线和中路穿插
      combat_effect:
        rewards_capabilities: [bush_ambush, speed_gear, wide_spread_check, pierce_mid_grouping]
        punishes_capabilities: [pure_long_range_no_scan]
        false_positive_capabilities: [tank_if_bushes_are_burned]
      objective_effect:
        payoff: 可把中路控制转化为金库入口
      draft_implication:
        bp_use: BP 需要探草/扫草与反伏击资源
    - id: split_side_lanes
      type: side_lane
      location: left_and_right_routes
      condition: 侧路分割让边路远程和单路压制有独立价值
      combat_effect:
        rewards_capabilities: [side_sniping, lane_duel, safe_dps_after_lane_win]
        punishes_capabilities: [single_lane_tunnel_vision, slow_rotation]
        false_positive_capabilities: [short_range_without_lane_win]
      objective_effect:
        payoff: 赢边路后能进入金库输出窗口
      draft_implication:
        bp_use: 阵容不能三人只打中路
    - id: right_thrower_safe_angle
      type: thrower_pocket
      location: right_side_wall_angles
      condition: 墙体角度允许投掷或绕射低风险施压
      combat_effect:
        rewards_capabilities: [thrower_safe_damage, arc_control, wall_bypass]
        punishes_capabilities: [linear_shooter_if_walls_intact]
        false_positive_capabilities: [thrower_if_enemy_has_easy_dive_route]
      objective_effect:
        payoff: 给金库或防守位持续压力
      draft_implication:
        bp_use: 后手需要 anti_thrower dive 或 wall break
  lane_dynamics:
    notes:
      - 中路草带负责争夺主动，边路负责打开金库入口。
      - 敌方堆中时穿透/范围伤害收益提升。
      - 投掷角度存在，但需要队友线权保护。
  map_rules:
    - if: 敌方缺探草
      then: 斜草伏击和 speed 侧压升值
      because: 草带贯穿中部，能打乱 Heist race 节奏
      bp_use: 可用草丛侧压作为后手
    - if: 敌方投掷占到右侧角度
      then: 需要开墙、突进或远程压制
      because: 否则会低风险拖防守并磨金库
      bp_use: must_answer 投掷口袋
    - if: 我方只有中路火力没有边路
      then: 金库触达会不稳定
      because: Heist 胜负取决于持续打库窗口
      bp_use: 补可赢边路的 safe DPS
  false_positive:
    - 草丛伏击在被烧草/探草后急剧贬值。
    - 投掷没有队友压线时容易被侧路突进处理。
```

## BP 用法

- 如果 `敌方缺探草`，则 `斜草伏击和 speed 侧压升值`；BP 上用于：可用草丛侧压作为后手。
- 如果 `敌方投掷占到右侧角度`，则 `需要开墙、突进或远程压制`；BP 上用于：must_answer 投掷口袋。
- 如果 `我方只有中路火力没有边路`，则 `金库触达会不稳定`；BP 上用于：补可赢边路的 safe DPS。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
