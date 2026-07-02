# Dueling Beetles

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Hot Zone`
- Fandom URL：https://brawlstars.fandom.com/wiki/Dueling_Beetles
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Dueling Beetles
  mode: Hot Zone
  summary: 单圈、封闭入口和草丛通道让中心占领后极难被翻，区域否定、持续站圈、炮台和破草最重要。
  topology:
    key_points:
      - 单一热区位于中心，入口受墙体和草丛限制。
      - 四周封闭路线让进圈方必须穿过可预判 chokepoint。
      - 中心被占后，炮台/区域技能能持续滚雪球。
  objective_access:
    objective_type: zone
    stable_goal: Hot Zone 的目标是持续站圈；这张图惩罚无法进圈或无法把敌人赶出圈的阵容。
  tactical_features:
    - id: single_zone_four_closed_lanes
      type: lane_funnel
      location: center_zone_entries
      condition: 多个封闭入口把进圈路线变成 choke
      combat_effect:
        rewards_capabilities: [area_denial, lane_lock, zone_sustain, knockback, slow]
        punishes_capabilities: [pure_long_range_without_zone_presence]
        false_positive_capabilities: [sniper_that_cannot_step_on_zone]
      objective_effect:
        payoff: 封门即可阻止敌方计分
      draft_implication:
        bp_use: 先手要有站圈或赶人能力
    - id: center_loss_snowball
      type: zone_snowball
      location: center_zone
      condition: 丢中心后敌方能用区域技能和炮台守住入口
      combat_effect:
        rewards_capabilities: [protected_turret, spawnable_anchor, thrower_control, bush_removal]
        punishes_capabilities: [low_area_damage]
        false_positive_capabilities: [dive_without_followup_clear]
      objective_effect:
        payoff: 中心控制会转化为持续计分
      draft_implication:
        bp_use: BP 需要重视开局抢圈和翻圈工具
    - id: grass_entry_denial
      type: grass_anchor
      location: zone_entry_bushes
      condition: 草丛入口制造伏击，也可被破草削弱
      combat_effect:
        rewards_capabilities: [bush_reveal, bush_sweep, tank_entry_with_control]
        punishes_capabilities: [blind_entry, slow_ranged_push]
        false_positive_capabilities: [tank_into_full_area_denial]
      objective_effect:
        payoff: 影响进圈时机和安全性
      draft_implication:
        bp_use: 探草/破草是翻圈资源
  lane_dynamics:
    notes:
      - 所有路线服务于中心热区，不存在远离目标的无效边路。
      - 拿圈方要守入口；丢圈方需要区域清除、开墙或强突进。
      - 长手必须能帮助站圈，不能只在圈外打消耗。
  map_rules:
    - if: 候选无法站圈也无法赶人
      then: 不适合作为核心 pick
      because: Hot Zone 计分要求身体进入目标区域
      bp_use: 优先 zone_sustain/area_denial
    - if: 敌方已经有炮台/投掷守圈
      then: 需要清场或开入口
      because: 中心一旦被锁，正面走进会被消耗
      bp_use: must_answer zone lock
    - if: 敌方缺破草/探草
      then: 草丛入口坦克或伏击升值
      because: 进入路径有隐藏空间
      bp_use: 可作为后手进圈工具
  false_positive:
    - 纯长手在圈外打得准，不等于能赢 Hot Zone。
    - 单个突进如果没有清场跟进，进圈后会被集火。
```

## BP 用法

- 如果 `候选无法站圈也无法赶人`，则 `不适合作为核心 pick`；BP 上用于：优先 zone_sustain/area_denial。
- 如果 `敌方已经有炮台/投掷守圈`，则 `需要清场或开入口`；BP 上用于：must_answer zone lock。
- 如果 `敌方缺破草/探草`，则 `草丛入口坦克或伏击升值`；BP 上用于：可作为后手进圈工具。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
