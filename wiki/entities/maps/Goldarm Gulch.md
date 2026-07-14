# Goldarm Gulch

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Knockout`
- Fandom URL：https://brawlstars.fandom.com/wiki/Goldarm_Gulch
- 来源：[[sources/Fandom-BSC-July-2026-Observed-Map-Pages|Fandom 来源摘要: BSC 2026 July 赛事补充地图页]]
- 赛事证据：[[sources/Liquipedia-Brawl-Stars-Championship-2026-July-EMEA-Monthly-Finals|BSC 2026 July EMEA]]
- 适配复核：[[sources/BSC-2026-July-Observed-Map-Fit-Review|BSC 2026 July 三张补充地图的适配复核]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-07-14

## BP-ready map_profile

```yaml
map_profile:
  name: Goldarm Gulch
  mode: Knockout
  summary: 中央小墙窄口、两侧长草与出生区大墙袋并存，形成隐蔽长线、投掷控制、侧路包夹和毒圈阶段从守墙转主动 collapse 的多阶段 Knockout。
  topology:
    key_points:
      - 中央被多组小墙围出窄口和短走廊，能保护投掷、穿墙和召唤物压力。
      - 两侧边缘有长草，可用于隐蔽狙击、侧压或绕过中央墙袋。
      - 出生区大墙面向中心，墙后直接连草；前期能保命，面对投掷或毒圈收缩时会变成困点。
  objective_access:
    objective_type: knockout_survival_and_first_kill
    stable_goal: 用双侧路线与中央墙压制造成第一杀，领先后保持交叉角度；毒圈收缩前必须有离开出生墙袋和处理突进的方案。
  tactical_features:
    - id: side_long_bush_sightlines
      type: concealed_long_lane
      location: both_outer_side_bushes
      condition: 侧草未被清除，长手可在草内改变出手点
      combat_effect:
        rewards_capabilities: [long_range_pressure, projectile_reliability, bush_snipe, bush_clear, scouting_or_vision]
        punishes_capabilities: [slow_mid_without_side_vision]
        false_positive_capabilities: [sniper_without_anti_flank]
      objective_effect:
        payoff: 从侧路建立低风险首杀压力并封住对方离开出生墙的角度
      draft_implication:
        bp_use: 至少一侧需要可靠长线或能逼退草内长手的手段
    - id: central_small_wall_chokes
      type: thrower_and_pierce_pocket
      location: small_wall_clusters_around_center
      condition: 中央墙组完整，目标经过窄口或停在墙后
      combat_effect:
        rewards_capabilities: [thrower_wall_control, wall_pierce, choke_control, spawnable_or_pet]
        punishes_capabilities: [linear_projectile_into_wall_pocket]
        false_positive_capabilities: [thrower_without_side_lane_control]
      objective_effect:
        payoff: 低风险压血、切断两侧支援或在毒圈前逼出位移
      draft_implication:
        bp_use: 中路控制必须和至少一侧线权绑定
    - id: spawn_wall_safe_pocket_until_smoke
      type: temporary_protected_base
      location: large_spawn_wall_and_bush
      condition: 回合前中期墙后可保护投掷/炮台，毒圈或敌方侧包尚未到达
      combat_effect:
        rewards_capabilities: [protected_turret, long_range_support, survival_plan]
        punishes_capabilities: [passive_three_backline]
        false_positive_capabilities: [camping_into_thrower_or_smoke]
      objective_effect:
        payoff: 可保存生命和资源，但不能作为全回合唯一计划
      draft_implication:
        bp_use: 阵容必须有离开墙袋、反投掷或反突进手段
    - id: dual_side_lane_collapse
      type: two_side_pressure
      location: both_side_bush_lanes_into_mid
      condition: 一侧失守后，胜线者可夹击中央或出生墙后目标
      combat_effect:
        rewards_capabilities: [side_lane_control, collapse, anti_flank_awareness, anti_dive]
        punishes_capabilities: [isolated_thrower_or_sniper]
        false_positive_capabilities: [mid_control_without_side_coverage]
      objective_effect:
        payoff: 把侧路线权转成第一杀或毒圈前的站位优势
      draft_implication:
        bp_use: 不能让中路核心同时承担双侧视野
  lane_dynamics:
    notes:
      - 早期可用墙袋保资源，中期依靠侧草和中央窄口找第一杀，后期毒圈迫使阵容离开出生墙。
      - 投掷/召唤物控制中央时需要侧路保护；纯长手也必须处理草内绕侧。
      - 高爆发突进只有在对方墙后核心孤立且落点控制不足时成立。
  map_rules:
    - if: 敌方双侧长草都能自由出枪
      then: 中路墙后核心会被交叉夹击
      because: 中央墙袋不能同时遮住两个外侧角度
      bp_use: 先补 side_lane_control 或 bush_clear
    - if: 敌方依赖出生墙后的投掷/炮台
      then: 侧包、穿墙或毒圈等待可拆掉保护
      because: 墙袋没有永久安全出口
      bp_use: response pick collapse_or_wall_pierce
    - if: 我方三人只想守出生墙
      then: 毒圈与敌方投掷会让阵容失去生存空间
      because: Knockout 后期必须主动换位
      bp_use: hard_gate survival_and_exit_plan
  false_positive:
    - 侧草不代表刺客自动强；没有落点资源或反控制时，突进仍会被中央火力集火。
    - 墙多不代表三投掷稳定；双侧路线一旦丢失，墙后低血核心会被直接 collapse。
```

## BP 用法

- 先分配双侧草线与中央墙袋职责，再决定长手、投掷或突进比例。
- 出生墙只提供阶段性保护；draft 必须通过位移、侧路线权、反投掷或 burst 准备毒圈阶段。
- 突进适合作为处理孤立墙后核心的条件后手，不适合作为无条件先手。

## 变动层边界

本页只记录稳定地形与 BP 职责。赛事中的具体英雄选择只作为复核入口，不直接成为地图强势列表。
