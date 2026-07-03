# Lola

## 基本信息

- 稀有度：Epic
- 定位：Damage Dealer
- 类型：长线六连发 / Ego 分身交叉火力 / 炮台式护盾

## 来源摘要

- Fandom：[[sources/Fandom-Lola|Fandom 来源摘要: Lola]]
- PLP：[[sources/PLP-Lola|PLP 来源摘要: Lola]]
- PLP 推荐模式：Brawl Ball, Heist, Bounty

## 角色定位总结

Lola 是“本体输出 + Ego 分身”的长线伤害英雄。她 9 格六连发有高命中上限，Super 生成的 Ego 会复制移动和攻击，能双线压迫、挡弹、攻击墙后目标或在 `Freeze Frame` 下用 50% 减伤硬吃火力。BP 上她适合需要长线持续 DPS、固定目标打库或 Bounty/Knockout 压线的地图；但 Ego 不能捡宝、不能占 Hot Zone，靠近 Lola 3 格内伤害会降低 35%，且非常怕 Penny/Jessie/Nita/Belle/Tara/Mr. P 等弹射、穿透、召唤物或投掷清分身方式。

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
    effective_range: "long; Lola 与 Ego 均 9 格攻击范围"
    projectile_reliability: "medium_high_on_lanes; 6 发 15 度 spread，0.85 秒卸弹，需跟踪"
    burst: "medium_high_with_improvise; 最后一发 ammo 攻击 +30%，双点命中上限高"
    sustained_dps: "high_when_ego_lives; 本体 1.7 秒装填，Ego 有独立 ammo/reload，可叠加火力"
    objective_damage: "high_conditional; Heist safe/固定目标可吃本体+Ego+Freeze Frame 保护"
    mobility: "low; Stunt Double 可与 Ego 换位，但默认 build 不带"
    survivability: "medium; 4000 HP，Ego 可挡非穿透弹，Freeze Frame 让 Ego 4 秒 50% 减伤"
    engage: "low; 主要压线和分身前压，不主动突进"
    disengage: "medium_with_stunt_double; 默认更依赖 Ego 挡弹和站位"
    anti_aggro: "medium; Ego 可挡弹/Spark? 非穿透攻击，但刺客绕过分身会威胁本体"
    anti_tank: "medium_high_if_lane_open; 高持续 DPS 压坦，但近身后缺硬控"
    wall_break: "none"
    throw_or_wall_bypass: "medium_spawnable_angle; Ego 可越墙投放后攻击墙后目标，本体不能隔墙"
    area_control: "medium_high; 双线火力和 Ego 占位压 chokepoint"
    scouting_or_vision: "medium; Ego 前置探路和承伤"
    team_support: "medium; Ego 挡弹，Sealed With a Kiss 变体可治疗队友"
    spawnable_or_pet: "high; Ego 2200 HP，Hyper Ego 5200 HP/更高伤害"
    crowd_control: "none"
    source_trace:
      - "[[sources/Fandom-Lola|Fandom-Lola]]"
      - "[[sources/PLP-Lola|PLP-Lola]]"

  build_switches:
    - build: "Freeze Frame / Improvise / Shield, Damage, Reload"
      source: "[[sources/PLP-Lola|PLP-Lola]]"
      changes_capabilities:
        - "Freeze Frame 让 Ego 停住 4 秒并获得 50% 减伤，能挡 safe/球路/长线火力"
        - "Improvise 在最后一格 ammo 时提高 30% 攻击伤害，配合 Damage/Reload gear 放大持续输出"
        - "Reload gear 同时影响 Ego 的独立装填，强化双点压线"
      enables:
        - "Heist safe pressure"
        - "Bounty/Knockout 长线交叉火力"
        - "Brawl Ball 中路 Ego 挡弹/压守门人"
      mitigates_failure_modes:
        - "ego_dies_before_value"
        - "reload_downtime_after_unload"
      best_when: "地图有长线、固定目标或可保护 Ego 的墙角"
      poor_when: "敌方有高效穿透/弹射/投掷清 Ego 或多突进直取本体"
      bp_use: "default_plp_crossfire_damage_build"
    - build: "Stunt Double / Sealed With a Kiss variant"
      source: "[[sources/Fandom-Lola|Fandom-Lola]]"
      changes_capabilities:
        - "Stunt Double 让 Lola 与 Ego 互换位置并各回复 20% 最大生命，可用于 Bounty/Knockout 进出敌方 base"
        - "Sealed With a Kiss 让 Ego 弹道治疗队友，但操作复杂且通常不如 Improvise 直接"
      enables:
        - "位置欺骗和撤退"
        - "低血换位保命"
        - "双线支援"
      mitigates_failure_modes:
        - "body_rushes_lola_not_ego"
        - "needs_escape_from_long_lane"
      best_when: "地图允许 Ego 安全插入敌方侧后，或需要换位保命"
      poor_when: "团队需要最大输出/打库，或 Ego 会被快速清掉"
      bp_use: "reposition_or_support_variant"

  map_feature_hooks:
    - id: "long_lane_ego_crossfire"
      map_feature_type: "long_sightline_crossfire"
      uses_feature_by: "Lola 本体和 Ego 同时 9 格输出，形成两个射线角度"
      route_or_position: "Bounty/Knockout 长线、Heist 三线、Brawl Ball 中路"
      objective_conversion: "保护星差、压退长手，或让敌方必须同时处理两个火力点"
      active_when: "Ego 可放在不贴近 Lola 且不被秒清的位置"
      fails_if: "敌方用弹射/穿透/投掷清 Ego，或墙体阻断双线"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
      bp_use: "required_capabilities.long_range_crossfire"
    - id: "heist_freeze_frame_safe_block"
      map_feature_type: "stationary_objective_ego_dps"
      uses_feature_by: "Ego 靠近 safe 或 safe 防线后 Freeze Frame 50% 减伤，Lola 在后方同步输出"
      route_or_position: "enemy safe 侧墙、safe 前挡弹位、自家 safe 防守线"
      objective_conversion: "把 Super+Gadget 转成 safe race、挡弹或强制敌方清分身"
      active_when: "Ego 能存活 4 秒并持续对 safe/防守者开火"
      fails_if: "Penny/Jessie/投掷/穿透利用 Ego 反打，或敌方 race 更快"
      example_maps:
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
      bp_use: "candidate_eval.heist_spawnable_dps_with_liability_check"
    - id: "brawl_ball_mid_ego_shield"
      map_feature_type: "ball_lane_spawnable_cover"
      uses_feature_by: "Ego 可开局放中路挡非穿透火力，Freeze Frame 让它硬吃防守弹药"
      route_or_position: "中路开球点、球门前防守线、侧草推进入口"
      objective_conversion: "保护抢球、压守门人、或让队友在分身后推进"
      active_when: "敌方主要是非穿透直线弹道且必须从正面处理 Ego"
      fails_if: "敌方绕侧刺本体、穿透/弹射清分身，或队伍缺 scorer/破墙"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_mid_cover_and_pressure"
    - id: "knockout_bounty_stunt_double_base_swap"
      map_feature_type: "clone_reposition_and_base_pressure"
      uses_feature_by: "Stunt Double 可与 Ego 互换位置并治疗，用于进出敌方 base 或撤离被压线位置"
      route_or_position: "Knockout 侧墙、Bounty 敌方 base 角、长线低血撤退点"
      objective_conversion: "制造侧后压力、骗火力，或保住星差/生命"
      active_when: "Ego 已安全走到可换位位置，且敌方缺即时 burst 覆盖两个点"
      fails_if: "Lola 带默认 Freeze Frame 而非 Stunt Double，或换位保留负面状态后仍被收掉"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "candidate_eval.clone_reposition_variant"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "Ego 中路挡弹和交叉火力"
        - "长线压守门人"
      cannot_fulfill:
        - "稳定破门"
        - "处理多突进贴本体"
      needs_teammate_support:
        - "scorer、破墙、反刺客"
      false_positive: "Ego 能挡弹但不能持球；球权转换仍靠队友"
    - mode: "Heist"
      can_fulfill:
        - "Ego + 本体打 safe"
        - "Freeze Frame 防守挡弹"
      cannot_fulfill:
        - "无路线时稳定进库"
        - "对 Penny/弹射阵容无脑放 Ego"
      needs_teammate_support:
        - "开路、护送分身、处理反分身英雄"
      false_positive: "Heist 价值取决于 Ego 存活，分身也可能成为敌方弹射跳板"
    - mode: "Bounty/Knockout"
      can_fulfill:
        - "长线交叉火力"
        - "Ego 探点和承伤"
        - "Stunt Double 变体撤退/进 base"
      cannot_fulfill:
        - "硬控刺客"
        - "处理深墙投掷口袋"
      needs_teammate_support:
        - "反投掷/开墙、近身 peel、视野"
      false_positive: "双线火力需要可保护 Ego 的角度；被快速清掉时 Lola 只是普通长手"

  failure_modes:
    - id: "ego_cannot_hold_objectives"
      active_when: "BP 把 Ego 当作能捡宝、占 Hot Zone 或带球的实体"
      exposed_by: "[[sources/Fandom-Lola|Fandom-Lola]] notes Ego cannot pick items or score Hot Zone"
      mitigation: "把 Ego 只当火力/挡弹/探路工具，目标由 Lola 或队友完成"
      bp_use: "objective_contract_hard_gate"
    - id: "ego_damage_penalty_near_lola"
      active_when: "Ego 放在 Lola 3 格内叠点输出"
      exposed_by: "Fandom Super damage penalty radius"
      mitigation: "保持分身离开 3 格，或只在需要挡弹/一致命中时临时贴身"
      bp_use: "damage_output_positioning_check"
    - id: "pierce_bounce_or_thrower_liability"
      active_when: "敌方 Penny/Jessie/Nita/Belle/Tara/Mr. P/投掷利用 Ego 或快速清掉它"
      exposed_by: "Fandom tips warn against bouncing or piercing attacks"
      mitigation: "避开对应 matchup，改变 Ego 位置，或不用分身挡 safe/队友"
      bp_use: "spawnable_counter_filter"
    - id: "low_mobility_body_dive"
      active_when: "敌方绕开 Ego 直接突 Lola 本体"
      exposed_by: "Lola has no default mobility and PLP target_favored speed/control signals"
      mitigation: "队友 peel、Stunt Double 变体、把 Ego 放在进场线而不是远端"
      bp_use: "requires_peel_against_dive"

  conditional_matchups:
    - target: ["Piper", "Byron", "Brock", "Griff", "Charlie"]
      direction: "subject_favored"
      source: "[[sources/PLP-Lola|PLP-Lola]]"
      mechanism: "Lola 用长线双点输出和 Ego 挡弹迫使线性长手处理额外火力点"
      active_when: "Ego 可避开穿透/弹射反利用，且 Lola 保持最大射程"
      fails_when: "目标有 thrower 支援、开墙后 outrange，或直接清 Ego"
      bp_use: "long_lane_crossfire_response"
    - target: ["Bibi", "Bull", "Shelly"]
      direction: "subject_favored"
      source: "[[sources/PLP-Lola|PLP-Lola]]"
      mechanism: "Ego 挡非穿透近身路线，Freeze Frame 吃第一轮弹药，本体和分身交叉火力压短手"
      active_when: "短手必须从可见正面接近，且没有草/墙直达 Lola"
      fails_when: "短手从侧草接触本体，或 knockback/爆发先清分身后继续追"
      bp_use: "anti_short_range_if_route_visible"
    - target: ["Penny", "Barley", "Dynamike", "Bo", "Willow"]
      direction: "target_favored"
      source: "[[sources/PLP-Lola|PLP-Lola]]"
      mechanism: "弹射、投掷、地雷或控制接管能绕过/利用 Ego，并惩罚 Lola 低机动"
      active_when: "墙袋或 objective 让 Lola 必须靠 Ego 承压"
      fails_when: "墙体打开、投掷被逼退，或 Lola 在开阔长线只用 Ego 作远端火力"
      bp_use: "must_answer_spawnable_liability"
    - target: ["8-Bit", "Sandy", "Max"]
      direction: "target_favored"
      source: "[[sources/PLP-Lola|PLP-Lola]]"
      mechanism: "Booster 火力、团队隐蔽或速度压缩会让 Lola 的静态双点输出跟不上 tempo"
      active_when: "他们能保护推进路线或快速绕过 Ego 直逼本体"
      fails_when: "Lola 的长线和队友控制先清核心资源，或 Ego 阻断唯一入口"
      bp_use: "tempo_and_resource_warning"

  slot_notes:
    slot_1: "长线/Heist 明确且反分身少时可早手；否则容易被后手投掷/弹射惩罚"
    slot_2_3: "作为持续 DPS 与交叉火力核心，后续补反突进和开墙"
    slot_4_5: "看到敌方缺清分身、缺突进时价值高"
    slot_6: "可最后手惩罚线性长手或短手正面阵容；多穿透/投掷时避选"
```

## 关联页面

- [[sources/Fandom-Lola|Fandom 来源摘要: Lola]]
- [[sources/PLP-Lola|PLP 来源摘要: Lola]]
- [[entities/brawlers/Rico|Rico]]
- [[entities/brawlers/8-Bit|8-Bit]]
- [[entities/brawlers/Pam|Pam]]
