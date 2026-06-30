# Frank

## 基本信息

- 稀有度：Epic
- 定位：Tank
- 类型：高血量控制前排 / 破墙眩晕 / Hot Zone 站圈

## 来源摘要

- Fandom：[[sources/Fandom-Frank|Fandom 来源摘要: Frank]]
- PLP：[[sources/PLP-Frank|PLP 来源摘要: Frank]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Hot Zone

## 角色定位总结

Frank 的 BP 价值来自高血量、受击充 Super、范围穿透普攻和破墙眩晕 Super。他能在墙多、目标拥挤、需要身体站圈或足球破门的地图里把线权转成强控窗口。但他攻击和 Super 都有明显前摇，过程中无法移动，且会被眩晕、拉拽、击退等打断。Frank 不是“血厚就能选”的坦克，而是一个需要控制资源管理和地形状态计划的强窗口英雄。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Frank|Fandom-Frank]] direct_raw_capture_2026-06-30-v2"
    plp: "[[sources/PLP-Frank|PLP-Frank]] direct_raw_capture_2026-06-30"
    user_notes: "按高水平 BP 处理：Frank 必须证明前摇不会被取消、破墙收益大于副作用、站圈/破门能转目标"

  capability_vector:
    effective_range: "中距离 6 格普攻，Super 7 格；范围穿透但需要前摇"
    projectile_reliability: "站稳时覆盖强；高血时普攻前摇长，低血时前摇下降"
    burst: "Irresistible Attraction + 普攻/Super 后接伤害高；Power Grab 击杀后提高输出"
    sustained_dps: "装填很快，但攻击期间 immobile，追击能力受前摇限制"
    objective_damage: "中；不是主 Heist DPS，目标价值主要来自站圈、破门、控人"
    mobility: "基础快但攻击/Super 期间失去移动；Hypercharge 提供速度且普攻延迟最低"
    survivability: "极高生命值；Trait 受击充 Super；Sponge/Health Gear 增强站场"
    engage: "依赖墙草接近、受击充能和队友压线；Super 是强开但可被取消"
    disengage: "弱；开打后靠高血量和控制脱身"
    anti_aggro: "强；近中距离穿透和眩晕惩罚短手贴脸"
    anti_tank: "对短手 body trade 很强，但被百分比伤害、击退和沉默削弱"
    wall_break: "Super 破坏障碍，能开球门/开区域控制点"
    throw_or_wall_bypass: "无越墙攻击；通过 Super 破墙或 Irresistible Attraction 拉墙边目标"
    area_control: "强；普攻/Super 穿透区域和眩晕可封入口"
    scouting_or_vision: "无稳定探草"
    team_support: "Super 眩晕和破墙给队友创造集火、进球或站圈窗口"
    spawnable_or_pet: "无"
    crowd_control: "Super 2 秒眩晕；Irresistible Attraction 拉人，Buffie 版本可减速"
    terrain_creation: "无"
    terrain_destruction: "强；Super 永久破墙并改变地图状态"

  build_switches:
    - build: "Irresistible Attraction / Power Grab / Health + Damage"
      source: "[[sources/PLP-Frank|PLP-Frank]] + [[sources/Fandom-Frank|Fandom-Frank]]"
      changes_capabilities:
        - "Irresistible Attraction 把下一次攻击转成远距离拉人和更高伤害，可在 Super 后补杀或清防守者"
        - "Power Grab 击杀后提高输出，适合 Hot Zone/Brawl Ball 连续站场"
        - "Health/Damage 服务高血量前排和击杀后的滚雪球"
      enables:
        - "Brawl Ball 拉开防守者或破门后得分"
        - "Hot Zone 站圈和入口封锁"
        - "墙多地图惩罚短手/投掷口袋"
      mitigates_failure_modes:
        - "partially_mitigates_target_walks_out_of_range"
        - "partially_mitigates_low_damage_after_stun"
      best_when: "敌方缺可保留给 Frank 的打断，地图目标迫使敌人进中近距离"
      poor_when: "敌方有 Colette/Lou/Shelly/Maisie/Surge/Emz 等持续反坦或打断"
      bp_use: "zone_body_control / brawl_ball_goal_open"
    - build: "Active Noise Canceling / Sponge"
      source: "[[sources/Fandom-Frank|Fandom-Frank]]"
      changes_capabilities:
        - "Active Noise Canceling 让 Frank 在 3.5 秒内免疫眩晕、减速、击退、沉默、定身等多数控制"
        - "Sponge 提升最大生命值，适合开阔或需要强吃伤害的场景"
      enables:
        - "抗打断 Super"
        - "高压站圈"
        - "开阔地图更高容错"
      mitigates_failure_modes:
        - "mitigates_super_cancel_by_common_disruptors"
      best_when: "敌方打断资源很多，但缺持续百分比/远程反坦"
      poor_when: "Frank 主要任务是拉人/补杀，或控制免疫窗口无法覆盖关键 Super"
      bp_use: "anti_cc_super_window"

  map_feature_hooks:
    - id: "brawl_ball_goalpost_break_and_stun"
      map_feature_type: "score_window"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      route_or_position: "球门墙、球门前防守者、中路开局近距离交战"
      objective_conversion: "Super 破门并眩晕防守者，或用 Irresistible Attraction 拉开防守者制造射门空间"
      active_when: "Frank 能在开局/中路充 Super，敌方没有保留打断，破墙后我方更容易进球"
      fails_if: "Super 被取消，破墙后敌方远程/射门线更强，或 Frank 只开墙没有球权跟进"
      bp_use: "slot_task.goal_wallbreak_and_stun"
    - id: "single_zone_stun_body"
      map_feature_type: "zone_presence"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
      route_or_position: "热区入口、圈旁墙体、敌方站圈重叠位置"
      objective_conversion: "高血量站圈吸收火力充 Super，再用眩晕把敌方赶出圈"
      active_when: "入口空间窄、敌方必须近中距离交战，队友能跟 Frank 眩晕集火"
      fails_if: "敌方用 Lou/Emz/Colette 等持续反坦从圈外处理，或 Frank 被打断后无法再进圈"
      bp_use: "map_bp_factors.zone_body_control"
    - id: "wall_dense_ambush_control"
      map_feature_type: "wall_choke_control"
      example_maps:
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Open Business|Open Business]]"
      route_or_position: "墙后伏击口、中心堡垒入口、圈旁低墙"
      objective_conversion: "用墙体缩短接近距离，普攻/Super 穿透 choke 并迫使敌方离开目标点"
      active_when: "墙体帮助 Frank 接近且不急于破掉，敌方无法安全 kite"
      fails_if: "过早 Super 破掉保护墙，让敌方长手接管，或对方有投掷/控制持续封入口"
      bp_use: "terrain_state_plan.keep_or_break_wall"
    - id: "anti_cc_super_window"
      map_feature_type: "resource_window"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      route_or_position: "目标争夺前 3.5 秒 Active Noise Canceling 窗口"
      objective_conversion: "在关键站圈、进球或翻圈时保证 Super 不被打断"
      active_when: "敌方主要答案是击退/眩晕/减速而不是百分比伤害，Frank 能在窗口内触发 Super"
      fails_if: "敌方等免控结束再控，或用 Colette/百分比伤害直接穿过高血量优势"
      bp_use: "resource_tracking.anti_cc_timing"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "goal_wallbreak"
        - "defender_stun"
        - "ball_carrier_body"
      cannot_fulfill:
        - "稳定远程清球"
        - "破墙后自动保证防守"
      needs_teammate_support:
        - "持球/补射/远程接管开放线"
      false_positive: "Frank 能破门，但错误破墙会让敌方更容易射门"
    - mode: "Hot Zone"
      can_fulfill:
        - "zone_body"
        - "zone_clear_stun"
        - "入口封锁"
      cannot_fulfill:
        - "圈外长线消耗"
        - "被多反坦覆盖时单独站圈"
      needs_teammate_support:
        - "跟眩晕集火和处理远程反坦"
      false_positive: "高血量不等于能站圈；如果进圈路径被 slow/百分比伤害覆盖会变成充能资源"
    - mode: "Gem Grab"
      can_fulfill:
        - "侧路身体压迫"
        - "中路 choke 控制"
        - "保护或逼退 gem carrier"
      cannot_fulfill:
        - "高安全度持宝石"
        - "开阔中路长期对枪"
      needs_teammate_support:
        - "稳定 mid、探草和远程补伤害"
      false_positive: "Frank 通常不是宝石位；更适合站前排和控 choke"

  failure_modes:
    - id: "attack_or_super_cancelled"
      active_when: "敌方有眩晕、拉拽、击退、定身、沉默或类似打断资源"
      exposed_by: "[[sources/Fandom-Frank|Fandom-Frank]] 明确普攻/Super 前摇期间被 stun/pull/knockback 会取消"
      mitigation: "使用 Active Noise Canceling 窗口，或等关键打断交出后开 Super"
      bp_use: "must_track_enemy_interrupts"
    - id: "open_map_kited"
      active_when: "长线开阔、缺墙草接近，或敌方远程能边退边消耗"
      exposed_by: "[[sources/Fandom-Frank|Fandom-Frank]] 提示 open map 要谨慎并更依赖 Sponge"
      mitigation: "只在墙多、目标拥挤或需要身体站圈/破门时选"
      bp_use: "map_hard_gate"
    - id: "wallbreak_backfires"
      active_when: "Super 破掉己方接近墙、球门防守墙或让敌方长手获得更好射线"
      exposed_by: "[[sources/Fandom-Frank|Fandom-Frank]] 提示 Brawl Ball 中过度开图会让敌方更容易得分"
      mitigation: "提前定义要破哪面墙、破后谁受益、是否能马上进球"
      bp_use: "terrain_state_plan_check"
    - id: "percent_or_control_anti_tank"
      active_when: "敌方 Colette/Lou/Shelly/Emz/Maisie/Surge 等能持续处理高血量前排"
      exposed_by: "[[sources/PLP-Frank|PLP-Frank]] counteredBy seed + Fandom 反制提醒"
      mitigation: "ban 核心反坦，或把 Frank 放到最后手确认敌方回答不足"
      bp_use: "must_avoid_or_ban_reason"

  conditional_matchup_seeds:
    - target: ["Squeak", "Grom", "Sprout", "Gene", "Penny", "Charlie", "Cordelius", "Ash"]
      direction: "subject_favored"
      source: "[[sources/PLP-Frank|PLP-Frank]]"
      mechanism: "Frank 用高血量顶住中近距离，穿透普攻/Super 眩晕把控制/投掷/短手拉入强控窗口"
      active_when: "地图墙多或目标必须站在 zone/ball/choke 附近，且 Frank 的前摇不会被打断"
      fails_when: "目标从开阔线 kite，或有队友保留打断/反坦处理 Frank"
      bp_use: "zone_or_choke_body_punish"
    - target: ["Colette", "Emz", "Lou", "Shelly", "El Primo", "Maisie", "Surge", "Fang"]
      direction: "target_favored"
      source: "[[sources/PLP-Frank|PLP-Frank]]"
      mechanism: "百分比伤害、减速/冻结、击退、强反坦 burst 或短眩晕能取消 Frank 前摇或让高血量优势失效"
      active_when: "这些英雄保留关键资源给 Frank 的进圈、破门或 Super 前摇"
      fails_when: "Frank 开出 Active Noise Canceling，目标资源已交，或队友先压低/控制反制者"
      bp_use: "must_avoid_or_enemy_response_prediction"
    - target: ["Draco", "Bull", "Sam", "Edgar", "Rosa", "Mortis"]
      direction: "subject_favored"
      source: "[[sources/Fandom-Frank|Fandom-Frank]]"
      mechanism: "近战目标必须进入 Frank 普攻/Super 范围，Frank 高血量、穿透伤害和眩晕会惩罚贴脸"
      active_when: "Frank 有弹药或 Super，敌方不能用位移躲掉前摇"
      fails_when: "对方有护盾/击退/爆发先手，或 Frank 前摇被闪避后遭集火"
      bp_use: "anti_close_range_body_trade"
    - target: ["Shelly", "Buzz", "Gene", "Nani", "Dynamike", "Bull", "Pearl", "Bibi", "Bo", "El Primo"]
      direction: "target_favored"
      source: "[[sources/Fandom-Frank|Fandom-Frank]]"
      mechanism: "这些打断源能在 Frank Super 前摇期间取消强控窗口"
      active_when: "Frank 没有 Active Noise Canceling 或免控窗口与 Super 时机错开"
      fails_when: "打断资源被 bait，或 Frank 先用免控窗口强行开 Super"
      bp_use: "resource_tracking.interrupt_check"

  slot_notes:
    slot_1: "只在 Brawl Ball/Hot Zone 地图强奖励站圈或破门、且核心反坦可 ban 时考虑；否则早手容易被明确反制"
    slot_2_3: "可围绕 Frank 建目标阵容，但必须补远程输出、探草和打断资源追踪"
    slot_4_5: "适合在已知敌方缺 Colette/Lou/Shelly/Maisie/Surge 等答案时补身体和强控"
    slot_6: "最后手可惩罚敌方没有打断/反坦且地图目标拥挤的阵容，要求明确 Super 会转进球、翻圈或击杀"
```

## 关联页面

- [[sources/Fandom-Frank|Fandom 来源摘要: Frank]]
- [[sources/PLP-Frank|PLP 来源摘要: Frank]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
