# Rosa

## 基本信息

- 稀有度：Rare
- 定位：Tank
- 类型：草丛前排 / 护盾目标身体

## 来源摘要

- Fandom：[[sources/Fandom-Rosa|Fandom 来源摘要: Rosa]]
- PLP：[[sources/PLP-Rosa|PLP 来源摘要: Rosa]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Hot Zone

## 角色定位总结

Rosa 是以草丛、护盾和短宽拳击推进目标的前排。Grow Light 能永久制造 3x3 草丛，Plant Life 让她在草中持续回血，Super 提供 4 秒 70% 减伤，Hypercharge 让 Super 周围形成跟随减速圈。她适合草图、目标接触和站圈/持球推进；在开阔 Bounty/Knockout、被破草或被控制/百分比伤害针对时价值急降。

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
    effective_range: "short; 3.67 格三段宽拳，必须维持近身"
    projectile_reliability: "high_in_melee; 宽弧穿透，远距离无威胁"
    burst: "medium; 普攻 unload 1.1 秒，Thorny Gloves/Super 可提高近身伤害"
    sustained_dps: "medium_high_in_range; 1 秒装填，贴身可持续输出"
    objective_damage: "low_medium; 不是 Heist 核心，但能在 Ball/Zone/Gem 用身体转目标"
    mobility: "medium; 770 fast，Speed gear/草丛和 Hypercharge 加速改善接近"
    survivability: "very_high_with_super_or_bush; 5400 HP，Super 70% 减伤，Plant Life 草中回血"
    engage: "medium_high_with_grass; Grow Light/草图/Speed gear 给接近路线"
    disengage: "medium; 草中回血和 Super 可撤，但无 dash"
    anti_aggro: "high_in_close_contact; 护盾和更长近战范围可反打多数刺客，Edgar 等例外要保持距离"
    anti_tank: "medium; Super 可赢近身互殴，但怕百分比伤害和高 DPS"
    wall_break: "none"
    throw_or_wall_bypass: "none"
    area_control: "medium_high; Grow Light 创造草，Unfriendly Bushes 范围探草/减速，Hypercharge 跟随减速圈"
    scouting_or_vision: "medium_with_unfriendly_bushes; 可全图草内揭示/减速敌人"
    team_support: "medium; 用身体挡伤、保护 carrier 或 escort scorer"
    terrain_creation: "high; Grow Light 生成草丛作为路线/回血/伏击地形"
    crowd_control: "conditional; Unfriendly Bushes 和 Hypercharge slow"

  build_switches:
    - build: "Grow Light / Plant Life / Shield, Damage"
      source: "[[sources/PLP-Rosa|PLP-Rosa]]"
      changes_capabilities:
        - "制造草并在草中回血，强化侧路推进和目标身体"
      enables:
        - "Gem Grab carrier/body"
        - "Brawl Ball 持球 walk-in"
        - "Hot Zone 站圈和入口控制"
      mitigates_failure_modes:
        - "open_lane_no_approach"
        - "chip_before_super"
      best_when: "地图已有草或能用 Grow Light 连接目标路线"
      poor_when: "敌方有高效破草、持续控制或百分比伤害"
      bp_use: "default_plp_grass_body_build"
    - build: "Unfriendly Bushes / Thorny Gloves / Speed, Damage"
      source: "[[sources/Fandom-Rosa|Fandom-Rosa]]"
      changes_capabilities:
        - "把 Rosa 从造草 sustain 转为草内探测、减速和 Super 期间击杀"
      enables:
        - "对草图刺客/坦克做反伏击，或在少草地图靠 Super 打短窗口"
      mitigates_failure_modes:
        - "enemy_bush_ambush"
      best_when: "敌方也依赖草，或我方已有足够草但缺探草/减速"
      poor_when: "需要 Grow Light 创造路线，或敌方能远程破草"
      bp_use: "bush_reveal_or_damage_variant"

  map_feature_hooks:
    - id: "grow_light_grass_route_and_sustain"
      map_feature_type: "grass_anchor_creation"
      uses_feature_by: "Grow Light 连接或新建 3x3 草丛，Plant Life/Speed gear 把草变成持续推进路线"
      objective_conversion: "把侧路草线转成中路压力、carrier 撤退或 scorer 接近"
      active_when: "草能连接到目标区且敌方缺持续破草"
      fails_if: "草被 Colt/Brock/Amber/Griff/Frank 等低成本破掉"
      example_maps: ["[[entities/maps/Double Swoosh|Double Swoosh]]", "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]", "[[entities/maps/Sneaky Fields|Sneaky Fields]]", "[[entities/maps/Ring of Fire|Ring of Fire]]"]
      bp_use: "map_bp_factors.grass_route_creation"
    - id: "gem_carrier_or_bodyguard_bush_retreat"
      map_feature_type: "gem_carrier_body"
      uses_feature_by: "高血量、Super 和草中回血让 Rosa 能收宝或保护 carrier 撤退"
      objective_conversion: "把矿区控制和倒计时撤退变成高血量身体任务"
      active_when: "队伍能处理投掷/破草，Rosa 有草或 Super"
      fails_if: "敌方有 Colette/Griff/Clancy 或控制链打断撤退"
      example_maps: ["[[entities/maps/Gem Fort|Gem Fort]]", "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]", "[[entities/maps/Double Swoosh|Double Swoosh]]"]
      bp_use: "Gem Grab body/carrier option"
    - id: "brawl_ball_super_walk_in_score"
      map_feature_type: "score_window_body"
      uses_feature_by: "开 Super 后拿球 walk-in，或 Hypercharge slow 逼守门者失位"
      objective_conversion: "把球权和草线推进转成得分窗口"
      active_when: "球门已开或队友能控/破门，Rosa 可以在 4 秒护盾内接触球门"
      fails_if: "敌方 stuns、pulls、pushbacks、knockbacks 或沉默守门"
      example_maps: ["[[entities/maps/Sneaky Fields|Sneaky Fields]]", "[[entities/maps/Center Stage|Center Stage]]", "[[entities/maps/Triple Dribble|Triple Dribble]]"]
      bp_use: "Brawl Ball front body and scorer escort"
    - id: "hot_zone_shield_body_and_bush_sustain"
      map_feature_type: "zone_body"
      uses_feature_by: "Super 减伤进圈，Plant Life 草中回血，Hypercharge slow 阻止敌方贴身清圈"
      objective_conversion: "把身体时间直接转成 Hot Zone 计分"
      active_when: "热区有草或可用 Grow Light 创造站圈/入口草"
      fails_if: "敌方墙后投掷/百分比伤害/持续控制让 Rosa 无法留在圈内"
      example_maps: ["[[entities/maps/Dueling Beetles|Dueling Beetles]]", "[[entities/maps/Ring of Fire|Ring of Fire]]", "[[entities/maps/Open Business|Open Business]]", "[[entities/maps/Parallel Plays|Parallel Plays]]"]
      bp_use: "Hot Zone primary body with anti-control check"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier、bodyguard、侧草推进和倒计时保护"
      cannot_fulfill:
        - "在开阔无草中长期对枪"
      needs_teammate_support:
        - "破草答案、投掷反制和远程补伤"
      false_positive: "Rosa 当 carrier 需要草/护盾和队友清控制，不是无条件安全"
    - mode: "Brawl Ball"
      can_fulfill:
        - "Super walk-in、scorer escort、草线持球推进"
      cannot_fulfill:
        - "独自处理闭门墙体或多重击退"
      needs_teammate_support:
        - "破门、控人或反 knockback"
      false_positive: "护盾很硬，但 4 秒窗口被击退/拉人就会空掉"
    - mode: "Hot Zone"
      can_fulfill:
        - "站圈、守入口、用草和护盾延长计分"
      cannot_fulfill:
        - "处理所有墙后投掷和百分比伤害"
      needs_teammate_support:
        - "开墙、治疗、反投掷或远程压制"
      false_positive: "只会站住不等于能进圈；入口被控时仍需要队友打开"
    - mode: "Bounty/Knockout"
      can_fulfill:
        - "极少数草墙后手惩罚"
      cannot_fulfill:
        - "常规开阔长线"
      needs_teammate_support:
        - "硬路线和对方缺控制"
      false_positive: "Fandom 明确指出 Rosa 在 Bounty/Knockout 常被长手压制"

  failure_modes:
    - id: "open_lane_no_approach"
      active_when: "地图开阔、草被破或敌方能持续扫草"
      exposed_by: "short range and no dash"
      mitigation: "只在草线/目标接触图选，或队伍提供速度/掩护"
      bp_use: "map_route_gate"
    - id: "bush_break_removes_core"
      active_when: "敌方 Colt/Brock/Amber/Griff/Frank 等破草"
      exposed_by: "Grow Light bushes are destroyed by obstacle-destroying tools"
      mitigation: "后手确认破草工具，或用 Unfriendly/Speed 打短窗口"
      bp_use: "terrain_state_check"
    - id: "cc_displacement_score_denial"
      active_when: "Rosa 准备持球/进圈时被 stun、pull、pushback、knockback 或 silence"
      exposed_by: "Fandom Brawl Ball warning"
      mitigation: "队友先骗控制或 Rosa 等关键技能交掉再开 Super"
      bp_use: "goal_or_zone_resource_check"
    - id: "anti_tank_dps_or_percent_damage"
      active_when: "Colette、Griff、Clancy、Crow 等能穿过护盾窗口或持续削血"
      exposed_by: "PLP counteredBy and Fandom control/low range warnings"
      mitigation: "补远程压制、治疗或选择不同前排"
      bp_use: "avoid_as_only_frontline"

  conditional_matchups:
    - target: ["Jae-Yong", "Poco", "Gus"]
      direction: "subject_favored"
      source: "[[sources/PLP-Rosa|PLP-Rosa]]"
      mechanism: "Rosa 的高身体和护盾能穿过低爆发支援壳，把战斗拖入近身目标接触"
      active_when: "草/墙/目标区让 Rosa 接近，且支援身边缺 anti-tank DPS"
      fails_when: "支援队友有高爆发或控制链保护"
      bp_use: "punish_low_damage_support_shell"
    - target: ["Sprout", "Squeak", "Piper", "Mandy", "Bolt"]
      direction: "subject_favored"
      source: "[[sources/PLP-Rosa|PLP-Rosa]]"
      mechanism: "Grow Light/草线和 Super 可越过 poke 或控制窗口，迫使低血远程/控制位后退"
      active_when: "草未被破，Rosa 能用 Speed/Plant Life 连接到目标"
      fails_when: "地图开阔、草被清，或目标有 knockback/bodyguard"
      bp_use: "grass_route_response_to_range_or_control"
    - target: ["Otis", "Clancy", "Griff", "Colette"]
      direction: "target_favored"
      source: "[[sources/PLP-Rosa|PLP-Rosa]]"
      mechanism: "沉默、成长爆发、反坦 burst 或百分比伤害能在 Rosa 护盾/近身窗口内反打"
      active_when: "Rosa 必须正面进入他们的有效范围"
      fails_when: "他们关键资源交掉，或 Rosa 通过草侧绕只打后排"
      bp_use: "must_answer_anti_tank_before_rosa"
    - target: ["Bibi", "Nita", "Crow", "Damian"]
      direction: "target_favored"
      source: "[[sources/PLP-Rosa|PLP-Rosa]]"
      mechanism: "击退/召唤物/毒伤/墙后控制可阻止 Rosa 持续贴身或站圈"
      active_when: "他们控制草口、球门或 zone 入口"
      fails_when: "Rosa 有 Super、草线和队友清召唤物/控制"
      bp_use: "requires_clear_and_control_bait"

  slot_notes:
    slot_1: "只在明确草图/目标身体图可早手；否则容易被破草和 anti-tank 后手针对"
    slot_2_3: "适合建立 Gem/Ball/Zone 前排计划，后续必须补远程与控制答案"
    slot_4_5: "看到敌方缺破草、缺击退或缺 anti-tank 时最稳"
    slot_6: "可惩罚低伤支援/长手阵容，但要确认路线和目标转化"
```

## 关联页面

- [[sources/Fandom-Rosa|Fandom 来源摘要: Rosa]]
- [[sources/PLP-Rosa|PLP 来源摘要: Rosa]]
