# Mr. P

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：弹跳公文包 / Porter 消耗 / 召唤物控图

## 来源摘要

- Fandom：[[sources/Fandom-Mr-P|Fandom 来源摘要: Mr. P]]
- PLP：[[sources/PLP-Mr-P|PLP 来源摘要: Mr. P]]
- PLP 推荐模式：Bounty, Knockout

## 角色定位总结

Mr. P 的 BP 价值来自“弹跳骚扰 + porters 持续耗弹”。主攻 7 格，触达最大距离或碰障碍后再弹 3.33 格并造成 1.5 格 splash，因此能像伪投掷一样打单格墙后或逼长手走位；Super 的 home base 持续召唤 porter 追敌，配合 `Service Bell / Revolving Door / Pet Power` 把 Bounty/Knockout 的 long lane 变成对手不断花 ammo 清宠的消耗局。风险是本体 3700 HP、爆发低，porters 会被穿透/弹射/范围伤害反利用，PLP 还显式标记 Avoid: GIGI。

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
    effective_range: "long_plus_bounce; 7 格直线，弹跳后总压到 10.33 格"
    projectile_reliability: "medium_high_vs_static_or_wall_targets; 需要墙/最大距离/目标站位触发二段 splash"
    burst: "low_to_medium; 双段命中可观，但主要靠持续消耗"
    sustained_dps: "medium_with_porters; 1.6 秒装填，porters 持续耗弹"
    objective_damage: "low; Heist 不建议作为主 safe DPS"
    mobility: "low"
    survivability: "medium; 3700 HP，靠 porter meat shield/墙角"
    engage: "low; 不主动开团"
    disengage: "medium; porters 可挡弹/拖近身"
    anti_aggro: "medium_if_porters_online; 低伤短手/长手会被 porters 追，但硬刺客仍危险"
    anti_tank: "low; 缺爆发和百分比"
    wall_break: "none"
    throw_or_wall_bypass: "medium; 公文包弹跳能越过单格墙或最大距离后 splash"
    area_control: "medium_high; home base + porters 持续推 lane"
    scouting_or_vision: "high_on_bush_maps; porters 可追踪并冲出隐藏敌人"
    team_support: "medium; ammo tax、meat shield、探草"
    spawnable_or_pet: "very_high; home base 2500 HP，porter 1400 HP，Hyper 可两只强 porter"
    crowd_control: "none_direct; 通过 ammo tax 和 body block 间接控制"
    source_trace:
      - "[[sources/Fandom-Mr-P|Fandom-Mr-P]]"
      - "[[sources/PLP-Mr-P|PLP-Mr-P]]"

  build_switches:
    - build: "Service Bell / Revolving Door / Shield, Damage, Pet Power"
      source: "[[sources/PLP-Mr-P|PLP-Mr-P]]"
      changes_capabilities:
        - "Service Bell 给当前 porter 回满并提高约 52.9% HP / 43.8% damage"
        - "Revolving Door 提高 Super porters 20% HP / 30% damage"
        - "Pet Power 强化 porter damage，适合 Bounty/Knockout 消耗"
      enables:
        - "Bounty/Knockout long lane ammo tax"
        - "探草和肉盾"
        - "低 burst 长手压制"
      mitigates_failure_modes:
        - "porter_dies_before_tax"
        - "low_direct_damage"
      best_when: "敌方长手/单发低 reload 需要频繁处理 porter，且缺穿透/弹射清宠"
      poor_when: "敌方有 dive、thrower、bounce/pierce 或 Gigi 这类避开正面消耗的路线"
      bp_use: "default_plp_porter_tax_build"
    - build: "Porter Reinforcements / Handle With Care variant"
      source: "[[sources/Fandom-Mr-P|Fandom-Mr-P]]"
      changes_capabilities:
        - "Porter Reinforcements 在下一发落点生成弱 porter，用于挡弹或立刻逼退低伤长手"
        - "Handle With Care 每 4 秒强化弹跳段伤害，在墙多图提升 poke"
      enables:
        - "即时挡弹"
        - "墙后二段伤害"
      mitigates_failure_modes:
        - "no_super_yet_for_porter_tax"
        - "wall_target_survives_bounce"
      best_when: "地图墙多、需要开局就给长手/草区压力"
      poor_when: "队伍更依赖持续 porter 质量和 Pet Power"
      bp_use: "wall_poke_or_no_super_variant"

  map_feature_hooks:
    - id: "bounty_knockout_porter_ammo_tax"
      map_feature_type: "long_lane_spawnable_tax"
      uses_feature_by: "home base 持续产 porter，Service Bell/Revolving Door 让对手花 ammo 清宠"
      route_or_position: "Bounty 长线、Knockout 中线、星差防守墙后"
      objective_conversion: "保护星差、逼长手后退、制造队友 peek 窗口"
      active_when: "home base 能被墙保护，敌方缺穿透/弹射/投掷快速清"
      fails_if: "Buzz/Edgar/Mortis/Fang 直接切本体，或 Barley/Penny 清 base 和 porters"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
      bp_use: "map_bp_factors.spawnable_ammo_tax_star_lead"
    - id: "single_wall_bounce_poke"
      map_feature_type: "one_tile_wall_bounce_pressure"
      uses_feature_by: "公文包打墙或到最大距离后弹跳 splash，可命中单格墙后目标"
      route_or_position: "单格墙角、Knockout/Bounty pocket、Gem Fort 中央墙边"
      objective_conversion: "逼墙后目标离开、阻断回血，或让低血不能安全藏墙"
      active_when: "墙厚/距离刚好触发二段，目标缺快速反打"
      fails_if: "墙袋更深或敌方 thrower 反过来压 Mr. P"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
      bp_use: "map_bp_factors.pseudo_thrower_single_wall_poke"
    - id: "bush_porter_scouting"
      map_feature_type: "spawnable_bush_scout"
      uses_feature_by: "porter 会追踪敌人，可把草内隐藏目标逼出来或吃第一发"
      route_or_position: "中心草、侧草绕后、Brawl Ball/Gem Grab 草口"
      objective_conversion: "降低草伏击风险，保护星差或 carrier 撤退"
      active_when: "敌方依赖隐藏接近，且 porter 能从安全 base 持续生成"
      fails_if: "敌方 AoE/穿透免费清宠，或草图需要即时 reveal 而 porter 来不及"
      example_maps:
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.spawnable_scouting_window"
    - id: "knockout_last_seconds_meatshield"
      map_feature_type: "spawnable_cover_and_round_clock"
      uses_feature_by: "porter/base 可挡非穿透弹，最后几秒保护低血队友或 star/round lead"
      route_or_position: "Knockout 缩圈边、Bounty 星差后撤线、低血队友藏点"
      objective_conversion: "用额外 body 吃一发关键弹，保住 round/star lead"
      active_when: "敌方伤害是单体非穿透，且 porter 能站在弹道线上"
      fails_if: "敌方穿透/弹射/投掷绕过肉盾，或把 porter 当跳板打队友"
      example_maps:
        - "[[entities/maps/Out in the Open|Out in the Open]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
      bp_use: "candidate_eval.spawnable_cover_endgame"

  objective_contracts:
    - mode: "Bounty/Knockout"
      can_fulfill:
        - "porter ammo tax"
        - "星差/回合领先保护"
        - "墙后二段 poke"
      cannot_fulfill:
        - "硬 anti-dive"
        - "快速爆发收割"
      needs_teammate_support:
        - "反刺客、投掷处理、长线击杀"
      false_positive: "Mr. P 会拖慢对手，不会自动赢星差；队伍仍要有击杀来源"
    - mode: "Gem/Ball"
      can_fulfill:
        - "草口 scout 和 ammo tax"
        - "低血撤退肉盾"
      cannot_fulfill:
        - "主 carrier/scorer"
        - "站区/破门"
      needs_teammate_support:
        - "目标执行者、前排、爆发"
      false_positive: "Fandom 支持探草，但 PLP 主模式是 Bounty/Knockout，其他模式应当作变体"

  failure_modes:
    - id: "pierce_bounce_or_thrower_punishes_porters"
      active_when: "敌方 Penny/Jessie/Belle/Carl/Rico/Tara/Bibi/Grom 等利用 spawnable"
      exposed_by: "[[sources/Fandom-Mr-P|Fandom-Mr-P]] warning about piercing/bouncing Brawlers"
      mitigation: "避开这些清宠/反利用阵容，改变 base 位置或不用 porter 肉盾挡 safe/队友"
      bp_use: "spawnable_liability_filter"
    - id: "dive_reaches_low_health_body"
      active_when: "Buzz/Edgar/Mortis/Fang/Sam 等绕过 porters 直接打 Mr. P"
      exposed_by: "[[sources/PLP-Mr-P|PLP-Mr-P]] target_favored dive signals"
      mitigation: "必须有 peel、草视野和更深 base；不要盲早手进多刺客"
      bp_use: "requires_anti_dive_support"
    - id: "home_base_cleared_before_cycle"
      active_when: "base 放在开阔线或投掷火力下"
      exposed_by: "home base is stationary and porters depend on it"
      mitigation: "放墙后、换新 base 立即产 porter，或等投掷资源被压走"
      bp_use: "spawnable_anchor_survival"
    - id: "low_direct_damage_into_tanks"
      active_when: "敌方高血 body 不需要花太多代价清 porter"
      exposed_by: "Mr. P low porter damage and no percent/burst"
      mitigation: "搭配 anti-tank DPS，或只用 Mr. P 压长手/低 burst lane"
      bp_use: "role_gap_filter"

  conditional_matchups:
    - target: ["Bea", "Piper", "Gene", "Crow"]
      direction: "subject_favored"
      source: "[[sources/PLP-Mr-P|PLP-Mr-P]]"
      mechanism: "porters 逼单发/低 burst 长手交 ammo，公文包二段压制他们的安全站位"
      active_when: "home base 有保护，目标缺穿透/范围清宠"
      fails_when: "目标有队友 dive/thrower 清 base，或用超远角不理 porter"
      bp_use: "long_lane_ammo_tax_response"
    - target: ["Stu", "Gray", "Maisie", "Colette"]
      direction: "subject_favored"
      source: "[[sources/PLP-Mr-P|PLP-Mr-P]]"
      mechanism: "porters 打乱技能射线和资源节奏，逼他们先处理 body 再执行 poke/位移"
      active_when: "目标必须在 Bounty/Knockout 线内持续 peek"
      fails_when: "Gray/Stu 从侧角直接开 Mr. P 或 Colette 用队友清宠后打本体"
      bp_use: "tempo_disruption_into_skillshot_or_resource_pick"
    - target: ["Buzz", "Sam", "Fang", "Edgar", "Mortis"]
      direction: "target_favored"
      source: "[[sources/PLP-Mr-P|PLP-Mr-P]]"
      mechanism: "高速贴脸/跳入直接越过 porter 消耗，惩罚 Mr. P 低血和低爆发"
      active_when: "地图有草墙入口或 last-pick 接近路线，Mr. P 队伍缺 peel"
      fails_when: "草被控、porters 预先挡路，队友有硬控/爆发守本体"
      bp_use: "avoid_without_peel"
    - target: ["Carl", "Barley", "Penny", "Gigi"]
      direction: "target_favored"
      source: "[[sources/PLP-Mr-P|PLP-Mr-P]]"
      mechanism: "穿透/投掷/弹射/特殊进场能清 base、反利用 porters 或绕过正面消耗"
      active_when: "他们拥有墙袋、反弹角或 endpoint 路线，Mr. P 必须靠召唤物控图"
      fails_when: "墙袋被打开，base 放在他们打不到的位置，或 Mr. P 只打远端二段 poke"
      bp_use: "must_answer_spawnable_counter_or_avoid_gigi"

  slot_notes:
    slot_1: "Bounty/Knockout 长线可早手，但会暴露给 dive/thrower/清宠"
    slot_2_3: "适合作为 ammo tax 和星差保护层，后续补 burst 与 anti-dive"
    slot_4_5: "看到敌方长手低 burst、缺清宠时可响应"
    slot_6: "最后手惩罚无清宠/无突进阵容；看到 Gigi 或多穿透时谨慎"
```

## 关联页面

- [[sources/Fandom-Mr-P|Fandom 来源摘要: Mr. P]]
- [[sources/PLP-Mr-P|PLP 来源摘要: Mr. P]]
