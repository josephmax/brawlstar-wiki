# Clancy

## 基本信息

- 稀有度：Mythic
- 定位：Damage Dealer
- 类型：阶段成长型输出英雄

## 攻击特征

- 主攻击会随着阶段提升而增加子弹数
- 前期火力较弱，后期会明显增强
- 更适合通过持续命中滚出优势

## 超级技能特征

- Super `Torrent` 也会随阶段成长
- 阶段越高，覆盖和伤害都越强
- 让 Clancy 在成长完成后具备很高的团战威胁

## 适合场景

- 能稳定打出命中的模式
- 中后期团战会越打越强的局面
- 需要先发育再接管战场的对局

## 角色定位总结

Clancy 是靠命中积累 token、逐阶段成长的输出英雄，前期要忍，后期会变得非常强势。

## 关联页面

- [[sources/Fandom-Clancy|Fandom 来源摘要: Clancy]]
- [[sources/PLP-Clancy|Power League Prodigy 来源摘要: Clancy]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "long_mid; 7.67-tile main attack and Stage 2+ Super range let Clancy contest mid lanes after token ramp"
    projectile_reliability: "stage_dependent; Stage 1 is narrow single shot, Stage 2 adds a second shot, Stage 3 adds diagonal bullets for wider coverage"
    burst: "very_high_after_stage_3_super; Torrent can deliver heavy cone damage, while early Stage 1 burst is weak"
    sustained_dps: "ramp_dependent; 2s reload is slow, but Pumping Up reloads all ammo on takedown and Stage upgrades multiply shot count"
    objective_damage: "conditional; Fandom notes Stage 3 Super can heavily damage safe, but PLP's recommended modes are Gem Grab, Brawl Ball, and Hot Zone"
    mobility: "medium_after_stage_3; normal speed early, +100 speed at Stage 3, and Tactical Retreat offers a short dash/reload variant"
    survivability: "medium_low; 3800 health and Shield/Speed gear help, but early Clancy is punishable before tokens"
    engage: "medium; he prefers farming hits and punishing forced entries rather than starting fights from nothing"
    disengage: "medium_with_tactical_retreat_variant; default build relies more on speed and damage pressure"
    anti_aggro: "high_after_super_or_stage_2; Snappy Shooting plus Super can rapidly farm tanks/assassins into Stage 3"
    anti_tank: "high_if_token_window_exists; PLP positive list is mostly bulky or close-route targets that feed his scaling"
    wall_break: low
    throw_or_wall_bypass: low
    area_control: "high_after_stage_3; wide attack pattern and Super cone control clustered entrances and zones"
    scouting_or_vision: low
    team_support: "low_direct; Clancy contributes damage and area denial rather than buffs"
    spawnable_or_pet: low
    crowd_control: low
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Clancy|Fandom-Clancy]]"
      - "[[sources/PLP-Clancy|PLP-Clancy]]"

  build_switches:
    - build: "Snappy Shooting / Pumping Up / Shield, Speed, Damage"
      source: "[[sources/PLP-Clancy|PLP-Clancy]]"
      changes_capabilities:
        - "Snappy Shooting doubles token gain for 5 seconds, turning early contact or tank entry into faster Stage 2/3 access"
        - "Pumping Up reloads all ammo on takedown, letting Clancy chain pressure after a confirmed kill"
        - "Shield improves early survival, Speed helps on grass maps, and Damage raises conversion once he is safe"
      enables:
        - token_ramp
        - anti_tank_scaling
        - zone_and_ball_clump_punish
      mitigates_failure_modes:
        - early_stage_1_weakness
        - slow_reload_after_kill
      best_when: "map has repeated objective contact, grouped entries, or short-range bodies that feed tokens without instantly killing Clancy"
      poor_when:
        - "enemy can split, outrange, poison, or control Clancy before he farms Stage 2"
        - "team needs immediate first-wave control and cannot wait for token ramp"
      bp_use: default_reviewed_build_for_scaling_damage
    - build: "Tactical Retreat / Recon variants"
      source: "[[sources/Fandom-Clancy|Fandom-Clancy]]"
      changes_capabilities:
        - "Tactical Retreat dashes 3.33 tiles and reloads 1 ammo, but is canceled by stun, pull, or knockback and cannot cross walls/water"
        - "Recon starts the match with 2 tokens, reducing early ramp time"
      enables:
        - emergency_reposition
        - faster_stage_2_timing
      mitigates_failure_modes:
        - early_focus_fire
        - token_denial
      poor_when:
        - "Snappy Shooting is needed to farm tanks or objective congestion into Stage 3"
      bp_use: situational_variant_for_survival_or_early_token_floor

  map_feature_hooks:
    - map_feature_type: "long_sightline"
      uses_feature_by: "Stage 2/3 attack pattern and 7.67 range let Clancy farm tokens from mid while controlling carrier routes"
      route_or_position: "Gem Grab open mid, fort entrance, or side grass edge where enemies must contest mine access"
      objective_conversion: "turn token ramp into mid control, carrier protection, and comeback damage"
      active_when: "enemy has to contest a shared mine entrance and Clancy survives the early Stage 1 window"
      fails_if: "enemy splits lanes, denies hits from long range, or forces Clancy to retreat before Stage 2"
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Double Swoosh
      bp_use: map_bp_factors.token_farm_mid_control
    - map_feature_type: "brawl_ball_clump_punish_and_anti_tank_lane"
      uses_feature_by: "Snappy Shooting and Torrent punish tanks/scorers entering predictable grass or goal routes"
      route_or_position: "center grass fight, side bush lane, or goal-entry choke"
      objective_conversion: "stop a close-range push, farm tokens from bodies, or clear clustered defenders before a score"
      active_when: "enemy draft contains tanks/scorers and the team can survive until Clancy's damage pattern widens"
      fails_if: "goal remains closed with no scorer, Clancy is dived before Super, or throwers deny his line"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: candidate_eval.anti_tank_ball_lane
    - map_feature_type: "hot_zone_stage3_area_control"
      uses_feature_by: "Stage 3 multi-shot attack and wide Super cone punish clustered zone entrances"
      route_or_position: "single-zone choke, grass entry, or wall-adjacent zone edge"
      objective_conversion: "clear zone, deny re-entry, or snowball after first takedown with Pumping Up"
      active_when: "Clancy reaches Stage 2/3 before the zone snowball is lost and enemies must enter through predictable routes"
      fails_if: "enemy controls thrower pocket, poisons/pokes Clancy out early, or he cannot stand near zone after spending Super"
      example_maps:
        - Dueling Beetles
        - Ring of Fire
        - Open Business
      bp_use: map_factor_fit.scaling_zone_clear

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - mid_token_farm
        - carrier_route_damage
        - late_countdown_area_control
      cannot_fulfill:
        - safe_early_gem_carrier
        - thrower_pocket_clear
      needs_teammate_support:
        - early stability while Clancy reaches Stage 2
        - vision or side control on grass maps
      false_positive: "Clancy scales into mine control; drafting him as the safest early carrier is a category error."
    - mode: "Brawl Ball"
      can_fulfill:
        - anti_tank_or_scorer_damage
        - clump_punish_on_goal_entry
        - late_push_clear_after_stage_3
      cannot_fulfill:
        - primary_wallbreak_goal_opening
        - immediate_opening_ball_control_at_stage_1
      needs_teammate_support:
        - scorer or wallbreak if goal geometry is closed
        - peel during early token ramp
      false_positive: "Clancy can delete a push later; he does not solve scoring geometry by himself."
    - mode: "Hot Zone"
      can_fulfill:
        - stage_3_zone_clear
        - anti_body_damage
        - takedown_reload_snowball
      cannot_fulfill:
        - first_wave_zone_body_before_ramp
        - wall_control_clear_without_line
      needs_teammate_support:
        - zone body or control partner for opening seconds
        - thrower/wall-pocket answer
      false_positive: "If the team loses the zone before Clancy ramps, Stage 3 upside may arrive too late."

  failure_modes:
    - id: "early_stage_1_pressure_deficit"
      active_when: "the first wave decides objective control before Clancy reaches Stage 2"
      exposed_by: "[[sources/Fandom-Clancy|Fandom-Clancy]] tips describing Stage 1 as almost useless and low mobility/damage"
      mitigation: "pair with an early lane stabilizer, use Snappy Shooting efficiently, or avoid maps decided by first contact"
      bp_use: slot_and_mode_false_positive_filter
    - id: "token_denial_by_split_or_range"
      active_when: "enemy spreads lanes, outranges Clancy, or refuses grouped contact that feeds tokens"
      exposed_by: "Fandom token thresholds and PLP target-favored mobile/range list"
      mitigation: "pick Clancy where objective forces contact or draft control that holds enemies in his lane"
      bp_use: map_fit_filter
    - id: "super_direction_lock_and_wall_loss"
      active_when: "enemy moves behind Clancy or walls delete returning Hypercharge projectiles"
      exposed_by: "[[sources/Fandom-Clancy|Fandom-Clancy]] Super tips and Hypercharge wall interaction"
      mitigation: "fire Torrent from mid-range with clear tracking and avoid relying on it through tight wall clutter"
      bp_use: execution_risk_check
    - id: "low_health_control_or_poison_focus"
      active_when: "enemy CC, poison, or burst targets Clancy before he ramps or cancels Tactical Retreat"
      exposed_by: "3800 health, Tactical Retreat cancellation rules, and PLP counteredBy list"
      mitigation: "draft peel, speed/Shield support, or avoid early pick into control-heavy comps"
      bp_use: must_protect_scaling_damage

  conditional_matchup_seeds:
    - target:
        - "Sam"
        - "Rosa"
        - "Trunk"
        - "El Primo"
        - "Bibi"
        - "Damian"
        - "Bolt"
        - "Jae-Yong"
      direction: "subject_favored"
      source: "[[sources/PLP-Clancy|PLP-Clancy]]"
      mechanism: "Bulky, close-route, or objective-contact targets feed Clancy tokens and become vulnerable to Stage 2/3 cone damage."
      active_when: "objective forces repeated contact in grass, zone, ball, or mine routes and Clancy has Snappy Shooting or Stage 2 timing"
      fails_when: "target reaches him before token ramp, has hard CC, or plays through a wall pocket outside his line"
      bp_use: response_pick_seed_against_body_or_close_route
    - target:
        - "Tara"
        - "Sandy"
        - "Charlie"
        - "Meeple"
      direction: "target_favored"
      source: "[[sources/PLP-Clancy|PLP-Clancy]]"
      mechanism: "Concealment, pull/control, target removal, or rule-bending space control can deny Clancy's line and interrupt his scaling window."
      active_when: "they control the grass/choke or can spend a key control tool before Clancy reaches Stage 3"
      fails_when: "Clancy reaches Stage 3 with teammate vision/peel and they must enter his cone to contest objective"
      bp_use: must_answer_control_before_clancy_plan
    - target:
        - "Shade"
        - "Crow"
        - "8-Bit"
        - "Stu"
      direction: "target_favored"
      source: "[[sources/PLP-Clancy|PLP-Clancy]]"
      mechanism: "Mobility, poison/chip, through-wall or stat-check pressure can punish Clancy before his token state stabilizes or dodge his fixed Super direction."
      active_when: "map gives them open dodge space, wall access, or repeated poke before objective contact"
      fails_when: "Clancy farms Stage 2/3 off a frontliner first or teammates pin the target into his cone"
      bp_use: avoid_first_pick_or_require_peel

  slot_notes:
    slot_1: "risky unless map guarantees repeated contact and the team can protect Stage 1 from immediate punishment."
    slot_2_3: "good when answering early tank/body picks while pairing him with a stable opener or zone body."
    slot_4_5: "use to punish enemy 2-3 that overcommit to tanks, grouped zone entry, or grass ball pressure."
    slot_6: "strong into drafts with no poke, poison, control, or mobility left to deny Clancy's token ramp."
```
