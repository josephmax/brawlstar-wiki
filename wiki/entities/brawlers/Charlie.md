# Charlie

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：禁锢控场英雄

## 攻击特征

- 普通攻击是往返式 yo-yo
- 同一发攻击能在前进和回收时都造成伤害
- 很依赖距离、墙体和回收节奏

## 超级技能特征

- Super 会把目标包进 cocoon
- Cocoon 会让目标短时间失去行动能力
- 她的控制能力非常适合打断推进和保住关键点位

## 适合场景

- Gem Grab、Brawl Ball 这类目标型模式
- 需要打断敌方冲锋或救援关键目标的局面
- 对单个核心目标进行强控的对局

## 角色定位总结

Charlie 是靠单体禁锢和持续控场吃饭的英雄，她的价值不只是输出，而是能把一个敌人直接从战局里暂时移除。

## 与其他英雄的区别

- 不同于 `Gene`：Charlie 是禁锢目标，Gene 是拉人重排站位
- 不同于 `Lou`：Charlie 更偏硬控，Lou 更偏冰冻压区
- 不同于 `Squeak`：Charlie 更直接封锁目标行动，Squeak 更像延迟区域威胁

## 关联页面

- [[sources/Fandom-Charlie|Fandom 来源摘要: Charlie]]
- [[sources/PLP-Charlie|Power League Prodigy 来源摘要: Charlie]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "long; 9-tile yo-yo lets Charlie play lane/control, but outbound attack does not pass through walls"
    projectile_reliability: "medium_high_in_single_lane; yo-yo returns through walls and reloads faster after hitting a wall or target, but Charlie has only one ammo cycle"
    burst: "low_by_self_high_with_cocoon_followup; attack damage is low, while Cocoon creates a teammate burst window and Digestive cuts remaining health"
    sustained_dps: "cycle_dependent; close-range or wall-hit yo-yo returns faster, open-range misses leave Charlie with no ammo until return"
    objective_damage: "low; PLP lists Heist but Charlie's BP value there is defender removal or shot tanking, not stable safe DPS"
    mobility: "low; Hypercharge adds speed only during its window"
    survivability: "medium; 3700 health, Shield gear, and Personal Space self-cocoon heal can buy time"
    engage: "control_engage; Cocoon removes one enemy from the fight and lets teammates close or score"
    disengage: "medium; Cocoon or Personal Space can stop a chase and create a heal/reset window"
    anti_aggro: "very_high_if_super_available; Cocoon cancels many incoming Supers and disarms ball or gem carriers"
    anti_tank: "medium_high_with_digestive_or_followup; Cocoon delays tanks and Digestive reduces remaining health, but Charlie still needs damage support"
    wall_break: low
    throw_or_wall_bypass: "low_medium; yo-yo return goes through walls but the attack cannot be fired through walls"
    area_control: "medium; Slimy trail slows, Spiders tax ammo, and Hypercharge adds extra spiders around Cocoon"
    scouting_or_vision: "medium_high_with_spiders_and_vision_gear; spiders can follow hidden enemies and tank single-target shots"
    team_support: "high_indirect; target removal, carrier disarm, and slow trail protect teammates rather than healing them"
    spawnable_or_pet: "medium; Spiders create temporary bodies for scouting, shot tanking, and pressure"
    crowd_control: "very_high_single_target; Cocoon disables movement, attack, Super, Gadget, Hypercharge, healing, and reloading for up to 5 seconds"
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Charlie|Fandom-Charlie]]"
      - "[[sources/PLP-Charlie|PLP-Charlie]]"

  build_switches:
    - build: "Spiders / Slimy / Shield, Damage, Vision"
      source: "[[sources/PLP-Charlie|PLP-Charlie]]"
      changes_capabilities:
        - "Spiders add bush scouting, single-target shot tanking, and temporary lane pressure"
        - "Slimy leaves a 2-tile slow trail for 5 seconds along Cocoon's path, improving zone and carrier control"
        - "Shield improves low-health survivability, Damage helps convert Cocoon follow-up, and Vision supports grass-heavy maps"
      enables:
        - carrier_disarm
        - bush_scout_and_shot_tank
        - zone_entry_slow
        - anti_aggro_cocoon
      mitigates_failure_modes:
        - bush_blindness
        - single_target_lane_pressure
        - no_followup_after_cocoon
      best_when: "map rewards carrier disarm, grass checking, zone entrance control, or stopping one high-value engage"
      poor_when:
        - "enemy has thrower/splash pressure that safely breaks spiders and cocoon"
        - "team lacks burst or objective follow-up after Charlie removes one target"
      bp_use: default_reviewed_build_for_control_and_vision
    - build: "Personal Space / Digestive variants"
      source: "[[sources/Fandom-Charlie|Fandom-Charlie]] / [[sources/PLP-Charlie|PLP-Charlie]]"
      changes_capabilities:
        - "Personal Space cocoons Charlie and heals 50% of her maximum health, useful into aggressive comps"
        - "Digestive makes Cocooned enemies lose 25% of remaining health, increasing anti-tank or burst-follow-up value"
      enables:
        - self_reset_into_aggro
        - high_health_target_softening
      mitigates_failure_modes:
        - low_health_focus_fire
        - tank_survives_cocoon_release
      poor_when:
        - "the team needs spiders for bush scouting or shot tanking more than self-reset"
      bp_use: situational_variant_into_aggro_or_high_health_targets

  map_feature_hooks:
    - map_feature_type: "gem_carrier_cocoon_drop_and_spider_vision"
      uses_feature_by: "Cocoon forces Gem Grab carriers to drop gems, while spiders and Vision gear tax grass routes"
      route_or_position: "center fort entrance, open mid with H bushes, or side grass countdown route"
      objective_conversion: "turn Super into gem drop, carrier reset, or countdown comeback window"
      active_when: "enemy carrier must cross a known entrance or grass route and Charlie's team can collect or secure the dropped gems"
      fails_if: "cocoon is broken by splash before follow-up, spiders are cleared for free, or Charlie lacks mid control after spending Super"
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Double Swoosh
      bp_use: map_bp_factors.carrier_disarm_and_vision_tax
    - map_feature_type: "brawl_ball_carrier_disarm_and_goal_stall"
      uses_feature_by: "Cocoon disarms the ball carrier and can cancel incoming Supers; Charlie can also kick without consuming ammo"
      route_or_position: "midfield grass fight, side-bush push, or goal-entry lane"
      objective_conversion: "stop a scorer, buy time for defenders to reset, or remove one defender before a scoring attempt"
      active_when: "ball route is predictable and Charlie has teammate damage or scorer follow-up after the target exits Cocoon"
      fails_if: "team has no scoring window, cocoon breaks instantly, or enemy wallbreak/open-field DPS makes Charlie's low damage irrelevant"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_disarm_and_score_window_support
    - map_feature_type: "zone_entrance_slow_and_spawnable_tax"
      uses_feature_by: "Slimy slows entry routes, Spiders tax ammo, and Cocoon removes the first body stepping onto zone"
      route_or_position: "single-zone entrance, L-wall support pocket edge, or grass entry near the zone"
      objective_conversion: "delay enemy entry, force ammo before a zone fight, or isolate the main zone body"
      active_when: "zone fight is clustered around choke/grass entrances and Charlie's team can stand zone after the disarm"
      fails_if: "enemy throwers control the wall pocket, splash clears spiders and cocoon, or Charlie remains outside zone with no body teammate"
      example_maps:
        - Dueling Beetles
        - Ring of Fire
        - Open Business
      bp_use: candidate_eval.zone_entry_control_not_primary_body

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - gem_carrier_cocoon_disarm
        - side_grass_spider_scout
        - countdown_comeback_pick
      cannot_fulfill:
        - primary_mid_dps
        - solo_carrier_if_enemy_has_thrower_pressure
      needs_teammate_support:
        - damage or body to collect dropped gems
        - thrower/splash answer if cocoon breaks too easily
      false_positive: "Cocoon creates the gem drop; it does not by itself secure the mine or the retreat."
    - mode: "Brawl Ball"
      can_fulfill:
        - ball_carrier_disarm
        - anti_aggro_super_cancel
        - defender_removal_before_score
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - solo_scorer_role
      needs_teammate_support:
        - scorer, wallbreak, or burst teammate
        - grass/side-lane control to keep Charlie's line available
      false_positive: "Stopping a carrier is not the same as creating a goal unless the team can convert the tempo."
    - mode: "Hot Zone"
      can_fulfill:
        - zone_entry_slow
        - first_body_cocoon
        - spider_ammo_tax
      cannot_fulfill:
        - main_zone_body
        - thrower_pocket_clear
      needs_teammate_support:
        - durable zone body or area clear
        - wallbreak/dive into enemy thrower pocket
      false_positive: "Charlie delays and isolates; she needs a teammate who actually holds the zone."
    - mode: "Heist"
      can_fulfill:
        - defender_cocoon_for_safe_entry
        - spider_shot_tank_against_single_target_defense
      cannot_fulfill:
        - stable_safe_dps
        - wallbreak_or_remote_safe_angle
      needs_teammate_support:
        - safe DPS teammate
        - lane winner who can enter while defender is cocooned
      false_positive: "PLP lists Heist, but Charlie is a utility enabler there rather than a primary safe-damage pick."

  failure_modes:
    - id: "single_ammo_yoyo_cycle_loss"
      active_when: "Charlie misses or fires through long open space while multiple threats pressure her"
      exposed_by: "[[sources/Fandom-Charlie|Fandom-Charlie]] attack section describing one ammo that reloads only when the yo-yo returns"
      mitigation: "play around walls, forced routes, or close-cycle fights where the yo-yo returns quickly"
      bp_use: projectile_reliability_filter
    - id: "cocoon_broken_or_splash_saves_target"
      active_when: "enemy splash, bounce, or teammate fire breaks cocoon before Charlie's team converts"
      exposed_by: "[[sources/Fandom-Charlie|Fandom-Charlie]] Cocoon health/decay mechanics and Penny splash warning"
      mitigation: "avoid placing cocoon next to splash paths and draft burst follow-up before relying on target removal"
      bp_use: false_positive_filter_for_control_pick
    - id: "low_damage_without_followup"
      active_when: "Charlie removes one target but the team cannot kill after release or convert objective tempo"
      exposed_by: "[[sources/Fandom-Charlie|Fandom-Charlie]] lead describing low damage output"
      mitigation: "pair with burst, scorer, zone body, or safe DPS depending on mode"
      bp_use: must_pair_with_conversion
    - id: "wall_or_thrower_pocket_denies_line"
      active_when: "enemy plays behind walls where Charlie cannot send the yo-yo outbound or cannot threaten cocoon follow-up"
      exposed_by: "yo-yo cannot be slung through walls and PLP target-favored thrower list"
      mitigation: "draft wallbreak/dive or keep Charlie on open/control lane instead of thrower pocket duty"
      bp_use: map_fit_filter

  conditional_matchup_seeds:
    - target:
        - "Chuck"
        - "Bolt"
        - "Shelly"
        - "Surge"
        - "Meg"
        - "Clancy"
        - "Glowy"
        - "Fang"
      direction: "subject_favored"
      source: "[[sources/PLP-Charlie|PLP-Charlie]]"
      mechanism: "Cocoon cancels engage, dash, scaling, or tank-forward plans and buys time for Charlie's team to burst or reset the objective."
      active_when: "target must enter a predictable ball, gem, zone, or safe route and Charlie has Super or Personal Space reset available"
      fails_when: "target baits Super, has wall/thrower cover, or Charlie's team cannot punish after Cocoon ends"
      bp_use: response_pick_seed_against_single_core_or_aggro
    - target:
        - "Sprout"
        - "Barley"
        - "Larry & Lawrie"
        - "Damian"
      direction: "target_favored"
      source: "[[sources/PLP-Charlie|PLP-Charlie]]"
      mechanism: "Thrower or wall-control pressure attacks around Charlie's outbound yo-yo line and can break spiders/cocoon from safer pockets."
      active_when: "walls remain intact and Charlie lacks wallbreak, dive, or a separate lane away from the pocket"
      fails_when: "terrain opens, thrower loses pocket, or Charlie can cocoon the carrier/scorer instead of dueling the thrower"
      bp_use: must_answer_thrower_pocket_before_charlie_plan
    - target:
        - "8-Bit"
        - "Lola"
        - "Poco"
        - "Ollie"
      direction: "target_favored"
      source: "[[sources/PLP-Charlie|PLP-Charlie]]"
      mechanism: "High sustained damage, extra bodies, healing, or support tempo can outlast Charlie's low damage and reduce one-target removal value."
      active_when: "fight is front-to-back and Charlie's team lacks burst or objective follow-up after Cocoon"
      fails_when: "Charlie removes the actual carrier/scorer or isolates one support before the sustain shell is grouped"
      bp_use: avoid_as_only_damage_or_control_layer

  slot_notes:
    slot_1: "viable only on maps where carrier disarm, anti-aggro, and vision tax are core duties and thrower answers are not cheap."
    slot_2_3: "strong as a response to an exposed scorer, tank, scaling pick, or single-core objective plan."
    slot_4_5: "repairs drafts that need carrier disarm or anti-aggro while leaving a teammate slot for damage conversion."
    slot_6: "punishes enemy comps that rely on one unrecoverable carrier/scorer/engager and lack thrower or splash counterplay."
```
