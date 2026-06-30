# Doug

## 基本信息

- 稀有度：Mythic
- 定位：Support
- 类型：复活支援英雄

## 攻击特征

- 主攻击是范围性近身攻击
- 既能伤害敌人，也能治疗友军
- 适合贴队友打节奏

## 超级技能特征

- Super 会给队友一个复活 buff
- 目标死亡后可在延迟后复活
- 能明显改变团战的容错率

## 适合场景

- 团队推进战
- 需要续航和复活的对局
- 队友更偏近战或突进时
- 想打滚雪球和翻盘节奏时

## 角色定位总结

Doug 是一个能同时提供治疗和复活价值的近身支援英雄。和 `Poco` 比，他更偏单体翻盘；和 `Pam` 比，他更偏贴身站位；和 `Byron` 比，他更像战斗中续命而不是远程消耗。

## 关联页面

- [[sources/Fandom-Doug|Fandom 来源摘要: Doug]]
- [[sources/PLP-Doug|Power League Prodigy 来源摘要: Doug]]

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  review_gate: reviewed_with_sources_map_hooks_and_matchup_edges
  source_quality:
    fandom: "[[sources/Fandom-Doug|Fandom-Doug]] direct_raw_capture_2026-06-30-v2"
    plp: "[[sources/PLP-Doug|PLP-Doug]] direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "short 3.33 tile circular body radius; value depends on route access, grass, walls, or teammate body pressure"
    projectile_reliability: "high inside radius because Snack Attack is immediate and does not require aim; low before contact because Doug has no dash"
    burst: "medium baseline, high only when Extra Mustard or Hypercharge mirror turns close contact into a finish window"
    sustained_dps: "medium in repeated close trades with 1.5s reload; cannot project stable DPS across open lanes"
    objective_damage: "low direct objective DPS; objective value comes from revive, carrier protection, and push sustain"
    mobility: "Fast movement speed with no dash or jump; route must be supplied by grass, walls, or teammate pressure"
    survivability: "high support body at 5200 health with Self Service self-heal and Second Serving revive; revived target has no invulnerability"
    engage: "low alone, high as support for a melee or assassin teammate who can enter while protected by revive"
    disengage: "medium through healing and revive reset; weak when enemy can wait out the hot dog or burst the revive location"
    anti_aggro: "medium against commit-heavy close threats when Doug holds ammo, Extra Mustard, or Super timing near the objective"
    anti_tank: "medium in point-blank objective fights; loses to higher burst tanks if they control first contact"
    wall_break: "none"
    throw_or_wall_bypass: "support-only bypass: Super passes through walls and homes to allies; attack can clip enemies or allies just behind a wall but is not a true thrower pattern"
    area_control: "low to medium around Doug's body; threatens a small circle rather than a remote zone"
    scouting_or_vision: "low; can sweep nearby grass only by physically entering"
    team_support: "very_high through heal pulses, Super revive, no-drop carrier timing, and Hypercharge ally mirror attack"
    spawnable_or_pet: "none"
    crowd_control: "none"
    terrain_creation: "none"
    terrain_destruction: "none"

  build_switches:
    - build: "Extra Mustard / Self Service / Shield, Damage"
      source: "[[sources/PLP-Doug|PLP-Doug]]"
      changes_capabilities:
        - "turns the next Snack Attack into a real close-range punish instead of a pure sustain tap"
        - "Self Service lets Doug heal even while cycling attacks and accelerates Super access through trait healing"
      enables:
        - "Brawl Ball close push body"
        - "Knockout revive swing after first contact"
      mitigates_failure_modes:
        - "short_range_damage_check"
        - "single_life_attrition_before_super"
      best_when: "map has grass, walls, or a teammate entry route that forces enemies into Doug's radius"
      poor_when: "enemy plays open range or can burst the revived target without stepping into Doug"
      bp_use: "default_build_for_close_objective_support"
    - build: "Double Sausage / Fast Food / Shield, Gadget Charge"
      source: "[[sources/Fandom-Doug|Fandom-Doug]]"
      changes_capabilities:
        - "converts next attack into a stronger ally heal with no damage"
        - "Fast Food fully heals Doug after an ally revive, extending the push if the revive is converted immediately"
      enables:
        - "carrier protection shell"
        - "second-wave Brawl Ball or Gem Grab push"
      mitigates_failure_modes:
        - "revive_location_focus_fire"
        - "team_push_runs_out_of_health"
      best_when: "Doug is drafted as dedicated support for a known close-range teammate rather than as damage"
      poor_when: "team still lacks a scorer, finisher, or lane opener"
      bp_use: "support_variant_when_damage_role_is_already_covered"

  map_feature_hooks:
    - map_feature_type: "brawl_ball_revival_and_close_push_body"
      route_or_position: "Center Stage center grass, Sneaky Fields side bush route, or Triple Dribble goal-entry choke"
      uses_feature_by: "walk with the ball carrier or scorer, heal during contact, then place Second Serving before the lethal trade"
      objective_conversion: "keeps a scorer alive through first burst, forces defenders to spend another cycle, or revives the carry for a second touch"
      active_when: "team has a real finisher and terrain lets Doug enter before the ball carrier dies"
      fails_if: "goal remains closed, enemy has layered knockback or burst at the revive location, or Doug is kited before Super"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_push_support_and_second_life_window"
    - map_feature_type: "knockout_revival_last_life_swing"
      route_or_position: "Belle's Rock wall lane, Flaring Phoenix side water-bush approach, or New Horizons central cover"
      uses_feature_by: "attach Super to the teammate taking first contact so a trade becomes a live body instead of a death"
      objective_conversion: "turns a 2v2 or first-pick race into a reset where Doug's team keeps body count"
      active_when: "ally has cover to survive the 2-second revive delay and enemies cannot simply wait out the hot dog"
      fails_if: "open range lets Piper, Nani, Belle, or similar picks pre-aim the revive spot"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "candidate_eval.revive_trade_math"
    - map_feature_type: "gem_carrier_countdown_no_drop_tech"
      route_or_position: "Gem Fort fort entrance, Hard Rock Mine mid retreat, or Double Swoosh side grass countdown route"
      uses_feature_by: "cast Second Serving on a gem carrier during the last seconds so defeat does not drop gems before revive"
      objective_conversion: "protects countdown and denies enemy comeback pickup"
      active_when: "Doug is close enough to cover the revive location and Super is timed inside the buff window"
      fails_if: "cast is too early, carrier dies outside team cover, or enemy controls the revive tile after the delay"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.carrier_protection_and_countdown_denial"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "escort a close-range scorer through first burst with heal and revive"
        - "turn a defender trade into a second scoring touch"
      cannot_fulfill:
        - "primary wallbreak"
        - "solo open-field scorer"
      needs_teammate_support:
        - "scorer or tank that actually converts the extra life"
        - "wallbreak or displacement when goal geometry is closed"
      false_positive: "calling Doug a ball pick without a route or scorer overvalues revive and undervalues his short range"
    - mode: "Knockout"
      can_fulfill:
        - "protect first-contact teammate and reverse trade math"
        - "punish close objective contact with Extra Mustard"
      cannot_fulfill:
        - "primary long-range lane control"
        - "safe poke on fully open maps"
      needs_teammate_support:
        - "ally that can take first contact near cover"
        - "range lane teammate to prevent full kite"
      false_positive: "revive loses value if the enemy can aim the revive tile without moving"
    - mode: "Gem Grab"
      can_fulfill:
        - "late-countdown carrier protection with Second Serving"
        - "mid push sustain when teammates already control lanes"
      cannot_fulfill:
        - "primary gem mine control on open maps"
        - "long-range carrier poke"
      needs_teammate_support:
        - "mid controller or long-range lane"
        - "bodyguard at revive location"
      false_positive: "no-drop carrier tech is timing-sensitive and should be treated as a late-game support contract"

  failure_modes:
    - id: "short_range_open_map_trap"
      active_when: "enemy comp plays Piper, Nani, Belle, Squeak, or other long-range/area control from open angles"
      exposed_by: "Doug has 3.33 tile range and no dash"
      mitigation: "draft only with grass, cover, speed support, or a close teammate that forces contact"
      bp_use: "hard_gate_against_open_range_first_pick"
    - id: "revive_timing_or_no_invulnerability"
      active_when: "Second Serving is cast too early, too late, or onto a target dying in visible focus fire"
      exposed_by: "Fandom notes the buff window and that revived targets have no invulnerability"
      mitigation: "cast during final commitment and cover the revive tile with teammate pressure"
      bp_use: "candidate_eval.revive_window_execution_check"
    - id: "team_comp_without_close_conversion"
      active_when: "Doug is paired with only passive ranged teammates or no scorer/frontline"
      exposed_by: "Doug's support tools require allies inside his radius or a target for Second Serving"
      mitigation: "pair with assassin, tank, or scorer that uses the extra life immediately"
      bp_use: "slot_fit.requires_conversion_teammate"
    - id: "higher_burst_close_mirror"
      active_when: "Bull, Darryl, El Primo, or similar picks choose first contact and delete Doug or the revived ally"
      exposed_by: "PLP counter list plus Doug's lack of hard CC"
      mitigation: "keep Super for teammate trade, add anti-tank damage, or avoid the short-range mirror"
      bp_use: "must_answer_close_burst_before_locking_doug"

  conditional_matchup_seeds:
    - target:
        - "Lola"
        - "Eve"
        - "Pearl"
        - "Tara"
        - "Gene"
        - "Tick"
      direction: "subject_favored"
      source: "[[sources/PLP-Doug|PLP-Doug]]"
      mechanism: "revive and close sustain reduce the payoff of one-control or poke-based trades, while Doug can heal allies and clip wall-edge targets during objective contact"
      active_when: "map forces those targets to hold gem, ball, zone, or knockout cover where Doug's teammate can enter"
      fails_when: "they keep fully open spacing, clear the close teammate before Doug arrives, or destroy the revive location from range"
      bp_use: "response_pick_candidate_against_control_or_poke_trade"
    - target:
        - "Stu"
        - "Chuck"
      direction: "volatile"
      source: "[[sources/PLP-Doug|PLP-Doug]]"
      mechanism: "Doug can deny a tempo engage with revive, but mobile targets can also reset outside his short radius if they avoid the protected teammate"
      active_when: "their dash or route must finish on the same objective body that Doug is protecting"
      fails_when: "they attack a separate lane, bait Second Serving, or force Doug to walk across open ground"
      bp_use: "route_and_objective_contact_check"
    - target:
        - "Darryl"
        - "Bull"
        - "El Primo"
        - "Emz"
        - "Squeak"
      direction: "target_favored"
      source: "[[sources/PLP-Doug|PLP-Doug]]"
      mechanism: "close burst, displacement, slow, or area denial can punish Doug before heal cycles convert and can cover the revive tile"
      active_when: "objective forces Doug into their preferred range or through a narrow choke"
      fails_when: "Doug has anti-tank teammate damage, Super timing, and cover that lets the protected ally trade first"
      bp_use: "must_avoid_or_draft_damage_support"
    - target:
        - "Piper"
        - "Nani"
        - "Belle"
      direction: "target_favored"
      source: "[[sources/PLP-Doug|PLP-Doug]]"
      mechanism: "long-range burst or precise poke keeps Doug out of range and can pre-aim a revive location"
      active_when: "map has open lanes such as Bounty/Knockout sightlines or opened Gem Grab mid"
      fails_when: "terrain forces them into close objective contact and Doug's team controls the revive tile"
      bp_use: "open_map_counter_warning"

  slot_notes:
    slot_1: "avoid unless map is clearly close-objective and your comp already commits to a Doug-enabled push shell"
    slot_2_3: "usable after seeing enemy lacks open-range punish or after locking a scorer/frontline that converts revive"
    slot_4_5: "best as response into control/poke trade comps on maps with protected entry and clear objective contact"
    slot_6: "strong punish when enemy draft cannot kill through revive twice or cannot cover the revive tile"
```
