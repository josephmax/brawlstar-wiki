# Hard Rock Mine

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Gem Grab`
- Fandom URL：https://brawlstars.fandom.com/wiki/Hard_Rock_Mine
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Hard Rock Mine
  mode: Gem Grab
  summary: 开放中场、H 形草带、窄横路和侧墙让中距离控线、草丛推进、投掷口袋与弹墙都能成立。
  topology:
    key_points:
      - 中路较开阔，但上下横向草带和墙体会切断视线。
      - 侧路草丛靠得更近，能让短手从侧边接近，但高水平局会频繁扫草。
      - 右侧 L 墙和小墙组能形成投掷/弹墙/炮台支援点。
  objective_access:
    objective_type: gem_mine
    stable_goal: Gem carrier 需要在开放中路收宝石，同时依赖草带和墙体保护撤退；边路线权会决定中路安全。
  tactical_features:
    - id: open_mid_with_h_bushes
      type: mixed_mid
      location: center_and_h_bushes
      condition: 开放中心与 H 形草带并存
      combat_effect:
        rewards_capabilities: [medium_range_control, wide_spread_check, bush_sustain, mid_survivability]
        punishes_capabilities: [pure_marksman_without_peel, artillery_without_side_control]
        false_positive_capabilities: [tank_after_bushes_are_constant_checked]
      objective_effect:
        payoff: 让中路既需要对枪又需要探草
      draft_implication:
        bp_use: 适合中距离稳定控线，不适合只靠长线或只靠偷袭
    - id: side_bush_approach
      type: flank_route
      location: left_and_right_bush_strips
      condition: 侧路草丛允许短手绕近敌方半场
      combat_effect:
        rewards_capabilities: [grass_flank, speed_gear, bush_heal, close_range_lane_pressure]
        punishes_capabilities: [slow_marksman_lane]
        false_positive_capabilities: [short_range_into_full_sweep_or_burn]
      objective_effect:
        payoff: 边路成功会迫使敌方中路后撤
      draft_implication:
        bp_use: 可作为回答长手中路的侧路手段，但必须配探草/掩护
    - id: l_wall_thrower_bounce_pocket
      type: thrower_pocket
      location: right_side_l_wall_and_wall_groups
      condition: L 墙和墙组提供投掷、弹墙和炮台站点
      combat_effect:
        rewards_capabilities: [thrower_wall_control, bounce_wall, protected_turret, choke_blocking]
        punishes_capabilities: [linear_shooter_if_walls_intact]
        false_positive_capabilities: [thrower_without_escape_against_side_flank]
      objective_effect:
        payoff: 可从安全点影响中路宝石矿
      draft_implication:
        bp_use: 中后手可用开墙或侧压处理
  lane_dynamics:
    notes:
      - 中路负责宝石和火力压制；边路负责草丛推进与防侧切。
      - 如果敌方持续扫草，草丛坦克价值下降，中距离控线价值上升。
      - 墙体未开时投掷/弹墙强；开墙后长手更容易接管。
  map_rules:
    - if: 敌方中路是纯长手
      then: 侧草和中距离压迫可以拆掉站位
      because: 长手必须同时处理视野和侧路接近
      bp_use: 可补草丛侧路或宽攻击控制
    - if: 敌方投掷/炮台依赖 L 墙
      then: 开墙或侧路贴近是主要回答
      because: 墙体口袋让其能低风险影响中路
      bp_use: 后手需要 wall_break 或 flank pressure
    - if: 我方拿宝石领先
      then: 撤退路线要优先保护草带/墙体
      because: 倒计时撤退比继续中路对枪更重要
      bp_use: 选择能护送和探草的补位
  false_positive:
    - Fandom 提到短手有用，但在高水平局必须假设敌方会扫草；没有路线保护的短手不能自动算强。
    - 纯投掷若侧路失控，会被草丛压缩。
```

## BP 用法

- 如果 `敌方中路是纯长手`，则 `侧草和中距离压迫可以拆掉站位`；BP 上用于：可补草丛侧路或宽攻击控制。
- 如果 `敌方投掷/炮台依赖 L 墙`，则 `开墙或侧路贴近是主要回答`；BP 上用于：后手需要 wall_break 或 flank pressure。
- 如果 `我方拿宝石领先`，则 `撤退路线要优先保护草带/墙体`；BP 上用于：选择能护送和探草的补位。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
