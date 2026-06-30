# Belle

## 基本信息

- 稀有度：Epic
- 定位：Marksman
- 类型：超远程标记型射手

## 攻击特征

- 主攻击是超远距离电弧弹体
- 命中后可在敌人之间跳弹
- 适合从安全距离持续点名和压线

## 超级技能特征

- Super 会标记目标
- 被标记敌人会承受更高后续伤害
- 非常适合为团队制造集火目标

## 适合场景

- 开阔地图
- 需要持续压线的模式
- 需要团队集火某个关键目标的对局

## 角色定位总结

Belle 是超远程点名和伤害放大的代表英雄。和 `Brock` 相比，她更像“标记器”而不是“炮击机”；和 `Piper` 相比，她的价值更稳定地体现在团队集火上。

## 关联页面

- [[sources/Fandom-Belle|Fandom 来源摘要: Belle]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-29"
    user_notes: "none"

  capability_vector:
    effective_range: very_long; Fandom attack range 10 and Super range 10.67
    projectile_reliability: high_on_open_lines; fast bolt, but bounce value requires nearby enemies
    burst: medium_alone_high_with_mark_followup
    sustained_dps: medium_high; fast reload and repeat poke
    objective_damage: medium; Heist fit comes from safe lane pressure, not from Super mark on safe
    mobility: low
    survivability: low_base_health_medium_with_Positive_Feedback
    engage: low; prefers forcing separation rather than initiating
    disengage: low_medium_with_Nest_Egg_route_tax
    anti_aggro: conditional; Nest Egg slow and Super mark punish entry but do not guarantee escape
    anti_tank: high_if_marked_and_distance_kept
    wall_break: low
    throw_or_wall_bypass: conditional_with_Reverse_Polarity
    area_control: medium; trap chokepoints and bounce punishes grouping
    scouting_or_vision: low_medium; trap trigger gives route information but no true reveal
    team_support: high; Spotter increases damage from any source on one target
    crowd_control: conditional_slow_from_Nest_Egg
    source_trace:
      - "[[sources/Fandom-Belle|Fandom-Belle]]"
      - "[[sources/PLP-Belle|PLP-Belle]]"

  build_switches:
    - build: "Nest Egg / Positive Feedback / Shield, Reload"
      source: "[[sources/PLP-Belle|PLP-Belle]]"
      changes_capabilities:
        - "Nest Egg adds choke and flank tax against aggro"
        - "Positive Feedback raises poke-lane survivability when Belle keeps landing attacks"
        - "Reload Gear supports repeated long-range chip and mark cycling"
      enables:
        - long_range_lane_control
        - choke_trap_control
        - marked_target_focus_plan
      mitigates_failure_modes:
        - no_escape_into_aggro
        - low_health_poke_trade
      poor_when:
        - "敌方主要答案是隔墙投掷或召唤物消耗，Nest Egg 很难接触关键目标"
      bp_use: default_reviewed_build_for_open_or_choke_maps
    - build: "Reverse Polarity / Grounded situational variant"
      source: "[[sources/Fandom-Belle|Fandom-Belle]]"
      changes_capabilities:
        - "Reverse Polarity lets the next bolt bounce from walls for surprise reach"
        - "Grounded can punish ammo-dependent close-range targets after Spotter hits"
      enables:
        - off_angle_wall_bounce
        - anti_reload_window_after_mark
      mitigates_failure_modes:
        - target_hiding_behind_single_wall
        - tank_or_assassin_with_ammo_committed
      poor_when:
        - "需要稳定全天候生存时，Positive Feedback 通常更可靠"
      bp_use: situational_build_requirement

  map_feature_hooks:
    - map_feature_type: "long_sightline"
      uses_feature_by: "very long bolt controls exposed lanes while Spotter creates a focus target"
      route_or_position: "open lane or safe lane where Belle can keep max range and avoid side entry"
      objective_conversion: "Bounty/Knockout low-commitment chip and Heist lane pressure"
      active_when: "sightline stays open and enemy entry path is predictable"
      fails_if: "walls or thrower pockets deny line, or enemy gets multiple covered approach paths"
      example_maps:
        - Shooting Star
        - Dry Season
        - Out in the Open
        - Bridge Too Far
      bp_use: required_capabilities.long_range_pressure
    - map_feature_type: "choke_trap_and_grouping_tax"
      uses_feature_by: "Nest Egg slows a key passage while Belle bounce punishes clustered enemies"
      route_or_position: "zone entrance, gem mid entrance, or lane funnel that enemies must cross"
      objective_conversion: "Hot Zone entry denial, Gem Grab mid tax, and Bounty split pressure"
      active_when: "enemy must enter through a known choke or tends to group near objective"
      fails_if: "enemy can trigger safely with summons, play from thrower pocket, or ignore the choke"
      example_maps:
        - Parallel Plays
        - Ring of Fire
        - Gem Fort
        - Hard Rock Mine
      bp_use: map_bp_factors.vision_tax_or_choke_control
    - map_feature_type: "single_target_focus_window"
      uses_feature_by: "Spotter marks one target for amplified team damage"
      route_or_position: "lane where a tank, gem carrier, or exposed defender must be focused"
      objective_conversion: "turn one marked target into kill, gem drop, zone clear, or safe lane win"
      active_when: "team has damage follow-up and target cannot immediately break line"
      fails_if: "Belle marks the wrong target, follow-up is absent, or target hides behind wall"
      example_maps:
        - Open Business
        - Hideout
        - New Horizons
      bp_use: candidate_eval.focus_fire_support

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - long_range_lane_pressure
        - anti_tank_or_aggro_mark_if_enemy_entries
        - choke_trap_route_delay
      cannot_fulfill:
        - direct_Spotter_safe_amplification
        - body_on_safe_or_wallbreak
      needs_teammate_support:
        - true_safe_dps
        - thrower_or_wall_answer_if_lane_blocked
      false_positive: "Heist value drops if Belle only pokes lanes and the team lacks safe damage"
    - mode: "Hot Zone"
      can_fulfill:
        - zone_entry_trap
        - long_range_zone_poke
        - marked_target_clear
      cannot_fulfill:
        - tank_body_on_zone
        - persistent_thrower_clear
      needs_teammate_support:
        - zone_body_or_sustain
        - anti_thrower_if_walls_intact
      false_positive: "A trap on entry is not enough if enemies clear zone from behind walls"
    - mode: "Bounty"
      can_fulfill:
        - low_commitment_star_pressure
        - force_enemy_spacing
        - focus_mark_for_pick
      cannot_fulfill:
        - close_range_escape
        - hard_engage_when_behind
      needs_teammate_support:
        - peel_against_assassins
        - wall_or_thrower_answer
      false_positive: "Long range is unsafe if enemy can approach through layered cover"
    - mode: "Knockout"
      can_fulfill:
        - opening_poke
        - marked_target_finish
        - trap_final_ring_entry
      cannot_fulfill:
        - solo_close_range_duel
        - guaranteed_thrower_answer
      needs_teammate_support:
        - followup_damage
        - anti_dive_or_wallbreak
      false_positive: "If Belle cannot keep range before gas closes, her low mobility becomes exposed"

  failure_modes:
    - id: "no_escape_into_aggro"
      active_when: "assassin, tank, or speed lane reaches Belle before Nest Egg or mark converts"
      exposed_by: "[[sources/Fandom-Belle|Fandom-Belle]] low health and tips on close-range vulnerability"
      mitigation: "hold max range, place Nest Egg on approach, pair with peel or lane control"
      bp_use: "false_positive_filter"
    - id: "mark_without_followup"
      active_when: "Spotter lands on a target that teammates cannot damage or that can hide safely"
      exposed_by: "[[sources/Fandom-Belle|Fandom-Belle]] Super is single-target amplification"
      mitigation: "draft burst follow-up and choose lanes where marked target must remain exposed"
      bp_use: "candidate_eval.required_support"
    - id: "thrower_or_wall_pocket_denies_line"
      active_when: "walls, L-corners, or thrower pockets prevent Belle from seeing the objective target"
      exposed_by: "[[sources/PLP-Belle|PLP-Belle]] counteredBy throwers and wall-dependent picks"
      mitigation: "pair wallbreak, avoid blind lane, or reserve Belle for open sightline maps"
      bp_use: "must_answer_or_avoid"
    - id: "grouping_tax_not_active"
      active_when: "enemy spacing is disciplined, summons absorb bounce value, or objective does not force clustering"
      exposed_by: "[[sources/Fandom-Belle|Fandom-Belle]] bounce mechanic only triggers on nearby targets"
      mitigation: "treat Belle as single-target poker and do not overvalue chain damage"
      bp_use: "false_positive_check"

  conditional_matchup_seeds:
    - target:
        - "El Primo"
        - "Jacky"
        - "Shelly"
        - "Buzz"
        - "Hank"
        - "Frank"
      direction: "subject_favored"
      source: "[[sources/PLP-Belle|PLP-Belle]]"
      mechanism: "very long poke plus Spotter amplification punishes bulky or linear targets before they connect"
      active_when: "map has long lanes, target lacks covered entry, and Belle has team damage follow-up"
      fails_when: "target uses grass/walls/speed support to force close range or Belle lacks peel"
      bp_use: "response_pick_candidate_against_linear_frontline"
    - target:
        - "Sprout"
        - "Barley"
        - "Willow"
        - "Larry & Lawrie"
      direction: "target_favored"
      source: "[[sources/PLP-Belle|PLP-Belle]]"
      mechanism: "throwers and wall control deny Belle's line while pressuring her low health"
      active_when: "walls remain intact and Belle has no wallbreak or dive teammate"
      fails_when: "terrain opens or Belle can play a separate long lane outside thrower reach"
      bp_use: "must_answer_thrower_pocket_before_picking"
    - target:
        - "Bibi"
        - "Rosa"
        - "Sandy"
        - "Chuck"
      direction: "target_favored"
      source: "[[sources/PLP-Belle|PLP-Belle]]"
      mechanism: "speed, cover, or route compression can bypass Belle's range and punish her lack of hard escape"
      active_when: "map creates grass/choke entry or objective forces Belle to stand near the route"
      fails_when: "Belle controls approach with Nest Egg and has peel or wide open retreat space"
      bp_use: "slot_6_punish_warning"

  slot_notes:
    slot_1: "可在开阔 Bounty/Knockout 或长线 Heist 先手，但要确认敌方 2-3 位没有低成本投掷/突脸组合。"
    slot_2_3: "适合作为长线回答或配合爆发队友建立 marked-target 计划。"
    slot_4_5: "用于补长线、反前排或 Hot Zone 入口税；同时检查敌方 6 位是否能补 thrower/dive。"
    slot_6: "当敌方缺投掷、缺侧路突脸且必须过窄口时，可以作为惩罚性安全输出。"
```
