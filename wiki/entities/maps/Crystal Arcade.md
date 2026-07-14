# Crystal Arcade

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Gem Grab`
- Fandom URL：https://brawlstars.fandom.com/wiki/Crystal_Arcade
- 来源：[[sources/Fandom-BSC-July-2026-Observed-Map-Pages|Fandom 来源摘要: BSC 2026 July 赛事补充地图页]]
- 赛事证据：[[sources/Liquipedia-Brawl-Stars-Championship-2026-July-EMEA-Monthly-Finals|BSC 2026 July EMEA]]、[[sources/Liquipedia-Brawl-Stars-Championship-2026-July-South-America-Monthly-Finals|BSC 2026 July South America]]
- 适配复核：[[sources/BSC-2026-July-Observed-Map-Fit-Review|BSC 2026 July 三张补充地图的适配复核]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-07-14

## BP-ready map_profile

```yaml
map_profile:
  name: Crystal Arcade
  mode: Gem Grab
  summary: 中央四组 2x2 墙、面向双方的草、向内弯曲的侧草与四角大草簇，让控矿、墙边范围压力、探草、侧夹和地形保留同时成为 BP 任务。
  topology:
    key_points:
      - 四组 2x2 墙围绕中央宝石矿，墙前草丛让中路接触不是纯开放对枪。
      - 两侧竖墙与向内弯曲的草连接到地图边缘，形成可绕中路的侧压路线。
      - 四角大草簇与出生点小墙提供撤退和伏击点，但也可能在落后追击时困住 carrier。
  objective_access:
    objective_type: gem_mine
    stable_goal: 先控制中央墙边与侧草视野，再把线权转成收宝、保护 carrier 和封锁倒计时撤退路线。
  tactical_features:
    - id: four_center_wall_pockets
      type: center_wall_control
      location: four_2x2_walls_around_gem_mine
      condition: 中央墙体完整，目标必须从墙边或墙间入口接近宝石矿
      combat_effect:
        rewards_capabilities: [gem_mid_control, through_wall_or_over_wall_pressure, bounce_wall, spawnable_or_pet, wide_spread]
        punishes_capabilities: [pure_linear_shooter_without_side_control]
        false_positive_capabilities: [thrower_without_flank_protection]
      objective_effect:
        payoff: 从墙侧低风险影响矿区，并迫使对方在进入收宝前交弹药或绕路
      draft_implication:
        bp_use: 阵容至少需要墙边处理或侧路入口，不能只靠正面长线
    - id: curved_side_bush_routes
      type: grass_flank_route
      location: vertical_side_walls_and_inward_curving_bushes
      condition: 侧草未被持续扫除，边路可以绕开中央墙面火力
      combat_effect:
        rewards_capabilities: [grass_flank, bush_sweep, scouting_or_vision, mid_survivability]
        punishes_capabilities: [isolated_slow_carrier]
        false_positive_capabilities: [short_range_without_scout_or_exit]
      objective_effect:
        payoff: 从侧面夹击中路、逼 carrier 离开安全墙角或保护己方撤退
      draft_implication:
        bp_use: 中后手要同时检查侧路接近和反草能力
    - id: corner_bush_retreat_and_pinches
      type: carrier_retreat_pocket
      location: four_corner_bush_clusters_and_spawn_walls
      condition: 领先方退入角草，追击方必须从有限方向进入
      combat_effect:
        rewards_capabilities: [carrier_safety, bush_sweep, area_control, pinch_pressure]
        punishes_capabilities: [single_angle_chase]
        false_positive_capabilities: [retreat_without_side_lane_control]
      objective_effect:
        payoff: 领先方可保倒计时，但侧路全失时角草会变成困点
      draft_implication:
        bp_use: carrier 与护送不能同时缺视野或脱离工具
    - id: preserve_or_open_center_walls
      type: terrain_state_choice
      location: enemy_and_friendly_2x2_center_walls
      condition: 破墙会移除控制/坦克的接近资源，也会扩大远程交叉火力
      combat_effect:
        rewards_capabilities: [controlled_wall_break, long_range_after_opening, terrain_preservation]
        punishes_capabilities: [automatic_wall_break]
        false_positive_capabilities: [overbreaking_if_our_comp_needs_cover]
      objective_effect:
        payoff: 正确的地形选择能保护己方收宝路线或拆掉敌方墙边控制点
      draft_implication:
        bp_use: 开墙前必须比较双方远程与短手对地形的净收益
  lane_dynamics:
    notes:
      - 中路负责控矿和 carrier 安全，边路负责探草、侧夹与阻止角草撤退。
      - 墙体完整时范围、召唤物、弹射和穿墙压力更稳定；开墙后长线和交叉火力权重上升。
      - 草多不等于纯短手图；持续扫草和中距离控制会显著提高短手接近成本。
  map_rules:
    - if: 我方没有墙边处理或侧路入口
      then: 只靠中路直线对枪难以稳定收宝
      because: 四组中央墙会切断单一射线
      bp_use: 补 through-wall、bounce、wide-spread 或可验证的侧草路线
    - if: 敌方 carrier 退入角草
      then: 先保住两侧出口再扫草
      because: 单角追击容易被墙草反打或拖完倒计时
      bp_use: 需要 pinch_pressure 与 bush_sweep
    - if: 我方阵容依赖中央墙接近
      then: 不应默认破掉敌方 2x2 墙
      because: 破墙可能让对方远程接管矿区并移除我方掩体
      bp_use: terrain_state_plan.preserve_or_selective_break
  false_positive:
    - Fandom 的推荐英雄只能作为机制提示，不能直接变成当前 tier 或候选表。
    - 四角和侧边草提供路线，但没有探草、续航或出口计划的低血短手仍可能被卡死。
```

## BP 用法

- 中央墙完整时优先覆盖墙边控制、探草和侧路；开墙后再转为长线交叉火力。
- 领先方可利用角草保倒计时，但必须保住两侧出口；落后方要先形成夹击再扫草。
- 破墙是双向地形选择，不是自动正收益。

## 变动层边界

本页只记录稳定地图结构和能力交互。赛事 pick / ban 频率保留在 Liquipedia 来源与 observation profile，不写成当前强势英雄列表。
