# Wendy

## 基本信息

- 稀有度：Mythic
- 定位：Support
- 类型：护盾与减伤支援英雄（全游戏最低基础血量，靠护盾、发生器与水面机动换取容错）

## 攻击特征

- 主攻击 Blow Dryer：远程直线 blast，距离 8（Long），装填 1.45 秒（Fast）
- 命中给自身叠加可消耗护盾；命中队友时给队友更强护盾
- 自身护盾不随时间衰减，只能由普攻回充；队友护盾按 0.5 秒 5% 衰减，最多叠至初始值的 4 倍

## 超级技能特征

- Super Planet Protector：部署 6 格半径风力发生器，把范围内 Wendy 与队友受到伤害的 60% 转移给发生器承担
- 发生器可被集火摧毁；Hypercharge GREEN ENERGY 下吸收比例提升到 90% 且耐久更高
- Trait：可在水面移动；自身护盾受到伤害时为 Super 充能（受盾伤约 3.33 倍护盾上限充满）

## 适合场景

- 需要护送持球/持宝石队友硬进点的 3v3 模式
- 有可站位的狭窄目标区、能吃到发生器减伤的阵地战
- 对手以持续 chip 与低速 poke 为主、缺乏单体爆发穿透时收益最大

## 角色定位总结

Wendy 是把团队伤害分摊和护盾资源做到极致的最低血量 Support：本体极脆，但出生即带等量护盾、普攻持续供盾、Super 用发生器集体减伤。她改写的是"队伍有效血量"，而不是自身输出；一旦发生器被拆或护盾循环断供，本体几乎没有任何自保。

## 关联页面

- [[sources/Fandom-Wendy|Fandom 来源摘要: Wendy]]
- [[sources/PLP-Wendy|Power League Prodigy 来源摘要: Wendy]]
- [[sources/Fandom-Release-Notes-August-2026|Fandom 来源摘要: Release Notes August 2026]]

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  review_gate: reviewed_with_sources_map_hooks_and_matchup_edges
  source_quality:
    fandom: "[[sources/Fandom-Wendy|Fandom-Wendy]] direct_raw_capture_2026-09-03"
    plp: "[[sources/PLP-Wendy|PLP-Wendy]] direct_raw_capture_2026-09-03"
    user_notes: "none"

  capability_vector:
    effective_range: "long 8 tile straight blast; best when she can chip and shield-cycle behind a frontline on open lanes"
    projectile_reliability: "medium to high on open lanes; straight projectile blocked by walls and bodies, and the shield cycle stalls when shots miss"
    burst: "low to medium; Power 11 单发 2000 的稳定输出，无爆发包"
    sustained_dps: "medium with 1.45s fast reload; sustained pressure exists but is support-grade"
    objective_damage: "low direct safe/objective DPS; objective contribution is shields, damage redirection and zone mitigation"
    mobility: "medium base 770 fast plus water walking; Wind-Powered adds a 5 tile jump over walls and water with airborne immunity"
    survivability: "lowest body in game at Power 11 4000, but effective spawn health is Power 11 8000 with the non-decaying starting shield; ally shields add Power 11 1520 per hit with stacking to 4x"
    engage: "medium as shield-entry support; feeding shields to a mobile or high-HP teammate creates a protected entry window"
    disengage: "high with Wind-Powered jump over walls or water and the slowing Green Grenade"
    anti_aggro: "high when turbine zone plus slow field meet a single diver; weak once burst exceeds shield and turbine breakpoints"
    anti_tank: "low to medium; moderate single-target damage does not cut through high-HP bodies, contribution is mitigation for the team answer"
    wall_break: "none"
    throw_or_wall_bypass: "Super is lobbed over walls to place the turbine; Wind-Powered jumps walls; attack remains line-of-sight"
    area_control: "high around a planted turbine: Slowing Shield field plus 60% damage redirection makes the zone a fortification; Green Grenade adds 2 tile slow and 5s anti-heal"
    scouting_or_vision: "low; no reveal tool"
    team_support: "very_high; personal and ally shields, team-wide damage redirection, water-route taxi via own mobility is limited to herself, shield-feeding turns a carrier into the effective health pool"
    spawnable_or_pet: "deployable turbine only; it is destructible and focusable, not a pet"
    crowd_control: "medium; turbine-area slow with Slowing Shield, grenade slow and anti-heal, no knockback or stun"
    terrain_creation: "none"
    terrain_destruction: "none"

  build_switches:
    - build: "Wind-Powered / Solar Shield / Shield, Damage, Vision"
      source: "[[sources/PLP-Wendy|PLP-Wendy]]"
      changes_capabilities:
        - "jump adds wall and water escape or entry with airborne immunity"
        - "Solar Shield raises turbine durability by Power 11 4000, extending the fortification window"
      enables:
        - "shield-fed carrier push on Brawl Ball goal routes"
        - "turbine-anchored zone stands on Gem Grab countdown and Hot Zone"
      mitigates_failure_modes:
        - "lowest_body_focus_fire"
        - "turbine_focus_collapse"
      best_when: "team has a carrier, bruiser or high-HP teammate that converts shields into objective pressure"
      poor_when: "enemy has pierce or max-health damage and burst that deletes shields faster than the attack cycle"
      bp_use: "default_build_for_protective_zone_support"
    - build: "Green Grenade / Slowing Shield / Shield, Damage"
      source: "[[sources/Fandom-Wendy|Fandom-Wendy]]"
      changes_capabilities:
        - "grenade adds 2 tile slow with 5s anti-heal, answering sustain comps"
        - "Slowing Shield turns the turbine into a slow field for peel and zone denial"
      enables:
        - "anti-heal answer into Byron, Poco, Juju style sustain"
        - "Hot Zone circle denial anchored on the turbine"
      mitigates_failure_modes:
        - "sustain_stalemate_against_low_burst"
      best_when: "enemy win condition is healing or chip sustain rather than burst"
      poor_when: "team already lacks mobility and needs Wind-Powered as the only escape"
      bp_use: "anti_sustain_zone_denial_variant"

  map_feature_hooks:
    - map_feature_type: "water_route_flank_and_retreat"
      route_or_position: "Flaring Phoenix side water route and other Ranked pool maps with playable water edges"
      uses_feature_by: "water walking to take flank angles or retreat across water that most divers cannot follow, then shield-cycle from the far side"
      objective_conversion: "converts an uncontestable angle into safe chip and shield feed before the objective contact"
      active_when: "water borders a contested lane or objective approach and the enemy lacks water-walking answers"
      fails_if: "enemy controls the landing bank, or the route ends inside burst range without the turbine planted"
      example_maps:
        - "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"
      bp_use: "required_capabilities.water_route_support_flank"
    - map_feature_type: "long_sightline_shield_cycle"
      route_or_position: "Shooting Star or Dry Season open lanes, Hideout side lane, Layer Cake layer angle"
      uses_feature_by: "chip from max range while feeding shields to the star-holder or exposed teammate, holding Super for the decisive route"
      objective_conversion: "wins star-lead trades by making the protected teammate effectively double-healthed"
      active_when: "line of sight is open enough for the 8 tile blast to cycle reliably"
      fails_if: "walls and body-blockers absorb shots and the shield cycle stalls"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Hideout|Hideout]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
      bp_use: "candidate_eval.shield_cycle_lane_presence"
    - map_feature_type: "objective_fortification_window"
      route_or_position: "Gem Fort mine approaches, Center Stage midfield, Hard Rock Mine mid retreat, Sneaky Fields push routes"
      uses_feature_by: "plant the turbine on the countdown or scoring contact point so the team fights inside 60% damage redirection"
      objective_conversion: "turns one objective contest into a protected carry window, especially with Solar Shield durability"
      active_when: "the objective forces enemies to enter the turbine radius to contest"
      fails_if: "the enemy focuses the turbine from outside its radius or simply trades outside the zone"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.anchor_objective_fortification"
    - map_feature_type: "shield_carry_goal_push"
      route_or_position: "Backyard Bowl ball routes and open goal approaches"
      uses_feature_by: "feed stacked ally shields to the ball carrier and drop the turbine on the goal approach, as documented in Fandom tips"
      objective_conversion: "carrier enters scoring range with shields plus 60% redirection; Green Grenade peel covers the last stretch"
      active_when: "carrier has CC immunity or the enemy lacks crowd control to stop the push"
      fails_if: "enemy bursts the carrier through shields faster than the decay, or walls close the goal route"
      example_maps:
        - "[[entities/maps/Backyard Bowl|Backyard Bowl]]"
      bp_use: "slot_task.protect_scorer_entry"

  objective_contracts:
    - mode: "Bounty"
      can_fulfill:
        - "protect the star-holder with shields and turbine redirection"
        - "long-range chip that trades safely on open lanes"
      cannot_fulfill:
        - "solo pick pressure or burst to close kills"
        - "wall-pocket removal"
      needs_teammate_support:
        - "a damage lane that converts the shielded trades"
      false_positive: "lowest body in the game means a lost 1v1 anchor is a free star swing even with shields"
    - mode: "Knockout"
      can_fulfill:
        - "turbine-anchored final circle control with slow field"
        - "anti-dive peel with grenade slow and Wind-Powered escape"
      cannot_fulfill:
        - "opening pick or dueling pressure"
        - "answers to deep thrower pockets"
      needs_teammate_support:
        - "a pick threat that uses the protected window"
      false_positive: "shrinking zones without cover expose the Power 11 4000 body once shields break"
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier shields during countdown and turbine fortification on the mine"
        - "anti-heal grenade into sustain mid comps"
      cannot_fulfill:
        - "primary mid DPS into spawnables"
        - "safe bush reveal"
      needs_teammate_support:
        - "mid controller that owns space while Wendy owns mitigation"
      false_positive: "the turbine helps the team hold gems only if someone else wins the mid trade"
    - mode: "Brawl Ball"
      can_fulfill:
        - "shield-fed scorer push with turbine cover on the goal route"
        - "peel on the ball with grenade slow"
      cannot_fulfill:
        - "wallbreak for closed goals"
        - "solo scoring threat"
      needs_teammate_support:
        - "an actual scorer or wallbreak teammate"
      false_positive: "shield push fails if the enemy bursts through the shield stack before goal range"
    - mode: "Heist"
      can_fulfill:
        - "turbine and shields to extend the safe-hitter's race window"
        - "anti-heal grenade on defense retreats"
      cannot_fulfill:
        - "direct safe damage"
        - "solo lane defense into ranged pressure"
      needs_teammate_support:
        - "true safe DPS that owns the race"
      false_positive: "Wendy adds zero objective damage; on race maps she is only as good as the hitter she protects"
    - mode: "Hot Zone"
      can_fulfill:
        - "turbine-anchored zone body support with Slowing Shield denial"
        - "sustain answer with Green Grenade anti-heal"
      cannot_fulfill:
        - "stand the circle alone at Power 11 4000 body"
        - "thrower pocket removal from safety"
      needs_teammate_support:
        - "durable zone holder that stands inside her turbine"
      false_positive: "the zone fortification is only real while the turbine stands and someone body's the circle"

  failure_modes:
    - id: "lowest_body_focus_fire"
      active_when: "enemy burst or focus reaches Wendy after shields or turbine are stripped"
      exposed_by: "Power 11 4000 body, lowest in game, with no decay on her own shield but no passive regeneration of it"
      mitigation: "keep max-range cycle, hold Wind-Powered for wall or water escape, and plant the turbine before committing to contested space"
      bp_use: "false_positive_filter_for_frontline_role"
    - id: "shield_cycle_stall"
      active_when: "shots are body-blocked or Wendy is forced out of lane so the attack cannot replenish shields"
      exposed_by: "her own shield does not decay but is only replenished by her attack, and ally shields decay 5% per 0.5s"
      mitigation: "play lanes with clean line of sight and time shield feed to contact windows instead of pre-firing"
      bp_use: "candidate_eval.shield_cycle_uptime"
    - id: "turbine_focus_collapse"
      active_when: "the enemy focuses the destructible turbine from outside its radius or disengages from the zone"
      exposed_by: "turbine is a focusable deployable and the 60% redirection ends when it breaks"
      mitigation: "plant it where contesting requires entering the radius, and layer Solar Shield durability or re-cast timing"
      bp_use: "must_answer_turbine_destruction"
    - id: "pierce_and_max_health_damage"
      active_when: "enemy runs Colette-style max-health damage or effects that interact through shields"
      exposed_by: "Fandom mechanics note that Colette attack and Super deal damage based on max health while the shield is active, ignoring the shield advantage"
      mitigation: "draft a separate answer to pierce comps and avoid treating shields as complete mitigation into them"
      bp_use: "must_answer_shield_pierce"
    - id: "burst_over_shield_breakpoints"
      active_when: "enemy burst exceeds the shield plus turbine mitigation in one trade window"
      exposed_by: "shields are consumable bars, not damage immunity; overkill damage carries through"
      mitigation: "keep the protected teammate behind the turbine zone and stagger shields rather than stacking early"
      bp_use: "false_positive_filter_into_burst_drafts"

  conditional_matchups:
    - target:
        - "Max"
        - "Bolt"
      direction: "subject_favored"
      source: "[[sources/PLP-Wendy|PLP-Wendy]]"
      mechanism: "speed-reliant pokers cannot break the shield cycle or the turbine, while Wendy's long blast chips them reliably and the slow field punishes their exit routes"
      active_when: "open lanes let her cycle and the turbine covers the contested space"
      fails_when: "they kite outside turbine range and the team collapses on Wendy's low body first"
      bp_use: "support_lane_response_candidate"
    - target:
        - "Stu"
        - "Lily"
      direction: "subject_favored"
      source: "[[sources/PLP-Wendy|PLP-Wendy]]"
      mechanism: "dash-in assassins meet slow field plus shields and a jump escape; their short combos do not clear effective spawn health before the turbine answers"
      active_when: "turbine or slow covers the dive route and Wind-Powered is held for the engage"
      fails_when: "they bait the jump and re-enter after the shield window, or walls hide their approach"
      bp_use: "anti_dive_peel_resource"
    - target:
        - "Barley"
      direction: "subject_favored"
      source: "[[sources/PLP-Wendy|PLP-Wendy]]"
      mechanism: "area-denial chip is absorbed by shields and turbine redirection, while Wendy's single long blast outranges his lob safety"
      active_when: "she cycles from max range and does not stand inside stacked fire zones"
      fails_when: "two area-denial sources layer the same lane and force her out of shield cycle range"
      bp_use: "zone_duel_response_candidate"
    - target:
        - "Jessie"
        - "Nita"
        - "Charlie"
      direction: "target_favored"
      source: "[[sources/PLP-Wendy|PLP-Wendy]]"
      mechanism: "summons and spiders body-block her straight blast, stall the shield cycle, and provide free chip into shields that also charges enemy Supers"
      active_when: "summons sit between Wendy and her targets on lane maps"
      fails_when: "the team clears bodies first and the turbine zone denies the summon's standing space"
      bp_use: "must_answer_body_block"
    - target:
        - "Bo"
        - "Surge"
        - "Pierce"
      direction: "subject_favored"
      source: "[[sources/PLP-Wendy|PLP-Wendy]]"
      mechanism: "chip-tempo pokers rely on repeated ranged hits to win the lane, but shields absorb the chip, the turbine blunts the lane, and Wendy's fast-reload long blast out-cycles their slower timers (Bo's arc, Surge's stage stacking, Pierce's charged shots)"
      active_when: "open lanes let her keep the shield cycle while the turbine covers the contested space"
      fails_when: "they outrange the turbine edge after Surge stacks late stages, mines deny her cycle lane, or charged shots overkill the shield bar faster than she replenishes it"
      bp_use: "support_lane_response_candidate"
    - target:
        - "Ash"
        - "Carl"
        - "Bull"
      direction: "target_favored"
      source: "[[sources/PLP-Wendy|PLP-Wendy]]"
      mechanism: "sustained or burst-heavy bodies out-trade her moderate damage; Ash and Carl chip through shields continuously and Bull's burst exceeds shield breakpoints in one window"
      active_when: "they reach Wendy or the turbine before the team answers"
      fails_when: "turbine slow plus grenade peel breaks the engage before the shield stack is stripped"
      bp_use: "avoid_or_pair_with_control"
    - target:
        - "Frank"
        - "Lola"
      direction: "target_favored"
      source: "[[sources/PLP-Wendy|PLP-Wendy]]"
      mechanism: "Frank's stun and huge body ignore the shield trade and walk through mitigation, while Lola's Ego adds a second body that strips shields from angles and can focus the destructible turbine"
      active_when: "they reach Wendy or the turbine before the team answers, or walls protect the Ego/attack path"
      fails_when: "turbine slow plus grenade peel kites the dive, or focus fire removes the Ego before it strips the cycle"
      bp_use: "avoid_or_pair_with_control"

  slot_notes:
    slot_1: "risky as an opener on burst-heavy drafts; acceptable on long-lane or water-route maps where the shield cycle is safe"
    slot_2_3: "strong after a carrier, bruiser or high-HP teammate is visible to receive shields and turbine value"
    slot_4_5: "good response to chip, speed and sustain comps; check the enemy has no pierce or max-health damage first"
    slot_6: "punishes drafts with no burst overkill and no summon body-block; verify a destructible-turbine answer is absent"
```

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "Wendy",
    "target_states": [
      {
        "id": "body",
        "entity_class": "brawler_body",
        "roster_target": true,
        "health": {"amount": 2000, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-Wendy|Fandom-Wendy]]"
      }
    ],
    "damage_packets": [
      {
        "id": "main.impact",
        "ability_kind": "main_attack",
        "packet_unit": "blast_impact",
        "delivery_variant": "impact",
        "repeat_model": "identical",
        "damage": 1000,
        "at_power_level": 1,
        "active_when": "单发 blast 直接命中；不假设多目标",
        "source_ref": "[[sources/Fandom-Wendy|Fandom-Wendy]]"
      }
    ],
    "defense_modifiers": [
      {
        "id": "spawn_shield",
        "source_kind": "trait",
        "loadout_group": "trait",
        "applies_to_states": ["body"],
        "effect": {"type": "barrier_hp", "amount": 2000, "at_power_level": 1},
        "active_when": "出生时自带、不随时间衰减、只能由普攻回充；被击破后消失直到回充",
        "sequence_validity": "静态近似仅代表满盾时点；对局中期实际护盾量取决于攻击循环",
        "source_ref": "[[sources/Fandom-Wendy|Fandom-Wendy]]"
      }
    ],
    "exclusions": [
      {"id": "attack_granted_shields", "reason": "普攻自盾 580 / 队友盾 760（Power 1）是随攻击循环与时序变化的临时护盾，不建模为静态 EHP", "change_class": "temporal_survival_excluded"},
      {"id": "planet_protector_redirect", "reason": "发生器把范围内多人伤害的 60%（Hypercharge 90%）redirect 到可被摧毁的 deployable，是伤害分配时序模型", "change_class": "unsupported_mechanic"},
      {"id": "turbine_health", "reason": "发生器耐久 2500（Power 1）与 Solar Shield +2000 属 deployable durability，不进英雄分母", "change_class": "non_breakpoint"},
      {"id": "green_energy_hypercharge", "reason": "Hypercharge 期间 90% 吸收与耐久提升依赖激活窗口", "change_class": "temporal_survival_excluded"}
    ]
  }
}
```
