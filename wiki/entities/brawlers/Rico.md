# Rico

## 基本信息

- 稀有度：Super Rare
- 定位：Damage Dealer
- 类型：远程反弹射手

## 攻击特征

- 主攻击的子弹会在墙体间反弹
- 擅长利用地形延长射程和改变角度
- 在狭窄地形里更容易打出高收益

## 超级技能特征

- Super 会发射更长、更密集的弹射子弹
- 子弹可穿透敌人并继续反弹
- 能把墙体地形转化成持续火力优势

## 适合场景

- 墙体多、走廊多的地图
- 需要远距离消耗和压线的模式
- 需要通过角度打穿敌方站位的对局

## 角色定位总结

Rico 是最典型的反弹路线输出之一。耐久墙体是他的最高收益来源；`Multiball Launcher` 能部署自动贩卖机作为临时掩体与人工反弹面，`Bouncy Castle` 则提供不消耗弹药的分裂弹道和 Buffie 减速窗口。因此他的 BP 路径包括耐久墙廊输出与临时人工反弹/控制，但不能把有冷却、可被清除的贩卖机当成永久地形。

## 关联页面

- [[sources/Fandom-Rico|Fandom 来源摘要: Rico]]
- [[sources/PLP-Rico|PLP 来源摘要: Rico]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-17"
    plp: "direct_raw_capture_2026-06-29"
    user_notes: "none"

  capability_vector:
    effective_range: "very_long_with_bounces; 普攻 9.67 格，每次反弹增加路程，Super 可穿透并反弹"
    projectile_reliability: "high_in_corridors_medium_in_open_field; 固定墙面或贩卖机可约束角度，纯开阔线仍要靠五弹串命中"
    burst: "high_if_bounce_volley_vending_explosion_or_split_projectiles_connect"
    sustained_dps: "high; 1.1 秒快装填，可持续用墙面压线"
    objective_damage: "high_conditional_on_durable_bounce_lane_or_safe_angle"
    mobility: "low_base_high_at_low_health_with_Robo_Retreat; 低于 40% HP 提速，Buffie 在极低血时最高提到 60%"
    survivability: "low_base_conditional_with_vending_cover_Bouncy_slow_or_Robo_Retreat; Bouncy Castle 不提供自疗"
    engage: "low_medium_with_Bouncy_Castle_slow_or_vending_angle"
    disengage: "medium_with_vending_cover_Bouncy_slow_or_Robo_Retreat"
    anti_aggro: "conditional; 墙廊反弹、贩卖机挡弹和 Bouncy Castle 减速可拖进场，开角跳脸仍危险"
    anti_tank: "medium_high_in_choke_if_bounce_lane_is_maintained"
    wall_break: "none; 偏好保留关键墙体"
    throw_or_wall_bypass: "high_via_bounce_angles_but_not_true_throw"
    area_control: "high_on_enclosed_lanes_conditional_in_semi_open_space_with_gadget_anchor"
    scouting_or_vision: "low"
    team_support: "lane_denial_temporary_projectile_cover_and_Bouncy_slow"
    wall_dependency: "medium_high; 贩卖机能短时制造反弹面，但不可代替耐久墙廊"
    spawnable_or_pet: "conditional; Multiball Launcher 贩卖机可挡非穿透弹道、承接反弹，被毁后环状放弹"
    crowd_control: "conditional_with_Bouncy_Castle_Buffie; 分裂小弹减速 2 秒"
    source_trace:
      - "[[sources/Fandom-Rico|Fandom-Rico]]"
      - "[[sources/PLP-Rico|PLP-Rico]]"
      - "[[sources/Fandom-Maintenance-July-8-2026|Fandom Maintenance July 8]]"

  build_switches:
    - build: "Multiball Launcher / Super Bouncy / Shield, Damage"
      source: "[[sources/Fandom-Rico|Fandom-Rico]] / [[sources/PLP-Rico|PLP-Rico]]"
      changes_capabilities:
        - "Multiball Launcher 部署可挡窄弹道的贩卖机，Rico 可向它反弹攻击；被毁时向四周发射穿透反弹子弹"
        - "Gadget Buffie 使命中贩卖机的反弹子弹累积更多爆裂弹，把掩体存活时间变成延迟释放资源"
        - "Super Bouncy 提高首次反弹后伤害，Buffie 还让反弹命中额外提供 Super 充能"
        - "Shield/Damage gears 保障低血对线容错"
      enables:
        - bounce_wall_lane_control
        - temporary_artificial_bounce_surface
        - projectile_cover_and_delayed_radial_clear
      mitigates_failure_modes:
        - open_field_no_durable_bounce_surface
        - low_health_dive_from_linear_projectiles
      poor_when:
        - "敌方可从墙后、穿透角或安全长线快速清掉贩卖机，不给 Rico 加载或爆裂转化"
        - "当队伍需要立即减速或远程分裂弹道时，贩卖机的延迟价值可能太慢"
      bp_use: "durable_wall_or_protected_temporary_anchor_build"
    - build: "Bouncy Castle / Robo Retreat control-or-escape variant"
      source: "[[sources/Fandom-Rico|Fandom-Rico]]"
      changes_capabilities:
        - "Bouncy Castle 不消耗弹药发射大子弹，碰墙或命中英雄后分成 3 枚小子弹"
        - "Gadget Buffie 让分裂小弹对英雄减速 2 秒，提供追击、脱离或路口集火窗口"
        - "Robo Retreat 在低血提供高移速，Buffie 让极低血逃生与走位更强"
      enables:
        - split_projectile_route_control
        - ranged_slow_confirm
        - low_health_kiting
      mitigates_failure_modes:
        - dive_escape_after_first_contact
        - mobile_target_leaves_bounce_lane
      poor_when:
        - "分裂角度无法覆盖目标路线，或敌方能一波秒杀而不给 Robo Retreat 操作窗口"
        - "这套构筑不提供自疗，不能按续航构筑评估"
      bp_use: "immediate_slow_and_low_health_mobility_switch"

  map_feature_hooks:
    - map_feature_type: "bounce_wall_corridor"
      uses_feature_by: "bullets bounce off walls, gain range, and can hit enemies behind cover"
      route_or_position: "side corridor, L-wall, or goal lane where Rico can shoot from cover"
      objective_conversion: "lane lock, ball control, gem side denial, or Knockout space control"
      active_when: "walls remain intact and enemy must pass through the bounce lane"
      fails_if: "enemy opens walls, plays fully open field, or outranges from non-bounce angle"
      example_maps:
        - Pinball Dreams
        - Hard Rock Mine
        - Layer Cake
        - Belle's Rock
        - Triple Dribble
      bp_use: required_capabilities.bounce_wall_control
    - map_feature_type: "vending_machine_temporary_bounce_anchor"
      uses_feature_by: "Multiball Launcher 在半开阔路线创造临时挡弹与反弹面，被清时再以环状子弹逼位"
      route_or_position: "宝石矿侧翼、球门防守口袋、长走廊中的少墙位或己方撤退线"
      objective_conversion: "在原本反弹不完整的位置暂时锁路、挡非穿透火力，并迫使敌方交清召唤物资源"
      active_when: "贩卖机能放在敌方难以隔墙/穿透秒清的位置，Rico 有时间向它反弹加载"
      fails_if: "对方不进相关路线，或用投掷、穿透、大范围火力在转化前安全清掉"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Triple Dribble
        - Center Stage
      bp_use: "map_factor_fit.temporary_artificial_bounce_anchor"
    - map_feature_type: "enclosed_anti_aggro_control"
      uses_feature_by: "反弹火力配合贩卖机挡路，或用 Bouncy Castle 分裂减速惩罚窄口进场"
      route_or_position: "short corridor, goal defense pocket, or side choke"
      objective_conversion: "deny scorer, slow assassin entry, or clear contested lane"
      active_when: "enemy engage path is narrow and Rico can preserve a bounce/control resource"
      fails_if: "dive enters from an open angle, disables Rico, or clears the vending machine without entering the lane"
      example_maps:
        - Pinball Dreams
        - Triple Dribble
        - Center Stage
      bp_use: candidate_eval.anti_aggro_in_closed_lane
    - map_feature_type: "safe_or_objective_bounce_angle"
      uses_feature_by: "bounce range and piercing Super create indirect damage routes"
      route_or_position: "safe-facing wall, zone edge, or gem mine side wall"
      objective_conversion: "Heist chip, zone denial, or forcing defenders off objective"
      active_when: "objective angle exists without Rico leaving cover"
      fails_if: "objective is fully open with no bounce value or enemy wallbreak removes angle"
      example_maps:
        - Hot Potato
        - Pit Stop
        - Gem Fort
      bp_use: map_factor_fit.objective_angle

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - side_lane_wall_control
        - gem_mine_angle_denial
        - punish_grouped_mid_from_bounce
        - temporary_vending_cover_for_retreat_or_mine_entry
      cannot_fulfill:
        - safe_gem_carrier
        - bush_vision_tax
      needs_teammate_support:
        - mid_carrier_or_sustain
        - anti_throw_or_pierce_if_vending_anchor_is_core
      false_positive: "贩卖机只是有冷却的临时掩体；Rico 锁住一路也不能代替 carrier 的撤退计划"
    - mode: "Brawl Ball"
      can_fulfill:
        - lane_denial_from_goal_walls
        - anti_scorer_corridor_slow_or_vending_block
        - clear_defenders_from_covered_angles
      cannot_fulfill:
        - primary_ball_carrier
        - reliable_wallbreak_score_window
      needs_teammate_support:
        - scorer_or_hard_displacement
        - grass_control
      false_positive: "Bouncy Castle 减速和贩卖机挡路不是硬击退；队友无差别开墙还会抹掉 Rico 的主要角度"
    - mode: "Heist"
      can_fulfill:
        - conditional_safe_damage_from_bounce_angle
        - lane_duel_pressure
        - punish_enemy_entry_route
      cannot_fulfill:
        - open_map_pure_safe_race_without_angle
        - base_body_defense
      needs_teammate_support:
        - wall_state_protection
        - true_safe_dps_if_bounce_angle_absent
      false_positive: "Heist label is weak if Rico cannot reach safe from a bounce route"
    - mode: "Knockout"
      can_fulfill:
        - wall_angle_space_control
        - final_ring_corridor_denial
        - punish_enemies_behind_cover
      cannot_fulfill:
        - open_field_marksman_duel_without_walls
        - hard_thrower_answer
      needs_teammate_support:
        - wallbreak_answer_to_enemy_throwers
        - peel_or_scouting
      false_positive: "Closed-map value flips if enemy has easy wallbreak or deeper thrower pocket"

  failure_modes:
    - id: "open_field_no_bounce_value"
      active_when: "map or wallbreak removes bounce angles and Rico must fight as a normal low-health shooter"
      exposed_by: "[[sources/Fandom-Rico|Fandom-Rico]] bounce-based attack and tips"
      mitigation: "优先选耐久墙廊；半开阔图只能把受保护的贩卖机当短窗口，不得当永久墙体"
      bp_use: "map_factor_false_positive_check"
    - id: "wallbreak_erases_plan"
      active_when: "enemy or teammate opens the specific walls Rico needs for lane control"
      exposed_by: "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]] terrain state plan"
      mitigation: "protect walls, ban/answer wallbreak, or choose non-wall-dependent DPS"
      bp_use: "terrain_state_plan_check"
    - id: "thrower_or_deeper_pocket_outcontrols"
      active_when: "enemy thrower controls Rico's bounce position from a safer wall pocket"
      exposed_by: "[[sources/PLP-Rico|PLP-Rico]] counteredBy thrower/control picks"
      mitigation: "pair wallbreak or dive, avoid picking Rico into uncontested thrower pockets"
      bp_use: "must_avoid_or_needs_support"
    - id: "vending_machine_cleared_before_conversion"
      active_when: "敌方能用投掷、穿透或大范围火力从安全角度清掉贩卖机，或 Rico 无法向它反弹加载"
      exposed_by: "[[sources/Fandom-Rico|Fandom-Rico]] current Multiball Launcher mechanics"
      mitigation: "放到敌方必须转线才能清的位置，或在清点资源交掉后再部署"
      bp_use: "spawnable_survival_and_conversion_gate"
    - id: "low_health_dive_in_open_angle"
      active_when: "assassin reaches Rico outside a corridor before vending cover, Bouncy slow, or bounce pressure converts"
      exposed_by: "[[sources/Fandom-Rico|Fandom-Rico]] low health and current vending/Bouncy/Robo Retreat tools"
      mitigation: "play near walls, hold the relevant Gadget, pair peel, or use Robo Retreat as an escape threshold"
      bp_use: "false_positive_filter"

  conditional_matchups:
    - target:
        - "Mortis"
        - "Shelly"
        - "Nita"
        - "Jessie"
        - "Mico"
        - "Spike"
      direction: "subject_favored"
      source: "[[sources/PLP-Rico|PLP-Rico]]"
      mechanism: "closed-lane bounce pressure, vending-machine cover and Bouncy Castle slow punish targets that must enter Rico's wall geometry"
      active_when: "walls create a narrow approach and Rico can preserve a bounce/control resource"
      fails_when: "target approaches from open angle, has hard CC, safely clears the vending machine, or walls are removed"
      bp_use: "response_pick_candidate_on_closed_maps"
    - target:
        - "Sprout"
        - "Tara"
        - "Barley"
        - "Carl"
        - "Stu"
      direction: "target_favored"
      source: "[[sources/PLP-Rico|PLP-Rico]]"
      mechanism: "thrower control, pull/CC, wallbreak, or high mobility can deny Rico's chosen bounce lane"
      active_when: "enemy has deeper wall pocket, reliable wallbreak, or multiple approach angles"
      fails_when: "Rico's team opens enemy pocket while preserving Rico's own bounce walls"
      bp_use: "must_answer_before_locking_rico"
    - target:
        - "Cordelius"
      direction: "target_favored"
      source: "[[sources/PLP-Rico|PLP-Rico]] / [[sources/Fandom-Maintenance-July-8-2026|Fandom Maintenance July 8]]"
      mechanism: "Shadow Realm 隔绝队友保护，且当前规则不允许 Rico 在领域内使用 Bouncy Castle，使他丢失分裂减速脱离手段"
      active_when: "Cordelius 能进入 Super 距离，并将 Rico 从贩卖机/墙廊和队友 peel 中隔离"
      fails_when: "Rico 保持超出 Cordelius 的进场距离，或 Cordelius 在低血、缺 Super 时强行接触"
      bp_use: "must_track_shadow_realm_gadget_denial"
    - target:
        - "Penny"
        - "Jessie"
        - "Nita"
      direction: "subject_favored"
      source: "[[sources/PLP-Rico|PLP-Rico]]"
      mechanism: "pierce/bounce lanes can hit grouped summons and owners from indirect angles"
      active_when: "summons are placed near walls or lane choke"
      fails_when: "summon anchors are protected by thrower pocket or force Rico into open field"
      bp_use: "summon_pressure_response_candidate"

  slot_notes:
    slot_1: "只在耐久反弹路线很明确，或贩卖机有受保护的目标锚点时先手；仍要预留对投掷、穿透清点和选择性开墙的回答。"
    slot_2_3: "可围绕耐久墙廊建立反弹核心，或用贩卖机补一个临时掩体/反弹面；需要队友保留关键墙体。"
    slot_4_5: "用于补 Brawl Ball/Gem/Knockout 的封路、临时掩体或分裂减速；先检查敌方是否已有穿透/投掷清贩卖机资源。"
    slot_6: "当敌方缺开墙、缺安全清贩卖机手段，且必须经过墙边或窄口时，Rico 是高收益惩罚位。"
```
