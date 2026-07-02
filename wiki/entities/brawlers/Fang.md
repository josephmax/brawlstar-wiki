# Fang

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：连跳收割 / 后排切入 / clump punish

## 来源摘要

- Fandom：[[sources/Fandom-Fang|Fandom 来源摘要: Fang]]
- PLP：[[sources/PLP-Fang|PLP 来源摘要: Fang]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Hot Zone, Bounty, Knockout

## 角色定位总结

Fang 的 BP 价值来自“用远端鞋子充 Super，再把一次进场转成连锁击杀”。他的贴脸伤害、Roundhouse Kick 短眩晕和 Fresh Kicks 重置让他能惩罚低自保后排、投掷和残血抱团，但 Super 过程中仍会吃伤害、控制和减速，且连跳不能穿过墙。Fang 不是泛用长手，他需要目标站位、地图路线和敌方控制资源同时满足。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Fang|Fandom-Fang]] direct_raw_capture_2026-06-30-v2"
    plp: "[[sources/PLP-Fang|PLP-Fang]] direct_raw_capture_2026-06-30"
    user_notes: "按高水平 BP 处理：连跳刺客必须证明进场目标、重置条件和控制资源状态"

  capability_vector:
    effective_range: "近身踢击 2.67 格；miss 后鞋子额外延伸到 9.33 格但只造成 25% 伤害"
    projectile_reliability: "贴脸可靠；鞋子适合充能和消耗，不适合当主要击杀手段"
    burst: "Super + 普攻 + Roundhouse Kick 的短窗口爆发很高"
    sustained_dps: "非常快装填，但 unload 和进退场节奏限制持续输出"
    objective_damage: "低到中；不是 Heist safe DPS，目标价值主要来自击杀后转目标"
    mobility: "Super 10 格高速突进并可最多连跳 4 个目标；Hypercharge 后 Super 可穿墙"
    survivability: "生命值高于多数刺客；Divine Soles/Shield Gear 可挡一次关键伤害，但进场中仍可被打断或集火"
    engage: "强条件 engage；需要 Super、目标距离和连跳路径"
    disengage: "Super 可用于逃生，但一旦落点被预判很难撤出"
    anti_aggro: "Roundhouse Kick 和 Corn-Fu 可惩罚部分依赖移动的刺客"
    anti_tank: "不是稳定反坦；可借坦克作为跳板打后排，但落到坦克脸上会亏"
    wall_break: "基础形态无破墙；Hypercharge Super 可穿墙但不等于常态路线"
    throw_or_wall_bypass: "Corn-Fu 可越墙/隔墙覆盖，Hypercharge Super 可穿墙"
    area_control: "Corn-Fu 提供短时地面爆点，主要用于封路或补伤害"
    scouting_or_vision: "无稳定探草"
    team_support: "主要通过击杀、逼退后排和连跳制造人数差"
    spawnable_or_pet: "无"
    crowd_control: "Roundhouse Kick 2.33 格短眩晕 0.5 秒"
    terrain_creation: "Corn-Fu/Hypercharge 路径产生 popcorn 爆点，但不改变墙体"
    terrain_destruction: "无常态地形破坏"

  build_switches:
    - build: "Roundhouse Kick / Fresh Kicks / Shield + Damage"
      source: "[[sources/PLP-Fang|PLP-Fang]] + [[sources/Fandom-Fang|Fandom-Fang]]"
      changes_capabilities:
        - "Roundhouse Kick 重置攻击节奏并短暂眩晕，让 Fang 能把 Super 落点转成确认击杀"
        - "Fresh Kicks 在 Super 击杀后立即重置 Super，放大残血连锁和多目标抱团惩罚"
        - "Shield/Damage 提高进场容错和击杀阈值"
      enables:
        - "后排/投掷收割"
        - "Brawl Ball 击杀防守者后得分"
        - "Bounty/Knockout 残血链式收头"
      mitigates_failure_modes:
        - "partially_mitigates_landing_target_survives"
        - "partially_mitigates_single_cc_window_if_target_dies_fast"
      best_when: "敌方有低自保后排、站位会被目标牵连，且主要控制/击退资源不稳定"
      poor_when: "敌方有 Surge/Shelly/Gale/Colette 等专门留资源处理突进，或站位极度分散"
      bp_use: "last_pick_chain_assassin / backline_punish"
    - build: "Corn-Fu / Divine Soles"
      source: "[[sources/Fandom-Fang|Fandom-Fang]]"
      changes_capabilities:
        - "Corn-Fu 提供围绕 Fang 的短时区域爆点，可隔墙打扰投掷或限制移动型刺客"
        - "Divine Soles 每 3 秒减少下一次投射物伤害，提高过线充能和吃一发关键伤害的能力"
      enables:
        - "墙后补伤害"
        - "反移动刺客近身"
        - "更保守的充能路线"
      mitigates_failure_modes:
        - "mitigates_open_lane_chip_before_super"
      best_when: "需要先靠鞋子/走位充 Super，或对方主要威胁来自远程单发消耗"
      poor_when: "目标击杀阈值依赖 Roundhouse Kick 确认控制"
      bp_use: "survival_or_area_denial_branch"

  map_feature_hooks:
    - id: "brawl_ball_chain_to_score"
      map_feature_type: "score_window"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      route_or_position: "中路抢球、侧草推进、球门前防守者和低血量补位链"
      objective_conversion: "用 Super/Roundhouse 击杀或眩晕防守者，随后制造直接射门或持球推进窗口"
      active_when: "敌方防守者站位靠近、缺 Gale/Shelly/Surge 等反突进资源，Fang 已有 Super 或可用鞋子安全充能"
      fails_if: "敌方分散站位、控制留给 Fang 落点，或 Fang 击杀后没有队友/球权转化为进球"
      bp_use: "slot_task.scoring_window_assassin"
    - id: "ko_bounty_backline_chain"
      map_feature_type: "pickoff_chain"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      route_or_position: "掩体边缘、复活后站位交汇处、低血量后排和投掷口袋"
      objective_conversion: "一次收头转成连跳或逼迫后排退位，服务 Bounty/Knockout 的人数差"
      active_when: "我方能先压低目标，敌方没有墙体阻断连跳，且 Fang 的落点不在三人火力中心"
      fails_if: "目标满血且有 peel，墙阻断 7 格连跳搜索，或 Fang Super 先落到高血量前排"
      bp_use: "candidate_eval.pickoff_chain"
    - id: "hot_zone_clump_clear"
      map_feature_type: "zone_clear"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
      route_or_position: "热区入口、圈旁墙后控制点、敌方抱团站圈位置"
      objective_conversion: "用 Super 连跳、Roundhouse 和 Corn-Fu 把站圈人员打散或击杀"
      active_when: "敌方为了站圈而空间重叠，且我方有队友同步清圈或接管区域"
      fails_if: "Fang 单人进圈被集火，敌方保留减速/击退，或站位分散导致无法连跳"
      bp_use: "map_bp_factors.clump_punish_zone_clear"
    - id: "wall_pocket_hypercharge_or_cornfu"
      map_feature_type: "wall_pocket_pressure"
      example_maps:
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
      route_or_position: "墙后投掷口袋、球门墙后防守位或区域控制点"
      objective_conversion: "用 Corn-Fu 越墙补伤害，或在 Hypercharge 后穿墙切入"
      active_when: "敌方依赖墙后低自保控制，且 Fang 不需要先穿越完整开阔线"
      fails_if: "没有 Hypercharge 时把穿墙当常态能力，或墙后目标有 bodyguard/控制"
      bp_use: "terrain_state_plan.conditional_wall_bypass"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "defender_pickoff"
        - "scoring_window_after_kill"
        - "side_lane_assassin_pressure"
      cannot_fulfill:
        - "稳定破门"
        - "无 Super 正面持球硬推"
      needs_teammate_support:
        - "球权、破墙或补射跟进"
      false_positive: "Fang 能杀人不等于能进球；必须说明击杀后如何转成得分窗口"
    - mode: "Bounty"
      can_fulfill:
        - "low_hp_chain_finisher"
        - "backline_threat"
      cannot_fulfill:
        - "全程长线消耗"
        - "无代价先进场开团"
      needs_teammate_support:
        - "先手压血和控制目标血线"
      false_positive: "鞋子远不等于射手；远端鞋子主要是充 Super 和补伤害"
    - mode: "Knockout"
      can_fulfill:
        - "late_round_pickoff"
        - "thrower_or_marksman_collapse"
      cannot_fulfill:
        - "无视敌方控制强行开局进场"
      needs_teammate_support:
        - "逼资源、压缩走位和保护 Fang 落点"
      false_positive: "敌方站位分散时 Fresh Kicks 价值下降，Fang 变成单次突进"
    - mode: "Hot Zone"
      can_fulfill:
        - "clump_punish"
        - "anti_thrower_clear"
      cannot_fulfill:
        - "长期站圈锚点"
        - "被控制覆盖时单人清圈"
      needs_teammate_support:
        - "清场后站圈的人"
      false_positive: "Fang 清圈不是占圈；没有队友站圈会赢击杀输计分"

  failure_modes:
    - id: "super_controlled_during_travel"
      active_when: "敌方保留 stun/slow/knockback/silence 或爆发火力覆盖 Fang 落点"
      exposed_by: "[[sources/Fandom-Fang|Fandom-Fang]] 明确 Super 过程中仍会受伤、被眩晕或减速"
      mitigation: "等待关键控制交出，或用队友先压血/控人再进场"
      bp_use: "must_track_enemy_cc_resources"
    - id: "chain_blocked_by_wall_or_spacing"
      active_when: "目标之间被墙隔开或敌方站位超过连跳半径"
      exposed_by: "[[sources/Fandom-Fang|Fandom-Fang]] Super 连跳要求附近目标且不能在墙后"
      mitigation: "只把连跳写入计划时，明确敌方会为目标/站圈/防守而靠近"
      bp_use: "map_and_position_gate"
    - id: "lands_on_tank_not_backline"
      active_when: "Fang Super 先命中高血量前排，且无法跳到后排或击杀重置"
      exposed_by: "[[sources/Fandom-Fang|Fandom-Fang]] 提示可借坦克跳后排但不应结束在坦克身上"
      mitigation: "用鞋子/队友伤害压低后排，或等待坦克与后排成链"
      bp_use: "target_selection_check"
    - id: "kill_only_no_objective"
      active_when: "Brawl Ball/Hot Zone 中 Fang 击杀后没有球权、站圈或队友接管"
      exposed_by: "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]] objective_conversion 要求"
      mitigation: "把 Fang 当 scoring window / zone clear，而不是唯一目标位"
      bp_use: "objective_contract_check"

  conditional_matchup_seeds:
    - target: ["Piper", "Tick", "Dynamike", "Grom", "Mr. P", "Berry"]
      direction: "subject_favored"
      source: "[[sources/PLP-Fang|PLP-Fang]]"
      mechanism: "Fang 用鞋子充能后通过 Super/Roundhouse 越过远程消耗区，惩罚低近战自保后排和投掷"
      active_when: "地图有掩体或目标被压血，后排没有 bodyguard，Fang 能在落点完成击杀"
      fails_when: "目标有墙阻断连跳、队友保护或保留控制，Fang 先被消耗到无法进场"
      bp_use: "last_pick_backline_punish"
    - target: ["Jessie", "El Primo"]
      direction: "volatile"
      source: "[[sources/PLP-Fang|PLP-Fang]]"
      mechanism: "Fang 可用 Super 处理孤立 Jessie 或借前排跳后排，但炮台/高血量身体会改变落点和击杀阈值"
      active_when: "目标孤立、炮台不影响落点，或前排只是跳板"
      fails_when: "Jessie 炮台和队友保护覆盖 Fang，或 Primo/Bull 类前排把 Fang 留在近身互打"
      bp_use: "route_and_landing_check"
    - target: ["Surge", "Shelly", "Nita", "Gale", "Chester", "Bull", "Colette", "Sirius"]
      direction: "target_favored"
      source: "[[sources/PLP-Fang|PLP-Fang]]"
      mechanism: "击退、反突进爆发、召唤物身体、百分比伤害或随机/控制爆发能阻断 Fang 落点击杀"
      active_when: "这些资源被留给 Fang 的 Super 或 Roundhouse 前后窗口"
      fails_when: "资源已交、目标低血孤立，或 Fang 只需要一次 Super 重置"
      bp_use: "must_avoid_or_ban_reason_for_fang_plan"
    - target: ["Mortis", "Kenji", "Alli", "Mico"]
      direction: "subject_favored"
      source: "[[sources/Fandom-Fang|Fandom-Fang]]"
      mechanism: "Corn-Fu 和 Roundhouse Kick 能限制依赖移动贴脸的刺客，Fang 贴脸爆发可反打"
      active_when: "Fang 有弹药或 gadget，且对方必须进 Fang 身边完成伤害"
      fails_when: "对方先手骗出 Roundhouse，或 Fang 被连续位移/队友伤害夹击"
      bp_use: "anti_mobile_aggro_branch"

  slot_notes:
    slot_1: "不建议作为普通一抢；早手会暴露刺客路线并被反突进/控制回答"
    slot_2_3: "仅在地图天然奖励后排切入或 clump punish 时可早出，并要求队友补目标承接"
    slot_4_5: "适合在已知敌方 2 位缺硬反突进时补后排威胁，或针对投掷/射手口袋"
    slot_6: "最适合最后手：确认敌方无稳定 peel、站位会被目标牵连，且 Fang 的击杀能转成进球、收星或站圈"
```

## 关联页面

- [[sources/Fandom-Fang|Fandom 来源摘要: Fang]]
- [[sources/PLP-Fang|PLP 来源摘要: Fang]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
