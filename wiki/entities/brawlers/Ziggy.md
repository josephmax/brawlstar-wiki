# Ziggy

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：延迟落雷 / 移动风暴 / 远程 chokepoint 控制

## 来源摘要

- Fandom：[[sources/Fandom-Ziggy|Fandom 来源摘要: Ziggy]]
- PLP：[[sources/PLP-Ziggy|PLP 来源摘要: Ziggy]]
- PLP 推荐模式：Gem Grab、Brawl Ball、Hot Zone、Heist、Bounty、Knockout

## 角色定位总结

Ziggy 是用延迟落雷和超大移动风暴控制路线的 Controller。普攻 `Ta-da!` 可指定 7.33 格内任意区域，包括墙后目标点，0.75 秒后在 1.5 格半径内造成范围伤害；Super `Ziggy's Fantastical Storm` 在 0.2 秒后生成宽 10、射程 13.33 的移动电风暴，造成持续伤害，遇到敌人会减速前进从而延长停留。PLP 默认 `Electric Shuffle / Thunderstruck / Shield, Damage`，强化持续落雷和 Super slow。短板是 3200 HP、几乎没有即时防守，普攻和 Super 都需要预判路线；`Now You See Me...` 传送也要等下一次攻击落雷完成，不能当瞬间 escape。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "long_area; 普攻 7.33 格指定区域，Super 13.33 格 very long"
    projectile_reliability: "medium_on_choke_low_open; 普攻 0.75 秒延迟，Super 轨迹可侧移躲"
    burst: "medium; 普攻 950 范围伤害，Electric Shuffle 连续追加"
    sustained_dps: "medium; 1.8 秒 reload，Electric Shuffle 5 秒内每秒免费落雷"
    objective_damage: "medium_with_storm_or_shuffle; Heist 需固定路线/目标"
    mobility: "medium_with_teleport_variant; 默认无位移，Now You See Me 需等攻击完成后传送"
    survivability: "low; 3200 HP，除传送变体外无逃生/防御"
    engage: "low_medium; 用区域逼位而非身体进场"
    disengage: "low_default_medium_with_teleport; 传送有延迟且会被高爆发惩罚"
    anti_aggro: "medium_if_pre_aimed; 可预判身前/身后落雷和风暴路线，但无硬控"
    anti_tank: "medium; Storm slow + DPS 可压路线 body，但怕直接贴脸"
    wall_break: "none"
    throw_or_wall_bypass: "high_targeted_area; 普攻可指定墙后区域"
    area_control: "very_high; 移动风暴、落雷和 Thunderstruck slow 控 chokepoint"
    scouting_or_vision: "medium; 落雷可检查草/墙后但不持续显形"
    team_support: "medium; slow/区域逼位给队友射线"
    spawnable_or_pet: "storm_area; Super 是持续移动区域，可多 storm 同时存在"
    crowd_control: "medium_with_thunderstruck; Super 命中 slow 20% 1 秒，可重复触发"
    source_trace:
      - "[[sources/Fandom-Ziggy|Fandom-Ziggy]]"
      - "[[sources/PLP-Ziggy|PLP-Ziggy]]"

  build_switches:
    - build: "Electric Shuffle / Thunderstruck / Shield, Damage"
      source: "[[sources/PLP-Ziggy|PLP-Ziggy]]"
      changes_capabilities:
        - "Electric Shuffle 5 秒内每秒对最近可见敌人召唤一次不耗弹药的落雷"
        - "Thunderstruck 让 Super 内敌人 slow 20% 持续 1 秒，并可多次触发"
        - "Shield gear 缓解 3200 HP，Damage gear 提高落雷/风暴惩罚"
      enables:
        - "Hot Zone / Brawl Ball chokepoint slow"
        - "Bounty / Knockout 安全区压迫"
        - "Gem / Heist 远程区域控制"
      mitigates_failure_modes:
        - "delayed_attack_misses_mobile_target"
        - "storm_path_easy_to_leave"
      best_when: "地图有固定入口、窄路、墙后目标或对手必须穿越风暴轨迹"
      poor_when: "敌方高机动刺客可直接贴脸，或开阔图让所有人横向躲 storm"
      bp_use: "default_plp_area_control_build"
    - build: "Now You See Me / The Great Ziggini variant"
      source: "[[sources/Fandom-Ziggy|Fandom-Ziggy]]"
      changes_capabilities:
        - "Now You See Me 让下一次落雷完成后把 Ziggy 传送到该位置"
        - "The Great Ziggini 命中后让下一次普攻 +18% 伤害，miss 会丢失加成"
      enables:
        - "重定位/越墙 endpoint"
        - "命中链伤害节奏"
      mitigates_failure_modes:
        - "no_escape_or_defensive_option"
        - "damage_too_low_without_chain"
      best_when: "传送落点安全且可转 objective 或逃生"
      poor_when: "敌方爆发/眩晕已贴脸，传送需要等待 0.75 秒落雷完成"
      bp_use: "route_reposition_or_damage_chain_variant"

  map_feature_hooks:
    - id: "hot_zone_storm_choke_slow"
      map_feature_type: "zone_choke_storm_slow"
      uses_feature_by: "Super 巨大风暴穿过区口，Thunderstruck 重复 slow 让敌方难以回区"
      route_or_position: "Hot Zone 区口、区内横线、敌方回区路径"
      objective_conversion: "延迟回区、逼敌离开站点、让队友在 slow 中集火"
      active_when: "区口/区内路线固定，敌方必须穿过 storm"
      fails_if: "敌方横向躲出轨迹或从区外投掷/长手清 Ziggy"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.zone_storm_slow"
    - id: "gem_wall_lightning_mine_control"
      map_feature_type: "wall_targeted_mine_control"
      uses_feature_by: "普攻可指定墙后/矿区区域，0.75 秒后打出 1.5 格范围伤害"
      route_or_position: "宝石矿、矿区侧墙、carrier 退线和墙后躲点"
      objective_conversion: "让敌方不能舒服收宝/卡墙，或迫使 carrier 换退线"
      active_when: "路线被墙或 chokepoint 限制，敌方难以在 0.75 秒内脱离"
      fails_if: "敌方高机动横移，或刺客从侧翼逼 Ziggy 后撤"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.wall_targeted_mine_control"
    - id: "brawl_ball_storm_lane_clear"
      map_feature_type: "ball_lane_storm_clear"
      uses_feature_by: "Super 沿球路推进，遇敌减速可延长压迫；普攻可预判门前落点"
      route_or_position: "中场球权、侧路推进线、门前三格或 overtime 直线"
      objective_conversion: "清球路、逼守门人移位、或阻止持球者直线推进"
      active_when: "球路直且敌方必须穿越 storm 或落雷区"
      fails_if: "持球者用 dash/墙绕开，或 Ziggy 无防守工具被先贴脸"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_lane_area_clear"
    - id: "bounty_knockout_delayed_area_pick"
      map_feature_type: "round_area_pick_and_retreat_tax"
      uses_feature_by: "延迟落雷和长距离 storm 可压回合末退线或墙后探头"
      route_or_position: "Bounty 长线、Knockout 墙角、末圈收缩路径"
      objective_conversion: "逼敌离开安全角、保护星/回合优势、或让队友收低血"
      active_when: "敌方退路固定且 Ziggy 有队友保护不被突进"
      fails_if: "目标开阔横移躲雷，或高机动刺客直接越过区域"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Hideout|Hideout]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "candidate_eval.round_delayed_area_pick"

  objective_contracts:
    - mode: "Hot Zone"
      can_fulfill:
        - "Super storm slow 区口"
        - "落雷墙后/区内预判"
        - "Electric Shuffle 追加压力"
      cannot_fulfill:
        - "单人站区 body"
        - "即时硬控突进"
      needs_teammate_support:
        - "站区者、反突进、开阔线输出"
      false_positive: "Ziggy 控区取决于 storm 轨迹，开阔图敌人可横向脱离"
    - mode: "Gem Grab"
      can_fulfill:
        - "墙后矿区落雷"
        - "carrier 退线压迫"
        - "风暴阻断追击/进矿"
      cannot_fulfill:
        - "安全主 carrier"
        - "被刺客贴脸后的自保"
      needs_teammate_support:
        - "主 carrier、视野、peel"
      false_positive: "普攻可打墙后，但 0.75 秒延迟要求目标路线被限制"
    - mode: "Brawl Ball"
      can_fulfill:
        - "storm 清球路"
        - "门前落雷预判"
      cannot_fulfill:
        - "破门"
        - "近身守门硬控"
      needs_teammate_support:
        - "scorer、守门/击退、反刺客"
      false_positive: "没有 knockback/stun，不能独自阻止已贴脸持球者"
    - mode: "Bounty / Knockout"
      can_fulfill:
        - "退线区域压迫"
        - "墙角 delayed pick"
        - "Electric Shuffle 对可见目标追压"
      cannot_fulfill:
        - "开阔对狙"
        - "无保护抗突进"
      needs_teammate_support:
        - "视野、first pick damage、peel"
      false_positive: "落雷不是 hitscan，不能把长射程当稳定 sniper"

  failure_modes:
    - id: "delayed_attack_autoaim_failure"
      active_when: "Ziggy auto-aim 或对高速目标中心点落雷"
      exposed_by: "[[sources/Fandom-Ziggy|Fandom-Ziggy]] tips warn not to auto-aim due to long delay"
      mitigation: "预判路线前/后方，选 choke 或目标必须停留的位置"
      bp_use: "projectile_reliability_gate"
    - id: "storm_trajectory_dodged"
      active_when: "Super 在开阔地直线穿过，敌人可横向离开"
      exposed_by: "Fandom notes Super is powerful but easily dodged by moving out of trajectory"
      mitigation: "只在 choke、目标点、球路或退线使用，配队友限制横移"
      bp_use: "map_choke_requirement"
    - id: "no_default_escape"
      active_when: "刺客/高爆发进入 Ziggy 近身，默认 build 没有逃生或防御"
      exposed_by: "Fandom tips note only Now You See Me provides escape/defense"
      mitigation: "站队友保护内，保 storm/落雷预判进场路径，或选 teleport 变体"
      bp_use: "draft_requires_peel"
    - id: "teleport_delay_vulnerable"
      active_when: "Now You See Me 被当作瞬间 escape 使用"
      exposed_by: "Fandom notes teleport waits for attack delay and is vulnerable to burst/stun"
      mitigation: "在敌人到达前预先启动，确认落点安全"
      bp_use: "mobility_route_gate"

  conditional_matchups:
    - target: ["Meg", "Ruffs", "Lou", "Lola"]
      direction: "subject_favored"
      source: "[[sources/PLP-Ziggy|PLP-Ziggy]]"
      mechanism: "墙后落雷和移动 storm 可迫使中距/阵地英雄离开稳定站位"
      active_when: "目标需要在区口、矿区或墙后站线，且 Ziggy 有安全预判位置"
      fails_when: "目标用长线/队友突进先压 Ziggy，或开阔横移躲 storm"
      bp_use: "area_control_response_to_static_midrange"
    - target: ["Charlie", "Emz", "Otis", "Bea"]
      direction: "subject_favored"
      source: "[[sources/PLP-Ziggy|PLP-Ziggy]]"
      mechanism: "延迟区域和 Thunderstruck slow 压缩控制位站线，让他们难以稳定守 chokepoint"
      active_when: "地图 chokepoint 明确，Electric Shuffle/Storm 可覆盖他们必须经过的位置"
      fails_when: "他们站在开阔长线或由刺客保护 Ziggy 的侧翼"
      bp_use: "choke_control_answer"
    - target: ["Edgar", "Bibi", "Mortis", "Kaze"]
      direction: "target_favored"
      source: "[[sources/PLP-Ziggy|PLP-Ziggy]]"
      mechanism: "高速近身或 burst 能在 0.75 秒落雷和 storm 转化前打掉低血 Ziggy"
      active_when: "他们有草/墙/位移路线并能选择第一接触"
      fails_when: "Ziggy 预判终点且队友提供 knockback/stun 或 bodyguard"
      bp_use: "avoid_without_peel"
    - target: ["Damian", "Sam", "Mico", "Melodie"]
      direction: "target_favored"
      source: "[[sources/PLP-Ziggy|PLP-Ziggy]]"
      mechanism: "墙控/速度 body/越墙跳跃/多段 dash 绕开直线 storm 并惩罚 Ziggy 无防守"
      active_when: "他们能侧绕或端点守住 teleport 路线"
      fails_when: "地图 funnels them through storm and teammates cover Ziggy's endpoint"
      bp_use: "requires_route_lock_and_endpoint_protection"

  slot_notes:
    slot_1: "只有地图 chokepoint 强、队伍有 peel 时可早手；否则会被刺客后手惩罚"
    slot_2_3: "作为区域控制核心时后续必须补站区 body 和反突进"
    slot_4_5: "看到敌方中距阵地/低机动控制时响应价值高"
    slot_6: "最后手可封死固定路线，但不能补硬控、逃生或主输出"
```

## 关联页面

- [[sources/Fandom-Ziggy|Fandom 来源摘要: Ziggy]]
- [[sources/PLP-Ziggy|PLP 来源摘要: Ziggy]]
