# Janet

## 基本信息

- 稀有度：Mythic
- 定位：Marksman
- 类型：蓄力长线 / 空中逃生 / 草区扬声器压制

## 来源摘要

- Fandom：[[sources/Fandom-Janet|Fandom 来源摘要: Janet]]
- PLP：[[sources/PLP-Janet|PLP 来源摘要: Janet]]
- PLP 推荐模式：Gem Grab

## 角色定位总结

Janet 是靠可变射程和空中 6 秒免伤窗口服务目标的 Marksman。她的主攻从短宽锥形逐渐收窄到 8.33 格长线，`Vocal Warm Up` 缩短蓄力时间；`Drop The Bass` 用 8 格半径持续伤害揭草、阻断回血；Super 让她在 Gem Grab 倒计时里携宝升空脱离追击。她的问题是伤害爆发不高、Super 期间不能回血或装填，且不能占 Hot Zone；`Backstage Pass` 是重要反突进变体，但默认 PLP build 更偏草区与 Gem Grab 信息控制。

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
    effective_range: "variable_mid_to_long; 普攻从 4 格宽锥形蓄到 8.33 格窄线"
    projectile_reliability: "medium_high_with_focus_time; piercing shockwave 稳定，但需要瞄准时间"
    burst: "low_to_medium; 单发 1000，Super 炸弹低伤害且不落正下方"
    sustained_dps: "medium; 1.5 秒装填，蓄力压线胜过爆发击杀"
    objective_damage: "low; 主要服务 Gem Grab carrier 和视野，不是 Heist race"
    mobility: "high_with_super_or_backstage; Super 6 秒高速飞行，Backstage Pass 可后跳越墙/水"
    survivability: "high_during_air_low_on_ground; 地面 3400 HP，空中免疫绝大多数伤害"
    engage: "low_to_medium; 靠长线 poke 和 Super 转点，不主动贴脸开战"
    disengage: "very_high_with_super; carrying gems 时可用 Super 躲 15 秒倒计时追击"
    anti_aggro: "medium_with_backstage_or_air; Backstage Pass 可躲快卸弹，Super 可脱离接触"
    anti_tank: "low; 缺百分比和硬控，需要队友处理高血量"
    wall_break: "none"
    throw_or_wall_bypass: "high_mobility_and_bombs; Super 飞越障碍投弹，Backstage Pass 反向越墙/水"
    area_control: "medium; Drop The Bass 8 格半径持续伤害揭草和阻断回血"
    scouting_or_vision: "high_on_bush_maps; Drop The Bass 揭草，Stage View 在 Super 期间扩大草丛视野"
    team_support: "medium_high; 视野、阻断回血、倒计时携宝"
    spawnable_or_pet: "speaker; Drop The Bass 1000 HP 并最多持续 10 秒"
    crowd_control: "low; 本体无硬控，靠位移和信息控制"
    source_trace:
      - "[[sources/Fandom-Janet|Fandom-Janet]]"
      - "[[sources/PLP-Janet|PLP-Janet]]"

  build_switches:
    - build: "Drop The Bass / Vocal Warm Up / Shield, Damage, Vision"
      source: "[[sources/PLP-Janet|PLP-Janet]]"
      changes_capabilities:
        - "Drop The Bass 以 8 格半径持续伤害揭草并阻断回血，但 speaker 只有 1000 HP 且会衰减"
        - "Vocal Warm Up 让普攻聚焦快 30%，提升从宽锥到长线压制的转换速度"
        - "Vision gear 强化草图和 speaker reveal 的团队收益"
      enables:
        - "Gem Grab carrier 倒计时逃生"
        - "草区信息压制"
        - "长线安全 poke"
      mitigates_failure_modes:
        - "focus_time_exposes_janet"
        - "bush_route_hidden_pressure"
      best_when: "地图有草区和可保护 speaker 的墙，且队伍需要安全 carrier"
      poor_when: "敌方有高速贴脸、强续航 body 或能快速清 speaker 的长手"
      bp_use: "default_plp_gem_grab_vision_build"
    - build: "Backstage Pass aggro variant"
      source: "[[sources/PLP-Janet|PLP-Janet]]"
      changes_capabilities:
        - "Backstage Pass 让下一次 High Note 把 Janet 后跳，蓄得越久距离越远，可越墙/水并在空中免疫"
        - "牺牲 speaker 视野，换取对快卸弹刺客和近身 burst 的逃生窗口"
      enables:
        - "反突进后撤"
        - "越墙保命或转线"
      mitigates_failure_modes:
        - "ground_low_health_dive"
        - "quick_unload_close_range"
      best_when: "敌方最后手给出 Leon/Edgar/Bibi/Bull 等贴脸压力"
      poor_when: "队伍依赖 Janet 提供草区 reveal 或阻断回血"
      bp_use: "anti_aggro_survival_variant"

  map_feature_hooks:
    - id: "gem_carrier_super_countdown_escape"
      map_feature_type: "carrier_airborne_escape"
      uses_feature_by: "Janet 可携带宝石后在 15 秒倒计时使用 Super 升空 6 秒，使地面敌人难以攻击"
      route_or_position: "宝石矿后撤线、己方半场墙后、倒计时转点路线"
      objective_conversion: "把领先局面转成安全拖倒计时，减少被强开掉宝的风险"
      active_when: "Janet 已持宝且有 Super，敌方缺提前施加的 DoT/状态或落点封锁"
      fails_if: "Super 前已被毒/燃烧/状态命中，落点被预判，或 Janet 没有足够血量起飞"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "slot_task.gem_carrier_escape"
    - id: "drop_the_bass_bush_reveal"
      map_feature_type: "temporary_bush_reveal_and_heal_denial"
      uses_feature_by: "speaker 在 8 格半径持续伤害草内敌人，揭示位置并阻断自然回血"
      route_or_position: "中心草、矿区侧草、球路草口、热区外草边"
      objective_conversion: "把隐藏伏击变成可见路线，并拖慢低血敌人的复位"
      active_when: "speaker 可放在墙后或敌方难以快速清掉的位置"
      fails_if: "speaker 被长手立刻清掉，或敌方从半径外绕路"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "map_bp_factors.bush_reveal_window"
    - id: "backstage_pass_wall_escape"
      map_feature_type: "anti_aggro_wall_reposition"
      uses_feature_by: "Backstage Pass 在攻击时后跳，可越墙/水并短时免疫伤害"
      route_or_position: "侧墙后、草口被贴脸处、长线被刺客压近的回撤角"
      objective_conversion: "把敌方贴脸开团变成 Janet 保命并继续远程压线"
      active_when: "敌方爆发依赖近身三发/短窗口卸弹，Janet 有 ammo 和 Gadget"
      fails_if: "后跳落点被预判、敌方有二段追击，或 Janet 无 ammo 无法触发后跳"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "candidate_eval.anti_dive_reposition"
    - id: "super_stage_view_scout_and_rotate"
      map_feature_type: "airborne_scout_and_wall_bypass"
      uses_feature_by: "Super 飞越障碍并可配合 Stage View 揭示大范围草丛，炸弹用于驱赶而非主伤害"
      route_or_position: "墙后转线、敌方草丛背面、carrier 安全落点"
      objective_conversion: "获取草区信息、重新定位，或逼敌方躲避炸弹离开关键路线"
      active_when: "目标是侦察/转点/拖时间，而不是在空中打高伤害"
      fails_if: "把 Super 当作击杀技能，或用于 Hot Zone 占区这类空中不能贡献的目标"
      example_maps:
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
      bp_use: "map_bp_factors.airborne_rotation_and_scout"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "安全 carrier 和倒计时升空"
        - "草区 speaker reveal"
        - "长线蓄力 poke 与阻断回血"
      cannot_fulfill:
        - "主坦克/主 burst"
        - "独立处理强贴脸或高血量前排"
      needs_teammate_support:
        - "反坦、硬控/peel、清 speaker 威胁的长手"
      false_positive: "Janet 能携宝逃生，但如果前期控矿失败或没有 peel，她很难单独拿到领先"
    - mode: "Brawl Ball"
      can_fulfill:
        - "草区 reveal 和长线压球路"
        - "Backstage Pass 逃离贴脸"
      cannot_fulfill:
        - "稳定破门"
        - "空中持球直接占位或射门计划"
      needs_teammate_support:
        - "破门/射门、前排、硬控"
      false_positive: "空中安全不等于模式目标收益；Brawl Ball 中 Janet 更多是视野/压线而非核心 scorer"
    - mode: "Hot Zone"
      can_fulfill:
        - "区外 reveal、阻断回血和长线支援"
      cannot_fulfill:
        - "Super 期间占区"
        - "单人顶区"
      needs_teammate_support:
        - "站区前排和区内持续输出"
      false_positive: "Fandom 明确 Super 期间不能占 Hot Zone，因此不能把空中免伤计入踩区能力"

  failure_modes:
    - id: "super_cannot_reload_heal_or_hold_zone"
      active_when: "队伍把 Janet Super 当作持续输出/占区工具"
      exposed_by: "[[sources/Fandom-Janet|Fandom-Janet]] Super restrictions"
      mitigation: "把 Super 用于 Gem 倒计时逃生、侦察和转点；Hot Zone 需要队友站区"
      bp_use: "objective_contract_hard_gate"
    - id: "speaker_low_hp_and_decay"
      active_when: "Drop The Bass 放在开阔地或敌方射线内"
      exposed_by: "Drop The Bass has 1000 HP and decays over time"
      mitigation: "放墙后、草后或敌方需要绕路才能清的位置"
      bp_use: "map_hook_reliability_check"
    - id: "focus_time_punished_by_dive"
      active_when: "Janet 需要蓄力到长线但敌方高速贴脸"
      exposed_by: "High Note range narrows/lengthens over aim time"
      mitigation: "Vocal Warm Up、Backstage Pass、队友 peel 或只在安全长线角架枪"
      bp_use: "candidate_eval.aggro_pressure_filter"
    - id: "super_bombs_low_precision"
      active_when: "Janet 试图用 Super 直接击杀站定目标"
      exposed_by: "Fandom notes bombs do not drop directly below and may hit stationary target once"
      mitigation: "用 Super 的免伤/位移/视野收益，不把空中炸弹当主伤害"
      bp_use: "damage_output_false_positive_filter"

  conditional_matchups:
    - target: ["Stu", "Tara", "Sandy", "Jae-Yong"]
      direction: "subject_favored"
      source: "[[sources/PLP-Janet|PLP-Janet]]"
      mechanism: "长线 poke、speaker reveal 和空中脱离能减少他们靠草/控制节奏逼近 carrier 的收益"
      active_when: "Janet 有安全蓄力位置，speaker 可保护，且队友能接住被 reveal 的目标"
      fails_when: "Tara/Sandy 提前控住落点或 Janet 没有 Super 处理倒计时追击"
      bp_use: "gem_carrier_vision_answer"
    - target: ["Nita", "Spike", "Charlie", "Sprout"]
      direction: "subject_favored"
      source: "[[sources/PLP-Janet|PLP-Janet]]"
      mechanism: "piercing 长线和空中越墙转点可以压制固定召唤物/墙后控制的站位，speaker 阻断低血复位"
      active_when: "Janet 不被强行贴脸，且能用 Super/Backstage 越过墙体压力"
      fails_when: "召唤物或墙后控制保护刺客进场，Janet 被迫近距离作战"
      bp_use: "long_line_control_into_static_threats"
    - target: ["Leon", "Bibi", "Edgar", "Rosa", "Bull"]
      direction: "target_favored"
      source: "[[sources/PLP-Janet|PLP-Janet]]"
      mechanism: "高速贴脸和高血量近战会惩罚 Janet 地面 3400 HP、低爆发和蓄力时间"
      active_when: "他们能从草口/墙后接触 Janet，且 Janet 没有 Backstage Pass 或 Super"
      fails_when: "speaker/vision 提前暴露路线，Backstage Pass 后跳成功，或队友 peel 及时"
      bp_use: "avoid_without_anti_aggro_variant"
    - target: ["Carl", "Pam", "Gale"]
      direction: "target_favored"
      source: "[[sources/PLP-Janet|PLP-Janet]]"
      mechanism: "稳定中远程压线、召唤/治疗续航或推离控制能清 speaker、压 Janet 落点并打断她的 carrier 节奏"
      active_when: "他们控制中线，Janet 的 Super 被迫用于逃生而非转优势"
      fails_when: "Janet 已经领先并可用 Super 拖倒计时，或队友先处理他们的续航/控制资源"
      bp_use: "needs_lane_help_or_last_pick_caution"

  slot_notes:
    slot_1: "Gem Grab 草图可考虑早手，但必须确认队伍后续能补反坦和 peel"
    slot_2_3: "适合作为 carrier/视野计划核心，后续围绕保护 speaker 和倒计时逃生建队"
    slot_4_5: "看到敌方缺强贴脸或草区依赖高时价值上升"
    slot_6: "可以最后手惩罚缺追击的控制阵容；遇到贴脸链要切 Backstage Pass 或避选"
```

## 关联页面

- [[sources/Fandom-Janet|Fandom 来源摘要: Janet]]
- [[sources/PLP-Janet|PLP 来源摘要: Janet]]
