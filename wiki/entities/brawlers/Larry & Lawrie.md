# Larry & Lawrie

## 基本信息

- 稀有度：Epic
- 定位：Artillery
- 类型：双段投掷控区 / Lawrie 召唤物经济 / Fall Back 换位续航

## 来源摘要

- Fandom：[[sources/Fandom-Larry-Lawrie|Fandom 来源摘要: Larry & Lawrie]]
- PLP：[[sources/PLP-Larry-Lawrie|PLP 来源摘要: Larry & Lawrie]]
- PLP 推荐模式候选：Brawl Ball, Hot Zone

## 角色定位总结

Larry & Lawrie 的 BP 价值来自两层压力：Larry 用长程越墙 Ticket Dispenser 打双段爆炸封路，3300 基础生命的 Lawrie 以每枚 200 基础伤害的近中距离散射追击、挡枪、骗弹药，并通过 `Protocol: Assist` 给 Larry 回弹。PLP 推荐 `Order: Fall Back / Protocol: Assist`，这意味着 Lawrie 存活且在 8 格内是核心门槛；没有 Lawrie，Larry 只是慢弹道、慢装填的投掷手。Fandom 同时提醒，面对范围伤害近战或能快速清 Lawrie 的突进时，需要保持双人距离，否则 Lawrie 可能被一起打掉。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-07-17
    plp: "[[sources/PLP-Larry-Lawrie|PLP-Larry-Lawrie]]"
    user_notes: none

  capability_vector:
    effective_range: long_thrower; 7.33 格越墙投掷
    projectile_reliability: medium_on_chokes_low_vs_fast_open_movement
    burst: medium_high_if_both_ticket_explosions_or_Lawrie_close_wave_hit; Lawrie 每枚 200 基础伤害，贴近时两段散射可形成明确击杀压力
    sustained_dps: conditional_on_Protocol_Assist_and_Lawrie_hits
    objective_damage: low_medium; 以控区/清人转目标为主
    mobility: medium_with_Order_Fall_Back_swap_if_path_clear
    survivability: medium_low; Larry 3000 HP，Lawrie 3300 HP body 与 Fall Back 双方 25% 治疗共同提供资源层容错
    engage: medium_with_Lawrie_spawn_pressure
    disengage: medium_high_with_Fall_Back_if_not_blocked_by_wall_or_water
    anti_aggro: conditional; Protect variant or Lawrie body can help, area melee is dangerous
    anti_tank: medium_if_route_is_choked; poor_if_tank_reaches_both_twins
    wall_break: none
    throw_or_wall_bypass: very_high
    area_control: high_with_double_explosion_and_Lawrie
    scouting_or_vision: medium; Lawrie seeks enemies including bushes
    team_support: spawnable_body_ammo_tax_and_area_denial
    spawnable_or_pet: Lawrie_3300_HP_body_and_Hypercharge_extra_Lawrie
    crowd_control: route_denial_not_hard_cc
    terrain_destruction: none

  build_switches:
    - build: "Order: Fall Back / Protocol: Assist / Shield, Damage"
      source: "[[sources/PLP-Larry-Lawrie|PLP-Larry-Lawrie]]"
      changes_capabilities:
        - "Order: Fall Back 让 Larry 与 Lawrie 互换位置并各自回复 25% 最大生命，但不能穿墙或过水"
        - "Protocol: Assist 在 Lawrie 8 格内命中敌人时给 Larry 回弹，缓解 very slow reload"
        - "Shield/Damage 提高低血投掷位的容错和击杀阈值"
      enables:
        - "Hot Zone sustained control"
        - "Brawl Ball body and route swap"
        - "spawnable ammo tax"
      mitigates_failure_modes:
        - "slow_reload_without_lawrie"
        - "first_contact_dive_pressure"
      best_when: "地图有墙袋/目标入口，Lawrie 能存活并持续命中或牵制"
      poor_when: "敌方范围近战、刺客或高身体能同时清 Larry 与 Lawrie"
      bp_use: default_lawrie_resource_build
    - build: "Protocol: Protect anti-melee variant"
      source: "[[sources/Fandom-Larry-Lawrie|Fandom-Larry-Lawrie]]"
      changes_capabilities:
        - "Lawrie 在 8 格内时可替 Larry 承受 30% 伤害，降低敌方从攻击 Larry 获得的 Super charge"
      enables:
        - "anti_single_melee_entry"
        - "bodyguard_for_thrower_pocket"
      mitigates_failure_modes:
        - "direct_dive_into_larry"
      best_when: "敌方是单体近战突进而非大范围同时打双人"
      poor_when: "Kenji、Mortis、Edgar、Bibi、Jacky 等范围/链式伤害同时命中 Larry 和 Lawrie"
      bp_use: defensive_variant_into_known_aggro

  map_feature_hooks:
    - map_feature_type: hot_zone_double_burst_lawrie_area_control
      uses_feature_by: "双段投掷覆盖 zone entrance，3300 基础生命 Lawrie 以强化散射逼敌方花弹药或绕路"
      route_or_position: "zone entrance、wall-adjacent zone edge、grass mouth、re-entry choke"
      objective_conversion: "延迟回区、清站区边缘、让队友获得 zone time"
      active_when: "墙体保护 Larry，Lawrie 可在 8 格内命中以触发 Assist"
      fails_if: "敌方从圈外远程清 Larry 或用范围近战同时清双人"
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.spawnable_thrower_zone_control
    - map_feature_type: brawl_ball_lawrie_body_and_fallback_route
      uses_feature_by: "Lawrie 可挡弹/追击门前目标，Order: Fall Back 可换位回血并制造突袭角度"
      route_or_position: "midfield ball、goal-front defender、side grass push、own-goal escape"
      objective_conversion: "延迟持球推进、骗防守弹药、给 scorer 或清球者制造窗口"
      active_when: "换位路径不被墙/水切断，Lawrie 存活且队友能转化球权"
      fails_if: "Fall Back 被地形截断，或敌方高爆发直接秒 Lawrie 后再打 Larry"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
        - Pinball Dreams
      bp_use: slot_task.ball_spawnable_body_and_swap_route
    - map_feature_type: gem_thrower_spawnable_mine_control
      uses_feature_by: "Ticket 双爆压矿区，Lawrie 搜草/吃弹药并威胁追击 carrier"
      route_or_position: "gem mine、center fort doorway、side grass entry、carrier countdown retreat"
      objective_conversion: "阻止收宝、保护 carrier、消耗敌方进矿资源"
      active_when: "Larry 有墙后角度，队友有实际 carrier，Lawrie 不会被免费清"
      fails_if: "Larry 被要求自己拿宝石，或敌方范围伤害把 Lawrie 当弹药补给"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Double Swoosh
      bp_use: map_bp_factors.mine_thrower_spawnable_control
    - map_feature_type: knockout_wall_pocket_order_fallback_bait
      uses_feature_by: "墙后双爆和 Lawrie 诱导敌方预瞄，Fall Back 可在紧急时互换并回血"
      route_or_position: "wall pocket、late-round choke、side bush、low-health retreat"
      objective_conversion: "保护回合 HP lead、逼敌方浪费弹药或从差路线进入"
      active_when: "Lawrie 可安全存在，Larry 不需要穿开阔长线"
      fails_if: "刺客直接越墙/跳入，或投掷镜像从更安全 pocket 清掉 Larry"
      example_maps:
        - Belle's Rock
        - New Horizons
        - Layer Cake
      bp_use: candidate_eval.round_spawnable_thrower_bait

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "ball_route_area_denial"
        - "Lawrie_body_ammo_tax"
        - "Fall_Back_escape_or_angle_shift"
      cannot_fulfill:
        - "primary_scorer"
        - "open_goalkeeper_without_wall"
      needs_teammate_support:
        - "scorer"
        - "anti_dive_or_wall_control"
      false_positive: "Lawrie 能造乱，但进球仍需要队友或清门窗口"
    - mode: "Hot Zone"
      can_fulfill:
        - "zone_entry_thrower_control"
        - "spawnable_ammo_tax"
        - "sustained_reload_with_Assist"
      cannot_fulfill:
        - "durable_zone_body"
      needs_teammate_support:
        - "zone_holder"
        - "anti_aggro_or_range_cover"
      false_positive: "Larry & Lawrie 控区强，但 Larry 本体不能替代站圈身体"
    - mode: "Gem Grab"
      can_fulfill:
        - "mine_entry_denial"
        - "carrier_retreat_pressure"
        - "bush_check_with_Lawrie"
      cannot_fulfill:
        - "primary_gem_carrier"
      needs_teammate_support:
        - "carrier"
        - "peel_for_thrower_pocket"
      false_positive: "PLP 未列 Gem Grab 主推荐，进入 BP 时只能作为地图条件满足后的扩展"

  failure_modes:
    - id: slow_projectile_and_reload_without_lawrie
      active_when: "Lawrie 死亡、离开 8 格或打不到人，Protocol: Assist 无法回弹"
      exposed_by: "[[sources/Fandom-Larry-Lawrie|Fandom-Larry-Lawrie]] attack and Assist mechanics"
      mitigation: "3300 基础生命提高 Lawrie 首轮存活率，但仍把其存活与 8 格距离写入候选门槛，不把 Larry 单体当高持续输出"
      bp_use: resource_tracking.lawrie_alive_and_in_range
    - id: area_melee_hits_both_twins
      active_when: "范围近战或链式突进同时打到 Larry 和 Lawrie，导致 Protect/Assist 资源反噬"
      exposed_by: "[[sources/Fandom-Larry-Lawrie|Fandom-Larry-Lawrie]] Protect tips"
      mitigation: "保持双人间距，或避免在敌方范围近战充足时盲选"
      bp_use: enemy_aggro_filter
    - id: fallback_path_blocked
      active_when: "Order: Fall Back 路径被墙/水截断，换位不能穿越地形"
      exposed_by: "[[sources/Fandom-Larry-Lawrie|Fandom-Larry-Lawrie]] Fall Back mechanics"
      mitigation: "只在直线路径能成立、且换位点不被敌方守住时使用"
      bp_use: route_geometry_check
    - id: thrower_pocket_removed_or_dove
      active_when: "Sam、Edgar、Bibi、Damian、Trunk、Bolt、Rosa、Shade 等通过速度/身体/路线进入 pocket"
      exposed_by: "[[sources/PLP-Larry-Lawrie|PLP-Larry-Lawrie]] counteredBy list"
      mitigation: "补 anti-aggro、墙体保护或后手确认敌方缺直接进入"
      bp_use: must_answer_dive_before_larry_lawrie

  conditional_matchup_seeds:
    - target: Sprout_or_Jae_Yong_or_Ruffs_or_Nani_or_Squeak_or_Mandy_or_Belle_or_Meg
      direction: subject_favored
      source: "[[sources/PLP-Larry-Lawrie|PLP-Larry-Lawrie]]"
      mechanism: "双段投掷和 Lawrie ammo tax 能惩罚固定控制、支援或长线站位，使其先处理召唤物/地面爆炸"
      active_when: "地图有墙袋或目标入口，Lawrie 能存活并逼目标交弹药"
      fails_when: "目标在纯开阔长线输出，或队友先清 Lawrie 后压 Larry"
      bp_use: spawnable_thrower_response_to_static_control
    - target: Sam_or_Edgar_or_Bibi_or_Damian_or_Trunk_or_Bolt_or_Rosa_or_Shade
      direction: target_favored
      source: "[[sources/PLP-Larry-Lawrie|PLP-Larry-Lawrie]]"
      mechanism: "高速身体、突进或范围近战可以越过慢投掷，清掉 Lawrie 并直接攻击 Larry"
      active_when: "地图给草/墙/跳入路线，Larry 缺队友 peel 或 Fall Back 退路"
      fails_when: "入口被双段爆炸锁死，Lawrie 保持距离并由队友补伤害"
      bp_use: must_answer_aggro_before_larry_lawrie
    - target: Area_melee_or_chain_damage
      direction: target_favored
      source: "[[sources/Fandom-Larry-Lawrie|Fandom-Larry-Lawrie]]"
      mechanism: "范围攻击会同时打 Larry 和 Lawrie，使 Protect 伤害转移和 Assist 回弹价值下降"
      active_when: "双人站位过近或目标必须进入同一 choke"
      fails_when: "Larry 保持距离，Lawrie 只作为远端诱饵或队友先控制近战"
      bp_use: spawnable_liability_filter
    - target: Ball_carrier_or_zone_entry
      direction: subject_favored
      source: "[[sources/Fandom-Larry-Lawrie|Fandom-Larry-Lawrie]]"
      mechanism: "双段爆炸、Lawrie 追击和 Fall Back 换位可打断固定球路/回区路线"
      active_when: "目标路线固定且队友能转化球权或 zone time"
      fails_when: "目标高速绕开爆炸，或 Lawrie 被提前清掉"
      bp_use: objective_specific_route_denial

  slot_notes:
    slot_1: "只在地图有稳定墙袋、且敌方清 Lawrie/突进面窄时早手。"
    slot_2_3: "可建立 Hot Zone / Brawl Ball 控区计划，但需要站区身体、scorer 或 anti-dive。"
    slot_4_5: "适合回答固定长手/支援或缺突进阵容，同时避免敌方最后手拿强范围近战。"
    slot_6: "如果敌方三人无法快速清 Lawrie 或进入投掷 pocket，可作为最后手封路和资源税 pick。"
```

## 关联页面

- [[sources/Fandom-Larry-Lawrie|Fandom 来源摘要: Larry & Lawrie]]
- [[sources/PLP-Larry-Lawrie|PLP 来源摘要: Larry & Lawrie]]
