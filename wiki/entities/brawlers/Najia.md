# Najia

## 基本信息

- 稀有度：Mythic
- 定位：Damage Dealer
- 类型：毒蛇罐远程压制 / 分段瞄准控场

## 来源摘要

- Fandom：[[sources/Fandom-Najia|Fandom 来源摘要: Najia]]
- PLP：[[sources/PLP-Najia|PLP 来源摘要: Najia]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Heist, Hot Zone, Bounty, Knockout

## 角色定位总结

Najia 用罐子落点和蛇的二段释放打出绕墙、远距和毒伤压制。她适合惩罚固定站位、矿区拥挤、热区入口和墙后目标，但缺少爆发和自保；BP 不能只看 PLP 的全模式信号，必须确认她的慢弹道和毒伤能转化成目标压力，而不是被刺客/高速角色直接贴脸。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-17"
    plp: "[[sources/PLP-Najia|PLP-Najia]]"
    user_notes: none

  capability_vector:
    effective_range: medium_to_long_with_jar_extension_and_snake_release
    projectile_reliability: medium_low_into_fast_targets; improves_against_fixed_or_grouped_routes
    burst: low_medium; poison_stack_is_pressure_not_instant_kill
    sustained_dps: medium_with_poison_stacks_and_fast_reload
    objective_damage: conditional_heist_aux_pressure_not_primary_race
    mobility: low
    survivability: low_medium; Najia_Jar_can_stall_but_not_solve_focus_fire
    engage: low
    disengage: conditional_with_Najia_Jar_knockback_or_preplaced_poison
    anti_aggro: low_medium_if_puddles_cover_route; weak_without_team_peel
    anti_tank: medium_if_poison_stacks_and_team_damage_convert
    wall_break: none
    throw_or_wall_bypass: high_with_jar_arc_and_snake_release
    area_control: high_with_poison_puddles_and_super_snakes_but_super_self_charge_caps_at_50_percent
    scouting_or_vision: medium_indirect_with_poison_trails_and_snakes
    team_support: route_denial_and_poison_setup_for_team_damage
    spawnable_or_pet: snake_spawn_from_super_or_death_synergy; Super snakes lose 16% health per second and one Super's own hits cannot supply more than 50% of the next Super
    crowd_control: low_direct; poison_area_forces_movement
    terrain_creation: temporary_poison_puddles

  build_switches:
    - build: Poison Puddles / Poisonous Protector / Shield, Damage
      source: "[[sources/PLP-Najia|PLP-Najia]]"
      changes_capabilities:
        - Poison Puddles 把命中后的位置轨迹转成持续路线否定
        - Poisonous Protector 让被毒目标死亡后生成蛇，增强团战后续控制
        - Shield/Damage 缓解低血和低爆发问题
      enables:
        - grouped_route_poison
        - wall_angle_pressure
        - objective_entry_denial
      mitigates_failure_modes:
        - poison_without_space_control
        - low_health_chipdown
      poor_when:
        - 敌方高速分散、能直接跳脸，或队伍缺少即时伤害把毒伤转换成击杀
      bp_use: default_poison_control_build
    - build: Najia Jar stall variant
      source: "[[sources/Fandom-Najia|Fandom-Najia]]"
      changes_capabilities:
        - 进入罐子短时间免伤并在破裂时击退周围敌人，可拖一波刺客或保护目标时间
      enables:
        - emergency_stall
        - ball_or_zone_delay
      mitigates_failure_modes:
        - first_contact_assassin_burst
      poor_when:
        - 敌方有高伤 Super、持续区域或能在罐子结束后继续追击
      bp_use: defensive_stall_variant_not_full_peel

  map_feature_hooks:
    - map_feature_type: gem_mid_poison_carrier_pressure
      uses_feature_by: 罐子/蛇二段可从墙边压矿区和 carrier 撤退路，毒池持续暴露或限制走位
      objective_conversion: 逼退宝石矿、打断倒计时撤退、让队友追杀中毒 carrier
      active_when: 敌方必须穿过矿区入口或草边路线，Najia 有队友保护不被突进
      fails_if: 敌方分散三路且高速绕开毒池，或 Najia 被迫自己持宝石对线刺客
      example_maps:
        - Hard Rock Mine
        - Double Swoosh
        - Gem Fort
      bp_use: map_bp_factors.poison_carrier_route_pressure
    - map_feature_type: hot_zone_grouped_poison_puddles
      uses_feature_by: 热区入口和站圈位置会放大毒伤、蛇和毒池的路线惩罚
      objective_conversion: 让敌方进圈损血、离开 zone 或把队友的范围伤害变成击杀
      active_when: 敌方需要重复从固定入口进圈，且我方有身体站圈
      fails_if: Najia 被要求自己站圈，或敌方从区域外长线清点不进入毒池
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
      bp_use: map_bp_factors.zone_poison_entry_tax
    - map_feature_type: knockout_wall_arc_poison_control
      uses_feature_by: 罐子可越墙，蛇释放能从落点改变角度，适合压缩墙袋和回合退路
      objective_conversion: 逼出墙后控制、保护血量领先、在缩圈前锁定敌方可站空间
      active_when: 墙体仍然存在且敌方缺强突进，Najia 可从安全角度连续投毒
      fails_if: 敌方开墙转纯长线，或刺客有清晰路线直接到 Najia
      example_maps:
        - Belle's Rock
        - New Horizons
        - Shooting Star
      bp_use: candidate_eval.wall_arc_round_control
    - map_feature_type: heist_remote_poison_aux_pressure
      uses_feature_by: 罐子/蛇和毒池可在赢线后给金库或防守路线施加低承诺压力
      objective_conversion: 辅助 safe pressure、逼回防、限制敌方从基地入口清人
      active_when: 队伍已有主 safe DPS，Najia 负责远程牵制或防守入口
      fails_if: draft 把 Najia 当作主要 race，或敌方直接用高速路线绕过毒区打库
      example_maps:
        - Safe Zone
        - Hot Potato
        - Pit Stop
        - Bridge Too Far
      bp_use: candidate_eval.heist_aux_control_not_primary_dps

  objective_contracts:
    - mode: Gem Grab
      can_fulfill:
        - mine_entry_poison
        - carrier_route_pressure
        - wall_angle_control
      cannot_fulfill:
        - safe_primary_carrier_under_dive
      needs_teammate_support:
        - anti_aggro_or_bodyguard
        - burst_to_convert_poison
      false_positive: 毒伤压线不等于能自己拿宝石撤退
    - mode: Hot Zone
      can_fulfill:
        - entry_tax
        - grouped_enemy_poison
        - wall_angle_area_control
      cannot_fulfill:
        - primary_zone_body
      needs_teammate_support:
        - zone_holder
        - ranged_or_burst_followup
      false_positive: 毒区赶人后必须有人站圈
    - mode: Bounty_or_Knockout
      can_fulfill:
        - wall_arc_pressure
        - retreat_route_poison
        - grouped_target_control
      cannot_fulfill:
        - instant_pick_vs_high_mobility
      needs_teammate_support:
        - peel
        - finishing_damage
      false_positive: 慢弹道在纯开阔高速对局里容易被躲
    - mode: Heist
      can_fulfill:
        - auxiliary_safe_pressure
        - defender_route_denial
      cannot_fulfill:
        - primary_safe_race
      needs_teammate_support:
        - main_safe_DPS
        - lane_winner_or_wall_control
      false_positive: PLP Heist 信号不能覆盖她低爆发/低自保的限制
    - mode: Brawl Ball
      can_fulfill:
        - ball_route_poison
        - defender_displacement_by_area
      cannot_fulfill:
        - primary_scorer
        - goal_wallbreak
      needs_teammate_support:
        - scorer_or_cc
        - anti_assassin_peel
      false_positive: 毒区拖慢推进，但不等于能打开球门

  failure_modes:
    - id: super_snake_cycle_and_durability_overestimated
      active_when: "阵容假设 Danger Noodles 能靠自己的罐子/蛇接近自循环，或把蛇当作持续站场身体"
      exposed_by: "[[sources/Fandom-Najia|Fandom-Najia]] 当前 Super 自充上限 50%，蛇每秒损失 16% 生命；Hypercharge 只是把数量提高到 6 并强化蛇，不取消可清除与衰减"
      mitigation: "把一次 Super 当单波路线压力，预留主攻击继续充能，并让队友在蛇衰减前立即把逼位转成击杀/站点"
      bp_use: "resource_tracking.super_cycle_and_spawnable_lifetime"
    - id: slow_projectile_and_aim_tax
      active_when: 敌方高速、分散或多路线移动，Najia 难以用罐子落点和蛇命中关键目标
      exposed_by: Fandom tips 对慢投射物和高难瞄准的说明
      mitigation: 选固定入口、墙角、热区或矿区路线，而非纯开放追人图
      bp_use: map_geometry_filter
    - id: low_burst_self_defense
      active_when: Edgar、Sam、Melodie、Chuck 等能直接到脸并要求即时爆发
      exposed_by: Fandom tips 对低爆发/自保差的说明
      mitigation: 搭配硬控/身体保护，或后手只惩罚缺突进的阵容
      bp_use: must_have_peel_against_aggro
    - id: poison_without_team_damage
      active_when: Najia 打出毒伤但队友没有补伤害，敌方靠治疗/撤退重置
      exposed_by: 毒伤是持续压力而非立即击杀
      mitigation: 搭配 burst、拉人、减速或目标必须站点的模式
      bp_use: comp_synergy_check
    - id: najia_jar_stall_risk
      active_when: Najia Jar 只能拖时间，结束后仍被高伤或控制接上
      exposed_by: Fandom 对 gadget 免伤和结束风险的说明
      mitigation: 把罐子作为队友支援到位的时间桥，不当自保终点
      bp_use: defensive_resource_timing

  conditional_matchup_seeds:
    - target: Dynamike_or_Meg_or_Gale_or_Mandy_or_Lou_or_R-T_or_Piper_or_Jae-Yong
      direction: subject_favored
      source: "[[sources/PLP-Najia|PLP-Najia]]"
      mechanism: Najia 的越墙/远距毒伤能逼迫固定控制、长线或站点目标离开安全角度，并用毒池惩罚撤退路线
      active_when: 地图有墙角、矿区、热区入口或目标必须守固定线
      fails_when: 目标有高速队友开到 Najia，或地图完全开放让慢弹道难以命中
      bp_use: wall_or_objective_route_response
    - target: Poco_or_Eve_or_Edgar_or_Sam_or_Damian_or_Melodie_or_Chuck_or_Lola
      direction: target_favored
      source: "[[sources/PLP-Najia|PLP-Najia]]"
      mechanism: 治疗、离水角度、刺客、高速路线、墙控或替身能化解毒伤节奏并惩罚 Najia 的低爆发
      active_when: 这些目标能绕开固定入口，或有治疗/资源让毒伤无法转换
      fails_when: 队友先锁路线，Najia 只负责远程毒区而不独立接触
      bp_use: must_answer_sustain_or_aggro_before_najia
    - target: Grouped_zone_or_gem_route
      direction: subject_favored
      source: "[[sources/Fandom-Najia|Fandom-Najia]]"
      mechanism: 毒池、蛇和 Super 多罐会叠加区域压力，惩罚中路拥挤和反复进圈
      active_when: 敌方抱团守矿、站圈或走同一 choke
      fails_when: 敌方分路、远程清点或用高速绕开毒区
      bp_use: objective_specific_grouped_route_punish
    - target: High_mobility_dive
      direction: target_favored
      source: "[[sources/Fandom-Najia|Fandom-Najia]]"
      mechanism: 高机动可以跳过毒池等待时间，直接逼 Najia 交 Jar 或击杀她
      active_when: 地图有侧草、跳点、dash 路线或 Najia 无队友保护
      fails_when: 入口被队友控制，Najia 预铺毒池且只需要拖一波
      bp_use: anti_aggro_false_positive_filter

  slot_notes:
    slot_1: 不建议仅因 PLP 多模式信号先手；除非地图是固定入口/墙角毒区图且敌方突进池受限。
    slot_2_3: 可建立墙角控制或热区/矿区入口计划，但队伍必须同时补身体和即时伤害。
    slot_4_5: 适合回答已暴露的固定后排、热区身体或低机动长线，但要防敌方最后手刺客/高速路线。
    slot_6: 当敌方三人缺 sustain、突进和远程清区时，Najia last pick 能把地图 chokepoint 转成高压毒区。
```

## 关联页面

- [[sources/Fandom-Najia|Fandom 来源摘要: Najia]]
- [[sources/PLP-Najia|PLP 来源摘要: Najia]]
