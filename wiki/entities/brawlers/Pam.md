# Pam

## 基本信息

- 稀有度：Epic
- 定位：Support
- 类型：治疗炮台 / 弹药剥夺 / 阵地续航

## 来源摘要

- Fandom：[[sources/Fandom-Pam|Fandom 来源摘要: Pam]]
- PLP：[[sources/PLP-Pam|PLP 来源摘要: Pam]]
- PLP 推荐模式：Gem Grab、Hot Zone

## 角色定位总结

Pam 是用 `Mama's Kiss` 治疗炮台和宽散射压制来拉长团战的支援英雄。她的主攻击一次射出 9 枚 scrap，距离长、装填快，但 1.05 秒卸弹和 30 度散射让远距离单点命中不稳定；近距离打满才有高伤。PLP 默认 `Scrapsucker / Mama's Hug / Damage, Super Turret` 让她在 Gem Grab 和 Hot Zone 里成为续航阵地：治疗炮台每秒治疗，`Mama's Hug` 命中回血，`Scrapsucker` 下一发每枚命中移除敌方 25% 最大弹药并返还 Pam 弹药。短板是阵地依赖炮台、贴脸会被高爆发短手击杀，炮台也会被投掷、穿透、弹射和 splash 变成负担。

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
    effective_range: "long_spread; 普攻 9 格但远距离单点不稳定"
    projectile_reliability: "medium_low_at_range; 9 枚弹片横扫且卸弹 1.05 秒，近距离或大体型更可靠"
    burst: "medium_close_range; 贴脸多弹命中才有爆发"
    sustained_dps: "medium_high_if_safe; 1.3 秒 very fast reload，但需要持续站线"
    objective_damage: "situational_heist_variant; Mama's Squeeze 可对 safe 做持续伤害，但非 PLP 默认模式"
    mobility: "low; 无位移"
    survivability: "high_with_station; 5000 HP + 炮台持续治疗 + Mama's Hug 命中回血"
    engage: "low; 主要守阵地和推进，不主动开团"
    disengage: "medium; 炮台 quick-fire 可挡伤，Scrapsucker 可剥夺突进者弹药"
    anti_aggro: "medium_high_with_resources; 弹药剥夺和治疗能拖刺客/坦克，但贴脸高爆发仍危险"
    anti_tank: "medium; 近距离弹片和 Scrapsucker 能惩罚短手弹药，但缺少硬控/百分比伤害"
    wall_break: "none"
    throw_or_wall_bypass: "heal_radius_through_walls_only; 炮台治疗半径可隔墙，Pam 普攻不能隔墙"
    area_control: "high_sustain_area; 治疗炮台定义可站区域，Mama's Squeeze 变体可反压墙边"
    scouting_or_vision: "medium_bush_sweep; 宽散射可扫草但不提供显形"
    team_support: "very_high; 炮台、Pulse Modulator、Mama's Hug 和 Super Turret 支撑队友"
    spawnable_or_pet: "healing_station; 3040 HP 炮台，3.33 格治疗半径"
    crowd_control: "ammo_denial; Scrapsucker 移除弹药而非 slow/stun/knockback"
    source_trace:
      - "[[sources/Fandom-Pam|Fandom-Pam]]"
      - "[[sources/PLP-Pam|PLP-Pam]]"

  build_switches:
    - build: "Scrapsucker / Mama's Hug / Damage, Super Turret"
      source: "[[sources/PLP-Pam|PLP-Pam]]"
      changes_capabilities:
        - "Scrapsucker 下一发每枚命中移除敌方 25% 最大弹药，并返还 Pam 一半被偷弹药"
        - "Mama's Hug 每枚命中在 4 格内治疗 Pam 和队友，适合持续团战"
        - "Super Turret gear 把炮台治疗提高 20%，强化阵地续航"
      enables:
        - "Gem Grab carrier / mid sustain"
        - "Hot Zone 站区续航和入口弹药税"
        - "反突进弹药剥夺窗口"
      mitigates_failure_modes:
        - "spread_inaccuracy_at_range"
        - "aggro_burst_before_healing_converts"
      best_when: "地图有墙后炮台位、固定目标区或 carrier 退线，且敌方没有低成本炮台清除"
      poor_when: "敌方拥有投掷/弹射/穿透/splash 能持续清炮台，或从多个角度贴脸"
      bp_use: "default_plp_sustain_and_ammo_denial_build"
    - build: "Pulse Modulator / Mama's Squeeze variant"
      source: "[[sources/Fandom-Pam|Fandom-Pam]]"
      changes_capabilities:
        - "Pulse Modulator 在炮台范围内即时治疗两跳，Pam 需在炮台 12 格内启动"
        - "Mama's Squeeze 让炮台每秒伤害范围内敌人，也能伤害 safe 和 spawnables"
      enables:
        - "紧急救人/保 carrier"
        - "Heist safe 贴炮台变体"
        - "墙后敌人受迫离开"
      mitigates_failure_modes:
        - "team_burst_before_station_heals"
        - "low_objective_damage"
      best_when: "队伍需要即时救援或 Heist/墙边阵地能保护炮台"
      poor_when: "炮台会被投掷或弹射瞬间清掉，或队伍更需要 Scrapsucker 反突进"
      bp_use: "mode_or_matchup_variant_not_default_plp"

  map_feature_hooks:
    - id: "gem_mid_healing_station_carrier_anchor"
      map_feature_type: "carrier_sustain_and_retreat_anchor"
      uses_feature_by: "炮台治疗半径可隔墙，Pam 可在矿区和退线之间持续补血"
      route_or_position: "宝石矿侧墙、carrier 倒计时退线、己方半区墙后炮台位"
      objective_conversion: "延长 carrier 存活、稳住矿区站位、让队友在倒计时中反打"
      active_when: "炮台能藏在墙后且队友围绕半径作战"
      fails_if: "投掷/弹射/穿透免费清炮台，或 carrier 离开治疗半径"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.carrier_sustain_anchor"
    - id: "hot_zone_station_and_scrapsucker_entry_tax"
      map_feature_type: "zone_sustain_and_ammo_denial"
      uses_feature_by: "治疗炮台维持站区，Scrapsucker 剥夺进区短手弹药"
      route_or_position: "单热区边墙、区口草边、敌方回区路线"
      objective_conversion: "把进区变成弹药亏损和治疗差，转成己方区时"
      active_when: "敌方必须重复进入同一区口，Pam 能站在炮台半径内命中"
      fails_if: "敌方从区外长手/投掷清区，或炮台位暴露"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.zone_sustain_and_ammo_tax"
    - id: "heist_mamas_squeeze_station_variant"
      map_feature_type: "safe_adjacent_station_damage"
      uses_feature_by: "Mama's Squeeze 炮台可对 safe 和防守者持续伤害，Pam 近距离弹片补 safe race"
      route_or_position: "safe 旁墙角、己方 safe 防守炮台位、lane win 后的 safe 贴位"
      objective_conversion: "把炮台存活时间转成 safe 伤害、防守治疗或迫使敌人回防"
      active_when: "炮台可安全贴近 safe 或防守角，敌方缺快速清炮台工具"
      fails_if: "投掷/splash/穿透立即清炮台，或远程 DPS race 更快"
      example_maps:
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
      bp_use: "candidate_eval.heist_station_variant"
    - id: "wide_spread_bush_sweep_bodyguard"
      map_feature_type: "bush_sweep_and_support_body"
      uses_feature_by: "宽散射可扫草，Pam 高血量和治疗让 carrier/长手有 bodyguard"
      route_or_position: "Gem Grab 侧草、Brawl Ball 中草、Hot Zone 草边入口"
      objective_conversion: "减少草区偷袭、保护队友站线、给 Scrapsucker 命中窗口"
      active_when: "敌方从草口进攻且 Pam 有队友跟随"
      fails_if: "敌方直接爆发秒 Pam，或草被投掷/远程控制覆盖"
      example_maps:
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.bush_sweep_support_body"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "矿区续航支点"
        - "carrier 倒计时保护"
        - "Scrapsucker 剥夺突进者弹药"
      cannot_fulfill:
        - "安全主 carrier 对抗长手 burst"
        - "单独处理投掷炮台清除"
      needs_teammate_support:
        - "长线输出、投掷处理、收割被剥弹药目标"
      false_positive: "Pam 的治疗强度需要队友留在半径内；分散三线时价值下降"
    - mode: "Hot Zone"
      can_fulfill:
        - "炮台站区续航"
        - "进区弹药税"
        - "Mama's Squeeze 变体墙边压制"
      cannot_fulfill:
        - "独自清投掷 pocket"
        - "无炮台时长期抗 burst"
      needs_teammate_support:
        - "站区 body、反投掷、远程压制"
      false_positive: "炮台一旦被低成本清掉，Pam 只是宽散射中速输出"
    - mode: "Heist"
      can_fulfill:
        - "Mama's Squeeze safe 贴炮台变体"
        - "近距离弹片 safe 伤害"
        - "防守治疗和弹药剥夺"
      cannot_fulfill:
        - "稳定远程 safe DPS race"
        - "穿墙打 safe"
      needs_teammate_support:
        - "lane win、炮台保护、race DPS"
      false_positive: "Heist 价值来自特定炮台位和 Star Power 变体，不等于默认 PLP 模式适配"

  failure_modes:
    - id: "spread_inaccuracy_at_range"
      active_when: "Pam 远距离单点打移动目标或低体型目标"
      exposed_by: "[[sources/Fandom-Pam|Fandom-Pam]] Scrapstorm wide spread and slow unload"
      mitigation: "选固定目标区/草口/近距离 body fight，或让队友先限制路线"
      bp_use: "projectile_reliability_gate"
    - id: "aggro_burst_before_healing_converts"
      active_when: "El Primo、Edgar、Darryl、Shelly、Buzz、Bull 等短手贴脸"
      exposed_by: "Fandom tips warn high burst close-range Brawlers can defeat Pam before she wins"
      mitigation: "保 Scrapsucker、站炮台半径内、配硬控/击退队友"
      bp_use: "anti_aggro_resource_check"
    - id: "station_liability_into_splash_pierce_bounce"
      active_when: "敌方有 Penny、Barley、Mr. P、Dynamike、Tick、Brock、Carl、Tara、Janet、Amber、Chuck、Nita、Jessie、Belle 等炮台惩罚"
      exposed_by: "Fandom lists splash, piercing, and bounce attacks that still damage Pam around station"
      mitigation: "换炮台位置、避免把 Pam 与炮台重叠，或改成更少依赖 station 的组合"
      bp_use: "spawnable_liability_filter"
    - id: "scrapsucker_requires_brawler_hits"
      active_when: "BP 计划把 Scrapsucker 用来打 safe、IKE、spawnable 或空弹目标"
      exposed_by: "Fandom notes Scrapsucker does not work against Heist safe or spawnables and returns no extra ammo from empty bars"
      mitigation: "只把 Scrapsucker 当作英雄弹药剥夺工具，配合固定进区路线使用"
      bp_use: "build_mechanism_sequence_check"

  conditional_matchups:
    - target: ["Jae-Yong", "Nani", "Glowy", "Piper"]
      direction: "subject_favored"
      source: "[[sources/PLP-Pam|PLP-Pam]]"
      mechanism: "Pam 的治疗炮台和 Mama's Hug 可把长线 chip 变成续航差，Scrapsucker 命中后剥夺反打弹药"
      active_when: "Pam/队友能站在炮台半径内，目标需要持续 poke 而非瞬间秒杀"
      fails_when: "目标保持完全开阔长线、集火炮台，或 Pam 弹片远距命中不足"
      bp_use: "sustain_response_into_poke_lane"
    - target: ["Sprout", "Alli", "Kaze", "Buzz"]
      direction: "subject_favored"
      source: "[[sources/PLP-Pam|PLP-Pam]]"
      mechanism: "高血量、炮台治疗和 Scrapsucker 弹药剥夺可拖低 wall/assassin 进场效率"
      active_when: "进场路线可被扫到，Pam 有炮台或队友保护，Scrapsucker 保留给真实进场"
      fails_when: "目标从盲草或墙后瞬间贴脸，炮台被先清，或 Pam 单独站线"
      bp_use: "conditional_anti_engage_support"
    - target: ["Bibi", "Rosa", "Edgar", "Bull"]
      direction: "target_favored"
      source: "[[sources/PLP-Pam|PLP-Pam]]"
      mechanism: "速度、草路、盾或瞬间近身爆发能在 Pam 慢卸弹和治疗转化前完成击杀"
      active_when: "地图有草/墙让短手选择第一接触，Pam 无硬控队友或 Scrapsucker miss"
      fails_when: "Pam 已站炮台半径内并命中 Scrapsucker，队友能惩罚短手空弹"
      bp_use: "avoid_without_peel_and_ammo_denial"
    - target: ["Nita", "Lumi", "Sandy", "Sirius"]
      direction: "target_favored"
      source: "[[sources/PLP-Pam|PLP-Pam]]"
      mechanism: "spawnable、wall control、隐蔽/区域控制或更稳定的中远压制能拆掉 Pam 的站点节奏"
      active_when: "他们能清炮台、控制草口或从 Pam 弹片外持续消耗"
      fails_when: "Pam 的队友先清 summon/控制资源，且 Pam 能用治疗站保护 carrier"
      bp_use: "must_answer_area_or_spawnable_before_pam_plan"

  slot_notes:
    slot_1: "只在地图有稳定炮台位且队伍愿意围绕 sustain 打时早手；否则容易被后手投掷/弹射惩罚"
    slot_2_3: "可作为 Gem/Hot Zone 阵地核心，后续补长手输出和炮台保护"
    slot_4_5: "看到敌方缺炮台清除或依赖 chip/进区弹药时响应价值高"
    slot_6: "最后手可惩罚低爆发 poke 或单一路线短手，但不能补硬控/开墙缺口"
```

## 关联页面

- [[sources/Fandom-Pam|Fandom 来源摘要: Pam]]
- [[sources/PLP-Pam|PLP 来源摘要: Pam]]
