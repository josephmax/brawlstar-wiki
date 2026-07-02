# Out in the Open

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Knockout`
- Fandom URL：https://brawlstars.fandom.com/wiki/Out_in_the_Open
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Out in the Open
  mode: Knockout
  summary: 开阔中路、少量墙草、跳板/水域角度让狙击优先，同时保留开墙、机动和隔水互动。
  topology:
    key_points:
      - 中路非常开阔，远程能从开局就影响空间。
      - 少量墙草提供临时遮挡和绕线。
      - 水域/跳板等特殊路线允许机动英雄改变站位。
  objective_access:
    objective_type: knockout_space
    stable_goal: Knockout 中远程先拿空间，但后手可用开墙、机动或特殊路线惩罚孤立站位。
  tactical_features:
    - id: open_mid_marksman
      type: long_sightline
      location: open_mid
      condition: 开阔中路奖励远程命中和低风险消耗
      combat_effect:
        rewards_capabilities: [marksman_range, projectile_reliability, long_range_support]
        punishes_capabilities: [melee_without_jump_or_cover]
        false_positive_capabilities: [sniper_without_escape_against_mobility]
      objective_effect:
        payoff: 远程可提前压缩敌方空间
      draft_implication:
        bp_use: 先手稳定远程价值高
    - id: wall_break_route_creation
      type: wall_break_transform
      location: minor_wall_grass
      condition: 开墙能进一步消除临时掩体或创造追击路线
      combat_effect:
        rewards_capabilities: [wall_break, range_snowball, anti_cover]
        punishes_capabilities: [cover_dependent_thrower, short_range_cover_use]
        false_positive_capabilities: [overbreak_if_enemy_range_better]
      objective_effect:
        payoff: 让长线优势扩大
      draft_implication:
        bp_use: 开墙要看双方远程质量
    - id: water_angle_and_retreat
      type: river_crossing
      location: water_edges
      condition: 水域提供隔水角度和撤退路径
      combat_effect:
        rewards_capabilities: [water_crossing_with_range, retreat_angle, mobility_reposition]
        punishes_capabilities: [normal_walk_short_range]
        false_positive_capabilities: [water_crossing_without_range]
      objective_effect:
        payoff: 给特定英雄安全换角度
      draft_implication:
        bp_use: 不应把所有过水英雄都视为强
    - id: mobility_flank_window
      type: engage_route
      location: jump_or_side_routes
      condition: 机动英雄可惩罚站位过散或无 peel 的远程
      combat_effect:
        rewards_capabilities: [dash_engage, jump_route, last_pick_punish_no_peel]
        punishes_capabilities: [blind_melee_into_open]
        false_positive_capabilities: [mobility_without_burst_confirm]
      objective_effect:
        payoff: 作为最后手高上限惩罚
      draft_implication:
        bp_use: 必须确认敌方剩余无法低成本回答
  lane_dynamics:
    notes:
      - 远程默认强，站位分散以避免被多目标技能惩罚。
      - 少量掩体被开后，生存压力更集中在走位和射程。
      - 机动最后手可以存在，但早手暴露风险很高。
  map_rules:
    - if: 我方缺远程基本面
      then: BP 难成立
      because: 地图开阔让短手接近成本高
      bp_use: 优先补 marksman_range
    - if: 敌方远程无位移/无 peel
      then: 机动后手可惩罚
      because: 开阔站位会让孤立目标暴露
      bp_use: last pick engage
    - if: 候选靠水域但无射程
      then: 不应高估
      because: 隔水路线需要输出或撤退价值
      bp_use: 标记 false_positive
  false_positive:
    - 短手不能因为“能跳/能冲”就默认成立；需要击杀确认和撤退路线。
    - 过水英雄如果手短，通常无法把角度转成实际击杀。
```

## BP 用法

- 如果 `我方缺远程基本面`，则 `BP 难成立`；BP 上用于：优先补 marksman_range。
- 如果 `敌方远程无位移/无 peel`，则 `机动后手可惩罚`；BP 上用于：last pick engage。
- 如果 `候选靠水域但无射程`，则 `不应高估`；BP 上用于：标记 false_positive。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
