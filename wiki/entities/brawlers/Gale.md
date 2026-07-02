# Gale

## 基本信息

- 稀有度：Epic
- 定位：Controller
- 类型：长射程减速 / 推离 / 入口封锁控制

## 来源摘要

- Fandom：[[sources/Fandom-Gale|Fandom 来源摘要: Gale]]
- PLP：[[sources/PLP-Gale|PLP 来源摘要: Gale]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Hot Zone

## 角色定位总结

Gale 的 BP 价值来自低门槛的路线控制：8.33 格宽普攻负责扫草和持续减速，10 格 Super 可以穿障碍推人，`Twister` 用 5 秒封住短手、坦克、抓钩和冲锋入口。他不是纯输出位，也不是稳定破墙位；他的强度来自把敌方进场、持球、踩区和 carrier 追击转化成“必须绕路或被推走”的时间税。需要注意的是，`Twister` 只阻碍移动不阻止敌人攻击，Super 推远 Piper/Emz 这类远距离收益目标也可能反向放大对方输出。

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
    effective_range: "long_control; 普攻 8.33 格，Super 10 格并可穿障碍"
    projectile_reliability: "high_for_area_sweep_medium_for_focus_kill; 6 个雪弹宽线易扫草/多人，但正常体型近距离最多约 4 发命中"
    burst: "medium_with_blustery_wall_stun; 需要 Super 推墙 1.25 秒 stun 后接普攻"
    sustained_dps: "medium; 1.2 秒 very fast reload 支撑持续压线，但单发伤害低"
    objective_damage: "low_to_medium; Heist 只能靠近距离多雪弹或 Spring Ejector 送队友，不是主 race"
    mobility: "team_route_tool; Spring Ejector 6 格弹板提供转点/返场/进库路径"
    survivability: "medium; 4000 HP，靠推离、减速和 Twister 保距离"
    engage: "medium; 可用 Super 把敌人推入队友或墙，不是自带突进"
    disengage: "high; Super 推开、Twister 断路、Freezing Snow 减速"
    anti_aggro: "high; Super/Twister/slow 对刺客、坦克、抓钩和冲锋进场成本很低"
    anti_tank: "high_when_route_is_narrow; 推离、减速和 Twister 让短手失去接触窗口"
    wall_break: "none"
    throw_or_wall_bypass: "medium_control_only; Super 穿障碍推人，Spring Ejector 越过地形，但普攻不能隔墙输出"
    area_control: "high; Twister 2 格半径持续 5 秒，Super 宽风路清入口"
    scouting_or_vision: "medium; 宽普攻扫草，Twister/slow 逼出草口路径"
    team_support: "high; 弹板转点、Super 保 carrier、Twister 帮队友守区"
    spawnable_or_pet: "terrain_tool; Spring Ejector 是持久弹板，Twister 是短时地形控制物"
    crowd_control: "very_high; knockback, slow, wall-stun, route denial"
    source_trace:
      - "[[sources/Fandom-Gale|Fandom-Gale]]"
      - "[[sources/PLP-Gale|PLP-Gale]]"

  build_switches:
    - build: "Twister / Freezing Snow / Shield, Damage"
      source: "[[sources/PLP-Gale|PLP-Gale]]"
      changes_capabilities:
        - "Twister 把 5 秒入口封锁加入 Gadget 资源，用来挡 Buzz/Fang/Darryl/Bull/Colette 等位移路线"
        - "Freezing Snow 让每次普攻命中附带 0.5 秒 slow，提升压区和防突进稳定性"
        - "Shield gear 给中血控制位更多站线容错，Damage gear 提高推墙后的击杀确认"
      enables:
        - "Hot Zone 单区入口封锁"
        - "Brawl Ball 持球人缴械与门前剥离"
        - "Gem Grab carrier 保护和矿区慢压"
      mitigates_failure_modes:
        - "aggro_crosses_control_line"
        - "wide_attack_low_focus_damage"
      best_when: "地图有窄口、草边或目标点入口，敌方依赖短手/位移/持球进入"
      poor_when: "敌方主输出可在 Twister 外远程打人，或队伍缺少实际击杀/目标伤害"
      bp_use: "default_plp_control_build"
    - build: "Spring Ejector / Blustery Blow variants"
      source: "[[sources/Fandom-Gale|Fandom-Gale]]"
      changes_capabilities:
        - "Spring Ejector 可隐藏在草里并长期存在，用于返场、进区、进库或越过障碍"
        - "Blustery Blow 在 Super 把敌人推到墙体时提供 1.25 秒 stun"
      enables:
        - "队友快速回区或越墙进攻"
        - "Heist/Siege 类目标快速接触"
        - "墙边击杀确认"
      mitigates_failure_modes:
        - "team_cannot_rotate_to_objective"
        - "super_only_pushes_without_kill"
      best_when: "地图有安全弹板落点、关键目标需要快速抵达，或墙体能稳定承接 Super"
      poor_when: "落点被守、弹板给敌人同样利用，或团队更需要 Twister 断突进"
      bp_use: "rotation_or_wall_stun_variant"

  map_feature_hooks:
    - id: "hot_zone_twister_entry_denial"
      map_feature_type: "single_or_choke_zone_entry_control"
      uses_feature_by: "Twister 封住区口 5 秒，Freezing Snow 让绕口进入的目标被持续减速"
      route_or_position: "单热区边缘、草口、墙边窄入口和敌方回区路线"
      objective_conversion: "延长己方踩区时间，逼敌方晚进区或绕路暴露在队友火力中"
      active_when: "区口可被 2 格半径 Twister 覆盖，敌方主要靠短手或位移进区"
      fails_if: "敌方长手可站在 Twister 外输出，或 thrower/墙后伤害直接清区"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "map_bp_factors.hot_zone_entry_tax"
    - id: "brawl_ball_super_disarm_and_goal_peel"
      map_feature_type: "ball_carrier_knockback"
      uses_feature_by: "Super 推走持球者并影响掉球位置，Twister 阻止短手/抓钩直接穿门"
      route_or_position: "中路球权、球门前三格、侧草推进线和 overtime 直线推进路"
      objective_conversion: "打断持球推进、清守门人，或把球/奖杯从 carrier 身上剥离"
      active_when: "Gale 有 Super 或 Twister，队友能接住掉球或补击杀"
      fails_if: "敌方有远程破门/墙后进攻，或 Gale 把目标推到更安全的射门角"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.ball_disarm_and_defensive_peel"
    - id: "gem_carrier_peel_and_mine_control"
      map_feature_type: "carrier_peel_and_mine_slow"
      uses_feature_by: "Super 把追击者从 carrier 身边推开，普攻 slow 和宽线扫草保矿区"
      route_or_position: "宝石矿左右口、carrier 倒计时撤退线、草边绕后入口"
      objective_conversion: "保住倒计时、延迟敌方接近矿区，并让己方 carrier 有时间撤退"
      active_when: "队伍已有稳定 carrier，Gale 负责 peel 而非拿宝"
      fails_if: "敌方远程能无视推离继续输出，或 Gale 没有 Super 时被双路夹击"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.gem_carrier_protection"
    - id: "spring_ejector_safe_or_zone_rotation"
      map_feature_type: "team_rotation_pad"
      uses_feature_by: "Spring Ejector 在草里或安全位铺弹板，让队友快速返区/进库/越过障碍"
      route_or_position: "己方出生到热区捷径、Heist 侧路进库线、Brawl Ball 后场返中路"
      objective_conversion: "把一次 Gadget 转成先到点、逼回防或 surprise lane entry"
      active_when: "落点未被敌方预控，队友能利用弹板后的短窗口打目标"
      fails_if: "敌方守落点、弹板方向暴露，或敌人反过来利用同一路径"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
      bp_use: "map_bp_factors.rotation_shortcut_with_landing_risk"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "矿区 slow 与扫草"
        - "carrier peel 和倒计时保护"
        - "Super 推开坦克/刺客追击"
      cannot_fulfill:
        - "独立长时间持宝抗压"
        - "远程击杀收割核心"
      needs_teammate_support:
        - "稳定 carrier、远程击杀、处理 thrower/长手输出"
      false_positive: "Gale 能保护 carrier，但如果队伍没人能持宝或收割，他只会拖时间"
    - mode: "Brawl Ball"
      can_fulfill:
        - "门前推离与掉球"
        - "Twister 封进球路线"
        - "Spring Ejector 快速返场或侧路推进"
      cannot_fulfill:
        - "稳定破墙"
        - "纯靠自己射门结束回合"
      needs_teammate_support:
        - "破门/射门位、远程火力、处理墙后输出"
      false_positive: "Super 推到人不一定等于进球；必须确认球落点和队友接应"
    - mode: "Hot Zone"
      can_fulfill:
        - "区口 5 秒封锁"
        - "slow 回区者"
        - "保护队友站区"
      cannot_fulfill:
        - "单人长期踩区并击杀全部对手"
        - "处理所有墙后投掷火力"
      needs_teammate_support:
        - "站区 body、thrower/长手处理、实际击杀"
      false_positive: "Twister 只挡移动不挡射击；敌方能在外面打区时 Gale 需要队友补输出"

  failure_modes:
    - id: "twister_blocks_movement_not_damage"
      active_when: "敌方长手或 thrower 站在 Twister 外继续输出"
      exposed_by: "[[sources/Fandom-Gale|Fandom-Gale]] notes Twister hinders movement, not attacks"
      mitigation: "只在短手入口、球路、carrier 追击线使用，或配合队友压掉远程火力"
      bp_use: "map_factor_false_positive_filter"
    - id: "super_push_improves_enemy_range"
      active_when: "Gale 把 Piper/Emz 等远距离收益英雄推到更适合输出的位置"
      exposed_by: "[[sources/Fandom-Gale|Fandom-Gale]] cautions about Emz/Piper range payoff"
      mitigation: "推墙 stun、推入队友或毒圈方向；不要无脑把远程打远"
      bp_use: "candidate_eval.control_direction_check"
    - id: "wide_attack_low_single_target_damage"
      active_when: "需要 Gale 单杀高血量目标或近距离爆发"
      exposed_by: "Fandom attack spread and close-range snowball hit count"
      mitigation: "把 Gale 作为控制/peel 位，另补 burst 或 objective DPS"
      bp_use: "role_gap_filter"
    - id: "spring_pad_landing_trap"
      active_when: "弹板落点被敌方预控，或敌方也能利用弹板"
      exposed_by: "Spring Ejector launches any target and has fixed facing/landing behavior"
      mitigation: "隐藏在草里、改位置、只在落点有队友压制时启用"
      bp_use: "rotation_risk_gate"

  conditional_matchups:
    - target: ["Mortis", "Fang", "Leon", "Mina"]
      direction: "subject_favored"
      source: "[[sources/PLP-Gale|PLP-Gale]]"
      mechanism: "Twister、Super 推离和 Freezing Snow 减速会切断刺客/短手从草口或墙边获得首次接触的路线"
      active_when: "接触路线狭窄，Gale 保留 Gadget/Super，队友能在被推离后补伤害"
      fails_when: "Gale 技能已交、被多路夹击，或刺客从视野外直接贴到身后"
      bp_use: "anti_aggro_response_pick"
    - target: ["Bolt", "Carl", "Griff", "Glowy"]
      direction: "subject_favored"
      source: "[[sources/PLP-Gale|PLP-Gale]]"
      mechanism: "宽线 slow 和 Super 位移能打断直线压线、钩入/回旋镐节奏和中距离站位推进"
      active_when: "他们需要沿固定路线进入矿区/球路/热区，且缺低成本远程压制 Gale"
      fails_when: "地图过开阔，目标在 Twister 外稳定输出，或队友无法利用 slow 收割"
      bp_use: "lane_control_answer"
    - target: ["Chester", "Pierce", "Sirius", "Shade"]
      direction: "target_favored"
      source: "[[sources/PLP-Gale|PLP-Gale]]"
      mechanism: "高爆发、绕墙/特殊路线或远近混合威胁能惩罚 Gale 中血量和低爆发本体"
      active_when: "他们可以避开正面风路，从侧墙、草边或 burst 窗口接触 Gale"
      fails_when: "Gale 有墙边 Super stun、队友先控视野，或地图入口被 Twister 完整覆盖"
      bp_use: "avoid_blind_pick_without_peel"
    - target: ["Poco", "Jae-Yong", "Meeple", "Damian"]
      direction: "target_favored"
      source: "[[sources/PLP-Gale|PLP-Gale]]"
      mechanism: "持续治疗/团队增益/墙后工具会把 Gale 的低伤害控制拖成无法转击杀的时间交换"
      active_when: "Gale 队伍缺 burst 或反治疗，敌方能在被推离后快速复位"
      fails_when: "Gale 的目标只是守倒计时/守球门，或队友有足够爆发利用 slow"
      bp_use: "draft_requires_damage_followup"

  slot_notes:
    slot_1: "只有在地图入口明确、队伍愿意围绕控制打时可早手；否则会暴露缺伤害"
    slot_2_3: "适合作为 Hot Zone/Brawl Ball/Gem Grab 的路线控制核心，后续必须补击杀或目标 DPS"
    slot_4_5: "看到敌方短手/冲锋/抓钩路线后非常适合响应"
    slot_6: "可作为最后手封死单一路线进场，但不要用来修补队伍缺输出的问题"
```

## 关联页面

- [[sources/Fandom-Gale|Fandom 来源摘要: Gale]]
- [[sources/PLP-Gale|PLP 来源摘要: Gale]]
