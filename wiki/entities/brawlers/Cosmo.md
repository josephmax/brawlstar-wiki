---
title: Cosmo
type: brawler
status: bp_ready
updated: 2026-10-28
sources:
  - "[[Fandom-Cosmo]]"
  - "[[PLP-Cosmo]]"
---

# Cosmo

![[../../../raw/assets/brawlers/cosmo.webp]]

## 稳定机制

普攻 Orbit 发射三颗环绕运动的行星，飞行越远体积和伤害越大；贴身与远端伤害不可当成同一个离散伤害包。超级技能 Gravitation Pull 命中后，在目标上形成持续 6 秒的引力区域，影响本人及队友的弹道；不把英雄本体位移攻击视为普通弹道。

## 妙具与星辉

- Planetary Pushback：范围击退；来源冷却为 14 秒。
- Telescope Trap：揭示指定区域 6 秒，包括隐形目标；区域内限制冲刺、跳跃、传送等移动能力；来源冷却为 20 秒。
- Precession：普攻行星的环绕速度增加 25%，不等同于飞行速度增加。
- Ammo Attractor：超级技能命中英雄时补回 2 发弹药。

## 使用边界

需要维持有效距离，近身时普攻伤害下降；用击退恢复距离与用区域限制移动是不同的妙具取舍。PLP 推荐同时保留两种妙具选择，并偏向 Ammo Attractor；它是第三方配装建议，不是不可替换的默认答案。

Fandom Tips 包含“必中”“穿过目标同时伤害金库”等较强推断，不能由弹道吸引机制直接证明，本页不采纳这些保证性结论。六种排位模式已逐项评估，地图与对位只按下列条件使用；没有将全部 PLP 候选提升为事实。

## 资源引用

应用资源目录使用 `brawler:cosmo` 头像，以及以上英文能力名称对应的妙具、星辉资源。本库保存上述 Fandom 肖像原图，出处见 [[新英雄头像与发布状态复核-2026-10]]；有图片不代表排位资格。

## 来源

- [[Fandom-Cosmo]]：机制与能力说明。
- [[PLP-Cosmo]]：第三方配装候选，不能替代正式上线与当前版本验证。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: "bp_ready"
  source_quality:
    fandom: "direct_raw_capture_2026-10-21; mechanics_review_2026-10-28"
    plp: "direct_raw_capture_2026-10-21; source_update_unknown; selective_pair_review_2026-10-28"
  capability_vector:
    effective_range: "long; Orbit 9 tiles; Super 9.33 tiles; not an extreme-range sniper"
    projectile_reliability: "conditional; three orbiting planets spread with distance; aim outer arc, not guaranteed three hits"
    burst: "distance_dependent; Power 11 single planet 500 to 2000; do not multiply by three as guaranteed ammo damage"
    sustained_dps: "limited_by_2_second_reload; Ammo Attractor restores 2 ammo only on Super hit"
    objective_damage: "conditional_at_range; no guaranteed safe piercing or homing safe damage"
    mobility: "normal; no native dash or water crossing"
    survivability: "Power 11 health 6800; relies on spacing and selected gadget, no unconditional self sustain"
    engage: "ranged_mark_and_team_followup; Super must hit first"
    disengage: "conditional_Planetary_Pushback_or_preplaced_Telescope_Trap"
    anti_aggro: "build_and_cooldown_dependent; one gadget only, no permanent movement lock"
    anti_tank: "requires_range_and_team_fire; weak_point_blank_trade"
    wall_break: "none"
    throw_or_wall_bypass: "no_reliable_main_attack_wall_bypass; lobbed_gadget_is_not_damage_lane"
    area_control: "Orbit_arc_pressure; Telescope_Trap_local_movement_denial_for_6_seconds"
    scouting_or_vision: "Telescope_Trap_reveals_area_and_invisible_targets_for_6_seconds"
    team_support: "Super_mark_bends_projectiles_passing_through_its_area_for_6_seconds; no guaranteed kill or body-dash guidance"
    source_trace:
      - "[[sources/Fandom-Cosmo#页面核心字段]]"
      - "[[sources/PLP-Cosmo#逐目标复核（2026-10-28）]]"
  build_switches:
    - build: "Planetary Pushback / Ammo Attractor / Shield, Damage"
      source: "[[sources/PLP-Cosmo]]; [[sources/Fandom-Cosmo]]"
      changes_capabilities:
        - "范围击退恢复距离，14 秒冷却；投掷落点需命中，不能视为常驻免疫"
        - "Super 命中回复 2 发弹药；空大不能补弹"
      enables:
        - "spacing_reset"
        - "marked_target_followup"
      mitigates_failure_modes:
        - "close_range_collapse"
        - "reload_window"
      poor_when:
        - "连续多路进场或妙具空窗；不具备 Telescope Trap 的探查与区域禁位移"
      bp_use: "有接近威胁时优先保留击退自保，不能因此独自承受突脸"
    - build: "Telescope Trap / Ammo Attractor / Shield, Damage"
      source: "[[sources/Fandom-Cosmo]]"
      changes_capabilities:
        - "投掷区域揭示隐形并限制区域内移动能力，持续 6 秒、冷却 20 秒"
        - "替换击退妙具，不会同时拥有 Planetary Pushback"
      enables:
        - "temporary_reveal"
        - "local_movement_denial"
      mitigates_failure_modes:
        - "hidden_flank"
      poor_when:
        - "敌人绕开区域、效果结束后进场或已经贴身；不保证取消已开始的位移"
      bp_use: "队友可保护自身时，用于争夺通路及探查；不能把 Max 加速等同为被封锁的位移"
  map_feature_hooks:
    - id: "cosmo_hideout_side_support"
      map_feature_type: "cosmo_hideout_side_support"
      uses_feature_by: "距离成长普攻维持远程压力；Super 命中后的弹道引导依赖队友射线和弹药"
      route_or_position: "开放边路靠可退掩体输出，避开中央墙后投掷封锁；使用 Telescope Trap 时先探草再转线"
      objective_conversion: "争取边线空间并帮助队友集火拿星，领先后保星"
      active_when: "队友负责中央墙区，Cosmo 有外圈射击距离且能撤回"
      fails_if: "中央投掷无人处理、草丛侧切或边路对手射程压制；不能因 LCQ 出场就忽略阵容"
      example_maps:
        - "Hideout"
      bp_use: "candidate_eval.map_route_and_failure_review"
    - id: "cosmo_shooting_star_followup"
      map_feature_type: "cosmo_shooting_star_followup"
      uses_feature_by: "距离成长普攻维持远程压力；Super 命中后的弹道引导依赖队友射线和弹药"
      route_or_position: "利用局部掩体推进到自身有效距离，队友从相邻射线跟进标记"
      objective_conversion: "远程支援拿星并压住接近路线"
      active_when: "己方有更长线队友承担最远距离对枪；对方不能一直站在 Cosmo 射程外"
      fails_if: "对方极长射程锁线、己方缺反投掷或被迫越过安全线；不是无条件狙击优势"
      example_maps:
        - "Shooting Star"
      bp_use: "candidate_eval.map_route_and_failure_review"
    - id: "cosmo_open_knockout_spacing"
      map_feature_type: "cosmo_open_knockout_spacing"
      uses_feature_by: "距离成长普攻维持远程压力；Super 命中后的弹道引导依赖队友射线和弹药"
      route_or_position: "开阔中路保留退路，与队友错位射击，检查跳板和水域绕侧路线"
      objective_conversion: "争取击杀窗口并保存人数优势"
      active_when: "己方能共同压线，气圈尚未挤掉距离且妙具可用于自保"
      fails_if: "跳板/绕侧突进、队友离场或气圈使近距离不可避免"
      example_maps:
        - "Out in the Open"
      bp_use: "candidate_eval.map_route_and_failure_review"
    - id: "cosmo_bridge_lane_support"
      map_feature_type: "cosmo_bridge_lane_support"
      uses_feature_by: "距离成长普攻维持远程压力；Super 命中后的弹道引导依赖队友射线和弹药"
      route_or_position: "在纵向一路维持距离；确认可达的跨线弹道，不假设自身可过水支援"
      objective_conversion: "先争取路线再让实际金库输出位接触目标，自己有安全距离时补输出"
      active_when: "实际分路可守、队友具备独立金库输出，敌方防守者处于可射击范围"
      fails_if: "被更长射程压出路线、需要近身守库或队伍没有金库伤害；Super 不保证穿过英雄打库"
      example_maps:
        - "Bridge Too Far"
      bp_use: "candidate_eval.map_route_and_failure_review"
  objective_contracts:
    - mode: "Bounty"
      can_fulfill:
        - "ranged_team_followup"
        - "mark_assisted_pick_window"
      cannot_fulfill:
        - "extreme_range_duel_guarantee"
        - "solo_thrower_clear"
      needs_teammate_support:
        - "longer_range_lane_partner"
        - "wall_answer_and_peel"
      false_positive: "拿星依赖先命中和队友跟进，不能靠标记保证击杀；领先后优先保命。"
    - mode: "Knockout"
      can_fulfill:
        - "spaced_poke_and_focus"
        - "temporary_reveal_with_Telescope_Trap"
      cannot_fulfill:
        - "last_ring_close_duel_guarantee"
        - "independent_dive_escape"
      needs_teammate_support:
        - "crossfire_and_peel"
        - "answer_to_protected_thrower"
      false_positive: "气圈和侧切可消除距离成长优势；不能按开局射程推断残局必胜。"
    - mode: "Heist"
      can_fulfill:
        - "ranged_lane_support"
        - "conditional_safe_chip_from_distance"
      cannot_fulfill:
        - "guaranteed_top_safe_dps"
        - "Super_safe_piercing_amplifier"
        - "durable_point_blank_defense"
      needs_teammate_support:
        - "dedicated_safe_damage"
        - "independent_lane_winners"
      false_positive: "PLP 推荐 Heist 不等于金库输出保证；没有可守分路及队友输出时是误选。"
    - mode: "Gem Grab"
      can_fulfill:
        - "ranged_pressure_on_mine_approach"
        - "marked_carrier_focus_with_team"
      cannot_fulfill:
        - "safe_primary_carrier_under_dive"
        - "continuous_bush_control"
      needs_teammate_support:
        - "reliable_gem_carrier"
        - "frontline_and_vision"
      false_positive: "远程辅助职责不能替代持宝和中央站场；本次没有据此提升全部宝石图适配。"
    - mode: "Brawl Ball"
      can_fulfill:
        - "ranged_defender_pressure"
        - "conditional_knockback_defense_with_Planetary_Pushback"
      cannot_fulfill:
        - "primary_ball_carrier"
        - "wallbreak_goal_creation"
        - "guaranteed_goal_line_save"
      needs_teammate_support:
        - "scorer_and_wallbreak"
        - "frontline_and_close_defense"
      false_positive: "贴脸出伤低且无自身位移，不作为单独守门或持球突破解法。"
    - mode: "Hot Zone"
      can_fulfill:
        - "zone_edge_poke"
        - "temporary_entry_denial_with_Telescope_Trap"
      cannot_fulfill:
        - "durable_zone_body"
        - "permanent_zone_movement_lock"
        - "safe_wall_pocket_clear"
      needs_teammate_support:
        - "durable_zone_holder"
        - "anti_thrower"
      false_positive: "区域限制有 6 秒窗口且可绕行；没有站点队友不能把输出空间当占点时间。"
  failure_modes:
    - id: "close_range_collapse"
      active_when: "突进进入近距离，击退/区域限制不在可用窗口"
      exposed_by: "[[sources/Fandom-Cosmo#BP 复核（2026-10-28）]]"
      mitigation: "选定一个自保妙具并保留退路，队友补保护"
      bp_use: "must_avoid_or_needs_protection"
    - id: "reload_window"
      active_when: "2 秒装填期间缺弹，Super 未命中或没有跟进弹药"
      exposed_by: "[[sources/Fandom-Cosmo#BP 复核（2026-10-28）]]"
      mitigation: "留弹、从掩体换弹；Ammo Attractor 不等于无条件续航"
      bp_use: "false_positive_filter"
    - id: "protected_thrower"
      active_when: "敌方墙后攻击覆盖站位，己方无开墙或绕侧能力"
      exposed_by: "[[sources/Fandom-Cosmo#BP 复核（2026-10-28）]]"
      mitigation: "换线或由队友处理投掷；不把吸引弹道当穿墙"
      bp_use: "must_avoid"
    - id: "hidden_flank"
      active_when: "视野外绕侧，Telescope Trap 未选用、未覆盖或已结束"
      exposed_by: "[[sources/Fandom-Cosmo#BP 复核（2026-10-28）]]"
      mitigation: "先探查并保留撤退距离，避免把暂时探查当永久清草"
      bp_use: "needs_protection"
    - id: "mark_without_conversion"
      active_when: "Super 未命中、队友缺弹/射线或目标可撤入掩体"
      exposed_by: "[[sources/Fandom-Cosmo#BP 复核（2026-10-28）]]"
      mitigation: "先建立交叉火力再用标记；不声称必中、瞬杀或金库连带收益"
      bp_use: "false_positive_filter"
  conditional_matchups:
    - target:
        - "Nani"
      direction: "target_favored"
      source: "[[sources/PLP-Cosmo#逐目标复核（2026-10-28）]]; [[sources/Fandom-Nani]]; [[sources/Fandom-Cosmo]]"
      mechanism: "汇聚后的弹体可继续远行，对 Cosmo 的有效射程形成压力；最远处不等于三弹汇聚爆发"
      active_when: "开放直线让 Nani 留在 Cosmo 有效射程外消耗，Cosmo 无侧翼或队友压线"
      fails_when: "Cosmo 利用掩体/侧翼接近有效射程、先命中标记并有队友跟进；Nani 不能维持长线"
      bp_use: "enemy_response_risk; check_map_build_and_team_answer_before_pick"
    - target:
        - "Tick"
      direction: "target_favored"
      source: "[[sources/PLP-Cosmo#逐目标复核（2026-10-28）]]; [[sources/Fandom-Tick]]; [[sources/Fandom-Cosmo]]"
      mechanism: "墙后布雷压缩走位与退路；Cosmo 缺稳定穿墙普攻及破墙，难直接回击"
      active_when: "完整墙体保护 Tick 且布雷能覆盖 Cosmo 的工作位置，队友没有处理投掷"
      fails_when: "墙被打开、Tick 被侧翼或队友驱离；开阔且不能安全布雷时不能套用"
      bp_use: "enemy_response_risk; check_map_build_and_team_answer_before_pick"
    - target:
        - "Sprout"
      direction: "target_favored"
      source: "[[sources/PLP-Cosmo#逐目标复核（2026-10-28）]]; [[sources/Fandom-Sprout]]; [[sources/Fandom-Cosmo]]"
      mechanism: "隔墙投弹及 Hedge 封路打断 Cosmo 保持外圈距离和队友跟进的路线"
      active_when: "墙体和狭路让 Sprout 安全投弹/封路，Cosmo 所在阵容无法开墙或绕侧"
      fails_when: "开放分路或队友破墙解除遮挡；不能仅因 Sprout 是投手就认定所有图占优"
      bp_use: "enemy_response_risk; check_map_build_and_team_answer_before_pick"
    - target:
        - "Mortis"
      direction: "target_favored"
      source: "[[sources/PLP-Cosmo#逐目标复核（2026-10-28）]]; [[sources/Fandom-Mortis]]; [[sources/Fandom-Cosmo]]"
      mechanism: "突进把交战压进 Cosmo 的低伤近圈，命中 Super 的回复帮助继续贴身"
      active_when: "Mortis 有接近路线和弹药，Cosmo 孤立且 Planetary Pushback 或 Telescope Trap 不在有效自保窗口"
      fails_when: "Telescope Trap 覆盖进场区域、及时击退与队友集火，或无接近路线；禁止脱离妙具状态判定"
      bp_use: "enemy_response_risk; check_map_build_and_team_answer_before_pick"
  slot_notes:
    slot_1: "不盲选。先确认长线可接触、反投掷与反突进能由队友补足；有地图适配不代表安全一抢。"
    slot_2_3: "补远程支援与标记集火；敌方未暴露时保留反投掷和自保位置。"
    slot_4_5: "按已知敌人选择击退或区域禁位移；确保队友有弹道、弹药和射线跟进标记。"
    slot_6: "核对实际分路和退路后补选；敌方墙后投掷或可避开妙具的突进未解决则规避，不因 PLP 名单宣称必胜。"
```
