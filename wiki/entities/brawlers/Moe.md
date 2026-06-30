# Moe

## 基本信息

- 稀有度：Mythic
- 定位：Damage Dealer
- 类型：分裂弹远程压制 / Driller 形态地形绕行爆发

## 来源摘要

- Fandom：[[sources/Fandom-Moe|Fandom 来源摘要: Moe]]
- PLP：[[sources/PLP-Moe|PLP 来源摘要: Moe]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Heist, Hot Zone

## 角色定位总结

Moe 的 BP 价值来自两层节奏：普通形态用分裂石块压中远距离、摸草和惩罚固定站位；Super 进入 Driller 形态后用地下路线、击退和短窗爆发制造目标转换。不要把“能钻地/能绕墙”单独当成地图加分，必须同时检查出土后的弹药比例、短手窗口、敌方控制和 DoT。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Moe|Fandom-Moe]]"
    plp: "[[sources/PLP-Moe|PLP-Moe]]"
    user_notes: none

  capability_vector:
    effective_range: long_mid_in_normal; short_high_pressure_in_driller
    projectile_reliability: medium; 普通石块要利用分裂点、墙体或目标走位，Driller 近身更稳定但窗口短
    burst: high_when_super_surfacing_or_driller_ammo_available
    sustained_dps: medium_in_normal; high_short_window_in_driller
    objective_damage: conditional_heist_pressure_after_tunnel_or_lane_win
    mobility: high_with_super_underground_route; conditional_dash_with_Rat_Race
    survivability: medium_low_base_health; underground avoids direct damage but status_or_dot仍可惩罚
    engage: high_if_super_route_reaches_backline_or_objective
    disengage: medium_with_Bail_Out_or_Rat_Race_path
    anti_aggro: conditional; surfacing knockback and short-range Driller damage punish predictable entry
    anti_tank: medium_if_Driller_window_is_protected; poor_if_front_to_front_into_hard_body
    wall_break: conditional_with_Rat_Race_or_route_transform
    throw_or_wall_bypass: high_with_underground_super
    area_control: medium; split rocks and surfacing zone tax chokes
    scouting_or_vision: medium_with_Vision_Gear_or_split_rock_bush_check
    team_support: knockback_disarm_and_terrain_route_creation
    spawnable_or_pet: none
    crowd_control: surfacing_knockback_and_Rat_Race_knockback
    terrain_destruction: conditional_Rat_Race_wall_break

  build_switches:
    - build: Dodgy Digging / Speeding Ticket / Vision, Speed, Shield, Damage
      source: "[[sources/PLP-Moe|PLP-Moe]]"
      changes_capabilities:
        - Dodgy Digging 加速 Super 循环，提升从普通形态进入 Driller 形态的频率
        - Speeding Ticket 让 Driller 窗口更像短时间路线压迫，而不是纯站桩爆发
        - Vision/Speed 只在草图或边路草线能转化成目标访问时升值
      enables:
        - gem_mid_split_pressure
        - brawl_ball_knockback_disarm
        - heist_route_entry
        - hot_zone_entry_clear
      mitigates_failure_modes:
        - slow_super_cycle
        - bush_route_information_gap
      poor_when:
        - 敌方有稳定 anti-tank body、沉默、硬控或 DoT，能在 Moe 出土后立刻惩罚
        - 地图给 Moe 绕行但没有金库、球门、矿区或热区收益
      bp_use: default_competitive_build_with_resource_gate
    - build: Rat Race route-break variant
      source: "[[sources/Fandom-Moe|Fandom-Moe]]"
      changes_capabilities:
        - Driller dash 可破坏障碍并击退敌人，适合处理关键球门墙、金库入口或墙袋
      enables:
        - terrain_state_plan.selective_break
        - brawl_ball_goal_or_disarm_angle
        - heist_base_entry_route
      mitigates_failure_modes:
        - closed_wall_blocks_objective_conversion
      poor_when:
        - 破墙后敌方远程或突进比我方更受益
      bp_use: route_break_variant_when_map_demands

  map_feature_hooks:
    - map_feature_type: brawl_ball_driller_knockback_score_or_disarm
      uses_feature_by: Super 地下接近、出土击退和 Bail Out 让 Moe 能从侧草或墙后切入球权点
      objective_conversion: 把一次出土窗口转成抢球、击退持球者、清门前防守或配合队友射门
      active_when: Moe 有 Super 或即将循环到 Super，队友能接球/补伤害，敌方门前缺沉默或硬击退
      fails_if: 出土后弹药比例不足、球门仍被墙体完全挡住、敌方保留硬控或反坦身体
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_route_entry_with_resource_gate
    - map_feature_type: gem_mid_split_rock_and_bush_choke_control
      uses_feature_by: 普通形态分裂石块可摸草、打墙边和压缩宝石矿附近站位
      objective_conversion: 保护 gem carrier、逼退矿区入口、惩罚敌方从侧草或堡垒入口挤进中路
      active_when: 地图有 H 草、螺旋草或中心入口，Moe 不需要裸钻进敌方三人火力
      fails_if: 敌方持续扫草并用长线压住 Moe，或 Moe 被迫用 Driller 当唯一进矿身体
      example_maps:
        - Hard Rock Mine
        - Double Swoosh
        - Gem Fort
      bp_use: map_bp_factors.mid_choke_split_projectile_pressure
    - map_feature_type: heist_driller_entry_or_safe_disruption
      uses_feature_by: Super 绕墙/过障碍进入敌方半场，Rat Race 可打开障碍并制造短时间金库压力
      objective_conversion: 逼回防、打断敌方 race，或在边路赢线后补一段近身 safe damage
      active_when: 队友已有主 safe DPS 或远程压线，Moe 只需要制造入侵与回防压力
      fails_if: Moe 被当成唯一打库核心，或敌方基地有保留控制/高 DPS 身体清掉 Driller
      example_maps:
        - Hot Potato
        - Pit Stop
        - Safe Zone
        - Safe(r) Zone
      bp_use: candidate_eval.heist_entry_disruption_not_primary_race
    - map_feature_type: terrain_bypass_with_ammo_gate
      uses_feature_by: 地下 Super 可穿过墙体和部分障碍，改变墙袋/热区/淘汰图的 first contact
      objective_conversion: 绕过墙袋压力、压低后排或清热区边缘控制点
      active_when: Moe 入场前有足够弹药，目标没有队友贴身保护，且路线终点能转换成击杀或赶人
      fails_if: 地下路线只把 Moe 送进短手陷阱，或状态/DoT 在地下期间持续压血
      example_maps:
        - Belle's Rock
        - New Horizons
        - Open Business
      bp_use: false_positive_filter.route_bypass_requires_exit_value

  objective_contracts:
    - mode: Gem Grab
      can_fulfill:
        - mid_pressure_with_split_rocks
        - side_route_pick_after_super
        - carrier_retreat_disruption
      cannot_fulfill:
        - stable_primary_gem_carrier_without_peel
      needs_teammate_support:
        - long_range_or_support_to_hold_mid_while_Moe_cycles_super
        - anti_control_or_body_clear_after_driller_exit
      false_positive: 只看 Super 绕后会高估 Moe；如果矿区正面没人站住，绕后只是交换资源
    - mode: Brawl Ball
      can_fulfill:
        - ball_carrier_disarm_with_surfacing_knockback
        - side_route_score_window
        - goal_wall_or_route_pressure_with_Rat_Race_variant
      cannot_fulfill:
        - always_on_goal_wallbreak
      needs_teammate_support:
        - scorer_or_pass_receiver
        - wallbreak_or_cc_if_goal_is_closed
      false_positive: 出土击退不等于进球，必须有射门路线或队友 follow-up
    - mode: Heist
      can_fulfill:
        - forced_recall_entry
        - auxiliary_safe_damage_after_lane_win
        - defender_knockback_or_base_disruption
      cannot_fulfill:
        - pure_remote_safe_DPS
        - solo_race_without_teammate_safe_damage
      needs_teammate_support:
        - real_safe_damage_core
        - lane_control_to_cover_entry
      false_positive: 会钻到金库附近不等于能持续打库
    - mode: Hot Zone
      can_fulfill:
        - entry_clear_with_driller
        - zone_edge_split_rock_pressure
        - control_point_disruption
      cannot_fulfill:
        - durable_primary_zone_body
      needs_teammate_support:
        - zone_holder
        - area_or_sustain_to_keep_zone_after_Moe_clears
      false_positive: Moe 清点后如果无人站圈，Hot Zone 收益会断档

  failure_modes:
    - id: super_exit_ammo_gate
      active_when: Moe Super 前弹药不足或出土后被迫立刻换形态
      exposed_by: Fandom 说明回到普通形态时弹药比例沿用入场前状态
      mitigation: 只在有弹药、队友压线或目标已被迫走位时入场
      bp_use: resource_tracking.before_route_commit
    - id: driller_short_window_trap
      active_when: Driller 窗口结束前没有击杀、进球、打库或撤退路线
      exposed_by: Fandom Driller 形态持续时间与短攻击范围
      mitigation: 把 Driller 当短时间目标转换工具，不当稳定前排
      bp_use: false_positive_filter.short_range_after_bypass
    - id: status_or_dot_during_burrow
      active_when: 敌方保留 DoT、沉默、减速、控制或基地防守资源
      exposed_by: Fandom 地下状态仍可能吃状态/DoT的说明
      mitigation: 先逼资源或让队友吸收控制，再用 Super 切入
      bp_use: must_check_enemy_control_before_pick
    - id: split_rock_reliability_into_fast_mobility
      active_when: 敌方有 Stu/Max/Leon/Mortis 等高速横移或多路线接近
      exposed_by: 分裂石块需要命中分裂点和预判
      mitigation: 选择入口明确地图、搭配减速/视野，或把 Moe 留到后手惩罚低机动阵容
      bp_use: avoid_blind_pick_into_multi_angle_mobility

  conditional_matchup_seeds:
    - target: Sprout_or_Nani_or_Bea_or_Piper_or_Squeak_or_Poco
      direction: subject_favored
      source: "[[sources/PLP-Moe|PLP-Moe]]"
      mechanism: Moe 用分裂石块消耗墙边/长线目标，并用 Super 绕过固定站位或低机动后排的安全距离
      active_when: 目标缺近身保镖，地图给 Moe 分裂角或地下切入路线
      fails_when: 目标有硬 peel、投掷口袋被队友保护，或 Moe 出土点被预判
      bp_use: response_pick_against_fragile_control_or_range
    - target: Jae-Yong_or_Lola
      direction: volatile
      source: "[[sources/PLP-Moe|PLP-Moe]]"
      mechanism: Moe 可以用路线切入惩罚支援/固定输出，但 Jae-yong 的节奏支援和 Lola 的替身/角度会让出土目标选择变难
      active_when: Moe 能先找到真身或支援核心，队友能跟上爆发
      fails_when: 替身、加速或队友保护让 Moe 钻到错误目标或空窗
      bp_use: matchup_requires_target_selection_check
    - target: Chester_or_Damian_or_Ash_or_Draco_or_Rosa_or_Trunk_or_8-Bit_or_Willow
      direction: target_favored
      source: "[[sources/PLP-Moe|PLP-Moe]]"
      mechanism: 高身体、爆发、持续 DPS、沉默/控制或墙控能吃下 Moe 出土窗口并反打短手 Driller
      active_when: 这些目标守住 Moe 必须进入的球门、热区、金库入口或矿区路线
      fails_when: Moe 只打侧面后排，或队友先拆掉控制/身体层
      bp_use: must_avoid_or_require_team_clear_before_Moe_entry
    - target: Ball_carrier_or_goal_defender_or_heist_safe
      direction: subject_favored
      source: "[[sources/Fandom-Moe|Fandom-Moe]]"
      mechanism: Super 出土击退和 Driller 窗口可以直接影响持球者、门前防守者或金库附近防线
      active_when: 目标正在固定位置执行目标动作，Moe 有 Super 且路线终点不被硬控覆盖
      fails_when: 击退没有队友接球/补伤害，或金库防守把 Moe 清掉后 race 继续
      bp_use: objective_specific_route_edge

  slot_notes:
    slot_1: 只在地图明确奖励 Moe 的分裂压制和 Super 路线，且敌方低成本控制面窄时考虑；否则早手容易暴露短窗弱点。
    slot_2_3: 适合作为建立中路压制加目标转换的计划手，但需要队友补站点/打库/得分职责。
    slot_4_5: 用来回答敌方脆弱后排、墙袋或缺 anti-aggro 阵容，同时检查别把强控制或高身体留给敌方 slot_6。
    slot_6: 最适合在敌方三人缺硬控和基地/门前清理时，作为高上限路线惩罚 pick。
```

## 关联页面

- [[sources/Fandom-Moe|Fandom 来源摘要: Moe]]
- [[sources/PLP-Moe|PLP 来源摘要: Moe]]
