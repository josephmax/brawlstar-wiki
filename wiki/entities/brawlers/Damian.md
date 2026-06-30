# Damian

## 基本信息

- 稀有度：Mythic
- 定位：Tank
- 类型：短手高血 / 受伤充能 / Mosh Pit 跳入控场

## 来源摘要

- Fandom：[[sources/Fandom-Damian|Fandom 来源摘要: Damian]]
- PLP：[[sources/PLP-Damian|PLP 来源摘要: Damian]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Hot Zone

## 角色定位总结

Damian 是高血、短手、靠受伤充能和进场资源打目标的坦克。他的普攻命中两次后获得强化攻击，强化攻击击退并标记目标，随后爆炸可连锁；Super 让他跳过障碍/水域落地生成 5 秒 `Mosh Pit`，用 speaker 边界把敌人向中心弹回。BP 里不能只看“Tank + 跳跃”就认为他能无脑进场：短射程会被开阔长手风筝，强化条会随时间衰减且空拳会清空，Mosh Pit 的边界可被打掉，敌人被弹起期间也会短暂无敌，需要队友和 Damian 的下一拳衔接。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Damian|Fandom-Damian]]"
    plp: "[[sources/PLP-Damian|PLP-Damian]]"
    user_notes: none

  capability_vector:
    effective_range: short; 2.67 格主攻击，Super 6 格跳入
    projectile_reliability: high_if_contact_reached; low_when_kited
    burst: medium_high_with_empowered_attack_chain_explosion
    sustained_dps: medium; 1.2 秒 fast reload 但需要持续贴身
    objective_damage: low_medium; 主要通过清人/站点转目标
    mobility: high_with_super_jump_over_obstacles_or_lakes
    survivability: high_health_and_tank_trait; depends_on_damage_taken_for_super
    engage: high_with_mosh_pit_or_empowered_speed
    disengage: medium_with_super_escape_or_spiritual_healing
    anti_aggro: medium_high_into_other_bodies_if_empowered_attack_ready
    anti_tank: medium; chain explosion and knockback matter more than raw DPS
    wall_break: none
    throw_or_wall_bypass: super_jump_bypasses_obstacles
    area_control: high_during_mosh_pit
    scouting_or_vision: low
    team_support: Spiritual_Healing_pickup_and_Wall_of_Sound_route_block
    spawnable_or_pet: temporary_speaker_boundary
    crowd_control: empowered_knockback_mosh_pit_launch_and_Crowdkill_wall_stun
    terrain_creation: Wall_of_Sound_and_mosh_pit_speaker_boundary
    terrain_destruction: none

  build_switches:
    - build: "Spiritual Healing / Vulgar Display Of Punch / Health, Damage"
      source: "[[sources/PLP-Damian|PLP-Damian]]"
      changes_capabilities:
        - "Spiritual Healing 提供可投掷麦克风治疗，支持 Damian 或队友在目标点延长一波站场"
        - "Vulgar Display Of Punch 让 Super 期间立即获得强化攻击，保证跳入后有 knockback/爆炸链资源"
        - "Health/Damage 与高血受伤充能、近身斩杀线相匹配"
      enables:
        - "Gem Grab carrier escape or dive"
        - "Brawl Ball goal route disruption"
        - "Hot Zone body control"
      mitigates_failure_modes:
        - "missing_empowered_attack_after_jump"
        - "sustain_after_first_entry"
      best_when: "地图目标迫使敌人进入短手/边界区域，队友能在 Damian 跳入后跟伤或站点"
      poor_when: "敌方长手/沉默/反坦能在 Damian 进入前持续消耗，或直接破坏 mosh pit 边界"
      bp_use: default_objective_body_build
    - build: "Wall of Sound / Crowdkill route-block variant"
      source: "[[sources/Fandom-Damian|Fandom-Damian]]"
      changes_capabilities:
        - "Wall of Sound 创造 3 个临时可破坏墙体，用于挡球路、封入口或制造强化攻击撞墙 stun"
        - "Crowdkill 只在强化攻击把目标击到普通墙体时触发，Super speaker 不计入"
      enables:
        - "temporary_route_block"
        - "empowered_attack_wall_stun"
      mitigates_failure_modes:
        - "open_route_kiting"
      best_when: "关键球路/热区入口/矿区退线可被 7 秒临时墙改变"
      poor_when: "敌方有廉价破墙或墙体方向无法对齐目标路线"
      bp_use: terrain_creation_variant

  map_feature_hooks:
    - map_feature_type: gem_super_escape_or_carrier_disruption
      uses_feature_by: "Super 跳跃可越障碍/水域逃生或切入敌方 carrier，Mosh Pit 边界限制追击路线"
      route_or_position: "gem mine、center fort doorway、carrier countdown retreat、side grass chase"
      objective_conversion: "保护己方 carrier、破坏敌方倒计时、或把追击者困在队友火力中"
      active_when: "Damian 有 Super 或能通过受伤快速充能，队友可跟进被困目标"
      fails_if: "他被当成稳定远程 carrier，或敌方沉默/反坦在进场点等他"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Double Swoosh
      bp_use: map_bp_factors.carrier_escape_or_disruption_body
    - map_feature_type: brawl_ball_mosh_pit_goal_or_disarm
      uses_feature_by: "跳入球路或门前生成 Mosh Pit，强化攻击击退持球者/防守者"
      route_or_position: "midfield ball、goal-front defender、side grass push、closed goal route"
      objective_conversion: "打断持球推进、困住门前防守、给队友射门或补伤害窗口"
      active_when: "球路固定且队友能接球或射门，Damian 有强化攻击或 Vulgar Display 可保证资源"
      fails_if: "敌方保存 Otis/Gale/Lou 类控制或远程先把 Damian 打残"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_body_disarm_and_goal_route_control
    - map_feature_type: hot_zone_mosh_pit_body_and_boundary
      uses_feature_by: "Mosh Pit 边界和强化攻击把敌方站区身体向中心拉回，Hypercharge 火区进一步惩罚聚集"
      route_or_position: "zone center、zone entrance、wall-adjacent body point、re-entry lane"
      objective_conversion: "清站区、强行买 zone time、让敌方重进区路径变窄"
      active_when: "队友能在 Damian 控住区域后站圈，敌方不能从圈外免费清他"
      fails_if: "speaker boundary 被快速打掉，或敌方用长手/投掷完全不进圈"
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.zone_body_boundary_control
    - map_feature_type: wall_of_sound_route_block_or_empowered_wall_stun
      uses_feature_by: "Wall of Sound 创建临时墙体改变路线；强化攻击可把目标撞向普通墙触发 Crowdkill stun"
      route_or_position: "goal mouth、zone entrance、fort doorway、retreat lane"
      objective_conversion: "临时封路、保护撤退、或用撞墙 stun 让队友击杀"
      active_when: "墙体方向能切断关键路线，且敌方破墙成本高"
      fails_if: "墙被立刻破坏、方向放错，或队友因墙体被反卡"
      example_maps:
        - Sneaky Fields
        - Pinball Dreams
        - Gem Fort
        - Belle's Rock
      bp_use: terrain_state_plan.temporary_wall_route_control

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier_escape_with_super"
        - "enemy_carrier_disruption"
        - "mine_body_pressure"
      cannot_fulfill:
        - "safe_long_range_carrier_without_support"
      needs_teammate_support:
        - "long_range_mid_or_healer"
        - "anti_control_after_jump"
      false_positive: "能用 Super 带宝石逃走，不等于能从开局当稳定 mid carrier"
    - mode: "Brawl Ball"
      can_fulfill:
        - "ball_carrier_knockback"
        - "goal_route_body_pressure"
        - "temporary_wall_or_mosh_pit_disruption"
      cannot_fulfill:
        - "reliable_goal_wallbreak"
      needs_teammate_support:
        - "scorer_or_wallbreak"
        - "followup_damage_after_knockback"
      false_positive: "跳进门前不等于进球；必须有球权转化和队友 follow-up"
    - mode: "Hot Zone"
      can_fulfill:
        - "zone_body"
        - "entry_displacement"
        - "temporary_boundary_control"
      cannot_fulfill:
        - "answer_throwers_from_outside_zone"
      needs_teammate_support:
        - "range_or_thrower_clear"
        - "sustain_or_followup"
      false_positive: "Damian 能站区和清区，但被远程不进圈消耗时会失去价值"

  failure_modes:
    - id: short_range_kited_before_super
      active_when: "Piper、Nani、Mr. P、Squeak 等在开阔线或墙外持续消耗 Damian"
      exposed_by: "[[sources/Fandom-Damian|Fandom-Damian]] short range and PLP matchup seeds"
      mitigation: "选有墙/草/目标接触点的地图，或保留 Super 作为 first contact"
      bp_use: false_positive_filter.not_open_lane_tank
    - id: empowered_bar_decay_or_miss
      active_when: "强化攻击 5 秒内没用到、空拳，或进场时没有 Vulgar Display 资源"
      exposed_by: "[[sources/Fandom-Damian|Fandom-Damian]] empowered attack bar mechanics"
      mitigation: "进关键目标前确认强化条或 Super+SP 可立即充能"
      bp_use: resource_tracking.empowered_attack_ready
    - id: mosh_pit_boundary_destroyed_or_misconverted
      active_when: "speaker 边界被打掉，敌人被弹起期间短暂无敌导致队友伤害空掉"
      exposed_by: "[[sources/Fandom-Damian|Fandom-Damian]] mosh pit speaker and airborne notes"
      mitigation: "把 Mosh Pit 当 route control，队友等落点补伤害"
      bp_use: objective_control_timing_gate
    - id: hard_control_and_anti_tank_waiting
      active_when: "Clancy、Otis、Chester、Bull、Doug、Jacky、Trunk 等保留控制/爆发/高身体反打 Damian"
      exposed_by: "[[sources/PLP-Damian|PLP-Damian]] counteredBy list"
      mitigation: "先骗资源或让队友从远端削弱，再跳入关键目标"
      bp_use: must_answer_anti_body_before_pick

  conditional_matchup_seeds:
    - target: Gale_or_Sprout_or_Squeak_or_Jae_Yong_or_Piper_or_Nani_or_Mr_P_or_Ziggy
      direction: subject_favored
      source: "[[sources/PLP-Damian|PLP-Damian]]"
      mechanism: "Damian 用跳跃和 Mosh Pit 跳过部分远程/墙控安全距离，把低身体或固定控制位拉入短手爆发与队友火力"
      active_when: "地图给 Damian Super 接近路线或目标必须守 objective，且反坦资源不足"
      fails_when: "目标在纯开阔长线持续风筝，或有队友控制等在落点"
      bp_use: route_based_tank_engage_response
    - target: Clancy_or_Otis_or_Chester_or_Bull_or_Juju_or_Doug_or_Jacky_or_Trunk
      direction: target_favored
      source: "[[sources/PLP-Damian|PLP-Damian]]"
      mechanism: "反坦 DPS、沉默、爆发、复活/高身体或墙控能吸收 Damian 跳入并惩罚短手停留"
      active_when: "他们守住球门、热区、矿区或 Damian 的落点"
      fails_when: "控制被提前骗掉，Damian 只跳后排或队友先拆掉身体层"
      bp_use: must_answer_anti_body_before_damian
    - target: Gem_carrier_or_ball_carrier_or_zone_holder
      direction: subject_favored
      source: "[[sources/Fandom-Damian|Fandom-Damian]]"
      mechanism: "Mosh Pit、强化击退和临时墙能直接改变 carrier/holder 的路线和目标动作"
      active_when: "目标必须留在固定路线，Damian 有 Super/empowered attack"
      fails_when: "目标有 dash、invulnerability、teammate peel or long-range cover"
      bp_use: objective_specific_displacement_edge
    - target: Wallbreak_or_thrower_clear
      direction: target_favored
      source: "[[sources/Fandom-Damian|Fandom-Damian]]"
      mechanism: "speaker 与 Wall of Sound 都是可被攻击/破坏的临时结构，投掷和破墙会降低边界价值"
      active_when: "Damian 的计划依赖临时墙/边界持续 5-7 秒"
      fails_when: "结构只需要争取一瞬间，或队友先控制清墙者"
      bp_use: terrain_creation_counterplay_filter

  slot_notes:
    slot_1: "只在地图目标强迫短距离接触、且敌方反坦面较窄时早手；开阔长线会让 Damian 变成被风筝目标。"
    slot_2_3: "可作为目标身体和进场计划手，但要补长手、清投掷或反控制。"
    slot_4_5: "适合回答敌方脆弱控制/支援阵容，同时避免把 Otis/Clancy/Chester 这类硬反制留给敌方最后手。"
    slot_6: "如果敌方三人缺稳定反坦和落点控制，Damian 可以作为高上限目标位压制 pick。"
```

## 关联页面

- [[sources/Fandom-Damian|Fandom 来源摘要: Damian]]
- [[sources/PLP-Damian|PLP 来源摘要: Damian]]
