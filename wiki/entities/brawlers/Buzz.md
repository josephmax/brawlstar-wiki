# Buzz

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：Trait 充能 / 抓钩眩晕刺客

## 来源摘要

- Fandom：[[sources/Fandom-Buzz|Fandom 来源摘要: Buzz]]
- PLP：[[sources/PLP-Buzz|PLP 来源摘要: Buzz]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Heist

## 角色定位总结

Buzz 是常驻 Mythic Assassin。Buzz 的 BP 价值来自 Trait 被动充 Super、10 格抓钩和落地眩晕：他能从墙、草、金库、球路或 carrier 撤退线发起强制接触，并用 `Reserve Buoy` 在关键时刻立即获得一次位移资源。风险也很清晰：普攻只有 2.67 格且 0.9 秒卸弹，抓钩路上不免伤，被击退、眩晕、拉扯等会中断；如果目标有近身爆发、反突进或控制，Buzz 很容易把自己送到对方手里。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-17"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "short_attack_long_engage; 普攻 2.67 格，Super 抓钩 10 格"
    projectile_reliability: "medium; Super 快但远距离横向移动目标会躲，普攻扇形近身稳定"
    burst: "high_if_stun_lands; 5 段 piercing whistle + very fast reload 可在 stun 内击杀脆目标"
    sustained_dps: "medium_high_at_point_blank; 1 秒装填，完整命中两轮五段 whistle 即可重新获得 Super，但必须持续贴身"
    objective_damage: "conditional; Heist 依赖抓 safe 后持续近身输出，不是远程 race"
    mobility: "high_with_super; Fast 基础移速，Super 4500 拉拽速度，可过水/穿越障碍路径"
    survivability: "medium_high_body_low_during_travel; 5000 HP，但抓钩路上不免伤"
    engage: "high; Reserve Buoy 和墙/敌人抓钩提供强制接触，落地后两轮完整普攻可建立下一次 Super 循环；Hypercharge 以当前 30% multiplier 累积"
    disengage: "medium; Reserve Buoy 可逃离或抓墙，但无 stun 的 Gadget Super 用作逃生更安全"
    anti_aggro: "medium_high_with_stun; Tougher Torpedo 可提高近距离 stun，打断敌方进攻"
    anti_tank: "conditional; 长距离 stun 可打坦，但点空或被近身爆发反打风险高"
    wall_break: "none"
    throw_or_wall_bypass: "high_mobility_only; Super 可穿过障碍/水到墙或敌人位置，但不能隔墙输出"
    area_control: "medium; Trait 半径制造隐形压力，X-Ray-Shades 可短时揭草"
    scouting_or_vision: "high_in_bush_maps; Trait 对隐身/草丛敌人充能，Eyes Sharp 扩到 8 格，X-Ray-Shades 共享揭草"
    team_support: "conditional; X-Ray-Shades 给队友 12 秒草丛视野"
    spawnable_or_pet: "none"
    crowd_control: "high_if_super_hits; 0.6-1.5 秒距离缩放眩晕，Tougher Torpedo 提高最低 stun"
    source_trace:
      - "[[sources/Fandom-Buzz|Fandom-Buzz]]"
      - "[[sources/PLP-Buzz|PLP-Buzz]]"

  build_switches:
    - build: "Reserve Buoy / Eyes Sharp / Speed, Damage"
      source: "[[sources/PLP-Buzz|PLP-Buzz]]"
      changes_capabilities:
        - "Reserve Buoy 立即充满 Super，但这次 Super 不眩晕；用于开局 tempo、追残血或逃生"
        - "Eyes Sharp 把 Trait 半径从 6 格扩到 8 格，使草丛/墙后充能和压力范围更大"
        - "Speed gear 支持草图接近，Damage gear 提高 stun 后击杀确认"
      enables:
        - "Gem Grab carrier 压力"
        - "Brawl Ball 抓球路/守门人"
        - "Heist 抓 safe 或防守入侵"
      mitigates_failure_modes:
        - "cannot_start_without_super"
        - "trait_radius_too_small_on_open_maps"
      best_when: "地图有草墙接近、目标路线固定，或敌方后排缺近身反制"
      poor_when: "敌方有多名近身爆发/硬控，或地图完全开阔且 Buzz 无法安全充 Super"
      bp_use: "default_plp_grapple_engage_build"
    - build: "X-Ray-Shades / Tougher Torpedo variants"
      source: "[[sources/Fandom-Buzz|Fandom-Buzz]]"
      changes_capabilities:
        - "X-Ray-Shades 让 Buzz 和队友看到 Trait 半径内草丛敌人 12 秒"
        - "Tougher Torpedo 把最短 stun 从 0.6 秒提高到 1.1 秒，适合近距离反坦/反短手"
      enables:
        - "草图视野税"
        - "近身反突进 stun 确认"
      mitigates_failure_modes:
        - "hidden_bush_entry"
        - "short_distance_stun_too_short"
      best_when: "草丛是地图主路线，或敌方必须近距离接触 Buzz"
      poor_when: "需要 Reserve Buoy 的即时 Super 启动或逃生"
      bp_use: "bush_vision_or_close_stun_variant"

  map_feature_hooks:
    - id: "gem_carrier_trait_and_grapple_pressure"
      map_feature_type: "carrier_route_assassin_pressure"
      uses_feature_by: "Trait 在半径内被动充 Super，抓钩眩晕可打 carrier 或护送者"
      route_or_position: "宝石矿入口、侧草追击路、carrier 倒计时撤退线"
      objective_conversion: "逼 carrier 后撤、强制掉宝或阻止倒计时安全撤退"
      active_when: "草墙让 Buzz 蓄 Trait 或接近，且敌方 carrier 缺近身保镖"
      fails_if: "carrier 旁有 Bull/Chester/Clancy 等近身爆发，或 Tara/Willow 控制守路线"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "map_bp_factors.carrier_assassination_window"
    - id: "brawl_ball_grapple_stun_score_or_disarm"
      map_feature_type: "ball_carrier_stun_and_score_window"
      uses_feature_by: "Super 抓墙/敌人后范围 stun，Reserve Buoy 可补第二次抓钩或逃生"
      route_or_position: "中路球权、侧草推进、球门前防守人或 overtime 开阔路线"
      objective_conversion: "打断持球、清守门人、或抢球后创造射门窗口"
      active_when: "Buzz 有 Super 或 Reserve Buoy，队友能接球/破门/跟伤害"
      fails_if: "球门未打开、敌方击退/控制守门，或 Buzz 抓钩被中断"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.ball_disarm_and_score_window"
    - id: "heist_safe_grapple_and_defender_stun"
      map_feature_type: "safe_grapple_entry"
      uses_feature_by: "Super 可抓 enemy safe 或墙位，近身后 very fast reload 打库；若两轮五段普攻完整命中防守者，可更快接回下一次 Super"
      route_or_position: "金库角、safe 前墙、侧草进库路或敌方基地入口"
      objective_conversion: "把一次 Super 转成 safe DPS 和强制回防"
      active_when: "Buzz 能安全充 Super，敌方基地缺近身爆发或 stun 免疫回答"
      fails_if: "防守者守在落点，Colette/Bull/Chester/Clancy 类低成本反杀，或 race 更快"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Safe Zone|Safe Zone]]"
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
      bp_use: "candidate_eval.heist_entry_damage_with_landing_risk"
    - id: "bush_trait_xray_scouting"
      map_feature_type: "bush_scout_and_hidden_charge"
      uses_feature_by: "Trait 对草内/隐形敌人仍充能，X-Ray-Shades 可揭示半径内草丛给队友"
      route_or_position: "中心大草、侧草球路、热区草边或宝石侧草"
      objective_conversion: "把隐藏伏击转成可预判路线，并让 Buzz 更快获得 Super"
      active_when: "草丛是主要进入路径，队伍需要短时视野而非持续探草专职"
      fails_if: "敌方直接烧草/开墙，或视野需求超过 X-Ray-Shades 12 秒窗口"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.bush_scout_plus_assassin_route"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier 追击和掉宝压力"
        - "侧草威胁和 Trait 充能"
        - "X-Ray-Shades 短时揭草"
      cannot_fulfill:
        - "安全长期 carrier"
        - "正面远程控矿"
      needs_teammate_support:
        - "独立 carrier、开墙/探草延续、反近身保镖"
      false_positive: "Buzz 能杀 carrier，但如果没有后续拾宝和撤退计划，击杀不一定转目标"
    - mode: "Brawl Ball"
      can_fulfill:
        - "抓球路、守门 stun、侧草 scorer 压力"
        - "overtime 抓持球者"
      cannot_fulfill:
        - "稳定破门"
        - "无 Super 正面推进"
      needs_teammate_support:
        - "破门、传球/射门者、反击退控制"
      false_positive: "抓到人不等于能进球；需要球门几何和队友接应"
    - mode: "Heist"
      can_fulfill:
        - "抓 safe 近身输出"
        - "stun 防守者或自家 safe 入侵者"
      cannot_fulfill:
        - "远程持续 safe DPS"
        - "落点被守时强行打库"
      needs_teammate_support:
        - "另一路 race 压力、落点清控、反坦/反 burst"
      false_positive: "Buzz 的 Heist 是入侵窗口，不是无条件打库核心"

  failure_modes:
    - id: "grapple_interrupt_or_landing_burst"
      active_when: "Buzz 抓钩途中或落地时遇到击退、眩晕、拉扯、爆发守点"
      exposed_by: "[[sources/Fandom-Buzz|Fandom-Buzz]] Super interruption and travel vulnerability"
      mitigation: "等控制交掉，抓墙近身而非直接抓移动目标，或保留 Reserve Buoy 逃生"
      bp_use: "engage_hard_gate"
    - id: "short_range_unload_punished"
      active_when: "Buzz 必须点脸输出，而目标有更快近身爆发或 bodyguard"
      exposed_by: "Fandom notes point-blank risk and 0.9 second unload"
      mitigation: "只抓残血/孤立目标，或用 Tougher Torpedo 延长 stun 确认；两轮普攻回 Super 的循环只在五段大多命中时成立"
      bp_use: "candidate_eval.point_blank_risk"
    - id: "super_access_starved_on_open_map"
      active_when: "地图开阔，敌方全程在 Trait 半径外消耗 Buzz"
      exposed_by: "Trait radius and short attack from [[sources/Fandom-Buzz|Fandom-Buzz]]"
      mitigation: "Eyes Sharp、Reserve Buoy、草墙路线，或不在纯开阔图早手"
      bp_use: "map_route_filter"
    - id: "vision_window_is_temporary"
      active_when: "队伍把 X-Ray-Shades 当作持续探草工具"
      exposed_by: "X-Ray-Shades lasts 12 seconds and ends if Buzz dies"
      mitigation: "把它用于进攻前窗口，或另补 Bo/Tara 等长期视野"
      bp_use: "bush_scout_false_positive_filter"

  conditional_matchups:
    - target: ["Mr. P", "Jessie", "Sprout", "Squeak", "Ziggy", "Nani"]
      direction: "subject_favored"
      source: "[[sources/PLP-Buzz|PLP-Buzz]]"
      mechanism: "墙草接近、Reserve Buoy 启动和抓钩 stun 能越过低机动控制/召唤物后排的射线"
      active_when: "目标缺近身 bodyguard，Buzz 能从墙/草/侧路接触"
      fails_when: "召唤物拖住 Buzz，目标有硬控队友，或地图开阔无法充 Super"
      bp_use: "last_pick_or_response_backline_assassin"
    - target: ["Bolt", "Jae-Yong"]
      direction: "subject_favored"
      source: "[[sources/PLP-Buzz|PLP-Buzz]]"
      mechanism: "stun 可以打断路线型或低爆发支援节奏，近身爆发在他们缺 peel 时快速转换"
      active_when: "Buzz 有 Super，目标正在目标路线上或已被队友压低"
      fails_when: "Bolt 有 Unstoppaball/Oil Change 或 Jae-Yong 队友提供硬控和伤害"
      bp_use: "resource_timing_punish"
    - target: ["Chester", "Bull", "Colette", "Clancy"]
      direction: "target_favored"
      source: "[[sources/PLP-Buzz|PLP-Buzz]]"
      mechanism: "近身随机爆发、霰弹、百分比伤害或阶段型反坦 DPS 会惩罚 Buzz 必须贴脸的输出模式"
      active_when: "他们守 carrier、safe、goal 或 Buzz 的抓钩落点"
      fails_when: "关键爆发已交，Buzz 抓另一路孤立目标，或队友先压低血线"
      bp_use: "avoid_as_primary_engage_into_close_counter"
    - target: ["Damian", "Sandy", "Tara", "Willow"]
      direction: "target_favored"
      source: "[[sources/PLP-Buzz|PLP-Buzz]]"
      mechanism: "墙后控制、隐身/沙暴、拉人或控制接管会暴露/打断 Buzz 的进场和撤退"
      active_when: "他们控制草口、目标路或落点，Buzz 必须从可预判方向进场"
      fails_when: "视野先开、控制被 bait，Buzz 用墙抓近身而不是直接抓人"
      bp_use: "requires_vision_and_control_bait"

  slot_notes:
    slot_1: "草墙和目标路线很明确时可早手；纯开阔图早手会被长手和硬控压到无 Super"
    slot_2_3: "适合作为 carrier/球路/safe 入侵计划，需要后续补破门、拾宝或 race"
    slot_4_5: "看到敌方后排缺保镖、缺近身爆发时，Buzz 可作为强制接触回答"
    slot_6: "最适合最后手惩罚无 peel 的控制/长手；不能修补队伍缺远程基本面"
```

## 关联页面

- [[sources/Fandom-Buzz|Fandom 来源摘要: Buzz]]
- [[sources/PLP-Buzz|PLP 来源摘要: Buzz]]
