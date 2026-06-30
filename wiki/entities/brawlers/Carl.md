# Carl

## 基本信息

- 稀有度：Super Rare
- 定位：Damage Dealer
- 类型：回旋镐压线 / 机动切入输出

## 来源摘要

- Fandom：[[sources/Fandom-Carl|Fandom 来源摘要: Carl]]
- PLP：[[sources/PLP-Carl|PLP 来源摘要: Carl]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Heist, Bounty

## 角色定位总结

Carl 的 BP 价值来自“单弹药回旋镐 + 墙体缩短回程 + Super 近身旋转”的组合。他能在中长距离用回旋路径消耗，也能用 `Heat Ejector` 或 `Flying Hook` 把路线转换成控路、打库、抢球或收割。`Protective Pirouette` 让 Super 切入更能承伤，但 Carl 的 Super 会被眩晕、击退、拉扯和沉默中断，且面对真正近身爆发时不能把自己当坦克。

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
    effective_range: "long_mid; 8.33 格回旋镐，回程可穿墙命中"
    projectile_reliability: "medium_high_on_lanes; 宽 1.67，墙体回弹可提高循环，但只有一个 ammo"
    burst: "medium_high_with_wall_bounce_or_tailspin; 靠快速回程、Heat Ejector 或 Super 近身"
    sustained_dps: "stateful; ammo 回到手才刷新，墙边/Power Throw 显著提高循环"
    objective_damage: "high_conditional; Heist 靠墙边快速回旋和 Heat Ejector/Super 打库"
    mobility: "medium_high_with_resources; Flying Hook 3000 速度拉到最远点，可过水/绳索；Super 速度翻倍"
    survivability: "medium; 4200 HP，Protective Pirouette 在 Super 中减伤 35%"
    engage: "medium_high_with_flying_hook_or_super; 但需要确认敌方控制已交"
    disengage: "medium; Flying Hook 和 Super 可逃离或转点"
    anti_aggro: "conditional; Heat Ejector 路径和 Super 可惩罚追击，但怕打断"
    anti_tank: "low_medium; 能消耗前排，不能用 Super 贴脸打 Bull/Bibi/Buzz 等爆发体"
    wall_break: "none"
    throw_or_wall_bypass: "medium; 回程可穿墙，Flying Hook 可越水/绳索，但主攻击不能穿墙发出"
    area_control: "medium; Heat Ejector 火路和 Super 火圈/Flamespin 可封路线"
    scouting_or_vision: "low"
    team_support: "lane pressure and route denial"
    spawnable_or_pet: "none"
    crowd_control: "low"
    source_trace:
      - "[[sources/Fandom-Carl|Fandom-Carl]]"
      - "[[sources/PLP-Carl|PLP-Carl]]"

  build_switches:
    - build: "Heat Ejector / Protective Pirouette / Shield, Damage"
      source: "[[sources/PLP-Carl|PLP-Carl]]"
      changes_capabilities:
        - "Heat Ejector 在下一次镐子路径留下持续火路，能封路、打库或惩罚追击"
        - "Protective Pirouette 在 Super 中提供 35% 减伤，降低切入和打库时被秒风险"
        - "Shield/Damage gears 稳定中距离换血和 Super/火路的收割"
      enables:
        - "Heist safe burst 和防守火路"
        - "Brawl Ball 路线封锁"
        - "Gem/Bounty 中距离 lane pressure"
      mitigates_failure_modes:
        - "super_bursted_before_conversion"
        - "enemy_walks_through_lane_without_tax"
      best_when: "地图有墙边快速回旋、safe 角或敌方必须穿过火路"
      poor_when: "敌方有稳定打断 Super 的控制或远程/投掷能让 Carl 无法靠墙循环"
      bp_use: "default_plp_lane_and_heist_build"
    - build: "Flying Hook / Protective Pirouette or Power Throw / Shield, Damage"
      source: "[[sources/Fandom-Carl|Fandom-Carl]]"
      changes_capabilities:
        - "Flying Hook 把下一次攻击变成拉拽位移，可抢球、越水、追后排或逃生"
        - "Power Throw 提高镐子速度，减少回程等待并提高墙边循环"
      enables:
        - "后排惩罚"
        - "Brawl Ball 抢中/转点"
        - "水域或绳索路线绕行"
      mitigates_failure_modes:
        - "cannot_reach_fragile_backline"
        - "needs_escape_from_ambush"
      best_when: "目标缺硬控，或地图给越水/长线拉点收益"
      poor_when: "敌方保留击退/眩晕/爆发守 Carl 落点"
      bp_use: "mobility_punish_variant"

  map_feature_hooks:
    - id: "heist_wall_bounce_heat_ejector_safe_pressure"
      map_feature_type: "safe_wall_bounce_and_fire_lane"
      uses_feature_by: "墙边缩短镐子回程，Heat Ejector 留火，Super/Protective 可在 safe 旁打窗口"
      route_or_position: "safe 旁墙角、金库入口、或敌方防守必须经过的火路"
      objective_conversion: "把 lane win 转成快速 safe DPS 或防守入侵路径税"
      active_when: "Carl 能靠墙循环且敌方无即时打断 Super 的资源"
      fails_if: "墙体被打开后失去快速回程，或 Bull/Bibi/Buzz 类守落点"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
      bp_use: "candidate_eval.heist_wall_bounce_dps"
    - id: "gem_mid_pickaxe_return_wall_angle"
      map_feature_type: "mid_lane_return_angle"
      uses_feature_by: "回旋镐返程可穿墙，墙边反弹缩短 reload 循环"
      route_or_position: "宝石矿侧墙、中心堡垒角、H 草横路或敌方躲墙低血位置"
      objective_conversion: "持续压矿、逼退 side lane，或用返程收残血保护 carrier"
      active_when: "墙体让 Carl 能安全回旋，队伍已有稳定 carrier"
      fails_if: "敌方投掷口袋更深，或刺客从草路贴住 Carl"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "map_bp_factors.mid_lane_return_pressure"
    - id: "brawl_ball_flying_hook_or_fire_route"
      map_feature_type: "ball_route_tempo_and_lane_denial"
      uses_feature_by: "Flying Hook 可快速抢球/转点，Heat Ejector 可封持球路线，Super 可收低血防守者"
      route_or_position: "中路抢球、侧草球路、球门入口或对方防守回撤线"
      objective_conversion: "抢第一球、封住防守路线，或为 scorer 创造短窗口"
      active_when: "队伍有真正 scorer/破门，Carl 负责 tempo 和路线封锁"
      fails_if: "Carl 用 Super 时不能捡球，或敌方击退/眩晕直接中断 Tailspin"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.ball_tempo_and_route_denial"
    - id: "bounty_long_lane_or_hook_punish"
      map_feature_type: "long_lane_with_mobility_punish"
      uses_feature_by: "8.33 格镐子压线，Flying Hook/Super 可惩罚低血长手或逃离危险"
      route_or_position: "Bounty 长线、Knockout 侧路、或少墙开阔 retreat line"
      objective_conversion: "安全消耗拿星，或在目标失位后用 Hook/Super 转击杀"
      active_when: "目标缺打断，Carl 能保持回旋镐距离或最后手进场"
      fails_if: "Gale/Bibi/Buzz/Bo 等控制打断 Super，或纯开阔图被更长线压制"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "candidate_eval.long_lane_plus_interrupt_check"

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - "墙边 quick-cycle safe DPS"
        - "Heat Ejector 打库和防守火路"
        - "Protective Pirouette Super 短窗口"
      cannot_fulfill:
        - "无墙角时稳定远程 race"
        - "强行 Super 进近身爆发守点"
      needs_teammate_support:
        - "开路/压线、反控制、落点保护"
      false_positive: "Carl 的 Heist 依赖墙位和资源时机，不是任意 safe lane 都稳定"
    - mode: "Gem Grab"
      can_fulfill:
        - "中路/边路压线"
        - "返程穿墙收残血"
        - "Flying Hook 追 carrier 或逃生"
      cannot_fulfill:
        - "主 carrier"
        - "独自处理深墙投掷"
      needs_teammate_support:
        - "carrier、探草、反投掷"
      false_positive: "Carl 能压线，但若草/投掷控路失控，单弹药节奏会被打断"
    - mode: "Brawl Ball"
      can_fulfill:
        - "抢球 tempo"
        - "路线封锁和防守消耗"
        - "低血防守者收割"
      cannot_fulfill:
        - "Super 期间持球"
        - "独自破门"
      needs_teammate_support:
        - "scorer、破门/强控、反击退"
      false_positive: "Carl 能快速到球点，但得分仍需要球门几何和队友补位"
    - mode: "Bounty"
      can_fulfill:
        - "长线消耗"
        - "Hook 惩罚无保护后排"
      cannot_fulfill:
        - "无打断检查的强行 Super"
        - "纯狙击镜像"
      needs_teammate_support:
        - "开墙/反投掷、peel、长线补伤"
      false_positive: "Super 追人若被打断会直接送星"

  failure_modes:
    - id: "super_interrupt_by_control"
      active_when: "敌方保留 stun、knockback、pull、silence 或 close-range interrupt"
      exposed_by: "[[sources/Fandom-Carl|Fandom-Carl]] Tailspin interruption list"
      mitigation: "先 bait 控制、用 Protective Pirouette 只承伤不吃控，或避免 Super 进关键目标"
      bp_use: "hard_gate_before_tailspin_engage"
    - id: "single_ammo_tempo_tax"
      active_when: "Carl 镐子飞行太远或被迫离墙，回程慢导致下一次攻击空窗"
      exposed_by: "Pickaxe reloads only when it returns from [[sources/Fandom-Carl|Fandom-Carl]]"
      mitigation: "靠墙缩短回程、Power Throw、或选择中距离站位"
      bp_use: "map_geometry_reliability_check"
    - id: "close_burst_outtrades_tailspin"
      active_when: "Carl 用 Super 贴到 Bull、Bibi、Buzz、Edgar 等高爆发短手"
      exposed_by: "Fandom tips warn against close-range Brawlers during Super"
      mitigation: "只打低血目标，保留 Hook 撤退，队友先消耗或控制"
      bp_use: "avoid_raw_melee_duel"
    - id: "terrain_dependency_flips_after_wallbreak"
      active_when: "Carl 依赖的 safe wall/side wall 被打开或过度破坏"
      exposed_by: "wall-bounce reload and map terrain rules"
      mitigation: "定义要保的墙和要开的墙，避免队友误开关键回旋点"
      bp_use: "terrain_state_plan_check"

  conditional_matchups:
    - target: ["Squeak", "Sprout", "Ziggy", "Mandy", "Piper", "Brock"]
      direction: "subject_favored"
      source: "[[sources/PLP-Carl|PLP-Carl]]"
      mechanism: "长距离回旋镐消耗、返程穿墙和 Flying Hook/Super 可惩罚低机动控制或长手"
      active_when: "目标缺硬控保镖，Carl 有墙角或 Hook 路线"
      fails_when: "目标有深墙口袋、打断队友，或 Carl 进场时被预瞄"
      bp_use: "response_or_last_pick_into_fragile_range"
    - target: ["Poco", "Jae-Yong"]
      direction: "subject_favored"
      source: "[[sources/PLP-Carl|PLP-Carl]]"
      mechanism: "中距离持续消耗和火路可以压低低爆发支援，让其难以安全保护 objective shell"
      active_when: "支援必须站在矿、球路或热区附近，Carl 队友能跟进"
      fails_when: "支援队伍有硬控/前排挡 Super，或 Carl 被投掷逼离墙位"
      bp_use: "support_shell_pressure"
    - target: ["Bolt", "Gale", "Bibi", "Edgar", "Bull"]
      direction: "target_favored"
      source: "[[sources/PLP-Carl|PLP-Carl]]"
      mechanism: "动量接触、击退、近身爆发或高血量短手能打断 Tailspin 或在近身对拼中胜出"
      active_when: "他们守 Carl 的 Super/Hook 落点或目标区入口"
      fails_when: "关键控制已交，Carl 只打低血目标并有 Protective Pirouette"
      bp_use: "requires_interrupt_bait_or_no_tailspin_commit"
    - target: ["Damian", "Trunk", "Shade"]
      direction: "target_favored"
      source: "[[sources/PLP-Carl|PLP-Carl]]"
      mechanism: "墙压、身体或穿墙/特殊路线可绕开 Carl 的回旋节奏，并迫使他在不利距离用 Super"
      active_when: "地图有墙后口袋、草路或短路线，Carl 缺开墙/视野支持"
      fails_when: "口袋被打开，Carl 保持长线 poke 或用 Hook 脱离"
      bp_use: "must_answer_route_or_wall_pressure"

  slot_notes:
    slot_1: "在 Heist 墙角或 Brawl Ball tempo 图可较早建立计划，但要预留反控制/反短手"
    slot_2_3: "适合补中距离 lane pressure 和路线封锁，后续要确认谁负责 carrier/scorer"
    slot_4_5: "看到敌方长手/控制缺打断时可补 Carl，利用 Hook 或 Super 惩罚"
    slot_6: "可最后手抓无保护后排；不能用来解决队伍缺硬反坦或缺持续探草"
```

## 关联页面

- [[sources/Fandom-Carl|Fandom 来源摘要: Carl]]
- [[sources/PLP-Carl|PLP 来源摘要: Carl]]
