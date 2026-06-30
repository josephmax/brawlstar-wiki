# Mico

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：跳跃机动刺客

## 攻击特征

- 普通攻击会让 Mico 跳跃并在落地时造成范围伤害
- 跳跃过程里拥有极强的机动和穿越能力
- 非常依赖进场、撤退和节奏判断

## 超级技能特征

- Super 会让 Mico 进行更长时间的跳跃
- 他可以在空中控制落点
- 落地时会击退周围敌人，制造很强的冲阵或逃生窗口

## 适合场景

- 需要高机动骚扰的对局
- 后排脆皮多、需要切入的模式
- 地形复杂、可以利用跳跃跨越障碍的地图

## 角色定位总结

Mico 是一个非常纯粹的高机动刺客，核心不在站桩输出，而在用跳跃不断制造威胁、切换位置和打乱对手节奏。

## 与其他英雄的区别

- 不同于 `Mortis`：Mico 更强调空中无敌和落点控制
- 不同于 `Stu`：Mico 更像跳跃刺客，不是连续冲刺型
- 不同于 `Leon`：Mico 的威胁来自跳跃节奏，不是隐身信息差

## 关联页面

- [[sources/Fandom-Mico|Fandom 来源摘要: Mico]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-29"
    user_notes: "none"

  capability_vector:
    effective_range: short_to_mid_with_jump
    projectile_reliability: high_if_target_landing_read_is_correct; misses are expensive
    burst: medium_high_with_ammo_or_Super_landing
    sustained_dps: low; very slow reload and ammo must be conserved
    objective_damage: high_conditional_in_Heist_with_Record_Smash
    mobility: very_high; attack and Super jump over obstacles/water
    survivability: medium; airborne immunity windows but vulnerable on landing and Super delay
    engage: high_against_isolated_backline
    disengage: high_if_ammo_or_Super_available
    anti_aggro: medium; Clipping Scream slow helps escape but Mico lacks sustained brawl
    anti_tank: low_medium; struggles into high health/constant damage
    wall_break: low
    throw_or_wall_bypass: very_high; jumps over walls and lakes
    area_control: low_medium; landing threat controls space but not persistent zone
    scouting_or_vision: low
    team_support: low; disruption and ammo theft are indirect
    objective_burst: high_vs_non_brawlers_with_Record_Smash
    source_trace:
      - "[[sources/Fandom-Mico|Fandom-Mico]]"
      - "[[sources/PLP-Mico|PLP-Mico]]"

  build_switches:
    - build: "Clipping Scream / Record Smash / Shield, Damage"
      source: "[[sources/PLP-Mico|PLP-Mico]]"
      changes_capabilities:
        - "Clipping Scream gives ranged slow to escape or secure landing"
        - "Record Smash doubles damage into Heist safe, boxes and spawnables"
        - "Shield/Damage supports risky landing trades"
      enables:
        - thrower_pocket_dive
        - heist_safe_burst
        - escape_after_entry
      mitigates_failure_modes:
        - slow_reload_after_entry
        - no_escape_if_ammo_empty
      poor_when:
        - "地图和模式不提供非英雄目标或后排口袋，Record Smash 会变窄"
      bp_use: default_reviewed_build_for_knockout_or_heist
    - build: "Presto / Monkey Business pickoff variant"
      source: "[[sources/Fandom-Mico|Fandom-Mico]]"
      changes_capabilities:
        - "Presto extends next jump range for surprise confirm"
        - "Monkey Business steals ammo while restoring Mico ammo"
      enables:
        - longer_gap_close
        - ammo_denial_pickoff
      mitigates_failure_modes:
        - short_range_gap_fail
        - landing_into_enemy_ammo
      poor_when:
        - "需要打 safe 或 spawnables 时，Record Smash 更直接"
      bp_use: last_pick_or_assassin_variant

  map_feature_hooks:
    - map_feature_type: "thrower_pocket"
      uses_feature_by: "jump attacks and Super bypass walls to reach protected backline"
      route_or_position: "wall pocket, layered Bounty lane, or Knockout cover stack"
      objective_conversion: "force thrower/sniper out, secure pick, or collapse protected lane"
      active_when: "target lacks peel and Mico can keep at least one ammo to exit"
      fails_if: "target has bodyguard, constant damage, or Mico lands with no ammo"
      example_maps:
        - Belle's Rock
        - Layer Cake
        - Hideout
        - New Horizons
      bp_use: must_answer_thrower_pocket_candidate
    - map_feature_type: "water_crossing_or_obstacle_bypass"
      uses_feature_by: "attack jump extends over blocks/lakes to nearest ground"
      route_or_position: "water edge or barrier route that shortens access to backline or safe"
      objective_conversion: "surprise entry, retreat over obstacle, or safe access"
      active_when: "bypass creates a kill or objective route and landing is protected"
      fails_if: "jump only crosses terrain into a short-range trap or no objective pressure"
      example_maps:
        - Safe Zone
        - Out in the Open
        - New Horizons
        - Flaring Phoenix
      bp_use: map_bp_factors.route_gate_and_false_positive_filter
    - map_feature_type: "heist_safe_burst_window"
      uses_feature_by: "Record Smash doubles attack damage against Heist safe"
      route_or_position: "safe-facing wall, jump route, or enemy base entry pocket"
      objective_conversion: "short burst safe damage after crossing obstacle or winning lane"
      active_when: "Mico can reach safe without being trapped and team pressures defenders"
      fails_if: "defenders body-block landing or Mico exhausts ammo before safe contact"
      example_maps:
        - Pit Stop
        - Hot Potato
        - Safe Zone
      bp_use: candidate_eval.heist_objective_access

  objective_contracts:
    - mode: "Knockout"
      can_fulfill:
        - route_based_backline_pick
        - final_ring_jump_threat
        - thrower_pocket_answer
      cannot_fulfill:
        - sustained_frontline_hold
        - reliable_multi_target_clear
      needs_teammate_support:
        - chip_or_control_before_entry
        - peel_after_landing
      false_positive: "Jump access is bad if landing does not secure a kill or escape route"
    - mode: "Heist"
      can_fulfill:
        - Record_Smash_safe_burst
        - obstacle_bypass_to_safe
        - punish_spawnables_or_defenders_near_safe
      cannot_fulfill:
        - long_range_safe_angle
        - stable_base_defense
      needs_teammate_support:
        - lane_pressure_to_open_entry
        - anti_tank_or_control_answer
      false_positive: "Heist damage is only real if Mico can repeatedly access safe"

  failure_modes:
    - id: "ammo_empty_after_entry"
      active_when: "Mico spends all attacks for movement and lands unable to damage or escape"
      exposed_by: "[[sources/Fandom-Mico|Fandom-Mico]] very slow reload and tips to keep ammo"
      mitigation: "enter with at least one ammo, use Clipping Scream, or delay until teammate pressure"
      bp_use: "must_avoid_or_needs_support"
    - id: "constant_damage_or_bodyguard_landing"
      active_when: "enemy has Carl/Gigi style constant damage, tank bodyguard, or burst waiting at landing"
      exposed_by: "[[sources/Fandom-Mico|Fandom-Mico]] tips warn against constant-damage enemies"
      mitigation: "avoid direct entry, isolate target, or pair with control"
      bp_use: "false_positive_filter"
    - id: "super_delay_cancelled"
      active_when: "Mico Super is hit by stun, pull, or knockback during the 1-second delay"
      exposed_by: "[[sources/Fandom-Mico|Fandom-Mico]] Super cancellation rule"
      mitigation: "start Super behind cover or after enemy CC is unavailable"
      bp_use: "candidate_eval.execution_risk"
    - id: "bypass_without_objective"
      active_when: "Mico can jump terrain but cannot convert landing into kill, safe damage, or escape"
      exposed_by: "[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]] false-positive rules"
      mitigation: "count only routes tied to target access and follow-up"
      bp_use: "map_factor_false_positive_check"

  conditional_matchup_seeds:
    - target:
        - "Sprout"
        - "Ziggy"
        - "Piper"
        - "Spike"
        - "Mandy"
        - "Bo"
        - "Dynamike"
        - "Poco"
      direction: "subject_favored"
      source: "[[sources/PLP-Mico|PLP-Mico]]"
      mechanism: "Mico jumps over walls and skillshot lanes to reach fragile or pocketed targets"
      active_when: "target is isolated, Mico has ammo, and map offers wall/obstacle route"
      fails_when: "target has peel, bodyguard, hard CC, or landing zone is covered"
      bp_use: "last_pick_or_response_against_backline"
    - target:
        - "Colette"
        - "R-T"
        - "Chester"
        - "Bull"
        - "Sam"
        - "Doug"
        - "Trunk"
        - "Nita"
      direction: "target_favored"
      source: "[[sources/PLP-Mico|PLP-Mico]]"
      mechanism: "high health, anti-dive, spawnables, or burst punish Mico's predictable landing and slow reload"
      active_when: "objective forces Mico to land near these targets or their protected teammate"
      fails_when: "Mico can bypass them and hit an isolated backline or safe"
      bp_use: "must_avoid_or_ban_reason_if_mico_plan"
    - target:
        - "Heist_safe"
        - "Jessie_turret"
        - "Pam_turret"
        - "Mr_P_porters"
      direction: "subject_favored"
      source: "[[sources/Fandom-Mico|Fandom-Mico]]"
      mechanism: "Record Smash doubles damage against non-Brawlers and special targets"
      active_when: "target is reachable and Mico can spend ammo on objective instead of escape"
      fails_when: "defenders body-block landing or Mico needs all ammo to survive"
      bp_use: "objective_or_spawnable_answer_seed"

  slot_notes:
    slot_1: "不宜裸先，除非地图明确奖励跳墙且敌方反刺客池被 ban；否则容易被坦克/控制 2-3 回答。"
    slot_2_3: "可回答早出的投掷/狙击，但必须搭配稳定前线或控制，避免 Mico 单人进场。"
    slot_4_5: "适合补 thrower pocket answer 或 Heist 安全入库路线；检查敌方 6 位 anti-dive。"
    slot_6: "敌方三人缺硬控、缺高血 bodyguard 且后排被墙保护时，Mico 是高收益惩罚位。"
```
