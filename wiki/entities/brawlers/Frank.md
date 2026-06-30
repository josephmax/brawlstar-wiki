# Frank

## 基本信息

- 稀有度：Epic
- 定位：Tank
- 来源：高血量前排，擅长开团和控场

## 攻击特征

- 主攻击是带明显前摇的震荡波
- 攻击会穿透敌人
- 生命越低，出手越快
- 很适合用来压缩对手走位空间

## 超级技能特征

- Super 是更大范围、更长距离的震荡波
- 可以摧毁障碍物
- 会眩晕命中的敌人
- 适合先手开团和打断对方节奏

## 适合场景

- 狭窄地图
- 需要强开团和控图的模式
- 需要拆墙、封路、逼退的局面
- 目标明确的正面团战

## 角色定位总结

Frank 是一个典型的重型前排，核心不是灵活，而是用高血量和大范围控制把战斗强行拉进自己节奏。

## 关联页面

- [[sources/Fandom-Frank|Fandom 来源摘要: Frank]]

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
    effective_range: "mid; fandom_attack_range=6 (Normal)"
    projectile_reliability: "needs_review; raw_mentions_slow_delay_spread_or_random"
    burst: "burst_candidate_from_damage_or_super_text"
    sustained_dps: "reload_signal_from_fandom=0.8 seconds (Very Fast)"
    objective_damage: "heist_candidate_from_plp_modes=False"
    mobility: "mobility_or_speed_tool_text_present"
    survivability: "fandom_health=6800; high_health_body_presence_candidate; self_or_team_sustain_text_present"
    engage: "engage_candidate_if_mobility_or_cc_text_activates"
    disengage: "disengage_candidate_if_mobility_slow_stun_or_knockback_text_activates"
    anti_aggro: "candidate_from_control_or_escape_text"
    anti_tank: "candidate_from_high_damage_percent_slow_or_continuous_damage_text"
    wall_break: "present_from_fandom_text"
    throw_or_wall_bypass: "present_from_artillery_or_over_obstacles"
    area_control: "present_from_area_zone_trap_puddle_or_spawnable_text"
    scouting_or_vision: "present_from_reveal_vision_bush_text"
    team_support: "present_from_heal_shield_speed_pull_or_buff_text"
    spawnable_or_pet: "present_from_spawn_turret_pet_minion_text"
    crowd_control: "present_from_slow_stun_knockback_pull_silence_text"
    terrain_creation: "present_from_wall_or_puddle_obstacle_creation_text"
    terrain_destruction: "present_from_fandom_text"

  build_switches:
    - build: "Irresistible Attraction / Power Grab / Health, Damage"
      source: "[[sources/PLP-Frank|PLP-Frank]]"
      changes_capabilities:
        - "third_party_build_candidate; exact capability delta needs mechanism review"
      enables:
        - "mode_candidate:Gem Grab"
        - "mode_candidate:Brawl Ball"
        - "mode_candidate:Hot Zone"
      mitigates_failure_modes:
        - "unknown_until_reviewed_against_failure_modes"
      best_when: "PLP mode/matchup seed aligns with current map_bp_factors"
      poor_when: "build is copied without checking map route, enemy answers, or slot duty"
      bp_use: "build_candidate_not_final_recommendation"

  map_feature_hooks:
    - map_feature_type: "wall_break_transform"
      uses_feature_by: "terrain destruction text present in Fandom raw"
      objective_conversion: "can create or deny lanes only if our comp benefits after transform"
      active_when: "key wall blocks objective route or protects enemy pocket"
      fails_if: "opening wall benefits enemy range/engage more than ours"
      example_maps: []
      bp_use: "terrain_state_plan_candidate"
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
    - id: "pocket_removed_or_dived"
      active_when: "enemy opens terrain or reaches thrower pocket"
      exposed_by: "artillery/over-wall capability candidate"
      mitigation: "ban cheap wall break, draft peel, or choose stable pocket map"
      bp_use: "map_factor_false_positive_check"
    - id: "terrain_transform_backfires"
      active_when: "opened lane improves enemy range or engage more than ours"
      exposed_by: "terrain destruction candidate"
      mitigation: "define exact wall and follow-up before pick"
      bp_use: "terrain_state_plan_check"

  conditional_matchup_seeds:
    - target:
        - "Squeak"
        - "Grom"
        - "Sprout"
        - "Gene"
        - "Penny"
        - "Charlie"
        - "Cordelius"
        - "Ash"
      direction: "subject_favored"
      source: "[[sources/PLP-Frank|PLP-Frank]]"
      mechanism: "pending; PLP seed must be explained through capability_vector before use"
      active_when: "requires map/mode/build validation"
      fails_when: "target has support, map disables mechanism, or source seed lacks local validation"
      bp_use: "conditional_matchup_seed_only"
    - target:
        - "Colette"
        - "Emz"
        - "Lou"
        - "Shelly"
        - "El Primo"
        - "Maisie"
        - "Surge"
        - "Fang"
      direction: "target_favored"
      source: "[[sources/PLP-Frank|PLP-Frank]]"
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
