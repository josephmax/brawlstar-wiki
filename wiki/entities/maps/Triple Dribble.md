# Triple Dribble

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Brawl Ball`
- Fandom URL：https://brawlstars.fandom.com/wiki/Triple_Dribble
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Triple Dribble
  mode: Brawl Ball
  summary: 球门 L 墙和桶阻挡直接射门，三路职责清晰，墙体互动、破门、弹墙和集结惩罚决定进球窗口。
  topology:
    key_points:
      - 球门前 L 墙和障碍阻挡直线射门。
      - 左右侧墙形成独立边路和弹墙/投掷角度。
      - 三路站位清晰，抱团推进会被范围和穿透惩罚。
  objective_access:
    objective_type: goal
    stable_goal: 核心是打开球门角度或用强控/弹墙/位移绕过防线；不处理墙体就难以稳定进球。
  tactical_features:
    - id: goal_barrel_block
      type: goal_barrier
      location: goal_front
      condition: 球门前障碍阻止直接射门
      combat_effect:
        rewards_capabilities: [wall_break_score_window, knockback_score, dash_or_jump_score, thrower_goal_control]
        punishes_capabilities: [poke_without_score_tool]
        false_positive_capabilities: [breaking_when_enemy_open_field_stronger]
      objective_effect:
        payoff: 破门或绕门是进球前提
      draft_implication:
        bp_use: BP 必须有 scoring window creator
    - id: side_4x4_wall_lane
      type: side_wall_lane
      location: side_lanes
      condition: 侧墙提供弹墙、投掷和边路推进路线
      combat_effect:
        rewards_capabilities: [bounce_wall, thrower_and_anti_thrower, side_lane_control, wall_use]
        punishes_capabilities: [linear_mid_only_comp]
        false_positive_capabilities: [thrower_without_peel]
      objective_effect:
        payoff: 边路线权能直接改变球门压力
      draft_implication:
        bp_use: 需要按边路职责分配英雄
    - id: team_clump_punish
      type: central_congestion
      location: mid_push_lane
      condition: 三人抱团推进容易被范围、穿透和控制惩罚
      combat_effect:
        rewards_capabilities: [clump_punish, pierce, area_denial, turret_or_pet_pressure]
        punishes_capabilities: [single_target_low_area]
        false_positive_capabilities: [clump_punish_if_enemy_splits_properly]
      objective_effect:
        payoff: 防守方可用多目标技能止推
      draft_implication:
        bp_use: 敌方堆中时后手补多目标惩罚
  lane_dynamics:
    notes:
      - 三路角色清晰，不能全员中路抱团。
      - 破门前墙体英雄价值高，破门后远程和直线射门价值升高。
      - 防守需要反突进和清球能力。
  map_rules:
    - if: 我方没有破门或绕门手段
      then: 阵容很难完成目标
      because: 球门结构阻止简单直射
      bp_use: 补 wall_break / dash / knockback
    - if: 敌方三人中路推进
      then: 范围和穿透收益上升
      because: 中路空间有限，抱团容易被惩罚
      bp_use: response pick clump punish
    - if: 敌方侧路弹墙/投掷成型
      then: 需要开墙或强侧路对抗
      because: 侧墙会持续制造球门压力
      bp_use: must_answer side wall value
  false_positive:
    - 只会击杀但不能破门的阵容会卡在球门前。
    - 过度破墙可能让敌方远程也获得更简单射门线。
```

## BP 用法

- 如果 `我方没有破门或绕门手段`，则 `阵容很难完成目标`；BP 上用于：补 wall_break / dash / knockback。
- 如果 `敌方三人中路推进`，则 `范围和穿透收益上升`；BP 上用于：response pick clump punish。
- 如果 `敌方侧路弹墙/投掷成型`，则 `需要开墙或强侧路对抗`；BP 上用于：must_answer side wall value。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
