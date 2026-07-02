# Penny

## 基本信息

- 稀有度：Super Rare
- 定位：Controller
- 类型：炮台控图 / 命中后散射 / Salty Barrel 阵地

## 来源摘要

- Fandom：[[sources/Fandom-Penny|Fandom 来源摘要: Penny]]
- PLP：[[sources/PLP-Penny|PLP 来源摘要: Penny]]
- PLP 推荐模式：Gem Grab、Heist、Hot Zone

## 角色定位总结

Penny 是靠 `Old Lobber` 炮台和 `Plunderbuss` 命中后散射来控制站位的 Controller。主攻击 8.67 格，击中目标后向后喷出 3 组金币，穿透后方目标并造成 75% 伤害；但主弹基础伤害不高且装填 2 秒慢，不能打墙触发散射。Super 放置远程炮台，越墙投射炮弹和火区，但炮弹飞行慢、落点有提示，目标可移动躲开。PLP 默认 `Salty Barrel / Master Blaster / Shield, Damage`，用桶挡非穿透弹、主动触发散射，用 Master Blaster 在炮台落地时击退近身敌人。

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
    effective_range: "long_control; 普攻 8.67 格，炮台 13.33 格超长越墙"
    projectile_reliability: "medium; 主弹直线可靠但散射需先命中目标，炮台落点可见且飞行慢"
    burst: "medium_with_barrel_or_cluster; Salty Barrel 近距离触发散射可爆发"
    sustained_dps: "low_medium; 2 秒 slow reload，炮台提供额外持续压迫"
    objective_damage: "medium_heist_variant; Salty Barrel 近 safe 和炮台火区可参与 race"
    mobility: "low; 无位移"
    survivability: "medium_with_barrel_or_cannon; 桶/炮台可挡非穿透弹，Master Blaster 击退"
    engage: "low; 主要用炮台逼位而非主动冲入"
    disengage: "medium_high_with_master_blaster; 炮台落地击退和桶 body block 反制突进"
    anti_aggro: "medium_high_if_barrel_or_super_ready; Master Blaster / Barrel 惩罚 dash 或 jump 进场"
    anti_tank: "medium; 桶触发散射和炮台火区能压坦克，但缺硬控持续锁"
    wall_break: "none"
    throw_or_wall_bypass: "high_with_cannon; 炮台越墙抛射，Penny 本体不能隔墙"
    area_control: "very_high_if_cannon_safe; 炮台远程炮弹和 3.9 秒火区迫使移动"
    scouting_or_vision: "medium_with_trusty_spyglass_variant; 默认不显形，Spyglass 需可见敌人"
    team_support: "medium; barrel/cannon 可挡线和制造空间"
    spawnable_or_pet: "cannon_and_barrel; 炮台与 Salty Barrel 都是可被清除的固定物"
    crowd_control: "knockback_with_master_blaster; 炮台落地击退附近敌人"
    source_trace:
      - "[[sources/Fandom-Penny|Fandom-Penny]]"
      - "[[sources/PLP-Penny|PLP-Penny]]"

  build_switches:
    - build: "Salty Barrel / Master Blaster / Shield, Damage"
      source: "[[sources/PLP-Penny|PLP-Penny]]"
      changes_capabilities:
        - "Salty Barrel 放置 35% Penny 最大生命的桶，挡非穿透弹并可触发 Penny 自身散射"
        - "Master Blaster 让炮台落地时击退并伤害附近敌人，成为反突进按钮"
        - "Shield/Damage gear 补低血量和关键散射伤害窗口"
      enables:
        - "Heist 近 safe 桶爆发"
        - "Gem Grab / Hot Zone 炮台控区"
        - "反 dash / jump 进场"
      mitigates_failure_modes:
        - "slow_reload_single_target"
        - "aggro_reaches_penny_before_cannon_value"
      best_when: "敌方会聚堆、从固定路线进目标，且炮台可藏在墙后"
      poor_when: "敌方有穿透、弹射、投掷或远程 splash 低成本清桶/炮台"
      bp_use: "default_plp_barrel_control_build"
    - build: "Trusty Spyglass / Heavy Coffers variant"
      source: "[[sources/Fandom-Penny|Fandom-Penny]]"
      changes_capabilities:
        - "Trusty Spyglass 让炮台向范围内每个可见敌人连续发炮，最多 17 个目标"
        - "Heavy Coffers 扩大散射角度并增加 2 组金币，强化聚堆惩罚"
      enables:
        - "可见多目标区域压制"
        - "对 summon / body block 的更宽惩罚"
      mitigates_failure_modes:
        - "cluster_target_not_punished_enough"
        - "cannon_idle_without_target_pressure"
      best_when: "地图有视野支持且敌方需要聚集站点"
      poor_when: "敌方分散、炮台难存活，或 Penny 更需要 Master Blaster 自保"
      bp_use: "vision_or_cluster_punish_variant"

  map_feature_hooks:
    - id: "gem_cannon_fire_mine_denial"
      map_feature_type: "mine_area_artillery_control"
      uses_feature_by: "炮台藏墙后越墙炮击矿区，火区逼敌移动"
      route_or_position: "宝石矿后墙、己方半区安全炮台位、carrier 退线"
      objective_conversion: "让敌方不能稳定站矿，保护 carrier 退线并消耗进入者"
      active_when: "炮台位能覆盖矿区且敌方缺快速越墙清炮台"
      fails_if: "炮弹落点太慢被躲，或投掷/穿透直接拆炮台"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.mine_artillery_control"
    - id: "hot_zone_lobber_fire_and_barrel_choke"
      map_feature_type: "zone_fire_and_body_block"
      uses_feature_by: "炮台火区限制站区，Salty Barrel 可挡入口弹线并触发散射"
      route_or_position: "单热区边墙、区口窄线、敌方回区路径"
      objective_conversion: "把回区路线变成火区和散射惩罚，买区时"
      active_when: "敌方必须从同一入口进区，Penny 能保护炮台/桶"
      fails_if: "敌方从区外投掷清炮台，或机动绕过桶后直接贴 Penny"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.zone_artillery_and_barrel_choke"
    - id: "heist_salty_barrel_safe_burst"
      map_feature_type: "safe_barrel_splash_angle"
      uses_feature_by: "Salty Barrel 可在 safe 附近触发散射，炮台火区对固定 safe 有持续收益"
      route_or_position: "safe 侧墙、safe 前桶位、lane win 后的贴 safe 角度"
      objective_conversion: "将桶散射和炮台火区转成 safe 伤害，或迫使敌方防守回头清炮台"
      active_when: "Penny 能靠近 safe 放桶且不会被立即爆发，炮台能存活"
      fails_if: "敌方远程 race 更快，或桶被穿透/splash 变成低价值目标"
      example_maps:
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
      bp_use: "candidate_eval.heist_barrel_burst"
    - id: "spawnable_or_body_cluster_splash_punish"
      map_feature_type: "cluster_and_body_block_punish"
      uses_feature_by: "主弹命中前排/summon 后散射穿透后方，惩罚 Mr. P porter、Bruce、rat、shadow clone 等 body"
      route_or_position: "中路窄口、球路 body block、站区入口或炮台/bear 周围"
      objective_conversion: "把敌方 body block 变成后排伤害和站位税"
      active_when: "敌方目标排成前后线或用 summon 挡路"
      fails_if: "敌方分散、主弹打不到第一目标，或穿透/弹射反过来清 Penny 资源"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
      bp_use: "candidate_eval.cluster_splash_response"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "炮台覆盖矿区和退线"
        - "散射惩罚聚堆/召唤物挡线"
        - "Master Blaster 防突进"
      cannot_fulfill:
        - "安全主 carrier"
        - "稳定远距单点击杀"
      needs_teammate_support:
        - "炮台保护、视野、快速收割被逼位目标"
      false_positive: "炮台控图强，但炮弹可被躲；不能把炮台存在等同于必定控矿"
    - mode: "Hot Zone"
      can_fulfill:
        - "火区和炮台逼退站区者"
        - "桶挡线/触发散射"
        - "落地击退反突进"
      cannot_fulfill:
        - "单人硬站区"
        - "对抗完整 thrower pocket"
      needs_teammate_support:
        - "站区 body、投掷处理、炮台位保护"
      false_positive: "如果敌方能从区外清炮台，Penny 的慢 reload 会暴露"
    - mode: "Heist"
      can_fulfill:
        - "Salty Barrel safe burst"
        - "炮台火区固定目标伤害"
        - "防守时 Master Blaster / barrel 挡突进"
      cannot_fulfill:
        - "全程最高 safe DPS"
        - "无 lane win 直接进 safe"
      needs_teammate_support:
        - "lane pressure、炮台保护、race DPS"
      false_positive: "Heist 价值取决于桶位和炮台存活，不是无条件打库强度"

  failure_modes:
    - id: "slow_reload_and_single_target_low_pressure"
      active_when: "Penny 打没有前后站位的单个移动目标"
      exposed_by: "[[sources/Fandom-Penny|Fandom-Penny]] slow reload and low pouch damage"
      mitigation: "利用桶、summon、墙角或敌方 body 触发散射，不把她当纯长手 DPS"
      bp_use: "single_target_damage_gate"
    - id: "cannon_shots_are_dodgeable"
      active_when: "BP 只依赖炮台命中开阔地移动目标"
      exposed_by: "Fandom notes cannonball landing is highlighted and slow"
      mitigation: "把炮台用于逼走位/封路，配队友射线惩罚移动，而不是单独指望命中"
      bp_use: "area_control_not_raw_damage_check"
    - id: "barrel_and_cannon_liability"
      active_when: "敌方有穿透、弹射、thrower、splash 或 Penny mirror"
      exposed_by: "Fandom notes barrel/cannon/body interactions and mirror weakness"
      mitigation: "避免资源与 Penny 重叠，换炮台位，或先 ban/处理低成本清除者"
      bp_use: "spawnable_liability_filter"
    - id: "master_blaster_timing_window"
      active_when: "Penny 无 Super 或炮台落点离突进者太远"
      exposed_by: "Master Blaster only triggers near cannon landing"
      mitigation: "保留 Super 给真实突进终点，或用 barrel 先挡第一轮"
      bp_use: "anti_aggro_resource_check"

  conditional_matchups:
    - target: ["Spike", "Lola", "Gene", "Bea"]
      direction: "subject_favored"
      source: "[[sources/PLP-Penny|PLP-Penny]]"
      mechanism: "炮台和散射迫使低/中血量长手离开固定线，Salty Barrel 可挡非穿透单线弹"
      active_when: "Penny 有安全炮台位或桶位，目标需要站线而非快速清资源"
      fails_when: "目标从开阔长线先清桶/炮台，或 Lola Ego/Spike splash 让资源变负担"
      bp_use: "control_response_into_static_range"
    - target: ["Surge", "Crow", "Eve", "Charlie"]
      direction: "subject_favored"
      source: "[[sources/PLP-Penny|PLP-Penny]]"
      mechanism: "散射、炮台火区和 Master Blaster 可惩罚聚线、脆皮 poke 或单点控制站位"
      active_when: "目标必须围绕矿区/站区/球路移动，且 Penny 资源存活"
      fails_when: "他们分散、用跳跃/飞行/控制绕开火区，或先拆炮台"
      bp_use: "objective_area_pressure_candidate"
    - target: ["Carl", "Barley", "Belle", "Mr. P"]
      direction: "target_favored"
      source: "[[sources/PLP-Penny|PLP-Penny]]"
      mechanism: "回旋镐、投掷、长线爆发或 porter 资源能清桶/炮台并压 Penny 慢 reload"
      active_when: "地图墙体保护他们的角度，Penny 无法安全打到第一目标触发散射"
      fails_when: "墙体打开或 Penny 炮台藏位逼他们移动到队友射线"
      bp_use: "must_answer_resource_clear_before_penny"
    - target: ["Squeak", "Sandy", "Ollie", "Poco"]
      direction: "target_favored"
      source: "[[sources/PLP-Penny|PLP-Penny]]"
      mechanism: "黏弹/隐蔽/坦克控制/治疗 sustain 能绕开或吃掉 Penny 的炮台节奏"
      active_when: "他们能用区域或 sustain 让 Penny 的低单体输出无法转击杀"
      fails_when: "Penny 的桶散射和队友集火先清核心资源或控制住入口"
      bp_use: "requires_sustain_or_area_answer"

  slot_notes:
    slot_1: "有明确炮台藏位、敌方缺资源清除时可早手；否则会被后手投掷/弹射克制"
    slot_2_3: "适合作为 Gem/Hot Zone 控图区核心，后续补站区 body 和长线收割"
    slot_4_5: "看到敌方召唤物/body block/聚堆站点时可响应，但要检查反炮台工具"
    slot_6: "最后手可惩罚无穿透/投掷的阵容，或用桶安全打 Heist 角度"
```

## 关联页面

- [[sources/Fandom-Penny|Fandom 来源摘要: Penny]]
- [[sources/PLP-Penny|PLP 来源摘要: Penny]]
