# Ollie

## 基本信息

- 稀有度：Mythic
- 定位：Tank
- 类型：Hypnotize 控制坦克 / 闭图跳入 / 低伤害功能前排

## 来源摘要

- Fandom：[[sources/Fandom-Ollie|Fandom 来源摘要: Ollie]]
- PLP：[[sources/PLP-Ollie|PLP 来源摘要: Ollie]]
- PLP 推荐模式：Bounty, Knockout

## 角色定位总结

Ollie 是高血量功能坦克，强点不是伤害，而是 `Hypnotize`：Super dash 后 1.5 秒蓄音爆，半径内敌人被 hypnotized 2.5 秒，会朝 Ollie 移动且不能攻击、用 Super 或 Hypercharge。默认 PLP build `Regulate / Renegade` 强调闭图：Regulate 可跳 3.67 格越墙/水并落地 1 秒 hypnotize，Renegade 在 Super dash 后给 3000 衰减盾。风险是 Super 本体不能穿墙/水，dash 期间被 stun/pull/knockback 会取消，且 Ollie 伤害低、Super 会消耗最多 50% ammo；如果队友不能跟伤，他只是把敌人拉近自己。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "mid_control; 普攻 6.33 格窄 cone，Super dash 5.67 格并半径控制"
    projectile_reliability: "medium; 普攻窄 cone 可穿透，伤害低"
    burst: "low; 控制强但单体伤害不足"
    sustained_dps: "low_to_medium; 1.8 秒 reload，Super 后还会消耗 ammo"
    objective_damage: "low"
    mobility: "high_with_resources; Fast 基础，Regulate 可越墙/水跳，Super dash 加速但不穿墙水"
    survivability: "high_with_renegade; 5400 HP，Renegade 3000 衰减盾，Regulate 空中免疫非 DoT/status"
    engage: "high_if_control_not_interrupted; Super/Regulate/All Eyez on Me 均可 hypnotize"
    disengage: "medium; Regulate 可跳走，Super 更偏进场"
    anti_aggro: "medium_high; hypnotize 阻止敌人攻击/技能，但需要命中和队友跟进"
    anti_tank: "conditional; 控制坦克移动/攻击，但低伤害需要队友"
    wall_break: "none"
    throw_or_wall_bypass: "medium_gadget_only; Regulate 可越墙/水，Super dash 不能"
    area_control: "medium; Super 3.33 半径，Hyper 半径 +50%"
    scouting_or_vision: "low"
    team_support: "high_control_low_damage; hypnotize 给队友击杀/进球窗口"
    spawnable_or_pet: "none"
    crowd_control: "very_high; hypnotize 1-2.5 秒使目标朝 Ollie 移动并禁止攻击/Super/Hyper"
    source_trace:
      - "[[sources/Fandom-Ollie|Fandom-Ollie]]"
      - "[[sources/PLP-Ollie|PLP-Ollie]]"

  build_switches:
    - build: "Regulate / Renegade / Shield, Damage, Health"
      source: "[[sources/PLP-Ollie|PLP-Ollie]]"
      changes_capabilities:
        - "Regulate 向前跳 3.67 格，可越墙/水，空中免疫大部分伤害，落地半径 1.67 hypnotize 1 秒"
        - "Renegade 在 Super dash 后给 3000 衰减盾，提高近身放音爆容错"
        - "Health/Shield gear 支持闭图 Bounty/Knockout 的反复控点"
      enables:
        - "闭图墙后开团"
        - "Knockout 首杀控制"
        - "Bounty 低风险拉人窗口"
      mitigates_failure_modes:
        - "super_dash_blocked_by_wall"
        - "ollie_bursted_during_delay"
      best_when: "地图墙体让 Regulate 能创造角度，队友有足够伤害跟 hypnotize"
      poor_when: "敌方控制能取消 dash，或队伍缺 follow-up damage"
      bp_use: "default_plp_closed_map_control_tank_build"
    - build: "All Eyez on Me / Kick, Push variant"
      source: "[[sources/Fandom-Ollie|Fandom-Ollie]]"
      changes_capabilities:
        - "All Eyez on Me 让下一次普攻命中也 hypnotize 1 秒，适合 Brawl Ball 射门后阻挡防守"
        - "Kick, Push 贴墙移动 +20% 速度，适合墙多闭图持续压迫"
      enables:
        - "Brawl Ball 射门保护"
        - "墙边持续游走"
      mitigates_failure_modes:
        - "super_not_available_for_control"
        - "needs_wall_route_tempo"
      best_when: "目标模式更需要普攻控制或墙边速度"
      poor_when: "需要 Regulate 越墙开团和躲关键技能"
      bp_use: "ball_or_wall_speed_variant"

  map_feature_hooks:
    - id: "knockout_closed_map_regulate_pick"
      map_feature_type: "closed_map_wall_jump_control"
      uses_feature_by: "Regulate 越墙/水跳入并落地 1 秒 hypnotize，Super/Renegade 接第二段控制"
      route_or_position: "Knockout 墙后口袋、Belle's Rock 侧墙、New Horizons 中央墙角"
      objective_conversion: "开首杀、逼敌方交位移，或在缩圈时把目标拉出掩体"
      active_when: "墙体让常规路径难接近，队友能在 hypnotize 时补伤害"
      fails_if: "落点被 Colette/Shelly/Rosa 等守住，或控制取消 Ollie dash"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
        - "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"
      bp_use: "slot_task.closed_map_control_engage"
    - id: "bounty_bodyguard_and_star_lead_control"
      map_feature_type: "bounty_bodyguard_control"
      uses_feature_by: "Ollie 高血量和 hypnotize 阻止敌方长手/刺客在星差局输出"
      route_or_position: "星差后撤线、队友长手前方、草墙侧翼接触点"
      objective_conversion: "保护低血队友、打断敌方收割，或用控制换首杀"
      active_when: "队友能输出被 hypnotize 的目标，Ollie 不需要自己完成击杀"
      fails_if: "敌方 Colette/Poco/Sandy 等削弱 Ollie body，或远程无视他打后排"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
      bp_use: "candidate_eval.bounty_control_bodyguard"
    - id: "brawl_ball_hypnotize_walk_in_or_block"
      map_feature_type: "ball_goal_control_window"
      uses_feature_by: "Super 让门前敌人朝 Ollie 移动并不能攻击，All Eyez 可射门后阻挡防守者"
      route_or_position: "球门前三格、中路持球推进、守门人站位"
      objective_conversion: "带球走入、阻止封堵射门，或让队友跟进射门"
      active_when: "Ollie 有 Super/All Eyez，队友能处理球门几何"
      fails_if: "Super dash 被取消、Ollie 低伤害无法清守门，或 goal still closed"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_control_tank_window"
    - id: "gem_control_tank_pull_off_carrier"
      map_feature_type: "carrier_peel_hypnotize"
      uses_feature_by: "Hypnotize 让追击者朝 Ollie 移动并不能攻击，Regulate 可越墙接近追击线"
      route_or_position: "carrier 倒计时撤退线、矿区侧草、己方半场入口"
      objective_conversion: "把追击者从 carrier 身边拉走，或让队友集火被控目标"
      active_when: "己方已有 carrier，Ollie 只负责 peel/控制"
      fails_if: "敌方用远程/投掷绕过 Ollie，或 Colette 百分比伤害打穿 shield"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.carrier_peel_control_tank"

  objective_contracts:
    - mode: "Bounty/Knockout"
      can_fulfill:
        - "闭图开团和首杀控制"
        - "星差 bodyguard"
        - "Regulate 越墙接触"
      cannot_fulfill:
        - "独立长线击杀"
        - "无 follow-up 时 solo carry"
      needs_teammate_support:
        - "爆发/长手跟伤、反百分比、清控制"
      false_positive: "Ollie 控住人不等于击杀；低伤害要求队友立即跟进"
    - mode: "Brawl Ball/Gem Grab"
      can_fulfill:
        - "带球/守门控制窗口"
        - "carrier peel"
      cannot_fulfill:
        - "稳定破门"
        - "安全主 carrier"
      needs_teammate_support:
        - "射门/破墙、carrier、补伤害"
      false_positive: "Super 会消耗 ammo，且本体伤害低，不能把 Ollie 当主要输出"

  failure_modes:
    - id: "super_cancelled_during_dash"
      active_when: "Ollie Super dash 中被 stun/pull/knockback"
      exposed_by: "[[sources/Fandom-Ollie|Fandom-Ollie]] Super cancellation rules"
      mitigation: "先 bait 控制，用 Regulate 绕角，或等队友压住控制位"
      bp_use: "engage_hard_gate"
    - id: "super_dash_not_wall_bypass"
      active_when: "BP 把 Ollie Super 当作越墙/过水路线"
      exposed_by: "Fandom notes Super cannot dash through walls or water"
      mitigation: "只有 Regulate 可越墙/水，Super 路线必须是可行地面"
      bp_use: "map_route_false_positive_filter"
    - id: "low_damage_without_followup"
      active_when: "Ollie hypnotize 多人但队友没有火力接"
      exposed_by: "Fandom low damage note and PLP support mode fit"
      mitigation: "只在队友能立即打控制目标时开团；否则作为 bodyguard/peel"
      bp_use: "team_damage_requirement"
    - id: "renegade_shield_countered_by_percent_or_sustain"
      active_when: "Colette 或高 sustain 阵容把 Ollie shield/HP 交换转成劣势"
      exposed_by: "Fandom notes Colette damage based on max health while shield active and PLP counters"
      mitigation: "避开百分比/高 sustain 反坦，或只作短时控制不正面换血"
      bp_use: "anti_tank_counter_filter"

  conditional_matchups:
    - target: ["Alli", "Mico", "Shade"]
      direction: "subject_favored"
      source: "[[sources/PLP-Ollie|PLP-Ollie]]"
      mechanism: "高血量、Regulate 空中免疫和 Hypnotize 能打断机动刺客的落点/接触节奏"
      active_when: "Ollie 预判落点或闭图路线，队友能在 hypnotize 期间补伤害"
      fails_when: "刺客绕开 Ollie 直取后排，或控制/爆发在 Ollie dash 前落下"
      bp_use: "control_tank_response_to_mobile_entry"
    - target: ["Lola", "Chuck", "Frank", "El Primo", "Bea"]
      direction: "subject_favored"
      source: "[[sources/PLP-Ollie|PLP-Ollie]]"
      mechanism: "Regulate/Hypnotize 能接触静态输出、路线英雄或慢前摇坦克，并让其短时无法攻击/用 Super"
      active_when: "地图闭、墙角能跳入，且队友能打被控目标"
      fails_when: "Lola/Ego 或 Bea 保持开阔最大距离，或坦克队友反控 Ollie"
      bp_use: "closed_map_control_pick"
    - target: ["Poco", "Meeple", "Najia", "Sandy", "Rosa"]
      direction: "target_favored"
      source: "[[sources/PLP-Ollie|PLP-Ollie]]"
      mechanism: "治疗/团队工具/隐蔽/高血 body 会把 Ollie 的低伤控制拖成无法转击杀的换血"
      active_when: "Ollie 队伍缺 burst，或敌方可用 sustain 复位控制窗口"
      fails_when: "Ollie 只负责 peel carrier/scorer，队友有足够 damage follow-up"
      bp_use: "requires_burst_followup"
    - target: ["Colette", "Fang", "Edgar"]
      direction: "target_favored"
      source: "[[sources/PLP-Ollie|PLP-Ollie]]"
      mechanism: "百分比伤害或高速刺客能惩罚 Ollie 高血低伤和 Super 延迟"
      active_when: "他们能逼 Ollie 正面换血或在 dash 前后接触后排"
      fails_when: "Ollie 预留 Regulate/hypnotize 只打一轮控制，队友先压低目标"
      bp_use: "avoid_as_primary_body_answer"

  slot_notes:
    slot_1: "不宜无 follow-up 早手；低伤害和取消风险会被针对"
    slot_2_3: "闭图 Bounty/Knockout 可作为控制 body 建队，后续补 burst"
    slot_4_5: "看到敌方机动/长手缺反控时可响应"
    slot_6: "最后手适合封闭图开首杀；遇 Colette/Poco/Sandy/Rosa 等应谨慎"
```

## 关联页面

- [[sources/Fandom-Ollie|Fandom 来源摘要: Ollie]]
- [[sources/PLP-Ollie|PLP 来源摘要: Ollie]]
