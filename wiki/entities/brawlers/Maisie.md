# Maisie

## 基本信息

- 稀有度：Epic
- 定位：Marksman
- 类型：长射程反突进 / Shockwave 推离 / Tremors 减速

## 来源摘要

- Fandom：[[sources/Fandom-Maisie|Fandom 来源摘要: Maisie]]
- PLP：[[sources/PLP-Maisie|PLP 来源摘要: Maisie]]
- PLP 推荐模式：Brawl Ball, Hot Zone

## 角色定位总结

Maisie 是长线 Marksman，但 BP 用法更像反突进控制：8.67 格主攻伤害高，弹体起速慢、越飞越快；Super `Shockwave` 有 0.5 秒前摇，之后 360 度推开周围敌人 3 格并伤害，`Tremors` 让命中的敌人 slow 2 秒。她在 Brawl Ball 和 Hot Zone 的价值来自防守球门、清区、打断短手推进和把敌人推离目标点；风险是主攻远距离容易被横移躲，Super 前摇会被 stun/pull/knockback 取消，`Disengage!` 也不能穿墙/水。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "long; 主攻 8.67 格，Super 半径 5 格"
    projectile_reliability: "medium; 主攻初速慢后段快，靠预判/slow/stun 提高命中"
    burst: "high_if_hit_chain; 单发 1500，Finish Them 可按目标缺失生命加伤，Hyper 近身爆发高"
    sustained_dps: "medium; 1.5 秒装填，弹药有限且需要命中"
    objective_damage: "medium_high_on_stationary_targets; Fandom 支持 Heist fixed safe burst，但 PLP 主推 Ball/Zone"
    mobility: "medium_with_disengage; Gadget dash 2.67 格并可 0.5 秒 stun 近敌，不能过墙/水"
    survivability: "medium; 4000 HP，依赖推离/slow/Disengage"
    engage: "medium; Super+Disengage 可主动贴近打 surprise shockwave"
    disengage: "high; Shockwave 推离、Tremors slow、Disengage dash"
    anti_aggro: "very_high; 反刺客/坦克进场是核心消费场景"
    anti_tank: "high_if_finish_them_or_super_cycle; 推离+slow+缺血加伤可惩罚坦克"
    wall_break: "none"
    throw_or_wall_bypass: "low; Shockwave 穿墙推人但不越墙输出，本体/Disengage 不穿墙水"
    area_control: "medium_high; Super AoE、Tremors slow 和 Hyper radial shots 清点"
    scouting_or_vision: "medium; 长线扫草但无专属 reveal"
    team_support: "medium; 推离/slow 给队友目标窗口"
    spawnable_or_pet: "none"
    crowd_control: "high; pushback, slow, 0.5s stun on Disengage"
    source_trace:
      - "[[sources/Fandom-Maisie|Fandom-Maisie]]"
      - "[[sources/PLP-Maisie|PLP-Maisie]]"

  build_switches:
    - build: "Disengage / Tremors / Shield, Damage"
      source: "[[sources/PLP-Maisie|PLP-Maisie]]"
      changes_capabilities:
        - "Disengage 2.67 格 dash，近敌 2.33 格内 stun 0.5 秒，可逃生或连 Super"
        - "Tremors 让 Shockwave 命中者 slow 2 秒，增强 Brawl Ball/Hot Zone 目标控制"
        - "Shield/Damage 提高反突进时的存活和击杀确认"
      enables:
        - "Brawl Ball 持球/守门推离"
        - "Hot Zone 清点"
        - "反突进后撤"
      mitigates_failure_modes:
        - "slow_projectile_misses"
        - "assassin_gets_inside"
      best_when: "敌方需要从草口/球门/热区入口近身，且缺前摇打断"
      poor_when: "敌方长手/投掷能在 Super 范围外压制，或多控制取消 Maisie 前摇"
      bp_use: "default_plp_anti_aggro_control_build"
    - build: "Finish Them / Pinpoint Precision variant"
      source: "[[sources/Fandom-Maisie|Fandom-Maisie]]"
      changes_capabilities:
        - "Finish Them 即刻回 1 ammo，并按目标缺失生命提高下一发伤害，不能作用于 Heist safe"
        - "Pinpoint Precision 满射程命中 +25% 伤害/充能"
      enables:
        - "反坦 finish"
        - "长线 poke 伤害"
        - "Heist 防守击杀而非 safe gadget burst"
      mitigates_failure_modes:
        - "high_hp_target_survives_shockwave"
      best_when: "需要打坦克/高血量目标且能命中长线"
      poor_when: "敌方多突进，需要 Disengage 的保命"
      bp_use: "anti_tank_or_long_range_variant"

  map_feature_hooks:
    - id: "brawl_ball_shockwave_goal_peel"
      map_feature_type: "goal_peel_and_ball_disarm"
      uses_feature_by: "Shockwave 推离持球者/守门人，Tremors slow 后续跟伤，Disengage 可补 stun"
      route_or_position: "球门前三格、中路球权、侧草推进和 overtime 直线"
      objective_conversion: "打断持球、清守门人、或把敌方推出射门线"
      active_when: "敌方必须靠近球门或聚集防守"
      fails_if: "Super 前摇被取消，或队伍没有 scorer/破墙跟进"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.goal_peel_and_ball_disarm"
    - id: "hot_zone_tremors_zone_clear"
      map_feature_type: "zone_body_push_and_slow"
      uses_feature_by: "Super 把站区 body 推出区，Tremors slow 2 秒阻止立刻回区"
      route_or_position: "单区中心、区边墙、敌方回区 chokepoint"
      objective_conversion: "把一次 Super 转成 zone score swing 和队友击杀窗口"
      active_when: "敌方必须站区或从固定入口进区，Maisie 有 Super"
      fails_if: "敌方 thrower/long range 从区外清 Maisie，或控制取消前摇"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "map_bp_factors.zone_body_displacement"
    - id: "gem_mine_long_damage_and_shockwave_peel"
      map_feature_type: "gem_mid_long_lane_anti_aggro"
      uses_feature_by: "长线高伤压矿区，Shockwave 推开刺客/坦克并保护 carrier"
      route_or_position: "宝石矿入口、carrier 撤退线、侧草突进路径"
      objective_conversion: "守住矿区射线，或在倒计时追击时推离敌方 body"
      active_when: "地图有足够长线给主攻加速，敌方从可预判草口进"
      fails_if: "敌方长手 outrange 或投掷墙袋压制 Maisie"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.gem_mid_anti_aggro_marksman"
    - id: "heist_safe_fixed_target_and_defense"
      map_feature_type: "stationary_target_damage_with_defensive_push"
      uses_feature_by: "safe 固定易吃主攻，Super 可防守推开入库者并 slow"
      route_or_position: "safe lane、safe 前墙、敌方入库线"
      objective_conversion: "把三发+Super 转成 safe burst，或防守入库短手"
      active_when: "Maisie 有安全直线输出且队伍能保护她不被突脸"
      fails_if: "敌方从墙后/多路进库，或需要更稳定远程 race"
      example_maps:
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
      bp_use: "candidate_eval.heist_auxiliary_damage_and_peel"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "守门推离和持球掉节奏"
        - "Tremors slow 后续射门/击杀"
      cannot_fulfill:
        - "稳定破门"
        - "Super 前摇被控制时硬守"
      needs_teammate_support:
        - "scorer、破墙、反投掷"
      false_positive: "Shockwave 推人不等于进球；队伍必须能接后续球权"
    - mode: "Hot Zone"
      can_fulfill:
        - "清点、推离 body、slow 回区"
      cannot_fulfill:
        - "长期主站区"
        - "处理所有区外长手"
      needs_teammate_support:
        - "站区 body、墙后处理、治疗"
      false_positive: "Maisie 清区强，但清完需要队友站住"
    - mode: "Gem Grab/Heist"
      can_fulfill:
        - "carrier peel"
        - "fixed safe damage variant"
      cannot_fulfill:
        - "安全主 carrier"
        - "无保护 solo race"
      needs_teammate_support:
        - "carrier、视野、反突进"
      false_positive: "Heist 是 Fandom 机制支持的变体，不是 PLP 默认模式"

  failure_modes:
    - id: "slow_start_projectile_dodged"
      active_when: "远距离对手横移或有 dash，Maisie 单发预判失败"
      exposed_by: "[[sources/Fandom-Maisie|Fandom-Maisie]] projectile starts slow then speeds up"
      mitigation: "用 Tremors/Disengage/队友 slow 后射击，或在 choke/近中距离打"
      bp_use: "projectile_reliability_filter"
    - id: "super_delay_cancelled"
      active_when: "Shockwave 0.5 秒前摇中被 stun/pull/knockback"
      exposed_by: "Fandom Super cancellation rules"
      mitigation: "等控制交掉、从草墙逼近，或用 Disengage 调角"
      bp_use: "cc_hard_gate"
    - id: "disengage_not_terrain_bypass"
      active_when: "把 Disengage 当作过墙/过水逃生"
      exposed_by: "Fandom notes Disengage cannot dash through walls or water"
      mitigation: "只按直线路径建模，预留墙前位置"
      bp_use: "map_route_false_positive_filter"
    - id: "long_range_pressure_outside_super"
      active_when: "敌方 Piper/Nani/Bea/8-Bit 等在 Super 范围外压制"
      exposed_by: "PLP target_favored range/body signals and Fandom long-range struggle note"
      mitigation: "补开墙/长手队友，不在纯开阔长线单独早手"
      bp_use: "draft_needs_lane_support"

  conditional_matchups:
    - target: ["Darryl", "Lily", "El Primo", "Chuck"]
      direction: "subject_favored"
      source: "[[sources/PLP-Maisie|PLP-Maisie]]"
      mechanism: "Shockwave 推离、Tremors slow 和 Disengage stun 能打断滚入/突进/短手接触"
      active_when: "他们必须从可预判路线进球门、热区或矿区"
      fails_when: "Maisie Super 前摇被打断，或目标从侧草贴脸先手"
      bp_use: "anti_aggro_response"
    - target: ["Jae-Yong", "Gigi", "Piper", "Nani"]
      direction: "subject_favored"
      source: "[[sources/PLP-Maisie|PLP-Maisie]]"
      mechanism: "高单发长线和反突进工具可惩罚低血支援/长手在目标路线上站位"
      active_when: "Maisie 有射线且队友能帮她进入有效距离"
      fails_when: "他们维持最大距离、墙后角度，或用队友控制取消 Super"
      bp_use: "long_lane_or_peel_response"
    - target: ["Sandy", "Rosa", "Nita", "Bibi"]
      direction: "target_favored"
      source: "[[sources/PLP-Maisie|PLP-Maisie]]"
      mechanism: "隐蔽、草丛 body、召唤物或速度短手能躲/吃掉 Maisie 的慢起弹道和前摇"
      active_when: "地图有草墙接近，Maisie 缺视野和队友 peel"
      fails_when: "草被清、Maisie 有 Super+Tremors，或队友先压低 body"
      bp_use: "requires_vision_and_anti_body_support"
    - target: ["Larry & Lawrie", "Damian", "Sirius", "8-Bit"]
      direction: "target_favored"
      source: "[[sources/PLP-Maisie|PLP-Maisie]]"
      mechanism: "墙后/召唤控制、特殊路线或高持续火力可在 Maisie 反开范围外压制她"
      active_when: "他们站墙袋、远线或召唤物后，Maisie 无开墙/突进队友"
      fails_when: "地图线打开，或 Maisie 只负责反突进而不和他们对线"
      bp_use: "must_answer_wall_or_sustain_lane"

  slot_notes:
    slot_1: "Brawl Ball/Hot Zone 可早手，但要防后手长手/投掷"
    slot_2_3: "作为反突进和目标点清场核心，后续补站区/scorer"
    slot_4_5: "看到敌方短手推进或球路 dash 后价值高"
    slot_6: "最后手可封死单一突进计划；遇多长手墙袋不要硬选"
```

## 关联页面

- [[sources/Fandom-Maisie|Fandom 来源摘要: Maisie]]
- [[sources/PLP-Maisie|PLP 来源摘要: Maisie]]
