# Open Business

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Hot Zone`
- Fandom URL：https://brawlstars.fandom.com/wiki/Open_Business
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Open Business
  mode: Hot Zone
  summary: 单圈低掩体但核心墙靠近热区，区域压制、投掷口袋、炮台锚点和反区域突进都重要。
  topology:
    key_points:
      - 单一热区附近有墙体簇，能保护投掷、炮台或区域技能。
      - 外围较开，长手可从圈外压制站圈者。
      - 墙体也给突进绕近和反投掷窗口。
  objective_access:
    objective_type: zone
    stable_goal: 目标是既能站圈，又能处理圈旁墙体后的控制点；只在外围消耗不够。
  tactical_features:
    - id: single_zone_near_wall_clusters
      type: zone_anchor
      location: zone_adjacent_walls
      condition: 热区旁墙体提供低风险控圈点
      combat_effect:
        rewards_capabilities: [area_denial, thrower_wall_pocket, turret_anchor, zone_sustain]
        punishes_capabilities: [bush_dependent_tank_without_zone_access]
        false_positive_capabilities: [thrower_if_enemy_has_easy_dive]
      objective_effect:
        payoff: 可把墙后控制转化为站圈时间
      draft_implication:
        bp_use: 先手重视区域压制和站圈稳定
    - id: low_cover_open_attack_side
      type: long_sightline
      location: open_approach_sides
      condition: 外围低掩体让远程能惩罚站圈
      combat_effect:
        rewards_capabilities: [long_range_zone_pressure, anti_tank_poke, wall_break_followup]
        punishes_capabilities: [slow_melee_crossing_open]
        false_positive_capabilities: [sniper_that_never_steps_zone]
      objective_effect:
        payoff: 给反圈方消耗入口
      draft_implication:
        bp_use: 远程必须能配合队友占圈
    - id: anti_area_denial_dive_window
      type: dive_window
      location: wall_cluster_edges
      condition: 墙体控制点也会被突进/开墙反制
      combat_effect:
        rewards_capabilities: [anti_thrower_dive, wall_break_transform, close_range_clear]
        punishes_capabilities: [static_thrower_no_peel]
        false_positive_capabilities: [dive_into_full_team_zone]
      objective_effect:
        payoff: 让后手能打破对方区域锁
      draft_implication:
        bp_use: BP 需要保留反区域答案
  lane_dynamics:
    notes:
      - 围绕单圈展开，远程消耗和身体站圈必须同时满足。
      - 墙体完整时投掷/炮台强，开墙后远程和突进更容易清点。
      - 敌方区域技能越多，反区域/开墙越重要。
  map_rules:
    - if: 敌方拿到墙后投掷/炮台
      then: 必须有开墙、突进或更强区域清除
      because: 否则热区被持续覆盖
      bp_use: must_answer area denial
    - if: 我方只有圈外远程
      then: 计分不足
      because: Hot Zone 需要实际站圈
      bp_use: 补 sustain 或 zone body
    - if: 敌方无 anti-dive
      then: 反区域突进可作为后手
      because: 墙后控制点会被贴脸清除
      bp_use: last pick dive/clear
  false_positive:
    - 名字叫 Open Business，但不能当成纯开放图；圈旁墙体决定很多对位。
    - 投掷如果无队友站圈，只能拖时间不能赢分。
```

## BP 用法

- 如果 `敌方拿到墙后投掷/炮台`，则 `必须有开墙、突进或更强区域清除`；BP 上用于：must_answer area denial。
- 如果 `我方只有圈外远程`，则 `计分不足`；BP 上用于：补 sustain 或 zone body。
- 如果 `敌方无 anti-dive`，则 `反区域突进可作为后手`；BP 上用于：last pick dive/clear。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
