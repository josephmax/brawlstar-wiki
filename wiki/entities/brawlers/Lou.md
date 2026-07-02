# Lou

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：Frost 进度 / Hot Zone 控场 / 冰冻反坦

## 来源摘要

- Fandom：[[sources/Fandom-Lou|Fandom 来源摘要: Lou]]
- PLP：[[sources/PLP-Lou|PLP 来源摘要: Lou]]
- PLP 推荐模式：Hot Zone

## 角色定位总结

Lou 是靠 Frost 进度和 Super 冰面控制目标区的 Controller。普攻三枚雪锥每枚叠 14.3% Frost，累计满后眩晕 1.5 秒；Super `Can-Do` 可越墙投放 10 秒冰面，区域内持续叠 Frost、阻断自然回血并让转向变难。PLP 默认 `Cryo Syrup / Hypothermia` 把 Hot Zone 中的敌人快速推向冰冻，并随 Frost 进度最高削 50% 输出。短板是 3500 HP、三发细弹需要命中，Frost 2.5 秒后会衰减；机动长手、范围消耗和拉人/毒伤会让 Lou 难以稳定叠满。

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
    effective_range: "very_long_control; 普攻 9.33 格，Super 7.67 格越墙投放"
    projectile_reliability: "medium; 3 枚细弹 0.7 秒卸弹，命中移动目标需要路线限制"
    burst: "low; 击杀依赖 Frost stun 后队友/后续命中"
    sustained_dps: "medium; 1.1 秒 very fast reload，但单枚伤害低"
    objective_damage: "low; 主要控区/控球/控 carrier，不是 Heist race"
    mobility: "low; 无位移"
    survivability: "medium_with_ice_block; 3500 HP，Ice Block 可 1 秒无敌但不能动/攻击"
    engage: "low_to_medium; 靠 Super 预铺目标点而非主动接触"
    disengage: "high_against_short_range; Frost、冰面和 Ice Block 可拖突进"
    anti_aggro: "high_if_frost_stacks; 眩晕、滑地、Hypothermia 输出削减惩罚坦克/刺客"
    anti_tank: "high_on_objective; 坦克站点越久越接近 stun 和伤害削减"
    wall_break: "none"
    throw_or_wall_bypass: "medium_area; Super 可越墙铺冰，普攻不能隔墙"
    area_control: "very_high; 10 秒冰面覆盖 Hot Zone 或球/矿区入口"
    scouting_or_vision: "medium_with_vision_gear; Super 阻回血/迫移动，Vision gear 支持草区持续标记"
    team_support: "high; stun、slow-like滑地、输出削减给队友击杀窗口"
    spawnable_or_pet: "area_syrup; Super 生成 10 秒区域"
    crowd_control: "very_high; Frost stun 1.5 秒，Cryo Syrup 即时 +50% Frost，Hyper Super 落点瞬冻"
    source_trace:
      - "[[sources/Fandom-Lou|Fandom-Lou]]"
      - "[[sources/PLP-Lou|PLP-Lou]]"

  build_switches:
    - build: "Cryo Syrup / Hypothermia / Super Charge, Vision, Damage, Shield"
      source: "[[sources/PLP-Lou|PLP-Lou]]"
      changes_capabilities:
        - "Cryo Syrup 只能在敌人处于 Lou Super 内时使用，并立即增加 50% Frost"
        - "Hypothermia 随 Frost 进度降低敌方输出，最高 50%，让站区 body 和坦克推进变弱"
        - "Super Charge gear 加速冰面循环，Vision 支持草区/Hot Zone 持续标记"
      enables:
        - "Hot Zone 区域锁定"
        - "坦克/刺客进场削伤"
        - "Super -> Gadget 快速 stun"
      mitigates_failure_modes:
        - "frost_decay_before_stun"
        - "tank_survives_low_damage"
      best_when: "敌方必须站在固定区域或通过单一入口，且 Lou 可循环 Super"
      poor_when: "敌方多机动长手分散站位，从冰面外持续输出"
      bp_use: "default_plp_hot_zone_control_build"
    - build: "Ice Block / Supercool variant"
      source: "[[sources/Fandom-Lou|Fandom-Lou]]"
      changes_capabilities:
        - "Ice Block 1 秒无敌可吃 Nani/Tick/Mandy/Dynamike Super 或刺客第一轮爆发"
        - "Supercool 把 Super 区内 Frost 叠加从 14%/秒提高到 16%/秒"
      enables:
        - "反爆发保命"
        - "更稳定 zone freeze"
      mitigates_failure_modes:
        - "lou_bursted_before_freeze"
        - "super_zone_frost_too_slow"
      best_when: "敌方有单次高伤/刺客 burst，或 Lou 需要独自撑过第一轮"
      poor_when: "敌方控制会在 Ice Block 后继续命中，或队伍更需要 Hypothermia 输出削减"
      bp_use: "survival_or_supercool_variant"

  map_feature_hooks:
    - id: "hot_zone_super_full_zone_freeze"
      map_feature_type: "zone_area_freeze_control"
      uses_feature_by: "Super 10 秒冰面覆盖区口/区内，Cryo Syrup 快速补 50% Frost"
      route_or_position: "单热区中心、区口窄线、敌方回区路径"
      objective_conversion: "让敌方进区即被滑地/冻结/削伤，转成己方踩区时间"
      active_when: "目标区可被 Super 覆盖，敌方必须站点或穿过冰面"
      fails_if: "敌方从冰面外远程/投掷清区，或 Lou 没有队友站区"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.hot_zone_freeze_control"
    - id: "brawl_ball_freeze_disarm"
      map_feature_type: "ball_carrier_frost_disarm"
      uses_feature_by: "普攻叠满 Frost stun 让持球者掉球，Super 铺在球/门前阻止拾球"
      route_or_position: "中路球权、球门前三格、球落点和侧草推进口"
      objective_conversion: "打断持球、延迟拾球、或冻结守门人创造射门窗口"
      active_when: "敌方持球或守门必须通过 Lou 的射线/冰面"
      fails_if: "球门未打开且队伍无 scorer，或敌方机动目标反复躲开三枚细弹"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_disarm_and_pickup_denial"
    - id: "gem_mine_super_and_carrier_freeze"
      map_feature_type: "gem_mine_frost_control"
      uses_feature_by: "Super 铺矿区让敌方收宝风险升高，普攻/Hyper 可冻结 carrier"
      route_or_position: "宝石矿正中、carrier 退线、矿区侧墙入口"
      objective_conversion: "保护收宝、冻结 carrier 逼掉宝，或让敌方不能安全进矿"
      active_when: "矿区路线固定，Lou 有 Super cycle 或 Hyper 落点"
      fails_if: "敌方远程从矿区外打 Lou，或队伍缺拾宝/收割"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.mine_freeze_and_carrier_punish"
    - id: "anti_tank_choke_hypothermia"
      map_feature_type: "choke_anti_tank_damage_debuff"
      uses_feature_by: "Frost stun 与 Hypothermia 输出削减让坦克/短手穿越 chokepoint 的收益下降"
      route_or_position: "热区入口、球路草口、矿区侧草和短手必须进入的窄线"
      objective_conversion: "把坦克推进变成低输出慢速目标，给队友集火窗口"
      active_when: "坦克/刺客必须重复经过同一条路线，且 Lou 保持射线"
      fails_if: "目标有突进绕后、免控/净化，或长手队友先把 Lou 打退"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
      bp_use: "candidate_eval.anti_tank_route_lock"

  objective_contracts:
    - mode: "Hot Zone"
      can_fulfill:
        - "区内 Super 覆盖和快速冰冻"
        - "Hypothermia 削站区者输出"
        - "Vision gear 草边持续标记"
      cannot_fulfill:
        - "单人长期站区"
        - "从墙后清所有 thrower"
      needs_teammate_support:
        - "站区 body、区外长手、投掷处理"
      false_positive: "Lou 控区强，但需要队友把冰冻窗口转成实际踩区/击杀"
    - mode: "Brawl Ball"
      can_fulfill:
        - "冻结持球者掉球"
        - "Super 封球落点/门前"
      cannot_fulfill:
        - "稳定破门或主 scorer"
        - "追高速目标到开阔地"
      needs_teammate_support:
        - "射门位、破墙、反突进"
      false_positive: "Lou 能防球路，但没有进球工具；进攻端要靠队友"
    - mode: "Gem Grab"
      can_fulfill:
        - "矿区冰面控制"
        - "冻结 carrier 或 bodyguard"
      cannot_fulfill:
        - "安全主 carrier"
        - "独自处理长手开阔线"
      needs_teammate_support:
        - "主 carrier、长手输出、收割冰冻目标"
      false_positive: "Frost 控制 carrier 后必须有队友接宝/补伤害"

  failure_modes:
    - id: "thin_projectiles_and_frost_decay"
      active_when: "Lou 间断命中，敌方 2.5 秒后让 Frost 开始衰减"
      exposed_by: "[[sources/Fandom-Lou|Fandom-Lou]] Frost meter and projectile details"
      mitigation: "选择 choke/zone 路线，铺 Super 后再用 Cryo Syrup/普攻补满"
      bp_use: "projectile_reliability_gate"
    - id: "cryo_syrup_requires_enemy_inside_super"
      active_when: "Lou 没有 Super 区内目标却指望 Gadget 直接冻人"
      exposed_by: "Cryo Syrup cannot be used if no enemies are in Lou's Super"
      mitigation: "先铺 Super 覆盖目标任务点，再等敌方进区使用 Gadget"
      bp_use: "build_resource_sequence_check"
    - id: "ice_block_immobile_after_control"
      active_when: "Lou 用 Ice Block 吃控制但解冻后仍被 stun/围杀"
      exposed_by: "Fandom notes Ice Block immobile and weak into some stun timings"
      mitigation: "用于吃单次高伤或刺客卸弹，不用于已经被控制链覆盖的位置"
      bp_use: "survival_false_positive_filter"
    - id: "outranged_or_flanked_before_super_cycle"
      active_when: "敌方 long range/thrower 从冰面外压低 Lou"
      exposed_by: "Lou low health and PLP target_favored range/mobility signals"
      mitigation: "补前排/开墙/视野，不在无掩护长线让 Lou 单独控区"
      bp_use: "map_openness_and_peel_check"

  conditional_matchups:
    - target: ["El Primo", "Bull", "Jacky", "Frank", "Darryl"]
      direction: "subject_favored"
      source: "[[sources/PLP-Lou|PLP-Lou]]"
      mechanism: "坦克/短手在进区或球路停留越久越容易被 Frost stun 和 Hypothermia 削伤"
      active_when: "目标必须经过 Lou 的冰面/射线并缺净化或远程护送"
      fails_when: "目标从草墙瞬间贴脸，Lou 无 Ice Block/Super，或队友无法击杀冻住目标"
      bp_use: "anti_tank_objective_response"
    - target: ["Poco", "Pam", "8-Bit"]
      direction: "subject_favored"
      source: "[[sources/PLP-Lou|PLP-Lou]]"
      mechanism: "站桩 sustain/阵地 body 被冰面和输出削减拖慢，无法轻松占住固定区"
      active_when: "战斗围绕 Hot Zone/矿区/球点聚集，Lou 有 Super cycle"
      fails_when: "他们用队友长手/投掷先清 Lou，或 sustain shell 分散不站冰面"
      bp_use: "zone_sustain_shell_counter"
    - target: ["Stu", "Max", "Bea", "Griff"]
      direction: "target_favored"
      source: "[[sources/PLP-Lou|PLP-Lou]]"
      mechanism: "机动、长线 burst 或高 DPS 让 Lou 难以连续命中细弹并维持 Frost"
      active_when: "地图开阔，目标可从冰面外打 Lou 或快速换线"
      fails_when: "目标被迫进 Hot Zone/choke，或队友 slow/控制先限制移动"
      bp_use: "avoid_open_lane_without_cover"
    - target: ["Crow", "Emz", "Tara", "Lola"]
      direction: "target_favored"
      source: "[[sources/PLP-Lou|PLP-Lou]]"
      mechanism: "毒伤/范围喷雾/拉人/分身长线会打断 Lou 的站线和 Frost cycle"
      active_when: "他们能从侧角或墙边压 Lou，迫使他交 Super 防守而非控目标"
      fails_when: "Lou 先铺目标区并有前排保护，或队友清掉分身/拉人威胁"
      bp_use: "requires_frontline_and_angle_control"

  slot_notes:
    slot_1: "Hot Zone 明确且队伍能站区时可早手；开阔图会被长手后手惩罚"
    slot_2_3: "作为控区/反坦计划核心，后续补实际站区和击杀"
    slot_4_5: "看到敌方坦克、阵地 sustain 或球路短手时响应价值高"
    slot_6: "最后手可封死单一目标区，但不能补队伍缺输出/站区 body"
```

## 关联页面

- [[sources/Fandom-Lou|Fandom 来源摘要: Lou]]
- [[sources/PLP-Lou|PLP 来源摘要: Lou]]
