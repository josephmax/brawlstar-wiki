# Gus

## 基本信息

- 稀有度：Super Rare
- 定位：Support
- 类型：治疗与护盾支援英雄

## 攻击特征

- 主攻击是远程气球投掷
- 普通攻击本身以稳定输出和攒条为主
- 命中敌人后能为后续治疗资源做准备

## 超级技能特征

- Super 会给自己或队友套护盾
- 同时会击退周围敌人
- 护盾与击退让他在防守和护航时很有价值

## 适合场景

- 需要保护队友站位的 3v3 对局
- 需要续航、护盾和防反打的模式
- 与前排或控场英雄一起推进时表现更好

## 角色定位总结

Gus 是靠 spirit 治疗和护盾保护队友的 Support，和纯输出英雄相比，他更像一个把团队容错率拉高的节奏型后援。

## 关联页面

- [[sources/Fandom-Gus|Fandom 来源摘要: Gus]]
- [[sources/PLP-Gus|Power League Prodigy 来源摘要: Gus]]

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  review_gate: reviewed_with_sources_map_hooks_and_matchup_edges
  source_quality:
    fandom: "[[sources/Fandom-Gus|Fandom-Gus]] direct_raw_capture_2026-06-30-v2"
    plp: "[[sources/PLP-Gus|PLP-Gus]] direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "very_long 9.33 tile straight projectile; best on lanes where Gus can tag safely while supporting a higher-value teammate"
    projectile_reliability: "medium to high on open lanes; blocked by walls, bodies, and spawnables because the attack is a straight projectile"
    burst: "medium baseline, high only when Kooky Popper spirits stack or Spirit Animal damage boost converts through an ally"
    sustained_dps: "medium with 1.5s reload; pressure is valuable because hits build spirit resources"
    objective_damage: "low direct safe/objective DPS; objective contribution is protection, carrier support, and pick conversion"
    mobility: "low; no dash or reposition tool"
    survivability: "low self body at 3300 health, but high ally survivability through 2600 shield and knockback"
    engage: "medium as support engage when shield and 25% Spirit Animal buff are placed on a mobile teammate"
    disengage: "high peel when Super shield and knockback are timed on the threatened ally"
    anti_aggro: "high as shield-plus-knockback resource against single dive or close engage"
    anti_tank: "medium through protected teammate and Kooky Popper traps; low as a solo tank duel"
    wall_break: "none"
    throw_or_wall_bypass: "Super passes through walls to shield an ally; attack remains line-of-sight"
    area_control: "medium through spirit pickup placement and Kooky Popper threat around gem or lane approaches"
    scouting_or_vision: "low to medium because spirits can mark contested spaces but do not replace true reveal"
    team_support: "very_high with shield, healing spirits, damage boost, and dive peel"
    spawnable_or_pet: "resource pickups rather than autonomous pets; can still tax space when Kooky Popper is available"
    crowd_control: "medium knockback around Super target"
    terrain_creation: "none"
    terrain_destruction: "none"

  build_switches:
    - build: "Kooky Popper / Spirit Animal / Shield, Damage"
      source: "[[sources/PLP-Gus|PLP-Gus]]"
      changes_capabilities:
        - "turns spirit placement into a burst trap or zone deterrent"
        - "adds a 25% damage boost to the shielded target for a short conversion window"
      enables:
        - "Bounty star-holder protection"
        - "Knockout shielded engage or peel"
      mitigates_failure_modes:
        - "low_self_health"
        - "lack_of_finish_after_shield"
      best_when: "team has a carry, sniper, assassin, or bruiser that can immediately use shield and damage boost"
      poor_when: "team lacks a conversion target or enemy can keep Gus behind walls without spirit access"
      bp_use: "default_build_for_protective_long_range_support"
    - build: "Kooky Popper / Health Bonanza / Shield, Gadget Charge"
      source: "[[sources/Fandom-Gus|Fandom-Gus]]"
      changes_capabilities:
        - "doubles spirit healing and makes placed spirits a stronger retreat resource"
        - "keeps Kooky Popper as area deterrent around predictable approaches"
      enables:
        - "gem carrier retreat support"
        - "melee teammate sustain after first contact"
      mitigates_failure_modes:
        - "shield_decay_timing"
        - "chip_attrition_before_super"
      best_when: "objective is about keeping a carrier or frontline alive rather than bursting a pick"
      poor_when: "team needs immediate damage boost to secure kills"
      bp_use: "sustain_variant_for_carrier_or_frontline_shell"

  map_feature_hooks:
    - map_feature_type: "long_sightline"
      route_or_position: "Shooting Star or Dry Season open lane, Hideout side lane, or Layer Cake layer angle"
      uses_feature_by: "tag from max range to build spirits while holding Super for the high-star or exposed teammate"
      objective_conversion: "protect Bounty lead, chip safely, and convert shielded teammate damage boost into first pick"
      active_when: "line of sight is open enough for Gus to hit and team has a protected carry or sniper lane"
      fails_if: "walls, porters, Eve hatchlings, Pam turret, or body-blockers absorb shots before spirit cycle starts"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Hideout|Hideout]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
      bp_use: "required_capabilities.long_range_support_and_star_lead_protection"
    - map_feature_type: "knockout_shield_peel_and_finish_window"
      route_or_position: "Out in the Open long lane, Flaring Phoenix side water-bush route, New Horizons central cover, or Belle's Rock wall lane"
      uses_feature_by: "shield the teammate taking first contact, knock back the diver, then use Spirit Animal or Kooky Popper to finish the trade"
      objective_conversion: "turns one engage into a protected pick or saves a low-health teammate during shrinking Knockout space"
      active_when: "ally can attack immediately after shield and enemy engage is single-lane rather than layered from two sides"
      fails_if: "shield is fired too early, decays before contact, misses the ally, or enemy attacks through wall pockets that Gus cannot contest"
      example_maps:
        - "[[entities/maps/Out in the Open|Out in the Open]]"
        - "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
      bp_use: "candidate_eval.shielded_trade_and_peel_window"
    - map_feature_type: "carrier_or_scorer_protection"
      route_or_position: "Gem Fort center fort, Hard Rock Mine mid retreat, Center Stage midfield, or Sneaky Fields side bush push"
      uses_feature_by: "place shield on gem carrier, scorer, or mobile teammate just before the decisive route contact"
      objective_conversion: "protect gem countdown, keep ball push alive, or let an assassin/bruiser survive entry long enough to finish"
      active_when: "Gus has line to ally or wall-passing Super angle and the protected teammate has a clear objective task"
      fails_if: "the protected teammate cannot convert, enemy waits out shield decay, or Colette-style max-health damage ignores the shield advantage"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.protect_carry_or_enable_entry"

  objective_contracts:
    - mode: "Bounty"
      can_fulfill:
        - "long-range chip while protecting high-star teammate"
        - "shield and damage boost to win first-pick exchange"
      cannot_fulfill:
        - "solo carry damage without a protected teammate"
        - "wall-pocket removal"
      needs_teammate_support:
        - "lane partner that uses shield to hold or swing star lead"
      false_positive: "long range alone is not enough if shots are body-blocked and spirits never cycle"
    - mode: "Knockout"
      can_fulfill:
        - "shielded engage support or anti-dive peel"
        - "late-round protection when one pick decides the round"
      cannot_fulfill:
        - "frontline body role"
        - "direct answer to deep thrower pockets"
      needs_teammate_support:
        - "teammate able to convert Spirit Animal damage boost"
      false_positive: "Gus loses value when drafted without a teammate who can turn shield into a kill or survival swing"
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier shield during countdown"
        - "spirit and Kooky Popper space control near mine approaches"
      cannot_fulfill:
        - "primary mid DPS into spawnables"
        - "safe bush reveal"
      needs_teammate_support:
        - "mid controller and lane damage"
      false_positive: "carrier protection is conditional support, not proof Gus wins the whole mid by himself"
    - mode: "Brawl Ball"
      can_fulfill:
        - "shielded scorer or bruiser entry"
        - "knockback peel against a single defender or diver"
      cannot_fulfill:
        - "wallbreak for closed goal"
        - "solo scorer"
      needs_teammate_support:
        - "actual scorer, wallbreak, or displacement teammate"
      false_positive: "shielded push fails if no one can convert the goal route before shield decays"

  failure_modes:
    - id: "low_self_health_focus"
      active_when: "enemy can force Gus into close duel or repeated long-range chip before shield value"
      exposed_by: "3300 health and no mobility"
      mitigation: "keep range, play behind teammate, and spend Super on the threatened carry rather than ego shielding late"
      bp_use: "false_positive_filter_for_frontline_role"
    - id: "walls_and_spawnables_block_cycle"
      active_when: "Mr. P porters, Eve hatchlings, Pam turret, walls, or body-blockers prevent clean Loony Balloons hits"
      exposed_by: "straight projectile and spirit spawning requires hits"
      mitigation: "draft summon clear, play a separate open lane, or avoid Gus into heavy body-block maps"
      bp_use: "must_answer_body_block_before_gus_plan"
    - id: "shield_decay_or_missed_target"
      active_when: "Super is fired too early, decays before contact, misses ally, or ally cannot attack during Spirit Animal window"
      exposed_by: "shield decays over time and Super has aimed travel"
      mitigation: "time shield just before first contact and choose a teammate with immediate conversion"
      bp_use: "candidate_eval.shield_timing_execution"
    - id: "no_conversion_teammate"
      active_when: "team has no assassin, sniper, carry, or bruiser that benefits from shield plus damage boost"
      exposed_by: "Gus's strongest value is support, not raw solo DPS"
      mitigation: "pair with a clear protected carry or select a more self-sufficient lane pick"
      bp_use: "slot_fit.requires_carry_or_entry_target"

  conditional_matchup_seeds:
    - target:
        - "Gray"
        - "Emz"
        - "Belle"
        - "Bo"
        - "Lola"
        - "Squeak"
        - "Amber"
      direction: "subject_favored"
      source: "[[sources/PLP-Gus|PLP-Gus]]"
      mechanism: "Gus can outlast or swing ranged/control lanes by shielding the threatened ally, using Spirit Animal for finish windows, and placing spirits near contested paths"
      active_when: "map has playable long lanes and the target lacks cheap body-block or wall control that stops Gus's hits"
      fails_when: "target plays behind deeper walls, receives summon cover, or deletes Gus before shield cycle"
      bp_use: "support_lane_response_candidate"
    - target:
        - "Fang"
        - "Bull"
        - "El Primo"
        - "Darryl"
        - "Mortis"
      direction: "volatile"
      source: "[[sources/Fandom-Gus|Fandom-Gus]]"
      mechanism: "shield knockback can stop single-lane engage, but Gus himself dies if the diver bypasses the protected teammate or chains a second engage"
      active_when: "Super is available and the diver must commit onto the shielded ally through a predictable lane"
      fails_when: "diver baits shield, enters from two angles, or reaches Gus directly after shield decay"
      bp_use: "anti_aggro_resource_check"
    - target:
        - "Mr. P"
        - "Nani"
        - "Bonnie"
        - "R-T"
        - "Pam"
        - "Mandy"
      direction: "target_favored"
      source: "[[sources/PLP-Gus|PLP-Gus]]"
      mechanism: "spawnables, longer-range burst, split bodies, or turret sustain block Gus's straight shots and punish low health before his support cycle matters"
      active_when: "map gives them wall cover, body-blocks, or open sightlines where Gus cannot safely charge spirits"
      fails_when: "Gus's team clears bodies first or a shielded teammate collapses before their range advantage stabilizes"
      bp_use: "must_answer_range_and_body_block"
    - target:
        - "Stu"
        - "Eve"
      direction: "target_favored"
      source: "[[sources/PLP-Gus|PLP-Gus]]"
      mechanism: "mobility or extra bodies can dodge or absorb Gus shots, then pressure his low-health position before shield converts"
      active_when: "map has enough open dodge space or Eve water/offsides that deny stable projectile tagging"
      fails_when: "Gus saves shield for the actual entry and teammate control pins the mobile target in place"
      bp_use: "avoid_or_pair_with_control"

  slot_notes:
    slot_1: "acceptable only on long-lane Bounty/Knockout maps when team can protect his low health and use the shield"
    slot_2_3: "strong after locking or revealing a carry/assassin/bruiser that benefits from shield and damage boost"
    slot_4_5: "good response to single-lane engage or fragile control lanes, but check spawnable and wall-pocket counters"
    slot_6: "punishes enemy drafts with no body-block, no deep thrower pocket, and one clear target to shield against"
```
