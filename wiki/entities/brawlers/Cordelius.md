# Cordelius

## 基本信息

- 稀有度：Legendary
- 定位：Assassin
- 类型：Shadow Realm 切入型英雄

## 攻击特征

- 普通攻击会发射两枚中距离蘑菇
- 贴近敌人时更容易打出完整伤害
- 属于中距离压迫和近身切入兼具的类型

## 超级技能特征

- Super 会把 Cordelius 和目标一起送进 Shadow Realm
- Shadow Realm 中双方都不能使用或充能 Super、Gadget 和 Hypercharge
- 这会强行把战斗切成一对一或局部隔离对局

## 适合场景

- 需要拆分敌方阵型的对局
- 想强行把关键目标拉出去单挑的局面
- 草丛、墙体和狭窄通道较多的地图

## 角色定位总结

Cordelius 是机制感很强的传奇刺客，和一般刺客不同，他不是单纯靠位移收割，而是通过 Shadow Realm 直接改写战斗规则。

## 与其他英雄的区别

- 不同于 `Mortis`：Cordelius 更偏技能隔离，Mortis 更偏连续位移收割
- 不同于 `Leon`：Cordelius 更像稳定单挑工具，Leon 更依赖隐身信息差
- 不同于 `Bull`：Bull 是正面冲阵，Cordelius 是规则改写

## 关联页面

- [[sources/Fandom-Cordelius|Fandom 来源摘要: Cordelius]]
- [[sources/PLP-Cordelius|Power League Prodigy 来源摘要: Cordelius]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "mid_short; 5.33-tile main attack and 9-tile wall-passing Super make him a route/control assassin rather than a pure long-lane pick"
    projectile_reliability: "medium_high_on_constrained_routes; two fast mushrooms reward close or choke contact, while open lanes let agile targets dodge the narrow shots"
    burst: "high_when_both_mushrooms_or_Poison_Mushroom_connect; Comboshrooms raises the second projectile and Shadow Realm reload speed improves duel tempo"
    sustained_dps: "high_in_1v1_window; very fast reload becomes faster in Shadow Realm, but range and health limit front-to-back fighting"
    objective_damage: "low_medium; PLP lists Heist, but value is isolating defenders or using Shadow Realm travel toward safe/zone, not primary safe DPS"
    mobility: "high_with_Replanting_and_Shadow_Realm; Replanting jumps 3 tiles and can cross walls/water, while Super grants speed in the realm"
    survivability: "medium_low_outside_realm; 3500 health is fragile, but Replanting, Shadow Realm escape, and Mushroom Kingdom healing can create reset windows"
    engage: "very_high_as_single_target_isolation; Super removes one target from the normal fight and blocks Super/Gadget/Hypercharge usage"
    disengage: "high_with_realm_or_jump; Super can escape, Replanting crosses terrain, and Mushroom Kingdom can heal during the realm"
    anti_aggro: "very_high_if_resource_ready; Poison Mushroom and Super stop attack/Super/Gadget windows from divers, scorers, and tanks"
    anti_tank: "high_as_response_pick; forced 1v1, silence, speed, and Comboshrooms punish tanks that must enter Cordelius range"
    wall_break: low
    throw_or_wall_bypass: "medium_high; Super projectile passes through walls and Replanting crosses terrain, but main attack still needs line"
    area_control: "medium; Trait rewards camping near contested chokes and Super can force enemies away from key objective space"
    scouting_or_vision: "medium; Trait charges from invisible or bush-camping enemies and Shadow Realm removes bush hiding, but it is proximity information rather than full reveal"
    team_support: "high_indirect; isolating a defender, carrier, or scorer creates teammate objective windows"
    spawnable_or_pet: low
    crowd_control: "very_high_single_target; Shadow Realm blocks Supers, Gadgets, Hypercharges, and charging for 8 seconds, while Poison Mushroom prevents actions for 1 second"
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Cordelius|Fandom-Cordelius]]"
      - "[[sources/PLP-Cordelius|PLP-Cordelius]]"

  build_switches:
    - build: "Replanting / Comboshrooms / Shield, Damage"
      source: "[[sources/PLP-Cordelius|PLP-Cordelius]]"
      changes_capabilities:
        - "Replanting adds terrain-crossing engage, escape, and route-gate bypass"
        - "Comboshrooms improves duel burst and Super charge if both mushrooms hit the same target"
        - "Shield raises the margin for low-health entries, while Damage improves kill confirmation inside Shadow Realm"
      enables:
        - shadow_realm_pickoff
        - terrain_jump_entry
        - single_target_anti_aggro
        - carrier_or_scorer_isolation
      mitigates_failure_modes:
        - middling_range_into_open_lane
        - low_health_entry
        - no_route_to_key_target
      best_when: "map has walls, grass, water, or choke routes that let Cordelius reach a high-value target and convert the isolation"
      poor_when:
        - "enemy composition outranges him and does not need to walk through his Trait radius"
        - "team cannot hold the normal fight while Cordelius leaves with one enemy"
      bp_use: default_reviewed_build_for_route_based_isolation
    - build: "Poison Mushroom / Mushroom Kingdom variant"
      source: "[[sources/Fandom-Cordelius|Fandom-Cordelius]] / [[sources/PLP-Cordelius|PLP-Cordelius]]"
      changes_capabilities:
        - "Poison Mushroom preloads a 1-second action lock that can still be used inside Shadow Realm"
        - "Mushroom Kingdom adds healing or damage pickups inside the realm, improving emergency reset and duel endurance"
      enables:
        - aggro_interrupt
        - realm_duel_sustain
        - brawl_ball_ball_denial
      mitigates_failure_modes:
        - target_preloads_gadget_or_burst
        - low_health_after_realm_exit
      best_when: "enemy relies on one close engage, scorer, or tank body that must act during the duel"
      poor_when:
        - "enemy wins by long-range poke or thrower pockets outside Cordelius reach"
      bp_use: situational_variant_into_aggro_or_high_value_carrier

  map_feature_hooks:
    - map_feature_type: "carrier_or_scorer_shadow_realm_isolation"
      uses_feature_by: "Super removes one enemy from the normal map, blocks Supers/Gadgets/Hypercharges, and lets Cordelius predict carrier or defender location after realm entry"
      route_or_position: "gem mine entrance, side grass countdown route, midfield ball lane, or goal-front defender position"
      objective_conversion: "force gem carrier drop/retreat, remove a goalkeeper before a score, or stop a tank/scorer push for 8 seconds"
      active_when: "the target must cross a known choke or objective route and Cordelius' team can hold the remaining 2v2 or convert after the isolation"
      fails_if: "Cordelius sends away the wrong target, his team collapses while he is absent, or the isolated target kites him until the timer ends"
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Sneaky Fields
        - Center Stage
      bp_use: map_bp_factors.single_target_objective_disarm
    - map_feature_type: "replanting_route_gate_and_shadow_objective_travel"
      uses_feature_by: "Replanting crosses wall/water gates and Fandom notes Shadow Realm can move Cordelius unseen toward Heist safe or Hot Zone"
      route_or_position: "safe barrier, water edge, central wall, or side route that normal walking cannot cross safely"
      objective_conversion: "turn a gated route into safe access, zone re-entry, or backline contact after isolating one defender"
      active_when: "terrain is the main access cost and Cordelius still has enough health, ammo, or realm timer to threaten after crossing"
      fails_if: "crossing only lands him in short-range focus fire, objective damage is too low, or a thrower/control pocket covers the landing"
      example_maps:
        - Safe Zone
        - Pit Stop
        - New Horizons
        - Flaring Phoenix
      bp_use: map_bp_factors.route_gate_bypass_with_target_access_check
    - map_feature_type: "anti_aggro_choke_guard"
      uses_feature_by: "Trait rewards guarding contested standoffs and Super/Poison Mushroom punish enemies that must enter Cordelius radius"
      route_or_position: "single-zone entrance, wall-adjacent zone edge, ball side lane, or close gem choke"
      objective_conversion: "deny the first body stepping onto zone, stop a dash scorer, or force a tank to retreat before objective contact"
      active_when: "enemy plan depends on one close-range body entering a predictable route and Cordelius has Super or Poison Mushroom available"
      fails_if: "enemy controls from outside his range, chains reveal/slow before entry, or baits the control tool with a low-value target"
      example_maps:
        - Dueling Beetles
        - Ring of Fire
        - Open Business
        - Triple Dribble
      bp_use: candidate_eval.anti_aggro_resource_gate

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - defender_isolation_for_safe_entry
        - replanting_or_shadow_route_to_safe
        - anti_aggro_defense_against_short_range_safe_threat
      cannot_fulfill:
        - primary_safe_dps
        - long_range_lane_race
      needs_teammate_support:
        - sustained safe DPS teammate
        - lane pressure while Cordelius commits to isolation
      false_positive: "Heist value comes from route/defender disruption; if the map asks only for long-range safe DPS, Cordelius is a utility pick, not the race engine."
    - mode: "Brawl Ball"
      can_fulfill:
        - goalkeeper_or_scorer_isolation
        - Poison_Mushroom_ball_action_denial
        - wall_or_water_jump_entry
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - open_field_primary_scorer
      needs_teammate_support:
        - scorer or wallbreak teammate to convert removed defender
        - damage after target exits Shadow Realm
      false_positive: "Removing one defender creates a score window only if the ball route and follow-up already exist."
    - mode: "Gem Grab"
      can_fulfill:
        - carrier_ambush_or_drop
        - side_grass_anti_aggro
        - countdown_route_disruption
      cannot_fulfill:
        - stable_open_mid_carrier
        - long_range_mine_control
      needs_teammate_support:
        - mid control while Cordelius leaves the normal map
        - teammate who can collect or guard dropped gems
      false_positive: "Shadow Realm can flip carrier tempo, but it can also leave his team exposed during the 2v2."
    - mode: "Hot Zone"
      can_fulfill:
        - first_body_zone_denial
        - route_guard_from_wall_or_grass
        - emergency_reentry_with_jump_or_realm_speed
      cannot_fulfill:
        - long_duration_zone_body
        - thrower_pocket_clear
      needs_teammate_support:
        - durable zone holder
        - wallbreak/dive answer if enemy controls pocket from outside Cordelius range
      false_positive: "Cordelius is an entry denial and isolation tool; he still needs someone to occupy the zone."

  failure_modes:
    - id: "middling_range_and_low_health_open_lane"
      active_when: "map is open, enemy can kite outside 5.33-tile main attack range, or Cordelius must lead a charge without cover"
      exposed_by: "[[sources/Fandom-Cordelius|Fandom-Cordelius]] attack range, 3500 health, and tips warning he struggles as a leading offensive Brawler"
      mitigation: "draft him as a response pick on constrained routes, with Replanting angles, or behind teammate lane pressure"
      bp_use: avoid_first_pick_on_open_range_maps
    - id: "team_exposed_while_in_shadow_realm"
      active_when: "Cordelius removes himself and one enemy while the remaining enemy comp can immediately collapse on his teammates"
      exposed_by: "[[sources/Fandom-Cordelius|Fandom-Cordelius]] tips warning Gem Grab isolation leaves the team vulnerable"
      mitigation: "use Super after teammate positioning is stable or when removing the target directly wins the objective"
      bp_use: objective_conversion_check
    - id: "wrong_target_or_preloaded_tool_in_realm"
      active_when: "the isolated enemy already has an attack-modifying Gadget active, is another Cordelius, or can stall the duel until timer ends"
      exposed_by: "[[sources/Fandom-Cordelius|Fandom-Cordelius]] Shadow Realm notes about preloaded Gadgets and enemy Cordelius buffs"
      mitigation: "track enemy resources before Super and prioritize carriers/scorers rather than generic frontliners"
      bp_use: target_selection_and_resource_tracking
    - id: "thrower_or_long_range_denies_access"
      active_when: "enemy plays behind walls or at long range where Cordelius cannot safely enter Trait radius"
      exposed_by: "[[sources/Fandom-Cordelius|Fandom-Cordelius]] tips saying he is weak to long-ranged and more agile Brawlers plus [[sources/PLP-Cordelius|PLP-Cordelius]] target-favored list"
      mitigation: "pair with wallbreak, flank pressure, or save Cordelius for last-pick route punishment"
      bp_use: map_fit_filter

  conditional_matchup_seeds:
    - target:
        - "Tara"
        - "Shelly"
        - "Rosa"
        - "Colette"
        - "Bull"
        - "Fang"
      direction: "subject_favored"
      source: "[[sources/PLP-Cordelius|PLP-Cordelius]]"
      mechanism: "Shadow Realm and Poison Mushroom deny close-range Supers/Gadgets and force tanks or engage picks into a Cordelius-favored 1v1."
      active_when: "target must enter a choke, ball route, zone, or gem lane and Cordelius has Super, Poison Mushroom, or Replanting angle ready"
      fails_when: "target keeps open spacing, baits Super, has teammate pressure on the remaining 2v2, or Cordelius lacks health to win the duel"
      bp_use: response_pick_candidate_against_tank_or_single_engage
    - target:
        - "Chuck"
        - "Stu"
      direction: "subject_favored"
      source: "[[sources/PLP-Cordelius|PLP-Cordelius]] / [[sources/Fandom-Cordelius|Fandom-Cordelius]]"
      mechanism: "Shadow Realm interrupts route or dash tempo by removing the target from the normal objective race and disabling Super/Gadget follow-up."
      active_when: "their value depends on a predictable dash/post/scoring route and Cordelius can hit the Super before objective contact"
      fails_when: "they bait the isolation, already completed the objective touch, or Cordelius' teammates lose the normal-map fight"
      bp_use: route_plan_disruption_candidate
    - target:
        - "Gale"
        - "Max"
        - "Griff"
        - "Crow"
        - "Amber"
        - "Surge"
      direction: "target_favored"
      source: "[[sources/PLP-Cordelius|PLP-Cordelius]]"
      mechanism: "Range, speed, slow/knockback, poison chip, or burst control can keep Cordelius outside his preferred radius or punish him before the realm duel starts."
      active_when: "map gives them open lanes, repeated kite space, or side angles that force Cordelius to cross visible ground"
      fails_when: "Cordelius reaches through grass/wall jump, catches the actual carrier/scorer, or their key escape/control is already spent"
      bp_use: avoid_open_lane_first_pick_or_require_route_support
    - target:
        - "Nita"
        - "Frank"
      direction: "volatile"
      source: "[[sources/PLP-Cordelius|PLP-Cordelius]] / [[sources/Fandom-Cordelius|Fandom-Cordelius]]"
      mechanism: "Cordelius can isolate bulky targets, but spawnables, stun pressure, or high health can outlast his short-range damage if he lacks Comboshrooms or teammate conversion."
      active_when: "Cordelius isolates them away from support near an objective route and enters with ammo/health advantage"
      fails_when: "Bruce or teammates tax his shots, Frank controls the choke before Super lands, or the normal fight collapses during isolation"
      bp_use: resource_and_objective_context_check

  slot_notes:
    slot_1: "risky except on maps where route denial and anti-aggro are mandatory and long-range/thrower punishers are already banned or weak."
    slot_2_3: "strong as response to a first-pick tank, scorer, Chuck-style route plan, or single-core carrier strategy."
    slot_4_5: "repairs drafts that need one-target removal, but keep a teammate slot for damage, zone body, or safe DPS conversion."
    slot_6: "best as last-pick punishment when enemy lacks open-range kite, thrower pocket, or a way to win the remaining 2v2 while Cordelius is in realm."
```
