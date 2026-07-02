# Pinball Dreams

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Brawl Ball`
- Fandom URL：https://brawlstars.fandom.com/wiki/Pinball_Dreams
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Pinball Dreams
  mode: Brawl Ball
  summary: 开放中路与侧边墙体共存，墙既是 trick-shot/控球资源，也是投掷、弹墙和破门决策的核心。
  topology:
    key_points:
      - 中路相对开放，持球推进和远程火力都能快速接触。
      - 侧边墙体/围栏提供投掷、弹墙、传球和 trick-shot 角度。
      - 破墙会打开球门和远程通路，但也可能移除己方战术墙。
  objective_access:
    objective_type: goal
    stable_goal: 目标是利用墙体或开墙制造进球窗口；地图不是简单越开越好。
  tactical_features:
    - id: trickshot_wall_value
      type: score_geometry
      location: side_and_goal_walls
      condition: 墙体可用于 trick-shot、传球和突然进球
      combat_effect:
        rewards_capabilities: [wall_use, trickshot_scorer, bounce_wall, ball_control]
        punishes_capabilities: [indiscriminate_wall_break]
        false_positive_capabilities: [breaking_walls_that_enable_own_scores]
      objective_effect:
        payoff: 墙体本身是进球资源
      draft_implication:
        bp_use: 不要默认所有墙都该破
    - id: side_fence_split
      type: thrower_pocket
      location: side_wall_lanes
      condition: 侧墙分割路线并保护投掷/弹墙角度
      combat_effect:
        rewards_capabilities: [thrower_pocket, bounce_wall, summon_pressure, lane_delay]
        punishes_capabilities: [linear_push_if_walls_intact]
        false_positive_capabilities: [thrower_without_center_control]
      objective_effect:
        payoff: 侧路能拖住防守并创造传球角度
      draft_implication:
        bp_use: 需要 anti_thrower 或选择性开墙
    - id: open_center_ball_lane
      type: open_lane
      location: center_lane
      condition: 开放中路让远程和快速推进更直接
      combat_effect:
        rewards_capabilities: [mid_range_control, long_range_poke, fast_ball_reset, anti_aggro]
        punishes_capabilities: [slow_tank_without_cover]
        false_positive_capabilities: [pure_sniper_if_side_walls_unanswered]
      objective_effect:
        payoff: 球权转换快，失误容易被反打
      draft_implication:
        bp_use: 阵容需兼顾中路稳定和侧墙处理
  lane_dynamics:
    notes:
      - 中路抢节奏，侧路利用墙体制造得分角度。
      - 开墙前投掷/弹墙更强，开墙后远程和直线推进更强。
      - 破墙决策要服务于己方得分路线。
  map_rules:
    - if: 我方有 trick-shot 或墙体得分手
      then: 不要过早破坏关键墙
      because: 墙是进球资源
      bp_use: 保留 scoring geometry
    - if: 敌方投掷/弹墙占侧路
      then: 需要选择性开墙或强突进
      because: 否则侧路会持续拖节奏
      bp_use: response pick anti-wall
    - if: 地图进入加时或墙被打开
      then: 远程和机动 scorer 升值
      because: 中路开放后控球更直接
      bp_use: 后续转 long range / fast scorer
  false_positive:
    - 无脑开墙可能帮敌方长手和削弱己方 trick-shot。
    - 投掷如果没有中路球权，难以单独创造得分。
```

## BP 用法

- 如果 `我方有 trick-shot 或墙体得分手`，则 `不要过早破坏关键墙`；BP 上用于：保留 scoring geometry。
- 如果 `敌方投掷/弹墙占侧路`，则 `需要选择性开墙或强突进`；BP 上用于：response pick anti-wall。
- 如果 `地图进入加时或墙被打开`，则 `远程和机动 scorer 升值`；BP 上用于：后续转 long range / fast scorer。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
