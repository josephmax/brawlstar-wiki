# Willow

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：投掷毒伤 / Hex 心控 / 目标位移控制

## 来源摘要

- Fandom：[[sources/Fandom-Willow|Fandom 来源摘要: Willow]]
- PLP：[[sources/PLP-Willow|PLP 来源摘要: Willow]]
- PLP 推荐模式：Gem Grab、Brawl Ball、Hot Zone

## 角色定位总结

Willow 是远程投掷控制英雄，普攻 `Lantern's Curse` 以 7.33 格弧线投掷，在 2 格范围内造成 3 跳毒伤；伤害可叠，但弹道/装填偏慢。Super `Hex` 是单发 tadpole，命中敌方 Brawler 后让 Willow 控制该目标 4 秒，同时 Willow 获得 50% 减伤；被控目标会先回满血，Willow 可移动并使用其普通攻击，但不能用其 Super/Gadget。控制会在 4 秒结束、目标低于 30% 最大生命、Willow 阵亡或被另一 Willow 覆盖时解除。PLP 默认 `Dive / Obsession / Shield, Damage`，强调安全心控和机动目标位移，而不是纯投掷输出。

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
    effective_range: "long_thrower; 普攻 7.33 格投掷，Super 8.33 格单发"
    projectile_reliability: "medium_low; 普攻/Hex 都可被移动躲避，弹道偏慢"
    burst: "medium_with_spellbound; 默认是 DoT，Spellbound 可把三跳毒伤一次结算并额外加伤"
    sustained_dps: "low_medium; 2 秒 slow reload，靠毒伤和控位"
    objective_damage: "low; 主要控人/控区，不是 Heist race"
    mobility: "low; Dive 是无敌停滞，不是位移"
    survivability: "low_without_dive; 3300 HP，Hex 控人时自己仍会被第三方威胁"
    engage: "medium_with_hex; 命中 Hex 后可把目标拉近/赶走/移出目标点"
    disengage: "high_with_dive_or_hex; Dive 2 秒无敌，Hex 可让追击者走开"
    anti_aggro: "medium_high_if_hex_hits; 心控能打断突进路线，但 miss 后很脆"
    anti_tank: "medium; 可把坦克移出目标点，伤害本身不稳定"
    wall_break: "none"
    throw_or_wall_bypass: "high; 普攻投掷越墙，Hex 本身不能穿墙"
    area_control: "high; 毒 puddle 与心控位移让目标点不安全"
    scouting_or_vision: "high_poison_reveal; 毒伤持续揭示草中目标"
    team_support: "high_control; Hex 为队友制造击杀、掉宝/掉球/离区窗口"
    spawnable_or_pet: "none; Hex 命中 spawnable 时改为造成 1500 伤害"
    crowd_control: "very_high_single_target_mind_control; 4 秒控制或 30% HP 解除"
    source_trace:
      - "[[sources/Fandom-Willow|Fandom-Willow]]"
      - "[[sources/PLP-Willow|PLP-Willow]]"

  build_switches:
    - build: "Dive / Obsession / Shield, Damage"
      source: "[[sources/PLP-Willow|PLP-Willow]]"
      changes_capabilities:
        - "Dive 让 Willow 2 秒无法行动但免疫直接伤害，DoT/debuff 仍可作用"
        - "Obsession 让 Hex 目标获得 +240 flat speed，实际持续 3 秒"
        - "Shield/Damage gear 缓解 3300 HP 和 DoT 输出不足"
      enables:
        - "Hex 后快速拖走 carrier/scorer/body"
        - "危险窗口保命"
        - "Gem/Brawl Ball/Hot Zone 关键目标位移"
      mitigates_failure_modes:
        - "willow_vulnerable_during_hex"
        - "low_health_pressure"
      best_when: "地图有墙后投掷位，目标必须带宝/持球/站区，且队友能保护 Willow 本体"
      poor_when: "敌方高机动刺客可绕墙贴 Willow，或 Hex 命中后满血目标无法被队友压到 30%"
      bp_use: "default_plp_hex_control_build"
    - build: "Spellbound / Love Is Blind variant"
      source: "[[sources/Fandom-Willow|Fandom-Willow]]"
      changes_capabilities:
        - "Spellbound 下一发把毒伤一次性结算并额外加伤，用于 burst/补刀"
        - "Love Is Blind 让中毒敌人 reload 速度降低 30% 持续 3 秒"
      enables:
        - "对低血脆皮补刀"
        - "削弱站区/突进者输出节奏"
      mitigates_failure_modes:
        - "dot_takes_too_long"
        - "enemy_outdamages_before_hex"
      best_when: "队伍更需要稳定毒伤节奏而不是 Dive 保命"
      poor_when: "敌方突进强，Willow 没有 Dive 会先被逼退"
      bp_use: "damage_or_reload_debuff_variant"

  map_feature_hooks:
    - id: "gem_hex_carrier_pull_or_drop"
      map_feature_type: "carrier_mind_control_displacement"
      uses_feature_by: "Hex 命中 carrier 后可控制其移动，逼近己方或离开安全退线"
      route_or_position: "宝石矿侧墙、carrier 倒计时退线、己方半区 ambush pocket"
      objective_conversion: "让 carrier 走出保护、被队友打到 30% 脱控掉宝，或延迟倒计时"
      active_when: "Willow 有安全墙后角度，队友能立刻压被控目标"
      fails_if: "Hex miss、Willow 本体暴露，或满血 carrier 被放回安全位置"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.carrier_mind_control_pick"
    - id: "brawl_ball_hex_carrier_or_goalkeeper_displacement"
      map_feature_type: "ball_carrier_mind_control"
      uses_feature_by: "Hex 可移动持球者或守门人，制造掉球/离门/错误站位窗口"
      route_or_position: "中场球权、门前守门位、侧墙持球推进线"
      objective_conversion: "让持球者离开射门路线、拖走守门人，或把目标带到队友火力"
      active_when: "Willow 能从墙后命中关键球员且队友准备接球/射门"
      fails_if: "自进球限制或控制解除让目标回位，Willow 无法保护自己"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
      bp_use: "slot_task.ball_carrier_or_goalkeeper_control"
    - id: "hot_zone_thrower_poison_and_hex_exit"
      map_feature_type: "zone_thrower_poison_and_body_displace"
      uses_feature_by: "普攻越墙毒区压站位，Hex 可把 zone body 拖出区外"
      route_or_position: "Hot Zone 墙后投掷位、区口、敌方主站区 body"
      objective_conversion: "削站区血量、降低 reload 变体输出、或用 Hex 让敌方离区"
      active_when: "墙体保护 Willow，队友能站区或击杀被拖出的目标"
      fails_if: "敌方 thrower/dive 直接处理 Willow，或毒伤无法赶走 sustain shell"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.zone_poison_and_mind_control_exit"
    - id: "knockout_hex_into_poison_or_teammate_burst"
      map_feature_type: "round_pick_mind_control"
      uses_feature_by: "Hex 可把脆皮带向队友 burst、毒云或危险角度"
      route_or_position: "Knockout 墙边、末圈毒云边、低血目标撤退线"
      objective_conversion: "制造 first pick、逼目标脱离掩体或让队友一轮打到 30% 解除并击杀"
      active_when: "Willow 不在开阔地控人，队友能在 4 秒内输出"
      fails_if: "被控目标满血过高、队友打不到，或 Willow 本体被第三方击杀"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "candidate_eval.knockout_hex_pick"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "Hex carrier 位移/掉宝窗口"
        - "墙后毒伤控矿"
        - "草区持续 reveal"
      cannot_fulfill:
        - "安全主 carrier"
        - "正面对抗刺客"
      needs_teammate_support:
        - "队友压被控目标、保护 Willow 本体、拾宝"
      false_positive: "Hex 会先把敌人回满；没有队友输出时可能只是帮敌方重置血量"
    - mode: "Brawl Ball"
      can_fulfill:
        - "移动持球者/守门人"
        - "墙后毒区封路"
      cannot_fulfill:
        - "稳定自进球套路"
        - "主 scorer"
      needs_teammate_support:
        - "接球/射门、破墙、保护 Willow"
      false_positive: "心控能改站位，但不能无条件让敌方自进球；要明确接球或射门者"
    - mode: "Hot Zone"
      can_fulfill:
        - "墙后 poison 控区"
        - "Hex 把 body 拖出区"
        - "Dive 保命拖时间"
      cannot_fulfill:
        - "单人长期站区"
        - "快速击杀高 sustain 前排"
      needs_teammate_support:
        - "站区者、burst、反刺客"
      false_positive: "毒伤慢且 reload 慢，必须和队友站区/伤害结合"

  failure_modes:
    - id: "willow_vulnerable_during_hex"
      active_when: "Willow 在开阔地控人，自己无法移动/攻击另一个威胁"
      exposed_by: "[[sources/Fandom-Willow|Fandom-Willow]] Super tips"
      mitigation: "从墙后或队友保护下 Hex，避免在敌方第三人射线内控人"
      bp_use: "super_positioning_gate"
    - id: "hex_full_heal_backfire"
      active_when: "Hex 命中高价值目标但队伍无法在 4 秒内压到 30% 或利用位移"
      exposed_by: "Hex heals enemy Brawler to full health and breaks below 30% or after 4 seconds"
      mitigation: "只 Hex carrier/scorer/body 位移目标，或确认队友 burst 准备好"
      bp_use: "objective_conversion_check"
    - id: "dive_immobile_and_dot_vulnerable"
      active_when: "Willow 用 Dive 规避伤害但位置被包围，或身上已有 DoT/debuff"
      exposed_by: "Dive is immobile and impervious except damage/debuffs over time"
      mitigation: "把 Dive 当延迟/吃单次爆发，不当位移或净化"
      bp_use: "survival_false_positive_filter"
    - id: "slow_thrower_reload_under_dive_pressure"
      active_when: "Mortis、Mico、Melodie、Stu、Lily、Moe、Gray、Sam 等从侧翼压 Willow"
      exposed_by: "[[sources/PLP-Willow|PLP-Willow]] target_favored signals and 3300 HP"
      mitigation: "补视野/peel，选墙后投掷角，避免无防守侧路"
      bp_use: "draft_requires_peel"

  conditional_matchups:
    - target: ["Spike", "Amber", "Maisie", "Gale"]
      direction: "subject_favored"
      source: "[[sources/PLP-Willow|PLP-Willow]]"
      mechanism: "Willow 可从墙后投毒并用 Hex 迫使中距控制/范围位离开目标点或走向队友"
      active_when: "墙体保护 Willow，目标需要站在固定区域或守 carrier/scorer"
      fails_when: "目标从开阔长线打 Willow 或队友无法利用 Hex 位移"
      bp_use: "control_response_into_midrange_area"
    - target: ["Penny", "Otis", "Jessie", "Eve"]
      direction: "subject_favored"
      source: "[[sources/PLP-Willow|PLP-Willow]]"
      mechanism: "投掷毒伤和 Hex 可绕开炮台/召唤物节奏，命中 spawnable 时也有固定伤害"
      active_when: "Willow 可安全攻击资源位或直接 Hex 关键本体"
      fails_when: "资源被保护在 Willow 射程外或对方刺客先处理 Willow"
      bp_use: "wall_control_and_spawnable_response"
    - target: ["Mortis", "Mico", "Melodie", "Stu"]
      direction: "target_favored"
      source: "[[sources/PLP-Willow|PLP-Willow]]"
      mechanism: "高机动刺客能绕过投掷弧线，在 Willow 慢 reload/低血时逼出 Dive 或击杀"
      active_when: "地图有侧路、墙跳或 dash 入口，Willow 缺硬 peel"
      fails_when: "Willow 预判 Hex 命中且队友可立刻集火"
      bp_use: "avoid_without_peel_and_hex_angle"
    - target: ["Lily", "Moe", "Gray", "Sam"]
      direction: "target_favored"
      source: "[[sources/PLP-Willow|PLP-Willow]]"
      mechanism: "隐身/地下/传送/速度 body 压迫会打断 Willow 的墙后投掷和 Hex 站位"
      active_when: "他们能选择第一接触或保护被 Hex 目标"
      fails_when: "地图路线被队友封住，Willow 从安全角度只控制实际 carrier/scorer"
      bp_use: "requires_route_lock_and_bodyguard_answer"

  slot_notes:
    slot_1: "有明确墙后投掷位和可被 Hex 转化的目标时可早手；否则低血会被后手刺客惩罚"
    slot_2_3: "作为控制层时必须补保护 Willow 本体的队友"
    slot_4_5: "看到敌方依赖 carrier/scorer/站区 body 时，Hex 响应价值高"
    slot_6: "最后手可针对无机动保护的核心目标，但不能补主站区或主输出"
```

## 关联页面

- [[sources/Fandom-Willow|Fandom 来源摘要: Willow]]
- [[sources/PLP-Willow|PLP 来源摘要: Willow]]
