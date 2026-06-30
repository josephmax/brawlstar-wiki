# Sirius

## 基本信息

- 稀有度：Ultra Legendary
- 定位：Controller
- 类型：影子经济控场 / 召唤体压迫与目标保护

## 来源摘要

- Fandom：[[sources/Fandom-Sirius|Fandom 来源摘要: Sirius]]
- PLP：[[sources/PLP-Sirius|PLP 来源摘要: Sirius]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Heist, Hot Zone, Bounty, Knockout

## 角色定位总结

Sirius 的强度来自影子数量、影子位置和 Super 调度，而不是单体对枪。她可以用影子逼走目标、守路、保护 carrier 或制造门前/热区资源税，但影子不能捡球、宝石、星星或能量块，且会被溅射、穿透和区域资源快速清掉。BP 中要明确她的任务是“影子创造空间”，不是替代真正的目标执行者。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Sirius|Fandom-Sirius]]"
    plp: "[[sources/PLP-Sirius|PLP-Sirius]]"
    user_notes: none

  capability_vector:
    effective_range: mid_long_dual_projectile_with_lob_component
    projectile_reliability: medium; 直线影击和抛物 Starr Bomb 需要节奏叠影
    burst: medium; rises_with_shadow_count_and_hypercharge
    sustained_dps: medium_if_shadows_survive
    objective_damage: conditional_heist_pressure_after_shadow_setup
    mobility: low_base
    survivability: low_medium; relies_on_shadow_bodies_and_positioning
    engage: medium_with_A_Starr_Is_Born_slow_or_shadow_relocation
    disengage: medium_with_Master_of_Shadows_recall_or_shadow_bodyguard
    anti_aggro: medium_high_if_shadows_body_block_and_slow_entry
    anti_tank: medium_if_shadow_stack_forces_body_to_spend_ammo
    wall_break: none
    throw_or_wall_bypass: medium_with_lobbed_Starr_Bomb
    area_control: high_when_shadow_stack_is_active
    scouting_or_vision: medium_with_shadow_patrol_and_bush_stack
    team_support: bodyguard_pressure_and_target_distraction
    spawnable_or_pet: high_shadow_economy
    crowd_control: slow_with_A_Starr_Is_Born
    terrain_creation: temporary_shadow_patrol_zones

  build_switches:
    - build: A Starr Is Born / The Darkest Starr / Shield, Damage
      source: "[[sources/PLP-Sirius|PLP-Sirius]]"
      changes_capabilities:
        - A Starr Is Born 直接生成目标影子并减速，提升第一波控场启动速度
        - The Darkest Starr 加快影子收集，让 Sirius 更快到达可调度资源量
        - Shield/Damage 缓解低血和单体输出不足
      enables:
        - shadow_stack_space_control
        - ball_or_gem_bodyguard
        - zone_patrol_tax
      mitigates_failure_modes:
        - slow_shadow_economy
        - low_self_duel_pressure
      poor_when:
        - 敌方有稳定溅射/穿透/投掷，能低成本清影子并打到 Sirius
      bp_use: default_shadow_economy_build
    - build: Master of Shadows recall variant
      source: "[[sources/Fandom-Sirius|Fandom-Sirius]]"
      changes_capabilities:
        - 召回并治疗影子，适合草图埋影子、保护自己或突然集结影子压目标
      enables:
        - bush_shadow_stack
        - emergency_bodyguard
        - surprise_relocation_pressure
      mitigates_failure_modes:
        - shadows_too_far_to_protect_core
      poor_when:
        - 影子被溅射持续清掉，或队伍需要更快影子收集而不是召回
      bp_use: map_specific_shadow_relocation_variant

  map_feature_hooks:
    - map_feature_type: gem_shadow_bodyguard_and_carrier_pressure
      uses_feature_by: 影子可站在矿区、侧草和 carrier 撤退路上，迫使敌方花弹药清资源
      objective_conversion: 保护宝石持有者、打断敌方倒计时追击、或用影子逼退矿区入口
      active_when: Sirius 已有影子资源，队友能收宝石，敌方缺低成本溅射清理
      fails_if: draft 期待影子捡宝石，或敌方用 Penny/Emz/投掷等资源一并清影子和本体
      example_maps:
        - Hard Rock Mine
        - Double Swoosh
        - Gem Fort
      bp_use: map_bp_factors.shadow_bodyguard_carrier_pressure
    - map_feature_type: brawl_ball_shadow_super_kick_or_bodyguard
      uses_feature_by: Super 可用来踢球/调度影子，影子本身可挡路线和吸弹
      objective_conversion: 保护持球推进、扰乱门前防守、制造一次突然射门或反推窗口
      active_when: Sirius 至少有影子资源，队友能接球/射门，影子只是开路而非持球者
      fails_if: 影子被误当成可持球单位，或敌方范围清掉影子后直接反打
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_shadow_bodyguard_not_carrier
    - map_feature_type: hot_zone_shadow_patrol_area_tax
      uses_feature_by: 影子可巡逻热区边缘、吃弹、逼迫进圈者绕路或先清资源
      objective_conversion: 给己方 zone body 买时间，并把敌方 re-entry 变成弹药税
      active_when: 队伍有实际站圈者，Sirius 的影子从墙边/草边保护入口
      fails_if: 影子被范围伤害瞬清，或 Sirius 被要求自己承担站圈主身体
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.shadow_zone_entry_tax
    - map_feature_type: bounty_knockout_shadow_stack_space
      uses_feature_by: 中长线双弹道和影子堆叠能在回合图里制造额外身体与追击压力
      objective_conversion: 保回合血量领先、挡关键子弹、逼出墙袋后排或缩圈时增加目标数量
      active_when: Sirius 能安全叠到 2-3 个影子，敌方缺即时 splash/pierce 清理
      fails_if: 低血本体被直接长线击杀，或影子变成敌方溅射收益
      example_maps:
        - Belle's Rock
        - New Horizons
        - Shooting Star
        - Dry Season
      bp_use: candidate_eval.round_shadow_space_control

  objective_contracts:
    - mode: Gem Grab
      can_fulfill:
        - carrier_bodyguard
        - mine_entry_shadow_tax
        - side_bush_shadow_pressure
      cannot_fulfill:
        - shadow_as_gem_carrier
        - stable_primary_carrier_if_body_is_exposed
      needs_teammate_support:
        - actual_gem_carrier
        - splash_resource_answer
      false_positive: 影子能保护路线，但不能捡宝石或替代 carrier
    - mode: Brawl Ball
      can_fulfill:
        - shadow_bodyguard
        - Super_kick_window
        - defender_ammo_tax
      cannot_fulfill:
        - shadow_ball_carry
        - goal_wallbreak
      needs_teammate_support:
        - scorer_or_pass_receiver
        - wallbreak_or_hard_control
      false_positive: 影子不能持球；Sirius 的球模式价值来自开路和 Super 时机
    - mode: Hot Zone
      can_fulfill:
        - entry_tax
        - shadow_patrol
        - bodyguard_for_zone_holder
      cannot_fulfill:
        - solo_zone_body
      needs_teammate_support:
        - zone_holder
        - area_or_sustain_followup
      false_positive: 影子拖时间不等于持续计分
    - mode: Bounty_or_Knockout
      can_fulfill:
        - shadow_body_block
        - low_commitment_space_control
        - slow_or_shadow_pick_setup
      cannot_fulfill:
        - pure_long_range_sniper_duel
      needs_teammate_support:
        - damage_to_convert_shadow_pressure
        - anti_thrower_or_anti_splash
      false_positive: 在纯开阔长线里，低血本体可能比影子更先被处理
    - mode: Heist
      can_fulfill:
        - defender_ammo_tax
        - auxiliary_safe_or_base_pressure_after_setup
      cannot_fulfill:
        - primary_safe_race
      needs_teammate_support:
        - main_safe_DPS
        - lane_control_to_keep_shadows_alive
      false_positive: 影子压基地如果不转化为打库或回防，只是拖时间

  failure_modes:
    - id: shadow_economy_not_ready
      active_when: Sirius 没有收集影子或只有一个影子，无法形成空间税
      exposed_by: Fandom 影子收集和 Super 召唤机制
      mitigation: 让 Sirius 在安全对线中积累资源，或用 A Starr Is Born 提前启动
      bp_use: resource_tracking.shadow_count
    - id: shadow_objective_limitation
      active_when: draft 把影子当成能拿球、宝石、星星或其他目标资源的单位
      exposed_by: Fandom 说明 shadows cannot pick up ball, power cubes, stars
      mitigation: 明确影子只负责 bodyguard、挡弹和空间压迫
      bp_use: hard_gate.objective_role_check
    - id: splash_or_pierce_shadow_clear
      active_when: 敌方 Penny、Emz、Nita、Tara、Carl、Barley、Larry & Lawrie 等能同时清影子和压本体
      exposed_by: Fandom tips 对 splash/pierce 清影子的说明
      mitigation: 只在敌方清资源成本高时堆影子，或让队友先处理清场者
      bp_use: enemy_resource_filter
    - id: low_hp_low_duel_damage
      active_when: Sirius 被迫单挑或没有影子保护的中距离对枪
      exposed_by: Fandom tips 对低 HP/低伤害 1v1 的说明
      mitigation: 跟随队友、用影子打空间，不独立守高风险边线
      bp_use: avoid_isolated_duel

  conditional_matchup_seeds:
    - target: Gale_or_Meg_or_Nani_or_Glowy_or_Pam_or_Shelly_or_Maisie_or_Fang
      direction: subject_favored
      source: "[[sources/PLP-Sirius|PLP-Sirius]]"
      mechanism: 影子身体、减速和调度能让中短距离控制/支援/单体输出目标花弹药处理额外单位，从而失去目标节奏
      active_when: Sirius 已有影子，目标必须守矿、球门、热区或回合路线
      fails_when: 目标队伍有溅射清场，或 Sirius 还没启动影子经济
      bp_use: shadow_resource_response_pick
    - target: Penny_or_Edgar_or_Damian_or_Brock_or_Mortis_or_Alli_or_Larry_and_Lawrie_or_Barley
      direction: target_favored
      source: "[[sources/PLP-Sirius|PLP-Sirius]]"
      mechanism: 炮台/溅射/投掷、刺客或墙控能绕过影子税，直接清资源或击杀低血本体
      active_when: 地图有墙袋、草路、长线开墙或投掷安全角度
      fails_when: 资源被先清，Sirius 站在队友保护后面且影子只做 bodyguard
      bp_use: must_answer_shadow_clear_or_dive
    - target: Nita_or_Tara_or_Carl_or_Emz_or_Penny
      direction: target_favored
      source: "[[sources/Fandom-Sirius|Fandom-Sirius]]"
      mechanism: 这些 splash/pierce/body 资源能清影子并同时威胁 Sirius，影子越多越可能变成范围收益
      active_when: 影子与本体站位靠近，或目标可以从墙后/中距离覆盖影子群
      fails_when: 影子分散巡逻且队友先压掉清场资源
      bp_use: spawnable_liability_filter
    - target: Ball_carrier_or_goal_defender_or_gem_carrier
      direction: subject_favored
      source: "[[sources/Fandom-Sirius|Fandom-Sirius]]"
      mechanism: 影子不能拿目标，但能挡路、吸弹、逼持有者改变路线，Super 调度可制造突然踢球或护送窗口
      active_when: 目标正在经过窄口、门前或 carrier 撤退线，Sirius 有影子资源
      fails_when: 队友无法接控制窗口，或敌方清影子后直接反打
      bp_use: objective_specific_shadow_bodyguard

  slot_notes:
    slot_1: 不宜无条件先手；影子经济怕清场资源，早手会给敌方明确拿 splash/pierce 的机会。
    slot_2_3: 可作为目标保护和资源税计划，但队伍必须已有真实 carrier/scorer/zone body。
    slot_4_5: 适合在敌方缺清影子资源时补空间控制，同时检查最后手刺客或投掷是否能直接处理本体。
    slot_6: 如果敌方三人低清场、低突进且目标路线固定，Sirius last pick 的影子税和护送上限很高。
```

## 关联页面

- [[sources/Fandom-Sirius|Fandom 来源摘要: Sirius]]
- [[sources/PLP-Sirius|PLP 来源摘要: Sirius]]
