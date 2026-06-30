# Tick

## 基本信息

- 稀有度：Super Rare
- 定位：Artillery
- 类型：长程雷区封路 / 回合制消耗 / Last Hurrah 自保

## 来源摘要

- Fandom：[[sources/Fandom-Tick|Fandom 来源摘要: Tick]]
- PLP：[[sources/PLP-Tick|PLP 来源摘要: Tick]]
- PLP 推荐模式候选：Bounty, Knockout

## 角色定位总结

Tick 是低血量、慢装填但极强路线压迫的长程投掷控场。普攻三颗地雷可越墙分散落地，接触或延迟后爆炸；Super 头部会追踪最近敌人，爆炸造成伤害、击退和破墙。Fandom 强调 Tick 适合被动模式、墙多地图、侧线隐藏输出和用地雷逼退敌人，但他血量全游戏最低、reload 很慢，不适合被迫站在开阔区域或独自承担 Hot Zone 计分身体。`Last Hurrah` 和 Super 可以救一次近身接触，但不是让他无条件克制刺客。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Tick|Fandom-Tick]]"
    plp: "[[sources/PLP-Tick|PLP-Tick]]"
    user_notes: none

  capability_vector:
    effective_range: very_long_thrower; 8.67 格普攻且越墙
    projectile_reliability: high_for_area_denial_medium_for_direct_hits; 雷区封路强，直接命中高速目标不稳定
    burst: high_if_multiple_mines_or_head_connect
    sustained_dps: low_medium; 2.4 秒 very_slow reload，Automa-Tick 可略改善
    objective_damage: low_for_heist_race; conditional_fixed_target_or_defense_only
    mobility: low
    survivability: very_low_base_health; Well_Oiled_and_Shield_help_recover_between_peeks
    engage: low; 主要逼位而非主动开团
    disengage: medium_with_Last_Hurrah_or_head_knockback
    anti_aggro: conditional; Headfirst and Last Hurrah punish single close entry if held
    anti_tank: medium_if_tank_must_cross_mines; poor_if_tank_reaches_without_resource_spent
    wall_break: conditional_with_head_explosion
    throw_or_wall_bypass: very_high
    area_control: very_high; mines cover chokes, objectives and retreat lanes
    scouting_or_vision: medium; mines/head can check bushes and nearest hidden target
    team_support: route_denial_and_ammo_tax
    spawnable_or_pet: Super_head_as_temporary_chaser
    crowd_control: knockback_with_head_or_Last_Hurrah
    terrain_destruction: head_explosion_wall_break

  build_switches:
    - build: "Last Hurrah / Well Oiled / Thicc Head, Vision, Shield"
      source: "[[sources/PLP-Tick|PLP-Tick]]"
      changes_capabilities:
        - "Last Hurrah 提供 1 秒左右 50% shield，随后爆炸击退近身目标，是 Tick 对刺客/坦克的关键自保资源"
        - "Well Oiled 让 Tick 更快进入自然回复，适合 Bounty/Knockout 的被动换血"
        - "Thicc Head 提高头部血量，迫使敌方花更多弹药处理追踪头"
        - "Vision/Shield 分别处理草图信息和低血容错"
      enables:
        - "Bounty star lead defense"
        - "Knockout wall_control"
        - "single_entry_self_peel"
      mitigates_failure_modes:
        - "very_low_health"
        - "assassin_first_contact"
      best_when: "地图有墙袋、回合制退线或 chokepoint，Tick 可从安全处持续封路"
      poor_when: "目标要求他自己站圈、过开阔路，或敌方有多突进/破墙连续处理他"
      bp_use: default_round_control_build
    - build: "Mine Mania area-denial variant"
      source: "[[sources/Fandom-Tick|Fandom-Tick]]"
      changes_capabilities:
        - "Mine Mania 下一发六颗地雷，瞬间扩大地面覆盖和 Super/Hypercharge 充能机会"
      enables:
        - "temporary_choke_lock"
        - "gem_or_ball_pickup_denial"
      mitigates_failure_modes:
        - "insufficient_area_coverage_in_one_window"
      best_when: "需要一波封矿、封球或封回区路线，且近身风险较低"
      poor_when: "敌方刺客威胁高，必须保留 Last Hurrah 自保"
      bp_use: area_coverage_variant_when_dive_pressure_is_low

  map_feature_hooks:
    - map_feature_type: bounty_knockout_minefield_wall_control
      uses_feature_by: "长程越墙地雷覆盖 peek 角、退线和缩圈 chokepoint，Headfirst 逼低血目标交弹药"
      route_or_position: "wall pocket、blue-star lane、late-round choke、low-health retreat path"
      objective_conversion: "保护星数/回合血量领先，逼敌方不能安全回复或穿过墙边"
      active_when: "Tick 有墙后安全位，队友能防侧路，敌方不能连续破墙或贴脸"
      fails_if: "纯开放地图让 Tick 暴露，或刺客/破墙者先处理他的 pocket"
      example_maps:
        - Belle's Rock
        - Layer Cake
        - New Horizons
        - Shooting Star
      bp_use: map_bp_factors.round_minefield_control
    - map_feature_type: gem_mine_area_denial_and_carrier_delay
      uses_feature_by: "地雷覆盖矿区、拾宝点和 carrier 撤退线，让敌方拾取/倒计时路线变慢"
      route_or_position: "gem mine、center fort doorway、side grass entry、carrier countdown retreat"
      objective_conversion: "阻止收宝、逼 carrier 走差路线、让队友远程收割"
      active_when: "己方有实际 carrier 或中路身体，Tick 只负责远程封路"
      fails_if: "Tick 被要求自己拿宝石，或敌方从多侧路绕过雷区切后排"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Double Swoosh
      bp_use: map_bp_factors.mine_pickup_denial_not_primary_carrier
    - map_feature_type: brawl_ball_head_or_mine_goal_disruption
      uses_feature_by: "地雷封门前和持球路线，Super 头部可击退防守者/持球者并破部分障碍"
      route_or_position: "midfield ball、goal-front choke、ball landing spot、己方门前防线"
      objective_conversion: "延迟持球推进、逼 defender 交弹药处理头部、给队友射门或清球窗口"
      active_when: "Tick 有墙后安全位且队友负责推进/射门，Mine Mania 或 head 可在关键时机封路线"
      fails_if: "Tick 被迫开放守门，或高机动 scorer 绕过地雷直接射门"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_route_denial_not_primary_scorer
    - map_feature_type: hot_zone_teammate_captures_tick_denies_entry
      uses_feature_by: "Tick 可从圈外用地雷延迟回区和封入口，但计分必须由队友完成"
      route_or_position: "zone entrance、wall-adjacent zone edge、re-entry lane、far-zone approach"
      objective_conversion: "买 zone time、阻止敌方踩点、迫使近战从地雷中穿过"
      active_when: "队友已经能站圈，Tick 有墙后安全位且无需自己长时间暴露在圈内"
      fails_if: "多圈图要求 Tick 自己站区，或 zone 过于开阔让他被长手清掉"
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: false_positive_filter.zone_denial_requires_teammate_body

  objective_contracts:
    - mode: Bounty
      can_fulfill:
        - "long_range_star_lane_denial"
        - "safe_retreat_control"
        - "head_ammo_tax_on_low_health_targets"
      cannot_fulfill:
        - "open_mid_body_under_dive"
      needs_teammate_support:
        - "side_route_peel"
        - "long_range_partner_or_wallbreak_support"
      false_positive: "Tick 能守星数优势，但被开墙或贴脸后会迅速崩盘"
    - mode: Knockout
      can_fulfill:
        - "closed_map_wall_control"
        - "late_round_choke_lock"
        - "anti_single_entry_with_Last_Hurrah_and_head"
      cannot_fulfill:
        - "frontline_duel"
        - "self_peel_against_multiple_divers"
      needs_teammate_support:
        - "peel_or_bodyguard"
        - "vision_on_side_grass"
      false_positive: "Last Hurrah 只覆盖一波；多突进连续进场仍然能打穿 Tick"
    - mode: Gem Grab
      can_fulfill:
        - "mine_pickup_denial"
        - "carrier_retreat_delay"
        - "bush_or_choke_check"
      cannot_fulfill:
        - "primary_gem_carrier"
      needs_teammate_support:
        - "actual_carrier"
        - "anti_aggro_or_mid_body"
      false_positive: "能封矿不等于能拿宝石；低血和慢 reload 会被追击惩罚"
    - mode: Hot Zone
      can_fulfill:
        - "entry_denial_from_cover"
        - "temporary_zone_clear"
      cannot_fulfill:
        - "durable_zone_body"
        - "multi_zone_standing_duty"
      needs_teammate_support:
        - "zone_holder"
        - "peel_and_long_range_cover"
      false_positive: "Fandom 明确指出 Hot Zone 很吃条件；Tick 需要队友计分"

  failure_modes:
    - id: very_low_health_exposure
      active_when: "Tick 被迫离开墙后安全位，或敌方长手/突进直接打到他"
      exposed_by: "[[sources/Fandom-Tick|Fandom-Tick]] lowest health note"
      mitigation: "保持墙后，搭配 peel，不承担正面站点或 carrier"
      bp_use: hard_gate.low_health_positioning
    - id: very_slow_reload_overcommit
      active_when: "Tick 一次性打空所有地雷，之后无法继续封 chokepoint 或防近身"
      exposed_by: "[[sources/Fandom-Tick|Fandom-Tick]] very slow reload and strategy tips"
      mitigation: "分批布雷，保留至少一发或 Super/Last Hurrah 给近身"
      bp_use: resource_tracking.ammo_pacing
    - id: close_range_chase_without_peel
      active_when: "Edgar、Mortis、Leon、Mina 等通过草/墙/速度贴近，Tick 没有 Last Hurrah 或 head"
      exposed_by: "[[sources/PLP-Tick|PLP-Tick]] target_favored list and Fandom chase defense tips"
      mitigation: "保留自保资源，预铺自己脚下/路径，并要求队友覆盖侧路"
      bp_use: draft_requires_peel
    - id: zone_body_false_positive
      active_when: "BP 把 Tick 的封路能力误当成 Hot Zone 站区能力"
      exposed_by: "[[sources/Fandom-Tick|Fandom-Tick]] Hot Zone caveat"
      mitigation: "只有队友能站圈时才把 Tick 计为 entry denial，不计为 zone body"
      bp_use: false_positive_filter.not_zone_body

  conditional_matchup_seeds:
    - target: Poco_or_Chuck_or_Meg_or_Lola_or_Berry_or_Lou_or_Jacky_or_Surge
      direction: subject_favored
      source: "[[sources/PLP-Tick|PLP-Tick]]"
      mechanism: "这些目标若必须守固定 objective 或穿过 chokepoint，会被 Tick 雷区、Headfirst 和 ammo tax 迫使减速或交资源"
      active_when: "地图有墙后投掷位，目标路线固定，Tick 有队友保护侧路"
      fails_when: "目标用速度/路线工具绕开雷区，或其队友先开墙/贴脸处理 Tick"
      bp_use: route_denial_response_to_static_or_objective_targets
    - target: Starr_Nova_or_Damian_or_Edgar_or_Mortis_or_Pearl_or_Mina_or_Leon_or_Brock
      direction: target_favored
      source: "[[sources/PLP-Tick|PLP-Tick]]"
      mechanism: "突进、隐身、速度、强远程或破墙会绕过 Tick 的慢地雷节奏，直接惩罚最低血量"
      active_when: "地图给侧路接近、开墙角度或纯开放长线，Tick 自保资源不足"
      fails_when: "入口被地雷和队友锁死，Last Hurrah/head 留给第一接触"
      bp_use: must_answer_dive_or_wallbreak_before_tick
    - target: Blue_star_or_gem_mine_or_ball_landing_spot
      direction: subject_favored
      source: "[[sources/Fandom-Tick|Fandom-Tick]]"
      mechanism: "Tick 可以把地雷放在模式关键物件或路径上，迫使敌方为了拾取/推进吃伤害或改路线"
      active_when: "目标点固定且敌方必须进入，队友能利用其走位变化"
      fails_when: "敌方可以远程清雷或从另一路绕开目标点"
      bp_use: objective_specific_pickup_denial
    - target: Gene_or_Tara_or_Jacky_pull_or_close_control
      direction: volatile
      source: "[[sources/Fandom-Tick|Fandom-Tick]]"
      mechanism: "Last Hurrah 可推开拉人/近身控制目标，但如果资源被骗或被连续开，Tick 仍会被秒"
      active_when: "Tick 保留 gadget 且敌方只靠单一路线接近"
      fails_when: "拉人后有队友补伤，或 Tick 被迫先交 Last Hurrah"
      bp_use: single_resource_peel_check

  slot_notes:
    slot_1: "只在 Bounty/Knockout 或强墙后封路图可早手；如果敌方后手有多突进/破墙，Tick 会成为明显攻击点。"
    slot_2_3: "可作为回合控制核心，但队伍必须补侧路视野、peel 和至少一个能主动拿击杀的人。"
    slot_4_5: "看到敌方固定 objective 阵容且缺 dive 时，Tick 可封死路线；同时要防敌方最后手拿 Leon/Mortis/Edgar/Brock。"
    slot_6: "最适合惩罚已暴露的无突进、无开墙阵容，用雷区控制回合和目标点。"
```

## 关联页面

- [[sources/Fandom-Tick|Fandom 来源摘要: Tick]]
- [[sources/PLP-Tick|PLP 来源摘要: Tick]]
