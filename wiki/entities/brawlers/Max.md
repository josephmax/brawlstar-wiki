# Max

## 基本信息

- 稀有度：Mythic
- 定位：Support
- 来源：神话辅助英雄

## 攻击特征

- 主攻击是快速发射的长距离多弹丸射击
- 输出稳定，擅长边走边打
- 适合持续施压、追击和撤退掩护

## 超级技能特征

- Super 会提高自己和队友的移动速度
- 能让整队更快进攻、转点或脱离危险
- 兼具节奏推进和团队救援价值

## 适合场景

- 需要快速轮转的模式
- 队伍要一起推进或撤退的对局
- 追击、控场和抢节奏的阵容
- 想把队伍整体速度拉高的团队配合

## 角色定位总结

Max 是速度型支援，她的核心价值是让整队更快地进、退、追和转点。

## 与其他英雄的区别

- 不同于 `Gene`：Gene 用拉人改变站位，Max 用加速改变节奏
- 不同于 `Byron`：Byron 是远程治疗与消耗，Max 是纯节奏支援
- 不同于 `Poco`：Poco 偏群体治疗，Max 偏全队机动性

## 关联页面

- [[sources/Fandom-Max|Fandom 来源摘要: Max]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-29"
    user_notes: "none"

  capability_vector:
    effective_range: mid_long
    projectile_reliability: medium_high; four quick projectiles with slight spread reward movement mirroring
    burst: medium_high_when_all_projectiles_connect
    sustained_dps: high; four ammo slots and very fast reload
    objective_damage: low_medium; contributes lane pressure more than direct safe race
    mobility: very_high; fast base speed, team Super speed, Phase Shifter dash
    survivability: medium_high_with_Phase_Shifter_or_Sneaky_Sneakers
    engage: high_as_team_tempo_enabler
    disengage: high; Super and Phase Shifter reset fights
    anti_aggro: medium; speed/immune dash avoids burst but lacks hard CC
    anti_tank: medium_if_kiting_space_exists
    wall_break: low
    throw_or_wall_bypass: low; Phase Shifter cannot pass walls or water
    area_control: medium_by_tempo_and_chip_not_zone_denial
    scouting_or_vision: low
    team_support: very_high; speed boost changes engage, retreat, rotation, and chase windows
    tempo_control: high
    source_trace:
      - "[[sources/Fandom-Max|Fandom-Max]]"
      - "[[sources/PLP-Max|PLP-Max]]"

  build_switches:
    - build: "Phase Shifter / Super Charged / Shield, Damage"
      source: "[[sources/PLP-Max|PLP-Max]]"
      changes_capabilities:
        - "Phase Shifter gives a short immune dash to dodge lethal projectiles or reset entry"
        - "Super Charged turns constant movement into more frequent team speed windows"
        - "Shield and Damage stabilize mid-range skirmishes while Max keeps tempo"
      enables:
        - team_speed_engage
        - rotation_and_retreat
        - projectile_dodge_lane
      mitigates_failure_modes:
        - caught_by_single_high_damage_projectile
        - slow_team_rotation
      poor_when:
        - "队伍没有能利用加速进场或追击的队友，Max 会只剩中等输出"
      bp_use: default_reviewed_build_for_team_tempo
    - build: "Sneaky Sneakers / Run n' Gun aggression variant"
      source: "[[sources/Fandom-Max|Fandom-Max]]"
      changes_capabilities:
        - "Sneaky Sneakers allows a 3-second aggressive trade followed by health reset if not killed"
        - "Run n' Gun improves reload while Max constantly moves"
      enables:
        - temporary_deep_pressure
        - sustained_midrange_dps
      mitigates_failure_modes:
        - low_damage_if_only_chipping
        - need_to_force_short_trade
      poor_when:
        - "return marker can be camped, especially near bushes or enemy spawn"
      bp_use: aggression_build_switch_if_return_anchor_safe

  map_feature_hooks:
    - map_feature_type: "team_speed_rotation"
      uses_feature_by: "Super speed boosts Max and nearby allies for engage, retreat, or rotation"
      route_or_position: "wide mid or split-lane map where rotating first creates objective access"
      objective_conversion: "Gem carrier retreat, Hot Zone rotation, Brawl Ball push, Knockout collapse"
      active_when: "team has brawlers that convert speed into pressure or survival"
      fails_if: "team is static, enemy has hard CC, or objective does not reward rotation"
      example_maps:
        - Double Swoosh
        - Hard Rock Mine
        - Parallel Plays
        - Center Stage
      bp_use: map_bp_factors.rotation_and_tempo
    - map_feature_type: "open_lane_dodge_pressure"
      uses_feature_by: "fast movement plus Phase Shifter lets Max contest projectile lanes without being a pure sniper"
      route_or_position: "open or semi-open lane with dodge space and no hard wall pocket"
      objective_conversion: "keep lane alive, bait sniper shots, create chase window after enemy misses"
      active_when: "enemy damage is projectile-based and Max has room to strafe"
      fails_if: "enemy uses unavoidable area control, traps, slows, or hard CC"
      example_maps:
        - Shooting Star
        - Out in the Open
        - Dry Season
        - Ring of Fire
      bp_use: candidate_eval.projectile_dodge_lane
    - map_feature_type: "speed_enabled_scoring_or_chase_window"
      uses_feature_by: "team speed converts a small health or position advantage into a score/kill"
      route_or_position: "Brawl Ball midfield or Gem Grab side lane after one enemy is low"
      objective_conversion: "score attempt, gem carrier chase, or collapse on exposed backline"
      active_when: "enemy has spent CC and our team can enter together"
      fails_if: "speed sends team into choke, wall, or anti-aggro setup"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
        - Gem Fort
      bp_use: slot_task.engage_timing_support

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - speed_carrier_retreat
        - side_lane_chase
        - mid_pressure_through_constant_chip
      cannot_fulfill:
        - safe_primary_gem_carrier_without_cover
        - hard_area_denial
      needs_teammate_support:
        - true_mid_control_or_tank_answer
        - bush_vision_if_grass_map
      false_positive: "Speed helps retreat only if the carrier already has a safe route"
    - mode: "Brawl Ball"
      can_fulfill:
        - team_speed_push
        - chase_after_wall_open_or_enemy_mistake
        - emergency_escape
      cannot_fulfill:
        - wallbreak_goal_opening
        - hard_knockback_defense
      needs_teammate_support:
        - scorer_or_wallbreak
        - anti_tank_or_stun
      false_positive: "Fast team movement does not equal scoring if goal geometry is closed"
    - mode: "Bounty"
      can_fulfill:
        - dodge_projectile_lane
        - chase_low_target
        - retreat_after_lead
      cannot_fulfill:
        - low_commitment_long_range_pick
        - thrower_pocket_clear
      needs_teammate_support:
        - long_range_damage_or_pull
        - vision_against_bush_flank
      false_positive: "Max can survive long lanes but may not create stars without a finisher"
    - mode: "Knockout"
      can_fulfill:
        - speed_collapse_after_chip
        - team_retreat_before_gas
        - dodge_and_bait_projectiles
      cannot_fulfill:
        - solo_burst_pick
        - hard_thrower_answer
      needs_teammate_support:
        - teammate_with_burst_or_control
        - anti_CC
      false_positive: "If gas closes into hard control, Max speed may only delay the loss"

  failure_modes:
    - id: "speed_without_conversion"
      active_when: "team has no scorer, finisher, tank, or burst follow-up to exploit Max Super"
      exposed_by: "[[sources/Fandom-Max|Fandom-Max]] Super is movement support, not damage or CC"
      mitigation: "pair with engage, scorer, or burst teammate before valuing Max highly"
      bp_use: "candidate_eval.required_support"
    - id: "hard_control_stops_tempo"
      active_when: "enemy has slow, stun, pull, trap, or silence on the route Max wants to accelerate through"
      exposed_by: "[[sources/Fandom-Max|Fandom-Max]] Phase Shifter still retains status effects"
      mitigation: "bait CC first, choose alternate route, or avoid speed engage plan"
      bp_use: "must_avoid_or_plan_protection"
    - id: "return_or_dash_anchor_punished"
      active_when: "Sneaky Sneakers marker or Phase Shifter endpoint is camped"
      exposed_by: "[[sources/Fandom-Max|Fandom-Max]] Gadget tips warn about ambush at return location"
      mitigation: "place return marker away from bushes/spawn or prefer Phase Shifter"
      bp_use: "false_positive_filter"
    - id: "low_pick_pressure_on_pure_long_range"
      active_when: "Max can dodge but cannot threaten kills into true snipers or throwers"
      exposed_by: "[[sources/PLP-Max|PLP-Max]] matchup signals include sniper/control answers"
      mitigation: "add long-range finisher, pull, or wallbreak teammate"
      bp_use: "role_coverage_check"

  conditional_matchup_seeds:
    - target:
        - "Colt"
        - "Nani"
        - "Brock"
        - "Bo"
        - "Tick"
        - "Sprout"
        - "Byron"
        - "Frank"
      direction: "subject_favored"
      source: "[[sources/PLP-Max|PLP-Max]]"
      mechanism: "speed and Phase Shifter let Max dodge linear pressure, close weak angles, or chase immobile targets after chip"
      active_when: "map gives dodge space and target lacks hard CC or protected pocket"
      fails_when: "target plays behind wall/summon or Max lacks damage follow-up"
      bp_use: "tempo_response_pick_candidate"
    - target:
        - "Tara"
        - "Bea"
        - "Gene"
        - "Ruffs"
        - "Spike"
        - "Carl"
        - "Crow"
        - "Otis"
      direction: "target_favored"
      source: "[[sources/PLP-Max|PLP-Max]]"
      mechanism: "control, slow, pull, silence, or persistent damage punishes Max's speed path and prevents clean tempo conversion"
      active_when: "enemy can hold the route Max must accelerate through"
      fails_when: "Max can bait key tool first or attack from a different lane with teammate cover"
      bp_use: "must_answer_control_before_speed_plan"
    - target:
        - "Piper"
        - "Mandy"
        - "Belle"
        - "Angelo"
      direction: "volatile"
      source: "[[sources/Fandom-Max|Fandom-Max]]"
      mechanism: "Max can dodge and close windows, but loses if long-range target keeps safe angle and Max lacks burst"
      active_when: "wide lane gives Max room and teammate can finish after speed engage"
      fails_when: "sniper has protected line, trap, or teammate peel"
      bp_use: "lane_execution_check"

  slot_notes:
    slot_1: "可在需要团队速度且地图不会被硬控低成本惩罚时先手；否则容易被 2-3 位控制/投掷压住。"
    slot_2_3: "适合作为节奏引擎，配合 scorer、刺客或爆发队友一起打开计划。"
    slot_4_5: "用于修复转点、追击或撤退能力；要检查敌方 6 位是否能补 hard CC。"
    slot_6: "如果敌方缺硬控和减速且已暴露脆后排，Max 可以作为速度收割或保领先选择。"
```
