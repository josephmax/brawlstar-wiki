# Rico

## 基本信息

- 稀有度：Super Rare
- 定位：Damage Dealer
- 类型：远程反弹射手

## 攻击特征

- 主攻击的子弹会在墙体间反弹
- 擅长利用地形延长射程和改变角度
- 在狭窄地形里更容易打出高收益

## 超级技能特征

- Super 会发射更长、更密集的弹射子弹
- 子弹可穿透敌人并继续反弹
- 能把墙体地形转化成持续火力优势

## 适合场景

- 墙体多、走廊多的地图
- 需要远距离消耗和压线的模式
- 需要通过角度打穿敌方站位的对局

## 角色定位总结

Rico 是最典型的地形利用型输出英雄之一。和 `Colt` 的直线穿透相比，他更强调反弹角度；和 `Jessie`、`Penny` 的炮台控场相比，他更依赖自己亲手打出墙体收益。

## 关联页面

- [[sources/Fandom-Rico|Fandom 来源摘要: Rico]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-29"
    user_notes: "none"

  capability_vector:
    effective_range: very_long_with_bounces
    projectile_reliability: high_in_corridors_medium_in_open_field
    burst: high_if_multiple_bullets_or_Multiball_connect
    sustained_dps: high; very fast reload
    objective_damage: high_conditional_on_bounce_lane_or_safe_angle
    mobility: low_medium; Robo Retreat creates low-health speed escape
    survivability: low_base_medium_with_Bouncy_Castle_or_Robo_Retreat
    engage: low
    disengage: medium_if_wall_bounce_cover_or_Robo_Retreat_active
    anti_aggro: conditional; strong in corridors with bounce pressure, weak in open dive
    anti_tank: medium_high_in_choke
    wall_break: low; prefers walls intact
    throw_or_wall_bypass: high_via_bounce_angles
    area_control: high_on_enclosed_lanes
    scouting_or_vision: low
    team_support: lane_denial_and_wall_punish
    wall_dependency: high
    source_trace:
      - "[[sources/Fandom-Rico|Fandom-Rico]]"
      - "[[sources/PLP-Rico|PLP-Rico]]"

  build_switches:
    - build: "Multiball Launcher / Super Bouncy / Shield, Damage"
      source: "[[sources/PLP-Rico|PLP-Rico]]"
      changes_capabilities:
        - "Multiball Launcher gives close-range burst and enclosed-area punish"
        - "Super Bouncy turns wall contact into major damage increase"
        - "Shield/Damage gears stabilize low-health ranged fights"
      enables:
        - bounce_wall_lane_control
        - anti_aggro_in_corridor
        - heist_or_ball_lane_damage
      mitigates_failure_modes:
        - low_health_duel_pressure
        - open_target_unreliability_when_walls_create_angles
      poor_when:
        - "敌方开墙后地图变开阔，Super Bouncy 价值大幅下降"
      bp_use: default_reviewed_build_for_closed_or_bounce_maps
    - build: "Bouncy Castle / Robo Retreat sustain-or-escape variant"
      source: "[[sources/Fandom-Rico|Fandom-Rico]]"
      changes_capabilities:
        - "Bouncy Castle turns bounce count into self-heal"
        - "Robo Retreat gives high speed below low-health threshold"
      enables:
        - survival_after_bounce_trade
        - low_health_kiting
      mitigates_failure_modes:
        - chip_damage_on_bounty_or_knockout
        - dive_escape_after_first_contact
      poor_when:
        - "地图缺多段反弹，或敌方能一波秒杀不让 Rico 触发循环"
      bp_use: survivability_build_switch

  map_feature_hooks:
    - map_feature_type: "bounce_wall_corridor"
      uses_feature_by: "bullets bounce off walls, gain range, and can hit enemies behind cover"
      route_or_position: "side corridor, L-wall, or goal lane where Rico can shoot from cover"
      objective_conversion: "lane lock, ball control, gem side denial, or Knockout space control"
      active_when: "walls remain intact and enemy must pass through the bounce lane"
      fails_if: "enemy opens walls, plays fully open field, or outranges from non-bounce angle"
      example_maps:
        - Pinball Dreams
        - Hard Rock Mine
        - Layer Cake
        - Belle's Rock
        - Triple Dribble
      bp_use: required_capabilities.bounce_wall_control
    - map_feature_type: "enclosed_anti_aggro_burst"
      uses_feature_by: "Multiball Launcher and Super Bouncy punish enemies trapped near Rico in a closed space"
      route_or_position: "short corridor, goal defense pocket, or side choke"
      objective_conversion: "deny scorer, punish assassin entry, or clear contested lane"
      active_when: "enemy engage path is narrow and Rico has wall geometry to multiply hits"
      fails_if: "dive enters from open angle, disables Rico, or forces him away from walls"
      example_maps:
        - Center Stage
        - Pinball Dreams
        - Triple Dribble
      bp_use: candidate_eval.anti_aggro_in_closed_lane
    - map_feature_type: "safe_or_objective_bounce_angle"
      uses_feature_by: "bounce range and piercing Super create indirect damage routes"
      route_or_position: "safe-facing wall, zone edge, or gem mine side wall"
      objective_conversion: "Heist chip, zone denial, or forcing defenders off objective"
      active_when: "objective angle exists without Rico leaving cover"
      fails_if: "objective is fully open with no bounce value or enemy wallbreak removes angle"
      example_maps:
        - Hot Potato
        - Pit Stop
        - Gem Fort
      bp_use: map_factor_fit.objective_angle

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - side_lane_wall_control
        - gem_mine_angle_denial
        - punish_grouped_mid_from_bounce
      cannot_fulfill:
        - safe_gem_carrier
        - bush_vision_tax
      needs_teammate_support:
        - mid_carrier_or_sustain
        - anti_wallbreak_if_Rico_plan_depends_on_walls
      false_positive: "Rico can dominate a wall lane but still fail if the gem carrier has no retreat plan"
    - mode: "Brawl Ball"
      can_fulfill:
        - lane_denial_from_goal_walls
        - anti_scorer_corridor_burst
        - clear_defenders_from_covered_angles
      cannot_fulfill:
        - primary_ball_carrier
        - reliable_wallbreak_score_window
      needs_teammate_support:
        - scorer_or_knockback
        - grass_control
      false_positive: "Indiscriminate wallbreak by teammates can erase Rico's best angles"
    - mode: "Heist"
      can_fulfill:
        - conditional_safe_damage_from_bounce_angle
        - lane_duel_pressure
        - punish_enemy_entry_route
      cannot_fulfill:
        - open_map_pure_safe_race_without_angle
        - base_body_defense
      needs_teammate_support:
        - wall_state_protection
        - true_safe_dps_if_bounce_angle_absent
      false_positive: "Heist label is weak if Rico cannot reach safe from a bounce route"
    - mode: "Knockout"
      can_fulfill:
        - wall_angle_space_control
        - final_ring_corridor_denial
        - punish_enemies_behind_cover
      cannot_fulfill:
        - open_field_marksman_duel_without_walls
        - hard_thrower_answer
      needs_teammate_support:
        - wallbreak_answer_to_enemy_throwers
        - peel_or_scouting
      false_positive: "Closed-map value flips if enemy has easy wallbreak or deeper thrower pocket"

  failure_modes:
    - id: "open_field_no_bounce_value"
      active_when: "map or wallbreak removes bounce angles and Rico must fight as a normal low-health shooter"
      exposed_by: "[[sources/Fandom-Rico|Fandom-Rico]] bounce-based attack and tips"
      mitigation: "pick Rico only where walls are durable or where bounce angle directly controls objective"
      bp_use: "map_factor_false_positive_check"
    - id: "wallbreak_erases_plan"
      active_when: "enemy or teammate opens the specific walls Rico needs for lane control"
      exposed_by: "[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]] terrain state plan"
      mitigation: "protect walls, ban/answer wallbreak, or choose non-wall-dependent DPS"
      bp_use: "terrain_state_plan_check"
    - id: "thrower_or_deeper_pocket_outcontrols"
      active_when: "enemy thrower controls Rico's bounce position from a safer wall pocket"
      exposed_by: "[[sources/PLP-Rico|PLP-Rico]] counteredBy thrower/control picks"
      mitigation: "pair wallbreak or dive, avoid picking Rico into uncontested thrower pockets"
      bp_use: "must_avoid_or_needs_support"
    - id: "low_health_dive_in_open_angle"
      active_when: "assassin reaches Rico outside a corridor before Multiball or bounce pressure converts"
      exposed_by: "[[sources/Fandom-Rico|Fandom-Rico]] low health and Robo Retreat/Bouncy Castle survival tools"
      mitigation: "play near walls, hold Multiball, pair peel, or switch to Bouncy Castle/Robo Retreat"
      bp_use: "false_positive_filter"

  conditional_matchup_seeds:
    - target:
        - "Mortis"
        - "Shelly"
        - "Nita"
        - "Jessie"
        - "Mico"
        - "Spike"
      direction: "subject_favored"
      source: "[[sources/PLP-Rico|PLP-Rico]]"
      mechanism: "closed-lane bounce pressure and Multiball punish targets that must enter Rico's wall geometry"
      active_when: "walls create narrow approach and Rico can keep range or point-blank burst in corridor"
      fails_when: "target approaches from open angle, has hard CC, or walls are removed"
      bp_use: "response_pick_candidate_on_closed_maps"
    - target:
        - "Sprout"
        - "Tara"
        - "Barley"
        - "Cordelius"
        - "Carl"
        - "Stu"
      direction: "target_favored"
      source: "[[sources/PLP-Rico|PLP-Rico]]"
      mechanism: "thrower control, pull/CC, wallbreak, or high mobility can deny Rico's chosen bounce lane"
      active_when: "enemy has deeper wall pocket, reliable wallbreak, or multiple approach angles"
      fails_when: "Rico's team opens enemy pocket while preserving Rico's own bounce walls"
      bp_use: "must_answer_before_locking_rico"
    - target:
        - "Penny"
        - "Jessie"
        - "Nita"
      direction: "subject_favored"
      source: "[[sources/PLP-Rico|PLP-Rico]]"
      mechanism: "pierce/bounce lanes can hit grouped summons and owners from indirect angles"
      active_when: "summons are placed near walls or lane choke"
      fails_when: "summon anchors are protected by thrower pocket or force Rico into open field"
      bp_use: "summon_pressure_response_candidate"

  slot_notes:
    slot_1: "只在墙体收益非常明确且敌方低成本开墙少时先手；否则容易被 2-3 位投掷/开墙回答。"
    slot_2_3: "适合回答短手进场或建立封路计划，并要求队友别过早破坏关键墙。"
    slot_4_5: "用于补 Brawl Ball/Gem/Knockout 的墙体控制；必须先检查敌方 6 位是否能补 thrower/wallbreak。"
    slot_6: "当敌方缺开墙、缺投掷且必须经过墙边目标路线时，Rico 是高收益惩罚位。"
```
