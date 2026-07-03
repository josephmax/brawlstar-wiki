# Nita

## 基本信息

- 稀有度：Rare
- 定位：Damage Dealer
- 类型：中距离召唤压制型英雄

## 攻击特征

- 主攻击是中距离震荡波
- 能穿透敌人并同时命中多个目标
- 兼顾范围压制与稳定输出

## 超级技能特征

- Super 会召唤 Bruce
- Bruce 会自动追击敌人并进行近战攻击
- 召唤物会给敌方持续施压，也会帮助占位

## 适合场景

- 中距离对线
- 敌人容易聚堆的局面
- 需要召唤物分担压力的模式
- 偏控制和持续压制的玩法

## 角色定位总结

Nita 是中距离压制与召唤物联动的代表英雄，适合用来理解“本体输出 + 召唤物场面控制”的双层玩法。

## 关联页面

- [[sources/Fandom-Nita|Fandom 来源摘要: Nita]]
- [[sources/PLP-Nita|PLP 来源摘要: Nita]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: mid; Fandom attack range 6 and 6.67 with Hyper Buffie
    projectile_reliability: high_into_grouping_medium_into_open_mobility; wide piercing shockwave rewards lanes and chokepoints
    burst: medium_without_Bruce_high_if_Bear_Paws_or_Hyper_Bear_connects
    sustained_dps: high; very fast reload plus Bruce pressure
    objective_damage: high_if_Bruce_reaches_safe_or_stationary_target
    mobility: low
    survivability: medium; Bruce can body-block and Faux Fur protects the bear, not Nita herself
    engage: medium; Super throw starts pressure, Bear Paws can create catch window
    disengage: medium_with_Bruce_bodyblock
    anti_aggro: conditional_high_when_Bruce_or_Bear_Paws_is_available
    anti_tank: medium_high_if_Bear_Paws_or_Hyper_Bear_sticks
    wall_break: low
    throw_or_wall_bypass: medium; Bruce can be thrown over walls and obstacles
    area_control: high; piercing shockwave plus bear anchor tax entrances and healing
    scouting_or_vision: medium; Bruce chases hidden enemies in bushes
    team_support: medium; Bruce absorbs ammo, protects Nita, and pressures carriers
    spawnable_or_pet: high; Bruce is the core second body
    crowd_control: conditional_stun_from_Bear_Paws
    source_trace:
      - "[[sources/Fandom-Nita|Fandom-Nita]]"
      - "[[sources/PLP-Nita|PLP-Nita]]"

  build_switches:
    - build: "Faux Fur / Hyper Bear / Shield, Damage, Speed"
      source: "[[sources/PLP-Nita|PLP-Nita]]"
      changes_capabilities:
        - "Faux Fur protects Bruce for a short objective window"
        - "Hyper Bear increases Bruce attack frequency, especially valuable when Bruce reaches safe or trapped target"
        - "Shield/Damage/Speed support lane trades and grass-map movement"
      enables:
        - heist_bear_safe_pressure
        - zone_spawnable_anchor
        - lane_ammo_tax
      mitigates_failure_modes:
        - bear_deleted_before_value
        - low_personal_range_against_open_lane
      poor_when:
        - "enemy has splash, pierce, thrower, or high burst that clears Bruce without losing objective position"
      bp_use: default_reviewed_build_for_objective_and_spawnable_pressure
    - build: "Bear Paws / Bear with Me control variant"
      source: "[[sources/Fandom-Nita|Fandom-Nita]]"
      changes_capabilities:
        - "Bear Paws adds a delayed area stun around Bruce"
        - "Bear with Me creates Nita-Bruce sustain loops when both can keep hitting Brawlers"
      enables:
        - anti_dive_stun
        - zone_or_goal_catch_window
        - sustained_bear_bodyguard
      mitigates_failure_modes:
        - diver_reaches_Nita
        - Bruce_needs_to_stick_to_target
      poor_when:
        - "target can kite Bruce, break line, or clear him before the delayed stun lands"
      bp_use: situational_build_for_control_or_anti_aggro

  map_feature_hooks:
    - map_feature_type: "central_congestion_pierce_and_bear_anchor"
      uses_feature_by: "wide piercing shockwaves punish grouped entrances while Bruce blocks, scouts, and taxes ammo"
      route_or_position: "Gem Grab center entrance, side grass lane, or fortress choke where enemies must cross a fixed path"
      objective_conversion: "hold gem mine access, force carrier retreat, or protect mid by creating a second body"
      active_when: "enemy must pass through a choke or grass route and lacks easy splash clear"
      fails_if: "enemy has thrower/splash/chain tools or can ignore Bruce from long range"
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Double Swoosh
      bp_use: map_bp_factors.entrance_blocking_and_spawnable_anchor
    - map_feature_type: "heist_bear_safe_access"
      uses_feature_by: "Nita throws Bruce over enemies or obstacles, then Hyper Bear and Faux Fur convert contact into safe damage"
      route_or_position: "safe-facing wall, side lane entry, or barrier where Bruce can be placed closer than Nita can walk"
      objective_conversion: "force defenders to shoot Bruce, open a safe-damage race window, or split defensive attention"
      active_when: "Nita's lane can deliver Super near the safe and defenders lack instant bear clear"
      fails_if: "Bruce is kited, burst down, or body-blocked before reaching safe"
      example_maps:
        - Hot Potato
        - Pit Stop
      bp_use: candidate_eval.heist_objective_access
    - map_feature_type: "zone_spawnable_anchor"
      uses_feature_by: "Bruce stands between entry and zone while Nita's pierce and Bear Paws/Faux Fur protect the point"
      route_or_position: "Hot Zone entrance, L-wall support pocket edge, or split-zone side where one body must delay entry"
      objective_conversion: "buy zone time, interrupt enemy healing, and force ammo before they step onto zone"
      active_when: "zone fight happens near walls or narrow entries and Nita has Super cycle"
      fails_if: "enemy clears from behind wall, outranges Nita, or double-zone rotation demands more mobility than she has"
      example_maps:
        - Dueling Beetles
        - Ring of Fire
        - Open Business
        - Parallel Plays
      bp_use: map_factor_fit.zone_body_and_ammo_tax

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - Bruce_safe_damage
        - defender_ammo_tax
        - side_lane_pressure_after_Super
      cannot_fulfill:
        - long_range_safe_race_without_Super
        - wallbreak_to_open_safe
      needs_teammate_support:
        - lane control to deliver Bruce
        - wallbreak or ranged DPS if Bruce cannot touch safe
      false_positive: "Nita is a Heist pick only when Bruce can actually reach the safe or force defenders away."
    - mode: "Gem Grab"
      can_fulfill:
        - center_or_side_pierce_control
        - Bruce_carrier_pressure
        - bush_scouting
      cannot_fulfill:
        - safe_primary_gem_carrier_into_long_range
        - pure_sniper_mid_duel
      needs_teammate_support:
        - long-range mid cover on open maps
        - anti-thrower or wallbreak if center is locked
      false_positive: "Bruce pressure does not replace a protected gem carrier if Nita is outranged."
    - mode: "Hot Zone"
      can_fulfill:
        - spawnable_zone_anchor
        - Bear_Paws_clear_window
        - pierce_through_entry
      cannot_fulfill:
        - fast_far_zone_rotation_by_herself
        - safe long-range zone poke
      needs_teammate_support:
        - zone body or healer on extended fights
        - thrower answer if enemy controls wall pocket
      false_positive: "A bear body is not enough if enemy clears zone from safe wall angles."
    - mode: "Brawl Ball"
      can_fulfill:
        - Bruce_bodyblock_for_ball
        - Bear_Paws_goal_or_defense_stun
        - pierce_against_clumped_push
      cannot_fulfill:
        - wallbreak_goal_opening
        - fast solo scorer
      needs_teammate_support:
        - scorer or wallbreak
        - anti-burst protection when Bruce is down
      false_positive: "Nita helps create windows but does not by herself solve closed goal geometry."

  failure_modes:
    - id: "bear_deleted_before_value"
      active_when: "enemy has splash, pierce, chain, high burst, or thrower control that clears Bruce safely"
      exposed_by: "[[sources/Fandom-Nita|Fandom-Nita]] warning that splash/bounce attacks punish hiding behind the bear"
      mitigation: "deploy Bruce after enemy ammo is spent or pair with lane pressure that forces awkward target choice"
      bp_use: "false_positive_filter"
    - id: "open_lane_outranged"
      active_when: "Nita must fight long sightlines before charging Super"
      exposed_by: "[[sources/Fandom-Nita|Fandom-Nita]] medium attack range and low mobility"
      mitigation: "draft her on chokepoints, grass, or objective barriers where pierce and Bruce matter"
      bp_use: "must_avoid_on_pure_open_maps"
    - id: "bear_paws_delay_kited"
      active_when: "target can leave Bruce's radius during Bear Paws delay"
      exposed_by: "[[sources/Fandom-Nita|Fandom-Nita]] Bear Paws activates after a delay and depends on Bruce range"
      mitigation: "use in narrow zone, goal, or wall pocket where target movement is constrained"
      bp_use: "build_requirement_check"
    - id: "split_rotation_limit"
      active_when: "map asks Nita to repeatedly rotate between far objectives"
      exposed_by: "[[sources/Fandom-Nita|Fandom-Nita]] normal movement and Bruce's local pressure pattern"
      mitigation: "assign Nita to a stable lane or pair with mobile teammate for far duty"
      bp_use: "slot_and_map_duty_filter"

  conditional_matchup_seeds:
    - target:
        - "Sandy"
        - "Squeak"
        - "Sprout"
        - "Jae-Yong"
      direction: "subject_favored"
      source: "[[sources/PLP-Nita|PLP-Nita]]"
      mechanism: "Bruce can be thrown over walls or into control pockets while Nita's pierce punishes grouped entrances and prevents easy healing."
      active_when: "walls, entrances, or objective congestion let Bruce reach the target and Nita can follow with pierce"
      fails_when: "target has deeper thrower angle, instant bear clear, or Nita cannot charge Super safely"
      bp_use: "response_pick_candidate_against_control_pocket"
    - target:
        - "Damian"
        - "Edgar"
        - "Barley"
        - "Lumi"
        - "Moe"
        - "Amber"
        - "Juju"
        - "Emz"
      direction: "target_favored"
      source: "[[sources/PLP-Nita|PLP-Nita]]"
      mechanism: "burst dive, thrower control, flame/area denial, or persistent damage can remove Bruce and punish Nita's medium range."
      active_when: "map lets them attack from behind walls, sweep Bruce without stepping forward, or burst Nita before Super value"
      fails_when: "Nita has Super ready, Faux Fur/Bear Paws timing, and teammate pressure that prevents safe bear clear"
      bp_use: "must_answer_before_locking_nita"
    - target:
        - "Fang"
        - "Darryl"
        - "Mortis"
        - "Bull"
      direction: "volatile"
      source: "[[sources/Fandom-Nita|Fandom-Nita]]"
      mechanism: "Bruce can body-block non-piercing dives and Bear Paws can punish close-range entry, but Nita loses if the diver reaches her while Bruce is absent."
      active_when: "Nita has Super or Bear Paws and the diver must pass through a narrow route"
      fails_when: "diver baits Bruce, attacks from open angle, or bursts Nita before the stun/body-block matters"
      bp_use: "anti_aggro_resource_check"

  slot_notes:
    slot_1: "可在 Gem/Hot Zone/Heist 的拥挤目标图先手，但要确认敌方 2-3 位不能低成本拿 thrower 或 splash 清 Bruce。"
    slot_2_3: "适合作为回答无 bear clear 的控制/短手计划，同时另一手补射程或开墙。"
    slot_4_5: "用于补 Heist 打库、Hot Zone 身体或 Gem Grab 入口封锁；必须检查敌方 6 位是否能一手清召唤物。"
    slot_6: "当敌方缺 splash/thrower、目标必须过窄口或安全区可被 Bruce 接触时，Nita 可以作为高收益惩罚。"
```
