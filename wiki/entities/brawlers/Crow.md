# Crow

## 基本信息

- 稀有度：Legendary
- 定位：Assassin
- 类型：中距离毒伤刺客

## 攻击特征

- 主攻击是三发长距离匕首
- 命中后会附带中毒效果
- 擅长持续削血和抑制回复

## 超级技能特征

- Super 会跳跃切入或脱离战斗
- 起落都会投出匕首，形成额外压制
- 既能追杀低血量目标，也能快速撤退

## 适合场景

- 需要持续骚扰和反治疗的对局
- 适合追击残血和残局收割
- 中远距离拉扯多、草丛较多的地图

## 角色定位总结

Crow 是最典型的毒伤消耗型刺客。和 `Leon` 比，他不依赖隐身爆发，而是靠持续中毒慢慢把敌人逼出节奏；和 `Spike` 比，他更像削血工具而不是范围爆发工具。

## 关联页面

- [[sources/Fandom-Crow|Fandom 来源摘要: Crow]]
- [[sources/PLP-Crow|Power League Prodigy 来源摘要: Crow]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "long_mid; 8.67-tile three-dagger spread lets him poke, reveal, and kite from outside many bruiser ranges"
    projectile_reliability: "medium_high_for_tagging; one dagger is easy to apply for poison/vision, while full damage requires closer angle or target movement into spread"
    burst: "medium_with_Carrion_or_Super; base poke is low, Carrion Crow improves execution below 50%, and Super burst requires landing on target"
    sustained_dps: "medium_chip_high_tempo; fast reload keeps poison refreshed but raw damage per hit is low"
    objective_damage: "low_medium; PLP lists Heist, but Crow contributes lane attrition, defender anti-heal, and slow windows rather than primary safe race"
    mobility: "high; very fast movement, Super jump engage/escape, and air immunity create reposition and cleanup windows"
    survivability: "low_by_health_medium_with_tools; 3000 health is fragile, while Shield gear, Instapoison shield, Super escape, and Extra Toxic reduce burst risk"
    engage: "conditional_cleanup; jumps are strong into low-health or slowed targets, weak as blind initiation"
    disengage: "high_with_Super_or_slow; Super escapes pressure and Slowing Toxin can stop chase routes"
    anti_aggro: "medium_high_with_slow_or_Extra_Toxic; poison damage debuff and 30% slow punish divers before contact"
    anti_tank: "high_as_kite_and_anti_heal; poison prevents healing, Extra Toxic reduces damage, and Slowing Toxin delays close-range entries"
    wall_break: low
    throw_or_wall_bypass: "low_medium; Super jumps over obstacles but main pressure still needs line of sight"
    area_control: "medium; poison denies natural regeneration, makes bush hiding unsafe, and slows objective re-entry with Gadget"
    scouting_or_vision: "high; poison reveals enemies in bushes and extends the time before they can safely heal or hide"
    team_support: "medium_high_indirect; anti-heal, damage debuff, reveal, and slow increase teammate conversion windows"
    spawnable_or_pet: low
    crowd_control: "medium; Slowing Toxin is a 2-second single-target slow and Extra Toxic lowers poisoned enemy damage"
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Crow|Fandom-Crow]]"
      - "[[sources/PLP-Crow|PLP-Crow]]"

  build_switches:
    - build: "Instapoison / Carrion Crow / Shield, Damage"
      source: "[[sources/PLP-Crow|PLP-Crow]]"
      changes_capabilities:
        - "Instapoison cashes out poison damage and converts it into a decaying shield for a safer dive or escape"
        - "Carrion Crow raises dagger and poison damage against targets at or below 50% health"
        - "Shield and Damage gears offset low health and improve kill confirmation after chip"
      enables:
        - low_health_cleanup
        - poison_chip_to_finish
        - shielded_super_entry
        - anti_heal_lane_pressure
      mitigates_failure_modes:
        - low_health_all_in
        - chip_without_conversion
        - weak_burst_against_retreating_targets
      best_when: "team can bring targets below half and map gives Crow repeated safe tags or cleanup jumps"
      poor_when:
        - "enemy has longer range, spawnables, or wall pockets that stop Crow from tagging priority targets"
        - "team needs hard zone body, wallbreak, or primary objective damage"
      bp_use: default_reviewed_build_for_chip_and_cleanup
    - build: "Slowing Toxin / Extra Toxic variant"
      source: "[[sources/Fandom-Crow|Fandom-Crow]] / [[sources/PLP-Crow|PLP-Crow]]"
      changes_capabilities:
        - "Slowing Toxin adds a 30% slow, extra poison, anti-heal, and with Buffie can bounce to nearby targets"
        - "Extra Toxic reduces poisoned enemy damage by 15%, improving team survival into high-damage or tank entries"
      enables:
        - anti_aggro_peel
        - tank_kiting
        - grouped_objective_slow
        - team_damage_reduction
      mitigates_failure_modes:
        - close_range_assassin_pressure
        - tank_reaches_lane
        - grouped_zone_or_ball_entry
      best_when: "enemy draft relies on tanks, divers, healers, or grouped objective entries"
      poor_when:
        - "enemy is pure long-range poke that outranges Crow before he can tag"
      bp_use: situational_variant_into_aggro_sustain_or_grouped_entries

  map_feature_hooks:
    - map_feature_type: "poison_vision_and_carrier_retreat_tax"
      uses_feature_by: "poison reveals bush targets, delays natural healing, and forces carriers to retreat earlier"
      route_or_position: "Gem Grab side grass, center spiral bushes, open mid H bushes, or Hot Zone center bush mass"
      objective_conversion: "protect gem carrier retreat, reveal flank pressure, and stop hidden enemies from healing before a countdown or zone fight"
      active_when: "map rewards bush scouting and Crow can tag enemies without overcommitting into thrower or sniper range"
      fails_if: "grass is burned, walls block repeated tags, or enemy outranges Crow on the route"
      example_maps:
        - Double Swoosh
        - Hard Rock Mine
        - Gem Fort
        - Ring of Fire
      bp_use: map_bp_factors.vision_tax_and_retreat_denial
    - map_feature_type: "anti_heal_slow_zone_entry"
      uses_feature_by: "poison halves healing, Extra Toxic lowers damage, and Slowing Toxin punishes the first body entering a grouped objective route"
      route_or_position: "single-zone entrance, grass entry, wall-adjacent zone edge, or midfield ball fight"
      objective_conversion: "delay zone re-entry, reduce tank damage during a push, or create a teammate finish window on slowed targets"
      active_when: "enemy plan needs healing, grouped entry, or close-range bodies to walk through a predictable lane"
      fails_if: "enemy controls from behind a wall, spreads across lanes, or Crow is forced to stand on zone as the main body"
      example_maps:
        - Dueling Beetles
        - Ring of Fire
        - Open Business
        - Center Stage
      bp_use: candidate_eval.anti_heal_and_slow_support
    - map_feature_type: "jump_score_or_cleanup_window"
      uses_feature_by: "Super can jump over defenders, self-pass in Brawl Ball, or land on a poisoned low-health target"
      route_or_position: "midfield ball lane, side-bush scoring path, or exposed low-health backline after poke"
      objective_conversion: "turn chip damage into a kill, retrieve a self-pass, or bypass a short defender for a score attempt"
      active_when: "target is below half, slowed, or isolated and Crow still has enough health or shield to survive landing"
      fails_if: "enemy holds knockback/burst, target is behind multiple teammates, or goal geometry remains closed"
      example_maps:
        - Sneaky Fields
        - Center Stage
        - Triple Dribble
        - Flaring Phoenix
      bp_use: slot_task.cleanup_or_scorer_support
    - map_feature_type: "heist_lane_attrition_not_primary_dps"
      uses_feature_by: "long-range poison, slow, and anti-heal can win a lane and stop defenders from resetting"
      route_or_position: "isolated lane, center grass approach, or safe-defense lane where Crow can repeatedly tag without crossing into burst range"
      objective_conversion: "convert lane chip into safe access for a DPS teammate or deny enemy short-range safe entry"
      active_when: "team already has safe DPS and Crow's job is lane control, anti-heal, and anti-aggro defense"
      fails_if: "draft expects Crow to be the main safe damage source or enemy wins with longer range/cross-lane DPS"
      example_maps:
        - Bridge Too Far
        - Kaboom Canyon
        - Hot Potato
      bp_use: false_positive_filter_for_heist_crow

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - bush_reveal_for_carrier_safety
        - anti_heal_mid_chip
        - low_health_cleanup_after_countdown_pressure
      cannot_fulfill:
        - primary_gem_carrier_into_long_range_focus
        - hard_mid_body
      needs_teammate_support:
        - durable carrier or mid control teammate
        - wallbreak/thrower answer if enemies hide behind pockets
      false_positive: "Poison can reveal and delay, but Crow's low health makes him a poor solo carrier when the enemy has long-range focus."
    - mode: "Brawl Ball"
      can_fulfill:
        - slowed_or_poisoned_defender_cleanup
        - self_pass_super_score_window
        - anti_tank_ball_lane_kiting
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - primary_frontline_body
      needs_teammate_support:
        - scorer, wallbreak, or knockback teammate
        - peel after Crow spends Super aggressively
      false_positive: "Crow can create or finish a score window; he does not solve closed goals or front-line holding by himself."
    - mode: "Heist"
      can_fulfill:
        - lane_attrition_and_anti_heal
        - defender_slow_for_safe_dps_teammate
        - anti_short_range_safe_entry
      cannot_fulfill:
        - primary_safe_race_damage
        - cross_map_long_range_dps_role
      needs_teammate_support:
        - true safe DPS teammate
        - lane winner that converts poisoned defenders into safe hits
      false_positive: "Heist Crow is a control/defense layer; drafting him as the sole race tool is a trap."
    - mode: "Hot Zone"
      can_fulfill:
        - anti_heal_zone_edge
        - slow_first_entry
        - bush_reveal_around_zone
      cannot_fulfill:
        - main_zone_body
        - thrower_wall_pocket_clear
      needs_teammate_support:
        - durable zone holder
        - area clear or wallbreak against pocket control
      false_positive: "Crow helps win the edge of the zone; he still needs teammates to occupy and clear the circle."

  failure_modes:
    - id: "low_health_pressure"
      active_when: "enemy can force close-range contact before Crow has Super, Gadget, or teammate peel"
      exposed_by: "[[sources/Fandom-Crow|Fandom-Crow]] low health and strategy warning about assassins at close range"
      mitigation: "play at max tag range, pair with anti-aggro teammate, or choose Slowing Toxin/Extra Toxic"
      bp_use: avoid_as_unprotected_first_pick_into_dive
    - id: "outranged_open_map"
      active_when: "enemy snipers or high-damage long-range picks hold open lanes and Crow cannot safely apply poison"
      exposed_by: "[[sources/Fandom-Crow|Fandom-Crow]] tips naming Brock, Piper, Colt, Mandy, 8-Bit, Rico, Amber, Bea, and Nani on open maps"
      mitigation: "draft Crow on bush/route maps or after bans remove long-lane punishers"
      bp_use: map_openness_filter
    - id: "chip_without_objective_conversion"
      active_when: "Crow repeatedly poisons targets but team lacks a scorer, safe DPS, zone body, or finisher"
      exposed_by: "[[sources/Fandom-Crow|Fandom-Crow]] low damage output and PLP mode list requiring objective context"
      mitigation: "pair with burst, carrier, frontliner, or safe DPS depending on mode"
      bp_use: team_comp_conversion_check
    - id: "spawnable_or_wall_pocket_tax"
      active_when: "enemy spawnables, porters, turrets, or thrower pockets absorb Crow's low damage and block priority tags"
      exposed_by: "[[sources/PLP-Crow|PLP-Crow]] target-favored list with Mr. P, Nita, Jessie, Tick and [[sources/Fandom-Crow|Fandom-Crow]] low damage profile"
      mitigation: "add wallbreak, splash, or a teammate that clears bodies before relying on poison pressure"
      bp_use: must_answer_summons_or_throwers

  conditional_matchup_seeds:
    - target:
        - "Byron"
        - "Pam"
      direction: "subject_favored"
      source: "[[sources/PLP-Crow|PLP-Crow]] / [[sources/Fandom-Crow|Fandom-Crow]]"
      mechanism: "Poison halves healing and delays natural regeneration, making healer or sustain shells lose tempo before objective contact."
      active_when: "fight is repeated poke around gem, zone, or ball objective and Crow can keep at least one poison tag active"
      fails_when: "healer's team hard-engages before poison accumulates or Crow cannot tag through walls/spawnables"
      bp_use: response_pick_seed_against_heal_or_sustain
    - target:
        - "Leon"
        - "Shelly"
        - "Bull"
        - "Max"
        - "Amber"
        - "Squeak"
      direction: "subject_favored"
      source: "[[sources/PLP-Crow|PLP-Crow]]"
      mechanism: "Long tag range, reveal, anti-heal, slow, and Super cleanup punish targets that rely on hiding, short-range entry, or post-chip retreat."
      active_when: "Crow has space to kite, target must cross visible grass/choke, and Slowing Toxin or Carrion converts a low-health window"
      fails_when: "target reaches close range without Crow Super, outranges him, or has a teammate body blocking the landing"
      bp_use: lane_pressure_or_cleanup_response_seed
    - target:
        - "Lola"
        - "Spike"
        - "Mr. P"
        - "Nita"
        - "Tick"
        - "Jessie"
        - "Tara"
        - "Pearl"
      direction: "target_favored"
      source: "[[sources/PLP-Crow|PLP-Crow]]"
      mechanism: "Spawnables, wall-control, area damage, or steadier mid-range DPS can absorb poison tags and punish Crow's low health before he converts chip."
      active_when: "map has walls, turret/bear/porter value, or grouped objective fights where Crow cannot isolate a low-health target"
      fails_when: "Crow has wallbreak/splash teammate support, tags the controller before setup, or Super cleans the key target after chip"
      bp_use: must_answer_bodies_and_pockets_before_crow_plan
    - target:
        - "Mortis"
        - "Mico"
        - "Buzz"
        - "Stu"
        - "Cordelius"
        - "Edgar"
      direction: "target_favored"
      source: "[[sources/Fandom-Crow|Fandom-Crow]]"
      mechanism: "High-mobility assassins can bypass Crow's poke range and force a close duel where his low health loses without Super, slow, or teammate peel."
      active_when: "they have grass, wall, dash, or jump route and Crow's Super/Gadget is unavailable"
      fails_when: "Crow tags early, slows the entry, keeps Super as escape, or plays grouped with close-range peel"
      bp_use: anti_aggro_resource_check

  slot_notes:
    slot_1: "acceptable only when map rewards poison vision/anti-heal and bans protect him from long-range or hard dive punishment."
    slot_2_3: "good into early sustain, tank, or bush-control plans if the team already has objective conversion."
    slot_4_5: "use to add anti-heal, reveal, and slow after seeing enemy front line, while keeping a final slot for body or damage."
    slot_6: "punishes drafts that lack long-range answer, cleanse, spawnable tax, or a way to stop a slowed low-health cleanup jump."
```
