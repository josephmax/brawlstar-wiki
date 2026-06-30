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
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "very_long; 10 格射程，适合低承诺长线压制"
    projectile_reliability: "medium; 六束激光有小散布且 0.8 秒卸弹，满射程打高速目标会失准"
    burst: "high_if_full_clip_or_extra_credits_connects; 但 Extra Credits 卸弹更慢，主要用于静态目标"
    sustained_dps: "high; 普通装填 1.5 秒，Reload Gear 和 Damage Booster 会显著放大队伍火力"
    objective_damage: "high; Heist lane 和静态目标是主要转换点"
    mobility: "low_base_medium_near_booster; 基础 580 very slow，Plugged In 在炮台 7 格内提升到 720"
    survivability: "medium_high_body_low_escape; 5200 HP 可抗线，但离开炮台或被贴脸后撤退差"
    engage: "low; Cheat Cartridge 可从炮台位移到敌侧或撤退点，但不是稳定开团"
    disengage: "medium_if_booster_anchor_exists; Cheat Cartridge 可回炮台，炮台也可临时挡弹"
    anti_aggro: "conditional; 开阔线和高 DPS 可提前融化前排，近墙/草贴脸会失效"
    anti_tank: "high_on_open_lane; Booster + 全弹命中能压坦克，但怕跳跃/控制绕过射线"
    wall_break: "none"
    throw_or_wall_bypass: "low; 只能把炮台丢过墙后用 Cheat Cartridge 接近，不能持续隔墙输出"
    area_control: "high_when_booster_lives; Damage Booster 让一片区域成为队伍火力锚点"
    scouting_or_vision: "conditional; Hypercharged turret 可探草和打断潜伏，但不是常规视野工具"
    team_support: "high; Damage Booster 对友方伤害和治疗攻击都有增益"
    spawnable_or_pet: "high; Damage Booster 是核心炮台/锚点"
    crowd_control: "low"
    source_trace:
      - "[[sources/Fandom-8-Bit|Fandom-8-Bit]]"
      - "[[sources/PLP-8-Bit|PLP-8-Bit]]"

  build_switches:
    - build: "Cheat Cartridge / Plugged In / Damage, Reload"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]]"
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
      bp_use: "default_plp_stationary_dps_build"
    - build: "Extra Credits / Boosted Booster / Damage, Reload"
      source: "[[sources/Fandom-8-Bit|Fandom-8-Bit]]"
      changes_capabilities:
        - "把单次攻击改成 18 束激光，配合 Booster 可对金库或 Boss 型静态目标爆发"
        - "Boosted Booster 把增伤半径扩大到 5 格并把增伤提高到 50%"
      enables:
        - "Heist/Siege 式静态目标爆发"
        - "团队围绕炮台的更大范围火力网"
      mitigates_failure_modes:
        - "team_cannot_stay_inside_small_booster_radius"
      best_when: "敌方难以贴脸且目标是静态安全输出"
      poor_when: "敌方高速进场或需要频繁位移；Extra Credits 卸弹期间很容易被惩罚"
      bp_use: "static_objective_or_team_buff_variant"

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
    - id: "extra_credits_lockout"
      active_when: "8-Bit 使用 Extra Credits 对移动目标或被刺客威胁时"
      exposed_by: "Fandom notes Extra Credits takes three times as long and aim cannot be adjusted"
      mitigation: "只对金库/静态目标使用，或坚持 Cheat Cartridge build"
      bp_use: "build_switch_warning"

  conditional_matchups:
    - target: ["El Primo", "Darryl", "Frank", "Hank", "Draco"]
      direction: "subject_favored"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]]"
      mechanism: "高血量前排必须穿越 8-Bit 的长线和 Booster 增伤区，接近前会被持续 DPS 消耗"
      active_when: "地图开阔、草墙接近路线被清，且 8-Bit 有 Booster 或队友 peel"
      fails_when: "目标用跳跃/滚入/墙草直接贴脸，或队友无法阻止二段进场"
      bp_use: "anti_frontline_on_open_lane"
    - target: ["Poco", "Jae-Yong", "Meg"]
      direction: "subject_favored"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]]"
      mechanism: "Booster 增伤和高持续火力能压过低爆发支援或目标区身体的续航节奏"
      active_when: "战斗是 front-to-back objective fight，8-Bit 队伍有视野和炮台保护"
      fails_when: "支援壳体配上投掷/刺客，或 Meg 机甲/队友先清掉 Booster"
      bp_use: "response_into_low_burst_sustain_shell"
    - target: ["Colt", "Colette", "Bo", "Barley", "Lumi"]
      direction: "target_favored"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]]"
      mechanism: "多弹道/百分比伤害/地雷视野/投掷或区域控制能打慢速 8-Bit，并低成本清炮台"
      active_when: "他们有长线、墙后口袋或目标区位置，8-Bit 必须暴露走位"
      fails_when: "8-Bit 的队伍先开墙、清口袋，并让炮台在射程外安全站住"
      bp_use: "must_answer_range_or_booster_clear"
    - target: ["Edgar", "Sandy", "Bibi"]
      direction: "target_favored"
      source: "[[sources/PLP-8-Bit|PLP-8-Bit]]"
      mechanism: "跳跃、隐蔽/草丛、击退和高速贴脸能绕过长线，惩罚 8-Bit 慢卸弹和慢移速"
      active_when: "地图给草墙接近或最后手确认 8-Bit 缺 peel"
      fails_when: "接近路线开阔、8-Bit 留 Cheat Cartridge，且队友有控制/反刺客"
      bp_use: "avoid_without_peel_or_grass_control"

  slot_notes:
    slot_1: "只在 Heist 长线或可保护炮台的 Gem/Hot Zone 图早手；否则会暴露慢速和炮台清点弱点"
    slot_2_3: "适合围绕 Booster 建立队伍火力核心，再补探草、反投掷和 peel"
    slot_4_5: "看到敌方缺投掷/刺客/多目标清炮台时可补为 DPS 核；需要确认目标转换"
    slot_6: "惩罚低爆发前排或支援壳体，但不能修补队伍缺机动、缺视野或缺清口袋的问题"
```

## 关联页面

- [[sources/Fandom-8-Bit|Fandom 来源摘要: 8-Bit]]
- [[sources/PLP-8-Bit|PLP 来源摘要: 8-Bit]]
