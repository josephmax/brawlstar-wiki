# Gem Fort

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Gem Grab`
- Fandom URL：https://brawlstars.fandom.com/wiki/Gem_Fort
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Gem Fort
  mode: Gem Grab
  summary: 中心堡垒、四入口和侧草连接让入口封锁、中心占领、探草与破墙成为主轴。
  topology:
    key_points:
      - 宝石矿位于中心堡垒附近，中心由直角墙围出四个主要入口。
      - 侧路草丛可连接到对侧，敌方可以从边缘草丛绕后或隐藏 gem carrier。
      - 中心角落可作为控场或炮台锚点，但怕投掷和破墙。
  objective_access:
    objective_type: gem_mine
    stable_goal: 核心是占住中心后让宝石矿变成己方可收、敌方难进的区域；撤退时中心墙体也能保护 gem carrier。
  tactical_features:
    - id: four_entry_center_fort
      type: lane_funnel
      location: center_fort
      condition: 中心只有少数入口，进出都经过可封锁通道
      combat_effect:
        rewards_capabilities: [area_denial, entrance_blocking, knockback, slow, spawnable_anchor]
        punishes_capabilities: [single_target_poke, short_range_without_entry_tool]
        false_positive_capabilities: [wall_break_without_followup_opening_own_cover]
      objective_effect:
        payoff: 控制入口即可控制宝石矿访问
      draft_implication:
        bp_use: 优先考虑能封门、推人、减速或放置物的英雄
    - id: bushy_side_connection
      type: grass_flank
      location: side_bush_lanes
      condition: 两侧草丛连接半场，能偷袭或保护撤退
      combat_effect:
        rewards_capabilities: [bush_reveal, bush_sweep, ambush_pressure, speed_rotation]
        punishes_capabilities: [low_area_long_range]
        false_positive_capabilities: [gem_carrier_hiding_without_team_control]
      objective_effect:
        payoff: 侧草决定敌方是否能绕开中心堡垒
      draft_implication:
        bp_use: 如果队伍中心强但无探草，仍可能被边路翻盘
    - id: center_wall_transform
      type: wall_break_transform
      location: center_enemy_side_walls
      condition: 破墙会改变堡垒入口和掩体价值
      combat_effect:
        rewards_capabilities: [selective_wall_break, long_range_after_opening, anti_thrower_angle]
        punishes_capabilities: [thrower_pocket, corner_camping]
        false_positive_capabilities: [overbreak_when_our_comp_needs_fort]
      objective_effect:
        payoff: 打开中心后让远程和直线压制接管
      draft_implication:
        bp_use: 破墙是中后手回答中心投掷/炮台的关键
  lane_dynamics:
    notes:
      - 默认中路争堡垒入口，边路负责草丛侦察和侧压。
      - 拿到中心后可用墙体保护撤退；丢中心后需要范围技能重新开门。
      - 三人挤中心会被范围、炮台、连锁和投掷惩罚。
  map_rules:
    - if: 敌方先手中心控场/炮台
      then: 需要入口封锁的反制或选择性破墙
      because: 中心一旦被占住，普通对枪很难进门
      bp_use: 补 area denial、thrower、wall break 或 knockback
    - if: 敌方缺探草
      then: 侧草偷袭和倒计时藏点价值上升
      because: 侧草连通地图边缘，能绕开正面堡垒
      bp_use: 可以补视野或侧压英雄
    - if: 我方阵容依赖中心墙体
      then: 不要无脑破墙
      because: 破墙同时会削弱己方撤退和中心锚点
      bp_use: 只在能转远程压制时开墙
  false_positive:
    - 单体 poke 如果不能处理入口和草丛，实际无法控制宝石矿。
    - 破墙不是天然收益；开墙后若没有远程压制，可能帮敌方进门。
```

## BP 用法

- 如果 `敌方先手中心控场/炮台`，则 `需要入口封锁的反制或选择性破墙`；BP 上用于：补 area denial、thrower、wall break 或 knockback。
- 如果 `敌方缺探草`，则 `侧草偷袭和倒计时藏点价值上升`；BP 上用于：可以补视野或侧压英雄。
- 如果 `我方阵容依赖中心墙体`，则 `不要无脑破墙`；BP 上用于：只在能转远程压制时开墙。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
