# Grom

## 基本信息

- 稀有度：Epic
- 定位：Artillery
- 类型：固定十字投掷 / 长线墙后控制 / Radio Check 固定目标爆发

## 来源摘要

- Fandom：[[sources/Fandom-Grom|Fandom 来源摘要: Grom]]
- PLP：[[sources/PLP-Grom|PLP 来源摘要: Grom]]
- PLP 推荐模式候选：Heist, Bounty, Knockout

## 角色定位总结

Grom 的 BP 价值来自超远距离越墙十字线压力：普攻落点后按地图坐标固定分裂成十字，分裂方向不随朝向变化；Super 也是更长、更宽的十字爆炸，并能击退和破墙。这个机制对墙边、窄路、固定 safe 和回合制卡位很强，但 Fandom 也明确指出敌人可以通过斜向走位躲开十字，且一旦贴脸，Grom 会因为落地慢和低血变得很脆弱。`Radio Check` 更适合固定目标或被 Super 击退后的落点，而不是追高速目标。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Grom|Fandom-Grom]]"
    plp: "[[sources/PLP-Grom|PLP-Grom]]"
    user_notes: none

  capability_vector:
    effective_range: very_long_thrower; 普攻落点 7.67 格且十字分裂可达 11 格
    projectile_reliability: medium_high_on_wall_clusters_low_vs_diagonal_mobility
    burst: high_with_Radio_Check_or_Super_combo
    sustained_dps: low_medium; 2 秒 slow reload，依赖命中十字线
    objective_damage: high_on_fixed_safe_or_stationary_target_with_Radio_Check
    mobility: low_base; Foot_Patrol speed only while Super is charged
    survivability: low; 3000 HP，贴脸后因落地慢很难自保
    engage: low_medium_with_Super_knockback_combo
    disengage: low_medium; Super knockback or Foot Patrol spacing only after charge
    anti_aggro: low_without_distance; medium_if_Super_knockback_and_wall_cluster_limit_entry
    anti_tank: medium_if_tank_must_walk_choke; poor_if_tank_reaches_contact
    wall_break: high_with_Super
    throw_or_wall_bypass: very_high
    area_control: high_on_cross_lanes_and_wall_clusters
    scouting_or_vision: medium_with_Watchtower_bush_radius
    team_support: vision_with_Watchtower_and_knockback_space
    spawnable_or_pet: Watchtower_vision_turret
    crowd_control: Super_knockback
    terrain_destruction: Super_wall_break

  build_switches:
    - build: "Radio Check / X-Factor / Shield, Damage"
      source: "[[sources/PLP-Grom|PLP-Grom]]"
      changes_capabilities:
        - "Radio Check 让下一次普攻连续发三发，对 safe、被击退目标或固定墙边站位收益很高"
        - "X-Factor 提升远端分裂伤害，鼓励把目标压到十字线外段"
        - "Shield/Damage 缓解低血和斩杀线问题，但不解决贴脸自保"
      enables:
        - "Heist fixed_safe_pressure"
        - "Bounty/Knockout wall_cluster_control"
        - "Super_knockback_into_Radio_Check_combo"
      mitigates_failure_modes:
        - "low_burst_without_resource"
        - "range_damage_threshold"
      best_when: "目标必须守墙边、长线或 fixed safe，且敌方不能低成本贴脸"
      poor_when: "地图给刺客/高速目标直接接近路线，或敌人能轻松斜走离开十字线"
      bp_use: default_long_thrower_burst_build
    - build: "Watchtower bush-scout variant"
      source: "[[sources/Fandom-Grom|Fandom-Grom]]"
      changes_capabilities:
        - "Watchtower 提供 10 格范围草丛视野，适合大草区或隐身/伏击信息压力"
      enables:
        - "bush_route_scouting"
        - "anti_ambush_setup"
      mitigates_failure_modes:
        - "side_grass_first_contact"
      best_when: "Ranked 图草路决定刺客或球路第一接触，且塔能放在不易被拆的位置"
      poor_when: "塔会被远程轻松清掉或地图主要问题不是草路信息"
      bp_use: information_variant_on_bush_route_maps

  map_feature_hooks:
    - map_feature_type: heist_radio_check_fixed_safe_pressure
      uses_feature_by: "safe 是固定目标，Radio Check 和 X-Factor 可把三发十字线转成高额金库压力"
      route_or_position: "safe 侧墙、远端投掷角、lane win 后安全 Radio Check 位置"
      objective_conversion: "补 safe damage、逼防守者回身、用 Super 破墙或击退守库身体"
      active_when: "Grom 能在墙后安全瞄 safe 或固定防守路线，队友有 lane pressure"
      fails_if: "Grom 被刺客/速度侧路先处理，或敌方 race 不需要经过他的十字区域"
      example_maps:
        - Bridge Too Far
        - Kaboom Canyon
        - Hot Potato
        - Safe Zone
      bp_use: candidate_eval.heist_fixed_target_thrower_pressure
    - map_feature_type: bounty_knockout_cross_lane_wall_cluster_control
      uses_feature_by: "十字线和 Super 击退惩罚墙边 peek、回合末 retreat 和有限通道"
      route_or_position: "wall edge、late-round choke、blue-star lane、low-health retreat path"
      objective_conversion: "拿第一杀、保护星数/回合血量领先、逼对方离开安全墙边"
      active_when: "地图有墙边/窄路让敌人难以纯斜走，且 Grom 不会被直接贴脸"
      fails_if: "纯开放长线让敌方稳定斜走躲十字，或刺客从侧路绕到 Grom 身边"
      example_maps:
        - Belle's Rock
        - Shooting Star
        - Dry Season
        - New Horizons
      bp_use: map_bp_factors.cross_pattern_round_control
    - map_feature_type: thrower_pocket_cross_choke_control
      uses_feature_by: "越墙普攻和固定十字分裂覆盖矿区/热区入口，迫使目标改变斜向移动"
      route_or_position: "mine entrance、center fort doorway、zone entry、wall-adjacent lane"
      objective_conversion: "阻止进矿/进区、清低血控制位，给队友安全站点或收宝"
      active_when: "入口被墙体或窄路限制，Grom 有 pocket 且敌方缺直接 dive"
      fails_if: "入口太宽使敌方斜走轻松离开十字，或 pocket 被破墙/传送/跳跃处理"
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Open Business
        - Dueling Beetles
      bp_use: map_bp_factors.wall_cluster_cross_choke_control
    - map_feature_type: bush_watchtower_or_crossline_scout
      uses_feature_by: "Watchtower 提供大半径草丛信息，十字线可预射草口和边路入口"
      route_or_position: "side bush、center grass、zone grass mouth、ball lane grass"
      objective_conversion: "降低刺客/草路第一接触收益，保护后排或 carrier"
      active_when: "塔能放到敌方不易清的位置，且草路决定目标路线"
      fails_if: "敌方远程秒拆 Watchtower，或隐身目标不被塔 reveal"
      example_maps:
        - Double Swoosh
        - Center Stage
        - Ring of Fire
        - Sneaky Fields
      bp_use: map_bp_factors.bush_information_support_not_primary_reveal

  objective_contracts:
    - mode: Heist
      can_fulfill:
        - "fixed_safe_Radio_Check_damage"
        - "long_thrower_lane_pressure"
        - "Super_wallbreak_or_defender_knockback"
      cannot_fulfill:
        - "frontline_safe_race"
        - "open_lane_self_defense_against_dive"
      needs_teammate_support:
        - "lane_body_or_anti_dive"
        - "primary_or_secondary_safe_DPS_to_convert_pressure"
      false_positive: "Heist 推荐依赖 safe 可被固定投掷角覆盖，不是所有三线竞速图都适合"
    - mode: Bounty
      can_fulfill:
        - "long_thrower_star_lane_pressure"
        - "wall_edge_pick"
        - "Watchtower_information_on_bush_routes"
      cannot_fulfill:
        - "close_range_star_carrier_under_dive"
      needs_teammate_support:
        - "peel_or_vision"
        - "long_range_partner_to_hold_open_lane"
      false_positive: "Grom 的长线来自投掷弧和十字线，不等于能赢所有纯开阔狙击线"
    - mode: Knockout
      can_fulfill:
        - "wall_cluster_area_control"
        - "late_round_choke_pressure"
        - "Super_knockback_finish"
      cannot_fulfill:
        - "survive_unprotected_assassin_entry"
      needs_teammate_support:
        - "anti_aggro_bodyguard"
        - "wallbreak_plan_if_enemy_pocket_is_safer"
      false_positive: "墙多有利，但深 pocket 被刺客或传送绕到身边时会反噬"

  failure_modes:
    - id: diagonal_dodge_cross_pattern
      active_when: "敌方有足够横向/斜向空间，能沿对角线离开固定十字分裂"
      exposed_by: "[[sources/Fandom-Grom|Fandom-Grom]] cross pattern and dodge tips"
      mitigation: "选择墙边、窄口、固定目标或用队友控制限制移动"
      bp_use: projectile_reliability_gate
    - id: helpless_if_close
      active_when: "Edgar、Mortis、Kaze、Sam 等贴到 Grom 身边，Grom 的落地慢无法阻止第一接触"
      exposed_by: "[[sources/Fandom-Grom|Fandom-Grom]] close-range weakness"
      mitigation: "保留 Super knockback、Watchtower/队友视野，或避免无保护早手"
      bp_use: draft_requires_peel
    - id: radio_check_on_moving_target
      active_when: "Radio Check 打高速移动目标而不是 safe、被击退点或固定墙边"
      exposed_by: "[[sources/Fandom-Grom|Fandom-Grom]] Radio Check best on stationary targets and combo advice"
      mitigation: "把 Radio Check 留给 safe、zone body、Super knockback 落点或已被限制路线目标"
      bp_use: resource_tracking.radio_check_target_quality
    - id: wallbreak_self_exposure
      active_when: "Super 破掉己方保护墙，让敌方长手或刺客更容易接近 Grom"
      exposed_by: "[[sources/Fandom-Grom|Fandom-Grom]] warning not to destroy walls near spawn"
      mitigation: "破墙前指定后续站位和受益方，只选择敌方 pocket 或目标墙"
      bp_use: terrain_state_plan_check

  conditional_matchup_seeds:
    - target: Bea_or_Poco_or_Meg_or_Pam_or_Lou_or_Surge_or_Emz_or_Shelly
      direction: subject_favored
      source: "[[sources/PLP-Grom|PLP-Grom]]"
      mechanism: "低机动或需要固定 objective 站位的目标容易被越墙十字线、Super knockback 和 Radio Check 逼离路线"
      active_when: "目标守墙边、矿区、热区、safe 防守线或回合 choke，且 Grom 不需要短距离对枪"
      fails_when: "目标从开阔空间斜走躲十字，或用队友/速度直接压到 Grom 身边"
      bp_use: wall_cluster_thrower_response
    - target: Bolt_or_Damian_or_Edgar_or_Mortis_or_Kaze_or_Sam
      direction: target_favored
      source: "[[sources/PLP-Grom|PLP-Grom]]"
      mechanism: "速度、突进、路线或近身爆发会跳过 Grom 的十字线等待时间，直接攻击低血投掷位"
      active_when: "地图给侧草、墙角或多路线接近，Grom 缺 Watchtower/peel/Super knockback"
      fails_when: "路线被队友视野和控制锁死，Grom 在远端只需输出固定目标"
      bp_use: must_answer_dive_before_grom
    - target: Mr_P_or_Najia
      direction: target_favored
      source: "[[sources/PLP-Grom|PLP-Grom]]"
      mechanism: "Porter ammo tax、毒区/弧线和墙控可让 Grom 难以把慢 reload 十字线打到真实目标"
      active_when: "资源层或 poison 路线能安全进入 Grom 的投掷 pocket 或迫使他换位"
      fails_when: "队友先清资源，或 Grom 在更远墙后只压固定 objective 路线"
      bp_use: must_answer_resource_or_wall_pressure
    - target: Heist_safe_or_wall_edge_retreat
      direction: subject_favored
      source: "[[sources/Fandom-Grom|Fandom-Grom]]"
      mechanism: "固定 safe 和墙边撤退路线无法像移动英雄一样斜走，Radio Check 和 Super 更容易转换伤害"
      active_when: "Grom 有安全投掷角，且队友保护他不被先切"
      fails_when: "safe race 来自其他 lane，或敌方 dive 迫使 Grom 无法站桩瞄准"
      bp_use: objective_specific_fixed_target_edge

  slot_notes:
    slot_1: "只在地图明确奖励墙后十字线与固定目标，且敌方低成本 dive 面较窄时早手；否则会被后手刺客/速度针对。"
    slot_2_3: "可作为长线投掷控制和 Heist/Bounty/Knockout 计划手，但队伍要补近身保护。"
    slot_4_5: "看到敌方固定站位、低机动或缺 dive 时可以补 Grom，同时避免敌方最后手拿 Mortis/Edgar/Kaze。"
    slot_6: "最适合惩罚已经没有突进资源的阵容，用 Radio Check/Super 处理 safe、墙边和回合 choke。"
```

## 关联页面

- [[sources/Fandom-Grom|Fandom 来源摘要: Grom]]
- [[sources/PLP-Grom|PLP 来源摘要: Grom]]
