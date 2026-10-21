# Deathcap Trap

## 基础信息

- 模式：`Gem Grab`
- 来源：[[sources/Fandom-Deathcap-Trap|Fandom Deathcap Trap]]，Layout / Tips；LCQ 使用事实见 [[sources/Liquipedia-Brawl-Stars-Championship-2026-Last-Chance-Qualifier|2026 LCQ]]。
- 同名 Bounty 版独立存在；本页合同只描述 Gem Grab。

## 稳定地图结构

```yaml
map_profile:
  name: Deathcap Trap
  mode: Gem Grab
  summary: 对角对称；开阔中央矿区与四侧 Z 形草路线交汇，横墙后可部署，角落孤草不保证安全退出。
  topology:
    key_points:
      - 中央开阔，矿区上下方各有小草片。
      - 中央四侧的 Z 形草与中心连接；角落另有藏身草。
      - 以己方视角，左路可进入敌侧 Z 草；右侧较开放但有局部墙簇。
  objective_access:
    objective_type: gem_mine
    stable_goal: 把中央持续射线与 Z 草探查结合，保证夺矿和持钻后撤；不可把横墙部署点当作全图遮蔽。
  tactical_features:
    - id: center_mine_crossfire
      type: objective_sightline
      location: 开阔中央矿区及其上下小草片
      condition: 中路线权尚未被侧草夹击，队友能提供持续探查
      combat_effect:
        rewards_capabilities: [mid_range_lane_pressure, ranged_poke, bush_sweep]
        punishes_capabilities: [unsupported_short_range_entry]
        false_positive_capabilities: [open_center_means_no_flank]
      objective_effect:
        payoff: 从矿区外封住取钻窗口并保留向己方 Z 草侧后撤的射线
      draft_implication:
        bp_use: required_capabilities.mine_control_and_flank_awareness
    - id: connected_z_bush_flank
      type: connected_bush_route
      location: 四侧 Z 形草与中央连接口
      condition: 路线未被扫清，进入点与撤退点有队友覆盖
      combat_effect:
        rewards_capabilities: [scouting_or_vision, anti_aggro, route_based_engage]
        punishes_capabilities: [blind_carrier_rotation]
        false_positive_capabilities: [bush_count_auto_tank_fit]
      objective_effect:
        payoff: 侧路压迫矿区、探明持钻撤退方向；代价是走出草后会暴露于中央交叉火力
      draft_implication:
        bp_use: map_bp_factors.connected_flank_and_carrier_retreat
    - id: horizontal_wall_deployment_anchor
      type: protected_resource_anchor
      location: 己方 Z 草内横墙后
      condition: 部署物范围能覆盖己方侧线，敌方没有直接跨墙清除资源
      combat_effect:
        rewards_capabilities: [spawnable_or_pet, team_support]
        punishes_capabilities: [static_anchor_without_vision]
        false_positive_capabilities: [protected_turret_is_unremovable]
      objective_effect:
        payoff: 以墙后资源支持两侧换血，接住 carrier 退线
      draft_implication:
        bp_use: terrain_state_plan.resource_anchor_with_clear_check
  lane_dynamics:
    notes:
      - 持钻者避免退入没有出口证据的角落孤草；探草后再转线。
      - 开墙可能强化中央远射线，也可能拆掉己方部署物保护，须明确受益队伍。
  map_rules: []
  false_positive:
    - 有草不等于可安全贴脸，必须证明与矿区相连的进出路线未被扫清。
    - 中央开阔不等于纯狙击场；Z 草侧翼必须有探查或反突进。
    - Bounty 同名地图不能继承本页的夺矿或持钻职责。
```

## 关联

- [[sources/Fandom-Deathcap-Trap]]
- [[concepts/Gem Grab]]
