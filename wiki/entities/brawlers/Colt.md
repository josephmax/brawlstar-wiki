# Colt

## 基本信息

- 稀有度：Rare
- 定位：Damage Dealer
- 类型：远程枪手型英雄

## 攻击特征

- 主攻击是六连发直线射击
- 射程长，子弹速度快
- 单发伤害不高，但全中爆发很强

## 超级技能特征

- Super 是更长距离的十二连发穿透射击
- 可以摧毁障碍
- 适合拆墙、压线和封走位

## 适合场景

- 开阔地图
- 远距离对线
- 需要拆墙开路的局面
- 依赖走位和瞄准精度的对局

## 角色定位总结

Colt 是标准远程压制型英雄，强项在于连续输出、拆障碍和用射线型火力逼迫敌人走位。

## 关联页面

- [[sources/Fandom-Colt|Fandom 来源摘要: Colt]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-29"
    user_notes: "none"

  capability_vector:
    effective_range: long_to_very_long_with_Magnum_Special
    projectile_reliability: high_if_tracking_path_predictable; low_if_enemy_can_stutter_or_break_line
    burst: high_when_full_clip_tracks
    sustained_dps: high; very fast reload and repeated bullet streams
    objective_damage: high_in_Heist_when_safe_angle_exists
    mobility: medium_with_Slick_Boots
    survivability: low_medium; low health but speed helps dodge
    engage: low
    disengage: medium_with_speed_and_Speedloader_slow
    anti_aggro: conditional; Speedloader slow can confirm burst or peel
    anti_tank: high_if_distance_kept_and_bullets_track
    wall_break: high; Super and Silver Bullet can open terrain
    throw_or_wall_bypass: low_except_Silver_Bullet_wall_pierce
    area_control: medium; bullet streams deny lanes during unload
    scouting_or_vision: low
    team_support: terrain_transform_and_lane_damage
    terrain_destruction: high
    source_trace:
      - "[[sources/Fandom-Colt|Fandom-Colt]]"
      - "[[sources/PLP-Colt|PLP-Colt]]"

  build_switches:
    - build: "Speedloader / Slick Boots / Shield, Damage"
      source: "[[sources/PLP-Colt|PLP-Colt]]"
      changes_capabilities:
        - "Speedloader adds slow and no-ammo peel/confirm tool"
        - "Slick Boots improves dodging, chasing and retreating"
        - "Damage gear increases punish when Colt is pressured but alive"
      enables:
        - heist_safe_dps_lane
        - anti_aggro_burst_confirm
        - open_lane_tracking
      mitigates_failure_modes:
        - low_health_dive_pressure
        - aim_reliability_into_fast_targets
      poor_when:
        - "地图非做不可职责是开关键墙或破门，且没有其他队友能开图"
      bp_use: default_reviewed_build_for_damage_lane
    - build: "Silver Bullet / Magnum Special wall-or-range variant"
      source: "[[sources/Fandom-Colt|Fandom-Colt]]"
      changes_capabilities:
        - "Silver Bullet gives precise wall pierce and obstacle break"
        - "Magnum Special extends main attack range and bullet speed"
      enables:
        - selective_wall_break
        - goal_wall_opening
        - longer_marksman_duel
      mitigates_failure_modes:
        - blocked_by_cover
        - insufficient_goal_or_safe_angle
      poor_when:
        - "开墙会暴露己方低血后排，或敌方更擅长开阔对枪"
      bp_use: terrain_state_plan_requirement

  map_feature_hooks:
    - map_feature_type: "long_sightline"
      uses_feature_by: "long straight bullet stream tracks lane movement and converts hits into high DPS"
      route_or_position: "straight side lane or safe lane where targets must move parallel to Colt"
      objective_conversion: "Heist safe damage, Gem side pressure, Brawl Ball lane clear"
      active_when: "lane is open enough for tracking and enemy lacks immediate dive"
      fails_if: "target breaks line behind walls, stutter-steps unpredictably, or Colt must shoot through clutter"
      example_maps:
        - Bridge Too Far
        - Kaboom Canyon
        - Safe(r) Zone
        - Dry Season
      bp_use: required_capabilities.sustained_lane_dps
    - map_feature_type: "wall_break_transform"
      uses_feature_by: "Super or Silver Bullet opens goal walls, safe angles or thrower cover"
      route_or_position: "goal mouth, safe-facing barrier, or thin wall protecting enemy pocket"
      objective_conversion: "creates scoring window, Heist firing lane, or anti-thrower angle"
      active_when: "our comp benefits from the opened lane and can immediately use it"
      fails_if: "overbreaking gives enemy snipers/tanks easier access than our team"
      example_maps:
        - Sneaky Fields
        - Triple Dribble
        - Pit Stop
        - Shooting Star
      bp_use: terrain_state_plan.transform
    - map_feature_type: "anti_aggro_slow_window"
      uses_feature_by: "Speedloader slows close targets and lets Colt land bullet streams"
      route_or_position: "narrow side entry or Brawl Ball defense lane"
      objective_conversion: "stop scorer, protect safe lane, or convert diver into kill"
      active_when: "enemy entry is linear and Colt has ammo/team follow-up"
      fails_if: "enemy comes from multiple angles or uses hard CC before Colt fires"
      example_maps:
        - Center Stage
        - Hot Potato
        - Gem Fort
      bp_use: candidate_eval.anti_aggro_peel

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - sustained_safe_dps
        - wallbreak_to_create_safe_angle
        - lane_duel_into_safe_pressure
      cannot_fulfill:
        - body_blocking_enemy_entry
        - throw_arc_safe_damage_without_line
      needs_teammate_support:
        - anti_dive
        - lane_control_after_wall_open
      false_positive: "High DPS is irrelevant if walls or route geometry prevent safe access"
    - mode: "Brawl Ball"
      can_fulfill:
        - goal_wall_break
        - lane_clear
        - anti_scorer_slow_if_Speedloader_available
      cannot_fulfill:
        - primary_ball_carrier
        - hard_knockback_scorer
      needs_teammate_support:
        - scorer_or_control_to_use_open_goal
        - protection_against_dive
      false_positive: "Opening goal walls can also help enemy shooters if our team cannot score quickly"
    - mode: "Gem Grab"
      can_fulfill:
        - side_lane_damage_pressure
        - wallbreak_to_expose_mid_pocket
        - punish_slow_gem_carrier
      cannot_fulfill:
        - safe_gem_carrier
        - bush_vision_tax
      needs_teammate_support:
        - mid_control
        - scouting_or_trap_control
      false_positive: "Colt can win side lane yet still fail if mid has no carrier safety"

  failure_modes:
    - id: "tracking_fails_into_mobility_or_cover"
      active_when: "enemy stutter-steps, dashes, or repeatedly breaks line during Colt's unload"
      exposed_by: "[[sources/Fandom-Colt|Fandom-Colt]] attack requires tracking six bullets"
      mitigation: "pick straight lanes, pair with slow/stun/pull, or use Speedloader to confirm"
      bp_use: "must_avoid_or_needs_support"
    - id: "low_health_dive_pressure"
      active_when: "assassin or tank reaches Colt before he can track a full burst"
      exposed_by: "[[sources/Fandom-Colt|Fandom-Colt]] low health and close-range warnings"
      mitigation: "Slick Boots spacing, Speedloader slow, teammate peel"
      bp_use: "false_positive_filter"
    - id: "terrain_transform_backfires"
      active_when: "opened lane improves enemy range or engage more than ours"
      exposed_by: "[[sources/Fandom-Colt|Fandom-Colt]] Super and Silver Bullet destroy cover"
      mitigation: "define exact wall, follow-up scorer/safe angle, and enemy range response before pick"
      bp_use: "terrain_state_plan_check"
    - id: "super_cancel_or_reload_lockout"
      active_when: "Colt uses Super into knockback, pull, stun, or pressure that cancels the channel"
      exposed_by: "[[sources/Fandom-Colt|Fandom-Colt]] Super cannot attack/reload and is cancelable"
      mitigation: "use Super from protected angle or after enemy CC is unavailable"
      bp_use: "candidate_eval.execution_risk"

  conditional_matchup_seeds:
    - target:
        - "Sprout"
        - "Tick"
        - "Ziggy"
      direction: "subject_favored"
      source: "[[sources/PLP-Colt|PLP-Colt]]"
      mechanism: "wallbreak plus long bullet lanes can remove pockets and punish low-health control picks"
      active_when: "key wall is breakable and Colt can shoot after opening without being dived"
      fails_when: "thrower has deeper pocket, Colt lacks wallbreak build, or enemy punishes the opened lane"
      bp_use: "response_pick_candidate_against_cover_control"
    - target:
        - "El Primo"
        - "Brock"
        - "Piper"
        - "Mandy"
      direction: "subject_favored"
      source: "[[sources/PLP-Colt|PLP-Colt]]"
      mechanism: "high DPS and speed punish linear or aim-locked targets when Colt has a clean tracking lane"
      active_when: "open side lane, predictable movement, and no immediate flank threat"
      fails_when: "target outranges from safer angle or closes through cover before full burst lands"
      bp_use: "lane_duel_candidate"
    - target:
        - "Angelo"
        - "Moe"
        - "Bibi"
        - "Stu"
        - "Chester"
      direction: "target_favored"
      source: "[[sources/PLP-Colt|PLP-Colt]]"
      mechanism: "mobility, burst, or superior angle pressure interrupts Colt's tracking window"
      active_when: "map has side cover or water/grass routes and Colt lacks peel"
      fails_when: "lane is fully open and Colt can pre-aim with slow or team control"
      bp_use: "avoid_first_pick_or_require_peel"

  slot_notes:
    slot_1: "只在 Heist 长线或需要早抢开墙/DPS 的地图先手；必须预留 anti-dive。"
    slot_2_3: "可回答敌方墙体口袋或前排计划，也可和控制队友组成命中保障。"
    slot_4_5: "适合修复 safe DPS、破门或开墙缺口；要检查开墙后是否喂给敌方 6 位。"
    slot_6: "当敌方缺机动和侧路威胁时，Colt 可作为惩罚性 DPS 或破图收口。"
```
