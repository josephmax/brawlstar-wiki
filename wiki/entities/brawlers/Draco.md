# Draco

## 基本信息

- 稀有度：Legendary
- 定位：Tank
- 类型：变身前压 / 驻点坦克 / 近中距离压线

## 来源摘要

- Fandom：[[sources/Fandom-Draco|Fandom 来源摘要: Draco]]
- PLP：[[sources/PLP-Draco|PLP 来源摘要: Draco]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Hot Zone

## 角色定位总结

Draco 的 BP 价值来自“先用短中距离穿透和受击充能建立 Super，再用 Dragon Solo 的移速、护盾和持续火焰把路口或目标区顶开”。他不是开放长线图的通用坦克；一旦缺少掩体、队友清场或 Super 进场窗口，容易被远程、击退和 anti-tank 爆发反制。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "short_mid; Lance Stab range 4, with double damage and doubled Super charge in the last 30% of the range"
    projectile_reliability: "medium_in_funnel_low_in_open; piercing Lance Stab rewards apex spacing, while Dragon Solo wants mid-close cone access"
    burst: "medium_high_after_transform; close Dragon Solo flame stream plus Damage gear can finish clustered targets"
    sustained_dps: "high_while_dragon_ammo_bar_active; very fast reload, 50% ammo refund on Super, and auto-reloading dragon ammo bar"
    objective_damage: "medium; PLP modes emphasize Gem Grab, Brawl Ball, and Hot Zone body pressure rather than safe-race damage"
    mobility: "conditional_high; Dragon Solo grants 20% speed and Hypercharge extends both speed and range"
    survivability: "very_high; 5600 health, 20% shield in Dragon Solo, Last Stand, and Shredding heal"
    engage: "high_with_Super_or_Last_Stand; can cross a choke after Super is active or use Last Stand to absorb a key focus window"
    disengage: "low_medium; Upper Cut can be an escape build, but PLP default gives up that hard interrupt for Last Stand"
    anti_aggro: "medium_high; high health, Last Stand, optional Upper Cut, and close cone damage punish direct entries"
    anti_tank: "high_if_spacing_or_dragon_active; Fandom strategy frames Draco as strong into tanks and close-ranged Brawlers"
    wall_break: low
    throw_or_wall_bypass: low
    area_control: "medium_high; dragon cone and body presence can deny a lane or zone entrance"
    scouting_or_vision: "medium; Fandom tips recommend checking bushes with Lance Stab apex damage before walking in"
    team_support: "medium; meat-shielding, lane cover, and optional Expose mark support teammate damage"
    spawnable_or_pet: low
    crowd_control: "medium_if_Upper_Cut_is_selected; PLP default Last Stand build has no hard CC"
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Draco|Fandom-Draco]]"
      - "[[sources/PLP-Draco|PLP-Draco]]"

  build_switches:
    - build: "Last Stand / Shredding / Speed, Damage"
      source: "[[sources/PLP-Draco|PLP-Draco]]"
      changes_capabilities:
        - "Last Stand lets Draco absorb a 2-second focus window and still charges Trait from would-be damage"
        - "Shredding heals when Dragon Solo completes, supporting repeated form cycles and zone re-entry"
        - "Speed gear improves grass and choke entry; Damage gear raises the close-range cone threat once Draco is already committed"
      enables:
        - zone_body_entry
        - brawl_ball_lane_pressure
        - gem_side_bush_check_and_bodyguard
      mitigates_failure_modes:
        - open_entry_focus_fire
        - dragon_cycle_sustain
      best_when: "map has grass, walls, or a forced objective lane where Draco can reach mid-close range"
      poor_when:
        - "enemy can kite from open long range or hold knockback/stun for the 0.5-second Super delay"
        - "Last Stand is activated while carrying the Brawl Ball, because Draco cannot hold the ball during the Gadget"
      bp_use: default_reviewed_build_for_zone_body_and_ball_lane_pressure
    - build: "Upper Cut / Expose pressure variant"
      source: "[[sources/Fandom-Draco|Fandom-Draco]]"
      changes_capabilities:
        - "Upper Cut gives a 1-second launch on the next Lance Stab, useful as peel or escape, but airborne enemies are immune to most damage"
        - "Expose can mark a target for 35% increased incoming damage for 5 seconds"
      enables:
        - peel_against_single_entry
        - focus_fire_mark
      mitigates_failure_modes:
        - hard_commit_without_interrupt
      poor_when:
        - "the team needs Last Stand's body window to enter zone or score lane"
      bp_use: situational_build_if_team_needs_peel_or_focus_mark

  map_feature_hooks:
    - map_feature_type: "zone_body_dragon_sustain"
      uses_feature_by: "Draco uses high health, Last Stand, Dragon Solo shield/speed, and Shredding heal to stand in or force through a Hot Zone entrance"
      route_or_position: "single-zone entrance, center grass edge, or wall-adjacent approach where enemies must fight through Draco's body"
      objective_conversion: "stand on zone, force defenders out of the entry, or buy time for an area-control teammate to stabilize"
      active_when: "Draco has Super or Last Stand timing and teammates can cover thrower or anti-tank fire"
      fails_if: "enemy clears from behind walls, chains knockback/stun during the Super delay, or applies damage-over-time that kills after Last Stand ends"
      example_maps:
        - Dueling Beetles
        - Ring of Fire
        - Open Business
      bp_use: candidate_eval.zone_body_with_cc_and_dot_filter
    - map_feature_type: "brawl_ball_mid_close_push"
      uses_feature_by: "Dragon Solo speed and cone pressure let Draco drive defenders off the ball lane while teammates convert the opening"
      route_or_position: "center grass, side bush lane, or goal approach where Draco can enter mid-close range before open-field kiting starts"
      objective_conversion: "clear a defender, escort a scorer, or turn a forced retreat into a scoring window"
      active_when: "team has a scorer, wallbreak, stun, or passing plan and Draco can pass before using Last Stand"
      fails_if: "Draco must carry while Last Stand is active, the goal remains closed with no scorer, or enemy knockback resets the push"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_lane_bodyguard_and_score_window_support
    - map_feature_type: "bush_apex_check_and_gem_side_pressure"
      uses_feature_by: "Lance Stab pierces and deals double damage at the range apex, letting Draco check bushes before using body pressure to guard side lanes"
      route_or_position: "Gem Grab side grass, center entrance, or fort choke where enemies must reveal before reaching the carrier"
      objective_conversion: "protect the gem carrier's retreat, force enemy side lane back, or build Super while denying ambush space"
      active_when: "map has grass/choke routes and Draco is not asked to play a pure open mid marksman role"
      fails_if: "grass is removed, enemy controls open range, or Draco cannot build Super before the countdown fight"
      example_maps:
        - Double Swoosh
        - Hard Rock Mine
        - Gem Fort
      bp_use: map_bp_factors.grass_check_and_side_body_pressure

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - side_lane_bodyguard
        - bush_check_before_carrier_retreat
        - choke_entry_pressure_after_Super
      cannot_fulfill:
        - primary_open_mid_gem_carrier
        - safe_long_range_control
      needs_teammate_support:
        - reliable mid or carrier
        - thrower or wall control answer if center is locked
      false_positive: "PLP lists Gem Grab, but Draco should be a side/bodyguard plan, not the team's only gem control."
    - mode: "Brawl Ball"
      can_fulfill:
        - lane_push_after_dragon_form
        - defender_displacement_by_body_pressure
        - scorer_escort
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - Last_Stand_ball_carry
      needs_teammate_support:
        - scoring finisher or wallbreak
        - anti_knockback_or_control follow-up
      false_positive: "Draco can create pressure, but Last Stand explicitly prevents ball holding during the Gadget."
    - mode: "Hot Zone"
      can_fulfill:
        - zone_body
        - entry_denial_with_dragon_cone
        - damage_absorption_for_teammate_area_control
      cannot_fulfill:
        - long_range_zone_clear_from_outside
        - thrower_pocket_answer_by_himself
      needs_teammate_support:
        - thrower clear, wallbreak, or anti-tank support
        - teammate damage once Draco forces defenders to move
      false_positive: "High survivability fails if the enemy can keep Draco out of the zone with CC or wall-protected damage."

  failure_modes:
    - id: "open_long_range_kiting"
      active_when: "map is open and enemy can hold Draco outside Lance Stab apex or Dragon Solo cone range"
      exposed_by: "[[sources/Fandom-Draco|Fandom-Draco]] tips noting he struggles against long-range Brawlers unless close"
      mitigation: "draft him on grass, chokes, or objective lanes with speed/cover support"
      bp_use: false_positive_filter
    - id: "super_delay_cancel"
      active_when: "enemy holds stun, knockback, or pull for the 0.5-second Dragon Solo delay"
      exposed_by: "[[sources/Fandom-Draco|Fandom-Draco]] Super section says transformation can be canceled during the delay"
      mitigation: "bait CC first, enter after teammate control, or avoid late-pick into stacked interrupts"
      bp_use: must_answer_cc_before_draco_plan
    - id: "last_stand_dot_and_ball_lockout"
      active_when: "Draco relies on Last Stand into poison/burn/status damage or tries to carry the ball during the Gadget"
      exposed_by: "[[sources/Fandom-Draco|Fandom-Draco]] Last Stand notes damage-over-time risk and Brawl Ball holding restriction"
      mitigation: "use Last Stand after passing or as a body screen, and avoid relying on it into persistent damage"
      bp_use: build_failure_filter
    - id: "low_value_without_super_cycle"
      active_when: "Draco cannot take or deal enough damage to charge Super before the decisive fight"
      exposed_by: "[[sources/Fandom-Draco|Fandom-Draco]] Trait and attack charge mechanics"
      mitigation: "pick into objective fights that naturally feed his Trait or pair with lane control that lets him hit apex stabs"
      bp_use: candidate_eval.super_cycle_requirement

  conditional_matchup_seeds:
    - target:
        - "Squeak"
        - "Meeple"
        - "Sprout"
        - "Gray"
      direction: "subject_favored"
      source: "[[sources/PLP-Draco|PLP-Draco]]"
      mechanism: "Last Stand plus Dragon Solo lets Draco cross a controlled choke and then use cone pressure or body presence to force wall/control picks off the objective."
      active_when: "map has a choke, grass route, or zone/ball objective that makes the target hold ground instead of freely kiting"
      fails_when: "target sits in a deeper thrower pocket, Draco's Super delay is interrupted, or the map is open enough to kite before entry"
      bp_use: response_pick_seed_against_control_pocket
    - target:
        - "Lily"
        - "Kenji"
        - "Melodie"
        - "Stu"
      direction: "subject_favored"
      source: "[[sources/PLP-Draco|PLP-Draco]]"
      mechanism: "High health, damage reduction, Last Stand, and close Dragon Solo damage can absorb a direct engage and punish mobile short-range threats after they commit."
      active_when: "the fight happens in a lane funnel or objective area and Draco has Super, Last Stand, or teammate control online"
      fails_when: "the mobile target baits Last Stand, dodges the dragon cone, or escapes into open space before Draco refreshes pressure"
      bp_use: anti_aggro_or_bruiser_response_seed
    - target:
        - "Maisie"
        - "8-Bit"
        - "Shelly"
        - "Clancy"
        - "Gale"
      direction: "target_favored"
      source: "[[sources/PLP-Draco|PLP-Draco]]"
      mechanism: "Anti-tank burst, sustained lane DPS, knockback, or slow can keep Draco outside cone range or cancel his Super timing before he converts health into objective pressure."
      active_when: "map gives these targets open lines, defensive walls, or a predictable Draco entry route"
      fails_when: "Draco reaches with cover, baits the key knockback, or has teammate control that forces them into his close range"
      bp_use: avoid_first_pick_or_require_entry_support
    - target:
        - "Doug"
        - "Darryl"
        - "Nita"
      direction: "target_favored"
      source: "[[sources/PLP-Draco|PLP-Draco]]"
      mechanism: "Bulk, revive/sustain, spawnable body pressure, or close-range burst can outlast Draco's dragon window and punish him once Last Stand or Shredding is spent."
      active_when: "objective forces repeated close fights and Draco lacks teammate DPS to finish the target during his form"
      fails_when: "Draco controls the route first, gets Expose/team focus damage, or avoids fighting the tank mirror as the primary win condition"
      bp_use: lane_execution_and_slot_6_check

  slot_notes:
    slot_1: "acceptable only on closed Hot Zone or Brawl Ball maps where zone body or lane pressure is a core duty and bans protect against stacked knockback/anti-tank"
    slot_2_3: "stronger as a plan-building pick after confirming the map rewards body pressure and the team has scorer, mid, or thrower-clear support"
    slot_4_5: "use to punish drafts that lack open-range kiting or CC; avoid if enemy still has an obvious Maisie/Gale/Shelly-style answer"
    slot_6: "best as a last response into control pockets or mobile aggro that must fight Draco in a choke, with Last Stand timing already mapped"
```

## 关联页面

- [[sources/Fandom-Draco|Fandom 来源摘要: Draco]]
- [[sources/PLP-Draco|PLP 来源摘要: Draco]]
