# Layer Cake

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Bounty`
- Fandom URL：https://brawlstars.fandom.com/wiki/Layer_Cake
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Layer Cake
  mode: Bounty
  summary: 多层墙草结构创造纵深、窄口、投掷落点和中路多目标收益，开墙和跳层能力会改变地图形态。
  topology:
    key_points:
      - 地图由多层横向墙草切成纵深区域。
      - 窄口让投掷、炮台、封路和多目标技能收益高。
      - 跳跃、越墙或开墙能打破层与层之间的自然防线。
  objective_access:
    objective_type: bounty_star
    stable_goal: Bounty 中每层掩体都能保护领先方；落后方需要开墙、投掷或越墙制造击杀窗口。
  tactical_features:
    - id: four_layer_wall_structure
      type: layered_cover
      location: horizontal_wall_layers
      condition: 多层墙体提供连续掩体和撤退纵深
      combat_effect:
        rewards_capabilities: [thrower_choke_control, protected_turret, retreat_safety, zone_denial]
        punishes_capabilities: [linear_marksman_if_walls_intact]
        false_positive_capabilities: [passive_comp_that_cannot_break_lead]
      objective_effect:
        payoff: 领先方可逐层后撤保星
      draft_implication:
        bp_use: 先手要考虑能否处理墙体
    - id: layer_choke_thrower_value
      type: lane_funnel
      location: narrow_layer_entries
      condition: 每层入口形成天然 choke
      combat_effect:
        rewards_capabilities: [thrower_choke_control, path_blocking, slow_or_stun_at_entry, spawnable_block]
        punishes_capabilities: [dash_in_without_followup]
        false_positive_capabilities: [thrower_if_enemy_has_jump_or_wall_break]
      objective_effect:
        payoff: 封入口即可阻止敌方拿星
      draft_implication:
        bp_use: 投掷/封路是强 response，但怕开墙和越墙
    - id: center_multi_hit_value
      type: central_congestion
      location: center_layer_intersections
      condition: 中路层间交汇容易多人重叠
      combat_effect:
        rewards_capabilities: [multi_hit_line, chain_damage, pierce, bounce_wall]
        punishes_capabilities: [single_target_low_area]
        false_positive_capabilities: [clump_punish_when_enemy_splits_wide]
      objective_effect:
        payoff: 放大连锁和穿透收益
      draft_implication:
        bp_use: 敌方堆中时可作为后手惩罚
    - id: jump_or_wallbreak_layer_skip
      type: route_bypass
      location: over_or_through_layers
      condition: 跳跃/开墙能绕过层级防守
      combat_effect:
        rewards_capabilities: [jump_over_layer, wall_break_transform, assassin_with_route]
        punishes_capabilities: [static_thrower_after_walls_removed]
        false_positive_capabilities: [jump_in_without_escape]
      objective_effect:
        payoff: 给落后方制造主动开战
      draft_implication:
        bp_use: 必须看敌方剩余反制位
  lane_dynamics:
    notes:
      - 默认围绕层级和窄口争夺，不是纯长线图。
      - 领先方更喜欢保墙；落后方更需要开墙或越墙。
      - 敌方堆中时多目标能力上升。
  map_rules:
    - if: 敌方投掷/封路占住层口
      then: 需要开墙或越墙改变路线
      because: 正面穿 chokepoint 会持续掉血
      bp_use: response pick wall_break/jump
    - if: 我方领先
      then: 保墙和退层比冒险追击重要
      because: Bounty 领先可以用层级拖时间
      bp_use: 选择保护和区域控制
    - if: 敌方多人堆中
      then: 连锁/穿透/炮台收益上升
      because: 层间交汇限制走位
      bp_use: 可补多目标惩罚
  false_positive:
    - 纯线性狙击在墙完整时会被削弱。
    - 跳进去不是自动好；如果无法撤出或秒杀，会在 Bounty 中送星。
```

## BP 用法

- 如果 `敌方投掷/封路占住层口`，则 `需要开墙或越墙改变路线`；BP 上用于：response pick wall_break/jump。
- 如果 `我方领先`，则 `保墙和退层比冒险追击重要`；BP 上用于：选择保护和区域控制。
- 如果 `敌方多人堆中`，则 `连锁/穿透/炮台收益上升`；BP 上用于：可补多目标惩罚。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
