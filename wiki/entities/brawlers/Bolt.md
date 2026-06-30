# Bolt

## 基本信息

- 稀有度：Epic
- 定位：Tank
- 类型：动量接触型坦克 / 路线惩罚英雄

## 来源摘要

- Fandom：[[sources/Fandom-Bolt|Fandom 来源摘要: Bolt]]
- PLP：[[sources/PLP-Bolt|PLP 来源摘要: Bolt]]
- PLP 推荐模式：Bounty

## 角色定位总结

Bolt 的 BP 价值来自“移动蓄速 -> 接触伤害 -> Overdrive 护盾与燃烧轨迹”的路线惩罚。他不是传统射手，也不是普通短手；他的输出要求自己以足够速度撞到敌人。地图必须给他清晰的长路线、少墙/少水的加速空间，或者让 `Bouncy Ball` 的跳墙/破墙能明确打开目标路线。风险同样尖锐：急转、停下、撞墙、水域、减速、击退、眩晕都会切断速度；而且他需要接触敌人才有主要伤害，错误进场会把自己送进对方集火点。

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
    effective_range: "contact_range_with_route; 伤害来自碰撞而非远程普攻"
    projectile_reliability: "not_projectile_based; 可靠性取决于路线、速度和敌方控制资源"
    burst: "medium_high_after_speed_and_ammo; ammo 可让 0.8 秒接触伤害翻倍，但只有 2 格 ammo 且装填很慢"
    sustained_dps: "medium_if_contact_loop_available; 需要持续贴到目标，不适合纯远程消耗"
    objective_damage: "low_medium; 对 safe/zone 的价值来自进场路线和干扰，不是稳定远程 DPS"
    mobility: "stateful_high; 初始 540 very slow，前进 3.5 秒可蓄满速度，Overdrive 加速蓄速"
    survivability: "high_during_overdrive_or_oil_change; 5400 HP，Super 40% 减伤，Oil Change 速度越高盾越厚"
    engage: "high_if_route_clear; 满速、Bouncy Ball 或 Overdrive 能强行接触目标"
    disengage: "medium; Overdrive 燃烧轨迹和 Bouncy Ball 可脱离，但停转会丢速度"
    anti_aggro: "medium_high; Toss Up/轨迹/接触伤害能惩罚追击者，但怕硬控"
    anti_tank: "conditional; Oil Change 可抗前排接触，伤害需要满速和 ammo 支持"
    wall_break: "conditional; Bouncy Ball 落地破坏周围障碍"
    throw_or_wall_bypass: "conditional; Bouncy Ball 可越过墙/水到最近地面，但会失去速度"
    area_control: "medium; Overdrive 轨迹燃烧可以切路线或阻止追击"
    scouting_or_vision: "low"
    team_support: "low; 主要提供路线压力和逼位"
    spawnable_or_pet: "none"
    crowd_control: "conditional; Toss Up 满速击飞，Unstoppaball 在 Super 中免疫负面效果"
    terrain_destruction: "conditional; Bouncy Ball 可打开墙体并改变目标路线"
    source_trace:
      - "[[sources/Fandom-Bolt|Fandom-Bolt]]"
      - "[[sources/PLP-Bolt|PLP-Bolt]]"

  build_switches:
    - build: "Bouncy Ball / Unstoppaball / Health, Damage"
      source: "[[sources/PLP-Bolt|PLP-Bolt]]"
      changes_capabilities:
        - "Bouncy Ball 提供短跳、落地范围伤害和破墙，但激活时会清空速度"
        - "Unstoppaball 让 Super 期间免疫控制并提高最高速度，修复 Bolt 最怕 CC 的一部分弱点"
        - "Health/Damage gears 支持回退再进场和接触伤害转化"
      enables:
        - "Bounty 蓝星/长路线压迫"
        - "越墙收残血或打开关键掩体"
        - "Super 期间穿过控制路线"
      mitigates_failure_modes:
        - "cc_stops_momentum"
        - "wall_blocks_route"
      best_when: "地图少墙少水或有一面关键墙值得用 Bouncy Ball 换速度打开"
      poor_when: "敌方有多段击退/减速/束缚，或地图需要稳定远程输出而非接触进场"
      bp_use: "default_plp_route_engage_build"
    - build: "Oil Change / Unstoppaball or Toss Up / Health, Shield"
      source: "[[sources/Fandom-Bolt|Fandom-Bolt]] / [[sources/PLP-Bolt|PLP-Bolt]]"
      changes_capabilities:
        - "Oil Change 按当前速度给 2000-4000 护盾，适合冲入松散人群或带球前使用"
        - "Toss Up 在满速接触时击飞，适合敌方缺硬控的短路线"
      enables:
        - "抗坦/抗集火进场"
        - "Brawl Ball 持球前护盾"
        - "路线反追击"
      mitigates_failure_modes:
        - "dies_before_contact"
      best_when: "需要穿过一段火力才能完成接触，或 PLP notes 提醒要用 Gadget 1 打坦"
      poor_when: "敌方百分比伤害、持续控制或击退链能让护盾只变成对方充能"
      bp_use: "tank_contact_variant"

  map_feature_hooks:
    - id: "bounty_open_route_blue_star_and_contact_pressure"
      map_feature_type: "open_route_momentum"
      uses_feature_by: "移动蓄 Super、蓄速度和 Overdrive 让 Bolt 可快速抢中线或逼退孤立长手"
      route_or_position: "蓝星路、开阔中线、少墙长路线或敌方后撤线"
      objective_conversion: "抢蓝星、逼退低机动目标、或在领先后用燃烧轨迹阻止追击"
      active_when: "路线直、墙水少，敌方缺立即击退/减速/眩晕"
      fails_if: "Bolt 需要急转、撞墙或被控制打断速度，或敌方全程保持远程交叉火力"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
      bp_use: "candidate_eval.open_route_contact_pressure"
    - id: "bouncy_ball_wall_break_or_finish_route"
      map_feature_type: "wall_break_transform_with_momentum_reset"
      uses_feature_by: "Bouncy Ball 越墙/破墙并造成落地伤害，但用完会失去全部速度"
      route_or_position: "中心掩体、目标墙角、球门屏障或投掷口袋边缘"
      objective_conversion: "打开射线、收残血、拆投掷口袋或创造队友后续输出路线"
      active_when: "被破的墙会立刻带来远程/得分/击杀收益，且 Bolt 落地不会被集火"
      fails_if: "破墙后敌方远程更受益，或 Bolt 失速后被反杀"
      example_maps:
        - "[[entities/maps/New Horizons|New Horizons]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
      bp_use: "terrain_state_plan.bouncy_ball_transform"
    - id: "hot_zone_overdrive_trail_entry_tax"
      map_feature_type: "zone_entry_trail_denial"
      uses_feature_by: "Overdrive 4 秒 40% 减伤并留下燃烧轨迹，能在入口或圈边切断追击路线"
      route_or_position: "单圈入口、zone 边缘绕圈路线、或墙边必须穿过的 choke"
      objective_conversion: "让敌方进圈路径付出燃烧/位移成本，为队友站圈争取时间"
      active_when: "Bolt 已有 Super，队友能站圈，敌方必须穿越他的轨迹进入目标"
      fails_if: "敌方有远程/投掷从圈外清人，或 CC 在 Super 前就打断 Bolt"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "candidate_eval.zone_entry_disruption_not_primary_body"
    - id: "brawl_ball_speed_mid_and_shield_score_window"
      map_feature_type: "ball_route_speed_and_body"
      uses_feature_by: "高速度可快速到中路，Oil Change 可在带球或冲门前吸收伤害"
      route_or_position: "中路抢球、侧草持球路线、或球门前破墙后的直线推进"
      objective_conversion: "抢第一球、制造持球推进或逼防守交控制"
      active_when: "队伍已有破门/控人，Bolt 不需要在持球后保持满速长期运球"
      fails_if: "持球速度上限降低、球门未打开、或敌方击退/眩晕守门"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.ball_tempo_body_with_cc_check"

  objective_contracts:
    - mode: "Bounty"
      can_fulfill:
        - "抢蓝星和开阔路线压迫"
        - "用 Overdrive 轨迹保护领先后撤"
        - "最后手惩罚无 CC 的孤立长手或墙后控制"
      cannot_fulfill:
        - "稳定远程换血"
        - "无路线时低风险拿星"
      needs_teammate_support:
        - "远程基本面、开墙、或控制资源引导 Bolt 接触"
      false_positive: "PLP 推荐 Bounty 不等于 Bolt 是狙击；必须证明接触路线和生存撤退"
    - mode: "Brawl Ball"
      can_fulfill:
        - "中路抢球节奏"
        - "护盾/速度推进"
        - "Bouncy Ball 破门或越墙收人"
      cannot_fulfill:
        - "独自稳定破门和射门"
        - "在持球减速后继续靠满速伤害解决防守"
      needs_teammate_support:
        - "破门、击退/眩晕、或真正 scorer"
      false_positive: "速度高不等于得分路径成立；球门几何和 CC 仍是硬门槛"
    - mode: "Hot Zone"
      can_fulfill:
        - "入口干扰和燃烧轨迹封路"
        - "对无控制后排的短窗口清场"
      cannot_fulfill:
        - "长时间单独站圈"
        - "墙后投掷清场"
      needs_teammate_support:
        - "站圈身体、治疗/清投掷、反控制"
      false_positive: "Bolt 能冲圈但不等于能站住；他更像扰乱入口的路线手"

  failure_modes:
    - id: "momentum_loss_from_walls_water_or_turns"
      active_when: "路线需要急转、撞墙、穿过水域边缘或频繁停走"
      exposed_by: "[[sources/Fandom-Bolt|Fandom-Bolt]] speed trait and tips"
      mitigation: "只在直线路线或已开墙状态下锁定，提前定义进出路线"
      bp_use: "map_route_hard_gate"
    - id: "cc_stops_contact_plan"
      active_when: "敌方持有 slow、stun、knockback、pull、Cocoon 或硬位移"
      exposed_by: "Fandom tips warn slows, stuns, knockbacks thwart charge; Unstoppaball only works during Super"
      mitigation: "用 Unstoppaball 进场、等待控制交掉，或把 Bolt 放到最后手"
      bp_use: "must_bait_or_ban_cc"
    - id: "contact_damage_requires_commitment"
      active_when: "Bolt 必须撞进敌方队伍才能输出，而队友无法跟进"
      exposed_by: "Fandom attack notes damage occurs on hitbox contact"
      mitigation: "只撞孤立目标、保留 Overdrive/Oil Change，或让队友先压低目标"
      bp_use: "candidate_eval.commitment_risk"
    - id: "bouncy_ball_speed_reset_backfires"
      active_when: "Bouncy Ball 为越墙/破墙清空速度后，Bolt 落在敌方射程内"
      exposed_by: "Fandom Bouncy Ball notes speed is lost on activation"
      mitigation: "只用于确定击杀、逃生或有队友立即利用的开墙"
      bp_use: "terrain_transform_false_positive_filter"

  conditional_matchups:
    - target: ["Grom", "Mr. P", "Squeak", "Lumi"]
      direction: "subject_favored"
      source: "[[sources/PLP-Bolt|PLP-Bolt]]"
      mechanism: "速度进场、Bouncy Ball 越墙和 Overdrive 轨迹能惩罚低机动墙控/召唤物控制目标"
      active_when: "目标没有近身保镖，Bolt 能从侧路或破墙点直接接触"
      fails_when: "目标有更深墙后保护、召唤物挡路，或 Bolt 失速后被反打"
      bp_use: "last_pick_or_response_into_unprotected_control"
    - target: ["Buster", "Frank", "Leon", "Carl"]
      direction: "subject_favored"
      source: "[[sources/PLP-Bolt|PLP-Bolt]]"
      mechanism: "接触伤害和 Super 免控/减伤可以绕过部分 projectile screen 或惩罚需要站位蓄力/固定路线的目标"
      active_when: "Bolt 已有速度或 Super，目标关键控制已交，队友能跟进接触后的伤害"
      fails_when: "Buster/Frank 等保留拉人、击退或队友集火，Leon 从隐身先手"
      bp_use: "resource_timing_contact_duel"
    - target: ["Gale", "Charlie", "Buzz", "Willow"]
      direction: "target_favored"
      source: "[[sources/PLP-Bolt|PLP-Bolt]]"
      mechanism: "击退、Cocoon、眩晕/钩锁或控制接管能在 Bolt 接触前后打断路线"
      active_when: "他们守住 Bolt 必须经过的 choke、球路或 Bounty 接触线"
      fails_when: "控制被 bait，Bolt 在 Unstoppaball 期间进场，或队友从另一路分散控制"
      bp_use: "avoid_without_cc_bait_plan"
    - target: ["Clancy", "Rosa", "Melodie", "Meg"]
      direction: "target_favored"
      source: "[[sources/PLP-Bolt|PLP-Bolt]]"
      mechanism: "高身体、稳定 DPS、草路盾量或多段位移能吃住 Bolt 第一轮接触并反杀失速点"
      active_when: "目标区迫使 Bolt front-to-back 撞身体，且他没有 Oil Change/Super 资源"
      fails_when: "Bolt 绕开身体直接撞后排，或队友先削弱目标血线"
      bp_use: "avoid_raw_frontline_answer"

  slot_notes:
    slot_1: "不适合盲早手；除非地图路线极清楚且敌方已暴露缺 CC，否则容易被控制和地形低成本回答"
    slot_2_3: "可作为 Bounty 开路线计划的一部分，但需要队伍已有远程基本面"
    slot_4_5: "看到敌方墙控/低机动核心且路线可破时，可以补为接触惩罚位"
    slot_6: "最适合最后手惩罚无 CC、无身体、无路线阻断的后排；不能弥补队伍缺远程输出"
```

## 关联页面

- [[sources/Fandom-Bolt|Fandom 来源摘要: Bolt]]
- [[sources/PLP-Bolt|PLP 来源摘要: Bolt]]
