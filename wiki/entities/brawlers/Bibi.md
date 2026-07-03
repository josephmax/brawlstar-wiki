# Bibi

## 基本信息

- 稀有度：Epic
- 定位：Tank
- 来源：近战压线与击退控制兼具的前排英雄

## 攻击特征

- 主攻击是短距离宽弧挥击
- 攻击前摇短，但需要贴近敌人
- `Home Run` 条充满后，下一次攻击会击退敌人
- 很适合持续逼退和卡位

## 超级技能特征

- Super 会发射可穿透、可弹墙、可重复命中的泡泡
- 在墙多的地图里，Super 很容易打出额外收益
- Hypercharge 会让 Super 分裂成两发，强化区域压制

## 适合场景

- Brawl Ball
- 近点争夺和控线
- 需要不断逼退对手的地图
- 需要边打边走的前排玩法

## 角色定位总结

Bibi 是一个靠挥棒、击退和弹墙泡泡来持续施压的控线型坦克，不只是硬冲，更强调路线控制。

## 关联页面

- [[sources/Fandom-Bibi|Fandom 来源摘要: Bibi]]
- [[sources/PLP-Bibi|Power League Prodigy 来源摘要: Bibi]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "short; 3.67-tile wide arc needs grass, wall pressure, ball route, or forced objective contact"
    projectile_reliability: "medium; main attack has a 0.6s wind-up, while Super travels long, pierces, and can bounce for repeat hits"
    burst: "medium_high_at_contact; fast reload plus Home Run knockback makes close trades swingy"
    sustained_dps: "medium_high_if_target_stays_close; 0.8s reload is strong, but range and wind-up limit uptime"
    objective_damage: "conditional_heist; bat damage and bouncing Super matter only after Bibi reaches safe or wall angle"
    mobility: "medium_high_with_Home_Run; Home Run star power gives speed while the bar is charged"
    survivability: "medium_high; 5000 health, Vitamin Booster healing, Shield gear, and optional Batting Stance help approach"
    engage: "high_on_grass_or_ball_lane; speed and knockback let Bibi force defenders backward"
    disengage: "medium; knockback and Vitamin Booster buy retreat time but do not solve open-lane kiting"
    anti_aggro: "high_in_closed_lane; Home Run knockback can interrupt tanks, dashes, or scoring attempts"
    anti_tank: "medium; knockback disrupts melee tanks, but anti-tank burst and silence still punish her"
    wall_break: low
    throw_or_wall_bypass: "low_for_body_medium_for_super_geometry; Bibi cannot cross walls, but bubble bounces exploit wall corridors"
    area_control: "medium; knockback and bounce paths force enemies off goals, safe angles, zones, or gem routes"
    scouting_or_vision: low
    team_support: "medium_indirect; displacement opens a scoring or safe-entry window rather than healing allies"
    spawnable_or_pet: low
    crowd_control: "high; Home Run knockback is the core BP signal and Extra Sticky adds a slow variant"
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Bibi|Fandom-Bibi]]"
      - "[[sources/PLP-Bibi|PLP-Bibi]]"

  build_switches:
    - build: "Vitamin Booster / Home Run / Shield, Damage"
      source: "[[sources/PLP-Bibi|PLP-Bibi]]"
      changes_capabilities:
        - "Vitamin Booster gives 4 seconds of self-heal for surviving the first close-range entry"
        - "Home Run star power adds movement speed while the bar is charged, improving Brawl Ball and side-lane approach"
        - "Shield and Damage gears support the short-range contact plan once Bibi has a route"
      enables:
        - ball_push_and_goalkeeping
        - grass_lane_entry
        - short_safe_burst_after_access
      mitigates_failure_modes:
        - approach_chip_before_contact
        - closed_lane_defender_burst
      best_when: "map has side grass, goal lanes, safe-facing walls, or bounce corridors where speed and knockback convert"
      poor_when:
        - "open long-range lanes let snipers chip Bibi before Vitamin Booster matters"
        - "knockback pushes the target out of teammate damage or away from the objective"
      bp_use: default_reviewed_build_for_brawl_ball_and_heist_entry
    - build: "Extra Sticky / Batting Stance variants"
      source: "[[sources/Fandom-Bibi|Fandom-Bibi]]"
      changes_capabilities:
        - "Extra Sticky turns Super into a slow zone, useful when the team needs chase confirmation more than self-heal"
        - "Batting Stance gives a shield while Home Run is charged, improving pre-contact survival over speed"
      enables:
        - chase_confirmation
        - pre_entry_tankiness
      mitigates_failure_modes:
        - open_lane_chip
      poor_when:
        - "Brawl Ball route or side-lane tempo requires Home Run speed to arrive on time"
      bp_use: situational_variant_for_slow_or_extra_survival

  map_feature_hooks:
    - map_feature_type: "brawl_ball_home_run_goalkeeping_and_push"
      uses_feature_by: "Home Run knockback, speed, and wide arc let Bibi clear ball routes, steal possession, or escort a push"
      route_or_position: "midfield grass, side bush approach, or goal-front pocket where one knockback changes possession"
      objective_conversion: "stop a scorer, push a defender off the goal, or create a brief scoring window"
      active_when: "team can follow the displacement with ball control, wallbreak, or a finisher"
      fails_if: "closed goal geometry remains unsolved, enemy has layered knockback/silence, or Bibi's knockback saves the defender"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
        - Pinball Dreams
      bp_use: slot_task.ball_lane_displacement
    - map_feature_type: "wall_bounce_spitball_safe_or_lane"
      uses_feature_by: "Bibi's bubble pierces, bounces from walls, and can hit the same target repeatedly when geometry holds it near the objective"
      route_or_position: "safe-facing wall, goal corridor, or side pocket where the bubble path stays near enemies or safe"
      objective_conversion: "add Heist safe chip, clear a defender from a wall lane, or force enemies out of goal-side cover"
      active_when: "walls remain intact and Bibi can charge Super without being outranged before contact"
      fails_if: "wallbreak removes the bounce path, the fight moves into open field, or enemy outranges the corridor"
      example_maps:
        - Pit Stop
        - Hot Potato
        - Safe(r) Zone
        - Pinball Dreams
      bp_use: map_factor_fit.bounce_wall_objective_angle
    - map_feature_type: "grass_speed_close_range_flank"
      uses_feature_by: "Home Run speed and Vitamin Booster let Bibi cross bush lanes into short-range pressure"
      route_or_position: "side grass lane, central bush mass, or safe-side bush entry"
      objective_conversion: "force back a lane defender, steal safe access, or threaten gem/ball carrier retreat"
      active_when: "grass remains and enemy lacks cheap reveal, slow, or anti-tank burst"
      fails_if: "grass is cleared, open sightlines cover the approach, or Bibi is forced to swing before entering range"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Hot Potato
        - Hard Rock Mine
      bp_use: map_bp_factors.grass_entry_and_short_range_route

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - goalkeeper_knockback
        - side_lane_push
        - defender_displacement_for_score
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - long_range_backline_control
      needs_teammate_support:
        - goal opener or trick-shot finisher
        - follow-up damage after knockback
      false_positive: "Bibi can make a scoring window, but a bad knockback can also push defenders to safety."
    - mode: "Heist"
      can_fulfill:
        - side_lane_entry
        - safe_burst_after_contact
        - bounce_super_chip_from_wall_geometry
      cannot_fulfill:
        - remote_safe_damage
        - open_long_lane_safe_race
      needs_teammate_support:
        - lane control or wall pressure that lets Bibi reach safe
        - ranged DPS if the map becomes open
      false_positive: "Bibi's Heist value is access-gated; do not compare her to stable ranged safe DPS."

  failure_modes:
    - id: "windup_and_short_range_kiting"
      active_when: "Bibi must cross an open lane or swing into mobile targets that can step out during her attack delay"
      exposed_by: "[[sources/Fandom-Bibi|Fandom-Bibi]] attack wind-up and short range"
      mitigation: "pick on grass, wall, or goal routes and pair with slow, speed, or lane pressure"
      bp_use: map_route_filter
    - id: "knockback_saves_target"
      active_when: "Home Run pushes a defender out of teammate fire, away from Bibi's second swing, or into a safer objective position"
      exposed_by: "[[sources/Fandom-Bibi|Fandom-Bibi]] strategy note that knockback can help enemies escape"
      mitigation: "time Home Run for objective displacement, wall pin, or ball clear rather than raw damage"
      bp_use: execution_and_candidate_eval_warning
    - id: "bounce_value_lost_after_wallbreak"
      active_when: "enemy opens the wall corridor that made Spitball or close approach valuable"
      exposed_by: "bubble bounce mechanics and Ranked map pages with wallbreak-sensitive lanes"
      mitigation: "preserve friendly walls or pivot Bibi into grass/ball pressure instead of bounce angle"
      bp_use: terrain_state_dependency
    - id: "burst_or_silence_outpaces_vitamin"
      active_when: "enemy anti-tank burst, silence, or sustained mid-range damage kills Bibi before heal and knockback convert"
      exposed_by: "[[sources/PLP-Bibi|PLP-Bibi]] target-favored list"
      mitigation: "avoid early pick into those answers or require teammate peel and route control"
      bp_use: must_answer_counter_chain

  conditional_matchup_seeds:
    - target:
        - "Jae-Yong"
        - "Sprout"
        - "Squeak"
        - "Poco"
        - "Mr. P"
        - "Ziggy"
        - "Tick"
        - "Leon"
      direction: "subject_favored"
      source: "[[sources/PLP-Bibi|PLP-Bibi]]"
      mechanism: "Speed entry, Home Run knockback, and bubble bounce punish low-health, utility, wall-control, or close-range targets once Bibi chooses first contact."
      active_when: "walls, grass, ball lane, safe route, or carrier pressure force the target to remain near Bibi's approach"
      fails_when: "target keeps open spacing, has deeper cover or peel, baits knockback, or fights before Bibi reaches range"
      bp_use: response_pick_candidate_against_wall_control
    - target:
        - "Otis"
        - "Clancy"
        - "Chester"
        - "Colette"
        - "Frank"
      direction: "target_favored"
      source: "[[sources/PLP-Bibi|PLP-Bibi]]"
      mechanism: "Silence, anti-tank burst, percent damage, or heavy close-range punishment can stop Bibi before Home Run and Vitamin Booster convert."
      active_when: "Bibi must enter their preferred range or defend a closed objective route repeatedly"
      fails_when: "Bibi has wall pin, teammate burst, or a route that lets her force them away from the objective first"
      bp_use: avoid_first_pick_or_require_route_control
    - target:
        - "Lola"
        - "Damian"
        - "Lumi"
      direction: "target_favored"
      source: "[[sources/PLP-Bibi|PLP-Bibi]]"
      mechanism: "Stable mid-range damage or control can chip Bibi down during the approach and deny her short-range timing."
      active_when: "map is semi-open, grass is cleared, or their team protects the lane Bibi must cross"
      fails_when: "Bibi enters through grass/walls with speed and her team collapses before they reset spacing"
      bp_use: map_openness_and_peel_warning

  slot_notes:
    slot_1: "unsafe except on very Bibi-shaped Brawl Ball or Heist maps; her counter chain is easy to prepare."
    slot_2_3: "works when the team wants early ball pressure and can still reserve answers to anti-tank or silence."
    slot_4_5: "best as a route repair pick after seeing enemy low-control lanes or a Heist/Brawl Ball access gap."
    slot_6: "strong punish into drafts without knockback, silence, reliable reveal, or long-range lane control."
```
