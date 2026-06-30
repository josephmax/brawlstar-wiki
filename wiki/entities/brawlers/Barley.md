# Barley

## 基本信息

- 稀有度：Rare
- 定位：Artillery
- 类型：越墙铺地、chokepoint 控制、Sticky Syrup 反突进

## 来源摘要

- Fandom：[[sources/Fandom-Barley|Fandom 来源摘要: Barley]]
- PLP：[[sources/PLP-Barley|PLP 来源摘要: Barley]]
- PLP 推荐模式：Brawl Ball、Hot Zone

## 角色定位总结

Barley 是典型低血投掷控场英雄。普攻落地后形成 2 格 puddle，命中和持续站在其中可造成两跳伤害；Super 连续投出 5 个瓶子，覆盖大面积路线和固定目标。PLP 默认 `Sticky Syrup Mixer / Medical Use / Shield, Damage`，把他定位成墙后控区与反突进工具；Heist 场景可按 PLP 注记切 `Extra Noxious` 增加 tick 伤害。BP 中 Barley 的核心不是“远程射手”，而是“墙后安全投掷位能否持续存在”：墙被打开、刺客绕后或 Super 被打断时，他会快速失去价值。

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
    effective_range: "long_thrower; 普攻 7.33 格，Super 9.33 格越墙覆盖"
    projectile_reliability: "medium_on_fixed_routes_low_vs_open_dash; 瓶子落地慢，近距离落更快"
    burst: "medium_if_target_stays_in_puddle; 普攻可两跳，多 puddle 叠加，但不是即时爆发"
    sustained_dps: "medium_area; 2 秒 reload，依赖落点和路线限制"
    objective_damage: "high_heist_if_super_on_safe; safe 可吃普攻两跳和 Super 多跳，Extra Noxious 强化"
    mobility: "low; 无位移"
    survivability: "medium_low; 2700 HP，Medical Use/Shield 缓解但仍怕贴脸"
    engage: "low; 通过封路逼退，不主动开团"
    disengage: "medium_with_sticky_syrup; 自身周围 slow 可拖刺客/坦克"
    anti_aggro: "medium_high_if_gadget_available; Sticky Syrup 4 秒 slow 可防门前/草口突进"
    anti_tank: "medium; 多跳地面伤害和 slow 能逼坦克绕路，贴脸仍危险"
    wall_break: "none"
    throw_or_wall_bypass: "very_high; 普攻和 Super 都可越墙"
    area_control: "very_high; puddle 堆叠、Super 大面积封路"
    scouting_or_vision: "low_medium; 可用瓶子/slow 检草，但无真实 reveal"
    team_support: "medium; Medical Use 自保，Herbal Tonic 可治疗队友但会打断 Super"
    spawnable_or_pet: "none"
    crowd_control: "slow_with_sticky_syrup; 3.33 格半径 4 秒 slow"
    source_trace:
      - "[[sources/Fandom-Barley|Fandom-Barley]]"
      - "[[sources/PLP-Barley|PLP-Barley]]"

  build_switches:
    - build: "Sticky Syrup Mixer / Medical Use / Shield, Damage"
      source: "[[sources/PLP-Barley|PLP-Barley]]"
      changes_capabilities:
        - "Sticky Syrup 在 Barley 身边留下 3.33 格 slow 区，适合阻止 aggro 和 Brawl Ball 门前冲刺"
        - "Medical Use 每次普攻治疗 Barley 10% 最大生命，提高墙后换血续航"
        - "Shield/Damage gear 提高低血投掷位容错和收割伤害"
      enables:
        - "Brawl Ball 门前防守"
        - "Hot Zone 墙后持续控区"
        - "草口/墙角反突进"
      mitigates_failure_modes:
        - "low_health_dive_pressure"
        - "pocket_collapses_after_chip"
      best_when: "墙体保护 Barley，敌方必须穿 chokepoint 或门前入口"
      poor_when: "敌方有多段位移/传送或廉价破墙直接打开投掷位"
      bp_use: "default_plp_control_build"
    - build: "Sticky Syrup Mixer / Extra Noxious / Damage variant"
      source: "[[sources/Fandom-Barley|Fandom-Barley]] / [[sources/PLP-Barley|PLP-Barley]]"
      changes_capabilities:
        - "Extra Noxious 每跳增加 200 伤害，显著提高 Heist safe 和固定目标收益"
        - "保留 Sticky Syrup 处理贴脸者"
      enables:
        - "Heist safe burst"
        - "固定 zone/body 高伤害威胁"
      mitigates_failure_modes:
        - "area_damage_not_converting_to_kill"
        - "safe_damage_too_low"
      best_when: "Barley 能安全把 Super/普攻投到 safe 或固定站位"
      poor_when: "需要 Medical Use 才能在投掷位存活"
      bp_use: "heist_or_damage_conversion_variant"

  map_feature_hooks:
    - id: "hot_zone_wall_puddle_choke_control"
      map_feature_type: "protected_thrower_pocket_zone_choke"
      uses_feature_by: "墙后连续普攻和 Super 覆盖区口，逼敌方绕路或离区"
      route_or_position: "Hot Zone 区口、墙后投掷 pocket、敌方回区 chokepoint"
      objective_conversion: "延迟回区、清站区边缘、保护己方 body 站区"
      active_when: "墙体未被打开，Barley 可安全预铺区口并保留 Sticky Syrup"
      fails_if: "敌方 wall break 打开 pocket，或 Edgar/Mortis/Kenji 等从侧路贴 Barley"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.protected_thrower_zone_control"
    - id: "brawl_ball_sticky_syrup_goal_defense"
      map_feature_type: "goal_choke_slow_and_puddle_defense"
      uses_feature_by: "Sticky Syrup 在门前/草口 slow 持球者，普攻 puddle 迫使掉球后撤"
      route_or_position: "门前窄口、侧草推进线、己方禁区墙后"
      objective_conversion: "拖慢 scorer、让队友补伤、阻断二次进球路线"
      active_when: "球路必须穿过门前窄口且 Barley 有墙后安全位"
      fails_if: "敌方先破门/破墙，或高机动 scorer 绕过 slow 区直接射门"
      example_maps:
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
      bp_use: "slot_task.goal_defense_and_anti_aggro"
    - id: "heist_extra_noxious_super_safe_burst"
      map_feature_type: "fixed_safe_thrower_burst"
      uses_feature_by: "Super 五瓶覆盖 safe，固定目标可吃满多跳；Extra Noxious 增加每跳伤害"
      route_or_position: "safe 前墙、safe 侧投掷角、lane win 后安全投 Super 位置"
      objective_conversion: "把一次 lane win 转换成高额 safe 伤害，同时封防守路线"
      active_when: "Barley 能在不被打断/近身的情况下完整释放 Super"
      fails_if: "Super 被 knockback/pull/stun 打断，或防守者直接处理 Barley"
      example_maps:
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
      bp_use: "candidate_eval.heist_thrower_safe_burst"
    - id: "gem_mine_thrower_pocket_control"
      map_feature_type: "mine_wall_thrower_area_denial"
      uses_feature_by: "墙后 puddle 覆盖矿区和收宝路径，逼宝石拾取者停顿或绕路"
      route_or_position: "宝石矿边墙、侧草入口、carrier 撤退线"
      objective_conversion: "阻止收宝、保护己方 carrier、迫使敌方进入长线队友火力"
      active_when: "矿区墙体保留且敌方缺直接 dive Barley 的路线"
      fails_if: "墙被打开，或敌方长手/投掷从更远角度反压 Barley"
      example_maps:
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.mine_thrower_denial"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "门前 Sticky Syrup slow"
        - "墙后 puddle 防守"
        - "进攻时封 defender 站位"
      cannot_fulfill:
        - "主 scorer"
        - "无墙开阔守门"
      needs_teammate_support:
        - "破门/持球者、反刺客、近身 body"
      false_positive: "Barley 可以防门前窄口，但不是硬控守门员；门被打开后价值下降"
    - mode: "Hot Zone"
      can_fulfill:
        - "墙后控区"
        - "Super 大范围清区"
        - "Sticky Syrup 防突进"
      cannot_fulfill:
        - "单人站区 body"
        - "被长手打开后的正面对枪"
      needs_teammate_support:
        - "站区前排、墙体保护、anti-dive"
      false_positive: "Hot Zone 推荐取决于 protected pocket 是否存在，不是所有区图通用"
    - mode: "Heist"
      can_fulfill:
        - "Super safe burst"
        - "普攻多跳固定目标伤害"
        - "防守近战 safe hitter 的路线"
      cannot_fulfill:
        - "开阔远程 race"
        - "被打断后继续输出"
      needs_teammate_support:
        - "赢线、保护释放 Super、处理 wall break"
      false_positive: "Heist 变体需要 Extra Noxious 和安全投掷角，不是默认 PLP 主模式"

  failure_modes:
    - id: "low_health_dive_pressure"
      active_when: "Edgar、Mortis、Kenji、Sam、Ollie、Bolt 等从草/墙角贴 Barley"
      exposed_by: "[[sources/PLP-Barley|PLP-Barley]] target_favored signals and 2700 HP"
      mitigation: "保留 Sticky Syrup，补队友 peel，不在无墙侧路单站"
      bp_use: "draft_requires_peel"
    - id: "thrower_pocket_opened"
      active_when: "敌方破墙或长手打开 Barley 安全投掷位"
      exposed_by: "Barley value depends on throwing over walls and low HP"
      mitigation: "优先选择稳定墙体地图，或 ban/回答 cheap wall break"
      bp_use: "map_factor_false_positive_filter"
    - id: "super_interrupted_or_misused"
      active_when: "Barley 释放 Super 的 1.5 秒内被 knockback、pull、stun，或用 Herbal Tonic 打断自己"
      exposed_by: "[[sources/Fandom-Barley|Fandom-Barley]] Super interruption and Herbal Tonic interaction"
      mitigation: "在安全墙后或敌方控制空窗释放；使用 Herbal Tonic 时不要覆盖关键 Super 时机"
      bp_use: "super_window_gate"
    - id: "slow_projectile_autoaim_miss"
      active_when: "敌方高速移动或开阔绕路，Barley 自动瞄准只能打一跳甚至落空"
      exposed_by: "Fandom notes slow projectile, closer throws land sooner, auto-aim often misses"
      mitigation: "预判 chokepoint 而非追着移动目标乱投，配控制或站位限制"
      bp_use: "projectile_reliability_gate"

  conditional_matchups:
    - target: ["Jae-Yong", "Sprout", "Poco", "Meg"]
      direction: "subject_favored"
      source: "[[sources/PLP-Barley|PLP-Barley]]"
      mechanism: "Barley 可从墙后持续给支援/阵地位脚下铺 puddle，迫使他们离开治疗、召唤或 body 站位"
      active_when: "目标需要固定站区/支援线，且 Barley 的墙后 pocket 安全"
      fails_when: "Meg/队友直接开墙或用 body 路线压到 Barley 面前"
      bp_use: "thrower_response_to_static_support"
    - target: ["Nani", "Mandy", "Squeak", "Piper"]
      direction: "subject_favored"
      source: "[[sources/PLP-Barley|PLP-Barley]]"
      mechanism: "越墙 puddle 可惩罚长线/延迟输出在墙边卡点，迫使他们离开瞄准线"
      active_when: "地图有墙角让 Barley 能先手投到目标站位"
      fails_when: "目标处于完全开阔长线，Barley 不能接近投掷距离"
      bp_use: "wall_pocket_pressure_into_long_lane"
    - target: ["Edgar", "Trunk", "Sam", "Damian"]
      direction: "target_favored"
      source: "[[sources/PLP-Barley|PLP-Barley]]"
      mechanism: "高机动或高血量 aggro 可穿过 puddle 承受一轮伤害，迫使 Barley 在低血时交 gadget 或阵亡"
      active_when: "他们有草/墙/位移接近路线，Barley 没有队友 peel"
      fails_when: "Sticky Syrup 先锁住入口并由队友跟伤"
      bp_use: "avoid_without_peel_or_slow_route"
    - target: ["Mortis", "Kenji", "Ollie", "Bolt"]
      direction: "target_favored"
      source: "[[sources/PLP-Barley|PLP-Barley]]"
      mechanism: "连续 dash、控制或速度压迫会绕开慢落点，并在 Barley reload/Super 施法时惩罚"
      active_when: "地图侧路开放或 Barley 的墙后位被迫向前"
      fails_when: "他们进场路径经过预铺 puddle/Sticky Syrup，且队友有即时 burst"
      bp_use: "draft_requires_route_lock"

  slot_notes:
    slot_1: "只有在地图明确保留墙后投掷位且敌方难以廉价破墙时才早手"
    slot_2_3: "作为控区层时要同时补 anti-dive；不要让 Barley 独自处理突进"
    slot_4_5: "看到敌方固定支援/长线站位且缺刺客时，Barley 的越墙惩罚价值高"
    slot_6: "最后手适合封死无位移阵地阵容或补 Heist safe burst 变体"
```

## 关联页面

- [[sources/Fandom-Barley|Fandom 来源摘要: Barley]]
- [[sources/PLP-Barley|PLP 来源摘要: Barley]]
