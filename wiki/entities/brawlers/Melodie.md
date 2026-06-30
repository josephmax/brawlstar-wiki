# Melodie

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：音符叠层刺客

## 攻击特征

- 主攻击是长距离 monster note
- 命中后会生成围绕自身旋转的音符
- 音符叠层后，本体和贴身输出都会更有威胁

## 超级技能特征

- Super `Catchy Chorus` 提供 3 段可分次使用的冲刺
- 可以用来连续切入、追击或调整站位
- 更像“分段位移工具”而不是单次爆发

## 适合场景

- 需要绕后收割的地图
- 可以先起手再切入的对局
- 对手站位比较分散、容易被逐个击破的模式

## 角色定位总结

Melodie 是靠音符叠层和多段冲刺慢慢把节奏滚起来的机动刺客，强点在持续积累后的突然切入。

## 关联页面

- [[sources/Fandom-Melodie|Fandom 来源摘要: Melodie]]

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
    effective_range: "long_mid; fandom_attack_range=8 (Long)<br>2.17 (monster notes)<br>3.47 (monster notes; with Perfect Pitch)"
    projectile_reliability: "needs_review; raw_mentions_slow_delay_spread_or_random"
    burst: "burst_candidate_from_damage_or_super_text"
    sustained_dps: "reload_signal_from_fandom=1.5 seconds (Normal)"
    objective_damage: "heist_candidate_from_plp_modes=True"
    mobility: "mobility_or_speed_tool_text_present; water_or_obstacle_interaction_text_present"
    survivability: "fandom_health=3800; self_or_team_sustain_text_present"
    engage: "engage_candidate_if_mobility_or_cc_text_activates"
    disengage: "disengage_candidate_if_mobility_slow_stun_or_knockback_text_activates"
    anti_aggro: "candidate_from_control_or_escape_text"
    anti_tank: "unknown_pending_matchup_review"
    wall_break: "not_observed_in_selected_raw"
    throw_or_wall_bypass: "not_observed_in_selected_raw"
    area_control: "present_from_area_zone_trap_puddle_or_spawnable_text"
    scouting_or_vision: "present_from_reveal_vision_bush_text"
    team_support: "present_from_heal_shield_speed_pull_or_buff_text"
    spawnable_or_pet: "present_from_spawn_turret_pet_minion_text"
    crowd_control: "not_observed_in_selected_raw"
    terrain_creation: "present_from_wall_or_puddle_obstacle_creation_text"
    terrain_destruction: "not_observed_in_selected_raw"

  build_switches:
    - build: "Interlude / Fast Beats / Shield, Damage"
      source: "[[sources/PLP-Melodie|PLP-Melodie]]"
      changes_capabilities:
        - "third_party_build_candidate; exact capability delta needs mechanism review"
      enables:
        - "mode_candidate:Brawl Ball"
        - "mode_candidate:Heist"
        - "mode_candidate:Bounty"
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
    - mode: "Heist"
      can_fulfill:
        - "Heist_candidate_from_plp"
        - "objective_damage_or_lane_pressure_needs_quant_review"
      cannot_fulfill:
        - "not_inferred_from_source; requires map/matchup review"
      needs_teammate_support:
        - "cover failure modes and convert source candidate into map objective"
      false_positive: "PLP mode fit is a seed; do not treat as unconditional map fit"
    - mode: "Bounty"
      can_fulfill:
        - "Bounty_candidate_from_plp"
        - "survival_range_pressure_candidate"
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
        - "Bolt"
        - "Sprout"
        - "Ziggy"
        - "Brock"
        - "Mandy"
        - "Spike"
        - "Dynamike"
        - "Piper"
      direction: "subject_favored"
      source: "[[sources/PLP-Melodie|PLP-Melodie]]"
      mechanism: "pending; PLP seed must be explained through capability_vector before use"
      active_when: "requires map/mode/build validation"
      fails_when: "target has support, map disables mechanism, or source seed lacks local validation"
      bp_use: "conditional_matchup_seed_only"
    - target:
        - "Sandy"
        - "Finx"
        - "Lola"
        - "Bibi"
        - "R-T"
        - "Pearl"
        - "Tara"
        - "Gale"
      direction: "target_favored"
      source: "[[sources/PLP-Melodie|PLP-Melodie]]"
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
