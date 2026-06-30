# Alli

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：草/水路线突进、低血追猎、隐身脉冲刺杀

## 来源摘要

- Fandom：[[sources/Fandom-Alli|Fandom 来源摘要: Alli]]
- PLP：[[sources/PLP-Alli|PLP 来源摘要: Alli]]
- PLP 推荐模式：Gem Grab、Brawl Ball、Heist、Hot Zone

## 角色定位总结

Alli 是依赖地形入口和低血追猎条件的短程 Assassin。她可在水面移动；当屏幕内有生命值不高于 50% 的敌方英雄时会进入 enraged 状态，朝该目标移动获得移速，并能透过草线索追踪目标。普攻在地面是短 dash，在草丛或水面会变成跳跃落点伤害；这让 Alli 在水/草连接路线里有突然进场和规避爆发的能力，但也让她的路线高度吃地图。Super `Stalker` 提供 7 秒脉冲隐身和下一次普攻额外伤害，适合收低血、偷固定目标或逼退后排；隐身有 4 格侦测警告，且强化攻击打空会浪费窗口。

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
    effective_range: "short_route_based; 地面 dash 约 2.33 格，草/水跳跃约 3.33 格，enraged 时距离随移速放大"
    projectile_reliability: "high_if_route_contact; 伤害来自 dash 路径或落点圈，不是长线弹道"
    burst: "high_with_stalker_bonus; Super 后下一次普攻按目标当前生命追加伤害，固定目标按上限收益"
    sustained_dps: "low_medium; dash reload 慢，草/水跳跃 reload 更慢，PLP reload Star Power 缓解 enraged 窗口"
    objective_damage: "medium_high_heist_window; Super 强化攻击对 safe 等固定目标吃满上限，但需要进场路线"
    mobility: "high_on_water_or_bush_routes; 可走水面，草/水普攻变跳跃并短暂无敌"
    survivability: "medium_with_jump_and_stalker; 3900 HP，需要跳跃免伤、隐身和击杀刷新压力"
    engage: "high_conditional; 低血 enrage、草/水跳跃和 Stalker 可开后排"
    disengage: "medium; 跳跃可躲一轮爆发，但跳跃路线经常单向且 reload 慢"
    anti_aggro: "medium; 可用跳跃躲 Edgar/Kenji 等近身爆发，但被 body 压住时缺稳定硬控"
    anti_tank: "low_medium; 能收残血坦克，正面打满血 body 风险高"
    wall_break: "none"
    throw_or_wall_bypass: "terrain_jump_only; 草/水跳跃越过部分障碍，不等同投掷"
    area_control: "low_medium; 主要靠威胁低血撤退线，而不是持续封区"
    scouting_or_vision: "high_when_enraged; blue-eye 追踪和足迹揭示草中低血目标"
    team_support: "medium_pick_pressure; 逼迫敌方低血撤退并制造队友收割窗口"
    spawnable_or_pet: "none"
    crowd_control: "none_direct; 依靠隐身/爆发威胁而非 slow/stun"
    source_trace:
      - "[[sources/Fandom-Alli|Fandom-Alli]]"
      - "[[sources/PLP-Alli|PLP-Alli]]"

  build_switches:
    - build: "Cold-Blooded / You Better Run You Better Take Cover / Speed, Shield, Damage"
      source: "[[sources/PLP-Alli|PLP-Alli]]"
      changes_capabilities:
        - "Cold-Blooded 主动触发 4 秒 enrage，让 Alli 可在没有自然低血目标时启动追击窗口"
        - "You Better Run You Better Take Cover 在 enraged 时提高 reload，缓解短手进场后空窗"
        - "Speed gear 与草线跳跃/追击联动，Shield/Damage 提高单次进场容错"
      enables:
        - "Gem Grab 低血 carrier 追猎"
        - "Brawl Ball 草/水侧路切入"
        - "Heist 固定目标 Stalker burst"
        - "Hot Zone 草边进区刺杀"
      mitigates_failure_modes:
        - "enrage_trigger_too_late"
        - "jump_reload_commitment"
        - "low_hp_after_entry"
      best_when: "地图有草/水接入后排或目标点，且敌方缺稳定 body peel"
      poor_when: "地图开阔、草水路线少，或敌方坦克/近战 answer 能守住 Alli 落点"
      bp_use: "default_plp_route_assassin_build"
    - build: "Feed the Gators / Lizard Limbs variant"
      source: "[[sources/Fandom-Alli|Fandom-Alli]]"
      changes_capabilities:
        - "Feed the Gators 让下一次攻击按伤害 100% 回复，适合高价值爆发后续航"
        - "Lizard Limbs 在 enraged 时让自然回血更快开始"
      enables:
        - "多段 skirmish"
        - "对低血残阵连续追击"
      mitigates_failure_modes:
        - "entry_trades_too_low"
        - "cannot_reset_after_pick"
      best_when: "敌方阵容给 Alli 多次短窗口接触，而不是一次性硬控击杀"
      poor_when: "进场会被控制或 body 链住，回血无法启动"
      bp_use: "sustain_variant_for_scrappy_maps"

  map_feature_hooks:
    - id: "gem_low_hp_retreat_stalker_pick"
      map_feature_type: "carrier_retreat_and_low_hp_chase"
      uses_feature_by: "enrage 追踪低血目标，Stalker 隐身从矿区侧翼切 carrier 或残血后排"
      route_or_position: "宝石矿侧草、敌方 carrier 倒计时退线、矿区水/墙旁入口"
      objective_conversion: "击杀或逼退 carrier，打断倒计时，迫使对方交控制保护残血"
      active_when: "敌方 carrier/控制位会以低血从固定侧路撤退，Alli 有草/水接近线"
      fails_if: "矿区开阔无跳跃路线，或敌方 body/侦测英雄守住 4 格隐身警告范围"
      example_maps:
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
      bp_use: "map_bp_factors.carrier_retreat_assassin_pick"
    - id: "brawl_ball_grass_or_water_jump_scorer_pressure"
      map_feature_type: "side_lane_jump_and_goal_pressure"
      uses_feature_by: "草/水普攻跳跃让 Alli 可越过近身火力并逼门前低血 defender"
      route_or_position: "Brawl Ball 侧草、门前草口、水边绕后线"
      objective_conversion: "清门前守门人、制造掉球、或迫使敌方把 peel 留在侧路"
      active_when: "持球推进能把守门人打到半血以下，Alli 有落点而队友可接球"
      fails_if: "跳跃后落在坦克 body 或硬控范围内，或强化攻击打空导致进攻空转"
      example_maps:
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.side_lane_pick_into_goal"
    - id: "heist_special_target_super_burst"
      map_feature_type: "fixed_objective_stalker_burst"
      uses_feature_by: "Stalker 强化普攻对 safe 等特殊目标按上限加伤，草/水路线辅助接近"
      route_or_position: "safe 侧草、水边偷点路线、己方 lane win 后的进 safe 角度"
      objective_conversion: "把一次隐身进场转化成 safe burst 或迫使防守者回防"
      active_when: "Alli 能安全接近 safe 且敌方无法用 body 控住她的落点"
      fails_if: "路线过长导致隐身被 4 格警告提前暴露，或防守者用坦克站位吸收进场"
      example_maps:
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
      bp_use: "candidate_eval.heist_stalker_burst_variant"
    - id: "hot_zone_grass_water_ambush_entry"
      map_feature_type: "zone_edge_ambush_and_low_hp_cleanup"
      uses_feature_by: "草/水跳跃和 enrage 追踪让 Alli 清理站区边缘残血目标"
      route_or_position: "Hot Zone 区边草、水路入口、敌方回区路径"
      objective_conversion: "把敌方离区治疗或回区路径变成击杀窗口，帮助己方重新站区"
      active_when: "区口有可隐藏路线，队友先把目标压到半血以下"
      fails_if: "敌方 sustain body 长期站区，Alli 无法从短手 burst 直接清满血目标"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.zone_edge_assassin_cleanup"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "低血 carrier 追猎"
        - "草/水侧路 ambush"
        - "隐身进矿区制造掉宝压力"
      cannot_fulfill:
        - "安全主 carrier"
        - "开阔长线持续控矿"
      needs_teammate_support:
        - "先手压血、矿区控线、对坦克 body 的处理"
      false_positive: "Alli 追猎很强，但 enrage 依赖低血可见目标；不能当作无条件开团点"
    - mode: "Brawl Ball"
      can_fulfill:
        - "侧路切后排/守门人"
        - "草/水跳跃制造门前击杀"
        - "Stalker 逼对方回防"
      cannot_fulfill:
        - "主站门坦克"
        - "稳定破墙或远程清球"
      needs_teammate_support:
        - "破门、传球接应、硬控或击退"
      false_positive: "跳跃进门前不是 scorer 保证；落点被 body 守住会直接亏节奏"
    - mode: "Heist"
      can_fulfill:
        - "Super 强化攻击偷 safe"
        - "惩罚低血防守者"
      cannot_fulfill:
        - "从正面持续 race"
        - "无路线时远程打 safe"
      needs_teammate_support:
        - "赢线、开通接近路线、吸引防守火力"
      false_positive: "Heist 值来自接近窗口和强化攻击上限，不是稳定远程 objective DPS"
    - mode: "Hot Zone"
      can_fulfill:
        - "草/水边缘击杀"
        - "清残血回区者"
        - "逼迫敌方后排远离区边"
      cannot_fulfill:
        - "长期单人站区"
        - "正面打满血坦克"
      needs_teammate_support:
        - "站区 body、压血来源、反控制"
      false_positive: "Alli 是清理和进场工具，不是稳定区控本体"

  failure_modes:
    - id: "enrage_depends_on_low_hp_visible_target"
      active_when: "敌方没有半血以下目标在屏幕内，或低血目标及时治疗/撤出视野"
      exposed_by: "[[sources/Fandom-Alli|Fandom-Alli]] enrage 触发与 5 秒保留规则"
      mitigation: "搭配先手 poke/控制，或用 Cold-Blooded 主动启动短窗口"
      bp_use: "engage_condition_gate"
    - id: "jump_route_commitment_and_slow_reload"
      active_when: "Alli 从草/水跳出后落点被 body 守住，且跳跃 reload 慢"
      exposed_by: "Fandom notes bush/water jump reload slower and often one-way"
      mitigation: "只选有撤退线或队友接应的草/水入口，避免孤立跳入满血阵型"
      bp_use: "map_route_false_positive_filter"
    - id: "stalker_detection_and_missed_boost"
      active_when: "敌方在 4 格内侦测隐身，或 Alli 强化攻击打空"
      exposed_by: "Stalker detection warning and boosted attack lost on miss"
      mitigation: "从非正面路线进场，等控制或球权/宝石压力固定敌方走位后再出手"
      bp_use: "super_window_reliability_check"
    - id: "tank_body_and_hard_cc_stop_entry"
      active_when: "Sam、Bull、Hank、Doug、Meg 等站住落点或用体型/回复吃掉 burst"
      exposed_by: "[[sources/PLP-Alli|PLP-Alli]] target_favored seeds"
      mitigation: "先 ban/回答 body，或把 Alli 留作后手惩罚脆后排"
      bp_use: "avoid_into_body_frontline"

  conditional_matchups:
    - target: ["Dynamike", "Grom", "Squeak", "Brock"]
      direction: "subject_favored"
      source: "[[sources/PLP-Alli|PLP-Alli]]"
      mechanism: "草/水路线和 Stalker 能绕过投掷/长线的预瞄节奏，直接贴到低血后排"
      active_when: "地图有侧草/水路，目标缺 body peel，且 Alli 能在被发现前进入短程"
      fails_when: "目标被坦克保护，或地图开阔让 Alli 无法接近"
      bp_use: "assassin_response_to_unprotected_backline"
    - target: ["Sandy", "Edgar", "Stu", "Bo"]
      direction: "subject_favored"
      source: "[[sources/PLP-Alli|PLP-Alli]]"
      mechanism: "enrage 追猎和跳跃免伤可惩罚低血突进/控制位，草内足迹降低伏击收益"
      active_when: "他们已经被压低或必须从可预测草口进入"
      fails_when: "他们先手满资源贴脸，或 Bo mines / Sandy 控场提前锁住 Alli 路线"
      bp_use: "low_hp_cleanup_and_bush_trace_response"
    - target: ["Shade", "Carl", "Melodie", "Sam"]
      direction: "target_favored"
      source: "[[sources/PLP-Alli|PLP-Alli]]"
      mechanism: "高机动、回旋伤害或持续贴身能力会覆盖 Alli 的短爆发，并能追住跳跃落点"
      active_when: "他们能选择第一接触或在 Alli 进场后立刻反打"
      fails_when: "Alli 只在他们半血以下、技能空窗时用 Stalker 收割"
      bp_use: "avoid_without_timing_or_peel"
    - target: ["Bull", "Hank", "Doug", "Meg"]
      direction: "target_favored"
      source: "[[sources/PLP-Alli|PLP-Alli]]"
      mechanism: "高血量 body、回复或形态资源能吸收 Alli 一次进场，并守住草/水出口"
      active_when: "地图目标要求 Alli 从短路线穿过前排，且队伍缺 anti-tank"
      fails_when: "队友先把 body 打残并迫使其离开落点"
      bp_use: "frontline_body_counterpick_warning"

  slot_notes:
    slot_1: "只有在地图草/水路线非常明确且队伍愿意围绕先压血建构时才早手"
    slot_2_3: "可作为进攻层，但需要同步补长线压血或反坦克答案"
    slot_4_5: "看到敌方后排缺保护、草/水侧路开放时价值最高"
    slot_6: "最后手可专门惩罚无 body peel 的低机动后排或 Heist 防守薄点"
```

## 关联页面

- [[sources/Fandom-Alli|Fandom 来源摘要: Alli]]
- [[sources/PLP-Alli|PLP 来源摘要: Alli]]
