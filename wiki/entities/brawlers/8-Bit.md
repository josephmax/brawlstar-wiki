# 8-Bit

## 基本信息

- 稀有度：Super Rare
- 定位：Damage Dealer
- 类型：阵地型增伤输出核心

## 来源摘要

- Fandom：[[sources/Fandom-8-Bit|Fandom 来源摘要: 8-Bit]]
- PLP：[[sources/PLP-8-Bit|PLP 来源摘要: 8-Bit]]
- PLP 推荐模式：Heist, Bounty, Gem Grab

## 角色定位总结

8-Bit 的 BP 价值来自“长射程高持续伤害 + Damage Booster 阵地”。他能把开阔路线、金库 lane、宝石中路或热区入口变成高火力区域；`Cheat Cartridge` 和 `Plugged In` 让他在围绕炮台时补足一部分机动缺陷。主要风险是极慢基础移速、0.8 秒慢卸弹、满射程散布、炮台被投掷/穿墙/召唤物低成本清掉，以及被高速刺客或跳跃进场直接贴脸。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-10"
    plp: "direct_raw_capture_2026-07-11"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "very_long; 10 格射程，适合低承诺长线压制"
    projectile_reliability: "medium; 六束激光有小散布且 0.8 秒卸弹，满射程打高速目标会失准"
    burst: "high_if_full_clip_or_extra_credits_connects; Extra Credits 是可主动瞄准、可与普攻并行的 18 束额外射击，适合静态目标或多目标弹射窗口"
    sustained_dps: "high; 普通装填 1.35 秒，Reload Gear 和 Damage Booster 会显著放大队伍火力"
    objective_damage: "high; Heist lane 和静态目标是主要转换点"
    mobility: "low_base_medium_near_booster; 基础 580 very slow，Plugged In 在炮台 7 格内提供 25% 加速至 725"
    survivability: "medium_high_body_low_escape; 5200 HP 可抗线，但离开炮台或被贴脸后撤退差"
    engage: "low; Cheat Cartridge 可从炮台位移到敌侧或撤退点，但不是稳定开团"
    disengage: "medium_if_booster_anchor_exists; Cheat Cartridge 可回炮台，炮台也可临时挡弹"
    anti_aggro: "conditional; 开阔线和高 DPS 可提前融化前排，近墙/草贴脸会失效"
    anti_tank: "high_on_open_lane; Booster + 全弹命中能压坦克，但怕跳跃/控制绕过射线"
    wall_break: "none"
    throw_or_wall_bypass: "low; 只能把炮台丢过墙后用 Cheat Cartridge 接近，不能持续隔墙输出"
    area_control: "high_when_booster_lives; Damage Booster 让一片区域成为队伍火力锚点"
    scouting_or_vision: "conditional; Hypercharged turret 可探草和打断潜伏，但不是常规视野工具"
    team_support: "high; Damage Booster 增益友方伤害和治疗攻击；Plugged In Buffie 给队友 15% 加速，Boosted Booster Buffie 每 5 秒生成可回 1 ammo 的弹药夹"
    spawnable_or_pet: "high; Damage Booster 是核心炮台/锚点"
    crowd_control: "low"
    source_trace:
      - "[[sources/Fandom-8-Bit|Fandom-8-Bit]]"
      - "[[sources/PLP-8-Bit|PLP-8-Bit]]"

  build_switches:
    - build: "Cheat Cartridge / Plugged In / Damage, Reload"
      source: "[[sources/Fandom-8-Bit|Fandom-8-Bit]]"
      changes_capabilities:
        - "Cheat Cartridge 把炮台变成撤退点或突袭锚点，修复极慢移速的第一层风险"
        - "Plugged In 让 8-Bit 围绕炮台时从静态炮塔变成可重新站位的阵地核"
        - "Damage/Reload gears 放大 Heist race 和 choke 里的持续火力"
      enables:
        - "Heist lane DPS 与金库 race"
        - "Gem Grab 中路火力锚点"
        - "Bounty/Knockout 中的守星和远程消耗"
      mitigates_failure_modes:
        - "slow_rotation_and_no_escape"
        - "booster_position_commitment"
      best_when: "地图给 8-Bit 一个能被队友保护的炮台点，且敌方缺低成本投掷/穿墙清点"
      poor_when: "敌方能通过墙后投掷、跳跃刺客或超远程精确火力绕过 Booster 区域"
      bp_use: "mobility_and_escape_variant_when_booster_anchor_is_safe"
    - build: "Extra Credits / Boosted Booster / Damage, Health"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]] / [[sources/Fandom-8-Bit|Fandom-8-Bit]]"
      changes_capabilities:
        - "主动发射可独立瞄准、可与普攻并行的 18 束额外激光；Buffie 命中后可向附近目标弹射，每次弹射保留 60% 伤害"
        - "Boosted Booster 把增伤半径扩大到 5 格、把增伤提高到 50%，Buffie 每 5 秒生成持续 8 秒并回复 1 ammo 的弹药夹"
        - "当前 PLP 以 Health Gear 替代 Reload Gear，偏向提高慢速阵地核的持续站场，而不是继续堆装填"
      enables:
        - "Heist/Siege 式静态目标爆发"
        - "团队围绕炮台的更大范围火力网和弹药资源循环"
      mitigates_failure_modes:
        - "team_cannot_stay_inside_small_booster_radius"
      best_when: "敌方难以贴脸，且有静态目标、抱团目标或队友能围绕炮台拾取弹药夹"
      poor_when: "敌方高速进场、投掷清炮台或需要频繁位移；选择 Extra Credits 也会放弃 Cheat Cartridge 的撤退锚点"
      bp_use: "current_plp_default_static_objective_and_team_resource_build"

  map_feature_hooks:
    - id: "heist_long_lane_booster_safe_dps"
      map_feature_type: "long_range_safe_damage"
      uses_feature_by: "10 格射程、Reload/Damage gear 和 Booster 增伤让 8-Bit 能在赢线后持续打库"
      route_or_position: "三路 Heist lane、远程打库角度、或金库入口前的炮台保护位"
      objective_conversion: "把 lane win 转成持续 safe DPS，并用炮台增伤队友的 race"
      active_when: "炮台能放在墙后或安全半场，敌方短手没有低成本接近路线"
      fails_if: "投掷/穿墙/召唤物清炮台，或敌方远程 race 不需要进入 8-Bit 火力区"
      example_maps:
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Safe Zone|Safe Zone]]"
      bp_use: "required_capabilities.long_range_sustained_safe_dps"
    - id: "gem_mid_booster_anchor_and_countdown_retreat"
      map_feature_type: "gem_mine_fire_anchor"
      uses_feature_by: "Booster 把中路射手/治疗输出转成高火力阵地，Plugged In 支持倒计时撤退"
      route_or_position: "宝石矿附近墙后炮台点、中心入口、或 carrier 撤退半径"
      objective_conversion: "保护宝石矿访问，领先后用炮台区守倒计时"
      active_when: "队伍有独立 carrier 或护送者，8-Bit 负责中线火力而不是独自拾宝"
      fails_if: "敌方从侧草绕过火力区，或 thrower pocket 直接打掉炮台"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "map_bp_factors.gem_mid_fire_anchor"
    - id: "hot_zone_protected_booster_entry_lock"
      map_feature_type: "zone_entry_fire_anchor"
      uses_feature_by: "炮台增伤让站圈队友和 8-Bit 在 choke 前形成高 DPS 封门"
      route_or_position: "单圈入口、L 墙支援口袋、或 zone 旁可保护炮台的位置"
      objective_conversion: "把站圈队友的生存时间和入口伤害转成计分"
      active_when: "队伍有真正站圈身体，8-Bit 在圈外提供火力和 Booster 支援"
      fails_if: "敌方用开墙/投掷清炮台，或 8-Bit 只能在圈外消耗而没人站圈"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "candidate_eval.zone_fire_anchor_not_primary_body"
    - id: "bounty_knockout_turret_cover_and_star_lead"
      map_feature_type: "long_sightline_with_turret_cover"
      uses_feature_by: "长射程低承诺消耗和炮台挡弹/增伤可保护星差，但 8-Bit 移动慢"
      route_or_position: "Bounty 长线、Knockout 开阔中路或临时掩体后方"
      objective_conversion: "拿到领先后减少换血成本，并用炮台挡非穿透 projectile"
      active_when: "敌方缺投掷、穿透或跳跃进场，且队伍能保护 8-Bit 的慢移速"
      fails_if: "Colt/Rico 类多弹道、Barley/Grom 类投掷、或刺客从墙/草贴脸"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
      bp_use: "candidate_eval.star_lead_anchor_with_anti_dive_check"

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - "持续 safe DPS"
        - "Booster 增伤队友 race"
        - "防守短手进库路线"
      cannot_fulfill:
        - "无开线支持时穿越墙/水去打库"
        - "单独追击高速入侵者"
      needs_teammate_support:
        - "清投掷/穿墙清炮台者"
        - "保护炮台的墙体或前排"
      false_positive: "Heist 强度依赖能否稳定打到库和保住 Booster，不是任意 Heist 图都可早手"
    - mode: "Gem Grab"
      can_fulfill:
        - "中路火力锚点"
        - "倒计时撤退炮台区"
        - "帮助队友 carrier 通过增伤控中"
      cannot_fulfill:
        - "安全独自 carrier"
        - "处理侧草视野税"
      needs_teammate_support:
        - "独立载宝、探草、反投掷"
      false_positive: "8-Bit 可守矿，但慢移速和炮台暴露会放大 carrier 风险"
    - mode: "Bounty"
      can_fulfill:
        - "守星火力"
        - "长线输出和炮台临时掩体"
      cannot_fulfill:
        - "主动追击落后局"
        - "无 peel 对抗刺客最后手"
      needs_teammate_support:
        - "反刺客、开墙或投掷答案"
      false_positive: "Bounty 长线只在敌方无法绕过炮台时成立"

  failure_modes:
    - id: "slow_rotation_and_assassin_entry"
      active_when: "敌方有 Mortis、Edgar、Mico、Leon、Kenji 或跳跃进场，并且地图有墙/草接近路线"
      exposed_by: "[[sources/Fandom-8-Bit|Fandom-8-Bit]] slowest movement speed and tips"
      mitigation: "只在开阔线或有队友 peel 时锁定，保留 Cheat Cartridge 作为撤退"
      bp_use: "hard_gate_against_unanswered_dive"
    - id: "booster_removed_by_wall_or_multi_target_pressure"
      active_when: "敌方投掷、穿墙、召唤物、多目标弹道能不进火力区清炮台"
      exposed_by: "Fandom tips list throwers, Squeak, Jacky, Doug, Hank, Shade, Brock, Mr. P, Mico as wall-counter pressure"
      mitigation: "换炮台位置、补开墙/反投掷，或改为不依赖 Booster 的 DPS"
      bp_use: "must_answer_booster_clear"
    - id: "peak_range_spread_and_slow_unload"
      active_when: "敌方是高速、细身位、远程 marksman 或能持续横向走位"
      exposed_by: "Fandom notes slight spread, slow unload speed, and poor peak-range accuracy"
      mitigation: "优先打中短手/静态目标，或让队友控制路线后再输出"
      bp_use: "candidate_eval.projectile_reliability_filter"
    - id: "extra_credits_targeting_and_escape_tradeoff"
      active_when: "8-Bit 选择 Extra Credits 对高速目标输出，或当前 draft 需要 Cheat Cartridge 提供撤退时"
      exposed_by: "Fandom current mechanics: Extra Credits is an independently aimed 18-laser shot; Buffie bounce retains 60% damage, and the build excludes Cheat Cartridge"
      mitigation: "优先打静态、被控或抱团目标；若刺客进场和撤退锚点更重要则改用 Cheat Cartridge"
      bp_use: "build_switch_warning"

  conditional_matchups:
    - target: ["Poco", "Jae-Yong", "Hank", "Rosa"]
      direction: "subject_favored"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]]"
      mechanism: "Booster 增伤、长线持续火力和当前 Health build 能压迫低爆发支援或必须正面推进的身体"
      active_when: "战斗是开阔 front-to-back objective fight，8-Bit 有安全炮台点与队友视野/保护"
      fails_when: "目标阵容有投掷或刺客先清炮台，或草墙让前排跳过远程消耗阶段"
      bp_use: "response_into_low_burst_sustain_or_frontline_shell"
    - target: ["Fang", "Cordelius", "Kit"]
      direction: "subject_favored"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]]"
      mechanism: "8-Bit 的高单轮伤害、炮台身体与队友 peel 能惩罚需要提交进场资源的刺客"
      active_when: "接近路线开阔、8-Bit 保持满弹药，且队友有击退/控制阻止第二段贴脸"
      fails_when: "Fang/Cordelius/Kit 从墙草或资源优势直接贴脸，或 8-Bit 放弃 Cheat Cartridge 后没有撤退路线"
      bp_use: "conditional_anti_commitment_response_not_blind_counter"
    - target: ["Sprout", "Damian", "Maisie", "R-T", "Brock"]
      direction: "target_favored"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]]"
      mechanism: "墙后控制、超长线或高可靠弹道能利用 8-Bit 的慢移速，并从安全角度清炮台或持续逼位"
      active_when: "地图提供墙后口袋或长直线，8-Bit 必须暴露走位才能守住目标"
      fails_when: "队伍先开墙/清口袋并把炮台放到敌方射程外，或目标缺少持续清点角度"
      bp_use: "must_answer_range_and_booster_clear"
    - target: ["Bolt", "Ash", "Buster"]
      direction: "target_favored"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]]"
      mechanism: "高身体、加速接触或推进掩护能吃住第一轮火力并把战斗压到 8-Bit 不擅长的近身距离"
      active_when: "地图有直线冲锋、草墙接近或目标区必须正面站住，且 8-Bit 缺少可靠 peel"
      fails_when: "路线完全开阔、8-Bit 满弹药且有控制队友，或 Cheat Cartridge 提供安全撤退锚点"
      bp_use: "avoid_body_or_contact_pressure_without_peel"

  slot_notes:
    slot_1: "只在 Heist 长线或可保护炮台的 Gem/Hot Zone 图早手；否则会暴露慢速和炮台清点弱点"
    slot_2_3: "适合围绕 Booster 建立队伍火力核心，再补探草、反投掷和 peel"
    slot_4_5: "看到敌方缺投掷/刺客/多目标清炮台时可补为 DPS 核；需要确认目标转换"
    slot_6: "惩罚低爆发前排或支援壳体，但不能修补队伍缺机动、缺视野或缺清口袋的问题"
```

## 关联页面

- [[sources/Fandom-8-Bit|Fandom 来源摘要: 8-Bit]]
- [[sources/PLP-8-Bit|PLP 来源摘要: 8-Bit]]
