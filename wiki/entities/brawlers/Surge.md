# Surge

## 基本信息

- 稀有度：Legendary
- 定位：Damage Dealer
- 类型：阶段成长与反近身输出英雄

## 攻击特征

- 主攻击命中敌人后会分裂，后续阶段会增加移速、射程和分裂数量。
- 初始阶段移速慢、射程一般且装填慢，必须安全获得并使用 Super；`Power Surge` 只会在 5 秒内提高 30% Super 充能率，Buffie 额外提高装填，不会直接补阶段。
- `To the Max!` 让攻击撞墙反弹；只有 Buffie 会让反弹弹体再分裂，是墙体/走廊图的条件化输出增强。

## 超级技能特征

- Super 让 Surge 短距离跳跃，空中期间免疫大多数直接伤害，落地造成伤害和击退并升级。
- `Serve Ice Cold` 让 Surge 在开局和复位时自带满 Super，可立即用一次 Party Tricks 重新取得速度阶段，但不会直接保留旧阶段。
- `Power Shield` 可以吃下一次弹道伤害并补弹药，PLP 特别标注可用于面对刺客或坦克。

## 角色定位总结

Surge 的 BP 价值来自“阶段成长后的中短距离压制”和“对近身/坦克路线的反制”。他不是稳定开局长手，也不是投掷；选他之前必须确认地图和 slot 能让他安全拿到第一阶段，或者当前局面本来就需要用跳跃、击退、Power Shield 和高爆发处理敌方近身路线。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-07-10
    plp: direct_raw_capture_2026-06-30
    user_notes: none

  capability_vector:
    effective_range: mid_at_stage0_long_after_stage2
    projectile_reliability: medium_high_after_stage; 初始阶段较短且慢，成长后长线和分裂压力明显提高
    burst: high_with_three_ammo_or_split_hits
    sustained_dps: medium_low_reload; 装填慢但单轮爆发高
    objective_damage: low_medium; 不是 Heist 主 race
    mobility: medium_high_after_stage1_or_Super_jump
    survivability: medium; Super 免疫窗口和 Power Shield 提供关键对拼容错
    engage: medium; 短跳可接近或躲技能，但不是长距离刺客进场
    disengage: medium_with_Super_or_speed
    anti_aggro: high_when_Super_or_Power_Shield_available
    anti_tank: high; 近身爆发、击退和 Power Shield 适合处理直线前排
    wall_break: none
    throw_or_wall_bypass: low; Super 可跳墙但主攻击不是投掷
    area_control: medium_with_split_projectiles
    scouting_or_vision: low
    team_support: low
    crowd_control: knockback_on_Super_landing

  build_switches:
    - build: Power Surge / Serve Ice Cold / Shield + Damage
      source: "[[sources/PLP-Surge|PLP-Surge]] / [[sources/Fandom-Surge|Fandom-Surge]]"
      changes_capabilities:
        - Power Surge 在 5 秒内提高 30% Super 充能率；Buffie 同时提高 30% 装填，用来缩短第一 Super 的获取窗口
        - Serve Ice Cold 让开局、复活、进球后和 Knockout 新回合自带满 Super，可立即用 Party Tricks 重新取得 Stage 1 速度
        - Shield/Damage 提高低血与爆发对拼容错
      enables:
        - brawl_ball_full_super_after_reset
        - gem_mid_stage_control
        - anti_tank_response
      mitigates_failure_modes:
        - stage0_tempo_tax
        - death_or_goal_reset_removing_speed
      poor_when:
        - 地图是纯长线，敌方不用进入 Surge 的中距离爆发区
      bp_use: 默认竞技 build；需要先判断满 Super 或加速充能能否安全转换成 Stage 1，而不是把 Gadget 当作直接升阶
    - build: Power Shield into assassins_or_tanks
      source: "[[sources/PLP-Surge|PLP-Surge]] / [[sources/Fandom-Surge|Fandom-Surge]]"
      changes_capabilities:
        - 下一次受击减伤并补 2 ammo，显著提升近身反杀窗口
      enables:
        - anti_assassin_duel
        - anti_tank_ammo_refund
      mitigates_failure_modes:
        - 慢装填导致三发后真空
        - 敌方贴脸一次性爆发
      poor_when:
        - 敌方主要从投掷、持续 area 或多段 poke 消耗，不给单发 Shield 高价值
      bp_use: 对面 2-3 位已暴露刺客/坦克时的 build requirement
    - build: To the Max! wall_split_variant
      source: "[[sources/Fandom-Surge|Fandom-Surge]]"
      changes_capabilities:
        - 主攻击撞墙后反弹；Buffie 才会让反弹弹体再分裂，让墙边走廊和窄口形成额外火力角度
      enables:
        - wall_split_choke_pressure
        - faster_super_charge_in_wall_lanes
      mitigates_failure_modes:
        - 目标躲在墙后或窄口不直接露头
      poor_when:
        - 地图开阔或更需要 Serve Ice Cold 在复位后立即提供满 Super
      bp_use: 墙体走廊图的条件 build，不是默认替换 Serve Ice Cold

  map_feature_hooks:
    - map_feature_type: brawl_ball_stage_speed_and_anti_aggro
      uses_feature_by: Serve Ice Cold 让开局/复位自带满 Super，可立即用 Party Tricks 重新取得速度阶段；Super 还能击退持球人或跳过小墙
      objective_conversion: 抢球、反推进、得分窗口和门前防守
      active_when: 球路需要中距离对拼或反近身，Surge 有 Stage 1/2、自带满 Super，或能用 Power Surge 加快充能
      fails_if: Surge 被长线/投掷压到无法充 Super，或敌方只用远程控球不进入中距离
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Pinball Dreams
        - Triple Dribble
      bp_use: candidate_eval.brawl_ball_anti_body_scaling_pick
    - map_feature_type: gem_mid_stage_control
      uses_feature_by: 升级后移速和射程提高，能在宝石矿边缘惩罚短手、挡突进并保持中路线权
      objective_conversion: 控矿、保护 carrier、打断敌方侧草前压
      active_when: 地图允许 Surge 通过中距离命中积累第一 Super，且队友能先处理投掷口袋
      fails_if: 敌方投掷/长手在墙后压制 Stage 0 Surge，或 carrier 需要纯远程支援
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Double Swoosh
      bp_use: map_bp_factors.mid_control_with_scaling_risk
    - map_feature_type: wall_split_choke_pressure
      uses_feature_by: To the Max! 让主攻击撞墙反弹，Buffie 或 Hypercharge 的分裂进一步惩罚墙角/窄口站位
      objective_conversion: 窄口压制、充能、反投掷辅助和边路控制
      active_when: 墙体仍完整且 Surge 可以站到中距离，敌方没有低成本投掷压身位
      fails_if: 地图被开成纯长线，或墙后目标是投掷并能先逼退 Surge
      example_maps:
        - Pinball Dreams
        - Hard Rock Mine
        - Gem Fort
        - Belle's Rock
      bp_use: terrain_state_plan.wall_split_variant

  objective_contracts:
    - mode: Gem Grab
      can_fulfill:
        - mid_lane_anti_aggro
        - stage_scaling_lane_control
        - carrier_peel_after_speed_stage
      cannot_fulfill:
        - safe_initial_carrier_on_open_long_map
        - thrower_pocket_answer_without_stage_or_route
      needs_teammate_support:
        - early_mid_cover_until_first_super
        - wall_or_thrower_answer
      false_positive: Surge 强在成长后控线，Stage 0 被压死时无法承担中路基本面
    - mode: Brawl Ball
      can_fulfill:
        - anti_tank_goal_defense
        - rapid_stage1_recovery_after_reset
        - knockback_disarm_or_score_window
      cannot_fulfill:
        - primary_wallbreak
        - long_range_open_field_anchor
      needs_teammate_support:
        - grass_control_or_ball_carrier
        - scorer_followup
      false_positive: 能反前排不等于能进球，阵容仍需破门或持球转换
    - mode: Bounty_or_Knockout
      can_fulfill:
        - situational_last_pick_anti_assassin_or_tank
      cannot_fulfill:
        - stable_open_sniper_basic
      needs_teammate_support:
        - first_super_setup
        - cover_against_long_range
      false_positive: 开阔长线图不要把 Surge 当作默认远程；他常在拿阶段前被消耗

  failure_modes:
    - id: stage0_tempo_tax
      active_when: Surge 开局或复位后还没有 Stage 1，移速慢、射程短、装填慢
      exposed_by: Fandom 阶段机制和 tips
      mitigation: Serve Ice Cold 直接提供满 Super 以取得 Stage 1，或用 Power Surge 加快充能；同时依靠队友保线和中距离接触
      bp_use: slot_fit_and_first_wave_risk
    - id: outranged_or_thrown_before_scaling
      active_when: Tick/Barley/Sprout/Willow 或 Piper/Belle 等在 Surge 成长前从安全距离压制
      exposed_by: PLP counteredBy 与地图长线/投掷口袋模型
      mitigation: 搭配开墙/投掷答案，或只在敌方已缺长线/投掷时后手
      bp_use: must_avoid_or_pair_with_answer
    - id: slow_reload_after_commit
      active_when: Surge 跳入或三发爆发未完成击杀，随后进入装填真空
      exposed_by: Fandom reload=2 seconds and Power Shield ammo refund mechanic
      mitigation: Power Shield、队友补伤、避免孤立深跳
      bp_use: false_positive_filter_for_aggressive_pick
    - id: reset_sensitive_modes
      active_when: Knockout 回合结束、Brawl Ball 进球或死亡导致阶段回退，需要重新使用 Super 取得速度阶段
      exposed_by: Fandom Super/Star Power 说明
      mitigation: 使用 Serve Ice Cold 保证复位时自带满 Super，并确认第一次 Party Tricks 能安全落地；否则把 Surge 作为后手对位而非整局唯一核心
      bp_use: build_requirement_check

  conditional_matchup_seeds:
    - target: Bull_or_Jacky_or_El_Primo_or_Frank
      direction: subject_favored
      source: "[[sources/PLP-Surge|PLP-Surge]]"
      mechanism: Super 击退/免疫、Power Shield 弹药返还和近身爆发能惩罚直线进入的高血量前排
      active_when: 目标必须穿过可见 choke、球路或宝石入口，Surge 有 Super/Power Shield 或至少 Stage 1
      fails_when: 前排由投掷/治疗/速度支援送到贴脸，或 Surge 仍是 Stage 0 且无资源
      bp_use: anti_tank_response_pick
    - target: Edgar_or_Bibi_or_Buzz_or_Doug
      direction: subject_favored
      source: "[[sources/PLP-Surge|PLP-Surge]]"
      mechanism: 跳跃击退、短距离免疫和三发爆发可以反打单一路线近身英雄
      active_when: 接近路线可预判，Power Shield 或 Super 留给 first contact
      fails_when: 敌方多路线夹击、先骗出 Super，或地图草墙让 Surge 无法预读
      bp_use: anti_aggro_route_guard
    - target: Tick_or_Barley_or_Sprout_or_Willow
      direction: target_favored
      source: "[[sources/PLP-Surge|PLP-Surge]]"
      mechanism: 投掷/墙后控制在 Surge 成长前压低血量并阻止他用直线主攻击充 Super
      active_when: 墙体完整、投掷有安全口袋、Surge 队伍缺开墙或 dive
      fails_when: 地图打开，Surge 已升级且能用速度压到中距离
      bp_use: must_answer_thrower_before_surge
    - target: Belle_or_Crow_or_Bonnie_or_Piper
      direction: target_favored
      source: "[[sources/PLP-Surge|PLP-Surge]]"
      mechanism: 更长射程、持续毒伤或远程爆发会在 Surge 成长前削血，迫使他交 Super 做防守
      active_when: 地图开阔、Surge 缺掩体/速度阶段，敌方能保持远距
      fails_when: 地图有墙角分裂/中距离接触，或 Surge 借 Power Surge 直接进入压制阶段
      bp_use: avoid_open_long_lane_early_pick

  slot_notes:
    slot_1: 风险较高；只有 Gem/Ball 中距离基本面强、可用 Power Surge 兜底且敌方低成本投掷/长线不明显时才考虑。
    slot_2_3: 适合回答敌方先手坦克/刺客，同时建立 Gem/Ball 成长控制路线。
    slot_4_5: 可修复己方反近身缺口，但要避免把投掷/长线弱点留给敌方 6 位。
    slot_6: 敌方已无投掷/长线答案且必须通过中近距离目标路线时，Surge 可以作为高上限惩罚 pick。
```

## 关联页面

- [[sources/Fandom-Surge|Fandom 来源摘要: Surge]]
- [[sources/PLP-Surge|PLP 来源摘要: Surge]]
