# Belle's Rock

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Knockout`
- Fandom URL：https://brawlstars.fandom.com/wiki/Belle%27s_Rock
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Belle's Rock
  mode: Knockout
  summary: 三路棋盘墙体、L 墙、投掷口袋、弹墙收益和破墙反制构成 Knockout 的核心三角。
  topology:
    key_points:
      - 多组墙体把三路切成小掩体和窄口。
      - 投掷和弹墙能从安全位置施压。
      - 破墙会显著改变所有对位，让线性远程重新接管。
  objective_access:
    objective_type: knockout_space
    stable_goal: Knockout 重视生存和缩圈前空间；墙体完整时控场强，墙体破后远程强。
  tactical_features:
    - id: checkered_wall_three_lanes
      type: thrower_pocket
      location: three_lane_wall_grid
      condition: 棋盘式墙体制造大量投掷与弹墙口袋
      combat_effect:
        rewards_capabilities: [thrower_pocket, path_blocking, bounce_wall, area_denial]
        punishes_capabilities: [linear_marksman_if_walls_intact]
        false_positive_capabilities: [thrower_if_enemy_has_unanswered_wallbreak]
      objective_effect:
        payoff: 能在不暴露身位的情况下压缩敌方空间
      draft_implication:
        bp_use: 先手强控但要防开墙
    - id: wall_break_counterplay
      type: wall_break_transform
      location: central_and_side_walls
      condition: 开墙会削弱投掷保护并打开长线
      combat_effect:
        rewards_capabilities: [wall_break, anti_thrower_angle, range_after_opening]
        punishes_capabilities: [static_thrower, wall_dependent_bounce]
        false_positive_capabilities: [overbreak_when_our_team_needs_cover]
      objective_effect:
        payoff: 改变地图对位结构
      draft_implication:
        bp_use: 中后手最关键回答之一
    - id: assassin_route_condition
      type: conditional_engage
      location: side_chokes_and_walls
      condition: 刺客能否克制投掷取决于墙草是否提供接近路线
      combat_effect:
        rewards_capabilities: [route_based_assassin, dash_through_choke, last_pick_no_peel]
        punishes_capabilities: [blind_assassin_into_closed_choke]
        false_positive_capabilities: [assassin_named_counter_without_route]
      objective_effect:
        payoff: 给最后手高上限反制窗口
      draft_implication:
        bp_use: 不能把刺客克投掷写成无条件
  lane_dynamics:
    notes:
      - 墙完整时投掷/弹墙/封路强；开墙后长线强。
      - Knockout 每次死亡不可恢复，突进必须有路线和击杀确认。
      - 缩圈前保空间比盲目追击更重要。
  map_rules:
    - if: 敌方投掷/弹墙成型
      then: 开墙或强路线刺客必须考虑
      because: 墙体让其低风险输出
      bp_use: must_answer wall pocket
    - if: 我方依赖投掷控场
      then: ban/answer 开墙英雄价值上升
      because: 开墙会直接拆地图基本面
      bp_use: 保护墙体计划
    - if: 想选刺客打投掷
      then: 必须确认接近路线和敌方无 peel
      because: 窄口会让刺客被预判
      bp_use: 适合作最后手
  false_positive:
    - 刺客不是无条件反投掷；在过道明确、入口被控时会送头。
    - 开墙也不是无条件收益；己方若靠墙体生存会被一起削弱。
```

## BP 用法

- 如果 `敌方投掷/弹墙成型`，则 `开墙或强路线刺客必须考虑`；BP 上用于：must_answer wall pocket。
- 如果 `我方依赖投掷控场`，则 `ban/answer 开墙英雄价值上升`；BP 上用于：保护墙体计划。
- 如果 `想选刺客打投掷`，则 `必须确认接近路线和敌方无 peel`；BP 上用于：适合作最后手。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
