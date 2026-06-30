# Maisie

## 基本信息

- 稀有度：Chromatic
- 定位：Controller
- 类型：反开团控制英雄

## 攻击特征

- 主攻击带有中距离冲击特性
- 适合打断推进和逼退近战
- 更偏防守反打而不是强压线

## 超级技能特征

- Super 会造成大范围冲击并减速
- 很适合把突进敌人推回去
- 具有明显的反冲锋价值

## 适合场景

- 对手喜欢冲脸或强开团的对局
- 需要守点和反推的模式
- 地图中存在很多强行进场路线时

## 角色定位总结

Maisie 是一个靠冲击波和大范围减速来反打的控制英雄，她的价值很大一部分来自把对手的进攻打断。

## 关联页面

- [[sources/Fandom-Maisie|Fandom 来源摘要: Maisie]]

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
    effective_range: "long_mid; fandom_attack_range=8.67 (Long)"
    projectile_reliability: "needs_review; raw_mentions_slow_delay_spread_or_random"
    burst: "burst_candidate_from_damage_or_super_text"
    sustained_dps: "reload_signal_from_fandom=1.5 seconds (Normal)"
    objective_damage: "heist_candidate_from_plp_modes=False"
    mobility: "mobility_or_speed_tool_text_present; water_or_obstacle_interaction_text_present"
    survivability: "fandom_health=4000; self_or_team_sustain_text_present"
    engage: "engage_candidate_if_mobility_or_cc_text_activates"
    disengage: "disengage_candidate_if_mobility_slow_stun_or_knockback_text_activates"
    anti_aggro: "candidate_from_control_or_escape_text"
    anti_tank: "candidate_from_high_damage_percent_slow_or_continuous_damage_text"
    wall_break: "not_observed_in_selected_raw"
    throw_or_wall_bypass: "not_observed_in_selected_raw"
    area_control: "present_from_area_zone_trap_puddle_or_spawnable_text"
    scouting_or_vision: "present_from_reveal_vision_bush_text"
    team_support: "present_from_heal_shield_speed_pull_or_buff_text"
    spawnable_or_pet: "not_observed_in_selected_raw"
    crowd_control: "present_from_slow_stun_knockback_pull_silence_text"
    terrain_creation: "present_from_wall_or_puddle_obstacle_creation_text"
    terrain_destruction: "not_observed_in_selected_raw"

  build_switches:
    - build: "Disengage / Tremors / Shield, Damage"
      source: "[[sources/PLP-Maisie|PLP-Maisie]]"
      changes_capabilities:
        - "third_party_build_candidate; exact capability delta needs mechanism review"
      enables:
        - "mode_candidate:Brawl Ball"
        - "mode_candidate:Hot Zone"
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
    - map_feature_type: "water_crossing_or_obstacle_bypass"
      uses_feature_by: "raw text mentions water/obstacle interaction"
      objective_conversion: "must be tied to route, target access, or survival anchor"
      active_when: "bypass creates real objective access"
      fails_if: "bypass leads to short-range trap or no objective pressure"
      example_maps: []
      bp_use: "false_positive_filter_candidate"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "Brawl Ball_candidate_from_plp"
        - "ball_mode_contract_needs_push_clear_score_review"
      cannot_fulfill:
        - "not_inferred_from_source; requires map/matchup review"
      needs_teammate_support:
        - "cover failure modes and convert source candidate into map objective"
      false_positive: "PLP mode fit is a seed; do not treat as unconditional map fit"
    - mode: "Hot Zone"
      can_fulfill:
        - "Hot Zone_candidate_from_plp"
        - "area_control_candidate"
      cannot_fulfill:
        - "not_inferred_from_source; requires map/matchup review"
      needs_teammate_support:
        - "cover failure modes and convert source candidate into map objective"
      false_positive: "PLP mode fit is a seed; do not treat as unconditional map fit"

  failure_modes:
    - id: "reliability_into_mobility"
      active_when: "enemy has speed, dash, cover, or unpredictable pathing"
      exposed_by: "selected Fandom text markers"
      mitigation: "pick on constrained routes or pair with control"
      bp_use: "must_avoid_or_needs_support"
    - id: "source_signal_not_reviewed"
      active_when: "BP relies on PLP mode/matchup seed without mechanism validation"
      exposed_by: "third-party guide fields"
      mitigation: "convert seed into conditional matchup or map hook before bp_ready"
      bp_use: "do_not_mark_bp_ready"

  conditional_matchup_seeds:
    - target:
        - "Jae-Yong"
        - "Gigi"
        - "Piper"
        - "Darryl"
        - "Lily"
        - "Chuck"
        - "El Primo"
        - "Nani"
      direction: "subject_favored"
      source: "[[sources/PLP-Maisie|PLP-Maisie]]"
      mechanism: "pending; PLP seed must be explained through capability_vector before use"
      active_when: "requires map/mode/build validation"
      fails_when: "target has support, map disables mechanism, or source seed lacks local validation"
      bp_use: "conditional_matchup_seed_only"
    - target:
        - "Sandy"
        - "Rosa"
        - "Larry & Lawrie"
        - "Damian"
        - "Sirius"
        - "Nita"
        - "8-Bit"
        - "Bibi"
      direction: "target_favored"
      source: "[[sources/PLP-Maisie|PLP-Maisie]]"
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
