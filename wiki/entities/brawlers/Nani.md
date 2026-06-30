# Nani

## 基本信息

- 稀有度：Epic
- 定位：Marksman
- 来源：高操作上限的技术型远程英雄

## 攻击特征

- 主攻击一次发射 3 枚弹体，飞行后逐渐收拢。
- 极远端命中上限很高，但近中距离和移动目标会显著降低稳定性。
- 对站位、预判和发射角度要求很高。

## 超级技能特征

- Super 会遥控 `Peep`，可以远程爆炸、击退并破坏地形。
- Nani 本体在操控 Peep 时非常脆弱。
- `Autofocus` 能把远距离 Peep 转成更高爆发，适合打远程对位或固定目标。

## 角色定位总结

Nani 是高上限远程爆发和远程 Peep 威慑英雄。她适合在开阔地图惩罚脆弱长手或用 Peep 改写墙体/血量局面，但非常怕贴脸、召唤物挡线和 Super 期间被切本体。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-06-30-v2
    plp: direct_raw_capture_2026-06-30
    user_notes: none

  capability_vector:
    effective_range: very_long_after_convergence
    projectile_reliability: medium; 极远端收束命中很强，但中距离、机动目标和遮挡会降低稳定性
    burst: very_high_if_full_convergence_or_Autofocus_Peep_hits
    sustained_dps: medium_low; 更偏高爆发窗口而非持续扫线
    objective_damage: high_conditional_in_heist_with_Peep_or_clean_lane
    mobility: conditional_with_Warpin_Time
    survivability: very_low_base_health; Tempered Steel 可保护操控 Peep 期间但不是常驻生存
    engage: medium_with_Peep_pick_or_Warpin_Time
    disengage: low_without_peep_teleport_or_teammate_cover
    anti_aggro: conditional_with_Return_to_Sender_or_Peep_knockback
    anti_tank: medium_if_full_burst_lands
    wall_break: high_with_Peep
    throw_or_wall_bypass: medium_high_with_Peep_remote_path
    area_control: low_medium; 主要靠威慑和爆点，不是持续铺场
    scouting_or_vision: medium_with_Peep_path_information
    team_support: terrain_transform_and_pick_threat
    terrain_destruction: high_with_Peep

  build_switches:
    - build: Warpin' Time / Autofocus / Shield + Damage
      source: "[[sources/PLP-Nani|PLP-Nani]] / [[sources/Fandom-Nani|Fandom-Nani]]"
      changes_capabilities:
        - 把 Peep 从纯远程爆破变成可位移的进攻/收割路线
        - Autofocus 强化长距离 Peep 命中后的秒杀和 Heist 爆发
      enables:
        - long_range_pick
        - peep_wallbreak
        - heist_peep_burst
      mitigates_failure_modes:
        - 缺少主动进场或收割路线
      poor_when:
        - 地图给敌方刺客直接碰到 Nani 本体，或 Peep 路线被召唤物/墙体资源吸收
      bp_use: 默认高上限 build；需要确认 Nani 能安全开 Super
    - build: Return to Sender / Tempered Steel defensive variant
      source: "[[sources/Fandom-Nani|Fandom-Nani]]"
      changes_capabilities:
        - 提高狙击镜像或单发爆发对位中的容错
        - 操控 Peep 期间更不容易被远程秒掉
      enables:
        - sniper_mirror_answer
        - peep_control_under_fire
      mitigates_failure_modes:
        - Piper/Angelo/Mandy 等单发压制
      poor_when:
        - 需要 Warpin' Time 提供进攻位移或 Heist 转化
      bp_use: 对方远程单发爆发过高时的 build requirement

  map_feature_hooks:
    - map_feature_type: open_lane_converged_burst
      uses_feature_by: 在开阔长线用收束三弹和高爆发威慑长手
      objective_conversion: Bounty/Knockout first pick、保星线、远程对位压制
      active_when: Nani 可站极远端发射，敌方没有召唤物或墙体挡线
      fails_if: 敌方有 Max/Leon/Carl 等机动切角，或墙体让三弹无法收束命中
      example_maps:
        - Shooting Star
        - Dry Season
        - Out in the Open
        - New Horizons
      bp_use: candidate_eval.high_burst_long_lane_marksman
    - map_feature_type: peep_wallbreak_pick_or_retarget
      uses_feature_by: Peep 远程绕路、破墙、击退并打残关键目标
      objective_conversion: 打开 Bounty/Knockout 墙体，逼投掷/狙击离开口袋，或创造收割窗口
      active_when: Nani 本体有安全角落，Peep 路线能接触关键墙或低血目标
      fails_if: 本体被切、Peep 被召唤物/墙体骗掉，或破墙后敌方长线更强
      example_maps:
        - Belle's Rock
        - Layer Cake
        - Shooting Star
        - Gem Fort
      bp_use: terrain_state_plan.peep_transform_and_pick
    - map_feature_type: heist_autofocus_peep_safe_pressure
      uses_feature_by: 用远距离 Peep、收束普攻或 Warpin' Time 路线制造固定目标爆发
      objective_conversion: Heist 金库爆发、迫使防守回头、或用破墙打开 safe angle
      active_when: Nani 能安全攒 Super，且金库路线不被召唤物或近身 defender 低成本拦截
      fails_if: 敌方 race 更快，或 Nani 操控 Peep 时被侧路突进击杀
      example_maps:
        - Bridge Too Far
        - Kaboom Canyon
        - Hot Potato
        - Safe Zone
      bp_use: candidate_eval.heist_peep_burst_with_body_risk

  objective_contracts:
    - mode: Bounty_or_Knockout
      can_fulfill:
        - extreme_range_burst
        - peep_wallbreak_or_pick
        - sniper_mirror_pressure
      cannot_fulfill:
        - stable_body_or_area_hold
        - close_range_self_peel_without_resource
      needs_teammate_support:
        - anti_dive
        - body_or_vision_to_protect_Super_cast
      false_positive: Nani 的长线价值依赖命中窗口；机动和召唤物会显著降低稳定性
    - mode: Heist
      can_fulfill:
        - peep_safe_burst
        - remote_wallbreak
        - long_lane_safe_pressure
      cannot_fulfill:
        - reliable_standing_safe_DPS_under_dive
      needs_teammate_support:
        - lane_body_or_defender_clear
        - anti_assassin_cover
      false_positive: Heist 适配来自 Peep/爆发窗口，不是持续站桩打库

  failure_modes:
    - id: super_body_vulnerable
      active_when: Nani 操控 Peep 时敌方有 Leon/Max/Mortis/Chuck 等能直接碰本体
      exposed_by: Fandom Super 机制与低生命值字段
      mitigation: 只在安全角落开 Super，或配队友视野/peel
      bp_use: must_avoid_or_needs_protection
    - id: convergence_unreliable_into_mobility
      active_when: 目标能横移、加速、dash 或在中距离打乱三弹收束
      exposed_by: Fandom 攻击机制
      mitigation: 选择开阔极远线、用队友 slow/control 固定目标
      bp_use: false_positive_filter
    - id: bodies_and_spawnables_absorb_shots
      active_when: Mr. P、Pam、Pearl、Eve 等用召唤物/身体/分体挡住三弹或 Peep
      exposed_by: PLP counteredBy
      mitigation: 先清资源，或只在资源不在路线上时开 Peep
      bp_use: must_answer_body_block_before_nani

  conditional_matchup_seeds:
    - target: Piper_or_Angelo_or_Belle_or_Mandy
      direction: subject_favored
      source: "[[sources/PLP-Nani|PLP-Nani]]"
      mechanism: Nani 的极远收束爆发、Return to Sender 变体和 Peep 威慑能惩罚单发长狙站位
      active_when: 地图开阔，Nani 能站极远端，目标没有召唤物/墙体保护
      fails_when: 目标先取得安全角度，或 Nani 被 side pressure 迫使中距离出手
      bp_use: sniper_mirror_response_candidate
    - target: Mortis_or_Fang_or_8-Bit_or_R-T
      direction: subject_favored
      source: "[[sources/PLP-Nani|PLP-Nani]]"
      mechanism: 满额爆发或 Peep 可惩罚直线进场/低机动目标，但条件是先看到路线
      active_when: 接近路线长而可预判，Nani 有 Super/Return to Sender 或队友 peel
      fails_when: 目标从草墙贴脸，或 Nani 没有资源时被逼近
      bp_use: conditional_anti_entry_or_low_mobility_pick
    - target: Max_or_Leon_or_Carl_or_Eve
      direction: target_favored
      source: "[[sources/PLP-Nani|PLP-Nani]]"
      mechanism: 速度、隐身、回旋镖压力或隔水/幼体资源会破坏 Nani 的收束命中和 Peep 安全窗口
      active_when: 地图有侧路、水域、墙体或 dodge space，让目标选择 first contact
      fails_when: 路线被队友视野锁住，或 Nani 保留 Peep/Return to Sender 等资源等真正进场
      bp_use: avoid_without_vision_or_peel
    - target: Pam_or_Mr_P_or_Pearl_or_Amber
      direction: target_favored
      source: "[[sources/PLP-Nani|PLP-Nani]]"
      mechanism: 高血量、召唤物、持续火力或火区能吸收/压制 Nani 的单次爆发窗口
      active_when: 目标能站在 objective 附近并让 Nani 的三弹或 Peep 打到非核心资源
      fails_when: Nani 有清晰极远线，或队友先拆掉 summon/body 让 Peep 直达本体
      bp_use: body_block_and_resource_warning

  slot_notes:
    slot_1: 只适合极开阔且反机动压力低的图；早手暴露后很容易被 Max/Leon/Mr. P 等功能回答。
    slot_2_3: 可作为长线镜像或 Heist 爆发计划的一部分，但需要补保护本体的队友。
    slot_4_5: 用于回答敌方脆弱长手或缺机动阵容，同时检查敌方 6 位是否能补切本体。
    slot_6: 敌方三人缺召唤物、缺机动、缺隔墙压制时，Nani 是高上限惩罚位。
```

## 关联页面

- [[sources/Fandom-Nani|Fandom 来源摘要: Nani]]
- [[sources/PLP-Nani|PLP 来源摘要: Nani]]
