# Pearl

## 基本信息

- 稀有度：Epic
- 定位：Damage Dealer
- 类型：Heat 成长输出 / 近身 Super 爆发 / 开墙击退

## 来源摘要

- Fandom：[[sources/Fandom-Pearl|Fandom 来源摘要: Pearl]]
- PLP：[[sources/PLP-Pearl|PLP 来源摘要: Pearl]]
- PLP 推荐模式：Gem Grab、Knockout

## 角色定位总结

Pearl 是依靠 Heat 条把伤害逐步抬高的长射程 Damage Dealer。Heat 9 秒充满，最高让普攻和 Super 获得 75% 伤害加成；普攻射出 6 枚散射 cookies，每枚只消耗相当于 0.38 秒蓄热，完整一轮消耗约 2.28 秒 Heat，因此满热状态可支持连续多轮开火。远距离单点仍不稳定，但高 Heat 近距离爆发很高。Super `Let Out Some Steam` 在 0.3 秒延迟后释放 3.33 格爆炸，伤害、击退并摧毁掩体，但延迟中被 stun / pull / knockback 会取消。PLP 默认 `Overcooked / Heat Shield / Shield, Damage, Health`，把 Pearl 建模为能在 Gem Grab / Knockout 持 Heat 站线、用高热爆发惩罚贴脸的中后期输出。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-17"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "long_spread; 普攻 9 格，6 枚散射 cookies"
    projectile_reliability: "medium_low_at_max_range; 宽散射打移动单体不稳定，近距离或窄路更可靠"
    burst: "high_when_heat_charged; Heat 最高 +75% 伤害，Super 近距离爆发和击退"
    sustained_dps: "medium_high_during_stored_heat_window; 1.5 秒 reload，每枚 cookie 消耗 0.38 秒蓄热、完整一轮约 2.28 秒，连续高热输出窗口更长但仍会逐弹降温"
    objective_damage: "medium; 可用高 Heat 打固定目标，但不是稳定远程 safe DPS"
    mobility: "low; 无位移"
    survivability: "medium_high_with_heat_shield; Power 11 本体 8600 HP，Heat >80% 的 20% Heat Shield 对应 10750 EHP，叠满 Shield gear 为 11875；一旦 Heat 降到 80% 或以下即失效"
    engage: "medium_short_range_super; 依赖目标进入 3.33 格 Super 半径"
    disengage: "medium_high_if_super_ready; Super 击退近身目标并可破墙"
    anti_aggro: "high_with_heat_and_super; 高 Heat、击退和 Overcooked 惩罚刺客/坦克贴脸"
    anti_tank: "medium_high_with_heat; 近距高热多弹和 Super 能压低坦克，但无持续 slow/stun"
    wall_break: "high_super; Super 3.33 格爆炸摧毁掩体"
    throw_or_wall_bypass: "none"
    area_control: "medium_with_hyper_or_overcooked; Overcooked DoT 和 Hyper Super 火区可短时控地"
    scouting_or_vision: "low"
    team_support: "low_to_medium_with_made_with_love; Made With Love 可治疗队友但非 PLP 默认"
    spawnable_or_pet: "none"
    crowd_control: "knockback_only; Super 击退，不提供 stun/slow"
    source_trace:
      - "[[sources/Fandom-Pearl|Fandom-Pearl]]"
      - "[[sources/PLP-Pearl|PLP-Pearl]]"

  build_switches:
    - build: "Overcooked / Heat Shield / Shield, Damage, Health"
      source: "[[sources/PLP-Pearl|PLP-Pearl]]"
      changes_capabilities:
        - "Overcooked 让下一发 6 枚 cookies 命中后附带 4 跳 DoT，伤害随 cookie 当前伤害变化"
        - "Heat Shield 在 Heat 超过 80% 时降低 20% 受到伤害；较低的逐弹 Heat 消耗延后降温，但完整开火仍会使护盾在弹幕过程中失效"
        - "Shield/Health gear 把 Pearl 的高 Heat 等待期变得更安全"
      enables:
        - "Knockout 持 Heat 威慑"
        - "Gem Grab 中线高热反突进"
        - "Super 击退/开墙后爆发"
      mitigates_failure_modes:
        - "heat_window_interrupted"
        - "close_range_burst_race"
      best_when: "Pearl 能安全积累 Heat，并在敌方必须接触目标区或回合末时开火"
      poor_when: "敌方长手/投掷持续消耗迫使 Pearl 频繁开火掉 Heat，或有控制取消 Super"
      bp_use: "default_plp_heat_hold_damage_build"
    - build: "Heat Retention / Made With Love variant"
      source: "[[sources/Fandom-Pearl|Fandom-Pearl]]"
      changes_capabilities:
        - "Heat Retention 让 Super 只消耗剩余 Heat 的一半，便于 Super 后继续普攻爆发"
        - "Made With Love 下一发穿过敌人治疗队友 4 跳，用于救 ally 或延长站线"
      enables:
        - "Super -> 普攻连段"
        - "队友救援/续航"
      mitigates_failure_modes:
        - "super_resets_heat_and_loses_followup"
        - "ally_dies_before_heat_window"
      best_when: "队伍需要 Pearl 提供二段爆发或临时治疗，而非默认 Heat Shield 持线"
      poor_when: "Pearl 本人会先被压低，需要 Heat Shield 才能站住"
      bp_use: "burst_chain_or_support_variant"

  map_feature_hooks:
    - id: "knockout_heat_hold_long_lane"
      map_feature_type: "round_timer_heat_threat"
      uses_feature_by: "Pearl 可在回合前段蓄 Heat，后段利用每轮约 2.28 秒 Heat 消耗连续打出高热普攻/Overcooked，威胁第一击杀"
      route_or_position: "Knockout 长线、墙边转角、回合末收缩前的中线"
      objective_conversion: "保护血量优势、逼退低血目标、或在回合末用高热爆发收割"
      active_when: "Pearl 有掩体/队友保护能等 Heat，敌方必须探头或进入固定线"
      fails_if: "投掷或超长手持续消耗 Pearl，迫使她掉 Heat 或交 Super 防守"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
      bp_use: "slot_task.round_timer_damage_threat"
    - id: "gem_heat_shield_mid_anchor"
      map_feature_type: "gem_mid_heat_anchor"
      uses_feature_by: "Heat Shield 和消耗更慢的高热普攻让 Pearl 在矿区附近有更长的反打序列和护身能力"
      route_or_position: "宝石矿中线、侧墙入口、carrier 退线"
      objective_conversion: "用高热威慑突进者、保护 carrier、或在矿区争夺中开墙"
      active_when: "矿区节奏允许 Pearl 保持 Heat，队伍有视野/前排避免被先手控制"
      fails_if: "敌方从墙后投掷或开阔长线逼 Pearl 提前开火"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
        - "[[entities/maps/Crystal Arcade|Crystal Arcade]]"
      bp_use: "candidate_eval.gem_mid_heat_anchor"
    - id: "brawl_ball_super_goal_wallbreak"
      map_feature_type: "goal_wall_break_and_knockback"
      uses_feature_by: "Super 可破门前墙并击退守门人，Fandom 明确提示可打开进球路径"
      route_or_position: "球门前墙、门口守门人、加时前的封闭球路"
      objective_conversion: "永久打开射门角度，或把守门人击退后创造射门窗口"
      active_when: "Pearl 有 Super 且队伍能立刻利用打开的门"
      fails_if: "0.3 秒延迟被控制取消，或破墙后开放长线更利于敌方"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
      bp_use: "map_bp_factors.goal_wall_transform"
    - id: "short_choke_super_knockback_zone_clear"
      map_feature_type: "short_radius_knockback_clear"
      uses_feature_by: "高 Heat Super 在短口爆发、击退并摧毁掩体"
      route_or_position: "Hot Zone 区口、Gem side choke、短手进场终点"
      objective_conversion: "清出站点、打断坦克进场、或把目标推离掩体"
      active_when: "敌方必须靠近 3.33 格内，Pearl 能承受延迟前的伤害"
      fails_if: "敌方控制打断 Super，或远程从半径外持续压制"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "candidate_eval.short_choke_burst_clear"

  objective_contracts:
    - mode: "Knockout"
      can_fulfill:
        - "回合计时内蓄 Heat 后威胁 first pick"
        - "Heat Shield 持线保护血量优势"
        - "Super 近身反突进和开墙"
      cannot_fulfill:
        - "无掩体跨全图对狙"
        - "单独清投掷 pocket"
      needs_teammate_support:
        - "视野、投掷处理、保护 Pearl 蓄 Heat 的前线"
      false_positive: "Pearl 不应在需要频繁开火试探的线位早早消耗 Heat"
    - mode: "Gem Grab"
      can_fulfill:
        - "中线高热反突进"
        - "carrier 退线保护"
        - "必要时开墙改变矿区"
      cannot_fulfill:
        - "稳定主 carrier"
        - "远距持续扫草"
      needs_teammate_support:
        - "主 carrier、草区控制、投掷/长手答案"
      false_positive: "较低 Heat 消耗延长威慑，但 Heat 掉完后短时间内仍只是普通散射长手"
    - mode: "Brawl Ball"
      can_fulfill:
        - "Super 破门前墙"
        - "击退守门人或持球坦克"
      cannot_fulfill:
        - "快速主 scorer"
        - "反复位移过人"
      needs_teammate_support:
        - "scorer、控球、破墙后长线利用"
      false_positive: "Brawl Ball 是机制变体，不是 PLP 默认适配；需要明确门墙收益"

  failure_modes:
    - id: "heat_wasted_by_unplanned_ammo"
      active_when: "Pearl 为试探或扫草频繁开火，Heat 仍按每枚 cookie 相当于 0.38 秒蓄热逐步消耗"
      exposed_by: "[[sources/Fandom-Pearl|Fandom-Pearl]] Heat bar and attack details"
      mitigation: "较低消耗允许更长连射，但不等于无限高热；仍只在有目标收益的线位开火，围绕回合/目标计时保存 Heat"
      bp_use: "resource_timing_gate"
    - id: "super_delay_cancelled"
      active_when: "Pearl 在 0.3 秒 Super 延迟中被 stun、pull 或 knockback"
      exposed_by: "Fandom Super cancellation note"
      mitigation: "等敌方控制交掉后再开 Super，或让队友先限制目标"
      bp_use: "engage_sequence_check"
    - id: "spread_unreliable_into_open_range"
      active_when: "Pearl 在最远距离试图单点命中小体型机动目标"
      exposed_by: "Fandom notes wide spread is inconsistent against one target at range"
      mitigation: "选择窄线/固定目标，或用 Overcooked 命中任一 cookie 后转 DoT"
      bp_use: "projectile_reliability_gate"
    - id: "outranged_or_controlled_before_heat_window"
      active_when: "Belle、Nani、Brock、Mandy、Eve、Amber、Lou 等从安全距离或控制位压 Pearl"
      exposed_by: "[[sources/PLP-Pearl|PLP-Pearl]] target_favored signals"
      mitigation: "补墙体/前排/投掷处理，避免 Pearl 独自承担开阔长线"
      bp_use: "map_openness_and_control_warning"

  conditional_matchups:
    - target: ["Edgar", "Mico", "Leon", "Mortis"]
      direction: "subject_favored"
      source: "[[sources/PLP-Pearl|PLP-Pearl]]"
      mechanism: "高 Heat 多弹、Heat Shield 和 Super 击退可惩罚刺客贴脸后的第一轮交火"
      active_when: "Pearl 保持高 Heat，有 Super 或 Overcooked，且刺客必须正面进入"
      fails_when: "刺客从盲角先手、Pearl Heat 低或 Super 被控制/爆发打断"
      bp_use: "anti_assassin_if_heat_ready"
    - target: ["El Primo", "Sam", "Gray", "Max"]
      direction: "subject_favored"
      source: "[[sources/PLP-Pearl|PLP-Pearl]]"
      mechanism: "高热 burst、击退和减伤让短手/位移目标难以直接换掉 Pearl"
      active_when: "路线可预测，Pearl 有空间拉扯，队友能补伤"
      fails_when: "Gray/Max 从多角度拉开或 Sam 逼掉 Super 后继续追击"
      bp_use: "conditional_body_or_mobility_answer"
    - target: ["Belle", "Nani", "Brock", "Mandy"]
      direction: "target_favored"
      source: "[[sources/PLP-Pearl|PLP-Pearl]]"
      mechanism: "更稳定的远程爆发和开阔线命中会在 Pearl 进入高 Heat 价值前压低她"
      active_when: "地图开阔，Pearl 必须探头蓄 Heat 或用散射对长线"
      fails_when: "墙体保住 Pearl 接近，或目标被迫进入 Super/高热普攻半径"
      bp_use: "avoid_open_snipe_lane"
    - target: ["Lou", "Eve", "Colette", "Amber"]
      direction: "target_favored"
      source: "[[sources/PLP-Pearl|PLP-Pearl]]"
      mechanism: "冰控/水位绕线/百分比伤害/持续区域伤害会破坏 Pearl 的蓄 Heat 和站线"
      active_when: "他们能持续压位置而不进入 Pearl 的短半径 Super"
      fails_when: "Pearl 保存高 Heat 等他们进目标区，或队伍先清控制区域"
      bp_use: "requires_control_area_answer_before_pearl"

  slot_notes:
    slot_1: "Knockout/Gem 有安全蓄 Heat 线位时可早手；开阔狙击或强投掷图不宜盲拿"
    slot_2_3: "可作为中后期伤害核心，后续补投掷处理和视野"
    slot_4_5: "看到敌方刺客/短手但缺硬控打断时，Pearl 可作为高热反突进"
    slot_6: "最后手适合惩罚无长手压制的短手阵容，或用 Super 解决明确门墙/掩体问题"
```

## 关联页面

- [[sources/Fandom-Pearl|Fandom 来源摘要: Pearl]]
- [[sources/PLP-Pearl|PLP 来源摘要: Pearl]]
- [[sources/BSC-2026-July-Observed-Map-Fit-Review|BSC 2026 July 地图适配复核]]

## 战斗断点输入

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "Pearl",
    "target_states": [
      {
        "id": "body",
        "entity_class": "brawler_body",
        "roster_target": true,
        "health": {"amount": 4300, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-Pearl|Fandom-Pearl]]"
      }
    ],
    "damage_packets": [],
    "defense_modifiers": [
      {
        "id": "heat_shield",
        "source_kind": "star_power",
        "loadout_group": "star_power",
        "applies_to_states": ["body"],
        "effect": {"type": "damage_reduction", "ratio": 0.20},
        "active_when": "Heat 高于 80%",
        "sequence_validity": "Heat 降到 80% 或以下即失效",
        "source_ref": "[[sources/Fandom-Pearl|Fandom-Pearl]]"
      }
    ]
  }
}
```
