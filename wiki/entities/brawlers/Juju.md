# Juju

## 基本信息

- 稀有度：Mythic
- 定位：Artillery
- 类型：地形元素投掷 / 水域路线 / Gris-Gris 召唤物压力

## 来源摘要

- Fandom：[[sources/Fandom-Juju|Fandom 来源摘要: Juju]]
- PLP：[[sources/PLP-Juju|PLP 来源摘要: Juju]]
- PLP 推荐模式候选：Brawl Ball, Heist, Hot Zone, Bounty, Knockout

## 角色定位总结

Juju 的 BP 价值来自“站位所在地形改变能力”。站在地面时伤害提高，站在草里射程提升到长程，站在水上攻击附带 3 秒 slow；她本身可在水上移动，`Elementalist` 又按地形提供护盾、隐身或水上加速。Super 召唤 4000 基础生命的 Gris-Gris，可在水上移动并追击敌人，`Guarded Gris-Gris` 再给召唤物额外衰减护盾。BP 中必须把 Juju 的价值绑定到具体地形：水域如果不连接目标路线，就只是移动噪声；草丛如果被清空，长射程和隐身价值会下降；地面高伤害则要求她能安全站位。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-07-17
    plp: "[[sources/PLP-Juju|PLP-Juju]]"
    user_notes: none

  capability_vector:
    effective_range: mid_thrower_base_long_from_bush_or_Voodoo_Chile
    projectile_reliability: medium; lobbed 2-tile splash improves chokes but still needs predicted routes
    burst: medium_high_on_ground_damage_or_Voodoo_Chile
    sustained_dps: medium; 1.6 秒 reload，Voodoo Chile active reload slows to 2 秒
    objective_damage: conditional_heist_thrower_pressure_not_primary_race
    mobility: high_on_water_with_trait_and_Elementalist_speed
    survivability: low_medium; 3100 HP, Elementalist ground shield or bush invis can protect windows
    engage: medium_with_bush_invis_or_water_speed
    disengage: medium_high_with_water_route_or_Elementalist
    anti_aggro: conditional_with_water_slow_or_Gris_Gris_body
    anti_tank: medium_if_slow_and_ground_damage_stack; weak_if_body_reaches_her
    wall_break: none
    throw_or_wall_bypass: high_lobbed_attack
    area_control: medium_high_with_splash_and_Gris_Gris
    scouting_or_vision: low_medium; Gris-Gris can chase nearest target but is not full reveal
    team_support: route_slow_and_spawnable_body
    spawnable_or_pet: Gris_Gris_4000_HP_water_crossing_body
    crowd_control: water_attack_slow_or_Numbing_Needles_variant
    terrain_destruction: none

  build_switches:
    - build: "Elementalist / Guarded Gris-Gris / Shield, Damage"
      source: "[[sources/PLP-Juju|PLP-Juju]]"
      changes_capabilities:
        - "Elementalist 在地面给 30% shield、草中给不因攻击失效的短隐身、水上给 40% speed"
        - "4000 基础生命的 Gris-Gris 已能承担更长 ammo tax；Guarded Gris-Gris 再提供初始为其最大生命 30% 的衰减护盾"
        - "Shield/Damage 补低血投掷位容错和地形伤害窗口"
      enables:
        - "water_slow_or_speed_route"
        - "bush_range_invisible_peek"
        - "Gris_Gris_ammo_tax"
      mitigates_failure_modes:
        - "low_health_dive_pressure"
        - "Gris_Gris_deleted_before_value"
      best_when: "地图有水/草/墙袋可把元素加成转成目标路线收益"
      poor_when: "地图开阔且缺可用地形，或敌方高机动直接越过 slow / summon"
      bp_use: default_terrain_element_build
    - build: "Voodoo Chile all-elements burst"
      source: "[[sources/Fandom-Juju|Fandom-Juju]]"
      changes_capabilities:
        - "下一发攻击同时获得地面伤害、草中长射程和水上 slow"
        - "适合不稳定地形或需要一发远程 slow/burst 的关键窗口"
      enables:
        - "single_shot_slow_burst"
        - "long_range_thrower_finish"
      mitigates_failure_modes:
        - "wrong_current_terrain"
      best_when: "当前站位无法同时满足 range/damage/slow，但下一发必须转换目标"
      poor_when: "战斗更需要 Elementalist 的隐身/加速/护盾生存"
      bp_use: single_window_element_stack_variant

  map_feature_hooks:
    - map_feature_type: water_slow_and_cross_angle
      uses_feature_by: "Juju 可站水上移动并把普攻变成 slow，Elementalist 水上加速提高进退场"
      route_or_position: "water lane、river edge、off-angle retreat、safe side water"
      objective_conversion: "从普通英雄不能站的位置减速进场者、保护撤退或制造远端打库/回合角度"
      active_when: "水域直接连接目标路线，Juju 的射程/投掷能从水上持续影响目标"
      fails_if: "水域远离目标，或敌方能用长手/跳跃/水上单位直接处理 Juju"
      example_maps:
        - Safe Zone
        - Safe(r) Zone
        - New Horizons
        - Flaring Phoenix
      bp_use: map_bp_factors.water_route_with_slow_and_thrower_value
    - map_feature_type: bush_range_and_invisible_ambush
      uses_feature_by: "草中射程提升，Elementalist 草中隐身且攻击不破隐身，可打低血撤退或目标入口"
      route_or_position: "side bush、center grass、ball lane grass、zone grass mouth"
      objective_conversion: "拉长投掷威胁、保护撤退、偷袭 carrier/scorer 或低血长手"
      active_when: "草丛未被持续扫掉，敌方必须经过 Juju 的长射程投掷线"
      fails_if: "草被烧/扫，或敌方靠 summon/vision 把隐身路线暴露"
      example_maps:
        - Double Swoosh
        - Center Stage
        - Ring of Fire
        - Sneaky Fields
      bp_use: map_bp_factors.bush_range_and_invisibility_route
    - map_feature_type: hot_zone_ground_damage_or_slow_entry
      uses_feature_by: "地面高伤害、水上 slow 或 Gris-Gris 召唤物压 zone entrance"
      route_or_position: "zone entrance、wall-adjacent zone edge、grass mouth、re-entry choke"
      objective_conversion: "逼退站区身体、减速重进区目标、让队友获得 zone time"
      active_when: "Juju 有墙后投掷角或水/草地形加成，队友负责站圈"
      fails_if: "敌方从圈外长手清她，或 Juju 被要求自己当 durable zone body"
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.elemental_zone_entry_control
    - map_feature_type: knockout_bounty_gris_gris_wall_control
      uses_feature_by: "投掷弧线和 4000 基础生命的 Guarded Gris-Gris 在墙边/回合末制造更持久的 ammo tax 和追击压力"
      route_or_position: "wall pocket、late-round choke、low-health retreat、long-lane side cover"
      objective_conversion: "逼低血目标不能安全回复，或让单发长手先处理召唤物再 peek"
      active_when: "Gris-Gris 能贴近目标或从墙边迫使其交弹药，Juju 本体有安全投掷位"
      fails_if: "召唤物被 splash/pierce 免费清掉，或刺客绕过 Gris-Gris 直接打 Juju"
      example_maps:
        - Belle's Rock
        - New Horizons
        - Layer Cake
        - Shooting Star
      bp_use: candidate_eval.round_spawnable_thrower_pressure

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "water_or_bush_route_control"
        - "ball_lane_slow"
        - "Gris_Gris_goal_pressure"
      cannot_fulfill:
        - "primary_scorer_without_teammate"
      needs_teammate_support:
        - "scorer_or_wallbreak"
        - "anti_dive"
      false_positive: "能在草/水获得角度不等于能自己进球，必须有球权转化"
    - mode: "Heist"
      can_fulfill:
        - "thrower_safe_or_defender_pressure"
        - "water_off_angle_support"
        - "Gris_Gris_ammo_tax"
      cannot_fulfill:
        - "solo_safe_race"
      needs_teammate_support:
        - "primary_safe_DPS"
        - "lane_control"
      false_positive: "PLP Heist 信号要检查她是否能从地形角度触达 safe 或 defender route"
    - mode: "Hot Zone"
      can_fulfill:
        - "entry_slow_or_damage"
        - "wall_thrower_zone_pressure"
        - "spawnable_ammo_tax"
      cannot_fulfill:
        - "durable_zone_body"
      needs_teammate_support:
        - "zone_holder"
        - "vision_or_peel"
      false_positive: "Juju 是控入口/支援，不应被计作稳定站区身体"
    - mode: "Bounty_or_Knockout"
      can_fulfill:
        - "wall_control"
        - "spawnable_ammo_tax"
        - "water_or_bush_angle"
      cannot_fulfill:
        - "open_sniper_mirror_without_terrain"
      needs_teammate_support:
        - "peel_against_assassins"
        - "range_partner_or_wallbreak"
      false_positive: "Juju 需要地形元素；纯开放图缺草/水/墙袋时价值下降"

  failure_modes:
    - id: terrain_dependency_mismatch
      active_when: "Juju 当前站在错误地形，拿不到需要的 range/damage/slow/Elementalist 效果"
      exposed_by: "[[sources/Fandom-Juju|Fandom-Juju]] environment-based attack and gadget mechanics"
      mitigation: "BP 时把水/草/地面位置写成具体路线，不用泛化标签"
      bp_use: map_factor_hard_gate
    - id: low_health_dive_pressure
      active_when: "Edgar、Sam、Kaze、Trunk 等越过投掷/slow，直接接触 3100 HP Juju"
      exposed_by: "[[sources/PLP-Juju|PLP-Juju]] counteredBy list"
      mitigation: "保留 Elementalist 逃生，配队友 peel 或选择水/草安全角"
      bp_use: draft_requires_peel
    - id: gris_gris_deleted_or_misdirected
      active_when: "Gris-Gris 从远处追目标低命中，或被 splash/pierce/summon 清掉"
      exposed_by: "[[sources/Fandom-Juju|Fandom-Juju]] Gris-Gris chase and tips"
      mitigation: "4000 基础生命提高首轮存活率，但仍需靠近目标或墙边部署；Guarded Gris-Gris 只视为更持久 ammo tax，不视为必杀"
      bp_use: spawnable_value_check
    - id: water_false_positive
      active_when: "地图有水但水线不影响 safe、zone、mine、ball 或回合角度"
      exposed_by: "Juju water trait and user map-modeling principle"
      mitigation: "只有水域给出射角、slow route 或撤退价值才计入地图适配"
      bp_use: false_positive_filter.water_must_convert_objective

  conditional_matchup_seeds:
    - target: Jae_Yong_or_Poco_or_Berry
      direction: subject_favored
      source: "[[sources/PLP-Juju|PLP-Juju]]"
      mechanism: "Juju 用投掷弧线、元素 slow/damage 和 Gris-Gris ammo tax 压低支援壳的固定站位"
      active_when: "支援目标必须站在矿区、热区、球路或 safe defender route"
      fails_when: "支援壳有强突进保护，或 Juju 的地形加成无法触达目标"
      bp_use: thrower_pressure_into_static_support
    - target: Lola_or_Meg_or_R_T_or_Shelly_or_Spike
      direction: volatile
      source: "[[sources/PLP-Juju|PLP-Juju]]"
      mechanism: "Juju 可用墙后投掷和召唤物压资源位，但这些目标的身体、替身、分体、近身爆发或 slow 也会反制她"
      active_when: "地图给 Juju 墙袋/水/草角度，目标被迫守固定路口"
      fails_when: "资源层吸收 Gris-Gris 或目标在开阔中距离先压 Juju"
      bp_use: map_geometry_and_resource_check
    - target: Brock_or_Rosa_or_Edgar_or_Gray_or_Sam_or_Trunk_or_Larry_Lawrie_or_Kaze
      direction: target_favored
      source: "[[sources/PLP-Juju|PLP-Juju]]"
      mechanism: "破墙、坦克进场、刺客/传送/速度和强投掷召唤物会绕过 Juju 的元素窗口或直接处理本体"
      active_when: "他们能到达 Juju 的地形站位或清掉 Gris-Gris"
      fails_when: "Juju 站在安全水/草/墙后角度且队友覆盖进场路线"
      bp_use: must_answer_dive_or_wallbreak_before_juju
    - target: Water_or_bush_route_target
      direction: subject_favored
      source: "[[sources/Fandom-Juju|Fandom-Juju]]"
      mechanism: "水上 slow、草中射程/隐身和地面高伤分别惩罚不同路线目标"
      active_when: "目标必须经过这些地形关联的路线，Juju 当前站位能触发对应元素"
      fails_when: "目标路线不经过元素价值区或有 vision/long-range clear"
      bp_use: objective_specific_terrain_edge

  slot_notes:
    slot_1: "只有地图水/草/墙袋明确服务目标时才早手；否则后手会被突进或长手针对。"
    slot_2_3: "可作为地形控路和召唤物压力计划手，但队伍要补站点身体或主 safe DPS。"
    slot_4_5: "适合看到敌方固定支援/低机动阵容后，用地形元素锁路线，同时防敌方最后手拿破墙或刺客。"
    slot_6: "如果敌方缺接近和清召唤物能力，Juju 可作为高上限地形惩罚 pick。"
```

## 关联页面

- [[sources/Fandom-Juju|Fandom 来源摘要: Juju]]
- [[sources/PLP-Juju|PLP 来源摘要: Juju]]
