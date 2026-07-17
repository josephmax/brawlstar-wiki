# R-T

## 基本信息

- 稀有度：Mythic
- 定位：Damage Dealer
- 类型：标记增伤长线 / 分体反突进身体

## 来源摘要

- Fandom：[[sources/Fandom-R-T|Fandom 来源摘要: R-T]]
- PLP：[[sources/PLP-R-T|PLP 来源摘要: R-T]]
- PLP 推荐模式候选：Bounty, Knockout

## 角色定位总结

R-T 的 BP 价值分为两种形态：普通形态用长射程标记把一次命中变成全队集火窗口；分体形态的头与腿各自释放 1240 基础伤害的短距瞬时范围信号，能直接惩罚贴近、绕墙和单一路线身体。分体不是免费增强，腿部静止、可被炮台/溅射/穿透处理，且 Hot Zone 只计算移动的头部站圈，BP 必须把“高伤分体能否覆盖接触点”和“分体后是否会送双端弱点”拆开判断。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-07-17
    plp: "[[sources/PLP-R-T|PLP-R-T]]"
    user_notes: none

  capability_vector:
    effective_range: very_long_in_normal; short_dual_area_in_split
    projectile_reliability: medium_high_on_open_lane; drops_if_enemy_uses_walls_or_speed
    burst: very_high_if_mark_is_consumed_or_split_dual_area_hits; 头与腿的 Eat Static 各有 1240 基础伤害并可穿墙瞬时生效
    sustained_dps: medium_in_normal_high_in_short_split_contact; 普通形态更依赖标记转化，分体形态以 1.8 秒装填维持近距双端压力
    objective_damage: low_direct_heist_value
    mobility: low_normal; medium_in_split_head_with_water_crossing
    survivability: medium; split_form_is_high_risk_because_head_or_legs_death_kills_R-T
    engage: low_in_normal; medium_as_split_counter_entry
    disengage: medium_with_Radar_Waves_recall
    anti_aggro: very_high_if_split_ready_endpoint_safe_and_contact_visible
    anti_tank: high_against_single_route_body_when_1240_split_pulses_can_overlap_or_mark_converts
    wall_break: none
    throw_or_wall_bypass: medium_in_split_area_signals_through_walls
    area_control: medium_high_on_short_routes_with_split_dual_1240_radius_and_mark_threat
    scouting_or_vision: low
    team_support: mark_damage_amplification_for_allies
    spawnable_or_pet: split_legs_as_stationary_body_liability
    crowd_control: low
    terrain_creation: none

  build_switches:
    - build: Out Of Line / Quick Maths / Shield, Damage, Health
      source: "[[sources/PLP-R-T|PLP-R-T]]"
      changes_capabilities:
        - Out Of Line 提供立即进入分体的资源开关；1240 基础伤害 Eat Static 让它既是反突进，也能在短口/墙边目标争夺前预置直接威胁
        - Quick Maths 延长标记持续时间，让 Bounty/Knockout 的集火窗口更稳定
        - Shield/Health 缓解 R-T 分体或长线被开到时的血量风险
      enables:
        - long_lane_mark_focus
        - split_form_anti_aggro
        - round_lead_bodyguard
      mitigates_failure_modes:
        - no_super_when_dive_arrives
        - mark_window_too_short
      poor_when:
        - 敌方能用穿透、溅射、炮台或召唤物稳定打腿
      bp_use: bounty_knockout_default_with_split_resource_tracking

  map_feature_hooks:
    - map_feature_type: bounty_knockout_long_mark_focus
      uses_feature_by: 10 格直线攻击给目标挂标记，让队友下一击获得额外伤害
      objective_conversion: 低风险拿星、逼退、保回合血量领先或把一枪命中变成击杀确认
      active_when: 长线清晰、敌方必须 peek，且我方有能吃标记收益的远程/爆发队友
      fails_if: 墙体完整遮挡直线、敌方高机动反复破线，或 R-T 被迫单人守近身路线
      example_maps:
        - Shooting Star
        - Dry Season
        - Belle's Rock
        - New Horizons
      bp_use: map_bp_factors.long_lane_mark_focus
    - map_feature_type: split_form_anti_aggro_wall_body
      uses_feature_by: 分体后头和腿各自释放 1240 基础伤害的近距离瞬时范围信号，可隔墙惩罚跳脸、滚入或短手绕墙
      objective_conversion: 保护后排、守淘汰回合空间、阻止球路或入口突进
      active_when: 腿部能藏在安全点，头/腿至少一端能覆盖接触点，敌方突进路线单一且必须进入短范围
      fails_if: 腿暴露给炮台/投掷/穿透，或敌方直接绕开 R-T 打队友
      example_maps:
        - Belle's Rock
        - New Horizons
        - Center Stage
      bp_use: candidate_eval.split_form_endpoint_guard
    - map_feature_type: gem_or_ball_split_speed_objective_touch
      uses_feature_by: 分体头部移速更快且可越水，能短时间抢宝石、追球或用 1240 基础范围信号清接触点
      objective_conversion: 争矿、救球、追击 low HP carrier 或清短口，而不是稳定站点
      active_when: 使用目标是一次性触碰/追击，腿部安全且 Radar Waves 可回收
      fails_if: 队伍要求 R-T 当主 carrier/scorer，或腿部被敌方固定火力处理
      example_maps:
        - Hard Rock Mine
        - Double Swoosh
        - Center Stage
      bp_use: objective_specific_split_touch_with_leg_safety
    - map_feature_type: hot_zone_head_only_presence_filter
      uses_feature_by: 分体头能进入区域但腿不会计入 Hot Zone，占圈价值低于直觉
      objective_conversion: 只适合短时间清入口或救远圈，不适合作主站圈身体
      active_when: 队伍已有 zone body，R-T 只需要阻止敌方进入或追击低血目标
      fails_if: draft 把分体腿当成站圈单位，或敌方 area/splash 把头腿一起打穿
      example_maps:
        - Dueling Beetles
        - Open Business
        - Parallel Plays
        - Ring of Fire
      bp_use: false_positive_filter.split_body_not_zone_anchor

  objective_contracts:
    - mode: Bounty
      can_fulfill:
        - long_range_mark_pressure
        - star_lead_bodyguard
        - anti_dive_split_guard
      cannot_fulfill:
        - route_based_assassin_or_fast_blue_star_rush
      needs_teammate_support:
        - teammate_damage_to_consume_marks
        - leg_cover_or_anti_thrower_if_split
      false_positive: 标记强不代表 R-T 能独自处理多角度刺客
    - mode: Knockout
      can_fulfill:
        - round_space_control
        - first_pick_focus_fire
        - split_form_close_route_guard
      cannot_fulfill:
        - safe_wall_pocket_thrower_clear_without_line
      needs_teammate_support:
        - wallbreak_or_thrower_answer_when_lines_are_closed
        - peel_against_pierce_or_splash
      false_positive: 分体守路必须确认腿部不会成为免费目标
    - mode: Gem Grab
      can_fulfill:
        - mark_focus_on_mid_target
        - emergency_carrier_chase_or_touch
      cannot_fulfill:
        - durable_primary_gem_carrier
      needs_teammate_support:
        - carrier
        - grass_or_wall_control
      false_positive: 分体快移速适合抢节奏，不适合长期带宝石
    - mode: Hot Zone
      can_fulfill:
        - anti_aggro_entry_guard
        - marked_focus_on_zone_body
      cannot_fulfill:
        - primary_zone_body_in_split_form
      needs_teammate_support:
        - real_zone_holder
        - area_clear_after_R-T_marks
      false_positive: 腿不计入站圈，不能把分体当双单位占点

  failure_modes:
    - id: split_legs_unprotected
      active_when: 分体腿留在可被投掷、炮台、溅射或穿透攻击的位置
      exposed_by: Fandom 分体任一部分死亡都会让 R-T 死亡
      mitigation: 只在腿部有墙体/队友保护且敌方缺低成本清腿时分体
      bp_use: hard_gate.before_split_form_pick
    - id: split_low_hp_commit
      active_when: R-T 低血量仍分体，头或腿任一端被秒
      exposed_by: Fandom 建议只在满血或近满血时分体
      mitigation: 先回血/等回合空间稳定，再把分体作为守路资源
      bp_use: resource_tracking.health_threshold
    - id: pierce_splash_hits_both_parts
      active_when: 敌方有 Penny、Jessie、Carl、Rico、Grom、Barley 等能同时压头腿的技能
      exposed_by: Fandom tips 对穿透、炮台和溅射的警告
      mitigation: 避免在相同弹道线上放头腿，或不在这些敌方资源在线时分体
      bp_use: enemy_resource_filter
    - id: mark_without_team_conversion
      active_when: R-T 命中标记但队友无法安全补下一击
      exposed_by: Fandom 标记由 R-T 或队友后续攻击触发额外伤害
      mitigation: 搭配长线/爆发队友，或把 R-T 当个人 poke 而非击杀核心
      bp_use: comp_synergy_check

  conditional_matchup_seeds:
    - target: Mico_or_El_Primo_or_Melodie_or_Sam_or_Buzz_or_Hank_or_Lily_or_Kaze
      direction: subject_favored
      source: "[[sources/PLP-R-T|PLP-R-T]]"
      mechanism: 分体头腿各自 1240 基础范围伤害与标记集火，能惩罚必须进入短距离的跳脸、滚入、冲刺或高身体路线
      active_when: 突进路线可见、腿部安全、R-T 有 Super 或 Out Of Line 可立即分体
      fails_when: 目标绕开 R-T 打后排，或先用队友资源清腿/逼分体
      bp_use: anti_aggro_response_pick
    - target: Marked_high_value_target
      direction: subject_favored
      source: "[[sources/Fandom-R-T|Fandom-R-T]]"
      mechanism: 标记让队友下一次命中获得额外伤害，适合把低血量远程、carrier 或 round target 转成击杀
      active_when: 队友有稳定命中或 burst，且目标必须继续 peek 目标区
      fails_when: 标记后无队友角度，目标脱战，或盟友命中被召唤物/body block 吃掉
      bp_use: team_focus_fire_edge
    - target: Najia_or_Grom_or_Colette_or_Sandy_or_Leon_or_Pierce_or_Mina_or_Mortis
      direction: target_favored
      source: "[[sources/PLP-R-T|PLP-R-T]]"
      mechanism: 远程毒/投掷、百分比伤害、隐身接近、资源型 marksman、控制或刺客能打破 R-T 的长线标记与分体安全
      active_when: 地图有墙袋、侧草、隐身路线或 R-T 腿部暴露点
      fails_when: 地图纯长线且 R-T 有队友保护，目标无法绕开标记火力
      bp_use: must_answer_before_R-T_core_plan
    - target: Penny_or_Jessie_or_Carl_or_Pierce_or_thrower_splash
      direction: target_favored
      source: "[[sources/Fandom-R-T|Fandom-R-T]]"
      mechanism: 炮台、弹射、穿透和投掷可以清腿、打头腿同线，或迫使 R-T 不能使用分体形态
      active_when: 这些资源能从安全位置碰到腿或绕过墙体
      fails_when: 腿部安全、地形打开成 R-T 长线，或队友先清掉资源
      bp_use: split_form_liability_filter

  slot_notes:
    slot_1: 适合长线 Bounty/Knockout 先手，但必须确认敌方低成本清腿和多角突进面不宽。
    slot_2_3: 可作为长线体系核心或反突进保护手，最好搭配能吃标记的稳定输出。
    slot_4_5: 用来回答敌方短手/刺客或单一短口计划；1240 分体范围伤害提高接触点惩罚，但仍要检查敌方最后手能否用投掷/炮台处理腿。
    slot_6: 如果敌方三人缺穿透/溅射/炮台且必须从单一路线进场，R-T last pick 的反突进上限很高。
```

## 关联页面

- [[sources/Fandom-R-T|Fandom 来源摘要: R-T]]
- [[sources/PLP-R-T|PLP 来源摘要: R-T]]

## 战斗断点输入

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "R-T",
    "target_states": [
      {
        "id": "body",
        "entity_class": "brawler_body",
        "roster_target": true,
        "health": {"amount": 4100, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-R-T|Fandom-R-T]]"
      },
      {
        "id": "split_head_full_health",
        "entity_class": "brawler_split_part",
        "roster_target": false,
        "health": {"amount": 4100, "at_power_level": 1, "scaling": "standard"},
        "state_rule": "实际分体头继承启动瞬间当前血量；此状态只表示满血启动",
        "source_ref": "[[sources/Fandom-R-T|Fandom-R-T]]"
      },
      {
        "id": "split_legs",
        "entity_class": "brawler_split_part",
        "roster_target": false,
        "health": {"amount": 3900, "at_power_level": 1, "scaling": "standard"},
        "intrinsic_damage_reduction": 0.29,
        "intrinsic_modifier_id": "split_legs_intrinsic",
        "state_rule": "独立可被击破目标；任一部分被击破即淘汰 R-T",
        "source_ref": "[[sources/Fandom-R-T|Fandom-R-T]]"
      }
    ],
    "damage_packets": [
      {
        "id": "main.split_eat_static_impact",
        "ability_kind": "main_attack",
        "form": "split",
        "packet_unit": "one_body_impact",
        "delivery_variant": "impact",
        "repeat_model": "resource_gated",
        "damage": {"amount": 1240, "at_power_level": 1, "scaling": "standard"},
        "active_when": "分体形态中头或腿的一次范围命中；双端同时命中必须另建组合包",
        "source_conflict_status": "none",
        "source_ref": "[[sources/Fandom-R-T|Fandom-R-T]]"
      }
    ],
    "defense_modifiers": [
      {
        "id": "recording_split_head",
        "source_kind": "star_power",
        "applies_to_states": ["split_head_full_health"],
        "loadout_group": "star_power",
        "effect": {"type": "damage_reduction", "ratio": 0.20},
        "active_when": "分体且装备 Recording",
        "source_ref": "[[sources/Fandom-R-T|Fandom-R-T]]"
      },
      {
        "id": "recording_split_legs",
        "source_kind": "star_power",
        "applies_to_states": ["split_legs"],
        "loadout_group": "star_power",
        "effect": {"type": "damage_reduction", "ratio": 0.50},
        "replaces_intrinsic_damage_reduction": true,
        "active_when": "分体且装备 Recording；替代默认 29% 而非与其相加",
        "source_ref": "[[sources/Fandom-R-T|Fandom-R-T]]"
      }
    ]
  }
}
```
