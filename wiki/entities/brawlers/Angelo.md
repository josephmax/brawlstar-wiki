# Angelo

## 基本信息

- 稀有度：Epic
- 定位：Marksman
- 类型：蓄力毒伤远程英雄

## 攻击特征

- 主攻击可以蓄力
- 蓄力后射程和伤害更高
- 攻击会附带持续压制效果

## 超级技能特征

- Super 会帮助他进一步建立远程压制和位移优势
- 很适合在拉开距离后继续施压
- 能把远程消耗打得更有持续性

## 适合场景

- 开阔地图
- 需要远程压制和反复骚扰的模式
- 想要兼顾狙击与持续伤害的对局

## 角色定位总结

Angelo 是一个靠蓄力远射和毒伤持续压制敌人的远程英雄，和 `Piper`、`Bea` 相比，他更强调持续伤害和消耗节奏。

## 关联页面

- [[sources/Fandom-Angelo|Fandom 来源摘要: Angelo]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-29"
    user_notes: "none"

  capability_vector:
    effective_range: very_long
    projectile_reliability: medium_high; one charged arrow is high value but miss cost is large
    burst: very_high_when_charged_and_poisoned
    sustained_dps: medium; quick reload but meaningful damage requires charge time
    objective_damage: high_conditional_in_Heist_with_safe_access_and_Super
    mobility: high; very fast speed, water trait, Stinging Flight jump
    survivability: medium_high_with_water_or_Empower; low_if_pinned_while_charging
    engage: medium; Stinging Flight can close, but Angelo prefers poke
    disengage: high_with_water_route_or_Stinging_Flight
    anti_aggro: conditional; jump and water spacing, not hard control
    anti_tank: medium_high_if_distance_and_charge_are_preserved
    wall_break: low
    throw_or_wall_bypass: conditional_with_Master_Fletcher
    area_control: medium; Super poison cloud controls a small zone
    scouting_or_vision: low
    team_support: low_medium; healing reduction poison helps team focus but no direct ally buff
    water_route_access: high
    source_trace:
      - "[[sources/Fandom-Angelo|Fandom-Angelo]]"
      - "[[sources/PLP-Angelo|PLP-Angelo]]"

  build_switches:
    - build: "Stinging Flight / Empower / Damage, Shield, Gadget Cooldown"
      source: "[[sources/PLP-Angelo|PLP-Angelo]]"
      changes_capabilities:
        - "Stinging Flight gives jump escape, wall crossing, and emergency finish"
        - "Empower turns Angelo's Super into self-sustain anchor"
        - "Gadget Cooldown raises escape or safe-entry frequency"
      enables:
        - water_or_jump_reposition
        - charged_pick_pressure
        - heist_safe_entry_burst
      mitigates_failure_modes:
        - low_health_dive_pressure
        - no_auto_regen_while_charging
      poor_when:
        - "地图缺水/跳跃路线，且敌方投掷或召唤物能持续占住掩体"
      bp_use: default_reviewed_build_for_open_or_water_maps
    - build: "Master Fletcher / Flow water-map variant"
      source: "[[sources/Fandom-Angelo|Fandom-Angelo]]"
      changes_capabilities:
        - "Master Fletcher lets one charged shot pierce walls and enemies"
        - "Flow raises water-path mobility"
      enables:
        - surprise_wall_pierce_pick
        - water_lane_dodge_and_reposition
      mitigates_failure_modes:
        - enemy_hiding_behind_single_wall
        - long_water_lane_duel
      poor_when:
        - "缺乏水域或墙后关键目标时，Empower/Stinging Flight 更稳定"
      bp_use: map_specific_build_switch

  map_feature_hooks:
    - map_feature_type: "long_sightline"
      uses_feature_by: "charged very-long arrow threatens low-health marksmen and controls open approach"
      route_or_position: "open side lane or Knockout/Bounty sightline with retreat space"
      objective_conversion: "early pick pressure, zone denial by threat, and safe poke"
      active_when: "Angelo can charge safely and enemy cannot hide after each shot"
      fails_if: "walls or summons absorb arrows, or pressure interrupts charge"
      example_maps:
        - Shooting Star
        - Dry Season
        - Out in the Open
        - Flaring Phoenix
      bp_use: required_capabilities.long_range_burst
    - map_feature_type: "water_crossing_or_obstacle_bypass"
      uses_feature_by: "Trait lets Angelo move over water; Flow and Stinging Flight amplify reposition"
      route_or_position: "water edge or water lane that creates an off-angle while keeping range"
      objective_conversion: "Heist safe access, Knockout retreat angle, Hot Zone safe poke"
      active_when: "water route gives range or objective pressure rather than only movement"
      fails_if: "crossing water puts Angelo in short-range trap or away from objective damage"
      example_maps:
        - Safe Zone
        - Safe(r) Zone
        - Out in the Open
        - New Horizons
        - Parallel Plays
      bp_use: map_bp_factors.route_gate_and_false_positive_filter
    - map_feature_type: "heist_safe_entry_window"
      uses_feature_by: "Stinging Flight plus Super can enter safe area and create poison damage window"
      route_or_position: "safe-side route with jump or water access"
      objective_conversion: "burst safe damage or force defenders to turn back"
      active_when: "entry is protected by teammate pressure and Angelo can leave or survive after Super"
      fails_if: "enemy has immediate anti-dive, safe route is watched, or Angelo dies before damage converts"
      example_maps:
        - Safe Zone
        - Bridge Too Far
        - Hot Potato
      bp_use: candidate_eval.heist_objective_access

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - conditional_safe_burst_with_Super
        - water_or_jump_safe_access
        - long_range_lane_pressure
      cannot_fulfill:
        - stable_body_defense
        - wallbreak_to_create_angle
      needs_teammate_support:
        - lane_pressure_to_cover_entry
        - anti_thrower_or_anti_dive
      false_positive: "Water access is a trap if it does not create a safe damage window"
    - mode: "Bounty"
      can_fulfill:
        - low_commitment_high_damage_pick
        - water_angle_survival
        - healing_reduction_on_poisoned_target
      cannot_fulfill:
        - rapid_multi_target_clear
        - safe_bush_check
      needs_teammate_support:
        - vision_or_wall_answer
        - teammate_pressure_while_Angelo_charges
      false_positive: "One-shot pressure can disappear if enemies use summons or force Angelo to stop charging"
    - mode: "Knockout"
      can_fulfill:
        - opening_pick_threat
        - final_ring_poke
        - water_or_jump_reposition
      cannot_fulfill:
        - guaranteed_close_range_duel
        - persistent_thrower_clear
      needs_teammate_support:
        - anti_thrower_or_summon_answer
        - peel_if_enemy_has_dive
      false_positive: "If gas or walls remove retreat space, Angelo's charge cycle becomes fragile"

  failure_modes:
    - id: "charge_cycle_interrupted"
      active_when: "Angelo is knocked back, pulled, stunned, or forced to cancel charged aim"
      exposed_by: "[[sources/Fandom-Angelo|Fandom-Angelo]] Take Aim charge and interruption rules"
      mitigation: "charge from protected angle, use water route, or keep Stinging Flight for reset"
      bp_use: "candidate_eval.execution_risk"
    - id: "no_auto_regen_while_charging"
      active_when: "poke damage accumulates while Angelo holds charge and cannot auto-heal"
      exposed_by: "[[sources/Fandom-Angelo|Fandom-Angelo]] attack section"
      mitigation: "Empower, Shield gear, shorter charge cycles, or healer support"
      bp_use: "false_positive_filter"
    - id: "water_route_without_pressure"
      active_when: "water movement exists but does not create range, safe damage, or retreat value"
      exposed_by: "[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]] false positive rule"
      mitigation: "only count water if it opens a real objective route or safe off-angle"
      bp_use: "map_factor_false_positive_check"
    - id: "wall_or_summon_absorbs_single_arrow"
      active_when: "enemy plays behind wall, deploys bodies, or rotates during Angelo charge"
      exposed_by: "[[sources/PLP-Angelo|PLP-Angelo]] counteredBy wall/control picks"
      mitigation: "Master Fletcher, wallbreak teammate, or choose open lane"
      bp_use: "must_answer_or_avoid"

  conditional_matchup_seeds:
    - target:
        - "Belle"
        - "Colette"
        - "Brock"
        - "Bea"
        - "Gene"
        - "Colt"
        - "Byron"
      direction: "subject_favored"
      source: "[[sources/PLP-Angelo|PLP-Angelo]]"
      mechanism: "very long charged burst and water/jump reposition let Angelo win poke windows against many linear marksmen"
      active_when: "open map, Angelo can hold charge safely, and water or speed creates dodge angle"
      fails_when: "target has safer wall angle, summons, or burst follow-up while Angelo charges"
      bp_use: "lane_duel_or_last_pick_seed"
    - target:
        - "Mandy"
        - "Grom"
        - "Larry & Lawrie"
        - "Tara"
        - "Nani"
        - "Mr. P"
      direction: "target_favored"
      source: "[[sources/PLP-Angelo|PLP-Angelo]]"
      mechanism: "longer prepared shots, thrower arcs, summons, or body pressure interfere with Angelo's single-arrow charge cycle"
      active_when: "walls/summons protect target or enemy can pressure Angelo before charge releases"
      fails_when: "map is open, summons are absent, or Angelo can take water off-angle"
      bp_use: "avoid_or_pair_with_wallbreak_and_summon_clear"
    - target:
        - "Kit"
        - "Stu"
        - "Mico"
        - "Edgar"
      direction: "volatile"
      source: "[[sources/Fandom-Angelo|Fandom-Angelo]]"
      mechanism: "Angelo can escape with Stinging Flight, but loses if dive forces charge cancel twice"
      active_when: "Stinging Flight is available and route lets Angelo reset to range"
      fails_when: "dive chains CC, lands after gadget is spent, or team lacks peel"
      bp_use: "build_requirement_or_ban_reason"

  slot_notes:
    slot_1: "适合在水图或极开阔长线图先手；需要避开敌方低成本召唤物/投掷 2-3 回答。"
    slot_2_3: "可回答敌方普通射手或建立 Heist 进库路线，但要配一手处理投掷/召唤物。"
    slot_4_5: "用于补远程爆发、水路访问或 safe burst；必须检查敌方 6 位是否能补硬突进。"
    slot_6: "当敌方缺召唤物、投掷和连段突脸时，Angelo 可作为高收益长线惩罚位。"
```
