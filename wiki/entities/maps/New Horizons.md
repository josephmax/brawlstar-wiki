# New Horizons

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Knockout`
- Fandom URL：https://brawlstars.fandom.com/wiki/New_Horizons
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: New Horizons
  mode: Knockout
  summary: 中央墙草和角落水域提供初始掩体与路线，但破墙会让短手路线迅速失效，地图形态变化很大。
  topology:
    key_points:
      - 中心障碍和草丛提供早期控场和接近路线。
      - 角落水域给部分英雄隔水角度或绕行可能。
      - 破墙后地图更开放，短手和投掷保护下降。
  objective_access:
    objective_type: knockout_space
    stable_goal: Knockout 中先控中心墙草能拿空间；但双方若有开墙，地图会转为远程和视野对抗。
  tactical_features:
    - id: central_obstacle_wall_bush
      type: central_cover
      location: center_walls_bushes
      condition: 中心墙草提供早期掩体、伏击和控场
      combat_effect:
        rewards_capabilities: [mid_control_if_walls_intact, thrower_pocket, bush_ambush, area_control]
        punishes_capabilities: [linear_marksman_if_walls_intact]
        false_positive_capabilities: [short_range_after_wall_break]
      objective_effect:
        payoff: 帮助队伍占空间和逼退敌方
      draft_implication:
        bp_use: 先手应考虑敌方开墙惩罚
    - id: corner_water_route
      type: river_crossing
      location: corner_water
      condition: 角落水域提供隔水角度或特殊路线
      combat_effect:
        rewards_capabilities: [water_angle, range_over_water, water_crossing_with_range]
        punishes_capabilities: [normal_walk_short_range]
        false_positive_capabilities: [water_crossing_without_pressure]
      objective_effect:
        payoff: 让特定英雄从非正面角度施压
      draft_implication:
        bp_use: 仍需证明能打到人或保命
    - id: wall_break_denies_short_range
      type: wall_break_transform
      location: central_walls
      condition: 破墙会削弱短手、投掷和草丛伏击
      combat_effect:
        rewards_capabilities: [wall_break_answer, range_after_opening, anti_thrower]
        punishes_capabilities: [short_range_after_wall_break, thrower_pocket_after_open]
        false_positive_capabilities: [opening_walls_if_our_comp_is_short_range]
      objective_effect:
        payoff: 把地图转成远程对枪
      draft_implication:
        bp_use: BP 中开墙既是答案也是风险
  lane_dynamics:
    notes:
      - 早期围绕中心墙草抢空间，中后期可能因破墙转长线。
      - 短手/投掷必须考虑墙体能否被保住。
      - 水域角度是附加路线，不是主胜利条件。
  map_rules:
    - if: 我方依赖中心墙草
      then: 必须评估敌方开墙威胁
      because: 墙破后英雄价值会急剧下降
      bp_use: ban/answer wall_break
    - if: 敌方短手和投掷抢中心
      then: 开墙可直接拆计划
      because: 中心墙草是其生存基础
      bp_use: response pick wall_break
    - if: 候选只因水域被加分
      then: 需要目标压力证明
      because: 角落水域不自动影响主战场
      bp_use: 标记为条件适配
  false_positive:
    - 短手在墙完整时可用，不代表墙被破后还能打。
    - 水域角度如果不能影响中心空间或击杀，不应高估。
```

## BP 用法

- 如果 `我方依赖中心墙草`，则 `必须评估敌方开墙威胁`；BP 上用于：ban/answer wall_break。
- 如果 `敌方短手和投掷抢中心`，则 `开墙可直接拆计划`；BP 上用于：response pick wall_break。
- 如果 `候选只因水域被加分`，则 `需要目标压力证明`；BP 上用于：标记为条件适配。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
