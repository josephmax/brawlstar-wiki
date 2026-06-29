# Flaring Phoenix

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Knockout`
- Fandom URL：https://brawlstars.fandom.com/wiki/Flaring_Phoenix
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- Schema：[[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Flaring Phoenix
  mode: Knockout
  summary: 窄路、中心墙、侧水草和伏击路线让狙击、投掷、突进与反突进同时成立，取决于路线是否被打开。
  topology:
    key_points:
      - 窄路让远程命中和封路技能收益提高。
      - 中心墙体保护投掷/控场，也为突进提供接近路径。
      - 侧水草提供伏击或角度，但需要可利用能力。
  objective_access:
    objective_type: knockout_space
    stable_goal: Knockout 需要先控空间再拿击杀；窄路放大单次技能和突进时机。
  tactical_features:
    - id: narrow_lane_marksman_value
      type: long_sightline
      location: narrow_main_lanes
      condition: 窄路让远程和线性技能更容易命中
      combat_effect:
        rewards_capabilities: [narrow_lane_range, projectile_reliability, long_linear_control]
        punishes_capabilities: [slow_dodge_brawler, unsupported_thrower_in_open]
        false_positive_capabilities: [sniper_without_peel_against_dash]
      objective_effect:
        payoff: 低承诺消耗能压缩敌方空间
      draft_implication:
        bp_use: 远程先手价值高但需防突进
    - id: central_wall_thrower_control
      type: thrower_pocket
      location: central_walls
      condition: 中心墙让投掷和区域技能可封路
      combat_effect:
        rewards_capabilities: [thrower_area_control, choke_blocking, wall_bypass]
        punishes_capabilities: [linear_push_if_walls_intact]
        false_positive_capabilities: [thrower_without_anti_dive]
      objective_effect:
        payoff: 阻止敌方穿过窄口
      draft_implication:
        bp_use: 后手需要开墙或突进答案
    - id: side_water_bush_ambush
      type: river_crossing
      location: side_water_bush
      condition: 侧水草提供特殊角度和伏击路线
      combat_effect:
        rewards_capabilities: [water_angle, bush_ambush, dash_engage, retreat_angle]
        punishes_capabilities: [pure_ground_short_range]
        false_positive_capabilities: [water_crossing_without_range_or_escape]
      objective_effect:
        payoff: 可绕开正面窄路
      draft_implication:
        bp_use: 必须验证过水/伏击后的击杀和撤退
    - id: dash_to_mid_pressure
      type: engage_route
      location: mid_choke_edges
      condition: 位移英雄可利用窄口惩罚孤立远程或投掷
      combat_effect:
        rewards_capabilities: [dash_engage, burst_confirm, anti_sniper_pressure]
        punishes_capabilities: [stationary_sniper_no_peel]
        false_positive_capabilities: [dash_into_full_control]
      objective_effect:
        payoff: 让远程不能无脑站线
      draft_implication:
        bp_use: 高风险后手，依赖敌方阵容缺控制
  lane_dynamics:
    notes:
      - 正面窄路远程和投掷强，侧路水草提供变线。
      - 突进必须等敌方控制交掉或路线打开。
      - 队伍需要同时处理长线和墙后控制。
  map_rules:
    - if: 敌方三远程无 peel
      then: 突进/侧路伏击升值
      because: 窄路让远程强但也容易被强开
      bp_use: last pick engage
    - if: 敌方中心投掷封路
      then: 需要开墙或水草绕路
      because: 正面穿窄口会持续亏血
      bp_use: must_answer central wall
    - if: 候选可过水但无射程/撤退
      then: 不自动强
      because: 侧水草只是路线，不保证击杀
      bp_use: 标记条件适配
  false_positive:
    - 只按“狙击图”处理会忽略中心墙和侧水草。
    - 只按“突进图”处理也错；窄路被控时突进会被预判。
```

## BP 用法

- 如果 `敌方三远程无 peel`，则 `突进/侧路伏击升值`；BP 上用于：last pick engage。
- 如果 `敌方中心投掷封路`，则 `需要开墙或水草绕路`；BP 上用于：must_answer central wall。
- 如果 `候选可过水但无射程/撤退`，则 `不自动强`；BP 上用于：标记条件适配。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
