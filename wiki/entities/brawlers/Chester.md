# Chester

## 基本信息

- 稀有度：Legendary
- 定位：Damage Dealer
- 类型：随机 Super 工具箱 / 铃铛序列爆发 / 后手反突进

## 来源摘要

- Fandom：[[sources/Fandom-Chester|Fandom 来源摘要: Chester]]
- PLP：[[sources/PLP-Chester|PLP 来源摘要: Chester]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Hot Zone

## 角色定位总结

Chester 的 BP 价值不是“随机所以万能”，而是他在中近距离用 1/2/3/4 铃铛序列制造爆发窗口，并用随机 Super 在不同局面承担击退、眩晕、毒伤、区域 slow 或自奶功能。Fandom 明确提醒：近距离 3/4 铃铛可以处理大量刺客/坦克，但开阔图遇到多个长射程时远端伤害不足。BP 中必须同时检查铃铛序列、当前 Super、地形是否允许接近，以及敌方是否能在 Chester 进入有效范围前先打掉他。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-17"
    plp: "[[sources/PLP-Chester|PLP-Chester]]"
    user_notes: none

  capability_vector:
    effective_range: mid_long_but_best_mid_close; 8.33 格基础射程，真正爆发依赖近中距离多铃命中
    projectile_reliability: variable; 铃铛数和扩散改变命中形态，Super 随机导致计划稳定性下降
    burst: high_with_3_or_4_bells_at_close_range
    sustained_dps: medium; Candy Beans 在 5 秒内随机提供 20% damage、2.5x reload、150 移速或每秒 420 治疗之一，效果不可指定且冷却 15 秒
    objective_damage: low_medium; 主要靠击杀和清人转目标，不是 Heist race 核心
    mobility: low_base; Candy_Beans_speed_buff_is_random
    survivability: medium; 3800 HP，加随机 Strong Mint 或 Candy Beans heal 可短窗续航
    engage: medium_if_speed_or_stun_super_available
    disengage: medium_with_Candy_Popper_knockback_or_Jawbreaker_stun
    anti_aggro: high_when_sequence_and_super_are_ready
    anti_tank: high_in_close_burst_windows; poor_if_forced_to_cross_open_lane
    wall_break: conditional_with_Candy_Popper
    throw_or_wall_bypass: low_conditional; Candy Popper lob can hit over obstacles
    area_control: conditional_with_Pop_Rocks_slow_zone
    scouting_or_vision: low
    team_support: low; 主要通过控制/击杀减压
    spawnable_or_pet: none
    crowd_control: Jawbreaker_stun_or_Pop_Rocks_slow_or_Candy_Popper_knockback
    terrain_destruction: Candy_Popper_wall_break

  build_switches:
    - build: "Candy Beans / Single Bellomania / Speed, Damage"
      source: "[[sources/PLP-Chester|PLP-Chester]]"
      changes_capabilities:
        - "Candy Beans 提供 5 秒随机 buff：20% damage、每秒 420 治疗、2.5x reload 或 150 移速之一；不可指定且冷却 15 秒"
        - "Single Bellomania 让第一铃伤害更高，改善序列前段的换血和开局预热"
        - "Speed/Damage 让 Chester 在草图和斩杀线附近更容易完成近中距离爆发"
      enables:
        - "Brawl Ball 中场/门前反突进"
        - "Hot Zone 入口爆发清人"
        - "Gem Grab 矿区 bodyguard 或反切"
      mitigates_failure_modes:
        - "sequence_low_burst_start"
        - "short_window_survivability"
      best_when: "地图有中近距离接触点，Chester 能预热到 3/4 铃并保留 Super 或 Candy Beans"
      poor_when: "地图完全开放，敌方长手可在 Chester 接近前持续消耗"
      bp_use: default_competitive_variance_build
    - build: "Spicy Dice Super selection variant"
      source: "[[sources/Fandom-Chester|Fandom-Chester]]"
      changes_capabilities:
        - "Spicy Dice 可重抽当前 Super，让 Chester 更主动寻找 stun、knockback、area 或 self-heal 需求"
      enables:
        - "resource_tracking.super_type_before_objective_fight"
        - "last_pick_super_swing"
      mitigates_failure_modes:
        - "wrong_random_super_for_current_task"
      best_when: "阵容需要某类 Super 才能处理球路、热区入口或淘汰回合"
      poor_when: "队伍更需要 Candy Beans 的稳定短窗属性"
      bp_use: super_type_control_variant

  map_feature_hooks:
    - map_feature_type: brawl_ball_close_bell_burst_and_super_utility
      uses_feature_by: "3/4 铃近身爆发配合 Jawbreaker stun、Candy Popper knockback 或 Pop Rocks 区域控制处理球路"
      route_or_position: "midfield ball、goal-front defender、side grass push、己方门前反打点"
      objective_conversion: "击杀/眩晕持球者，逼退门前防守，或用随机 Super 创造一次射门窗口"
      active_when: "Chester 已预热到多铃，球路会经过中近距离，队友能接球或补伤害"
      fails_if: "Chester 只有低铃序列、Super 不匹配，或敌方在开阔长线先把他压低"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_burst_or_disarm_with_sequence_gate
    - map_feature_type: hot_zone_pop_rocks_or_jawbreaker_entry_punish
      uses_feature_by: "Pop Rocks 可封入口，Jawbreaker stun 或 Candy Popper knockback 可惩罚站区身体"
      route_or_position: "zone entrance、zone edge wall、grass mouth、re-entry choke"
      objective_conversion: "清掉进圈目标、打断回区、给己方 body 站区时间"
      active_when: "目标必须反复进入同一入口，Chester 有合适 Super 或多铃爆发"
      fails_if: "随机 Super 不适配当前 zone fight，或敌方用长手/投掷从圈外清 Chester"
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.zone_entry_burst_with_random_super_gate
    - map_feature_type: gem_mid_sequence_burst_bodyguard
      uses_feature_by: "Chester 预存 3/4 铃，在矿区入口或 carrier 退路线惩罚刺客/坦克接近"
      route_or_position: "gem mine、center fort doorway、H 草入口、carrier countdown retreat"
      objective_conversion: "保护 carrier、清敌方进矿 body，或在倒计时阶段反打追击者"
      active_when: "己方已有 carrier，Chester 站在中近距离保护位而不是裸站开阔中路"
      fails_if: "敌方长手站远端消耗，或 Chester 被迫自己拿宝石承受多角度压力"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Double Swoosh
      bp_use: map_bp_factors.carrier_bodyguard_with_sequence_gate
    - map_feature_type: knockout_random_super_last_pick_swing
      uses_feature_by: "随机 Super 工具箱和多铃爆发可在墙边/缩圈时制造一次高上限回合翻转"
      route_or_position: "late-round choke、wall edge、low-health retreat、closed lane approach"
      objective_conversion: "用 stun、knockback、毒伤或区域 slow 拿第一杀或保护血量领先"
      active_when: "敌方缺多长手压制，回合会进入中距离或墙边接触"
      fails_if: "地图是纯开放狙击镜像，Chester 在进入铃铛爆发距离前被打残"
      example_maps:
        - Belle's Rock
        - New Horizons
        - Layer Cake
        - Flaring Phoenix
      bp_use: slot_task.last_pick_round_swing_with_super_variance

  objective_contracts:
    - mode: Gem Grab
      can_fulfill:
        - "mine_entry_bodyguard"
        - "carrier_chase_punish"
        - "mid_close_burst_pick"
      cannot_fulfill:
        - "stable_long_range_mid_into_multiple_snipers"
        - "primary_carrier_without_peel"
      needs_teammate_support:
        - "true_carrier_or_range_anchor"
        - "vision_or_thrower_answer"
      false_positive: "PLP Gem Grab 信号不能直接推出 Chester 能打所有矿图；他需要中近距离接触点"
    - mode: Brawl Ball
      can_fulfill:
        - "ball_carrier_burst_or_stun"
        - "goal_defender_knockback_or_area_control"
        - "anti_aggro_midfield_trade"
      cannot_fulfill:
        - "always_on_goal_wallbreak"
        - "solo_scorer_without_followup"
      needs_teammate_support:
        - "scorer_or_pass_receiver"
        - "wallbreak_if_goal_is_closed"
      false_positive: "Chester 能制造门前爆发窗口，但随机 Super 不保证每次都有进球工具"
    - mode: Hot Zone
      can_fulfill:
        - "zone_entry_burst"
        - "random_super_area_or_stun_window"
        - "anti_body_clear"
      cannot_fulfill:
        - "durable_primary_zone_body"
      needs_teammate_support:
        - "actual_zone_holder"
        - "range_or_thrower_cover"
      false_positive: "Chester 清人强于长期站区；无队友站圈时价值会断"
    - mode: Knockout
      can_fulfill:
        - "last_pick_midrange_swing"
        - "anti_assassin_burst"
        - "random_super_finish_or_peel"
      cannot_fulfill:
        - "pure_open_sniper_mirror"
      needs_teammate_support:
        - "cover_to_close_distance"
        - "long_range_teammate_or_wall_control"
      false_positive: "Fandom 说 Knockout 可行，条件是能接触到中距离，而非开阔图硬对狙"

  failure_modes:
    - id: random_super_variance
      active_when: "当前 Super 与目标任务不匹配，例如需要 stun 但只有 heal/poison，或需要 wallbreak 但没有 Candy Popper"
      exposed_by: "[[sources/Fandom-Chester|Fandom-Chester]] random Super mechanics"
      mitigation: "进入关键团前记录 Super 类型，必要时使用 Spicy Dice 变体"
      bp_use: resource_tracking.current_super_type
    - id: sequence_misalignment
      active_when: "Chester 以 1 铃或 2 铃进入必须爆发的近身对抗"
      exposed_by: "[[sources/Fandom-Chester|Fandom-Chester]] bell sequence tips"
      mitigation: "开局/团前预热铃铛，保留 3/4 铃给刺客、持球者或坦克"
      bp_use: resource_tracking.bell_sequence_before_fight
    - id: open_sniper_range_tax
      active_when: "Piper、Belle、Angelo、Byron 等在开阔长线持续输出，Chester 不能进入多铃有效距离"
      exposed_by: "[[sources/Fandom-Chester|Fandom-Chester]] warning against multiple sharpshooters on open maps"
      mitigation: "只在有墙、草、队友压线或中距离目标点时选"
      bp_use: false_positive_filter.not_a_pure_marksman
    - id: candy_beans_rng_window
      active_when: "Candy Beans roll 出的 buff 不是当前需要的 damage/reload/speed/heal"
      exposed_by: "[[sources/Fandom-Chester|Fandom-Chester]] Candy Beans random buff"
      mitigation: "按当前 20% damage / 2.5x reload / 150 speed / 420 HPS 的 5 秒随机结果估算，并把 15 秒冷却后的下一次使用当独立资源；不写成确定开团能力"
      bp_use: build_rng_gate

  conditional_matchup_seeds:
    - target: Edgar_or_Mortis_or_Kit_or_Lily
      direction: subject_favored
      source: "[[sources/PLP-Chester|PLP-Chester]] / [[sources/Fandom-Chester|Fandom-Chester]]"
      mechanism: "3/4 铃近身 burst 加 Jawbreaker/Candy Popper/Pop Rocks 可在刺客进场时反杀或打断第一波接触"
      active_when: "Chester 预热到高铃，保留 Super 或 Candy Beans，刺客必须进入正面近距离"
      fails_when: "刺客从侧草/墙后先手且 Chester 当前是低铃或错误 Super"
      bp_use: anti_assassin_if_sequence_ready
    - target: Jacky_or_Frank_or_Pam_or_Sandy
      direction: subject_favored
      source: "[[sources/PLP-Chester|PLP-Chester]]"
      mechanism: "多铃爆发和随机 Super 控制可惩罚固定 objective body 或低机动支援站位"
      active_when: "目标必须守球路、热区、矿区入口且不能从远端白打 Chester"
      fails_when: "目标有队友长手/投掷支援，或 Frank/Jacky 先拿到控制窗口"
      bp_use: objective_body_response_with_burst_gate
    - target: Piper_or_Belle_or_Angelo_or_Byron
      direction: target_favored
      source: "[[sources/PLP-Chester|PLP-Chester]] / [[sources/Fandom-Chester|Fandom-Chester]]"
      mechanism: "极长线或稳定长手在 Chester 进入多铃爆发距离前压低血量，并让随机 Super 工具难以触发"
      active_when: "地图开放、缺墙草接近路线，Chester 队伍不能压缩距离"
      fails_when: "墙体/草线让 Chester 能预热后进入中近距离，或长手被队友先压退"
      bp_use: avoid_open_lane_into_multiple_snipers
    - target: Charlie_or_Meg_or_Willow_or_Lola
      direction: target_favored
      source: "[[sources/PLP-Chester|PLP-Chester]]"
      mechanism: "茧、机甲身体、控制接管、替身/双火力会打乱 Chester 的单体爆发目标和随机 Super 转化"
      active_when: "他们能在目标点用资源吃掉 Chester 的多铃窗口或逼他打错误目标"
      fails_when: "资源层被队友先清，Chester 只负责补短窗爆发"
      bp_use: must_answer_resource_or_body_before_chester

  slot_notes:
    slot_1: "不宜盲先手，除非地图天然进入中近距离且敌方难以用长手压制；随机资源会给后续阵容留下反制口。"
    slot_2_3: "可作为反突进/中距离爆发计划手，但需要队友补稳定长线或站点职责。"
    slot_4_5: "适合回答已暴露的刺客、坦克或固定 objective body，同时避免把纯开阔长手留给敌方 slot_6。"
    slot_6: "最适合作为高上限后手，在确认敌方缺多长手和硬资源层后用随机 Super 工具箱压制局部。"
```

## 关联页面

- [[sources/Fandom-Chester|Fandom 来源摘要: Chester]]
- [[sources/PLP-Chester|PLP 来源摘要: Chester]]

## 战斗断点输入

```json
{"combat_breakpoint_profile":{"schema":"brawler_breakpoint_profile.v1","brawler":"Chester","target_states":[{"id":"body","entity_class":"brawler_body","roster_target":true,"health":{"amount":3800,"at_power_level":1,"scaling":"standard"},"source_ref":"[[sources/Fandom-Chester|Fandom-Chester]]"}],"damage_packets":[{"id":"super.candy_popper_explosion","ability_kind":"super","packet_unit":"explosion","delivery_variant":"impact","repeat_model":"resource_gated","damage":{"amount":1600,"at_power_level":1,"scaling":"standard"},"active_when":"随机抽到 Candy Popper 并命中","source_conflict_status":"none","source_ref":"[[sources/Fandom-Chester|Fandom-Chester]]"}],"defense_modifiers":[]}}
```
