# Jae-yong

## 基本信息

- 稀有度：Mythic
- 定位：Support
- 类型：长线团队加速 / 治疗支援

## 来源摘要

- Fandom：[[sources/Fandom-Jae-yong|Fandom 来源摘要: Jae-yong]]
- PLP：[[sources/PLP-Jae-yong|PLP 来源摘要: Jae-yong]]
- PLP 推荐模式：Knockout, Bounty

## 角色定位总结

Jae-yong 的 BP 价值不是单人击杀，而是用长距离穿透弹道、Work mode 的路径加速、Party mode 的穿透治疗，以及自动充能 Super 的切换节奏，帮助队伍更早到达关键点、维持换血优势或带球/载宝撤退。Weekend Warrior 可以短时间补足低 DPS，Time For a Slow Song 则把他从纯支援改成反近身与封路工具。

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
    effective_range: "long; 8.33 格穿透弹道，主要用来提供支援线、探草命中和队伍换速，而非单点爆发"
    projectile_reliability: "medium_high; 弹道可穿透且宽容度高，但伤害低，命中本身不能直接完成击杀"
    burst: "low_baseline; Weekend Warrior 激活后进入 medium，配合 Extra High Note 和多目标穿透时可惩罚抱团"
    sustained_dps: "low_medium; 1.5 秒装填和低基础伤害使他无法承担主 DPS 位"
    objective_damage: "low; 不作为 Heist 或纯拆目标英雄"
    mobility: "team_high; Work slipstream、切回 Work 的范围加速和 The Crowd Goes Mild 可让队伍抢点、撤退或追击"
    survivability: "medium; 3700 HP 加自疗/加速可拉扯，但被近身隔离后很脆"
    engage: "team_speed_engage; 通过开局加速、Super 加速和草/通道穿透帮助队友先到位"
    disengage: "team_speed_or_heal_reset; Party 治疗、Work 加速和 slow gadget 可帮助队伍脱离第二波交火"
    anti_aggro: "medium; Time For a Slow Song 和 Work speed 能拖住刺客接近，但没有硬控或位移"
    anti_tank: "low_medium; 依赖队友吃到速度/治疗后 kite，不适合独自处理高血量前排"
    wall_break: "none"
    throw_or_wall_bypass: "none"
    area_control: "medium; slipstream 或 slow paperwork 在通道、宝石矿和撤退路线上形成短时路线收益"
    scouting_or_vision: "medium_with_vision_gear; 长宽穿透弹道适合在草图用 Vision gear 反复标记"
    team_support: "very_high; 速度、治疗、自动充能 Super 和范围模式切换是核心价值"
    crowd_control: "conditional; Time For a Slow Song 提供范围与路径减速"

  build_switches:
    - build: "Weekend Warrior / The Crowd Goes Mild / Shield, Damage"
      source: "[[sources/PLP-Jae-yong|PLP-Jae-yong]]"
      changes_capabilities:
        - "把低击杀支援临时转成可收残血的中等爆发位"
        - "让 Hypercharge 与 Extra High Note 类输出窗口更容易转成击杀"
      enables:
        - "Bounty/Knockout 中抢第一波位置后，用爆发窗口结束低血目标"
        - "面对中低血量远程、召唤物或支援位时减少队友补伤压力"
      mitigates_failure_modes:
        - "low_dps_support_shell"
      best_when: "队伍已有主要输出，只需要 Jae-yong 在关键窗口补伤和保人"
      poor_when: "敌方能强开近身，或地图主要矛盾是墙后投掷/硬控而非换血"
      bp_use: "default_plp_build_for_open_lane_support"
    - build: "Time For a Slow Song / The Crowd Goes Mild / Vision, Shield"
      source: "[[sources/Fandom-Jae-yong|Fandom-Jae-yong]]"
      changes_capabilities:
        - "把支援路线从加速转为防突进和探草封路"
      enables:
        - "草多图保护 gem carrier 或长线核心"
        - "对 Lily、Mico、Sam、Stu 类接近英雄制造失速窗口"
      mitigates_failure_modes:
        - "assassin_contact_without_slow_or_speed"
      best_when: "敌方接近路线清晰，且我方需要保护主输出或载宝位"
      poor_when: "我方缺伤害，需要 Jae-yong 自己补击杀"
      bp_use: "anti_engage_variant"

  map_feature_hooks:
    - id: "bounty_blue_star_speed_cross"
      map_feature_type: "long_sightline_bounty_start"
      uses_feature_by: "开局向前打出 Work slipstream 或用 Super 加速，让队伍更早争夺 Blue Star 与长线站位"
      objective_conversion: "先到中线后进入低风险保星换血，Jae-yong 用治疗/加速维持星差"
      active_when: "地图长线开阔，队友能利用速度抢到安全线位"
      fails_if: "敌方有强投掷口袋、爆发开线，或我方三人因支援范围抱团被穿透/范围惩罚"
      example_maps: ["[[entities/maps/Shooting Star|Shooting Star]]", "[[entities/maps/Dry Season|Dry Season]]", "[[entities/maps/Hideout|Hideout]]", "[[entities/maps/Layer Cake|Layer Cake]]"]
      bp_use: "Bounty 先手支援计划；必须配真正长线输出"
    - id: "knockout_team_speed_heal_reset"
      map_feature_type: "open_mid_marksman_with_reset"
      uses_feature_by: "在第一波长线换血后用 Party 治疗或 Work 加速让队友重置站位"
      objective_conversion: "Knockout 中把一次没死的换血转成下一次更安全的压缩空间"
      active_when: "敌方主要靠远程换血而不是瞬间强开"
      fails_if: "敌方有可穿墙投掷、可取消 Jae-yong 队形的硬控，或刺客能绕到支援身边"
      example_maps: ["[[entities/maps/Out in the Open|Out in the Open]]", "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]", "[[entities/maps/New Horizons|New Horizons]]", "[[entities/maps/Belle's Rock|Belle's Rock]]"]
      bp_use: "Knockout 支援/重置位；不替代击杀位"
    - id: "gem_mid_slipstream_or_carrier_escape"
      map_feature_type: "gem_mine_route_support"
      uses_feature_by: "早期 slipstream 帮队伍抢矿，中后期 Super 加速或 Party 治疗保护 gem carrier 撤退"
      objective_conversion: "把中线速度优势转成宝石拾取和倒计时撤离"
      active_when: "我方有稳定中路或草控英雄能接住加速收益"
      fails_if: "敌方侧草伏击无人探，或载宝位因依赖 Jae-yong 支援而缺独立逃生"
      example_maps: ["[[entities/maps/Gem Fort|Gem Fort]]", "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]", "[[entities/maps/Double Swoosh|Double Swoosh]]"]
      bp_use: "Gem Grab 条件支援位；需要探草或中路身体"
    - id: "brawl_ball_carrier_speed_support"
      map_feature_type: "score_window_support"
      uses_feature_by: "为持球者提供加速，或用自动充能 Super 在踢球/换模式间维持推进节奏"
      objective_conversion: "把线权转成持球突破，而不是只做远程消耗"
      active_when: "队友有明确 scorer、破门或强控窗口"
      fails_if: "我方没有进球创造者，或敌方范围控制能惩罚持球与支援靠近"
      example_maps: ["[[entities/maps/Center Stage|Center Stage]]", "[[entities/maps/Sneaky Fields|Sneaky Fields]]", "[[entities/maps/Triple Dribble|Triple Dribble]]"]
      bp_use: "足球二层推进工具，不单独解决破门"

  objective_contracts:
    - mode: "Bounty"
      can_fulfill:
        - "开局加速争 Blue Star 和长线站位"
        - "用治疗/速度维持星差，Weekend Warrior 收残血"
      cannot_fulfill:
        - "单独作为主狙或主击杀来源"
      needs_teammate_support:
        - "至少一名稳定远程输出或开墙反投掷工具"
      false_positive: "把 Jae-yong 当纯长手会高估；他的主要收益来自队友能否吃到加速/治疗"
    - mode: "Knockout"
      can_fulfill:
        - "帮助队友先到位、换血后重置、保护关键血线"
        - "用 slow gadget 反制最后手刺客接近"
      cannot_fulfill:
        - "在无输出队友时独立结束回合"
      needs_teammate_support:
        - "击杀确认、投掷反制或反刺客保护"
      false_positive: "队友不吃支援收益时，Jae-yong 会变成低伤害远程"
    - mode: "Gem Grab"
      can_fulfill:
        - "抢中线、保护 carrier 撤退、用 Vision gear 反复探草"
      cannot_fulfill:
        - "独立处理强侧草伏击和高压刺客"
      needs_teammate_support:
        - "中路身体、草控或稳定清草"
      false_positive: "加速不能替代宝石图的探草和入口控制"
    - mode: "Brawl Ball"
      can_fulfill:
        - "给 scorer 加速并在推进中治疗/重置"
      cannot_fulfill:
        - "独自破门或制造硬进球窗口"
      needs_teammate_support:
        - "破门、强控、位移 scorer 或能接速度的坦克"
      false_positive: "只有支援没有得分路径时，不应把他当足球核心"

  failure_modes:
    - id: "low_dps_support_shell"
      active_when: "敌方能承受 Jae-yong 低基础伤害并正面压进"
      exposed_by: "baseline attack low damage and support-first kit"
      mitigation: "使用 Weekend Warrior，或只在队友输出充足时选"
      bp_use: "draft_check_for_primary_damage"
    - id: "grouped_support_splash_punish"
      active_when: "队伍为了吃速度/治疗过度抱团"
      exposed_by: "4.17 格范围支援鼓励靠近"
      mitigation: "只在关键窗口集合，平时分散站线"
      bp_use: "avoid_into_area_burst_or_pierce"
    - id: "assassin_contact_without_slow_or_speed"
      active_when: "Lily、Mico、Sam、Stu 等能绕过长线直接贴身"
      exposed_by: "no hard escape; anti-aggro relies on mode/gadget timing"
      mitigation: "Time For a Slow Song、防突进队友、后手确认敌方缺硬切"
      bp_use: "must_pair_with_peel_on_flank_maps"
    - id: "teammates_do_not_convert_support"
      active_when: "队友缺 range、score route、gem control 或 zone body"
      exposed_by: "Jae-yong 的收益多为队伍增益"
      mitigation: "把他放在已有明确 win condition 的阵容里"
      bp_use: "not_a_standalone_win_condition"

  conditional_matchups:
    - target: ["Gale", "Charlie", "Lola", "Meg"]
      direction: "subject_favored"
      source: "[[sources/PLP-Jae-yong|PLP-Jae-yong]]"
      mechanism: "长距离穿透支援和速度/治疗重置能让队友在控制或中远程换血里多打一轮"
      active_when: "地图允许我方长线站住，且敌方不能直接切掉 Jae-yong"
      fails_when: "敌方控制转成硬开，或墙体/投掷让 Jae-yong 无法安全给线"
      bp_use: "作为支援型回答，前提是我方已有输出"
    - target: ["El Primo", "Mico", "Sam", "Stu"]
      direction: "volatile_subject_favored"
      source: "[[sources/PLP-Jae-yong|PLP-Jae-yong]]"
      mechanism: "Work speed 和 slow gadget 能拉开接近窗口，但只在进场路线可预判时成立"
      active_when: "敌方进场必须经过开阔通道或草口，Jae-yong 还留有 gadget/Super"
      fails_when: "敌方绕后贴身、我方无 peel，或 Jae-yong 为了治疗队友站位过前"
      bp_use: "可作为反接近辅助，不能单独承担 anti-assassin"
    - target: ["Bibi", "Rosa", "Doug", "Sandy"]
      direction: "target_favored"
      source: "[[sources/PLP-Jae-yong|PLP-Jae-yong]]"
      mechanism: "高身体、草控或隐蔽推进能穿过 Jae-yong 的低伤害区，把战斗拖成近身"
      active_when: "草丛/墙体给目标连续接近，或敌方能迫使 Jae-yong 团队抱团"
      fails_when: "地图被清草开阔，且 Jae-yong 带 slow variant 并有队友输出"
      bp_use: "遇到这些前排/隐蔽推进时需补硬控或高 DPS"
    - target: ["Willow", "Lumi", "Damian", "Barley"]
      direction: "target_favored"
      source: "[[sources/PLP-Jae-yong|PLP-Jae-yong]]"
      mechanism: "投掷、墙后控制或区域封路能让 Jae-yong 的长线支援难以安全落点"
      active_when: "地图存在稳定墙后口袋，且我方无开墙/突进回答"
      fails_when: "墙体被打开，或我方能用速度迅速换线切入"
      bp_use: "draft 时检查 wall pocket answer"

  slot_notes:
    slot_1: "仅在 Bounty/Knockout 开阔图、队伍准备围绕长线支援开局时可早手；否则容易暴露低 DPS"
    slot_2_3: "适合作为 sniper 或控制核心的支援补位，补速度、治疗和反接近"
    slot_4_5: "看到敌方缺硬切或依赖中远程换血时价值最高"
    slot_6: "可惩罚无切入、无投掷、无爆发的远程阵容；不能用来补最后一手主输出"
```

## 关联页面

- [[sources/Fandom-Jae-yong|Fandom 来源摘要: Jae-yong]]
- [[sources/PLP-Jae-yong|PLP 来源摘要: Jae-yong]]
