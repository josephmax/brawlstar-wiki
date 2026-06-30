# Jacky

## 基本信息

- 稀有度：Super Rare
- 定位：Tank
- 类型：穿墙近战 / 拉人控球 / 草墙入口前排

## 来源摘要

- Fandom：[[sources/Fandom-Jacky|Fandom 来源摘要: Jacky]]
- PLP：[[sources/PLP-Jacky|PLP 来源摘要: Jacky]]
- PLP 推荐模式候选：Brawl Ball, Hot Zone

## 角色定位总结

Jacky 的 BP 价值来自短距离圆形即时伤害、隔墙打人、Pneumatic Booster 接近和 Super 拉人。她在足球和热区中可以惩罚墙后投掷、草口短手、持球者和站圈目标，但她射程短、装填较慢，面对开阔远程、稳定减速、反坦和更强坦克时会很难接近。Jacky 不是无脑前排，她必须证明路线、墙体、草丛或目标迫使敌人进入她的半径。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Jacky|Fandom-Jacky]] direct_raw_capture_2026-06-30-v2"
    plp: "[[sources/PLP-Jacky|PLP-Jacky]] direct_raw_capture_2026-06-30"
    user_notes: "按高水平 BP 处理：Jacky 必须证明接近路线、墙体利用和目标转化，不按低分局硬冲评估"

  capability_vector:
    effective_range: "短；3.33 格圆形范围，Super 5 格拉人"
    projectile_reliability: "即时圆形伤害，不需要瞄准，可命中身后和墙后一格左右目标"
    burst: "中高；三发主攻击 + Counter Crush 能快速处理低中血目标"
    sustained_dps: "中；装填 1.8 秒较慢，打完一轮后需要撤出或等弹药"
    objective_damage: "低到中；主要不是 Heist safe DPS，而是足球/热区目标控制"
    mobility: "Pneumatic Booster 提供 4 秒 25% 加速，可用于接近、追击、撤退和抢目标"
    survivability: "高血量，Hardy Hard Hat 20% 减伤，Trait 受击充 Super"
    engage: "依赖草墙、墙后压迫、加速和敌方目标位置"
    disengage: "Pneumatic Booster 可撤退，但被 slow/knockback 后撤退质量下降"
    anti_aggro: "强；圆形即时伤害和 Counter Crush 惩罚 Mortis/Edgar 等贴身刺客"
    anti_tank: "不稳定；Fandom 明确提示她通常打不过更强坦克或高爆发反坦"
    wall_break: "无稳定破墙；Rebuild 反向恢复地形"
    throw_or_wall_bypass: "主攻击可穿墙伤害近距离目标，能限制墙后投掷"
    area_control: "中；近身圆形威胁、Super 拉人和 Hypercharge 减速影响入口"
    scouting_or_vision: "Super 拉到草里/隐身目标时可揭示，但不是常态探草"
    team_support: "Super 拉人取消攻击/移动，能给队友范围技能创造集火窗口"
    spawnable_or_pet: "无"
    crowd_control: "Super 拉人并让目标 1 秒无法移动或攻击；Hypercharge 后拉人附带减速"
    terrain_creation: "Rebuild 可恢复 3x3 范围破坏地形"
    terrain_destruction: "无"

  build_switches:
    - build: "Pneumatic Booster / Counter Crush / Shield + Damage"
      source: "[[sources/PLP-Jacky|PLP-Jacky]] + [[sources/Fandom-Jacky|Fandom-Jacky]]"
      changes_capabilities:
        - "Pneumatic Booster 让 Jacky 在短窗口内跨过开口、追击持球者或切墙后目标"
        - "Counter Crush 把受伤的一部分转成圆形反伤，显著提高对刺客/低中血目标的互打能力"
        - "Shield/Damage 提高接近容错和三发击杀阈值"
      enables:
        - "Brawl Ball 持球者拉人/掉球"
        - "Hot Zone 墙边站圈和入口压迫"
        - "隔墙处理投掷或低血后排"
      mitigates_failure_modes:
        - "partially_mitigates_short_range_entry"
        - "partially_mitigates_slow_reload_body_trade"
      best_when: "地图有草墙/墙后目标/足球防守点，敌方缺稳定 slow、反坦和击退"
      poor_when: "地图开阔，敌方有 Shelly/Colette/Otis/Maisie/Gale/Griff 等回答"
      bp_use: "brawl_ball_or_zone_close_range_control"
    - build: "Hardy Hard Hat / Rebuild"
      source: "[[sources/Fandom-Jacky|Fandom-Jacky]]"
      changes_capabilities:
        - "Hardy Hard Hat 常驻减伤，适合更需要承伤接近而不是反伤击杀的场景"
        - "Rebuild 可恢复附近墙、草、障碍，保护接近路线或重建球门/墙后口袋"
      enables:
        - "保持墙体接近路线"
        - "防止己方关键掩体被过度打开"
      mitigates_failure_modes:
        - "mitigates_opened_map_removes_jacky_route"
      best_when: "己方有破墙队友或 overtime，Rebuild 不会让双方都无法处理墙体"
      poor_when: "Jacky 需要依赖加速完成核心接近，或 Rebuild 让队伍失去功能 gadget"
      bp_use: "terrain_state_plan.rebuild_branch"

  map_feature_hooks:
    - id: "brawl_ball_pull_drop_and_score"
      map_feature_type: "score_window"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      route_or_position: "球门前防守者、持球者路线、侧草推进或球门墙后"
      objective_conversion: "Super 拉人让持球者掉球、拖开防守者，或配合传球制造进球"
      active_when: "敌方必须贴近球门/草口防守，Jacky 有 Super 或加速能进半径"
      fails_if: "敌方远程清球不进入 Jacky 半径，或 Jacky 被 slow/knockback 阻止接近"
      bp_use: "slot_task.ball_carrier_displacement"
    - id: "hot_zone_wall_edge_body"
      map_feature_type: "zone_presence"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      route_or_position: "热区入口、圈旁墙边、远圈/本方圈的墙后站位"
      objective_conversion: "利用墙体缩短距离并隔墙打人，拉开或击杀站圈目标"
      active_when: "热区附近有墙体或草口，敌方缺持续区域封锁/反坦，队友能接管站圈"
      fails_if: "敌方只在圈外长线消耗，或区域技能让 Jacky 进圈前被迫交加速撤退"
      bp_use: "map_bp_factors.zone_body_wall_edge"
    - id: "through_wall_thrower_pressure"
      map_feature_type: "wall_pocket_pressure"
      example_maps:
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
      route_or_position: "墙后一格投掷位、低墙口袋、中心堡垒边缘"
      objective_conversion: "主攻击隔墙命中，迫使投掷/低血控制位离开保护墙"
      active_when: "目标需要靠墙保护且无法拉开到 Jacky 半径之外"
      fails_if: "墙太厚或目标保持距离，Jacky 必须穿越开阔区才能接触"
      bp_use: "candidate_eval.anti_thrower_wall_pressure"
    - id: "speed_booster_grass_flank"
      map_feature_type: "grass_route"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      route_or_position: "中心草、侧草通道、宝石侧路或足球突进线"
      objective_conversion: "用加速把草丛威胁转成追击、掉球、逼退 carrier 或抢目标"
      active_when: "草丛未被稳定清扫，敌方缺探草/击退，Jacky 有弹药可打完一轮"
      fails_if: "草被清、入口被 slow 或 Jacky 冲到更强坦克/反坦脸上"
      bp_use: "map_bp_factors.grass_speed_entry"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "ball_carrier_pull_or_drop"
        - "goal_front_body_pressure"
        - "short_range_scorer_with_speed"
      cannot_fulfill:
        - "稳定远程清球"
        - "无路线硬穿开阔图"
      needs_teammate_support:
        - "破门、补射或范围伤害跟拉人"
      false_positive: "Jacky 贴近球门很强，但没有 Super/加速或墙草路线时无法接近"
    - mode: "Hot Zone"
      can_fulfill:
        - "zone_body"
        - "wall_edge_clear"
        - "pull_enemy_out_of_position"
      cannot_fulfill:
        - "圈外远程区域封锁"
        - "独自处理多反坦阵容"
      needs_teammate_support:
        - "远程压血、区域清除或治疗"
      false_positive: "高血量站圈如果无法赶人，只是在给对面充 Super"
    - mode: "Gem Grab"
      can_fulfill:
        - "侧草压迫"
        - "追击/逼退 gem carrier"
        - "墙后投掷惩罚"
      cannot_fulfill:
        - "高安全度中路持宝石"
        - "开阔中线长期对枪"
      needs_teammate_support:
        - "稳定 mid、探草和远程补伤害"
      false_positive: "加速抢宝石不是稳定持宝石方案；Jacky 更适合侧压和反切"

  failure_modes:
    - id: "open_map_outranged"
      active_when: "地图极开阔或目标可一直保持 Jacky 半径外"
      exposed_by: "[[sources/Fandom-Jacky|Fandom-Jacky]] 明确提示 Jacky 不适合极开阔地图"
      mitigation: "只在草墙、球门、热区或墙后目标迫使近身时选"
      bp_use: "map_hard_gate"
    - id: "slow_or_knockback_denies_entry"
      active_when: "敌方有 Bea/Spike/Lou/Emz/Gale/Griff 等 slow、击退或区域反制"
      exposed_by: "[[sources/Fandom-Jacky|Fandom-Jacky]] 提醒 slow 会让 Jacky 无法追击"
      mitigation: "ban 核心反制，或等资源交出后用加速进场"
      bp_use: "must_track_entry_denial"
    - id: "loses_to_heavy_tank_or_anti_tank"
      active_when: "敌方 Bull/El Primo/Rosa/Darryl/Shelly/Colette/Otis/Maisie 等能近身爆发或专门反坦"
      exposed_by: "[[sources/Fandom-Jacky|Fandom-Jacky]] 明确提示 Jacky 通常不能 outmatch other tanks"
      mitigation: "避免正面坦克镜像；只打目标侧的低中血或慢装填英雄"
      bp_use: "must_avoid_or_ban_reason"
    - id: "reload_after_commit"
      active_when: "Jacky 打完三发仍未击杀，或 Super 拉人后没有弹药"
      exposed_by: "[[sources/Fandom-Jacky|Fandom-Jacky]] 提醒使用 Super 前要装满弹药且装填慢"
      mitigation: "进场前确认弹药，拉人后需要队友范围伤害跟进"
      bp_use: "ammo_state_check"

  conditional_matchup_seeds:
    - target: ["Mortis", "Edgar", "Tick", "Dynamike", "Grom", "Poco", "Doug", "Hank"]
      direction: "subject_favored"
      source: "[[sources/PLP-Jacky|PLP-Jacky]]"
      mechanism: "Jacky 的即时圆形伤害、隔墙命中和 Counter Crush 惩罚必须贴身或靠墙输出的低中血目标"
      active_when: "地图有墙草或目标必须进入足球/热区/宝石路线，Jacky 有弹药和接近窗口"
      fails_when: "目标保持距离、被队友保护，或 Jacky 被 slow/反坦资源挡在半径外"
      bp_use: "close_wall_route_punish"
    - target: ["Shelly", "El Primo", "Otis", "Colette", "Maisie", "Gale", "Chester", "Griff"]
      direction: "target_favored"
      source: "[[sources/PLP-Jacky|PLP-Jacky]]"
      mechanism: "爆发反坦、沉默、百分比伤害、击退、控制或高近战 body trade 会让 Jacky 无法完成接近/三发击杀"
      active_when: "这些资源保留给 Jacky 的加速进场或 Super 后窗口"
      fails_when: "资源已交、目标被队友压低，或 Jacky 只需要一次拉人/掉球目标转化"
      bp_use: "must_avoid_or_enemy_response_prediction"
    - target: ["Ball carrier", "Goal defender", "Zone holder"]
      direction: "subject_favored"
      source: "[[sources/Fandom-Jacky|Fandom-Jacky]]"
      mechanism: "Super 拉人取消移动/攻击，Brawl Ball 中持球者被拉会掉球，热区中可把目标拉离站位"
      active_when: "目标必须靠近球门、热区或防守路径，Jacky 能进入 5 格 Super 半径"
      fails_when: "目标远程清球/站圈不进半径，或 Jacky Super 后没有弹药/队友跟伤害"
      bp_use: "objective_specific_displacement"
    - target: ["Bull", "Rosa", "Draco", "Darryl", "Leon", "Nani", "Buzz"]
      direction: "target_favored"
      source: "[[sources/Fandom-Jacky|Fandom-Jacky]]"
      mechanism: "更高爆发、护盾、强近身互打或远程爆发会让 Jacky 在短射程承诺后亏交换"
      active_when: "Jacky 被迫正面互打且没有队友压血或拉人目标收益"
      fails_when: "Jacky 只需守墙角/掉球，或对方资源已交且进入 Counter Crush 半径"
      bp_use: "close_tank_mirror_check"

  slot_notes:
    slot_1: "通常不适合一抢；只有足球/热区地图明确有草墙入口且主要反坦可 ban 时才考虑"
    slot_2_3: "可作为目标计划手，但必须补远程压血、破门/范围跟伤害和反反坦答案"
    slot_4_5: "适合在敌方缺击退/反坦/减速时补足球掉球或热区墙边身体"
    slot_6: "最适合最后手惩罚无反坦、无探草且必须靠墙/靠目标站位的阵容，要求明确进球、翻圈或抓 carrier 方案"
```

## 关联页面

- [[sources/Fandom-Jacky|Fandom 来源摘要: Jacky]]
- [[sources/PLP-Jacky|PLP 来源摘要: Jacky]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
