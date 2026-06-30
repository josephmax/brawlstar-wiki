# Jessie

## 基本信息

- 稀有度：Super Rare
- 定位：Controller
- 来源：早期解锁英雄之一

## 攻击特征

- 主攻击是长距离弹射能量球
- 最多可命中 3 个敌人
- 在敌人站位密集或躲墙后时更容易打出价值

## 超级技能特征

- Super 会部署名为 `Scrappy` 的炮台
- 炮台能自动攻击、占位并吸引火力
- 炮台让 Jessie 从“单点输出”变成“输出 + 场面干扰”双角色

## 适合场景

- 控图和守点
- 地图中有可利用墙体或固定据点的模式
- 需要持续施压、拖慢对手节奏的对局

## 角色定位总结

Jessie 是中距离控制和召唤物压制的代表英雄。和 `Shelly` 的贴脸爆发、`Colt` 的直线压制相比，她更依赖弹射、站位和炮台带来的持续场面优势。

## 关联页面

- [[sources/Fandom-Jessie|Fandom 来源摘要: Jessie]]

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
    effective_range: "very_long_or_long; fandom_attack_range=9 (Long)"
    projectile_reliability: "needs_review; raw_mentions_slow_delay_spread_or_random"
    burst: "unknown_pending_damage_review"
    sustained_dps: "reload_signal_from_fandom=1.8 seconds (Normal)"
    objective_damage: "heist_candidate_from_plp_modes=False"
    mobility: "mobility_or_speed_tool_text_present"
    survivability: "fandom_health=3300; low_health_failure_check; self_or_team_sustain_text_present"
    engage: "engage_candidate_if_mobility_or_cc_text_activates"
    disengage: "disengage_candidate_if_mobility_slow_stun_or_knockback_text_activates"
    anti_aggro: "candidate_from_control_or_escape_text"
    anti_tank: "candidate_from_high_damage_percent_slow_or_continuous_damage_text"
    wall_break: "not_observed_in_selected_raw"
    throw_or_wall_bypass: "present_from_artillery_or_over_obstacles"
    area_control: "present_from_area_zone_trap_puddle_or_spawnable_text"
    scouting_or_vision: "present_from_reveal_vision_bush_text"
    team_support: "present_from_heal_shield_speed_pull_or_buff_text"
    spawnable_or_pet: "present_from_spawn_turret_pet_minion_text"
    crowd_control: "present_from_slow_stun_knockback_pull_silence_text"
    terrain_creation: "present_from_wall_or_puddle_obstacle_creation_text"
    terrain_destruction: "not_observed_in_selected_raw"

  build_switches:
    - build: "Spark Plug / Energize / Shield, Damage"
      source: "[[sources/PLP-Jessie|PLP-Jessie]]"
      changes_capabilities:
        - "third_party_build_candidate; exact capability delta needs mechanism review"
      enables:
        - "mode_candidate:Gem Grab"
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
    - map_feature_type: "thrower_pocket"
      uses_feature_by: "over-wall or artillery signal from Fandom raw"
      objective_conversion: "can contest protected zones if pocket remains intact"
      active_when: "walls survive and enemy lacks cheap wall break or dive"
      fails_if: "terrain is opened or dive path reaches the pocket"
      example_maps: []
      bp_use: "map_factor_fit_candidate"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "Gem Grab_candidate_from_plp"
        - "area_control_candidate"
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
    - id: "pocket_removed_or_dived"
      active_when: "enemy opens terrain or reaches thrower pocket"
      exposed_by: "artillery/over-wall capability candidate"
      mitigation: "ban cheap wall break, draft peel, or choose stable pocket map"
      bp_use: "map_factor_false_positive_check"

  conditional_matchup_seeds:
    - target:
        - "Jae-Yong"
        - "Poco"
        - "Nani"
        - "Spike"
        - "Pam"
        - "Lola"
        - "Sprout"
        - "Glowy"
      direction: "subject_favored"
      source: "[[sources/PLP-Jessie|PLP-Jessie]]"
      mechanism: "pending; PLP seed must be explained through capability_vector before use"
      active_when: "requires map/mode/build validation"
      fails_when: "target has support, map disables mechanism, or source seed lacks local validation"
      bp_use: "conditional_matchup_seed_only"
    - target:
        - "Alli"
        - "Buzz"
        - "Darryl"
        - "Edgar"
        - "Fang"
        - "Gigi"
        - "Kaze"
        - "Kenji"
      direction: "target_favored"
      source: "[[sources/PLP-Jessie|PLP-Jessie]]"
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
