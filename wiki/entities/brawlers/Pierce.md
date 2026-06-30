# Pierce

## 基本信息

- 稀有度：Legendary
- 定位：Marksman
- 类型：弹壳资源型长手 / 中距离节奏压制

## 来源摘要

- Fandom：[[sources/Fandom-Pierce|Fandom 来源摘要: Pierce]]
- PLP：[[sources/PLP-Pierce|PLP 来源摘要: Pierce]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Heist, Hot Zone, Bounty, Knockout

## 角色定位总结

Pierce 不是普通长手射手。他的输出和装填依赖弹壳循环：命中后掉壳、捡壳补弹并触发自动射击，最后一发有额外伤害/减速价值。BP 里要把“射程很长”和“资源循环脆弱”同时写进判断；在纯开放狙击镜像里他可能被更稳定的狙击手压制，在中距离目标图里则可以用弹壳、减速和 Super 反复制造节奏。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Pierce|Fandom-Pierce]]"
    plp: "[[sources/PLP-Pierce|PLP-Pierce]]"
    user_notes: none

  capability_vector:
    effective_range: very_long_but_best_on_medium_long_objective_lanes
    projectile_reliability: medium; 直线长手命中稳定性受弹壳位置和敌方机动影响
    burst: high_if_last_ammo_bonus_or_super_homing_hits
    sustained_dps: conditional_on_shell_pickups; empty_ammo_reload_is_slow
    objective_damage: conditional_heist_lane_pressure_after_shell_cycle
    mobility: low_base; short_speed_burst_with_Slip_n_Snipe_if_selected
    survivability: low_base_health; shield_and_shell_cache_reduce_one_entry_window
    engage: low
    disengage: medium_with_shell_knockback_or_slow_resource
    anti_aggro: conditional_with_shell_cache_You_Only_Brawl_Twice_or_last_ammo_slow
    anti_tank: medium_if_spacing_and_shell_cycle_are_kept
    wall_break: none
    throw_or_wall_bypass: low; Super homing shots pass obstacles after lock but setup is delayed
    area_control: medium; shell positions and Super target circle tax objective routes
    scouting_or_vision: low
    team_support: slow_knockback_and_resource_pressure
    spawnable_or_pet: none; spawnables_are_a_liability_because_they_waste_ammo
    crowd_control: conditional_slow_or_knockback
    terrain_creation: temporary_shell_resource_nodes

  build_switches:
    - build: Bottomless Mags / Mission Swimpossible / Shield, Damage
      source: "[[sources/PLP-Pierce|PLP-Pierce]]"
      changes_capabilities:
        - Bottomless Mags 补一发弹药并创造弹壳，降低空弹期
        - Mission Swimpossible 让最后一发附带减速，提升中距离对线和防突进能力
        - Shield/Damage 让低血长手更能撑过第一波接近
      enables:
        - medium_lane_shell_cycle
        - last_ammo_slow_pick
        - super_shell_swing
      mitigates_failure_modes:
        - empty_ammo_lockout
        - low_health_first_contact
      poor_when:
        - 敌方用召唤物、宠物或区域伤害干扰弹壳路线，或用刺客逼 Pierce 离开弹壳
      bp_use: default_resource_cycle_build
    - build: You Only Brawl Twice anti-aggro variant
      source: "[[sources/Fandom-Pierce|Fandom-Pierce]]"
      changes_capabilities:
        - 吸收弹壳转护盾并击退附近敌人，适合防一波强突进
      enables:
        - close_entry_peel
        - shell_cache_defensive_conversion
      mitigates_failure_modes:
        - dive_after_shell_drop
      poor_when:
        - 弹壳太分散或 Pierce 需要持续弹药循环而不是一次性护盾
      bp_use: defensive_variant_into_known_aggro

  map_feature_hooks:
    - map_feature_type: medium_lane_shell_resource_control
      uses_feature_by: 长手射击和弹壳回收在中距离矿区/热区边缘形成资源循环
      objective_conversion: 稳定压线、保护矿区/热区入口、用最后一发减速创造击杀或逼退
      active_when: Pierce 能安全捡壳且目标必须进入中距离 objective lane
      fails_if: 弹壳落在危险区，或敌方召唤物/范围技能让 Pierce 空弹
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Open Business
      bp_use: map_bp_factors.shell_cycle_mid_control
    - map_feature_type: bounty_knockout_super_shell_swing
      uses_feature_by: 长线基础射程配合 Super 锁定范围，可在对方 peek 或缩圈时制造高伤害追踪波
      objective_conversion: 争取第一杀、保护回合血量领先或逼出敌方关键位
      active_when: Pierce 有壳/弹药资源，敌方不能轻易用墙体或召唤物吃掉节奏
      fails_if: 纯开放长线镜像被更稳定狙击手压制，或 Super 1 秒延迟被轻松离开
      example_maps:
        - Shooting Star
        - Dry Season
        - Belle's Rock
        - New Horizons
      bp_use: candidate_eval.long_lane_resource_marksman
    - map_feature_type: brawl_ball_last_ammo_slow_or_shell_knockback
      uses_feature_by: 最后一发减速、弹壳护盾/击退和 Super 追踪可处理持球者或门前防守者
      objective_conversion: 减速持球推进、打断门前身体、或为队友创造射门窗口
      active_when: Pierce 有弹壳缓存或最后一发资源，且队友能接住控制窗口
      fails_if: Pierce 被迫自己带球推进，或对方用多身体/召唤物吃掉弹药
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_control_marksman_with_resource_gate
    - map_feature_type: heist_shell_cycle_after_lane_win
      uses_feature_by: 长线赢边后可以用弹壳循环维持金库压力，但不是无条件 race 核心
      objective_conversion: 边路压制、补 safe damage、迫使敌方回防
      active_when: Pierce 已赢线或有队友控住入口，弹壳能安全回收
      fails_if: 需要他裸冲金库、弹壳在敌方基地危险区，或敌方 race 速度更快
      example_maps:
        - Bridge Too Far
        - Kaboom Canyon
        - Hot Potato
        - Pit Stop
      bp_use: candidate_eval.heist_lane_pressure_after_shell_setup

  objective_contracts:
    - mode: Gem Grab
      can_fulfill:
        - lane_pressure
        - last_ammo_slow_on_carrier_route
        - shell_cycle_mid_control
      cannot_fulfill:
        - primary_gem_carrier_under_dive_pressure
      needs_teammate_support:
        - bush_check_or_anti_aggro
        - body_or_support_to_hold_mid_when_Pierce_recovers_shells
      false_positive: 长射程不能替代矿区身体和探草
    - mode: Brawl Ball
      can_fulfill:
        - slow_or_knockback_ball_route
        - door_front_damage_pressure
      cannot_fulfill:
        - primary_scorer
        - goal_wallbreak
      needs_teammate_support:
        - scorer
        - wallbreak_or_hard_cc
      false_positive: 控制持球者不等于能进球，必须有射门/破门跟进
    - mode: Heist
      can_fulfill:
        - lane_win_to_safe_pressure
        - defensive_marksman_against_entry
      cannot_fulfill:
        - solo_safe_race_if_shells_are_unsafe
      needs_teammate_support:
        - primary_safe_DPS_or_wallbreak
        - anti_dive_on_safe_lane
      false_positive: PLP Heist 信号要落到具体打库角度和弹壳回收路径
    - mode: Hot Zone
      can_fulfill:
        - zone_edge_pressure
        - last_ammo_slow_on_entry
      cannot_fulfill:
        - durable_zone_body
      needs_teammate_support:
        - zone_holder
        - area_clear_or_sustain
      false_positive: Pierce 在圈外打准不代表能持续计分
    - mode: Bounty_or_Knockout
      can_fulfill:
        - long_range_pick_pressure
        - Super_finish_window
        - defensive_shell_cache
      cannot_fulfill:
        - safe_close_duel_when_shells_are_gone
      needs_teammate_support:
        - peel
        - wallbreak_or_control_against_thrower_pockets
      false_positive: 纯开放狙击镜像里要检查对面是否有更稳定弹道和更低资源成本

  failure_modes:
    - id: shell_resource_tax
      active_when: Pierce 为了捡壳必须走进危险区或离开关键角度
      exposed_by: Fandom 弹壳回收和空弹慢装填机制
      mitigation: 只在弹壳落点可控、中距离目标路线明确时选
      bp_use: resource_tracking.shell_position
    - id: low_health_aggro_window
      active_when: 敌方刺客、速度或草路能在 Pierce 空弹/捡壳时贴脸
      exposed_by: Fandom 低血量与 PLP counteredBy
      mitigation: 保留壳护盾/击退，搭配视野和队友 peel
      bp_use: must_have_peel_or_shell_cache
    - id: pure_long_sniper_mirror
      active_when: 地图完全开放且对手是更稳定长手，Pierce 难以安全滚动壳资源
      exposed_by: Fandom tips 对长射手镜像的风险说明
      mitigation: 选择中距离目标图，或确保 Super/队友控制能迫使对方进圈/进路
      bp_use: false_positive_filter.not_every_long_map
    - id: spawnable_or_pet_ammo_waste
      active_when: 敌方用 Nita、Mr. P、Jessie、Penny、Larry & Lawrie 等身体/资源吃掉 Pierce 弹药
      exposed_by: Fandom tips 对 pets/spawnables 干扰装填的说明
      mitigation: 先清资源或避免把 Pierce 当唯一输出
      bp_use: enemy_resource_filter

  conditional_matchup_seeds:
    - target: Gale_or_Jacky_or_Meg_or_El_Primo_or_R-T_or_Dynamike_or_Sam_or_Jae-Yong
      direction: subject_favored
      source: "[[sources/PLP-Pierce|PLP-Pierce]]"
      mechanism: Pierce 用中长线、最后一发减速和弹壳资源惩罚固定路线、短手身体或需要站位输出的目标
      active_when: 目标必须穿过可见 objective lane，Pierce 有弹药/弹壳缓存
      fails_when: 目标有队友遮挡、召唤物吃弹，或地图给其草/墙先手
      bp_use: resource_gated_lane_response
    - target: Chuck_or_Damian_or_Barley_or_Amber_or_Eve_or_Sprout_or_Lola_or_Nita
      direction: target_favored
      source: "[[sources/PLP-Pierce|PLP-Pierce]]"
      mechanism: 路线突进、墙控、区域燃烧、水/角度、替身或召唤物会干扰 Pierce 的壳循环和直线输出
      active_when: 地图给这些目标墙袋、侧角、水线或资源保护
      fails_when: 墙体被打开、资源被清，且 Pierce 能保持中长线弹壳循环
      bp_use: must_answer_resource_disruption_before_pierce
    - target: Mr_P_or_Jessie_or_Penny_or_spawnable_core
      direction: target_favored
      source: "[[sources/Fandom-Pierce|Fandom-Pierce]]"
      mechanism: 额外身体会浪费 Pierce 弹药、打乱掉壳节奏，并让他无法把最后一发资源打到真实目标
      active_when: 召唤物能安全过线或炮台/宠物站在 Pierce 必须射击的角度
      fails_when: 我方先清资源，或 Pierce 只负责补伤害不负责独自处理资源层
      bp_use: spawnable_liability_filter
    - target: Ball_carrier_or_goal_defender
      direction: subject_favored
      source: "[[sources/Fandom-Pierce|Fandom-Pierce]]"
      mechanism: 最后一发减速、Super 追踪和弹壳击退可以打断固定持球路线或门前防守站位
      active_when: 球路经过中距离直线，队友能接控制窗口完成射门
      fails_when: 目标有多身体挡弹或 Pierce 控住后无人转化进球
      bp_use: objective_specific_control_edge

  slot_notes:
    slot_1: 只有在地图目标路线适合中长线壳循环，且敌方召唤物/刺客反制面窄时可先手。
    slot_2_3: 可作为长手控制和资源压线手，但队伍必须补身体、探草或反突进。
    slot_4_5: 适合回答敌方短手/固定路线，同时防止敌方最后手拿召唤物、墙控或强突进。
    slot_6: 如果敌方三人缺资源干扰和近身开口，Pierce 可作为高收益壳循环惩罚 pick。
```

## 关联页面

- [[sources/Fandom-Pierce|Fandom 来源摘要: Pierce]]
- [[sources/PLP-Pierce|PLP 来源摘要: Pierce]]
