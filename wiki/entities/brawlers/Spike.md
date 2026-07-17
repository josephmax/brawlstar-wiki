# Spike

## 基本信息

- 稀有度：Legendary
- 定位：Damage Dealer
- 类型：中距离爆发与控区英雄

## 攻击特征

- 主攻击命中或到达终点后爆开并向周围散射尖刺。
- `Curveball` 会改变尖刺轨迹，提高绕角骚扰和命中压力。
- 贴近目标或固定目标时，尖刺多段命中能形成很高爆发。

## 超级技能特征

- Super 会生成持续伤害和减速区域。
- 能逼退站点、切断持球/进场路线，也能让队友补伤害。

## 角色定位总结

Spike 是高爆发、区域减速和中距离卡点英雄。他不是纯长手，也不是纯投掷；BP 中要把他理解成“惩罚身体/路线/目标区拥挤”的控制爆发位。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-07-17
    plp: direct_raw_capture_2026-06-30
    user_notes: none

  capability_vector:
    effective_range: mid_long
    projectile_reliability: medium_high_with_Curveball; 角度压力强但直线远端不等于狙击稳定性
    burst: very_high_at_close_or_fixed_target
    sustained_dps: medium; 装填慢但命中质量高；普通直接命中节奏约需 4 发主攻击充满 Super，多段尖刺命中可缩短循环
    objective_damage: high_conditional_with_Popping_Pincushion_or_close_safe_access
    mobility: low
    survivability: low_medium; 生命值不高，依赖距离和 Life Plant/队友；Fertilize 可按 Super 实际伤害回复 75%
    engage: low
    disengage: low
    anti_aggro: high_if_Super_or_close_burst_ready
    anti_tank: high; 多段尖刺和减速区域惩罚前排
    wall_break: none
    throw_or_wall_bypass: medium_with_spike_split_angles
    area_control: high_with_Super
    scouting_or_vision: medium; Curveball/散射可检查草边和角落
    team_support: slow_zone_and_route_denial
    crowd_control: high_slow_with_Super

  build_switches:
    - build: Popping Pincushion / Curveball / Shield + Damage
      source: "[[sources/PLP-Spike|PLP-Spike]] / [[sources/Fandom-Spike|Fandom-Spike]]"
      changes_capabilities:
        - Curveball 提高中距离命中和绕角骚扰
        - Popping Pincushion 提高近身反打和固定目标爆发
      enables:
        - anti_tank_burst
        - objective_choke_control
        - heist_fixed_target_burst
      mitigates_failure_modes:
        - 纯普攻难以瞬间清前排
      poor_when:
        - 需要持续远程狙击、开墙或逃生位移
      bp_use: 默认竞技 build；地图/模式要求 close burst 或目标区控制时价值最高
    - build: Life Plant / Fertilize sustain variant
      source: "[[sources/Fandom-Spike|Fandom-Spike]]"
      changes_capabilities:
        - Life Plant 提供可破坏挡线并在摧毁时治疗；Fertilize 按 Super 实际伤害回复 75%，让已充好的慢区同时成为自保区
      enables:
        - zone_anchor_survival
        - projectile_blocking
      mitigates_failure_modes:
        - 被远程单发或投掷 chip 压出位置
      poor_when:
        - 需要 Popping Pincushion 的爆发打库或反坦
      bp_use: Hot Zone/Gem Grab 需要活在目标边缘时的 build requirement

  map_feature_hooks:
    - map_feature_type: zone_choke_slow_and_area
      uses_feature_by: Super 覆盖入口、减速前排，并让队友集火被困目标
      objective_conversion: Hot Zone 站圈时间、重进场税和防守反打
      active_when: Spike 已通过约 4 发普通直接命中或多段尖刺命中取得 Super，且热区入口/L 墙附近形成敌方必须经过的重复路线
      fails_if: 敌方投掷/长手从圈外清 Spike，或目标有跳跃/无敌/强位移绕开区域
      example_maps:
        - Ring of Fire
        - Open Business
        - Dueling Beetles
        - Parallel Plays
      bp_use: map_bp_factors.zone_slow_and_anti_body
    - map_feature_type: gem_mine_curveball_control
      uses_feature_by: Curveball 和散射尖刺检查草边/墙角，Super 切 carrier 退路
      objective_conversion: 控矿、保护 carrier、惩罚敌方倒计时撤退
      active_when: 宝石矿附近有入口/草边/墙角让敌人反复经过
      fails_if: 敌方投掷占深口袋，或 Spike 被长手从安全距离压退
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Double Swoosh
      bp_use: map_bp_factors.mine_route_control
    - map_feature_type: brawl_ball_goal_choke_and_anti_tank
      uses_feature_by: Super 减速持球/防守者，贴近多段爆发清前排或门前身体
      objective_conversion: 防守进球、创造射门窗口、惩罚坦克推进
      active_when: 球路经过草口、窄口或门前防守区，队友能接 slow 后的击杀
      fails_if: 敌方投掷/位移 scorer 从侧路绕开，或我方没有破门/得分手
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Pinball Dreams
        - Triple Dribble
      bp_use: slot_task.ball_route_slow_and_body_clear
    - map_feature_type: heist_popping_pincushion_safe_or_defense
      uses_feature_by: Popping Pincushion 和贴近多段尖刺打固定 safe 或入库前排
      objective_conversion: 短窗口 safe burst、反入库坦克、迫使防守资源
      active_when: Spike 能通过线权/草墙接近 safe，或敌方前排必须进入他的爆发区
      fails_if: 开阔长线让 Spike 永远摸不到 safe，或敌方远程 race 更快
      example_maps:
        - Hot Potato
        - Pit Stop
        - Kaboom Canyon
        - Safe Zone
      bp_use: candidate_eval.heist_close_burst_with_access_check

  objective_contracts:
    - mode: Hot Zone_or_Gem Grab
      can_fulfill:
        - route_slow_and_area_denial
        - anti_body_burst
        - carrier_or_zone_retreat_cut
      cannot_fulfill:
        - pure_long_range_anchor
        - wallbreak_to_open_thrower_pocket
      needs_teammate_support:
        - thrower_or_long_range_answer
        - actual_zone_body_or_carrier
      false_positive: Spike 控区强，但被隔墙压制时不能单独站点
    - mode: Brawl Ball
      can_fulfill:
        - anti_tank_goal_defense
        - slow_scorer_or_defender
        - goal_choke_control
      cannot_fulfill:
        - primary_wallbreak
        - fastest_scorer
      needs_teammate_support:
        - scorer_or_wallbreak
        - anti_thrower_cover
      false_positive: 防守慢住不等于能进球，必须有得分转化
    - mode: Heist
      can_fulfill:
        - close_safe_burst_if_access_exists
        - anti_aggro_defense
      cannot_fulfill:
        - stable_remote_safe_DPS
      needs_teammate_support:
        - lane_win_or_speed_to_reach_safe
        - ranged_race_component
      false_positive: 只有能摸到 safe 或能反入库时才是 Heist 候选

  failure_modes:
    - id: super_control_requires_charge_setup
      active_when: "阵容把 Spike 的 slow zone 当作开局或每波必有的基础控制，但他尚未完成普通约 4 发直接命中的充能循环"
      exposed_by: "[[sources/Fandom-Spike|Fandom-Spike]] 当前 AttackSuperCharge 使普通直接命中节奏约需 4 发攻击；多尖刺命中才会更快"
      mitigation: "先用 Curveball/路线限制稳定命中，或让队友守住第一波；只有确认 Super 已有时才把 slow zone 计入硬控制"
      bp_use: resource_tracking.super_zone_available
    - id: outranged_or_walled_out
      active_when: 敌方投掷/长狙在墙后或开阔远端攻击，Spike 不能稳定接触
      exposed_by: Fandom 射程与 PLP counteredBy
      mitigation: 队友开墙、突进清口袋、选择中距离目标图
      bp_use: false_positive_filter
    - id: mobility_bypasses_slow_zone
      active_when: Mico/Melodie/Edgar/Chuck 等从跳跃、dash 或路线技能绕过 Super 区域
      exposed_by: PLP counteredBy
      mitigation: 保存 Super 到落点，配硬控/视野，或避免开放多路线图
      bp_use: must_avoid_or_needs_peel
    - id: no_objective_conversion
      active_when: Spike 只消耗但队伍缺站圈、carrier、scorer 或 safe DPS
      exposed_by: BP objective_contract
      mitigation: 搭配目标身体、得分手或远程 race 组件
      bp_use: role_coverage_check

  conditional_matchup_seeds:
    - target: El_Primo_or_Fang_or_Meg_or_Gale
      direction: subject_favored
      source: "[[sources/PLP-Spike|PLP-Spike]]"
      mechanism: 多段尖刺和 Super slow 惩罚必须进入中近距离的前排/控制英雄
      active_when: 目标要穿过 choke、草口、球路或站圈入口，Spike 持有 ammo/Super
      fails_when: 目标用队友投掷/长手先压退 Spike，或从多路线同时进场
      bp_use: anti_body_or_route_response
    - target: Bea_or_Lou_or_Glowy_or_Jae_yong
      direction: subject_favored
      source: "[[sources/PLP-Spike|PLP-Spike]]"
      mechanism: Curveball 和区域 slow 能压迫低血或节奏型控制/支援位，让他们难以稳定站目标边缘
      active_when: 地图是中距离目标区，目标必须在 Spike 射程内反复 peek
      fails_when: 目标保持全开放远线或有队友清掉 Spike 的站位
      bp_use: midrange_control_pressure_candidate
    - target: Mico_or_Melodie_or_Edgar_or_Chuck
      direction: target_favored
      source: "[[sources/PLP-Spike|PLP-Spike]]"
      mechanism: 跳跃、连续 dash 或路径技能可绕过 Spike 的预置慢区并直接攻击低血本体
      active_when: 地图有侧路、墙草或 safe/goal route 让他们选择 first contact
      fails_when: Spike 预判落点留 Super，且队友有硬控或爆发接 slow
      bp_use: avoid_without_peel_or_route_lock
    - target: Larry_and_Lawrie_or_Jessie_or_Frank_or_Damian
      direction: target_favored
      source: "[[sources/PLP-Spike|PLP-Spike]]"
      mechanism: 召唤物、投掷/墙压、重身体或特殊路线会消耗 Spike 弹药并逼他离开中距离爆发点
      active_when: 地图墙体保护资源，或 objective 迫使 Spike 先清额外身体
      fails_when: 队友先清 summon/wall pocket，Spike 只负责 Super slow 和爆发收割
      bp_use: must_answer_resource_or_wall_control

  slot_notes:
    slot_1: 可以在目标区/反坦价值稳定的图先手，但要警惕投掷和机动后手。
    slot_2_3: 适合建立 anti-body 和控区基本面，尤其队友已有远程/开墙时。
    slot_4_5: 用于惩罚敌方缺投掷/缺机动的前排或中距离阵容，同时补足我方目标区控制。
    slot_6: 敌方三人已经暴露必须走 choke 或缺远程答案时，Spike 是高收益 last pick。
```

## 关联页面

- [[sources/Fandom-Spike|Fandom 来源摘要: Spike]]
- [[sources/PLP-Spike|PLP 来源摘要: Spike]]
