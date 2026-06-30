# Darryl

## 基本信息

- 稀有度：Super Rare
- 定位：Tank
- 类型：滚动切入英雄

## 攻击特征

- 主攻击是双管霰弹
- 近距离命中时威胁更高
- 适合在切入后持续贴脸压制

## 超级技能特征

- Super 会变成桶状滚动
- 能穿墙、击退并减伤
- 还会随时间自动充能，形成独特的进场节奏

## 适合场景

- 需要快速切入的局面
- 草丛和墙体较多的地图
- 需要抓住一波进场时机的模式

## 角色定位总结

Darryl 是靠滚桶切入和滚动压制吃饭的前排英雄，和 `Bull` 一样擅长开团，但更强调 Super 的路线控制和自动充能节奏。

## 关联页面

- [[sources/Fandom-Darryl|Fandom 来源摘要: Darryl]]
- [[sources/PLP-Darryl|Power League Prodigy 来源摘要: Darryl]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "short_mid; 6-tile shotgun range exists, but real burst comes from point-blank shell density after a roll"
    projectile_reliability: "high_at_contact_low_at_edge; wide shotgun and Tar Barrel help close fights, but missing roll spacing can leave him outside burst range"
    burst: "very_high_point_blank; double shotgun plus roll knockback can delete fragile targets or punish a safe/goal defender"
    sustained_dps: "medium_before_roll_high_with_Rolling_Reload; 1.8s reload is ordinary, while Rolling Reload doubles reload speed for 5 seconds after Super"
    objective_damage: "high_if_heist_entry_connects; Recoiling Rotator and point-blank shells can damage safe, but he needs a route and Super timing"
    mobility: "high_resource_based; auto-charging double Barrel Roll gives two long, shielded entries and can cross water"
    survivability: "high_during_entry; 5500 health, 50% roll shield, and Steel Hoops 25% post-roll shield let him absorb one engage window"
    engage: "high_route_based; roll knockback and Tar Barrel force contact when terrain narrows the entry"
    disengage: "medium_high; roll can escape or cross water, but spending both rolls removes pressure until auto-charge returns"
    anti_aggro: "medium_high; knockback, Tar Barrel slow, and shotgun burst punish divers if Darryl has roll or close spacing"
    anti_tank: "medium; close burst is real, but percent damage, knockback chains, or heavier melee can reverse the trade"
    wall_break: low
    throw_or_wall_bypass: "medium; roll bounces off walls and crosses water, but does not pass through rope fences or hard obstacles"
    area_control: "low_medium; Tar Barrel creates a moving slow aura around Darryl for objective-contact fights"
    scouting_or_vision: "low_medium_with_Recoiling_Rotator; Gadget can scout bushes by spraying pellets"
    team_support: "medium_indirect; knockback can drop ball or protect a teammate from an engage, but Darryl is mainly a self-entry tank"
    spawnable_or_pet: low
    crowd_control: "medium; roll knockback plus Tar Barrel slow can interrupt Supers and force close-range contact"
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Darryl|Fandom-Darryl]]"
      - "[[sources/PLP-Darryl|PLP-Darryl]]"

  build_switches:
    - build: "Tar Barrel / Steel Hoops / Shield, Damage"
      source: "[[sources/PLP-Darryl|PLP-Darryl]]"
      changes_capabilities:
        - "Tar Barrel adds a moving 2.33-tile slow aura around Darryl to secure contact after roll"
        - "Steel Hoops extends survivability after roll with 25% damage reduction for 2 seconds"
        - "Shield and Damage gears increase entry margin and close-range kill confirmation"
      enables:
        - shielded_roll_entry
        - tar_slow_contact_confirm
        - anti_thrower_or_sniper_dive
        - ball_carrier_knockback
      mitigates_failure_modes:
        - roll_stops_short_of_target
        - post_roll_focus_fire
        - close_target_kites_after_knockback
      best_when: "map provides wall, grass, water, or side route that lets Darryl roll into a high-value target without crossing full open range"
      poor_when:
        - "enemy has layered knockback, percent damage, hard control, or a tank mirror waiting at the landing"
        - "draft needs ranged safe DPS or wallbreak rather than entry pressure"
      bp_use: default_reviewed_build_for_safe_or_knockout_entry
    - build: "Recoiling Rotator / Rolling Reload variants"
      source: "[[sources/Fandom-Darryl|Fandom-Darryl]]"
      changes_capabilities:
        - "Recoiling Rotator sprays 15 shells around Darryl, scouts bushes, and can add Heist safe damage from point blank"
        - "Rolling Reload doubles reload speed for 5 seconds after Super, improving tank duels and safe burst"
      enables:
        - safe_burst_after_entry
        - bush_scout
        - tank_duel_after_roll
      mitigates_failure_modes:
        - low_damage_after_first_burst
        - hidden_bush_defender
      best_when: "Heist route reaches safe or a close tank duel is unavoidable after the roll"
      poor_when:
        - "survival after roll matters more than extra DPS"
      bp_use: situational_variant_for_heist_or_tank_trade

  map_feature_hooks:
    - map_feature_type: "heist_roll_to_safe_burst_window"
      uses_feature_by: "Barrel Roll crosses water, bounces off walls, grants 50% damage reduction, and can be followed by point-blank shells or Recoiling Rotator"
      route_or_position: "safe barrier, side grass entry, water edge, or safe-facing wall where roll reaches the vault"
      objective_conversion: "turn a lane win or roll charge into immediate safe damage and force defenders to hold close anti-tank tools"
      active_when: "Darryl has Super, a route to safe, and teammates prevent defenders from camping the landing for free"
      fails_if: "open long-range lanes stop charge, enemy holds Colette/Shelly/Gale-style denial, or Darryl reaches safe without ammo"
      example_maps:
        - Pit Stop
        - Hot Potato
        - Safe Zone
        - Safe(r) Zone
      bp_use: candidate_eval.heist_entry_and_safe_burst
    - map_feature_type: "knockout_wall_bounce_last_pick_engage"
      uses_feature_by: "roll can bounce off walls, hit multiple times in confined areas, knock back targets, and enter with shield"
      route_or_position: "Knockout side choke, checkered wall pocket edge, side water-bush route, or central cover corner"
      objective_conversion: "punish an exposed thrower/sniper/control pick after enemy peel is known and secure the first knockout"
      active_when: "enemy lacks close peel or hard CC and the map offers a roll angle that ends in shotgun range"
      fails_if: "Darryl rolls through the target, lands in full-team control, or the wall pocket is protected by anti-tank burst"
      example_maps:
        - Belle's Rock
        - Flaring Phoenix
        - New Horizons
        - Out in the Open
      bp_use: slot_task.last_pick_route_based_engage
    - map_feature_type: "brawl_ball_knockback_and_double_roll_score"
      uses_feature_by: "Fandom notes Darryl can knock ball carriers loose, defend goal, and kick-forward plus roll twice to score"
      route_or_position: "midfield ball race, side grass lane, goal-front pocket, or closed-lane scoring route"
      objective_conversion: "drop enemy ball, delay a scoring attempt, or cover distance for a two-roll score"
      active_when: "ball route is predictable and enemy has no immediate counter near goal"
      fails_if: "goal remains closed with no wallbreak/control support, enemy holds knockback/silence, or Darryl rolls into stacked defenders"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_carrier_disarm_and_score_route
    - map_feature_type: "grass_or_water_short_range_entry_filter"
      uses_feature_by: "Darryl can use grass, walls, and water roll extension to shorten approach cost"
      route_or_position: "center grass band, side bush lane, water gap, or lane split where walking short-range is punished"
      objective_conversion: "convert hidden approach into lane win, safe entry, or defender displacement"
      active_when: "grass/water actually ends in target contact and Darryl can leave after spending the roll"
      fails_if: "vision clears grass, water crossing leaves him in open fire, or target can kite beyond shotgun density"
      example_maps:
        - Hot Potato
        - Kaboom Canyon
        - Bridge Too Far
        - Flaring Phoenix
      bp_use: map_bp_factors.short_range_route_false_positive_filter

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - roll_entry_to_safe
        - point_blank_safe_burst
        - close_defender_displacement
      cannot_fulfill:
        - long_range_safe_race
        - wallbreak_route_creation
      needs_teammate_support:
        - lane control until Super is ready
        - answer to anti-tank defender at landing
      false_positive: "Darryl is a route-to-safe burst pick; if he cannot touch safe, he is not a Heist DPS substitute."
    - mode: "Knockout"
      can_fulfill:
        - route_based_last_pick_engage
        - protected_first_contact
        - anti_thrower_or_sniper_punish
      cannot_fulfill:
        - blind_frontline_entry_into_full_control
        - open_lane_poke_without_super
      needs_teammate_support:
        - lane pressure or wall control to force target path
        - ban/answer to anti-tank CC if picked early
      false_positive: "Knockout Darryl is strongest after enemy peel is known; first-picking him invites hard anti-tank answers."
    - mode: "Brawl Ball"
      can_fulfill:
        - ball_carrier_knockback
        - two_roll_score_route
        - goal_defense_delay
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - long_open_mid_control
      needs_teammate_support:
        - wallbreak/scorer if goal geometry is closed
        - control teammate to stop counter-push after Darryl spends rolls
      false_positive: "Fandom supports Brawl Ball utility, but scoring depends on route and counter location rather than generic tank value."

  failure_modes:
    - id: "roll_route_predictability_and_landing_camp"
      active_when: "enemy can hold the endpoint with knockback, burst, percent damage, or spawnable body before Darryl exits roll"
      exposed_by: "[[sources/Fandom-Darryl|Fandom-Darryl]] notes on roll route/spacing plus [[sources/PLP-Darryl|PLP-Darryl]] target-favored list"
      mitigation: "save Darryl for later slots, vary bounce angle, or draft teammate pressure that punishes endpoint campers"
      bp_use: endpoint_and_route_check
    - id: "open_range_before_super"
      active_when: "Darryl must walk through open long lanes before Super is ready or after both rolls are spent"
      exposed_by: "[[sources/Fandom-Darryl|Fandom-Darryl]] auto-charge timing and short-range burst profile"
      mitigation: "use grass/walls/water routes, protect early lane, or avoid on maps where every route is visible"
      bp_use: early_lane_false_positive_filter
    - id: "shotgun_spacing_miss"
      active_when: "roll stops too far away, rolls through the target, or knockback pushes the target out of shell density"
      exposed_by: "[[sources/Fandom-Darryl|Fandom-Darryl]] attack and strategy warnings about point-blank positioning"
      mitigation: "aim bounce angles for contact, use Tar Barrel after roll, and evaluate lanes with predictable endpoints"
      bp_use: execution_reliability_filter
    - id: "anti_tank_or_control_chain"
      active_when: "enemy has Colette percent damage, Shelly/Bull/Bibi close burst, Gale knockback, Chester burst, Willow control, Sandy reveal/control, or Nita body-block"
      exposed_by: "[[sources/PLP-Darryl|PLP-Darryl]] counteredBy list"
      mitigation: "ban or bait the key answer before committing Darryl, or use him on a separate objective route"
      bp_use: must_answer_before_drafting_darryl

  conditional_matchup_seeds:
    - target:
        - "Mr. P"
        - "Jessie"
        - "Sprout"
        - "Piper"
        - "Ziggy"
      direction: "subject_favored"
      source: "[[sources/PLP-Darryl|PLP-Darryl]]"
      mechanism: "Shielded roll, wall bounce, knockback, and point-blank shotgun burst punish fragile, static, or wall-control targets once Darryl has a valid route."
      active_when: "map gives a grass, wall, water, or choke path ending in shotgun range and target lacks a bodyguard or hard interrupt"
      fails_when: "target controls from a deeper pocket, endpoint is camped, or Darryl must cross open range before roll"
      bp_use: response_pick_candidate_against_fragile_control
    - target:
        - "Alli"
        - "Jae-Yong"
        - "Poco"
      direction: "subject_favored"
      source: "[[sources/PLP-Darryl|PLP-Darryl]]"
      mechanism: "Darryl can force close contact before utility or support tempo accumulates, using Tar Barrel and roll knockback to prevent clean retreat."
      active_when: "objective forces the target to stand near a lane, safe, or zone route and Darryl has Super or a protected flank"
      fails_when: "support shell has anti-tank damage, Darryl cannot isolate the target, or he spends both rolls without a kill"
      bp_use: dive_or_objective_contact_response_candidate
    - target:
        - "Chester"
        - "Bull"
        - "8-Bit"
        - "Willow"
        - "Sandy"
        - "Colette"
        - "Nita"
        - "Bibi"
      direction: "target_favored"
      source: "[[sources/PLP-Darryl|PLP-Darryl]]"
      mechanism: "Close burst, percent damage, sustained DPS, control, spawnable body-block, concealment, or knockback can punish Darryl's predictable landing and deny follow-up shells."
      active_when: "they can guard the roll endpoint, force repeated close trades, or hold objective space Darryl must enter"
      fails_when: "Darryl attacks a different route, baits the key control, or teammates punish the defender while Darryl draws attention"
      bp_use: avoid_first_pick_or_require_route_protection
    - target:
        - "Frank"
        - "Shelly"
        - "El Primo"
        - "Jacky"
      direction: "volatile"
      source: "[[sources/Fandom-Darryl|Fandom-Darryl]]"
      mechanism: "Darryl can cancel some Supers with roll knockback and burst at point blank, but heavy melee bodies can also win if he lands without ammo, shield, or Tar Barrel."
      active_when: "Darryl has Super, Tar Barrel, ammo, and a bounce angle that controls first contact"
      fails_when: "enemy holds their CC/burst until post-roll or Darryl crosses into multiple close-range bodies"
      bp_use: tank_mirror_resource_check

  slot_notes:
    slot_1: "risky unless map hard-requires roll entry and major anti-tank answers are banned; early Darryl is easy to route-camp."
    slot_2_3: "usable into an exposed fragile/control first pick on Heist or Knockout if teammates can cover early charge time."
    slot_4_5: "good for adding route-based engage after seeing enemy 2-3, while reserving a final answer to anti-tank or long-range punish."
    slot_6: "strongest when enemy lacks endpoint CC, spawnable body-block, or close burst and the map gives a confirmed roll angle to target or safe."
```
