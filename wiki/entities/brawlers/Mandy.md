# Mandy

## 基本信息

- 稀有度：Chromatic
- 定位：Marksman
- 类型：蓄力狙击英雄

## 攻击特征

- 主攻击在专注时会拉长并增强
- 适合超远距离压线和精准惩罚
- 很依赖节奏和站位

## 超级技能特征

- Super 会发射一条超长射线
- 很适合穿线、收割和远距离压制
- 能在开阔地图里打出很强的存在感

## 适合场景

- 开阔地图
- 需要长线压制的模式
- 想通过一枪定节奏的对局

## 角色定位总结

Mandy 是一个靠蓄力超远射击和直线大招建立压制的狙击英雄，和 `Piper` 一样讲距离，但更强调专注后的高额一枪。

## 关联页面

- [[sources/Fandom-Mandy|Fandom 来源摘要: Mandy]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: draft_from_raw_signals
  review_gate: not_bp_ready; requires conditional matchup and map_bp_factor review
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "very_long_or_long; fandom_attack_range=9 (Long)<br> 12 (Focused)"
    projectile_reliability: "needs_review; raw_mentions_slow_delay_spread_or_random"
    burst: "burst_candidate_from_damage_or_super_text"
    sustained_dps: "reload_signal_from_fandom=1.5 seconds (Normal)"
    objective_damage: "heist_candidate_from_plp_modes=False"
    mobility: "mobility_or_speed_tool_text_present"
    survivability: "fandom_health=3000; low_health_failure_check; self_or_team_sustain_text_present"
    engage: "engage_candidate_if_mobility_or_cc_text_activates"
    disengage: "disengage_candidate_if_mobility_slow_stun_or_knockback_text_activates"
    anti_aggro: "candidate_from_control_or_escape_text"
    anti_tank: "candidate_from_high_damage_percent_slow_or_continuous_damage_text"
    wall_break: "not_observed_in_selected_raw"
    throw_or_wall_bypass: "not_observed_in_selected_raw"
    area_control: "present_from_area_zone_trap_puddle_or_spawnable_text"
    scouting_or_vision: "present_from_reveal_vision_bush_text"
    team_support: "present_from_heal_shield_speed_pull_or_buff_text"
    spawnable_or_pet: "present_from_spawn_turret_pet_minion_text"
    crowd_control: "present_from_slow_stun_knockback_pull_silence_text"
    terrain_creation: "present_from_wall_or_puddle_obstacle_creation_text"
    terrain_destruction: "not_observed_in_selected_raw"

  build_switches:
    - build: "Cookie Crumbs / In My Sights / Shield, Damage"
      source: "[[sources/PLP-Mandy|PLP-Mandy]]"
      changes_capabilities:
        - "third_party_build_candidate; exact capability delta needs mechanism review"
      enables:
        - "mode_candidate:Bounty"
        - "mode_candidate:Knockout"
      mitigates_failure_modes:
        - "unknown_until_reviewed_against_failure_modes"
      best_when: "PLP mode/matchup seed aligns with current map_bp_factors"
      poor_when: "build is copied without checking map route, enemy answers, or slot duty"
      bp_use: "build_candidate_not_final_recommendation"

  map_feature_hooks:
    - map_feature_type: "long_sightline"
      uses_feature_by: "range pressure candidate from Fandom attack range"
      objective_conversion: "mode/objective payoff must be checked against active map_bp_factors"
      active_when: "route offers safe line of sight and target access"
      fails_if: "enemy has low-cost approach, walls block line, or projectile reliability fails"
      example_maps: []
      bp_use: "candidate_generation_not_final"

  objective_contracts:
    - mode: "Bounty"
      can_fulfill:
        - "Bounty_candidate_from_plp"
        - "survival_range_pressure_candidate"
      cannot_fulfill:
        - "not_inferred_from_source; requires map/matchup review"
      needs_teammate_support:
        - "cover failure modes and convert source candidate into map objective"
      false_positive: "PLP mode fit is a seed; do not treat as unconditional map fit"
    - mode: "Knockout"
      can_fulfill:
        - "Knockout_candidate_from_plp"
        - "survival_range_pressure_candidate"
      cannot_fulfill:
        - "not_inferred_from_source; requires map/matchup review"
      needs_teammate_support:
        - "cover failure modes and convert source candidate into map objective"
      false_positive: "PLP mode fit is a seed; do not treat as unconditional map fit"

  failure_modes:
    - id: "low_health_pressure"
      active_when: "enemy can force close-range duel or repeated chip"
      exposed_by: "Fandom health field and selected mechanics"
      mitigation: "peel, range discipline, terrain plan, or survivability build"
      bp_use: "false_positive_filter"
    - id: "reliability_into_mobility"
      active_when: "enemy has speed, dash, cover, or unpredictable pathing"
      exposed_by: "selected Fandom text markers"
      mitigation: "pick on constrained routes or pair with control"
      bp_use: "must_avoid_or_needs_support"

  conditional_matchup_seeds:
    - target:
        - "El Primo"
        - "Meg"
        - "Jacky"
        - "Chuck"
        - "Poco"
        - "Frank"
        - "Lola"
        - "Clancy"
      direction: "subject_favored"
      source: "[[sources/PLP-Mandy|PLP-Mandy]]"
      mechanism: "pending; PLP seed must be explained through capability_vector before use"
      active_when: "requires map/mode/build validation"
      fails_when: "target has support, map disables mechanism, or source seed lacks local validation"
      bp_use: "conditional_matchup_seed_only"
    - target:
        - "Pearl"
        - "Najia"
        - "Angelo"
        - "Eve"
        - "Darryl"
        - "Damian"
        - "Sprout"
        - "Buster"
      direction: "target_favored"
      source: "[[sources/PLP-Mandy|PLP-Mandy]]"
      mechanism: "pending; PLP seed must be explained through capability_vector before use"
      active_when: "requires map/mode/build validation"
      fails_when: "map or comp removes target's access to the punishment mechanism"
      bp_use: "must_avoid_or_protection_seed_only"

  slot_notes:
    slot_1: "only if map objective contract and low-cost counter checks are already satisfied; PLP seed alone is insufficient"
    slot_2_3: "use as response or plan-building pick after checking enemy slot_1 and map duties"
    slot_4_5: "can repair role gaps or answer enemy 2-3, but must not leave a clean slot_6 punish"
    slot_6: "can punish exposed enemy draft only when conditional matchup seed is activated by map/mode/build"
```
