# Center Stage

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Brawl Ball`
- Fandom URL：https://brawlstars.fandom.com/wiki/Center_Stage
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Center Stage
  mode: Brawl Ball
  summary: 中心草、侧草和球门入口让抢球、草控、推进、反 aggro 与得分手能力共同决定 BP。
  topology:
    key_points:
      - 球在中路附近，中心草丛决定开局抢球和中路视野。
      - 侧路草带允许绕后、持球突进和切断传球。
      - 球门附近需要清墙/控人/得分窗口配合。
  objective_access:
    objective_type: goal
    stable_goal: Brawl Ball 的目标不是杀人，而是制造持球推进、破门或强控得分窗口。
  tactical_features:
    - id: center_grass_ball_fight
      type: grass_anchor
      location: center_grass
      condition: 中心草影响开局抢球和中路控制
      combat_effect:
        rewards_capabilities: [grass_control, wide_spread, anti_aggro, ball_pickup_pressure]
        punishes_capabilities: [pure_marksman_without_grass_control]
        false_positive_capabilities: [tank_if_enemy_has_constant_sweep]
      objective_effect:
        payoff: 让先手节奏和球权归属变化
      draft_implication:
        bp_use: BP 需要至少一个能处理中心草的人
    - id: side_bush_strip
      type: flank_route
      location: side_bush_lanes
      condition: 侧草允许绕后切传球线或持球突进
      combat_effect:
        rewards_capabilities: [flank_pressure, speed_gear, scorer_pressure, bush_reveal]
        punishes_capabilities: [slow_rotation, static_mid_stack]
        false_positive_capabilities: [flanker_without_ball_followup]
      objective_effect:
        payoff: 制造边路突破和夹击
      draft_implication:
        bp_use: 适合作为第二层推进计划
    - id: goal_entry_pressure
      type: score_window
      location: goal_approach
      condition: 进球需要控人、破门或位移创造窗口
      combat_effect:
        rewards_capabilities: [wall_break_for_goal, knockback, stun, dash_scorer, area_control_on_goal]
        punishes_capabilities: [kill_only_no_ball_pressure]
        false_positive_capabilities: [wall_break_when_enemy_has_better_dps_after_opening]
      objective_effect:
        payoff: 把线权转化为得分
      draft_implication:
        bp_use: 候选必须说明如何参与得分，而非只打伤害
  lane_dynamics:
    notes:
      - 中路争球，边路负责草丛侧压和得分线路。
      - 加时或破墙后长手价值上升，但前期仍要处理草丛。
      - 队伍必须有至少一条明确得分路径。
  map_rules:
    - if: 候选只会远程消耗不会处理草
      then: 前期球权不稳定
      because: 中心草会遮蔽开局和持球路线
      bp_use: 补草控/宽攻击
    - if: 敌方缺 anti-aggro
      then: 侧草持球和突进得分升值
      because: 草带提供接近和传球切线
      bp_use: 可用 scorer pressure 惩罚
    - if: 我方无破门/强控/位移
      then: 不要只按击杀阵容 draft
      because: Brawl Ball 需要把优势转成进球
      bp_use: 补 scoring window creator
  false_positive:
    - 纯击杀优势不等于能进球。
    - 长手如果无法处理草丛，前期会被侧草持续压缩。
```

## BP 用法

- 如果 `候选只会远程消耗不会处理草`，则 `前期球权不稳定`；BP 上用于：补草控/宽攻击。
- 如果 `敌方缺 anti-aggro`，则 `侧草持球和突进得分升值`；BP 上用于：可用 scorer pressure 惩罚。
- 如果 `我方无破门/强控/位移`，则 `不要只按击杀阵容 draft`；BP 上用于：补 scoring window creator。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
