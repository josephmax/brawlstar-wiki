# Meg

## 基本信息

- 稀有度：Legendary
- 定位：Tank
- 类型：机甲形态中线控制 / 目标区前排

## 来源摘要

- Fandom：[[sources/Fandom-Meg|Fandom 来源摘要: Meg]]
- PLP：[[sources/PLP-Meg|PLP 来源摘要: Meg]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Hot Zone, Heist

## 角色定位总结

Meg 的 BP 价值是形态节奏：本体很脆但移动快、射程长，机甲形态提供身体、宽弹幕和近身 swing 控制。她适合需要“站住中线/热区/球门前”的地图，也能在 Heist 用机甲期打出可观 safe 压力。风险在于变身 1 秒窗口可被打断，机甲破掉后本体容易被收割，且召唤物、墙后压制和高爆发近战会把她的形态循环打断。

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
    effective_range: "long_stateful; 本体 9 格低伤 poke，机甲 7.33 格宽弹幕负责中线压制"
    projectile_reliability: "medium_high_in_mecha; 宽弹幕和 swing 对中近距离可靠，远距离单点精度一般"
    burst: "medium; 机甲 Super swing 近身爆发高，本体爆发低"
    sustained_dps: "high_in_mecha; 机甲 1.1 秒装填和多弹幕适合持续压目标区，本体输出较低"
    objective_damage: "high_when_mecha_online; Heist 和目标区推进依赖机甲 uptime"
    mobility: "stateful; 本体 very fast，机甲 normal，整体不是突进位"
    survivability: "stateful_high_if_mecha; 本体 2400 HP 很脆，机甲 3700 HP 加 Jolting Volts 提高站场"
    engage: "medium; 通过机甲身体和范围 swing 推进，不靠瞬间位移"
    disengage: "low_after_mecha_break; 机甲破后本体易被追死"
    anti_aggro: "medium_high_in_mecha; 宽弹幕、swing、Heavy Metal 爆炸/击退可阻止近身推进"
    anti_tank: "medium; 机甲持续火力可磨前排，但怕高爆发贴脸和控制链"
    wall_break: "none"
    throw_or_wall_bypass: "none"
    area_control: "high_in_mecha; 宽弹幕和 swing 能守入口、热区和球门"
    scouting_or_vision: "low"
    team_support: "conditional; Toolbox 可提供范围 reload buff，但 PLP 默认不是核心 build"
    spawnable_or_pet: "conditional; Toolbox turret 作为团队 reload anchor"
    crowd_control: "conditional; Heavy Metal 在机甲破坏时击退，Mecha swing 提供近身驱赶"

  build_switches:
    - build: "Jolting Volts / Heavy Metal / Shield, Damage"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      changes_capabilities:
        - "提高机甲 uptime，并在机甲被毁时用爆炸/击退保护本体或阻止突进"
      enables:
        - "Hot Zone/Brawl Ball 的目标区身体"
        - "Heist 的机甲期 safe 压力"
        - "Gem Grab 中线控场"
      mitigates_failure_modes:
        - "base_form_collapse_after_mecha_destroyed"
        - "mecha_uptime_taxed_by_poke"
      best_when: "地图奖励站点、守入口或持续目标压力"
      poor_when: "敌方能用墙后投掷、召唤物或高爆发近身持续打断机甲循环"
      bp_use: "default_plp_mecha_control_build"
    - build: "Toolbox / Force Field or Heavy Metal / Shield, Damage"
      source: "[[sources/Fandom-Meg|Fandom-Meg]]"
      changes_capabilities:
        - "把 Meg 从纯机甲身体改成团队 reload anchor"
      enables:
        - "Heist/Hot Zone 中给队友提高持续输出或守区效率"
      mitigates_failure_modes:
        - "team_lacks_sustained_fire"
      best_when: "队友能安全围绕 turret 输出，敌方缺低成本清炮台"
      poor_when: "地图需要 Meg 自己持续抗线，或敌方投掷能轻松清 Toolbox"
      bp_use: "team_reload_variant"

  map_feature_hooks:
    - id: "hot_zone_mecha_mid_body_control"
      map_feature_type: "single_zone_body_and_entry_control"
      uses_feature_by: "机甲身体站圈，宽弹幕和 swing 守入口，Jolting Volts 延长站圈时间"
      objective_conversion: "Hot Zone 单圈图中把站住中心转成持续计分"
      active_when: "入口清晰、敌方必须穿过 choke 进圈，队友能帮 Meg 清投掷/召唤物"
      fails_if: "敌方墙后投掷或召唤物反复消耗机甲，或变身窗口被打断"
      example_maps: ["[[entities/maps/Dueling Beetles|Dueling Beetles]]", "[[entities/maps/Ring of Fire|Ring of Fire]]", "[[entities/maps/Open Business|Open Business]]", "[[entities/maps/Parallel Plays|Parallel Plays]]"]
      bp_use: "Hot Zone 中心身体核心"
    - id: "brawl_ball_mecha_goal_defense_and_push_body"
      map_feature_type: "goal_entry_pressure_and_anti_aggro"
      uses_feature_by: "机甲在球门前抗伤、用 swing/Heavy Metal 阻断持球突进，同时作为推进身体给 scorer 开路"
      objective_conversion: "把人数/血量优势转成持球推进或防守清球"
      active_when: "队伍有破门、得分手或控人，Meg 负责站住球门区域"
      fails_if: "敌方用投掷/召唤物绕过机甲，或机甲破后本体被连续击杀导致防线断层"
      example_maps: ["[[entities/maps/Center Stage|Center Stage]]", "[[entities/maps/Sneaky Fields|Sneaky Fields]]", "[[entities/maps/Triple Dribble|Triple Dribble]]", "[[entities/maps/Pinball Dreams|Pinball Dreams]]"]
      bp_use: "足球前排/防守核心；仍需 scoring tool"
    - id: "heist_mecha_safe_lane_uptime"
      map_feature_type: "safe_dps_after_lane_win"
      uses_feature_by: "机甲期宽弹幕和持续输出赢边路后打 safe，Jolting Volts 延长 safe pressure"
      objective_conversion: "把机甲上线期转成金库 race 领先"
      active_when: "Meg 能安全变身并靠队友赢线，敌方缺快速清机甲资源"
      fails_if: "本体期被压死，或敌方 race 更快且无须处理 Meg"
      example_maps: ["[[entities/maps/Hot Potato|Hot Potato]]", "[[entities/maps/Pit Stop|Pit Stop]]", "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]", "[[entities/maps/Bridge Too Far|Bridge Too Far]]"]
      bp_use: "Heist 条件 safe pressure，依赖机甲上线"
    - id: "gem_mid_mecha_control_with_carrier_warning"
      map_feature_type: "gem_mine_mid_control"
      uses_feature_by: "机甲站中线和入口，宽弹幕压缩敌方拾宝空间"
      objective_conversion: "控制宝石矿和撤退半径，但不建议在机甲破坏风险高时做唯一 carrier"
      active_when: "队伍有独立 carrier 或能保护本体重置"
      fails_if: "Meg 机甲破后携带宝石，或敌方侧草/投掷持续逼退中心"
      example_maps: ["[[entities/maps/Gem Fort|Gem Fort]]", "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]", "[[entities/maps/Double Swoosh|Double Swoosh]]"]
      bp_use: "Gem Grab 中线身体；carrier 职责需谨慎分配"

  objective_contracts:
    - mode: "Hot Zone"
      can_fulfill:
        - "机甲站圈、守入口、用范围 swing 清进圈"
      cannot_fulfill:
        - "独自处理墙后投掷/炮台体系"
      needs_teammate_support:
        - "清投掷、开墙、治疗或区域控制"
      false_positive: "Meg 能站圈，但若机甲循环被断，计分能力会瞬间下降"
    - mode: "Brawl Ball"
      can_fulfill:
        - "球门防守、前排推进、吸收火力"
      cannot_fulfill:
        - "单独破门或稳定 carry 进球"
      needs_teammate_support:
        - "scorer、破门/强控、清投掷"
      false_positive: "有身体不等于有得分路径"
    - mode: "Heist"
      can_fulfill:
        - "机甲上线后边路压制和 safe DPS"
      cannot_fulfill:
        - "本体期稳定打库或远程低承诺打库"
      needs_teammate_support:
        - "帮 Meg 安全变身、赢线和防快攻"
      false_positive: "Heist 价值高度依赖机甲 uptime，不是开局就稳定 race"
    - mode: "Gem Grab"
      can_fulfill:
        - "中线站位、入口压制、保护 carrier 撤退路线"
      cannot_fulfill:
        - "在高风险机甲破坏阶段做唯一 carrier"
      needs_teammate_support:
        - "独立载宝位、探草和反投掷"
      false_positive: "中线身体强不代表载宝安全"

  failure_modes:
    - id: "mecha_transform_cancel_window"
      active_when: "Meg 开 Super 变身时处于敌方 stun、knockback、pull 或爆发范围"
      exposed_by: "Super has 1 second delay and can be cancelled"
      mitigation: "在墙后、安全血量或队友控线后变身"
      bp_use: "resource_timing_check"
    - id: "base_form_collapse_after_mecha_destroyed"
      active_when: "机甲被打掉后，本体 2400 HP 被追击"
      exposed_by: "stateful HP and no hard escape"
      mitigation: "Heavy Metal/Force Field、队友 peel、避免本体携带关键目标"
      bp_use: "avoid_as_sole_carrier_or_last_body"
    - id: "thrower_spawnable_or_close_swarm_tax"
      active_when: "敌方用 Nita、Larry & Lawrie、Damian、Lumi 或墙后投掷持续消耗机甲"
      exposed_by: "PLP counteredBy and no wall bypass"
      mitigation: "补开墙、清召唤物或反投掷"
      bp_use: "must_answer_before_picking_meg"
    - id: "open_sniper_kiting_before_mecha_online"
      active_when: "本体期无法安全充 Super 或走到目标区"
      exposed_by: "base form low HP and low damage"
      mitigation: "靠掩体、队友压线或选择中短线目标图"
      bp_use: "avoid_if_mecha_access_is_unreliable"

  conditional_matchups:
    - target: ["Nani", "Piper", "Byron", "Glowy"]
      direction: "subject_favored"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      mechanism: "机甲身体和宽弹幕能在目标区逼迫脆长手后退，使其难以只靠单发 poke 控目标"
      active_when: "Meg 已机甲上线且地图目标要求对方靠近中线/热区/球门"
      fails_when: "地图极开阔，Meg 在本体期就被压死，或长手能从安全 off-angle 持续风筝"
      bp_use: "mid_control_into_fragile_range"
    - target: ["Jae-Yong", "Squeak", "Sprout", "Bolt"]
      direction: "subject_favored"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      mechanism: "机甲能吃支援/控制型低爆发输出并持续推进，迫使对手交资源处理身体"
      active_when: "墙体不让投掷免费输出，且 Meg 有队友保护机甲路径"
      fails_when: "投掷口袋完整，或 Squeak/Sprout 等能从墙后反复消耗无代价"
      bp_use: "body_pressure_response"
    - target: ["Rosa", "Bibi", "Edgar"]
      direction: "target_favored"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      mechanism: "高近身爆发、草丛接近或贴脸连击能绕过 Meg 的中距离压制，并在机甲破后收本体"
      active_when: "草墙路线或球门/zone 入口让目标能贴到 Meg"
      fails_when: "Meg 有 Heavy Metal、队友控制和开阔视野提前消耗"
      bp_use: "requires_peel_and_grass_control"
    - target: ["Nita", "Larry & Lawrie", "Damian", "Lumi", "Sirius"]
      direction: "target_favored"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      mechanism: "召唤物、墙后控制或持续区域压力会税掉机甲血量和变身空间"
      active_when: "地图有墙后口袋或中心入口拥挤，Meg 必须先处理附加目标"
      fails_when: "队友能快速清召唤物/开墙，Meg 可直接站住目标区"
      bp_use: "do_not_pick_without_clear_plan"

  slot_notes:
    slot_1: "Hot Zone 或 Brawl Ball 中线/球门图可早手，但要准备回答投掷与召唤物"
    slot_2_3: "适合建立目标区身体核心，让后续补开墙、清草、得分或 safe DPS"
    slot_4_5: "看到敌方缺反前排、缺墙后消耗时价值更稳"
    slot_6: "惩罚脆长手或低爆发支援阵容，但不能修补队伍缺开墙/缺清召唤物的问题"
```

## 关联页面

- [[sources/Fandom-Meg|Fandom 来源摘要: Meg]]
- [[sources/PLP-Meg|PLP 来源摘要: Meg]]
