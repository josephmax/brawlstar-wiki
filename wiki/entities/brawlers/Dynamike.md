# Dynamike

## 基本信息

- 稀有度：Super Rare
- 定位：Artillery
- 类型：延迟投掷爆破 / Satchel 控制 / Super 开墙与固定目标伤害

## 来源摘要

- Fandom：[[sources/Fandom-Dynamike|Fandom 来源摘要: Dynamike]]
- PLP：[[sources/PLP-Dynamike|PLP 来源摘要: Dynamike]]
- PLP 推荐模式候选：Heist, Hot Zone, Brawl Ball

## 角色定位总结

Dynamike 的 BP 价值来自墙后投掷爆发和资源窗口，而不是稳定远程消耗。他的普攻两根炸药有约 1 秒引信，Super 有高伤害、击退和 2.67 格破墙；`Satchel Charge` 让下一次普攻造成 1.5 秒眩晕，是处理门前、热区入口、金库防守和近身目标的关键资源。Fandom 同时强调，刺客和高速移动是巨大威胁，Super 破墙也可能拆掉自己赖以安全输出的掩体。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Dynamike|Fandom-Dynamike]]"
    plp: "[[sources/PLP-Dynamike|PLP-Dynamike]]"
    user_notes: none

  capability_vector:
    effective_range: long_thrower; 7.33 格普攻和 Super 越墙投掷
    projectile_reliability: low_medium_vs_open_mobility; high_on_fixed_routes_or_stunned_targets
    burst: very_high_if_double_stick_or_Super_connects
    sustained_dps: medium; 1.6 秒 reload，但命中依赖预判和路线限制
    objective_damage: high_heist_if_wall_pocket_reaches_safe
    mobility: low_base; Dyna_Jump_is_high_skill_route_tool
    survivability: low; 3000 HP，依赖墙体、Satchel、Dyna-Jump 或队友 peel
    engage: medium_with_Satchel_or_Super_knockback
    disengage: medium_with_Satchel_stun_or_Dyna_Jump_if_mastered
    anti_aggro: conditional_high_when_Satchel_available
    anti_tank: high_if_tank_path_is_predictable_or_stunned
    wall_break: high_with_Super
    throw_or_wall_bypass: very_high
    area_control: medium_high; delayed bombs and Hypercharge fragments tax chokes
    scouting_or_vision: low_medium; bombs can check bush/pocket
    team_support: terrain_break_and_stun_window
    spawnable_or_pet: none
    crowd_control: Satchel_stun_and_Super_knockback
    terrain_destruction: Super_wall_break

  build_switches:
    - build: "Satchel Charge / Demolition / Shield, Damage"
      source: "[[sources/PLP-Dynamike|PLP-Dynamike]]"
      changes_capabilities:
        - "Satchel Charge 把下一次普攻变成 1.5 秒 stun，是 Dynamike 从预判投掷升级成确定击杀/防守窗口的核心"
        - "Demolition 增加 Super 伤害，提升 Heist safe、坦克和关键击杀阈值"
        - "Shield/Damage 提供低血投掷位的容错和斩杀线"
      enables:
        - "Heist 墙后打库"
        - "Brawl Ball 门前 stun 和清防守"
        - "Hot Zone 入口眩晕清点"
      mitigates_failure_modes:
        - "delayed_fuse_reliability"
        - "low_health_first_contact"
      best_when: "地图有稳定墙袋/窄口，目标必须经过可预判路线，且敌方缺廉价 dive 或先手破墙"
      poor_when: "敌方多高速突进、多角度接近，或地形一旦打开就让 Dynamike 无处站"
      bp_use: default_control_burst_build
    - build: "Dyna-Jump escape or route variant"
      source: "[[sources/Fandom-Dynamike|Fandom-Dynamike]]"
      changes_capabilities:
        - "Dyna-Jump 可让 Dynamike 用普攻/Super 自跳短暂免伤，高手能规避部分刺客和重置位置"
      enables:
        - "wall_pocket_escape"
        - "unexpected_route_or_goal_pressure"
      mitigates_failure_modes:
        - "assassin_first_contact"
      best_when: "玩家熟练掌握跳跃时间，地图墙袋能用跳跃重置"
      poor_when: "需要稳定输出或玩家不能稳定执行跳跃"
      bp_use: skill_dependent_escape_variant

  map_feature_hooks:
    - map_feature_type: heist_wall_safe_thrower_damage
      uses_feature_by: "墙后投掷和 Demolition Super 把固定 safe 转成高伤害目标"
      route_or_position: "safe 前墙、side lane wall pocket、lane win 后的投掷角"
      objective_conversion: "持续 safe damage、逼防守者绕墙接近、用 Satchel/Super 处理回防身体"
      active_when: "Dynamike 能安全站墙后，safe 或防守路线进入投掷范围"
      fails_if: "敌方破墙/突进先处理 Dynamike，或需要他在开阔 lane 纯 race"
      example_maps:
        - Hot Potato
        - Pit Stop
        - Safe Zone
        - Safe(r) Zone
      bp_use: candidate_eval.heist_thrower_safe_burst_with_pocket_check
    - map_feature_type: brawl_ball_wall_pocket_satchel_goal_control
      uses_feature_by: "Satchel Charge stun 和 Super knockback/wallbreak 可处理门前防守、持球者或 goal wall"
      route_or_position: "goal-front wall、midfield ball choke、side grass push、己方门前反打点"
      objective_conversion: "眩晕持球者、清防守者、破关键门墙，给 scorer 进球窗口"
      active_when: "球路必须穿过墙边或窄口，Dynamike 有 Satchel 或 Super，队友能接球/补伤害"
      fails_if: "敌方高机动 scorer 绕过炸点，或 Super 破墙后让对方长手更容易射门"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
        - Pinball Dreams
      bp_use: slot_task.goal_control_with_satchel_resource
    - map_feature_type: hot_zone_satchel_entry_stun_and_pocket_control
      uses_feature_by: "墙后预铺炸药封 zone entrance，Satchel 对重复进圈者给确定控制"
      route_or_position: "zone entrance、wall-adjacent zone edge、grass mouth、re-entry choke"
      objective_conversion: "拖延回区、眩晕站区身体、让队友获得 zone time"
      active_when: "墙体保护 Dynamike，敌方必须从明确入口进入热区"
      fails_if: "敌方从圈外远程/投掷清掉 Dynamike，或多路线进区使炸点失效"
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.thrower_stun_zone_entry_control
    - map_feature_type: terrain_break_super_backfire_filter
      uses_feature_by: "Super 破墙可打开敌方 pocket、safe route 或球门几何，但也可能拆掉自己的保护墙"
      route_or_position: "thrower pocket wall、goal wall、safe wall、center fort wall"
      objective_conversion: "移除敌方安全位、打开进球/打库路线、让己方长手接管"
      active_when: "破墙后我方更受益，且 Dynamike 仍有后续安全位"
      fails_if: "过度开图让敌方长手/刺客更容易处理 Dynamike 或队友"
      example_maps:
        - Belle's Rock
        - Gem Fort
        - Pit Stop
        - Shooting Star
      bp_use: terrain_state_plan.selective_wallbreak_with_self_exposure_check

  objective_contracts:
    - mode: Heist
      can_fulfill:
        - "wall_pocket_safe_damage"
        - "Satchel_defense_against_safe_entry"
        - "Super_burst_and_wall_transform"
      cannot_fulfill:
        - "open_lane_pure_race_without_cover"
      needs_teammate_support:
        - "lane_control_or_peel"
        - "anti_wallbreak_or_anti_dive"
      false_positive: "Heist 强度取决于墙后投掷角和防守路径，不是所有金库图都可硬选"
    - mode: Brawl Ball
      can_fulfill:
        - "Satchel_ball_carrier_stun"
        - "goal_wall_or_defender_clear"
        - "midfield_choke_control"
      cannot_fulfill:
        - "primary_scorer"
        - "open_goalkeeper_against_high_mobility"
      needs_teammate_support:
        - "scorer_or_wallbreak_followup"
        - "peel_for_dive"
      false_positive: "Dynamike 能制造进球窗口，但 Satchel 命中和队友 follow-up 是必要条件"
    - mode: Hot Zone
      can_fulfill:
        - "zone_entry_denial"
        - "Satchel_stun_clear"
        - "wall_pocket_control"
      cannot_fulfill:
        - "durable_zone_body"
        - "long_open_lane_duel"
      needs_teammate_support:
        - "actual_zone_holder"
        - "vision_or_anti_aggro"
      false_positive: "他能清圈但不能替代站圈身体"

  failure_modes:
    - id: delayed_fuse_into_mobility
      active_when: "Stu、Max、Mortis、Edgar、Kenji 等高速目标能横移或多段接近，离开 1 秒引信落点"
      exposed_by: "[[sources/Fandom-Dynamike|Fandom-Dynamike]] delayed fuse and assassin warning"
      mitigation: "只在 chokepoint、墙边或 Satchel 资源可用时接这类目标"
      bp_use: projectile_reliability_gate
    - id: low_health_assassin_pressure
      active_when: "刺客从草/墙角贴脸，Dynamike 无 Satchel、Super 或 Dyna-Jump 逃生"
      exposed_by: "3000 HP and PLP target_favored list"
      mitigation: "保留 Satchel，队友 peel，避免无视野侧路单站"
      bp_use: draft_requires_peel_or_route_lock
    - id: wallbreak_self_exposure
      active_when: "Super 打掉保护自己或队友的墙，导致对面长手/突进获得更好角度"
      exposed_by: "[[sources/Fandom-Dynamike|Fandom-Dynamike]] notes about Super wallbreak making him vulnerable"
      mitigation: "破墙前指定受益方和后续站位，不把 Super 当默认开图"
      bp_use: terrain_state_plan_check
    - id: satchel_cooldown_or_miss
      active_when: "Satchel 空掉或 23 秒 cooldown 内敌方再次进场"
      exposed_by: "[[sources/Fandom-Dynamike|Fandom-Dynamike]] Satchel Charge cooldown and one-attack window"
      mitigation: "把 Satchel 留给持球者/刺客/关键站区身体，而非低价值预判"
      bp_use: resource_tracking.satchel_available

  conditional_matchup_seeds:
    - target: Meg_or_Jae_Yong_or_Lola_or_Sprout_or_Squeak_or_Lou_or_Mandy_or_Nani
      direction: subject_favored
      source: "[[sources/PLP-Dynamike|PLP-Dynamike]]"
      mechanism: "墙后投掷、Satchel stun 和 Super burst 能惩罚固定站位、低机动控制或长线在墙边卡点的目标"
      active_when: "地图给 Dynamike 安全 pocket，目标必须守矿区、热区、球路或金库防守线"
      fails_when: "目标在开阔远端输出，或有队友突进先处理 Dynamike"
      bp_use: thrower_burst_response_to_fixed_control
    - target: Sam_or_Kaze_or_Edgar_or_Mortis_or_Kenji_or_Damian_or_Gray_or_Stu
      direction: target_favored
      source: "[[sources/PLP-Dynamike|PLP-Dynamike]]"
      mechanism: "高机动、传送/拉人或强突进可绕过延迟炸点，逼迫 Dynamike 在低血和 reload 窗口被贴脸"
      active_when: "地图有侧草、墙角或多路线接近，Dynamike 缺 Satchel/peel"
      fails_when: "入口被锁死，Satchel 保留给第一接触，或队友提前控制突进路线"
      bp_use: must_avoid_without_peel_or_satchel
    - target: Heist_safe_or_goal_defender_or_zone_holder
      direction: subject_favored
      source: "[[sources/Fandom-Dynamike|Fandom-Dynamike]]"
      mechanism: "固定目标和固定路线更容易吃到双炸、Demolition Super 或 Satchel 后续爆发"
      active_when: "目标不能离开 safe/球门/热区位置，Dynamike 可从墙后完整释放"
      fails_when: "目标能离开炸点或用控制打断 Dynamike 的释放/站位"
      bp_use: objective_specific_fixed_target_burst
    - target: Brock_or_Hank_or_Squeak_or_Jacky_wall_hit_tools
      direction: target_favored
      source: "[[sources/Fandom-Dynamike|Fandom-Dynamike]]"
      mechanism: "能穿墙/炸墙/墙边命中的工具会惩罚 Dynamike 过度贴墙躲避"
      active_when: "Dynamike 必须靠墙藏身且这些目标能从安全角度打到墙后"
      fails_when: "Dynamike 换位、队友开线压走对方，或 Satchel 先惩罚他们接近"
      bp_use: wall_pocket_counterplay_filter

  slot_notes:
    slot_1: "只在地图稳定保护投掷 pocket，且敌方低成本 dive/破墙反制面窄时考虑；否则早手会暴露明显反制。"
    slot_2_3: "可作为 Heist/Hot Zone/Brawl Ball 的墙后爆发计划手，但必须补站点或得分主体。"
    slot_4_5: "看到敌方固定控制、低机动后排或缺突进时可以后手惩罚，同时封掉强刺客 slot_6。"
    slot_6: "最佳用途是最后手惩罚无机动、无破墙、必须走 chokepoint 的阵容，用 Satchel/Super 决定关键目标。"
```

## 关联页面

- [[sources/Fandom-Dynamike|Fandom 来源摘要: Dynamike]]
- [[sources/PLP-Dynamike|PLP 来源摘要: Dynamike]]
