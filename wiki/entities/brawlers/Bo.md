# Bo

## 基本信息

- 稀有度：Epic
- 定位：Controller
- 类型：远程压线 / 地雷控区 / 视野税英雄

## 来源摘要

- Fandom：[[sources/Fandom-Bo|Fandom 来源摘要: Bo]]
- PLP：[[sources/PLP-Bo|PLP 来源摘要: Bo]]
- PLP 推荐模式：Gem Grab, Hot Zone, Heist

## 角色定位总结

Bo 的 BP 价值不是单纯“射得远”，而是把入口、草丛、宝石矿、热区或金库路线提前变成有成本的区域。`Snare A Bear` 地雷眩晕、`Super Totem` 充能圈、`Circling Eagle` 探草和 `Tripwire` 主动引爆分别让他在控图、视野、目标伤害和反推进之间切换。风险在于普攻有扫射节奏、地雷有延迟且可被拆，面对高机动、跳跃、瞬移或能绕开地雷的英雄时，控制很容易变成空威胁。

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
    effective_range: "long_mid; 8.67 格普攻和 8.67 格 Super 投放"
    projectile_reliability: "medium; 三箭从左到右扫射，能控线但远距离命中依赖预判"
    burst: "medium_high_if_mines_or_tripwire_connect; 单次地雷 1440，Snare A Bear 可转击杀窗口"
    sustained_dps: "medium; 1.7 秒装填，近中距离三箭全中伤害高"
    objective_damage: "conditional; Heist 依赖地雷/Tripwire 或赢线后持续箭矢"
    mobility: "normal; 无位移，依赖提前布雷和视野"
    survivability: "medium; 3800 HP，靠控制区保护自己"
    engage: "low_medium; 地雷逼位和眩晕能创造 engage，但不是即时突进"
    disengage: "medium; 地雷、击退/眩晕和视野可以保护撤退路线"
    anti_aggro: "high_if_route_predictable; 地雷和视野惩罚草路/入口推进"
    anti_tank: "medium; 地雷眩晕可配队友打坦，但 Bo 自己不是稳定反坦 DPS"
    wall_break: "conditional; 地雷爆炸和 Tripwire 可破坏附近障碍"
    throw_or_wall_bypass: "medium; Super 可越墙布雷，但普攻不能隔墙"
    area_control: "high; 隐形地雷、入口封锁和 Totem 充能区"
    scouting_or_vision: "high_with_circling_eagle_or_vision_gear; 5 格草丛视野能把草路变成公开路线"
    team_support: "medium; Super Totem 为队友 Super 充能，视野共享给全队"
    spawnable_or_pet: "medium; Super Totem 是可被清的团队充能锚点"
    crowd_control: "high_with_snare_a_bear; 地雷改为 2 秒眩晕"
    terrain_destruction: "conditional; 地雷爆炸/Tripwire 可破墙，需避免误开己方掩体"
    source_trace:
      - "[[sources/Fandom-Bo|Fandom-Bo]]"
      - "[[sources/PLP-Bo|PLP-Bo]]"

  build_switches:
    - build: "Super Totem / Snare A Bear / Vision, Shield, Damage"
      source: "[[sources/PLP-Bo|PLP-Bo]]"
      changes_capabilities:
        - "Super Totem 提高 Bo 和队友 Super cycling，适合围绕热区/宝石矿滚资源"
        - "Snare A Bear 把地雷从击退改为 2 秒眩晕，提升击杀确认和入口封锁"
        - "Vision gear 与 Bo 的草丛视野主题叠加，扩大草图信息优势"
      enables:
        - "Gem Grab 宝石矿入口封锁"
        - "Hot Zone 单圈/入口滚雪球"
        - "Heist 中布雷防守或打库窗口"
      mitigates_failure_modes:
        - "mine_delay_allows_escape"
        - "grass_route_blindness"
      best_when: "地图有固定入口、草丛路线或需要队友快速转 Super 的中心目标"
      poor_when: "敌方可飞跃/瞬移/高速变向绕过地雷，或投掷能轻松清 Totem"
      bp_use: "default_plp_control_and_vision_build"
    - build: "Tripwire / Snare A Bear or Circling Eagle / Vision, Damage"
      source: "[[sources/Fandom-Bo|Fandom-Bo]]"
      changes_capabilities:
        - "Tripwire 可主动引爆已放地雷，抢在敌方拆雷或目标经过时转换伤害"
        - "在 Heist 或 Brawl Ball 可用来破墙、开门或打静态目标"
      enables:
        - "Heist safe burst"
        - "Brawl Ball goal barrier transform"
        - "敌方拆雷时的反惩罚"
      mitigates_failure_modes:
        - "enemy_disarms_or_waits_out_mines"
      best_when: "目标位置固定或需要地形转换"
      poor_when: "Tripwire 1.5 秒引爆节奏被敌方预判，或立即引爆只炸到两颗雷"
      bp_use: "terrain_or_static_objective_variant"

  map_feature_hooks:
    - id: "gem_fort_mine_entry_lock"
      map_feature_type: "gem_mine_entrance_blocking"
      uses_feature_by: "三颗隐形地雷和 Snare A Bear 把中心入口变成必须支付的路线成本"
      route_or_position: "宝石矿入口、中心堡垒门口、H 形草带横路或 carrier 撤退路线"
      objective_conversion: "阻止敌方进矿、保护 carrier 倒计时、或眩晕进门者完成击杀"
      active_when: "敌方必须经过少数入口，且 Bo 队友能跟伤害"
      fails_if: "敌方有飞跃/瞬移/召唤物拆雷，或地雷被提前触发后无人跟进"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "map_bp_factors.entrance_trap_and_carrier_protection"
    - id: "hot_zone_choke_mine_totem_cycle"
      map_feature_type: "zone_entry_trap_and_super_cycle"
      uses_feature_by: "地雷封入口，Super Totem 帮 Bo 与队友更快拿到清场/守圈 Super"
      route_or_position: "单圈入口、L 墙支援口袋旁、或敌方必须进圈的 choke"
      objective_conversion: "把入口延迟和眩晕窗口转成站圈时间"
      active_when: "我方已有站圈身体或区域技能，Bo 负责封门和滚资源"
      fails_if: "敌方投掷占墙后口袋清 Totem，或远程从圈外开墙后绕开入口"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "candidate_eval.zone_lock_support"
    - id: "bush_vision_tax_and_lane_safety"
      map_feature_type: "bush_reveal_and_grass_route_denial"
      uses_feature_by: "Circling Eagle 让 Bo 和队友看到 5 格草丛，Vision gear 进一步惩罚草路英雄"
      route_or_position: "中心大草、侧草进攻路、球门前草带或宝石倒计时藏点"
      objective_conversion: "把草丛伏击转成可预瞄路线，保护球权/宝石/站圈"
      active_when: "草丛是地图主路线且敌方依赖隐藏接近"
      fails_if: "草被烧掉后视野价值下降，或敌方不通过草路而用远程/投掷接管"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "required_capabilities.bush_scouting_and_route_denial"
    - id: "tripwire_terrain_or_safe_burst_window"
      map_feature_type: "terrain_transform_and_static_objective_burst"
      uses_feature_by: "Tripwire 主动引爆地雷，可破墙、炸 safe/IKE 或在球门前开路"
      route_or_position: "金库前墙、球门屏障、或敌方防守站位必须踩雷的窄口"
      objective_conversion: "把预埋地雷转成开门、打库或即时防守爆发"
      active_when: "Bo 能安全把雷放到目标附近，且队伍准备利用开墙后的形态"
      fails_if: "过早引爆只触发两颗雷，或开墙后敌方远程反而更受益"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
      bp_use: "terrain_state_plan.tripwire_transform"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "宝石矿入口封锁"
        - "草丛视野税"
        - "倒计时撤退布雷"
      cannot_fulfill:
        - "单独长期 carrier"
        - "无队友跟伤害时靠地雷完成击杀"
      needs_teammate_support:
        - "稳定 carrier、地雷眩晕后的爆发、反投掷"
      false_positive: "有地雷不等于中心可控；敌方若能低成本拆雷或绕路，Bo 的控区会被稀释"
    - mode: "Hot Zone"
      can_fulfill:
        - "入口地雷封锁"
        - "Totem 帮队友滚 Super"
        - "草丛视野与反推进"
      cannot_fulfill:
        - "独自作为主站圈身体"
        - "隔墙清投掷"
      needs_teammate_support:
        - "站圈前排/治疗/开墙或反投掷"
      false_positive: "Bo 能控入口，但 Hot Zone 仍需要实际站圈与清场能力"
    - mode: "Heist"
      can_fulfill:
        - "Tripwire/地雷打库或防入侵"
        - "普攻赢线后打库"
      cannot_fulfill:
        - "远程低承诺稳定打库如纯射手"
        - "快速追击跨线入侵者"
      needs_teammate_support:
        - "开线、安全布雷、反突进"
      false_positive: "Heist 价值取决于地雷是否能接触 safe 或路线，而不是只看普攻 DPS"

  failure_modes:
    - id: "mobile_bypass_or_airborne_ignores_mine_route"
      active_when: "敌方有 Mico、Eve、Mortis、Melodie、Kaze、Mina 等机动/越障路线"
      exposed_by: "[[sources/PLP-Bo|PLP-Bo]] target-favored list and Fandom mine route mechanics"
      mitigation: "把地雷放在落点/目标点而非入口起点，或补即时控制"
      bp_use: "avoid_as_only_anti_mobility"
    - id: "mine_delay_and_disarm_window"
      active_when: "敌方触发后能走出 1.15 秒爆炸半径，或可用召唤物/远程拆雷"
      exposed_by: "[[sources/Fandom-Bo|Fandom-Bo]] mine trigger delay and Tripwire notes"
      mitigation: "Snare A Bear 配队友预瞄，Tripwire 抢敌方拆雷时间"
      bp_use: "candidate_eval.mine_confirmation_check"
    - id: "totem_or_pocket_cleared_by_thrower"
      active_when: "Super Totem 或 Bo 自己站在墙边口袋，被投掷/墙后控制低风险清掉"
      exposed_by: "Super Totem is a 2000 HP decaying spawnable from [[sources/Fandom-Bo|Fandom-Bo]]"
      mitigation: "换 Totem 点、补开墙或让 Bo 只承担视野/布雷职责"
      bp_use: "must_answer_thrower_before_totem_plan"
    - id: "terrain_transform_backfires"
      active_when: "Tripwire/地雷破墙后帮助敌方长手接管，或破坏己方 carrier/站圈掩体"
      exposed_by: "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]] terrain_state checks"
      mitigation: "BP 中先定义要开的墙和后续远程/得分/打库收益"
      bp_use: "terrain_state_plan_check"

  conditional_matchups:
    - target: ["Gray", "Dynamike", "Mandy", "Gene", "Squeak"]
      direction: "subject_favored"
      source: "[[sources/PLP-Bo|PLP-Bo]]"
      mechanism: "地雷封走位、视野税和长中距离三箭能压迫低机动或依赖墙/固定位置的控制与长手"
      active_when: "目标必须经过入口、矿区或热区路线，Bo 的地雷有队友跟伤害"
      fails_when: "目标拥有更深墙后口袋、传送/拉人先手，或 Bo 地雷被提前拆掉"
      bp_use: "control_lane_response_candidate"
    - target: ["Frank", "Jae-Yong", "Gale"]
      direction: "subject_favored"
      source: "[[sources/PLP-Bo|PLP-Bo]]"
      mechanism: "慢前排/低爆发支援/固定推线需要进目标区，Snare A Bear 可把入口接触变成击杀窗口"
      active_when: "地图目标迫使他们靠近矿、圈或球路，并且 Bo 队友有 burst 跟进"
      fails_when: "他们有跳跃/推开/队友开墙保护，或 Bo 的雷只起到逼位不产生击杀"
      bp_use: "objective_entry_trap_punish"
    - target: ["Sam", "Mico", "Mortis", "Melodie", "Kaze", "Mina"]
      direction: "target_favored"
      source: "[[sources/PLP-Bo|PLP-Bo]]"
      mechanism: "高速、跳墙、连段突进或绕位能避开地雷区域，直接贴到 Bo 或后排"
      active_when: "地图有墙草接近、跳点或 Bo 无即时 peel"
      fails_when: "Bo 预埋在落点/目标点，队友持有硬控或反刺客伤害"
      bp_use: "requires_peel_and_route_prediction"
    - target: ["Damian", "Eve"]
      direction: "target_favored"
      source: "[[sources/PLP-Bo|PLP-Bo]]"
      mechanism: "墙后/特殊路线压力让 Bo 的普攻和地雷不容易命中关键目标，且可持续打掉 Totem 或逼退站位"
      active_when: "地图有墙后口袋、水域或侧角度，Bo 队伍缺开墙/远程答案"
      fails_when: "口袋被打开，或 Bo 改用视野/入口布雷而不站在受压位置"
      bp_use: "must_answer_off_angle_or_wall_pressure"

  slot_notes:
    slot_1: "可在草丛/入口价值极高的 Gem/Hot Zone 图早手，但要预留反投掷和反机动"
    slot_2_3: "适合与站圈身体、carrier 或爆发队友组成地雷确认链"
    slot_4_5: "看到敌方缺越障和拆雷资源时补 Bo，能把目标入口变成高成本路线"
    slot_6: "可惩罚低机动目标区阵容；若队伍缺实际输出或缺清投掷，Bo 不能单独修复"
```

## 关联页面

- [[sources/Fandom-Bo|Fandom 来源摘要: Bo]]
- [[sources/PLP-Bo|PLP 来源摘要: Bo]]
