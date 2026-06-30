# Trunk

## 基本信息

- 稀有度：Epic
- 定位：Tank
- 类型：蚂蚁区域型短手坦克 / 墙边压迫与站点身体

## 来源摘要

- Fandom：[[sources/Fandom-Trunk|Fandom 来源摘要: Trunk]]
- PLP：[[sources/PLP-Trunk|PLP 来源摘要: Trunk]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Hot Zone

## 角色定位总结

Trunk 的核心不是“短手坦克”四个字，而是用蚂蚁区域给自己加速/增伤，并通过短范围圆形攻击、墙后命中、Super dash 和区域减伤来占住目标附近的狭窄空间。BP 里必须确认他是否能站在蚂蚁区域内完成任务；如果地图太开、入口太长、或敌方能用控制打断攻击延迟，Trunk 会变成被风筝的近战身体。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Trunk|Fandom-Trunk]]"
    plp: "[[sources/PLP-Trunk|PLP-Trunk]]"
    user_notes: none

  capability_vector:
    effective_range: short_with_small_through_wall_edge
    projectile_reliability: medium; 主攻击有0.35秒延迟但圆形范围覆盖墙边
    burst: medium_high_if_edge_damage_or_full_combo_lands
    sustained_dps: high_while_standing_on_ant_area
    objective_damage: low_direct_heist_value
    mobility: medium_high_with_ant_speed_and_super_dash; Super 可越水并弹墙
    survivability: high_body_with_super_damage_reduction_and_Worker_Ants_heal_window
    engage: medium_high_on_grass_wall_or_zone_routes
    disengage: medium_with_super_dash_or_speed_area
    anti_aggro: medium; 短手身体、区域增益和墙边圆形伤害可反打贴脸
    anti_tank: medium_if_damage_buff_active; poor_into_dedicated_anti_tank_or_silence
    wall_break: none
    throw_or_wall_bypass: low_medium; 圆形攻击可打一格墙后但不是远程投掷
    area_control: medium_high_with_ants_area_and_enemy_damage_debuff
    scouting_or_vision: conditional_with_Colony_Scouts
    team_support: area_debuff_and_bodyguard_pressure
    spawnable_or_pet: ant_area_not_targetable_pet
    crowd_control: low_direct; relies_on_body_pressure_not_hard_cc
    terrain_creation: ant_area_as_temporary_combat_terrain

  build_switches:
    - build: Worker Ants / New Insect Overlords / Shield, Damage
      source: "[[sources/PLP-Trunk|PLP-Trunk]]"
      changes_capabilities:
        - Worker Ants 把下一段伤害转成治疗，增强第一次接触和站点容错
        - New Insect Overlords 让敌人在蚂蚁区域内伤害降低，强化热区、球门和矿区身体价值
      enables:
        - zone_body_with_debuff
        - brawl_ball_body_push
        - grass_or_wall_route_pressure
      mitigates_failure_modes:
        - first_contact_burst
        - short_range_trade_without_sustain
      poor_when:
        - 敌方能从区域外持续消耗，或用沉默/控制阻止 Trunk 建立蚂蚁区域
      bp_use: default_body_and_zone_build
    - build: Colony Scouts map-vision variant
      source: "[[sources/Fandom-Trunk|Fandom-Trunk]]"
      changes_capabilities:
        - 蚂蚁区域可显形草丛和隐身目标，牺牲部分区域减伤换取信息价值
      enables:
        - bush_route_check
        - anti_stealth_or_ambush_filter
      mitigates_failure_modes:
        - blind_grass_entry
      poor_when:
        - 地图不围绕草丛或敌方没有隐身/伏击路线
      bp_use: map_specific_vision_variant

  map_feature_hooks:
    - map_feature_type: grass_ant_reveal_and_side_pressure
      uses_feature_by: 蚂蚁区域、速度加成和 Colony Scouts 变体可把草丛入口变成 Trunk 的接触范围
      objective_conversion: 保护 gem carrier、切侧草、扫掉球路或热区入口的伏击威胁
      active_when: 草丛连接目标路线，Trunk 能在队友火力覆盖下进入并维持蚂蚁区域
      fails_if: 草被清掉后路线变开，或敌方在区域外用长射程/投掷白嫖 Trunk
      example_maps:
        - Double Swoosh
        - Hard Rock Mine
        - Sneaky Fields
        - Ring of Fire
      bp_use: map_bp_factors.grass_body_entry_with_vision_option
    - map_feature_type: brawl_ball_ant_speed_score_or_body
      uses_feature_by: 蚂蚁区域加速、短手身体和 Super dash 让 Trunk 能压球门或护送持球路线
      objective_conversion: 把中场赢线转成持球推进、挡人、吃伤害或门前身体压迫
      active_when: 队伍已有破门/射门手段，Trunk 负责把防守者挤出路线
      fails_if: 球门未打开且没有强控得分，或敌方留有沉默、击退、百分比伤害
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_body_pressure_not_primary_scorer
    - map_feature_type: hot_zone_ant_debuff_body
      uses_feature_by: 蚂蚁区域内移速/伤害增益和 New Insect Overlords 减伤，把热区入口变成 Trunk 的优势接触点
      objective_conversion: 站圈、赶人、吃第一波技能并让队友接管区域
      active_when: 热区入口短、墙体或草丛让 Trunk 能到达站点
      fails_if: 远程/投掷从区域外清点，或敌方控制让 Trunk 无法持续站在蚂蚁区域内
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.zone_body_with_area_debuff
    - map_feature_type: wall_edge_thrower_pressure
      uses_feature_by: 主攻击圆形范围可以打一格墙后，迫使浅墙后的投掷或控制位后撤
      objective_conversion: 清掉墙边控制点，打开矿区/热区/淘汰图的入口
      active_when: 敌方依赖浅墙或 L 墙边缘，而 Trunk 不需要穿越长开放地带
      fails_if: 墙袋太深、敌方有开阔长线，或控制在 Trunk 攻击延迟期间打断
      example_maps:
        - Belle's Rock
        - Open Business
        - Hard Rock Mine
      bp_use: candidate_eval.shallow_wall_body_pressure

  objective_contracts:
    - mode: Gem Grab
      can_fulfill:
        - side_grass_pressure
        - carrier_bodyguard
        - mine_entry_body_block
      cannot_fulfill:
        - stable_long_range_mid_carrier
      needs_teammate_support:
        - long_or_mid_range_to_collect_and_hold_gems
        - wallbreak_or_thrower_answer_when_pocket_is_deep
      false_positive: 草图短手价值必须建立在可到达矿区和可保护撤退上
    - mode: Brawl Ball
      can_fulfill:
        - body_push
        - ball_route_block
        - anti_scorer_short_contact
      cannot_fulfill:
        - reliable_goal_wallbreak
        - pure_scorer_without_team_window
      needs_teammate_support:
        - scorer_or_wallbreak
        - ranged_cover_after_Trunk_enters
      false_positive: Trunk 能走到门前不等于队伍有进球路径
    - mode: Hot Zone
      can_fulfill:
        - zone_body
        - entry_debuff
        - grass_or_wall_entry_guard
      cannot_fulfill:
        - circle_outside_long_range_clear
      needs_teammate_support:
        - thrower_or_range_to_clear_enemies_outside_ant_area
        - anti_control_against_silence_or_knockback
      false_positive: 如果敌方能一直从区域外清 Trunk，坦度不会转化成计分

  failure_modes:
    - id: short_range_open_lane
      active_when: 地图或破墙后变成长线，Trunk 必须正面横穿开放地
      exposed_by: Fandom 短射程与地图 profile 的长线规则
      mitigation: 只在草、墙、热区入口或球门路径能缩短接触距离时选
      bp_use: false_positive_filter.open_map_short_range
    - id: windup_cancel_by_cc
      active_when: 敌方有沉默、击退、眩晕、拉扯或强控制覆盖 Trunk 攻击延迟/Super
      exposed_by: Fandom 说明主攻击和 Super 可被控制打断
      mitigation: 逼出控制、搭配 anti-control 或把 Trunk 留作后手
      bp_use: resource_tracking.enemy_interrupt_check
    - id: ant_area_dependency
      active_when: Trunk 离开蚂蚁区域或区域被迫铺在无目标位置
      exposed_by: Fandom 蚂蚁区域提供自身速度/伤害和敌方减伤的机制
      mitigation: 围绕目标入口铺区域，不在无目标边线交换资源
      bp_use: map_factor_requires_stationary_contact_zone
    - id: super_endpoint_camped
      active_when: Super dash 终点被反坦、召唤物、减速或高 DPS 预瞄
      exposed_by: Fandom Super dash 和伤害减免时间很短
      mitigation: 让队友先压低终点或把 Super 作为二段调整而非裸开
      bp_use: avoid_raw_dash_entry

  conditional_matchup_seeds:
    - target: Sprout_or_Squeak_or_Nani_or_Piper_or_Mandy_or_Jae-Yong
      direction: subject_favored
      source: "[[sources/PLP-Trunk|PLP-Trunk]]"
      mechanism: Trunk 可用墙边圆形伤害、草/墙路线和高身体压缩低血量控制或长线目标的安全空间
      active_when: 地图有浅墙、草路或目标必须守矿/球门/热区入口
      fails_when: 目标在全开放长线输出，或有反坦队友保护入口
      bp_use: route_based_response_into_fragile_control
    - target: Shade_or_Mico
      direction: volatile
      source: "[[sources/PLP-Trunk|PLP-Trunk]]"
      mechanism: Trunk 的短手身体和墙边伤害能惩罚落点/接触点，但这些目标也可能绕过 Trunk 打后排
      active_when: 目标必须进入 Trunk 守住的 objective endpoint
      fails_when: 它们选择另一条路线打脆皮，或 Trunk 没有队友补伤害
      bp_use: endpoint_guard_not_universal_counter
    - target: Otis_or_Clancy_or_Crow_or_Damian_or_Colette_or_Nita_or_Doug_or_Juju
      direction: target_favored
      source: "[[sources/PLP-Trunk|PLP-Trunk]]"
      mechanism: 沉默、反坦 DPS、毒伤、百分比伤害、召唤物或墙控会让 Trunk 无法稳定站在蚂蚁区域中
      active_when: 这些目标守住热区、球门或矿区入口，Trunk 必须正面进入
      fails_when: Trunk 只承担短时间 bodyguard，且队友先清掉控制/召唤物
      bp_use: must_answer_before_committing_trunk_body
    - target: Zone_holder_or_ball_carrier_or_thrower_pocket
      direction: subject_favored
      source: "[[sources/Fandom-Trunk|Fandom-Trunk]]"
      mechanism: 蚂蚁区域、Super dash 和一格墙后攻击能把固定目标从入口、球路或浅墙口袋挤走
      active_when: 目标位置固定且离 Trunk 接触路线很近
      fails_when: 目标位于深墙袋或有控制链保护
      bp_use: objective_specific_body_pressure

  slot_notes:
    slot_1: 只在地图天然短接触、草/墙/热区入口收益极高且敌方反坦池被 ban 掉时先手。
    slot_2_3: 可作为 Hot Zone 或 Brawl Ball 的身体计划，但需要同时补远程/投掷清外圈。
    slot_4_5: 适合回答缺反坦的脆皮控制阵容，尤其敌方 2-3 位已暴露低机动后排。
    slot_6: 若敌方三人缺沉默、百分比伤害和召唤物身体，可作为高压短路口 last pick。
```

## 关联页面

- [[sources/Fandom-Trunk|Fandom 来源摘要: Trunk]]
- [[sources/PLP-Trunk|PLP 来源摘要: Trunk]]
