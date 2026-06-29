# Pit Stop

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Heist`
- Fandom URL：https://brawlstars.fandom.com/wiki/Pit_Stop
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Pit Stop
  mode: Heist
  summary: 金库屏障、弯曲草带和墙体角度让投掷、跳墙/滚入、破墙开线和近身金库爆发成为核心。
  topology:
    key_points:
      - 金库前有墙体/屏障保护，直线远程初始不易获得稳定角度。
      - 弯曲草带和侧路提供接近路线。
      - 墙体一旦被打开，地图会从近身/投掷图转为远程 DPS 图。
  objective_access:
    objective_type: safe
    stable_goal: 目标访问高度依赖能否越过、绕过或破坏金库屏障；普通射手需要开线后才有稳定价值。
  tactical_features:
    - id: safe_barrier_wall
      type: objective_barrier
      location: around_safe
      condition: 金库被墙体保护，正面直线输出受限
      combat_effect:
        rewards_capabilities: [wall_bypass, throw_arc_safe_damage, jump_to_safe, roll_to_safe, wall_break_route_creation]
        punishes_capabilities: [marksman_without_wall_break]
        false_positive_capabilities: [melee_without_super_access]
      objective_effect:
        payoff: 决定谁能第一时间打到金库
      draft_implication:
        bp_use: BP 要先问候选如何接触金库
    - id: curved_bush_entry
      type: grass_route
      location: curved_side_bushes
      condition: 弯曲草带让近身和突进能蓄资源后进库
      combat_effect:
        rewards_capabilities: [close_range_safe_burst, super_charge_route, ambush_entry]
        punishes_capabilities: [static_long_range_no_scan]
        false_positive_capabilities: [tank_without_breakthrough_or_escape]
      objective_effect:
        payoff: 允许低血量高爆发英雄制造打库窗口
      draft_implication:
        bp_use: 需要反坦、控制或探草作为回答
    - id: wall_break_mode_switch
      type: wall_break_transform
      location: safe_side_walls
      condition: 选择性破墙会改变整张图目标访问
      combat_effect:
        rewards_capabilities: [wall_break_for_marksman, long_range_safe_angle, anti_thrower_opening]
        punishes_capabilities: [thrower_safe_angle_if_opened]
        false_positive_capabilities: [indiscriminate_wall_break_helping_enemy_dps]
      objective_effect:
        payoff: 让远程 DPS 从条件适配变成强适配
      draft_implication:
        bp_use: 开墙时机是 BP 和局内执行核心
  lane_dynamics:
    notes:
      - 前期围绕墙体和草丛进库；开墙后转向远程 race。
      - 投掷需要队友保护线权，突进需要蓄 Super 或有入口。
      - 防守方必须保留反坦/控制，否则近身打库会滚雪球。
  map_rules:
    - if: 我方候选无法越墙/开墙/绕墙
      then: 不要只因 Heist DPS 高就选
      because: 初始金库屏障会让输出打不到目标
      bp_use: 优先目标访问能力
    - if: 敌方选投掷或跳墙进库
      then: 必须有开墙、反坦或控制回答
      because: 否则目标访问成本过低
      bp_use: ban/pick anti-thrower 或 anti-dive
    - if: 墙已被打开或我方有稳定开墙
      then: 远程 safe DPS 价值上升
      because: 目标暴露后普通长手能接管 race
      bp_use: 后续 pick 可转 DPS
  false_positive:
    - 高 DPS 射手如果没有开墙支持，初期可能无法打到金库。
    - 近战会突进不等于能打库；没有 Super 入口或生存窗口会卡在墙外。
```

## BP 用法

- 如果 `我方候选无法越墙/开墙/绕墙`，则 `不要只因 Heist DPS 高就选`；BP 上用于：优先目标访问能力。
- 如果 `敌方选投掷或跳墙进库`，则 `必须有开墙、反坦或控制回答`；BP 上用于：ban/pick anti-thrower 或 anti-dive。
- 如果 `墙已被打开或我方有稳定开墙`，则 `远程 safe DPS 价值上升`；BP 上用于：后续 pick 可转 DPS。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
