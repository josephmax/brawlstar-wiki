# Mortis

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：位移收割 / 低血后排惩罚

## 来源摘要

- Fandom：[[sources/Fandom-Mortis|Fandom 来源摘要: Mortis]]
- PLP：[[sources/PLP-Mortis|PLP 来源摘要: Mortis]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Hot Zone

## 角色定位总结

Mortis 是典型资源型刺客：攻击即位移，Coiled Snake 缩短长 dash 充能，Combo Spinner 补无 ammo 时的收割，Life Blood 用穿墙长线蝙蝠回复并延长作战。BP 中他只在“路线、目标、ammo、撤退/回血”都成立时强；无脑进场会因为 2.4 秒极慢装填和近身反打直接崩盘。

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
    effective_range: "short_dash; 2.67 格基础 dash，长 dash 4.67 格，Super 10 格穿墙"
    projectile_reliability: "high_for_contact_low_for_open_poke; 接触后可靠，但必须把自己送进危险半径"
    burst: "medium_high_with_combo_spinner; 3 ammo + Combo Spinner + Super 可收低中血，但 Combo Spinner 是 18 秒资源，Buffie 仅对半血以下目标提高 30% 伤害"
    sustained_dps: "low; 2.4 秒极慢装填，失败进场后断 ammo"
    objective_damage: "low; Fandom 明确不适合 Heist/special target"
    mobility: "very_high; 普攻 dash、长 dash、Creature of the Night 越障/过水"
    survivability: "medium_if_super_hits; 4000 HP，Super 命中多个目标可大量回血，miss 则无回复"
    engage: "high_conditional; 需要长 dash、草墙路线或敌方低血"
    disengage: "medium; ammo/长 dash/Creature gadget 可撤，空 ammo 时很差"
    anti_aggro: "low_medium; 可 dodge 一些前摇，但怕近战爆发和控制"
    anti_tank: "low; 不适合正面打高血量前排"
    wall_break: "none"
    throw_or_wall_bypass: "high_with_super_or_creature; Super 穿墙，Creature of the Night 可短时越障/过水/免疫"
    area_control: "low"
    scouting_or_vision: "low; Fandom 明确他不擅长探未知草"
    team_support: "low"
    crowd_control: "none"

  build_switches:
    - build: "Combo Spinner / Coiled Snake / Shield, Damage"
      source: "[[sources/PLP-Mortis|PLP-Mortis]]"
      changes_capabilities:
        - "Combo Spinner 不耗 ammo 补击杀阈值；当前冷却 18 秒，Buffie 仅对半血以下目标增加 30% 伤害，不能当作每次进场都有的第四发"
        - "Coiled Snake 将长 dash 充能从 4.5 秒降到 2.5 秒"
      enables:
        - "Gem carrier 暗杀或撤退"
        - "Brawl Ball 自传/追球/守门 dash"
        - "Hot Zone/墙后控制位的最后手惩罚"
      mitigates_failure_modes:
        - "ammo_exhaustion_after_entry"
      best_when: "目标低血、缺硬控，地图给草墙/侧路路线"
      poor_when: "敌方有 Shelly/Bull/Gale/Jacky/Nita/Buster 等近身或反突进守点"
      bp_use: "default_plp_assassin_build"
    - build: "Creature of the Night / Coiled Snake or Creepy Harvest / Shield, Damage"
      source: "[[sources/Fandom-Mortis|Fandom-Mortis]]"
      changes_capabilities:
        - "短时免疫、不可选中、越墙/过水，改善进出路线"
      enables:
        - "跨水/越障抓后排或从危险草口撤离"
      mitigates_failure_modes:
        - "route_blocked_or_trap_entry"
      best_when: "地图路线门槛高，击杀阈值不完全依赖 Combo Spinner"
      poor_when: "需要额外伤害补低血目标"
      bp_use: "route_bypass_variant"

  map_feature_hooks:
    - id: "gem_carrier_dash_pick_or_escape"
      map_feature_type: "gem_carrier_chase_and_escape"
      uses_feature_by: "长 dash 接近 carrier，Super/Combo Spinner 收割后用剩余 ammo 或 Super heal 撤退"
      objective_conversion: "逼掉宝石、打断倒计时，或自己快速拾宝撤离"
      active_when: "carrier 后撤路线经过草/墙且缺近身保护"
      fails_if: "Mortis 进场后空 ammo，或目标身边有 Nita/Bull/Gale 类反切"
      example_maps: ["[[entities/maps/Gem Fort|Gem Fort]]", "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]", "[[entities/maps/Double Swoosh|Double Swoosh]]"]
      bp_use: "Gem Grab 后手刺客/翻盘窗口"
    - id: "brawl_ball_self_pass_and_goal_defense"
      map_feature_type: "dash_score_and_ball_disarm"
      uses_feature_by: "踢球后 dash 追球自传，防守时反向 dash 截球"
      objective_conversion: "快速推进、突然得分或阻止敌方进球"
      active_when: "队友牵制防守者，或球门路线已经打开"
      fails_if: "目标缺破门，Mortis 用完 ammo 后被守门控制击杀"
      example_maps: ["[[entities/maps/Center Stage|Center Stage]]", "[[entities/maps/Sneaky Fields|Sneaky Fields]]", "[[entities/maps/Triple Dribble|Triple Dribble]]"]
      bp_use: "Brawl Ball scorer/defensive dash utility"
    - id: "wall_pocket_thrower_assassination"
      map_feature_type: "route_based_assassin_into_thrower_pocket"
      uses_feature_by: "长 dash、Super 穿墙和 Creature variant 可跨越墙口抓投掷/控制位"
      objective_conversion: "清掉墙后控制后，队伍可进矿、进圈或保星"
      active_when: "投掷位缺 bodyguard，Mortis 有长 dash/Creature 或草墙路线"
      fails_if: "投掷口袋被近战反打保护，或 Mortis 被窄口预判控制"
      example_maps: ["[[entities/maps/Belle's Rock|Belle's Rock]]", "[[entities/maps/Layer Cake|Layer Cake]]", "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]", "[[entities/maps/New Horizons|New Horizons]]"]
      bp_use: "last_pick answer to fragile wall control"
    - id: "hot_zone_backline_clear_not_zone_body"
      map_feature_type: "anti_area_denial_dive_window"
      uses_feature_by: "从侧路切掉圈旁投掷/支援，帮助真正站圈队友进入"
      objective_conversion: "打破区域锁，而不是自己长期站圈"
      active_when: "敌方 zone 控制位孤立且我方已有 zone body"
      fails_if: "Mortis 被迫自己站圈，或敌方前排/召唤物守住控制位"
      example_maps: ["[[entities/maps/Open Business|Open Business]]", "[[entities/maps/Ring of Fire|Ring of Fire]]", "[[entities/maps/Dueling Beetles|Dueling Beetles]]"]
      bp_use: "Hot Zone 反控制后手，不是主站圈"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "暗杀 carrier、快速拾宝或用 dash 逃离矿区"
      cannot_fulfill:
        - "无支援长期正面控矿"
      needs_teammate_support:
        - "中路控线、补伤和反近战保护"
      false_positive: "Mortis 能摸 carrier，但队友会短时 2v3，需要明确跟进"
    - mode: "Brawl Ball"
      can_fulfill:
        - "自传得分、快速回防、切守门低血"
      cannot_fulfill:
        - "独自破门或正面抗线"
      needs_teammate_support:
        - "破墙、控人、吸引火力"
      false_positive: "dash scorer 若无球门窗口，会在门前空 ammo"
    - mode: "Hot Zone"
      can_fulfill:
        - "切掉圈外投掷/低血支援，帮助队友进圈"
      cannot_fulfill:
        - "作为唯一 zone body"
      needs_teammate_support:
        - "站圈前排、区域控制或治疗"
      false_positive: "刺客清人后没人站圈，Hot Zone 仍然不计分"
    - mode: "Bounty/Knockout"
      can_fulfill:
        - "最后手惩罚低血后排和投掷"
      cannot_fulfill:
        - "早手进开阔长线送击杀"
      needs_teammate_support:
        - "视野、路线或 enemy peel 已暴露"
      false_positive: "失败进场在单命模式/星数模式惩罚极大"

  failure_modes:
    - id: "ammo_exhaustion_after_entry"
      active_when: "Mortis 用三 dash 进场但未击杀"
      exposed_by: "2.4 秒极慢 reload"
      mitigation: "保留一段撤退；若依赖 Combo Spinner，先确认其 18 秒冷却已转好且目标已进入可靠斩杀线"
      bp_use: "resource_gate"
    - id: "missed_super_no_heal"
      active_when: "Super 未命中 Brawler 或只打非 Brawler"
      exposed_by: "Life Blood only heals on enemy Brawler hit"
      mitigation: "瞄准多人线或低血收割线，不把 Super 当无条件续航"
      bp_use: "healing_reliability_check"
    - id: "close_body_counter_screen"
      active_when: "Shelly、Bull、Jacky、El Primo、Buster、Buzz 等守在目标身边"
      exposed_by: "PLP counteredBy and Fandom warnings about heavyweights"
      mitigation: "只后手抓孤立目标，或让队友先逼控制/击退"
      bp_use: "must_screen_before_pick"
    - id: "poor_bush_check"
      active_when: "Mortis 需要进入未知草丛"
      exposed_by: "Fandom notes he cannot check bushes well"
      mitigation: "队友先探草，或预瞄反向 dash 逃跑"
      bp_use: "avoid_blind_grass_entry"

  conditional_matchups:
    - target: ["Dynamike", "Barley", "Sprout", "Grom", "Tick", "Willow"]
      direction: "subject_favored"
      source: "[[sources/PLP-Mortis|PLP-Mortis]]"
      mechanism: "dash 和穿墙 Super 可快速接触墙后低血投掷，Combo Spinner 补伤避免空 ammo"
      active_when: "目标缺近战保护，Mortis 有长 dash 或路线"
      fails_when: "口袋被 bodyguard/控制守住，或墙口被预判"
      bp_use: "last_pick_wall_control_punish"
    - target: ["Emz", "Mr. P"]
      direction: "subject_favored"
      source: "[[sources/PLP-Mortis|PLP-Mortis]]"
      mechanism: "Mortis 可绕过中距离持续压制，直接打低血本体并用 Super/Creepy Harvest 续航"
      active_when: "Porter/范围压力未堆满，目标孤立"
      fails_when: "召唤物、队友或区域控制耗掉 Mortis ammo"
      bp_use: "punish_low_mobility_control"
    - target: ["Shelly", "Bull", "Jacky", "El Primo", "Buster", "Buzz"]
      direction: "target_favored"
      source: "[[sources/PLP-Mortis|PLP-Mortis]]"
      mechanism: "近身爆发、击退/钩人、屏障或高身体可赢 Mortis 必须创造的贴身接触"
      active_when: "他们守住 carrier、goal、zone 或投掷身边"
      fails_when: "被拉开、技能交掉，或 Mortis 只切另一侧低血后排"
      bp_use: "avoid_as_primary_engage_into_close_body"
    - target: ["Gale", "Nita"]
      direction: "target_favored"
      source: "[[sources/PLP-Mortis|PLP-Mortis]]"
      mechanism: "击退/减速或 Bruce body-block 会切断 dash 路线并消耗 Mortis 稀缺 ammo"
      active_when: "Gale/Nita 有资源守目标或草口"
      fails_when: "资源被先骗掉，或 Mortis 从侧路抓孤立目标"
      bp_use: "requires_resource_bait_or_team_clear"

  slot_notes:
    slot_1: "不早手；需要看敌方后排和反刺客资源"
    slot_2_3: "除非地图和队伍明确围绕 Gem/Ball 刺客节奏，否则风险高"
    slot_4_5: "看到投掷/低血后排且反切不足时可锁"
    slot_6: "最佳最后手惩罚位；必须确认目标、路线、ammo 和撤退"
```

## 关联页面

- [[sources/Fandom-Mortis|Fandom 来源摘要: Mortis]]
- [[sources/PLP-Mortis|PLP 来源摘要: Mortis]]
