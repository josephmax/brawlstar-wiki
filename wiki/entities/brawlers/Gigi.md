# Gigi

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：路线刺客 / 弹道充能 / 传送进出

## 来源摘要

- Fandom：[[sources/Fandom-Gigi|Fandom 来源摘要: Gigi]]
- PLP：[[sources/PLP-Gigi|PLP 来源摘要: Gigi]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Bounty, Knockout

## 角色定位总结

Gigi 的 BP 价值不是“短手无脑切后排”，而是利用敌方弹道给 Trait 充能，在墙草或混合掩体附近用 Shadow Puppet 进出，并用 A Helping Hand 的治疗保住第一轮切入。她在纯开放长线图里很依赖最后手条件；如果没有接近路线、弹道充能或队友压制，短射程会迅速变成负担。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "short; Pirouette Power-up hits around Gigi in a 2.33-tile radius and can damage enemies behind walls"
    projectile_reliability: "route_based; attack itself requires proximity, but Trait converts nearby enemy projectiles into Super charge"
    burst: "medium_high_if_teleport_connects; Shadow Puppet deals return damage and Hypercharge can add arrival damage"
    sustained_dps: "high_in_contact_window; very fast ammo-bar reload and accelerating spin frequency reward staying near the target"
    objective_damage: "low_medium; PLP modes favor kill pressure, space theft, and ball/gem tempo rather than safe or stationary DPS"
    mobility: "high; 35% speed while attacking, 7.33-tile Super teleport, and optional return within 3 seconds"
    survivability: "medium_with_build; 4100 health, Shield gear, and A Helping Hand heal after initial teleport"
    engage: "high_when_route_and_super_exist; can enter over space after the 0.8-second teleport delay"
    disengage: "conditional; return teleporter can reset position, but only inside the 3-second Super window"
    anti_aggro: "medium; spin damage punishes close contact but loses to heavier burst or hard CC"
    anti_tank: "low_medium; can kite around walls but lacks reliable tank shred without team damage"
    wall_break: low
    throw_or_wall_bypass: "medium_high; attack can hit behind walls and Super changes position across a line"
    area_control: "medium; proximity threat and optional Disappearing Act can deny a small wall/grass pocket"
    scouting_or_vision: "low_medium; pressure comes from route threat, not reveal"
    team_support: "medium_if_Disappearing_Act_is_selected; PLP default focuses on Longer Strings and self-heal"
    spawnable_or_pet: low
    crowd_control: low
    terrain_creation: "low_medium; Disappearing Act creates a temporary invisibility tent area, not durable terrain"
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Gigi|Fandom-Gigi]]"
      - "[[sources/PLP-Gigi|PLP-Gigi]]"

  build_switches:
    - build: "Longer Strings / A Helping Hand / Shield, Damage"
      source: "[[sources/PLP-Gigi|PLP-Gigi]]"
      changes_capabilities:
        - "Longer Strings expands the Trait radius to 4.67 tiles for 4 seconds, making projectile-lane Super charging easier"
        - "A Helping Hand heals after the initial Shadow Puppet teleport, supporting first-contact survival"
        - "Shield and Damage gears support short-range entry and finish windows"
      enables:
        - projectile_lane_super_charge
        - wall_edge_teleport_entry
        - last_pick_backline_pressure
      mitigates_failure_modes:
        - entry_health_gap
        - slow_super_cycle_against_projectiles
      best_when: "enemy draft has projectile lanes near cover and lacks reliable peel on the teleport destination"
      poor_when:
        - "enemy damage is instant, melee, or route-denying enough that Trait cannot charge safely"
        - "Gray is available as a direct avoid signal from PLP and the map lets him punish endpoints"
      bp_use: default_reviewed_build_for_route_assassin_and_projectile_charge
    - build: "Disappearing Act team pocket variant"
      source: "[[sources/Fandom-Gigi|Fandom-Gigi]]"
      changes_capabilities:
        - "creates a 2-tile invisibility area for Gigi and allies for 3 seconds"
      enables:
        - hidden_entry_window
        - short_team_reposition
      mitigates_failure_modes:
        - exposed_pre_entry_position
      poor_when:
        - "the team needs Longer Strings to reliably cycle Super from projectile traffic"
      bp_use: situational_support_tool_for_wall_or_bush_pocket

  map_feature_hooks:
    - map_feature_type: "projectile_lane_super_charge"
      uses_feature_by: "Gigi farms Super when enemy projectiles or melee attack hitboxes enter her Trait radius, with Longer Strings expanding that radius for a timed window"
      route_or_position: "wall edge, mid cover, or side lane where enemy shots pass near Gigi but she can dodge instead of taking direct damage"
      objective_conversion: "turn projectile traffic into Shadow Puppet tempo for a gem-side collapse, Bounty pick attempt, or Knockout space steal"
      active_when: "enemy has projectile-heavy lanes and the map gives cover or dodge space near the shot path"
      fails_if: "enemy attacks have no travel time, use themselves as projectiles, or simply outrange Gigi from fully open space"
      example_maps:
        - Hard Rock Mine
        - Hideout
        - Belle's Rock
        - New Horizons
      bp_use: map_bp_factors.projectile_charge_route
    - map_feature_type: "wall_edge_pirouette_and_teleport_entry"
      uses_feature_by: "Pirouette Power-up can damage enemies behind walls, while Shadow Puppet lets Gigi choose a short engage and return line"
      route_or_position: "side wall pocket, center layer entrance, or thrower pocket edge where Gigi can reach without crossing a full open lane"
      objective_conversion: "force thrower/control picks off cover, secure a Knockout/Bounty pick, or open a Gem/Ball side lane"
      active_when: "walls remain useful for Gigi's approach and enemy peel is not already covering the landing point"
      fails_if: "wallbreak removes the route, a bodyguard waits at the destination, or Gigi loses the 3-second return option"
      example_maps:
        - Belle's Rock
        - Layer Cake
        - Gem Fort
        - Pinball Dreams
      bp_use: must_answer_thrower_pocket_or_backline_route
    - map_feature_type: "brawl_ball_shadow_puppet_tempo"
      uses_feature_by: "attack speed boost, teleport threat, and close spin pressure can force a defender to give up a ball lane"
      route_or_position: "midfield grass, side wall lane, or goal approach after a teammate creates a scoring angle"
      objective_conversion: "clear the ball path, pressure the last defender, or chase a weak carrier before reset"
      active_when: "team has ball follow-up and Gigi can enter from cover rather than a naked open line"
      fails_if: "enemy has knockback, hard CC, or a tank bodyguard waiting on the teleport endpoint"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Pinball Dreams
      bp_use: slot_task.tempo_scorer_support

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - side_lane_pick_pressure
        - projectile_charge_into_carrier_collapse
        - wall_edge_threat_against_mid_control
      cannot_fulfill:
        - safe_primary_gem_carrier
        - long_range_mid_control_without_route
      needs_teammate_support:
        - stable mid or carrier
        - vision, slow, or damage follow-up after teleport
      false_positive: "Gigi can threaten the carrier route, but she should not be treated as the team's stable gem holder."
    - mode: "Brawl Ball"
      can_fulfill:
        - defender_pressure_after_teleport
        - side_wall_lane_threat
        - tempo_clear_for_scorer
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - solo_score_through_hard_CC
      needs_teammate_support:
        - scorer, wallbreak, or control follow-up
        - anti-tank answer if enemy drafts a bodyguard
      false_positive: "Teleport tempo does not replace a goal-opening plan."
    - mode: "Bounty"
      can_fulfill:
        - last_pick_route_assassin
        - wall_pocket_pressure
        - projectile_lane_super_cycle
      cannot_fulfill:
        - early_blind_pick_on_extreme_open_lanes
        - low_risk_star_hold_after_failed_entry
      needs_teammate_support:
        - long-range teammates who can hold stars while Gigi threatens route
        - wallbreak or control if enemy owns the central pocket
      false_positive: "On Shooting Star or Dry Season style open maps, Gigi is a high-risk last response, not a default Bounty opener."
    - mode: "Knockout"
      can_fulfill:
        - route_based_pick_pressure
        - center_space_steal
        - anti_thrower_or_sniper_endpoint_threat
      cannot_fulfill:
        - blind_dive_into_peel
        - durable_frontline_anchor
      needs_teammate_support:
        - teammate chip to make the teleport lethal
        - endpoint cover or reset route
      false_positive: "Knockout deaths are permanent; Gigi needs a route and a confirmed target, not just a target name."

  failure_modes:
    - id: "open_long_range_no_route"
      active_when: "map is a pure long sightline and Gigi must cross without walls, grass, or teammate pressure"
      exposed_by: "[[sources/Fandom-Gigi|Fandom-Gigi]] short attack range and [[entities/maps/Shooting Star|Shooting Star]] / [[entities/maps/Dry Season|Dry Season]] open-lane rules"
      mitigation: "reserve Gigi for mixed-cover maps or last-pick only after enemy peel is gone"
      bp_use: false_positive_filter
    - id: "trait_not_charging_from_target"
      active_when: "enemy attacks have no travel time, enemy uses themselves as the projectile, or the shot path never enters the Trait radius"
      exposed_by: "[[sources/Fandom-Gigi|Fandom-Gigi]] Trait exclusions for game objects, self-projectile movement, and instant attacks"
      mitigation: "check target attack type before valuing Longer Strings or projectile-charge routes"
      bp_use: matchup_activation_filter
    - id: "teleport_endpoint_trap"
      active_when: "enemy holds bodyguard, burst, knockback, or CC at the Shadow Puppet destination or return point"
      exposed_by: "[[sources/Fandom-Gigi|Fandom-Gigi]] 0.8-second teleport delay and 3-second return window"
      mitigation: "enter after enemy peel is spent or choose endpoints with teammate cover"
      bp_use: slot_6_execution_check
    - id: "short_range_into_heavy_burst"
      active_when: "Gigi is forced to spin inside tank, shotgun, or heavy melee range without a kill threshold"
      exposed_by: "[[sources/PLP-Gigi|PLP-Gigi]] target-favored list including Chester, Bull, Doug, Fang, and Bibi"
      mitigation: "avoid early pick into unshown anti-aggro; pair with slow, chip, or anti-tank"
      bp_use: avoid_first_pick_or_require_team_damage

  conditional_matchup_seeds:
    - target:
        - "Mr. P"
        - "Jessie"
        - "Dynamike"
        - "Sprout"
      direction: "subject_favored"
      source: "[[sources/PLP-Gigi|PLP-Gigi]]"
      mechanism: "Gigi can threaten wall or spawnable/control pockets because Pirouette hits around her and Shadow Puppet changes position without walking the full lane."
      active_when: "map has walls or layered cover and the target lacks a bodyguard covering Gigi's endpoint"
      fails_when: "target has deeper peel, summon/bodyguard protection, or wallbreak opens the lane before Gigi can use cover"
      bp_use: response_pick_seed_against_wall_control
    - target:
        - "Bea"
        - "Lola"
        - "Piper"
        - "Chuck"
      direction: "subject_favored"
      source: "[[sources/PLP-Gigi|PLP-Gigi]]"
      mechanism: "Projectile traffic and aim-locked lanes can feed Gigi's Trait while teleport tempo punishes targets that lack close peel after the first dodge window."
      active_when: "Gigi can charge near cover and close after a miss or teammate chip"
      fails_when: "the target keeps a fully open long lane, has trap/peel support, or Gigi cannot enter Trait range without taking lethal damage"
      bp_use: last_pick_or_side_lane_pressure_seed
    - target:
        - "Chester"
        - "Bull"
        - "Doug"
        - "Fang"
        - "Bibi"
      direction: "target_favored"
      source: "[[sources/PLP-Gigi|PLP-Gigi]]"
      mechanism: "Close-range burst, body health, knockback, or chain engage punishes Gigi's need to remain near the target during the spin window."
      active_when: "objective or endpoint forces Gigi into their preferred melee range"
      fails_when: "Gigi can attack from a wall edge, return safely, or has teammate chip that makes the engage a confirmed finish"
      bp_use: avoid_first_pick_or_require_chip
    - target:
        - "Gray"
        - "Sandy"
        - "Pearl"
      direction: "target_favored"
      source: "[[sources/PLP-Gigi|PLP-Gigi]]"
      mechanism: "Reposition, concealment, area damage, or high punish windows can cover the teleport endpoint and deny Gigi's return route."
      active_when: "map has a predictable wall route or Gigi must enter through a narrow endpoint"
      fails_when: "Gigi waits for the control tool to be spent or attacks a separated target outside the support pocket"
      bp_use: endpoint_control_warning

  slot_notes:
    slot_1: "risky except on maps with obvious wall routes and bans against heavy anti-aggro; early Gigi invites tank/burst/Gray-style answers"
    slot_2_3: "usable as a plan piece if the enemy already showed projectile lanes and the team can hold mid while Gigi threatens side routes"
    slot_4_5: "good to answer thrower/pocket or fragile long-range picks when endpoint peel is limited"
    slot_6: "best as a last-pick route assassin after confirming no bodyguard, hard CC, or open-map kiting answer remains"
```

## 关联页面

- [[sources/Fandom-Gigi|Fandom 来源摘要: Gigi]]
- [[sources/PLP-Gigi|PLP 来源摘要: Gigi]]
