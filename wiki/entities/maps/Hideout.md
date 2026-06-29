# Hideout

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Bounty`
- Fandom URL：https://brawlstars.fandom.com/wiki/Hideout
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Hideout
  mode: Bounty
  summary: 中央墙草与开放边线并存，投掷、狙击、破草和炮台都能成立，但取决于分路与掩体状态。
  topology:
    key_points:
      - 中部有墙草簇，能保护投掷和中距离控场。
      - 边线更开放，长射程能建立安全星差。
      - 草丛/墙体被破会改变投掷和短手的可用性。
  objective_access:
    objective_type: bounty_star
    stable_goal: Bounty 要在拿星后保命；中路控墙和边路远程同时提供得分路线。
  tactical_features:
    - id: central_wall_grass_clumps
      type: thrower_pocket
      location: center_wall_bush
      condition: 中路墙草保护投掷、炮台和控场
      combat_effect:
        rewards_capabilities: [thrower_wall_control, protected_turret, area_denial, bush_clear]
        punishes_capabilities: [linear_marksman_if_walls_intact]
        false_positive_capabilities: [thrower_without_anti_dive_when_side_lost]
      objective_effect:
        payoff: 可通过墙体影响星星争夺区
      draft_implication:
        bp_use: 敌方若无开墙/突进，投掷会持续压制
    - id: open_side_marksman_lane
      type: long_sightline
      location: open_side_lane
      condition: 开放边路允许狙击和远程支援低风险拿星
      combat_effect:
        rewards_capabilities: [side_lane_marksman, long_range_support, projectile_reliability]
        punishes_capabilities: [short_range_side_lane]
        false_positive_capabilities: [sniper_if_center_thrower_unanswered]
      objective_effect:
        payoff: 边路远程可迫使敌方不敢集中中路
      draft_implication:
        bp_use: 需要防中路投掷切断支援
    - id: bush_destroy_priority
      type: terrain_denial
      location: central_and_side_bushes
      condition: 破草会削弱伏击和中路隐藏
      combat_effect:
        rewards_capabilities: [bush_clear, wall_break, vision_reveal]
        punishes_capabilities: [bush_dependent_assassin, hidden_thrower]
        false_positive_capabilities: [destroying_own_retreat_cover_when_ahead]
      objective_effect:
        payoff: 减少敌方偷星和倒计时追击
      draft_implication:
        bp_use: 领先方可用地形否定保星
  lane_dynamics:
    notes:
      - 中路投掷/控场与边路狙击并行，缺一边容易被对手单点突破。
      - 墙草完整时投掷更强，开墙后边路长线更强。
      - 领先后要优先保星，不要让中路草丛给敌方突袭窗口。
  map_rules:
    - if: 敌方中路投掷无人能处理
      then: 必须补开墙、突进或反投掷
      because: 否则中路星星区域会被封锁
      bp_use: must_answer thrower_pocket
    - if: 敌方只有长线无中路处理
      then: 可用墙草控场压缩视野
      because: 中路墙体会切断远程支援
      bp_use: response pick thrower/control
    - if: 我方领先
      then: 破草和保命价值高于继续进攻
      because: Bounty 翻盘来自隐蔽接近和多杀
      bp_use: 地形否定可变成胜利条件
  false_positive:
    - 不能把 Hideout 简化成纯狙击图；中路墙草足以让投掷改变对位。
    - 也不能简化成投掷图；边路开放会惩罚无保护投掷。
```

## BP 用法

- 如果 `敌方中路投掷无人能处理`，则 `必须补开墙、突进或反投掷`；BP 上用于：must_answer thrower_pocket。
- 如果 `敌方只有长线无中路处理`，则 `可用墙草控场压缩视野`；BP 上用于：response pick thrower/control。
- 如果 `我方领先`，则 `破草和保命价值高于继续进攻`；BP 上用于：地形否定可变成胜利条件。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
