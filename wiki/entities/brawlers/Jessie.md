# Jessie

## 基本信息

- 稀有度：Super Rare
- 定位：Controller
- 类型：弹射压线 / 炮台据点 / Spark Plug 减速控制

## 来源摘要

- Fandom：[[sources/Fandom-Jessie|Fandom 来源摘要: Jessie]]
- PLP：[[sources/PLP-Jessie|PLP 来源摘要: Jessie]]
- PLP 推荐模式：Gem Grab, Hot Zone

## 角色定位总结

Jessie 的 BP 价值来自“站位惩罚 + 炮台据点”。9 格主攻在命中后会向 6.67 格内最近目标弹射，最多打 3 人，能够惩罚抱团、墙后和草内目标；Scrappy 炮台可以越墙部署、挡弹、占线并配合 `Spark Plug` 在 4.33 格半径减速。她的弱点是本体 3300 HP、投射物偏慢、炮台怕高效清宠/投掷/穿透和强突进；如果敌方会分散站位并快速清炮台，Jessie 的控制会迅速变成低伤害消耗。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-10"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "long; 主攻 9 格，弹射额外追 6.67 格最近目标"
    projectile_reliability: "medium; 原弹偏慢，命中后弹射可追墙后/草内/超射程目标"
    burst: "medium_with_spark_plug_or_recoil; 本体爆发一般，减速或 Recoil Spring 后炮台可确认伤害"
    sustained_dps: "medium_high_when_turret_survives; 本体 1.8 秒装填，炮台 0.3 秒攻击"
    objective_damage: "conditional_high_on_stationary_targets; Recoil Spring 适合 Heist safe/炮台/不会躲的目标"
    mobility: "low; 无位移"
    survivability: "low_to_medium; 3300 HP，靠炮台挡弹和站位保护"
    engage: "low; 依赖对手进 chokepoint 或被 Spark Plug slow"
    disengage: "medium_with_turret_slow; Spark Plug 和炮台可拖追击"
    anti_aggro: "medium_high_if_turret_ready; 炮台挡路 + Spark Plug slow 能防重装/刺客"
    anti_tank: "conditional; grouped tanks 被弹射/slow 惩罚，单高血量可清炮台时较弱"
    wall_break: "none"
    throw_or_wall_bypass: "medium_spawnable; 炮台可越墙投放，主攻弹射可打墙后最近目标"
    area_control: "high_when_scrappy_lives; 炮台占线、减速圈和弹射惩罚 chokepoint"
    scouting_or_vision: "medium_high; 主攻弹射可暴露草内/隐形目标位置，但炮台不主动打隐藏敌人"
    team_support: "medium; 炮台挡弹、slow、占线和制造集火窗口"
    spawnable_or_pet: "high; Scrappy 3600 HP，Hyper turret +50% HP/+20% damage"
    crowd_control: "medium_high_with_spark_plug; 4.33 格半径 slow 3 秒以上"
    source_trace:
      - "[[sources/Fandom-Jessie|Fandom-Jessie]]"
      - "[[sources/PLP-Jessie|PLP-Jessie]]"

  build_switches:
    - build: "Spark Plug / Energize / Shield, Damage"
      source: "[[sources/PLP-Jessie|PLP-Jessie]]"
      changes_capabilities:
        - "Spark Plug 让 Scrappy 周围 4.33 格 shockwave slow，能穿墙命中并持续 3 秒以上"
        - "Energize 让 Jessie 射炮台回复 50% 攻击伤害，同时弹射继续寻找敌人"
        - "Shield gear 增加低血本体容错，Damage gear 提升减速后的收割"
      enables:
        - "Gem Grab 矿区炮台 anchor"
        - "Hot Zone chokepoint turret"
        - "反刺客/反重装 slow"
      mitigates_failure_modes:
        - "scrappy_cleared_too_fast"
        - "slow_projectile_misses_mobile_targets"
      best_when: "地图有墙/窄口可保护炮台，敌方需要抱团或走固定路线"
      poor_when: "敌方有投掷、高穿透、强突进或能低成本秒清炮台"
      bp_use: "default_plp_control_turret_build"
    - build: "Recoil Spring / Shocky Heist variant"
      source: "[[sources/Fandom-Jessie|Fandom-Jessie]]"
      changes_capabilities:
        - "Recoil Spring 让炮台 5 秒内攻速翻倍，适合 safe、炮台、站定目标和不会躲的 spawnables"
        - "Shocky 让炮台子弹弹射，强化敌方抱团防守时的连锁伤害"
      enables:
        - "Heist safe offense/defense"
        - "清固定召唤物"
        - "抱团惩罚"
      mitigates_failure_modes:
        - "turret_damage_too_low_without_stationary_target"
      best_when: "目标固定或敌方防守必须抱团，炮台能存活完整 5 秒"
      poor_when: "敌方快速集火炮台、分散站位或用 Penny 类弹射反利用"
      bp_use: "stationary_objective_damage_variant"

  map_feature_hooks:
    - id: "gem_mid_scrappy_anchor"
      map_feature_type: "mine_choke_turret_anchor"
      uses_feature_by: "Scrappy 放在矿区侧墙/拐角，Energize 续命，Spark Plug slow 进矿者"
      route_or_position: "宝石矿两侧墙、矿区 chokepoint、己方 carrier 撤退口"
      objective_conversion: "用炮台和弹射把敌方进矿成本变高，让己方 carrier 安全收宝"
      active_when: "炮台有墙体保护，敌方缺快速清炮台或投掷角"
      fails_if: "炮台被投掷/穿透秒清，或敌方分散站位让弹射没有价值"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "map_bp_factors.gem_mine_spawnable_anchor"
    - id: "hot_zone_turret_choke_and_spark_plug"
      map_feature_type: "zone_choke_spawnable_slow"
      uses_feature_by: "炮台占据区边线，Spark Plug 让进区者 slow，主攻弹射惩罚区内抱团"
      route_or_position: "热区边墙、区口直线、敌方回区 chokepoint"
      objective_conversion: "拖慢敌方回区，迫使他们先清炮台再踩区"
      active_when: "区口可被炮台覆盖，Jessie 能在安全处 heal turret"
      fails_if: "敌方在区外清炮台，或 thrower 无视炮台位置打 Jessie"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "slot_task.zone_slow_anchor"
    - id: "heist_recoil_spring_stationary_target"
      map_feature_type: "stationary_objective_turret_damage"
      uses_feature_by: "Recoil Spring 把 Scrappy 攻速翻倍 5 秒，可打 safe 或挡自家 safe 入侵者"
      route_or_position: "敌方 safe 侧墙、己方 safe 前、固定炮台/宠物清理线"
      objective_conversion: "把一次 Super + Gadget 转成 safe race 或防守减速窗口"
      active_when: "炮台可贴近固定目标且不被立刻清掉"
      fails_if: "Penny/投掷/穿透利用炮台反打 safe，或炮台无法存活到 Gadget 全程"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
        - "[[entities/maps/Safe Zone|Safe Zone]]"
      bp_use: "candidate_eval.stationary_objective_variant"
    - id: "bounce_chain_bush_and_group_reveal"
      map_feature_type: "bounce_reveal_group_punish"
      uses_feature_by: "主攻命中后弹向最近未命中目标，可追到墙后/草内/隐形目标并揭示站位"
      route_or_position: "中心草边、球路抱团线、热区/矿区 chokepoint"
      objective_conversion: "惩罚抱团、逼散站位，并给队友提供隐藏目标方位"
      active_when: "敌方需要靠近队友/炮台/目标物移动，或草图中存在可先命中的前排"
      fails_if: "敌方严格分散站位，或 Jessie 第一发慢弹被高机动目标反复躲掉"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "map_bp_factors.grouping_punish_and_scout"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "矿区炮台 anchor"
        - "弹射惩罚抱团和草内站位"
        - "Spark Plug 保护 carrier 撤退口"
      cannot_fulfill:
        - "高机动追杀"
        - "无炮台状态下单人控矿"
      needs_teammate_support:
        - "前排/peel、投掷处理、长手补伤害"
      false_positive: "Jessie 有炮台才有强控制；没有 Super 或炮台被秒清时，她只是慢弹长手"
    - mode: "Hot Zone"
      can_fulfill:
        - "区口炮台占线"
        - "Spark Plug slow 回区者"
        - "抱团弹射惩罚"
      cannot_fulfill:
        - "自己硬顶区"
        - "处理所有墙后火力"
      needs_teammate_support:
        - "站区 body、反投掷、开阔线压制"
      false_positive: "炮台占区收益依赖存活；敌方能从安全角度清炮台时不应把 Jessie 当稳定站区"
    - mode: "Heist"
      can_fulfill:
        - "Recoil Spring safe damage"
        - "炮台挡 safe 入侵者"
        - "弹射打抱团防守"
      cannot_fulfill:
        - "持续远程 race"
        - "炮台被反利用时强行守 safe"
      needs_teammate_support:
        - "开墙/护送炮台、远程 race、防 Penny 类反弹射"
      false_positive: "PLP 默认模式不含 Heist；Heist 只作为 Fandom 机制支持的 build 变体"

  failure_modes:
    - id: "scrappy_cleared_before_value"
      active_when: "炮台放在开阔射线或投掷/穿透火力下"
      exposed_by: "[[sources/Fandom-Jessie|Fandom-Jessie]] turret placement and counterplay notes"
      mitigation: "用墙保护、靠 Energize 续命，或等敌方清宠资源交掉"
      bp_use: "spawnable_survival_gate"
    - id: "slow_projectile_into_mobile_targets"
      active_when: "敌方高机动、长距离横移或严格分散站位"
      exposed_by: "Fandom notes slow projectile speed and reduced bounce speed/range"
      mitigation: "用炮台/Spark Plug 限走位，或选择 chokepoint 地图"
      bp_use: "candidate_eval.projectile_reliability"
    - id: "turret_does_not_target_hidden_enemies"
      active_when: "敌方藏草或隐身接近炮台"
      exposed_by: "Scrappy does not fire at invisible or bush-hidden enemies"
      mitigation: "用主攻弹射/队友探草确认位置，不把炮台当完整视野工具"
      bp_use: "vision_false_positive_filter"
    - id: "enemy_uses_turret_as_liability"
      active_when: "对方 Penny 等英雄可借炮台扩大对 safe/队友伤害"
      exposed_by: "Fandom Heist warning about Penny"
      mitigation: "避开对应 matchup，或把炮台放到不会连到 safe/队友的位置"
      bp_use: "objective_positioning_risk"

  conditional_matchups:
    - target: ["Jae-Yong", "Poco", "Pam", "Lola"]
      direction: "subject_favored"
      source: "[[sources/PLP-Jessie|PLP-Jessie]]"
      mechanism: "低爆发/支援壳若无法快速清炮台，会被 Scrappy 占线、Spark Plug slow 和弹射逼散"
      active_when: "炮台有墙保护，Jessie 能 Energize，队友能利用 slow 集火"
      fails_when: "他们有高效清宠队友或治疗量超过 Jessie 队伍伤害"
      bp_use: "anti_support_anchor"
    - target: ["Nani", "Spike", "Sprout", "Glowy"]
      direction: "subject_favored"
      source: "[[sources/PLP-Jessie|PLP-Jessie]]"
      mechanism: "炮台越墙投放和弹射可迫使静态长手/墙后控制转移火力，减少他们自由压线"
      active_when: "Jessie 能把炮台放到迫使目标处理的位置，并保留 Spark Plug 确认"
      fails_when: "目标隔墙快速清炮台或地图过开阔让慢弹难以命中"
      bp_use: "spawnable_pressure_into_static_control"
    - target: ["Buzz", "Darryl", "Edgar", "Fang"]
      direction: "target_favored"
      source: "[[sources/PLP-Jessie|PLP-Jessie]]"
      mechanism: "强位移刺客能越过慢弹和炮台射线直接贴到 Jessie 本体，逼出低血量短板"
      active_when: "Jessie 没有炮台/Spark Plug，或炮台位置不能挡进场线"
      fails_when: "Spark Plug 预埋在进场点，队友 peel，或刺客先被弹射压低"
      bp_use: "requires_peel_against_dive"
    - target: ["Alli", "Gigi", "Kaze", "Kenji"]
      direction: "target_favored"
      source: "[[sources/PLP-Jessie|PLP-Jessie]]"
      mechanism: "高机动或特殊进场会绕开 Scrappy 的固定射线，快速清炮台或直取 Jessie"
      active_when: "地图有侧草/墙后绕路，Jessie 队伍缺探草和反突进"
      fails_when: "炮台在 chokepoint 内被保护，Spark Plug 命中并有队友接伤害"
      bp_use: "avoid_without_vision_and_frontline"

  slot_notes:
    slot_1: "Gem/Hot Zone 地图有稳定炮台点时可早手；否则容易被后手突进或投掷惩罚"
    slot_2_3: "适合作为矿区/热区 anchor，后续补 frontliner 和反突进"
    slot_4_5: "看到敌方低爆发支援、抱团控制或缺清宠手段时价值高"
    slot_6: "最后手可惩罚静态阵容；看到多突进/高效清宠则不要硬选"
```

## 关联页面

- [[sources/Fandom-Jessie|Fandom 来源摘要: Jessie]]
- [[sources/PLP-Jessie|PLP 来源摘要: Jessie]]
