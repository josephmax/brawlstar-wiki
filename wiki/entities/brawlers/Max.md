# Max

## 基本信息

- 稀有度：Mythic
- 定位：Support
- 来源：神话辅助英雄

## 攻击特征

- 主攻击是快速发射的长距离多弹丸射击
- 输出稳定，擅长边走边打
- 适合持续施压、追击和撤退掩护

## 超级技能特征

- Super 会提高自己和队友的移动速度
- 能让整队更快进攻、转点或脱离危险
- 兼具节奏推进和团队救援价值

## 适合场景

- 需要快速轮转的模式
- 队伍要一起推进或撤退的对局
- 追击、控场和抢节奏的阵容
- 想把队伍整体速度拉高的团队配合

## 角色定位总结

Max 是速度型支援，她的核心价值是让整队更快地进、退、追和转点。

## 与其他英雄的区别

- 不同于 `Gene`：Gene 用拉人改变站位，Max 用加速改变节奏
- 不同于 `Byron`：Byron 是远程治疗与消耗，Max 是纯节奏支援
- 不同于 `Poco`：Poco 偏群体治疗，Max 偏全队机动性

## 关联页面

- [[sources/Fandom-Max|Fandom 来源摘要: Max]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-17"
    plp: "direct_raw_capture_2026-07-11"
    user_notes: "none"

  capability_vector:
    effective_range: mid_long
    projectile_reliability: medium_high; four quick projectiles with slight spread reward movement mirroring
    burst: medium_high_when_all_projectiles_connect
    sustained_dps: high; four ammo slots and very fast reload
    objective_damage: low_medium; contributes lane pressure more than direct safe race
    mobility: very_high; fast base speed, team Super speed, Phase Shifter dash
    survivability: "medium_high_with_Phase_Shifter_or_Sneaky_Sneakers; 前者有双段免伤 dash 窗口，后者回到锚点时恢复期间损失的生命"
    engage: "high_as_team_tempo_enabler; Super Charged Buffie 还为被 Super 覆盖的队友提供 4 秒 25% 护盾"
    disengage: "high; Super、双段 Phase Shifter 和 Sneaky Sneakers 回程都能重置交火"
    anti_aggro: "medium; speed/two-dash immunity/return anchor 可规避爆发，但无硬控且 dash 仍会保留状态效果"
    anti_tank: medium_if_kiting_space_exists
    wall_break: low
    throw_or_wall_bypass: low; Phase Shifter cannot pass walls or water
    area_control: medium_by_tempo_and_chip_not_zone_denial
    scouting_or_vision: low
    team_support: "very_high; Super 提速改变进退/转点，Super Charged Buffie 给队友 4 秒护盾，Sneaky Sneakers Buffie 在回程锚点治疗附近队友，Hyper Buffie 每次命中给 2.67 格内队友 7% Super 充能"
    tempo_control: high
    source_trace:
      - "[[sources/Fandom-Max|Fandom-Max]]"
      - "[[sources/PLP-Max|PLP-Max]]"

  build_switches:
    - build: "Sneaky Sneakers / Super Charged / Shield, Damage"
      source: "[[sources/PLP-Max|PLP-Max]] / [[sources/Fandom-Max|Fandom-Max]]"
      changes_capabilities:
        - "Sneaky Sneakers 记录一个 3 秒回程锚点；Max 存活回程时恢复期间损失的生命，Buffie 还回满弹药并以同等恢复量治疗锚点附近队友"
        - "Super Charged 让 Max 在自身 Super 生效期间每命中一发延长 0.25 秒加速窗口；Buffie 使被 Super 覆盖的队友获得 4 秒 25% 护盾"
        - "Shield and Damage stabilize mid-range skirmishes while Max keeps tempo"
      enables:
        - team_speed_engage
        - rotation_and_retreat
        - temporary_deep_pressure_with_ammo_reset
        - team_heal_at_safe_return_anchor
        - shielded_team_commitment
      mitigates_failure_modes:
        - need_to_force_short_trade
        - slow_team_rotation
      poor_when:
        - "队伍没有能利用加速进场或追击的队友，Max 会只剩中等输出"
        - "return marker 可被守点，Max 可在 3 秒内被击杀，或队友无法在锚点附近安全接受治疗"
      bp_use: current_plp_default_team_tempo_with_return_anchor
    - build: "Phase Shifter / Run n' Gun mobility variant"
      source: "[[sources/Fandom-Max|Fandom-Max]]"
      changes_capabilities:
        - "Phase Shifter 可瞄准 dash 3.33 格并在 0.5 秒内免疫伤害；Buffie 在首段后 3 秒内给第二次 dash"
        - "两段 dash 都不能穿墙/水，也不清除现有状态，眩晕和击退仍可施加"
        - "Run n' Gun 在移动时提高装填；Buffie 每次普攻命中还给 Max 1 秒 20% 加速"
      enables:
        - projectile_dodge_lane
        - two_step_entry_or_exit
        - sustained_midrange_dps
      mitigates_failure_modes:
        - caught_by_single_high_damage_projectile
        - return_or_dash_anchor_punished
      poor_when:
        - "队伍更需要一次可回收的深压窗口，而不是即时 dash 自保"
        - "路线被墙/水截断，或敌方用持续状态和硬控让免伤 dash 无法完成二次转位"
      bp_use: mobility_build_switch_when_return_anchor_is_unsafe

  map_feature_hooks:
    - map_feature_type: "team_speed_rotation"
      uses_feature_by: "Super 给 Max 和 4 格内队友提速；Super Charged 用命中延长窗口，Buffie 再给队友 4 秒 25% 护盾"
      route_or_position: "wide mid or split-lane map where rotating first creates objective access"
      objective_conversion: "Gem carrier retreat, Hot Zone rotation, Brawl Ball push, Knockout collapse"
      active_when: "team has brawlers that convert speed/shield into pressure or survival, and allies can enter the initial Super radius"
      fails_if: "team is static or split too far, enemy has hard CC, Max cannot land extension shots, or objective does not reward rotation"
      example_maps:
        - Double Swoosh
        - Hard Rock Mine
        - Parallel Plays
        - Center Stage
      bp_use: map_bp_factors.rotation_and_tempo
    - map_feature_type: "open_lane_dodge_pressure"
      uses_feature_by: "fast movement, Run n' Gun hit-speed bursts and the two-dash Phase Shifter window let Max contest projectile lanes without being a pure sniper"
      route_or_position: "open or semi-open lane with dodge space and no hard wall pocket"
      objective_conversion: "keep lane alive, bait sniper shots, create chase window after enemy misses"
      active_when: "enemy damage is projectile-based, Max has room to strafe, and both dash endpoints stay on traversable ground"
      fails_if: "enemy uses unavoidable area control, traps, slows, hard CC, or wall/water geometry truncates the dash"
      example_maps:
        - Shooting Star
        - Out in the Open
        - Dry Season
        - Ring of Fire
      bp_use: candidate_eval.projectile_dodge_lane
    - map_feature_type: "speed_enabled_scoring_or_chase_window"
      uses_feature_by: "team speed plus Super Charged Buffie shield converts a small health or position advantage into a protected score/kill attempt"
      route_or_position: "Brawl Ball midfield or Gem Grab side lane after one enemy is low"
      objective_conversion: "score attempt, gem carrier chase, or collapse on exposed backline"
      active_when: "enemy has spent CC and our team can enter together"
      fails_if: "speed sends team into choke, wall, or anti-aggro setup"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
        - Gem Fort
      bp_use: slot_task.engage_timing_support
    - map_feature_type: "sneaky_sneakers_safe_return_anchor"
      uses_feature_by: "Max 从安全锚点向前压 3 秒后回程，回满弹药并按自身恢复量治疗锚点附近队友"
      route_or_position: "宝石 carrier 撤退线、热区边墙后、或足球中场的己方安全口袋"
      objective_conversion: "用一次可回收换血逼退对手，回程时为自己重装并给保护锚点的队友一次团队恢复"
      active_when: "锚点不在敌方草丛/出生点旁，Max 不会在 3 秒内被秒，队友可在锚点附近安全集结"
      fails_if: "敌方守住回程标记、Max 在回程前被击杀，或队伍终始分路而无法吃到治疗"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Ring of Fire
        - Center Stage
      bp_use: "map_factor_fit.return_anchor_team_reset"
    - map_feature_type: "hyper_close_formation_super_resource"
      uses_feature_by: "Hyper Buffie 期间每命中一发都给 Max 及她 2.67 格内队友 7% Super 充能"
      route_or_position: "热区入口、足球集体推进线或宝石护送站位"
      objective_conversion: "在一次 Hyper 推进内加速队友下一个 Super 窗口，提高连续进攻/守点能力"
      active_when: "Max 能持续命中，队友可在 2.67 格内结阵，且对方没有高收益抱团惩罚"
      fails_if: "队友分线、Max 被逼停火/失准，或敌方范围控制让近距离结阵不安全"
      example_maps:
        - Center Stage
        - Ring of Fire
        - Dueling Beetles
      bp_use: "candidate_eval.hyper_resource_window_not_baseline_support"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - speed_carrier_retreat
        - side_lane_chase
        - mid_pressure_through_constant_chip
        - safe_return_anchor_ammo_and_team_heal
      cannot_fulfill:
        - safe_primary_gem_carrier_without_cover
        - hard_area_denial
      needs_teammate_support:
        - true_mid_control_or_tank_answer
        - bush_vision_if_grass_map
      false_positive: "Speed/return heal only helps if the carrier already has a safe route and can regroup near an uncontested anchor"
    - mode: "Brawl Ball"
      can_fulfill:
        - team_speed_push
        - shielded_team_push_with_Super_Charged_Buffie
        - chase_after_wall_open_or_enemy_mistake
        - emergency_escape
      cannot_fulfill:
        - wallbreak_goal_opening
        - hard_knockback_defense
      needs_teammate_support:
        - scorer_or_wallbreak
        - anti_tank_or_stun
      false_positive: "Fast team movement does not equal scoring if goal geometry is closed"
    - mode: "Bounty"
      can_fulfill:
        - dodge_projectile_lane
        - chase_low_target
        - retreat_after_lead
      cannot_fulfill:
        - low_commitment_long_range_pick
        - thrower_pocket_clear
      needs_teammate_support:
        - long_range_damage_or_pull
        - vision_against_bush_flank
      false_positive: "Max can survive long lanes but may not create stars without a finisher"
    - mode: "Knockout"
      can_fulfill:
        - speed_collapse_after_chip
        - team_retreat_before_gas
        - dodge_and_bait_projectiles
      cannot_fulfill:
        - solo_burst_pick
        - hard_thrower_answer
      needs_teammate_support:
        - teammate_with_burst_or_control
        - anti_CC
      false_positive: "If gas closes into hard control, Max speed may only delay the loss"

  failure_modes:
    - id: "speed_without_conversion"
      active_when: "team has no scorer, finisher, tank, or burst follow-up to exploit Max Super"
      exposed_by: "[[sources/Fandom-Max|Fandom-Max]] Super is movement support, not damage or CC"
      mitigation: "pair with engage, scorer, or burst teammate before valuing Max highly"
      bp_use: "candidate_eval.required_support"
    - id: "hard_control_stops_tempo"
      active_when: "enemy has slow, stun, pull, trap, or silence on the route Max wants to accelerate through"
      exposed_by: "[[sources/Fandom-Max|Fandom-Max]] Phase Shifter still retains status effects"
      mitigation: "bait CC first, choose alternate route, or avoid speed engage plan; Phase Shifter immunity does not cleanse statuses"
      bp_use: "must_avoid_or_plan_protection"
    - id: "return_or_dash_anchor_punished"
      active_when: "Sneaky Sneakers marker is camped, Phase Shifter endpoint is blocked by terrain/control, or Max dies before the three-second return"
      exposed_by: "[[sources/Fandom-Max|Fandom-Max]] Gadget tips warn about ambush at return location"
      mitigation: "place return marker away from bushes/spawn or prefer Phase Shifter"
      bp_use: "false_positive_filter"
    - id: "hyper_resource_requires_close_hits"
      active_when: "BP 计划把 Hyper Buffie 当成全图团队充能，但 Max 无法命中或队友不在她 2.67 格内"
      exposed_by: "[[sources/Fandom-Max|Fandom-Max]] current 7% on-hit nearby-team charge mechanic"
      mitigation: "只在可安全结阵且 Max 有稳定命中窗口时计入，不把它当常驻团队资源"
      bp_use: "team_resource_window_gate"
    - id: "low_pick_pressure_on_pure_long_range"
      active_when: "Max can dodge but cannot threaten kills into true snipers or throwers"
      exposed_by: "[[sources/PLP-Max|PLP-Max]] matchup signals include sniper/control answers"
      mitigation: "add long-range finisher, pull, or wallbreak teammate"
      bp_use: "role_coverage_check"

  conditional_matchup_seeds:
    - target:
        - "Colt"
        - "Nani"
        - "Brock"
        - "Bo"
        - "Tick"
        - "Sprout"
        - "Byron"
        - "Frank"
      direction: "subject_favored"
      source: "[[sources/PLP-Max|PLP-Max]]"
      mechanism: "speed and Phase Shifter let Max dodge linear pressure, close weak angles, or chase immobile targets after chip"
      active_when: "map gives dodge space/two valid dash endpoints and target lacks hard CC or protected pocket"
      fails_when: "target plays behind wall/summon or Max lacks damage follow-up"
      bp_use: "tempo_response_pick_candidate"
    - target:
        - "Tara"
        - "Bea"
        - "Gene"
        - "Ruffs"
        - "Spike"
        - "Carl"
        - "Crow"
        - "Otis"
      direction: "target_favored"
      source: "[[sources/PLP-Max|PLP-Max]]"
      mechanism: "control, slow, pull, silence, or persistent damage punishes Max's speed path and prevents clean tempo conversion"
      active_when: "enemy can hold the route Max must accelerate through"
      fails_when: "Max can bait key tool first or attack from a different lane with teammate cover"
      bp_use: "must_answer_control_before_speed_plan"
    - target:
        - "Piper"
        - "Mandy"
        - "Belle"
        - "Angelo"
      direction: "volatile"
      source: "[[sources/Fandom-Max|Fandom-Max]]"
      mechanism: "Max can dodge and close windows, but loses if long-range target keeps safe angle and Max lacks burst"
      active_when: "wide lane gives Max room and teammate can finish after speed engage"
      fails_when: "sniper has protected line, trap, or teammate peel"
      bp_use: "lane_execution_check"

  slot_notes:
    slot_1: "可在队伍有明确速度/护盾转化者时先手；要接受敌方用硬控、投掷或抱团惩罚回答。"
    slot_2_3: "适合作节奏引擎；预先确定是用 Sneaky 锚点回弹/团疗，还是用 Phase Shifter 双段重定位。"
    slot_4_5: "用于修复转点、追击、撤退或一次受保护的团队进场；不得把 Hyper 7% 充能当常驻辅助。"
    slot_6: "敌方缺硬控/减速且已暴露脆后排时，可用双段 dash 或可回收锚点惩罚；同时检查队友是否能进入护盾/近距充能半径。"
```

## 战斗断点输入

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "Max",
    "target_states": [
      {
        "id": "body",
        "entity_class": "brawler_body",
        "roster_target": true,
        "health": {"amount": 3500, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-Max|Fandom-Max]]"
      }
    ],
    "damage_packets": [],
    "defense_modifiers": [],
    "external_defense_effects": [
      {
        "id": "super_charged_star_buffie_ally_shield",
        "effect": {"type": "damage_reduction", "ratio": 0.25},
        "applies_to": "allies affected by Max Super",
        "active_when": "Super 命中队友后的 4 秒",
        "audit_status": "recorded_not_expanded_across_roster_in_v1",
        "source_ref": "[[sources/Fandom-Max|Fandom-Max]]"
      }
    ],
    "excluded_temporal_defenses": [
      {
        "id": "phase_shifter_immunity",
        "reason": "0.5 秒免疫不是静态 EHP",
        "source_ref": "[[sources/Fandom-Max|Fandom-Max]]"
      }
    ]
  }
}
```
