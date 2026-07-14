# Meeple

## 基本信息

- 稀有度：Epic
- 定位：Controller
- 类型：规则区域控线 / 穿墙射击放大 / Mansions 陷阱与 Ragequit 反近身

## 来源摘要

- Fandom：[[sources/Fandom-Meeple|Fandom 来源摘要: Meeple]]
- PLP：[[sources/PLP-Meeple|PLP 来源摘要: Meeple]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Hot Zone, Bounty, Knockout

## 角色定位总结

Meeple 的 BP 价值不是纯长手对枪，而是用 `Critical Success` 把一块 10 秒区域改造成“己方投射物可穿过障碍”的规则区，再通过 `Do Not Pass Go` 提高穿墙伤害，或者用 `Rule Bending` 给队友 reload buff。Fandom 明确指出 Meeple 在完全开阔图会被 Piper、Brock、Nani、Colt、Rico、Amber、Lou、R-T、Mandy 等长线压制，真正适合的是同时有短线和长线、Super 能改变墙体收益的地图。`Mansions of Meeple` 能制造 6x6 dice wall 陷阱并打断动作，但会同时困住队友和敌人；`Ragequit` 是低血量时更强的穿墙击退/眩晕工具，尤其用于 Brawl Ball 进球窗口或 Gem Grab 逃生。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Meeple|Fandom-Meeple]]"
    plp: "[[sources/PLP-Meeple|PLP-Meeple]]"
    user_notes: none

  capability_vector:
    effective_range: long_controller; 7.67 格，普攻略微追踪最近敌人
    projectile_reliability: medium; slight_homing helps lane poke but 0.5 秒出手和 slow reload 需要路线约束
    burst: medium_high_with_Do_Not_Pass_Go_or_Mansions_trap
    sustained_dps: conditional; base reload 1.7 秒，Rule Bending 区域可给自己和队友 +20% reload
    objective_damage: low_medium; 以控线/清防守/转化目标为主，不是 Heist race 核心
    mobility: low_base_conditional_high_only_during_Hypercharged_Super_area
    survivability: low_medium; 3300 HP plus Shield gear, terrain rule zone, and Ragequit emergency peel
    engage: medium_with_Mansions_trap_or_Ragequit_goal_stun
    disengage: medium_high_with_Ragequit_if_enemy_enters_6.67_radius
    anti_aggro: conditional; Ragequit is key into aggressive comps, otherwise low HP can be punished
    anti_tank: medium_if_through_wall_damage_and_trap_force_body_to_stop
    wall_break: none
    throw_or_wall_bypass: very_high_during_Super_area; Mansions next attack becomes thrown
    area_control: high_with_Critical_Success_area_and_Mansions_wall
    scouting_or_vision: low
    team_support: high_if_allies_can_use_Super_area_or_Rule_Bending_reload
    spawnable_or_pet: none
    crowd_control: Ragequit stun_knockback; Mansions trap_and_displacement
    terrain_creation: Mansions_creates_temporary_dice_walls
    terrain_destruction: none

  build_switches:
    - build: "Mansions Of Meeple / Do Not Pass Go / Shield, Damage"
      source: "[[sources/PLP-Meeple|PLP-Meeple]]"
      changes_capabilities:
        - "Mansions 让下一次攻击变为投掷，并生成 4 秒 6x6 dice wall 陷阱，命中区造成伤害并可打断攻击或 Super"
        - "Do Not Pass Go 在穿过障碍攻击时提高伤害和 Super charge，适合把 Critical Success 当作个人击杀区"
        - "Shield/Damage 补 3300 HP 容错和低血爆发阈值"
      enables:
        - "wall_pierce_super_lane_control"
        - "trap_grouped_enemies_or_objective_route"
        - "greedy_super_kill_window"
      mitigates_failure_modes:
        - "open_map_range_mirror"
        - "slow_reload_without_rule_area"
      best_when: "地图有短线/长线混合墙体，敌方必须经过可被 Super 或 Mansions 改写的目标路线"
      poor_when: "完全开阔长线、敌方有低成本破墙/无敌盾撞墙，或我方会被 Mansions 一起困住"
      bp_use: default_rule_area_damage_build
    - build: "Ragequit anti-aggro or Brawl Ball variant"
      source: "[[sources/Fandom-Meeple|Fandom-Meeple]] / [[sources/PLP-Meeple|PLP-Meeple]]"
      changes_capabilities:
        - "Ragequit 在 6.67 格半径内穿墙击退并眩晕敌人，血量越低击退和眩晕越强，最高 1.5 秒眩晕"
        - "PLP notes 标记 GADGET 2 AGGRO，Fandom 推荐在 Brawl Ball 射门后用 Ragequit 创造免费进球窗口"
      enables:
        - "anti_aggro_emergency_peel"
        - "brawl_ball_stun_goal_window"
        - "gem_low_health_escape_or_turnaround"
      mitigates_failure_modes:
        - "direct_dive_into_low_hp"
        - "goal_front_body_block"
      best_when: "敌方有近身/突进威胁，或地图目标需要一段短眩晕来完成射门、逃生、反杀"
      poor_when: "战斗主要发生在远程开阔线，敌方不会进入 Ragequit 半径"
      bp_use: anti_aggro_or_objective_stun_variant
    - build: "Rule Bending team reload variant"
      source: "[[sources/Fandom-Meeple|Fandom-Meeple]]"
      changes_capabilities:
        - "Critical Success 区域内己方 reload speed 提高 20%，比 Do Not Pass Go 更偏队伍增益且不依赖高墙密度"
      enables:
        - "team_reload_buff_zone"
        - "ally_wall_pierce_conversion"
      mitigates_failure_modes:
        - "Meeple_personal_damage_not_enough"
      best_when: "队友投射物能在规则区内持续打目标，且阵容更需要 reload buff 而不是 Meeple 单点加伤"
      poor_when: "队友技能不能从 Super 规则中获益，或地图无法让多人安全站在区域内"
      bp_use: team_synergy_variant

  map_feature_hooks:
    - map_feature_type: wall_pierce_super_lane_control
      uses_feature_by: "Critical Success 让己方投射物穿过区域内障碍，Do Not Pass Go 提高 Meeple 穿墙伤害"
      route_or_position: "wall edge, mixed short/long sightline, round choke, gem fort doorway, or zone-adjacent cover"
      objective_conversion: "把墙体从保护敌方变成我方输出通道，逼目标离开回合线、矿区入口或热区边缘"
      active_when: "Super 区域覆盖关键墙体，Meeple/队友能安全站位并持续向目标投射"
      fails_if: "地图完全开阔、墙体被破坏后敌方长手更强，或队友投射物无法利用 Super 规则"
      example_maps:
        - Belle's Rock
        - Layer Cake
        - New Horizons
        - Gem Fort
      bp_use: map_bp_factors.rule_area_wall_pierce_conversion
    - map_feature_type: brawl_ball_ragequit_stun_goal_window
      uses_feature_by: "带球对齐球门后射门并使用 Ragequit，眩晕/击退门前防守者"
      route_or_position: "goal mouth, goal-front defender, midfield ball pickup, side grass push"
      objective_conversion: "制造短射门窗口、打断防守者清球或保护己方 scorer"
      active_when: "Meeple 能进入 Ragequit 半径且队友或本人有明确射门线"
      fails_if: "球门墙未开且无传球/破墙计划，或敌方从半径外清球、控制 Meeple"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
        - Pinball Dreams
      bp_use: slot_task.brawl_ball_stun_score_window
    - map_feature_type: hot_zone_mansions_group_trap_or_thrower_combo
      uses_feature_by: "Mansions 困住聚集敌人，配合投掷手或 Rico 在 dice wall 内反复命中"
      route_or_position: "zone entrance, grouped zone body, wall-adjacent zone edge, re-entry choke"
      objective_conversion: "延迟回区、困住站区身体、让队友投掷/弹射把陷阱转为击杀"
      active_when: "敌方多人靠近目标入口，且我方有投掷、Rico 或持续输出可惩罚被困目标"
      fails_if: "Mansions 困住己方核心、敌方破墙/无敌盾清墙，或敌方根本不聚集进入目标"
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.temporary_wall_trap_zone_combo
    - map_feature_type: gem_mid_rule_area_carrier_pressure
      uses_feature_by: "Super 穿墙区域压矿区/撤退墙边，Ragequit 可在低血追击时争取逃生或反杀"
      route_or_position: "gem mine, center wall, carrier countdown retreat, side choke"
      objective_conversion: "保护 carrier 撤退、打断敌方进矿、逼追击者穿过 Meeple 规则区"
      active_when: "矿区墙体或撤退线可被 Critical Success 改写，且 Meeple 不被迫自己长期带宝石"
      fails_if: "敌方多角度切入让低血 Meeple 无法守住区域，或 8-Bit/Mr. P/召唤物持续压缩本体"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Double Swoosh
        - Crystal Arcade
      bp_use: map_bp_factors.mine_rule_area_and_carrier_escape

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "mine_wall_pierce_control"
        - "carrier_retreat_rule_area"
        - "Ragequit_escape_or_turnaround"
      cannot_fulfill:
        - "primary_gem_carrier_against_multi_angle_aggro"
      needs_teammate_support:
        - "stable_carrier"
        - "anti_spawnable_or_anti_body_clear"
      false_positive: "能压矿区不等于能拿宝石；Meeple 低血且怕多角度追击"
    - mode: "Brawl Ball"
      can_fulfill:
        - "Ragequit_stun_score_window"
        - "goal_front_rule_area_clear"
        - "Mansions_trap_defender_if_followed_by_damage"
      cannot_fulfill:
        - "durable_primary_scorer_without_resource"
      needs_teammate_support:
        - "scorer_or_wallbreak"
        - "ball_holder_that_converts_stun"
      false_positive: "Ragequit 只制造窗口，球门几何和队友转化仍然是硬门槛"
    - mode: "Hot Zone"
      can_fulfill:
        - "zone_entry_rule_area"
        - "temporary_wall_trap"
        - "team_reload_or_thrower_combo"
      cannot_fulfill:
        - "solo_zone_body"
      needs_teammate_support:
        - "durable_zone_holder"
        - "thrower_or_Rico_combo_if_using_Mansions"
      false_positive: "Mansions 是惩罚聚集的工具，不是稳定站圈身体"
    - mode: "Bounty_or_Knockout"
      can_fulfill:
        - "mixed_sightline_wall_pierce"
        - "HP_lead_protection_from_rule_area"
        - "late_round_trap_or_Ragequit_peel"
      cannot_fulfill:
        - "open_sniper_mirror_into_dedicated_long_range"
      needs_teammate_support:
        - "peel_against_assassins"
        - "teammates_that_use_rule_area_without_overclumping"
      false_positive: "Fandom 明确警告完全开阔图会被长手压制，必须有墙体/短线让 Super 改变价值"

  failure_modes:
    - id: open_map_sniper_outclassed
      active_when: "地图完全开阔且主要胜负来自纯长线对枪"
      exposed_by: "[[sources/Fandom-Meeple|Fandom-Meeple]] Tips / Game Modes and Maps"
      mitigation: "只在短线和长线并存、Super 能改写墙体收益的图把 Meeple 计入长手候选"
      bp_use: hard_gate.map_geometry_not_pure_open
    - id: mansions_traps_allies_or_is_destroyed
      active_when: "Mansions 同时困住己方/敌方，或敌方破墙、无敌盾接触、投掷绕过 dice wall"
      exposed_by: "[[sources/Fandom-Meeple|Fandom-Meeple]] Mansions mechanics"
      mitigation: "确认己方不会被困，且有投掷/Rico/持续输出能转化被困目标"
      bp_use: false_positive_filter.temporary_wall_can_backfire
    - id: super_rule_does_not_affect_all_actions
      active_when: "队友输出是足球、以自身为 projectile 的攻击/Super，或 no travel time 攻击"
      exposed_by: "[[sources/Fandom-Meeple|Fandom-Meeple]] Critical Success mechanics"
      mitigation: "BP 中逐个检查队友是否能真实利用穿墙规则，不把 Super 视作泛用 team buff"
      bp_use: team_synergy_hard_gate
    - id: low_health_aggro_dependency
      active_when: "Damian、Trunk、Rosa、Sandy、8-Bit、Ash、Mr. P、Draco 等能用身体、召唤、范围或控制压到 Meeple 本体"
      exposed_by: "[[sources/PLP-Meeple|PLP-Meeple]] counteredBy list and 3300 HP Fandom stat"
      mitigation: "保留 Ragequit、配 peel，或后手确认敌方无法从草/墙/多角度进入"
      bp_use: must_answer_aggro_or_resource_before_meeple
    - id: slow_reload_without_rule_value
      active_when: "Meeple 没有 Super 区域、Rule Bending、或 Do Not Pass Go 的穿墙伤害窗口"
      exposed_by: "[[sources/Fandom-Meeple|Fandom-Meeple]] reload and Super mechanics"
      mitigation: "不要把 Meeple 当无条件长手；需要先验证 Super 获取与区域落点"
      bp_use: resource_tracking.super_area_available

  conditional_matchup_seeds:
    - target: Gale_or_Ollie_or_Meg_or_Clancy_or_Chuck_or_Griff_or_Lou_or_Shelly
      direction: subject_favored
      source: "[[sources/PLP-Meeple|PLP-Meeple]]"
      mechanism: "Meeple 用穿墙规则区、Mansions 陷阱、Ragequit 眩晕和 7.67 格略追踪普攻惩罚固定控制/身体/目标路线"
      active_when: "这些目标必须守矿区、热区、球门或回合墙边，且 Meeple 的 Super 或 Gadget 能改写其站位"
      fails_when: "目标不需要进入规则区，或用远程/队友先清掉 Meeple 本体"
      bp_use: rule_area_response_to_static_or_objective_targets
    - target: Damian_or_Trunk_or_Rosa_or_Sandy_or_8_Bit_or_Ash_or_Mr_P_or_Draco
      direction: target_favored
      source: "[[sources/PLP-Meeple|PLP-Meeple]]"
      mechanism: "高身体、持续压制、召唤物、隐蔽/控制或推进资源会迫使 3300 HP Meeple 在 Super 转化前先处理生存问题"
      active_when: "地图给草/墙/身体推进路线，或目标能用召唤/炮台/增益压缩 Meeple 站位"
      fails_when: "Meeple 有 Ragequit 和队友 peel，且目标必须进入被 Super/Mansions 控制的单一路线"
      bp_use: must_answer_body_spawnable_or_aggro_before_meeple
    - target: Open_map_snipers
      direction: target_favored
      source: "[[sources/Fandom-Meeple|Fandom-Meeple]]"
      mechanism: "Piper、Brock、Nani、Colt、Rico、Amber、Lou、R-T、Mandy 等在完全开阔图可用更稳定长线压制 Meeple"
      active_when: "地图缺可被 Critical Success 利用的墙体，且胜负主要是远距离对枪"
      fails_when: "地图有短线/墙体让 Meeple 的 Super 把掩体变成己方输出通道"
      bp_use: open_map_false_positive_filter
    - target: Thrower_or_Rico_teammate_combo
      direction: ally_synergy
      source: "[[sources/Fandom-Meeple|Fandom-Meeple]]"
      mechanism: "Mansions 困住目标后，Dynamike、Barley、Tick、Larry & Lawrie 等投掷手或 Rico 弹射能在 dice wall 内放大伤害"
      active_when: "敌方多人靠近，队友能从安全角度输出被困目标"
      fails_when: "敌方破墙、无敌盾清墙，或 Mansions 同时困住己方关键英雄"
      bp_use: combo_requirement_for_mansions_pick

  slot_notes:
    slot_1: "不适合无脑早手；只有地图明确是短线+长线混合、Super 能改写关键墙体，且敌方开放长手/突进答案有限时才考虑。"
    slot_2_3: "可作为规则区计划手，但队伍要补稳定目标身体、peel，或能利用 Rule Bending / Critical Success 的投射物队友。"
    slot_4_5: "适合看到敌方固定身体、支援或控制路线后，用 Mansions/Ragequit/穿墙区作为回答，同时防敌方 slot_6 拿纯开阔长手或强突进。"
    slot_6: "最适合惩罚敌方三人缺破墙、缺多角度突进、且必须站在墙边目标路线的局面；可以选择 Mansions 上限或 Ragequit 反 aggro/进球。"
```

## 关联页面

- [[sources/Fandom-Meeple|Fandom 来源摘要: Meeple]]
- [[sources/PLP-Meeple|PLP 来源摘要: Meeple]]
- [[sources/BSC-2026-July-Observed-Map-Fit-Review|BSC 2026 July 地图适配复核]]
