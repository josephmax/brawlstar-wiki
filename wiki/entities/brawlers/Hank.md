# Hank

## 基本信息

- 稀有度：Epic
- 定位：Tank
- 类型：蓄力范围爆发 / 墙后压迫 / 近身鱼雷反打坦克

## 来源摘要

- Fandom：[[sources/Fandom-Hank|Fandom 来源摘要: Hank]]
- PLP：[[sources/PLP-Hank|PLP 来源摘要: Hank]]
- PLP 推荐模式：Brawl Ball, Hot Zone, Gem Grab

## 角色定位总结

Hank 是靠蓄力水泡制造路线恐惧的坦克。满蓄 3 秒后水泡可以形成 5.33 格宽的穿透爆发，并且能像 Jacky/Doug 一样打到墙后目标；`Barricade` 与 `It's Gonna Blow` 让他能把蓄力窗口转换成推进窗口。他的 BP 风险同样高：蓄力时在草里可见、不能自然回血，被击退/拉扯/眩晕会取消攻击；Super 虽有 50% 已损生命治疗和近身多鱼雷爆发，但离目标不够近时收益很低。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "short_to_wall_piercing_mid; 水泡 1-5.33 格宽，打点范围 1.67-3.33 格并可越薄墙爆炸"
    projectile_reliability: "timing_dependent; 满蓄需 3 秒，释放方向可临时旋转，但被控制会取消"
    burst: "very_high_if_full_bubble_or_point_blank_super; 满蓄 2100，近身 Super 多鱼雷叠中"
    sustained_dps: "medium_by_autoaim_spam; 0.25 秒 reload 很快，但高爆发依赖蓄力"
    objective_damage: "medium; 能威胁近身目标和守门/守区，不是远程 race"
    mobility: "medium_with_its_gonna_blow; 满蓄 80% 后 +10% 速度"
    survivability: "high_body_with_resource; 5200 HP，Barricade 3 秒 40% 减伤，Super 治疗 50% 已损生命"
    engage: "medium; 靠墙体、满蓄移速和 Barricade 走入范围"
    disengage: "low_to_medium; 主要靠 Barricade 和 Super 治疗，缺直接位移"
    anti_aggro: "high_at_point_blank; 近身 Super 和满蓄爆发能惩罚刺客/坦克"
    anti_tank: "high_if_centered_super; 贴中心可多鱼雷命中并回血"
    wall_break: "none"
    throw_or_wall_bypass: "high_damage_through_walls; 水泡爆炸可伤害墙后敌人，Hyper Super 鱼雷可绕向墙后目标"
    area_control: "high_zone_threat; 满蓄水泡让敌方不敢进窄口或墙边"
    scouting_or_vision: "low; 蓄力反而让 Hank 在草里暴露"
    team_support: "bodyguard; 用身体和威胁区护送球/热区/矿区"
    spawnable_or_pet: "none"
    crowd_control: "medium_with_gadget; Water Balloons 可让下一次水泡 slow 3 秒，默认 build 更偏减伤推进"
    source_trace:
      - "[[sources/Fandom-Hank|Fandom-Hank]]"
      - "[[sources/PLP-Hank|PLP-Hank]]"

  build_switches:
    - build: "Barricade / It's Gonna Blow / Shield, Damage"
      source: "[[sources/PLP-Hank|PLP-Hank]]"
      changes_capabilities:
        - "Barricade 提供 3 秒 40% 减伤，用于持球走入、顶区或贴脸释放 Super"
        - "It's Gonna Blow 在水泡超过 80% 蓄力时给 Hank +10% 移速，弥补短手接近"
        - "Shield + Damage gear 保留进场容错并提高低血线爆发"
      enables:
        - "Brawl Ball 持球/护球推进"
        - "Hot Zone 墙边 body presence"
        - "Gem Grab 侧路 bodyguard"
      mitigates_failure_modes:
        - "charged_attack_exposes_hank"
        - "approach_before_bubble_reaches_range"
      best_when: "地图有墙体/窄口，Hank 能安全蓄力后从侧面走入"
      poor_when: "敌方有稳定击退、拉扯、眩晕、百分比伤害或长手放风筝"
      bp_use: "default_plp_bubble_tank_build"
    - build: "Water Balloons / Take Cover / Health variant"
      source: "[[sources/Fandom-Hank|Fandom-Hank]]"
      changes_capabilities:
        - "Water Balloons 让下一次水泡命中后 slow 3 秒，适合限制绕墙逃跑目标"
        - "Take Cover 靠墙获得 20% 减伤，Health gear 缩短无法自然回复造成的空窗"
      enables:
        - "墙边持久顶区"
        - "slow 后收割"
      mitigates_failure_modes:
        - "enemy_walks_out_of_bubble"
        - "natural_regeneration_delay"
      best_when: "地图墙体密集、Hank 可以长期贴墙压迫"
      poor_when: "需要 Barricade 走入高 DPS 火力，或没有足够墙体触发减伤"
      bp_use: "wall_anchor_or_slow_variant"

  map_feature_hooks:
    - id: "brawl_ball_barricade_walk_in"
      map_feature_type: "ball_body_walk_and_goal_pressure"
      uses_feature_by: "Barricade 减伤配合满蓄水泡威胁门前防守，Super 可贴脸回血/反坦"
      route_or_position: "中路持球、门前短墙、侧路草墙推进线"
      objective_conversion: "把身体推进转成射门压力、逼防守后退或为队友清门"
      active_when: "球路有墙体掩护，敌方缺低成本击退/眩晕取消蓄力"
      fails_if: "Bibi/Gale/Tara/Frank 等控制守门，或 Hank 蓄力被打断后无法二次进场"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.ball_walk_in_tank"
    - id: "hot_zone_wall_bubble_anchor"
      map_feature_type: "wall_adjacent_zone_body"
      uses_feature_by: "Hank 在墙边蓄力，水泡威胁区口与墙后目标，Take Cover/Barricade 提供抗压"
      route_or_position: "热区边墙、区口拐角、敌方回区必经窄线"
      objective_conversion: "逼敌方离开区口，给队友踩区和回血窗口"
      active_when: "热区附近有可蓄力的墙角，敌方必须靠近或穿过窄口"
      fails_if: "敌方远程/thrower 无需进泡区即可清区，或控制链反复取消水泡"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "map_bp_factors.wall_anchor_zone_pressure"
    - id: "gem_side_wall_pierce_bodyguard"
      map_feature_type: "side_lane_wall_pierce_guard"
      uses_feature_by: "满蓄水泡能越墙打侧路敌人，Hank 身体保护 carrier 撤退线"
      route_or_position: "矿区侧墙、宝石撤退口、敌方侧路绕后拐角"
      objective_conversion: "让敌方侧路无法轻松压 carrier，或逼出控制技能后再推进"
      active_when: "己方已有 carrier，Hank 负责侧翼占位和反突进"
      fails_if: "Hank 被迫中路持宝，或敌方长手双路风筝不进入水泡区"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.carrier_bodyguard_side_lane"
    - id: "point_blank_super_anti_assassin_trap"
      map_feature_type: "close_contact_punish_window"
      uses_feature_by: "Super 6 发鱼雷在贴中心时可多发命中，同时回复 50% 已损生命"
      route_or_position: "草口伏击点、球门前、热区中心、矿区侧墙贴脸点"
      objective_conversion: "把敌方刺客/坦克的接触转换成反杀和续站"
      active_when: "Hank 有 Super 或接近满 Super，敌方必须靠近才能完成任务"
      fails_if: "敌方用击退/拉扯/远程消耗逼出 Super，或反治疗削弱回血"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.point_blank_anti_aggro_resource"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "Barricade 持球推进"
        - "满蓄水泡清门前短手"
        - "近身 Super 反打防守坦克/刺客"
      cannot_fulfill:
        - "稳定远程破门"
        - "被控制链守门时强行进球"
      needs_teammate_support:
        - "破门、反控制、远程压低防守者"
      false_positive: "Hank 有身体不等于能进门；如果蓄力反复被取消，他只会浪费球权"
    - mode: "Hot Zone"
      can_fulfill:
        - "墙边水泡区控"
        - "身体站区和减伤顶伤害"
        - "贴脸 Super 反打进区者"
      cannot_fulfill:
        - "无墙开阔区长期追人"
        - "单独处理远程 thrower 清区"
      needs_teammate_support:
        - "长手清外圈、反 thrower、补控制"
      false_positive: "敌方不进水泡范围时 Hank 的区控会变成被风筝"
    - mode: "Gem Grab"
      can_fulfill:
        - "侧路 bodyguard"
        - "墙后水泡威胁"
        - "carrier 撤退线保护"
      cannot_fulfill:
        - "安全主 carrier"
        - "远距离控矿"
      needs_teammate_support:
        - "独立 carrier、矿区长手、视野/探草"
      false_positive: "Hank 能保护撤退线，但不能替队伍提供持续矿区射程"

  failure_modes:
    - id: "charge_cancelled_by_control"
      active_when: "Hank 蓄力中被击退、拉扯、眩晕"
      exposed_by: "[[sources/Fandom-Hank|Fandom-Hank]] attack cancellation mechanics"
      mitigation: "等控制交掉、从墙后蓄力、用 Barricade 走入或让队友先压控制位"
      bp_use: "hard_gate.control_density_check"
    - id: "visible_and_no_auto_heal_while_charging"
      active_when: "Hank 在草里蓄力或长时间维持水泡"
      exposed_by: "Fandom notes Hank is visible in bushes and cannot auto-regenerate while inflating"
      mitigation: "短蓄换血、Health gear/队友治疗、只在安全墙后满蓄"
      bp_use: "map_route_filter"
    - id: "point_blank_super_geometry"
      active_when: "Hank Super 离目标太远或鱼雷角度未命中多发"
      exposed_by: "Fandom fixed radial torpedo pattern and point-blank damage note"
      mitigation: "贴目标中心释放、记鱼雷角度，或等待敌方主动贴脸"
      bp_use: "candidate_eval.super_resource_reliability"
    - id: "kited_by_long_range_or_throwers"
      active_when: "敌方能在水泡范围外稳定输出或隔墙清 Hank"
      exposed_by: "short attack range and charging downtime"
      mitigation: "只在墙体和窄口足够的地图选，搭配开墙/长手压制"
      bp_use: "avoid_open_map_false_positive"

  conditional_matchups:
    - target: ["Jae-Yong", "Poco", "Mr. P", "Sprout"]
      direction: "subject_favored"
      source: "[[sources/PLP-Hank|PLP-Hank]]"
      mechanism: "低爆发/召唤物/墙后控制若无法取消蓄力，会被 Hank 的墙后水泡和 body pressure 推离目标点"
      active_when: "Hank 能靠墙蓄力接近，队友补足远程压制"
      fails_when: "他们有队友硬控保护，或地图开阔到 Hank 无法接近"
      bp_use: "wall_anchor_into_low_burst_control"
    - target: ["Gigi", "Squeak", "Piper", "Cordelius"]
      direction: "subject_favored"
      source: "[[sources/PLP-Hank|PLP-Hank]]"
      mechanism: "Hank 用满蓄水泡威胁墙边/草口并用 Barricade 吃第一轮伤害；近身 Super 惩罚必须接触的目标"
      active_when: "他们被目标路线逼入 Hank 水泡范围，且关键位移/控制已被 bait"
      fails_when: "Piper 等长手保持最大距离，或 Cordelius 隔离后让 Hank 无法贴脸多鱼雷"
      bp_use: "conditional_lane_pressure"
    - target: ["Rosa", "Ash", "Frank", "Bibi", "Trunk"]
      direction: "target_favored"
      source: "[[sources/PLP-Hank|PLP-Hank]]"
      mechanism: "更稳定的近身 body、击退/眩晕/高血量换血会取消或吃掉 Hank 的蓄力窗口"
      active_when: "他们守球门、热区或窄口，Hank 必须正面走入"
      fails_when: "Hank 已有 Super 且能贴中心释放，或队友先压低血线"
      bp_use: "avoid_frontline_mirror_without_support"
    - target: ["Damian", "Sandy", "Tara"]
      direction: "target_favored"
      source: "[[sources/PLP-Hank|PLP-Hank]]"
      mechanism: "墙后控制、隐身/沙暴和拉扯会让 Hank 的蓄力路线暴露并取消攻击"
      active_when: "他们控制草口或目标点，Hank 没有视野/反控"
      fails_when: "Hank 从墙后短窗口释放，或队伍先清掉控制资源"
      bp_use: "requires_control_bait_and_vision"

  slot_notes:
    slot_1: "不宜盲早手，除非地图墙体和模式任务强制近距离争点"
    slot_2_3: "可作为 Brawl Ball/Hot Zone 的前排计划，但后续要补远程和反控"
    slot_4_5: "看到敌方低爆发控制或缺控制链时可响应"
    slot_6: "适合最后手惩罚无击退/无拉扯阵容；不要进长手开阔图"
```

## 关联页面

- [[sources/Fandom-Hank|Fandom 来源摘要: Hank]]
- [[sources/PLP-Hank|PLP 来源摘要: Hank]]
