# Undermine

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Gem Grab`
- Fandom URL：https://brawlstars.fandom.com/wiki/Undermine
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Undermine
  mode: Gem Grab
  summary: 开放中路与重草侧区并存，宝石位要求稳定中路，侧路要求持续探草、防伏击和倒计时撤退管理。
  topology:
    key_points:
      - 中路较开阔，是 gem carrier 的主要活动区。
      - 左右两侧草丛很重，墙体把中路和上下区域隔开。
      - 墙体更多是障碍而不是坚固防御，侧路可以反复威胁中路。
  objective_access:
    objective_type: gem_mine
    stable_goal: 中路负责稳定拿宝石，边路负责阻止敌方从草丛推进；倒计时撤退通常依赖己方半场墙后草丛。
  tactical_features:
    - id: open_gem_mid
      type: open_objective_lane
      location: center_mine
      condition: 宝石矿区域较开阔，gem carrier 必须能稳定存活
      combat_effect:
        rewards_capabilities: [mid_survivability, medium_range_lane_control, support_heal, long_poke_with_peel]
        punishes_capabilities: [low_area_marksman, fragile_carrier_without_cover]
        false_positive_capabilities: [carrier_that_cannot_check_side_bushes]
      objective_effect:
        payoff: 提供宝石收集和中路火力交换
      draft_implication:
        bp_use: 先手应避免过度暴露且无法保护宝石的英雄
    - id: side_bush_pressure
      type: grass_flank
      location: left_and_right_bush_sections
      condition: 两侧重草允许伏击、绕后和追击倒计时宝石
      combat_effect:
        rewards_capabilities: [bush_checking, wide_attack, side_lane_bounce, ambush_burst]
        punishes_capabilities: [tunnel_vision_mid_stack]
        false_positive_capabilities: [tank_without_stealth_or_control_at_high_level]
      objective_effect:
        payoff: 边路压力直接决定中路是否能安全收宝石
      draft_implication:
        bp_use: BP 中必须配探草或可靠边路
    - id: countdown_retreat_anchor
      type: retreat_anchor
      location: own_side_bushes_behind_walls
      condition: 倒计时可撤到己方墙后草区，但也会被敌方探草惩罚
      combat_effect:
        rewards_capabilities: [escort_control, vision_reveal, anti_assassin_peel]
        punishes_capabilities: [low_mobility_carrier_if_flanked]
        false_positive_capabilities: [hiding_without_map_control]
      objective_effect:
        payoff: 给领先方提供保宝石位置
      draft_implication:
        bp_use: 落后方可用探草、跳入或拉人制造翻盘
  lane_dynamics:
    notes:
      - 一名中路 gem carrier，两侧负责防伏击和侧压。
      - 敌方边路失控时，中路英雄的理论对枪优势会被削弱。
      - 倒计时阶段地图从中路争夺转为撤退路线争夺。
  map_rules:
    - if: 我方没有探草
      then: 中路优势不稳定
      because: 侧草能让敌方突然贴到 gem carrier
      bp_use: 补 vision、wide spread 或可控边路
    - if: 敌方宝石领先并撤入己方半场草丛
      then: 需要显形、拉人或侧路突破
      because: 单纯正面推进会被墙体和草丛拖时间
      bp_use: 后手选择能破撤退锚点的英雄
    - if: 敌方短手依赖侧草
      then: 持续扫草会让其失效
      because: 高水平局不能默认短手免费接近
      bp_use: 用宽攻击、烧草或控制削弱
  false_positive:
    - 坦克在低水平可能好用，但高水平持续探草会显著降低其稳定性。
    - 只会中路对枪、不能处理侧草的英雄不适合作为单核 gem carrier。
```

## BP 用法

- 如果 `我方没有探草`，则 `中路优势不稳定`；BP 上用于：补 vision、wide spread 或可控边路。
- 如果 `敌方宝石领先并撤入己方半场草丛`，则 `需要显形、拉人或侧路突破`；BP 上用于：后手选择能破撤退锚点的英雄。
- 如果 `敌方短手依赖侧草`，则 `持续扫草会让其失效`；BP 上用于：用宽攻击、烧草或控制削弱。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
