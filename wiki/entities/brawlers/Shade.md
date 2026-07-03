# Shade

## 基本信息

- 稀有度：Epic
- 定位：Assassin
- 类型：穿墙贴身刺客

## 攻击特征

- 主攻击是短距离弧形挥击
- 中心命中会造成更高伤害
- 攻击能穿过墙体打到对手

## 超级技能特征

- Super 让 Shade 短时穿墙并获得移速加成
- 可以改变进场路线，也能用来压迫后排
- 很适合在墙多的地图里反复切位

## 适合场景

- 墙体密集、路线复杂的地图
- 需要贴身骚扰和绕后的模式
- 对手依赖固定站位的局面

## 角色定位总结

Shade 是把地形当作武器的刺客，靠穿墙和短程压迫不断制造切入窗口。

## 关联页面

- [[sources/Fandom-Shade|Fandom 来源摘要: Shade]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-29"
    user_notes: "none"

  capability_vector:
    effective_range: short_to_mid_with_Longarms
    projectile_reliability: high_in_wall_or_choke_range; attack has wind-up and center sweet spot
    burst: high_if_center_hit_or_Hypercharged_Super
    sustained_dps: medium_high; very fast reload but short range
    objective_damage: medium_conditional; close-range DPS if it reaches target
    mobility: very_high_with_Super_and_water_trait
    survivability: medium_high_during_Super_with_Hardened_Hoodie
    engage: high_from_wall_phase_or_water_route
    disengage: medium_high_if_Super_duration_remaining
    anti_aggro: medium; Jump Scare slow helps, but Shade prefers initiating from terrain
    anti_tank: low_medium; high-health melee can punish short range
    wall_break: low
    throw_or_wall_bypass: very_high; attacks through walls and Super passes obstacles
    area_control: medium; wall threat and Radius trait tax nearby enemies
    scouting_or_vision: medium; Radius trait charges even from invisible/bush enemies in range
    team_support: low; pressure and route denial are indirect
    water_route_access: high
    source_trace:
      - "[[sources/Fandom-Shade|Fandom-Shade]]"
      - "[[sources/PLP-Shade|PLP-Shade]]"

  build_switches:
    - build: "Longarms / Hardened Hoodie / Shield, Damage"
      source: "[[sources/PLP-Shade|PLP-Shade]]"
      changes_capabilities:
        - "Longarms extends next attack and helps charge Super from safer distance"
        - "Hardened Hoodie gives damage reduction during wall-phase Super"
        - "Shield/Damage stabilizes short-range entry trades"
      enables:
        - wall_phase_entry
        - through_wall_pressure
        - short_range_objective_brawl
      mitigates_failure_modes:
        - short_range_gap_before_Super
        - burst_taken_during_Super_entry
      poor_when:
        - "地图开阔、墙体少，Longarms 仍不足以解决接近成本"
      bp_use: default_reviewed_build_for_wall_dense_maps
    - build: "Jump Scare / Spooky Speedster chase variant"
      source: "[[sources/Fandom-Shade|Fandom-Shade]]"
      changes_capabilities:
        - "Jump Scare gives a local slow after Shade reaches contact range"
        - "Spooky Speedster rewards center hits with chase speed"
      enables:
        - close_range_chase
        - scorer_or_carrier_catch
      mitigates_failure_modes:
        - target_escapes_after_first_hit
      poor_when:
        - "需要进场生存时，Hardened Hoodie 通常更稳"
      bp_use: last_pick_chase_or_ball_mode_variant

  map_feature_hooks:
    - map_feature_type: "thrower_pocket"
      uses_feature_by: "Shade attacks through walls and can enter walls during Super"
      route_or_position: "wall-adjacent pocket, Hot Zone wall, or Gem/Ball side wall"
      objective_conversion: "force thrower/control off wall, clear zone edge, or open scoring path"
      active_when: "walls are intact and target cannot outrange or hit Shade through wall"
      fails_if: "enemy is a thrower that still hits Shade, or Super ends in bad position"
      example_maps:
        - Parallel Plays
        - Belle's Rock
        - Hard Rock Mine
        - Pinball Dreams
      bp_use: must_answer_wall_pocket_candidate
    - map_feature_type: "water_crossing_or_obstacle_bypass"
      uses_feature_by: "Water trait and Super obstacle pass create unusual approach lines"
      route_or_position: "water edge, wall-water gap, or obstacle route near objective"
      objective_conversion: "reach carrier/zone/safe route from an angle normal short-range heroes cannot use"
      active_when: "route lets Shade start within threat range and still retreat before Super ends"
      fails_if: "route only moves Shade into open fire or short-range mirror"
      example_maps:
        - Safe Zone
        - Safe(r) Zone
        - New Horizons
        - Parallel Plays
      bp_use: map_bp_factors.route_gate_and_false_positive_filter
    - map_feature_type: "wall_phase_survival_anchor"
      uses_feature_by: "Super lets Shade hide inside/through walls while pressuring nearby enemies"
      route_or_position: "wall next to zone, gem mine, or ball lane"
      objective_conversion: "stall zone, threaten carrier, or deny defender position"
      active_when: "enemy lacks through-wall answer and Shade tracks Super duration"
      fails_if: "enemy outranges through angle, throws over wall, or Super expires into enemy"
      example_maps:
        - Parallel Plays
        - Ring of Fire
        - Center Stage
        - Gem Fort
      bp_use: candidate_eval.survival_space_and_route_denial

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - wall_side_pressure
        - punish_gem_carrier_near_wall
        - route_denial_with_Radius_trait
      cannot_fulfill:
        - safe_long_range_mid_control
        - bush_vision_from_distance
      needs_teammate_support:
        - mid_range_damage
        - anti_thrower_if_enemy_can_hit_wall
      false_positive: "Wall pressure does not help if gem mine is open and Shade never gets Super"
    - mode: "Brawl Ball"
      can_fulfill:
        - wall_phase_defender_disruption
        - short_range_scoring_pressure
        - slow_or_center_hit_chase
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - long_range_clear
      needs_teammate_support:
        - scorer_or_wallbreak
        - control_to_hold_ball_lane
      false_positive: "Shade can reach defenders but still needs a scoring route"
    - mode: "Heist"
      can_fulfill:
        - short_range_safe_pressure_if_route_exists
        - wall_or_water_entry_to_base
        - defender_disruption
      cannot_fulfill:
        - long_range_safe_angle
        - stable_base_anchor
      needs_teammate_support:
        - lane_pressure_to_cover_entry
        - true_safe_dps_if_Shade_cannot_stay
      false_positive: "Heist fit is route-dependent; short range can become a trap near enemy base"
    - mode: "Hot Zone"
      can_fulfill:
        - wall_zone_pressure
        - contest_zone_edge
        - force_ranged_enemy_off_position
      cannot_fulfill:
        - open_zone_body_against_long_range
        - thrower_clear_from_safety
      needs_teammate_support:
        - zone_body_or_heal
        - anti_thrower
      false_positive: "Shade cannot solo hold a zone if enemies can hit the wall anchor safely"

  failure_modes:
    - id: "super_ends_in_bad_position"
      active_when: "Shade remains inside or beyond a wall when Incorporeal Form expires"
      exposed_by: "[[sources/Fandom-Shade|Fandom-Shade]] Super duration and push-out rule"
      mitigation: "track timer, refresh Super, or retreat before expiry"
      bp_use: "candidate_eval.execution_risk"
    - id: "open_map_range_gap"
      active_when: "map lacks walls/water routes and enemy can kite Shade before Super charges"
      exposed_by: "[[sources/Fandom-Shade|Fandom-Shade]] short range and Longarms build note"
      mitigation: "pick only on wall-dense maps or pair with speed/control"
      bp_use: "must_avoid_or_needs_support"
    - id: "through_wall_answer_exists"
      active_when: "enemy thrower, Hank/Doug/Jacky/Mico, or similar can damage Shade despite wall"
      exposed_by: "[[sources/Fandom-Shade|Fandom-Shade]] tips warn about enemies that can still hit Shade"
      mitigation: "avoid wall-anchor plan or draft answer to that enemy first"
      bp_use: "must_answer_or_avoid"
    - id: "center_hit_dependency"
      active_when: "Shade only clips outer arc and loses doubled damage or Spooky Speedster chase"
      exposed_by: "[[sources/Fandom-Shade|Fandom-Shade]] Haunted Hug center damage"
      mitigation: "use Longarms/Jumpscare timing or attack from wall where center hit is likely"
      bp_use: "map_factor_false_positive_check"

  conditional_matchup_seeds:
    - target:
        - "Mr. P"
        - "Jessie"
        - "Gale"
        - "Sprout"
        - "Brock"
        - "Jae-Yong"
        - "Squeak"
        - "Nani"
      direction: "subject_favored"
      source: "[[sources/PLP-Shade|PLP-Shade]]"
      mechanism: "wall-phase entry and through-wall attacks punish backline or control picks that depend on fixed cover"
      active_when: "map has walls near the target and Shade can charge or activate Super before being kited"
      fails_when: "target has through-wall answer, bodyguard, or open retreat space"
      bp_use: "response_pick_candidate_against_wall_backline"
    - target:
        - "Doug"
        - "Jacky"
        - "Trunk"
        - "Frank"
        - "Finx"
        - "Bibi"
        - "Ash"
        - "Hank"
      direction: "target_favored"
      source: "[[sources/PLP-Shade|PLP-Shade]]"
      mechanism: "bulky short-range or through-wall punishers survive Shade's burst and punish its close-range timing"
      active_when: "objective forces Shade into melee or enemy can hold the wall anchor"
      fails_when: "Shade can ignore them and access a fragile backline or carrier"
      bp_use: "avoid_or_require_team_damage"
    - target:
        - "Barley"
        - "Larry & Lawrie"
        - "Willow"
        - "Mico"
        - "Jacky"
      direction: "volatile"
      source: "[[sources/Fandom-Shade|Fandom-Shade]]"
      mechanism: "Shade likes walls, but some enemies can still damage through/over walls and deny the anchor"
      active_when: "enemy controls the same wall pocket Shade wants to use"
      fails_when: "Shade has Super timing, teammate pressure, or alternate wall route"
      bp_use: "wall_anchor_false_positive_check"

  slot_notes:
    slot_1: "只在墙体密集且敌方 through-wall 回答受限时考虑先手；开阔图先手风险很高。"
    slot_2_3: "适合回答依赖固定墙位的后排/控场，同时要求队友补远程输出。"
    slot_4_5: "可用于补墙体进场、Hot Zone 贴墙压制或 Brawl Ball 后排骚扰；检查敌方 6 位坦克/投掷回答。"
    slot_6: "敌方缺厚前排、缺穿墙/投掷答案且关键目标靠墙时，Shade 可以作为惩罚位。"
```
