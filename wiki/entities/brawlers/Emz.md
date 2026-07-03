# Emz

## 基本信息

- 稀有度：Epic
- 定位：Controller
- 类型：持续范围压制英雄

## 攻击特征

- 主攻击会喷出持续雾气
- 越靠近越容易吃满伤害
- 适合卡线和惩罚站位

## 超级技能特征

- Super 会释放更大范围的雾气
- 同时带减速效果
- 非常适合把敌人赶出关键区域

## 适合场景

- 需要逼位和控图的对局
- 对手喜欢卡近中距离站位的地图
- 防守反打和区域封锁场景

## 角色定位总结

Emz 是一个靠喷雾持续伤害和减速区域来逼位的控场英雄，强在让对手无法舒服站在线上。

## 关联页面

- [[sources/Fandom-Emz|Fandom 来源摘要: Emz]]
- [[sources/PLP-Emz|Power League Prodigy 来源摘要: Emz]]

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  review_gate: reviewed_with_sources_map_hooks_and_matchup_edges
  source_quality:
    fandom: "[[sources/Fandom-Emz|Fandom-Emz]] direct_raw_capture_2026-06-30"
    plp: "[[sources/PLP-Emz|PLP-Emz]] direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "mid 6.67 tile spray; strongest around the outer-middle band where enemies take multiple ticks"
    projectile_reliability: "high into chokes, grass edges, and grouped pushes; lower against long-range sidestep lanes or targets already inside her minimum comfort range"
    burst: "medium to high when the target stays in the 3-tick band or Bad Karma stacks; weak if the target exits immediately"
    sustained_dps: "medium area pressure with 2s reload; ammo must be preserved for entry denial"
    objective_damage: "conditional Heist pressure only when modifier or map forces safe defenders into spray range; not a primary safe DPS profile"
    mobility: "low; no dash, so position must be pre-held"
    survivability: "medium through Hype healing when Super hits enemies; base 3900 health is punishable if she is outranged"
    engage: "medium as zone-entry slow and walking cloud; not a hard dive tool"
    disengage: "high against close entry with Friendzoner knockback plus Super slow"
    anti_aggro: "high when she holds Friendzoner or Super and the diver must cross spray range"
    anti_tank: "high in midrange lanes where tanks absorb multiple spray ticks; lower once they reach point-blank after tools are spent"
    wall_break: "none"
    throw_or_wall_bypass: "limited Acid Spray one-attack wall pass; default attack is not a thrower pattern"
    area_control: "very_high through lingering spray lanes and 5-second slowing Super"
    scouting_or_vision: "medium as wide spray/bush sweep at close to mid range"
    team_support: "indirect peel through slow, knockback, and forced spacing"
    spawnable_or_pet: "none"
    crowd_control: "high with Super slow and Friendzoner knockback; Buffie wall-stun variant adds a punish angle"
    terrain_creation: "none"
    terrain_destruction: "none"

  build_switches:
    - build: "Friendzoner / Hype / Shield, Damage"
      source: "[[sources/PLP-Emz|PLP-Emz]]"
      changes_capabilities:
        - "raises anti-aggro and ball-defense reliability by pushing close threats back into spray"
        - "Hype converts multi-target Super into zone sustain"
      enables:
        - "Gem Grab mid choke control"
        - "Brawl Ball carrier disarm and goal defense"
        - "Hot Zone entry denial"
      mitigates_failure_modes:
        - "point_blank_deadzone"
        - "multi_body_zone_pressure"
      best_when: "enemy has tanks, assassins, or scorers that must enter Emz's spray band"
      poor_when: "enemy outranges her from behind walls or can bait Friendzoner before the real engage"
      bp_use: "default_build_for_anti_aggro_control"
    - build: "Acid Spray / Bad Karma / Shield, Damage"
      source: "[[sources/Fandom-Emz|Fandom-Emz]]"
      changes_capabilities:
        - "adds one through-wall poke cycle and stronger damage when targets stay inside the spray"
        - "trades some close-entry safety for wall-edge pressure"
      enables:
        - "Gem Fort or Open Business wall-edge denial"
        - "higher burst into grouped mid lanes"
      mitigates_failure_modes:
        - "wall_angle_denial"
      best_when: "enemy lacks immediate dive and the map has a wall edge Emz can repeatedly threaten"
      poor_when: "enemy has Edgar, Mortis, Fang, Lily, Kit, Mico, or other direct entry that demands Friendzoner"
      bp_use: "damage_variant_when_peel_is_covered"

  map_feature_hooks:
    - map_feature_type: "zone_choke_spray_and_super_slow"
      route_or_position: "Dueling Beetles four-lane entrance, Ring of Fire center bush edge, or Open Business zone wall cluster"
      uses_feature_by: "hold the edge of the zone so entrants spend time in the multi-tick spray band and Super slow"
      objective_conversion: "deny zone entry, heal through Hype during multi-body contact, and force tanks to retreat before scoring zone time"
      active_when: "enemy must walk through a choke or grass edge and lacks safe thrower/range pressure"
      fails_if: "throwers control the wall pocket, long-range lanes open the zone first, or Emz is forced to stand point-blank"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "map_bp_factors.zone_entry_denial_and_anti_aggro"
    - map_feature_type: "brawl_ball_friendzoner_goal_disarm"
      route_or_position: "Center Stage midfield grass, Sneaky Fields side-bush approach, or Triple Dribble goal-entry choke"
      uses_feature_by: "hold Friendzoner for the scorer or diver, then spray the pushed target while Super slows the recovery"
      objective_conversion: "stop ball carry, push defender/scorer off the lane, or turn a goal push into a kill window"
      active_when: "ball fight compresses into midrange and enemy has to walk through Emz rather than scoring from a dash-only angle"
      fails_if: "goal geometry still requires wallbreak, enemy baits Friendzoner, or a mobility Super re-enters immediately"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_disarm_and_anti_scorer_peel"
    - map_feature_type: "gem_mid_wide_spray_and_bush_check"
      route_or_position: "Gem Fort fort entrance, Hard Rock Mine H-bush mid, or Double Swoosh spiral side grass"
      uses_feature_by: "sweep bush edges and hold the mine approach so carriers cannot retreat through the same spray band"
      objective_conversion: "protect gem mine access, punish grouped carrier escorts, and delay countdown retreats"
      active_when: "gem route is midrange and enemies must expose themselves to collect or exit"
      fails_if: "enemy outranges from side lanes, throws over walls, or splits enough that Emz cannot cover both carrier and flank"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.mid_choke_control_and_carrier_retreat_tax"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "hold mid entrance and punish grouped gem escorts"
        - "sweep grass routes with wide spray"
      cannot_fulfill:
        - "solo long-range carrier control"
        - "wall-protected thrower removal"
      needs_teammate_support:
        - "longer-range lane partner or wallbreak into thrower pockets"
      false_positive: "Emz mid control collapses if the map is opened into pure marksman sightlines"
    - mode: "Brawl Ball"
      can_fulfill:
        - "anti-scorer peel with Friendzoner"
        - "midfield clump punish and slow-based chase"
      cannot_fulfill:
        - "primary wallbreak for closed goals"
        - "dash scorer role"
      needs_teammate_support:
        - "scorer or wallbreaker that converts after Emz forces defenders back"
      false_positive: "anti-aggro value does not automatically solve closed goal geometry"
    - mode: "Heist"
      can_fulfill:
        - "conditional safe pressure when modifiers or map geometry keep defenders in spray"
        - "safe-defense anti-entry against short-range attackers"
      cannot_fulfill:
        - "primary stable safe DPS on open lanes"
        - "race plan without a dedicated safe hitter"
      needs_teammate_support:
        - "true safe DPS or lane opener"
      false_positive: "Heist tag from PLP should be filtered through modifier, safe approach, and enemy range"
    - mode: "Hot Zone"
      can_fulfill:
        - "deny zone entrances with spray and slowing Super"
        - "heal through multi-target fights with Hype"
      cannot_fulfill:
        - "tank body standing alone without teammate pressure"
        - "thrower pocket clear from safety"
      needs_teammate_support:
        - "body or wallbreak teammate when enemies attack from behind cover"
      false_positive: "zone control is strong only if Emz reaches the zone edge before being outranged"

  failure_modes:
    - id: "point_blank_deadzone_after_peel_spent"
      active_when: "assassin or tank reaches Emz after Friendzoner and Super are spent or baited"
      exposed_by: "Fandom notes her close-range weakness and Friendzoner as the cover tool"
      mitigation: "hold gadget for real entry, draft peel, or keep enough midrange space"
      bp_use: "anti_aggro_resource_gate"
    - id: "long_range_or_thrower_outspace"
      active_when: "enemy uses Bea, 8-Bit, Grom, Larry & Lawrie, or similar range/wall pressure"
      exposed_by: "PLP counter list and Emz's 6.67 range"
      mitigation: "add wallbreak, lane partner, or avoid open/wall-heavy maps"
      bp_use: "must_answer_before_locking_emz"
    - id: "slow_reload_ammo_exhaustion"
      active_when: "Emz sprays early at max range, misses the 3-tick band, or must cover multiple entrances"
      exposed_by: "2s reload and tick-position damage pattern"
      mitigation: "hold shots for choke timing and pair with teammate slow/stun or body pressure"
      bp_use: "candidate_eval.ammo_and_route_compression"
    - id: "heist_primary_dps_false_positive"
      active_when: "draft expects Emz to race safe damage on open Heist lanes"
      exposed_by: "Fandom tips frame high Heist value as modifier-dependent rather than a stable role"
      mitigation: "use as anti-entry lane or modifier-specific pick with a true safe DPS"
      bp_use: "false_positive_filter_for_heist_pick"

  conditional_matchup_seeds:
    - target:
        - "Jae-Yong"
        - "Shelly"
        - "Gale"
        - "Meg"
        - "Doug"
      direction: "subject_favored"
      source: "[[sources/PLP-Emz|PLP-Emz]]"
      mechanism: "midrange spray, Super slow, and Friendzoner punish bulky or close-objective bodies before they can stay on the goal, zone, or mine"
      active_when: "objective requires walking through Emz's spray band and she has peel resources available"
      fails_when: "target outranges first, baits Friendzoner, or reaches point-blank with mobility still available"
      bp_use: "response_pick_candidate_against_close_or_body_pressure"
    - target:
        - "Squeak"
        - "Glowy"
        - "Brock"
      direction: "volatile"
      source: "[[sources/PLP-Emz|PLP-Emz]]"
      mechanism: "Emz can punish these targets when map geometry forces them into midrange, but wall or long-lane control can reverse the lane"
      active_when: "their lane must contest a choke, ball lane, or zone edge inside 6.67 tiles"
      fails_when: "they keep safe wall or long-range angles and Emz lacks Acid Spray or wallbreak support"
      bp_use: "map_geometry_lane_check"
    - target:
        - "Gray"
        - "Ollie"
        - "Sam"
        - "Bolt"
      direction: "target_favored"
      source: "[[sources/PLP-Emz|PLP-Emz]]"
      mechanism: "teleport, direct engage, or bursty route compression can bypass the preferred spray band and force Emz to spend peel before damage converts"
      active_when: "map has side cover, wall route, or objective pressure that lets them choose first contact"
      fails_when: "Emz holds Friendzoner/Super for the actual entry and teammates cover the second angle"
      bp_use: "avoid_or_require_peel_layer"
    - target:
        - "Larry & Lawrie"
        - "Bea"
        - "8-Bit"
        - "Grom"
      direction: "target_favored"
      source: "[[sources/PLP-Emz|PLP-Emz]]"
      mechanism: "longer range, wall arcs, or sustained DPS can damage Emz before she reaches her spray band"
      active_when: "walls or open lanes let them attack without stepping into the lingering cloud"
      fails_when: "terrain or teammate pressure forces them into midrange and Emz has enough ammo for the choke"
      bp_use: "must_answer_range_or_thrower_pressure"

  slot_notes:
    slot_1: "reasonable only on clear zone/ball/gem choke maps where long-range and thrower counters are already constrained"
    slot_2_3: "strong response after enemy shows close-range bodies or scorers that must enter midrange"
    slot_4_5: "use to patch anti-aggro and zone denial, while checking for open slot_6 thrower or marksman punish"
    slot_6: "excellent into drafts with no wall/range answer and multiple targets that must walk through spray"
```
