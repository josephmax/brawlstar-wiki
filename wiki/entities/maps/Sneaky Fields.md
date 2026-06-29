# Sneaky Fields

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Brawl Ball`
- Fandom URL：https://brawlstars.fandom.com/wiki/Sneaky_Fields
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Sneaky Fields
  mode: Brawl Ball
  summary: H 形草丛、球门屏障和侧路突进让破门、草控、投掷控中与持球突破成为核心。
  topology:
    key_points:
      - 中路和侧路大量草丛遮蔽球权与进攻路线。
      - 球门前屏障使直接射门受限，需要破门或强制窗口。
      - 主墙体保护投掷，也会让短手得分手接近。
  objective_access:
    objective_type: goal
    stable_goal: 进球通常来自草丛控线、破门、强控或侧路位移，而不是纯远程消耗。
  tactical_features:
    - id: h_bush_ball_mid
      type: grass_anchor
      location: h_shaped_mid_bushes
      condition: H 形草丛覆盖中路球权和侧路推进
      combat_effect:
        rewards_capabilities: [grass_control, bush_reveal, speed_scorer, wide_spread, anti_aggro]
        punishes_capabilities: [pure_long_range_without_goal_pressure]
        false_positive_capabilities: [tank_if_grass_is_denied]
      objective_effect:
        payoff: 让抢球和接近都围绕草丛展开
      draft_implication:
        bp_use: BP 必须带探草/扫草或强草丛英雄
    - id: goal_barrier_break_value
      type: goal_barrier
      location: goal_mouth_walls
      condition: 球门屏障限制直接射门
      combat_effect:
        rewards_capabilities: [wall_break_for_goal, thrower_main_wall_control, dash_score_window, knockback_score]
        punishes_capabilities: [ranged_poke_no_score]
        false_positive_capabilities: [wall_break_when_enemy_has_better_open_field]
      objective_effect:
        payoff: 破门后得分路径显著变短
      draft_implication:
        bp_use: 破门能力是硬门槛之一
    - id: side_lane_dash_score
      type: flank_score_route
      location: side_bush_lanes
      condition: 侧路草丛允许持球突进、传球和突然进球
      combat_effect:
        rewards_capabilities: [scorer_dash, speed_gear, close_range_burst, ball_carry_pressure]
        punishes_capabilities: [slow_rotation]
        false_positive_capabilities: [dive_without_ball_or_cc]
      objective_effect:
        payoff: 能把边路赢线直接转成进球
      draft_implication:
        bp_use: 需要反冲、击退或减速回答
  lane_dynamics:
    notes:
      - 中路草控决定开局和球权，侧路决定突破。
      - 破门前投掷/短手更强，破门后远程也能参与。
      - 队伍必须同时回答草丛和球门屏障。
  map_rules:
    - if: 我方无破墙且无强控得分
      then: 得分路径不足
      because: 球门屏障会拖慢所有正面推进
      bp_use: 补 wall_break/scorer
    - if: 敌方草丛进攻很强
      then: 必须有扫草、击退或范围控制
      because: 否则侧草会形成连续进球压力
      bp_use: must_answer grass aggression
    - if: 墙被打开后
      then: 远程和直线防守升值
      because: 地图从草丛进攻转为开放防守
      bp_use: 后续 pick 可转 anti-scorer range
  false_positive:
    - 只会远程消耗但无法破门/进球，在这张图容易赢击杀输目标。
    - 草丛英雄如果没有持球或控人跟进，也只是拖时间。
```

## BP 用法

- 如果 `我方无破墙且无强控得分`，则 `得分路径不足`；BP 上用于：补 wall_break/scorer。
- 如果 `敌方草丛进攻很强`，则 `必须有扫草、击退或范围控制`；BP 上用于：must_answer grass aggression。
- 如果 `墙被打开后`，则 `远程和直线防守升值`；BP 上用于：后续 pick 可转 anti-scorer range。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
