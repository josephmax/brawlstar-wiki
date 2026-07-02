# Shooting Star

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Bounty`
- Fandom URL：https://brawlstars.fandom.com/wiki/Shooting_Star
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Shooting Star
  mode: Bounty
  summary: 经典长线开阔 Bounty 图，极长射程、命中稳定性、少量墙体利用与开墙滚雪球决定 BP。
  topology:
    key_points:
      - 中路和边路长线极开阔，远程英雄能低承诺换血。
      - 少量墙体/草丛提供局部投掷或躲线角度。
      - 墙体被开后投掷和短手更难发挥。
  objective_access:
    objective_type: bounty_star
    stable_goal: Bounty 中远程拿星和保星是主线；落后方需要开墙、投掷角度或强制进场。
  tactical_features:
    - id: open_sniper_bounty
      type: long_sightline
      location: full_map_lanes
      condition: 大部分区域为长线开阔
      combat_effect:
        rewards_capabilities: [extreme_range, projectile_reliability, long_range_support, vision_control]
        punishes_capabilities: [close_range_without_forced_push]
        false_positive_capabilities: [sniper_with_bad_matchup_into_faster_sniper]
      objective_effect:
        payoff: 远程能低风险累积星差
      draft_implication:
        bp_use: 先手应优先稳定长线或反长线
    - id: few_wall_thrower_pocket
      type: thrower_pocket
      location: limited_wall_clusters
      condition: 少量墙体能给投掷提供暂时口袋
      combat_effect:
        rewards_capabilities: [thrower_if_walls_intact, arc_pressure, temporary_cover_use]
        punishes_capabilities: [linear_shooter_if_walls_intact]
        false_positive_capabilities: [thrower_after_wall_break]
      objective_effect:
        payoff: 投掷可作为条件反狙手段
      draft_implication:
        bp_use: 必须评估敌方是否能开墙
    - id: wall_break_snowball
      type: wall_break_transform
      location: limited_cover
      condition: 开墙会迅速把地图推向纯长线
      combat_effect:
        rewards_capabilities: [wall_break, range_snowball, anti_thrower]
        punishes_capabilities: [cover_dependent_thrower, short_range_cover_push]
        false_positive_capabilities: [opening_walls_when_behind_without_range]
      objective_effect:
        payoff: 剥夺敌方保护点并扩大领先
      draft_implication:
        bp_use: 适合回答投掷/短手
  lane_dynamics:
    notes:
      - 默认长线分散站位，死亡成本高。
      - 墙体完整时投掷有局部窗口，墙体被破后贬值。
      - 水域/空旷区让无法远程换血的英雄难以安全接近。
  map_rules:
    - if: 我方缺极长线
      then: BP 基本面劣势
      because: 地图给远程低风险拿星空间
      bp_use: 优先补 sniper 或长线支援
    - if: 敌方投掷依赖少量墙体
      then: 开墙是直接回答
      because: 墙体数量少，破掉后难恢复
      bp_use: wall_break 可作为 must_answer
    - if: 想用刺客反狙
      then: 必须等最后手且确认敌方无 peel/开阔弱点
      because: 地图默认不支持免费接近
      bp_use: 高风险高上限，不适合早手
  false_positive:
    - “投掷克制狙击”只在墙体完整且有安全口袋时成立。
    - 短手反狙如果没有强制进场条件，通常只是送星。
```

## BP 用法

- 如果 `我方缺极长线`，则 `BP 基本面劣势`；BP 上用于：优先补 sniper 或长线支援。
- 如果 `敌方投掷依赖少量墙体`，则 `开墙是直接回答`；BP 上用于：wall_break 可作为 must_answer。
- 如果 `想用刺客反狙`，则 `必须等最后手且确认敌方无 peel/开阔弱点`；BP 上用于：高风险高上限，不适合早手。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
