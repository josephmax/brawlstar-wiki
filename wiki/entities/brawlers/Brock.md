# Brock

## 基本信息

- 稀有度：Rare
- 定位：Marksman
- 类型：远程火箭压制英雄

## 攻击特征

- 主攻击是单发远程火箭
- 命中后带范围溅射和燃烧地面效果
- 适合在安全距离持续压线

## 超级技能特征

- Super 会对大范围区域进行连续火箭轰炸
- 兼顾伤害与拆墙
- 非常适合开图、逼位和打退阵型

## 适合场景

- 开阔地图
- 需要拆墙的对局
- 需要远距离消耗和控场的模式
- 需要提前预判敌人走位的场景

## 角色定位总结

Brock 是远程炮击和拆墙开图的代表英雄。和 `Colt` 相比，他更强调单发高溅射和地图改造；和 `Barley` 相比，他更偏瞬间轰炸而不是持续铺场。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-07-17
    plp: direct_raw_capture_2026-07-11
    user_notes: none

  capability_vector:
    effective_range: "long; Rocket No. 4 Buffie 每 6 秒让下一发额外射程 2 格，不是持续射程"
    projectile_reliability: medium; 火箭弹速慢，需要预判，打固定目标更稳定
    burst: high_when_ammo_or_super_available
    sustained_dps: medium; 慢装填，需要 Reload Gear 或弹药管理
    objective_damage: high_in_heist_when_safe_angle_exists
    mobility: "conditional_high_with_aimable_Rocket_Laces; 可瞄准跳跃最高 4 格并越墙/水，命中敌方的 Buffie 还提供 2 秒 30% 加速"
    survivability: low_base_health; Shield Gear 可缓解但不能替代保护
    engage: low
    disengage: "medium_high_with_Rocket_Laces; 起跳和落地两端均有击退/伤害，但状态效果与持续伤害仍会保留"
    anti_aggro: "conditional; 可瞄准 Rocket Laces 以双端击退跨墙脱离，但有 20 秒冷却且不是持续硬控"
    anti_tank: medium_if_range_kept
    wall_break: "high; 跟随 Brock 移动轨迹的 Super 可大面积改图，Rocket Fuel 提供单发精确开墙"
    throw_or_wall_bypass: medium; Super 可越墙轰炸
    area_control: "medium_high; 溅射、火焰地面、跟随移动的 Super 与 Rocket Fuel Buffie 分裂火箭共同逼位"
    scouting_or_vision: low
    team_support: "terrain_transform_long_range_pressure_and_conditional_double_knockback"
    terrain_destruction: high

  build_switches:
    - build: Rocket Laces / More Rockets / Damage + Shield
      source: "[[sources/PLP-Brock|PLP-Brock]]"
      changes_capabilities:
        - "Rocket Laces 可瞄准跳最高 4 格、越墙/水，在起跳与落地的 2 格圆内击退并造成伤害"
        - "Rocket Laces Buffie 命中英雄后再获得 2 秒 30% 加速，能把一次自保转成二次重定位"
        - "More Rockets 增加 Super 火箭并压缩发射间隔；Buffie 让 Brock 施放 Super 时提速 30%"
        - "Damage + Shield 更偏向爆发阈值与低血容错"
      enables:
        - long_range_pressure
        - anti_aggro_escape_or_obstacle_crossing
        - moving_super_channel_reposition
      mitigates_failure_modes:
        - low_health_ambush
      poor_when:
        - draft 需要精确开关键墙而不是保命
        - 对局需要 Reload Gear 支撑持续压制，当前 build 的装填空窗会更明显
        - "在 Super 施放中使用 Rocket Laces 会直接取消剩余轰炸，不能把两个窗口无成本叠加"
      bp_use: 默认竞技 build 候选，不直接等于最终推荐
    - build: Rocket Fuel wall-break variant
      source: "[[sources/Fandom-Brock|Fandom-Brock]]"
      changes_capabilities:
        - "发射一枚更快、更宽的大火箭，不必先攒 Super 就能精确打开关键墙体"
        - "该火箭不带地面火，且伤害低于普攻；Buffie 爆炸后再分成 4 枚 75% 伤害小火箭"
      enables:
        - wall_break_transform
        - goal_barrier_opening
        - safe_angle_creation
        - post_break_area_punish
      mitigates_failure_modes:
        - 被投掷或墙体掩护低成本卡住
      poor_when:
        - 开墙会让敌方远程或突进更受益
        - "敌方召唤物/身体能提前挡下大火箭，使预定墙体未被打开"
      bp_use: 地图状态需要主动改图时的 build requirement
    - build: "Rocket No. 4 long-sightline cadence variant"
      source: "[[sources/Fandom-Brock|Fandom-Brock]]"
      changes_capabilities:
        - "弹药上限从 3 变 4，但装填速度不变，打空后全回满的时间更长"
        - "Buffie 每 6 秒充好一次，仅让下一发多 2 格射程；这是可储存的单发对线资源，不是持续 11 格射程"
      enables:
        - intermittent_range_advantage
        - four_ammo_burst_or_round_start_hold
      mitigates_failure_modes:
        - relative_range_shortfall_into_marksmen
      best_when: "Bounty/Knockout 长线节奏允许保留充能发，且一发超距离消耗能改变站位"
      poor_when: "对局要求持续快速清线，或敌方高机动使充能发也不稳定"
      bp_use: "candidate_eval.intermittent_extra_range_not_baseline_range"

  map_feature_hooks:
    - map_feature_type: heist_remote_safe_angle
      uses_feature_by: 长射程火箭从隔水/长直线安全角度压线和打库
      objective_conversion: Heist 远程 safe DPS、迫使敌方回防或让队友赢另一侧
      active_when: 视线长、接近路径单一、Brock 不需要越过危险地形就能碰到金库
      fails_if: 敌方有侧草突进、多路线夹击、或我方缺少反突进保护
      example_maps:
        - Bridge Too Far
        - Safe Zone
        - Kaboom Canyon
        - Hot Potato
      bp_use: required_capabilities.heist_remote_safe_damage
    - map_feature_type: selective_wall_break_transform
      uses_feature_by: Super 或 Rocket Fuel 破关键墙，把墙体保护转成远程对枪图
      objective_conversion: 打开反投掷角度、剥夺 Bounty/Knockout 掩体、扩大长线领先
      active_when: 我方阵容能利用开墙后的长线
      fails_if: 过度开墙反而帮助敌方射程或突进
      example_maps:
        - Shooting Star
        - Belle's Rock
        - Layer Cake
        - Gem Fort
      bp_use: terrain_state_plan.transform
    - map_feature_type: charged_extra_range_long_sightline
      uses_feature_by: "Rocket No. 4 Buffie 在 6 秒节奏后储存一发额外 2 格射程火箭"
      objective_conversion: "在 Bounty/Knockout 开局、回合重置或卡位期先逼退长手，为后续普通射程换血抢位"
      active_when: "长直线有可预判目标，Brock 能保留该发而不被迫先清路"
      fails_if: "需要持续输出、高机动目标躲掉充能发，或把单发射程误当整个对线期的常驻射程"
      example_maps:
        - Shooting Star
        - Dry Season
        - Out in the Open
        - Safe Zone
      bp_use: "map_factor_fit.intermittent_range_cadence"
    - map_feature_type: brawl_ball_goal_wallbreak_and_defender_zone
      uses_feature_by: Rocket Fuel 或 Super 打开球门/防守墙，用溅射/分裂火箭逼位，或用 Rocket Laces 起跳+落地击退阻断持球线
      objective_conversion: 把一次线权或击杀转成射门窗口
      active_when: 队友有 scorer / tank pressure / pass route 可以立刻吃到破门收益
      fails_if: 我方没有得分手，或开墙后敌方远程/突进更容易反打
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.goal_wallbreak_window_with_followup

  objective_contracts:
    - mode: Heist
      can_fulfill:
        - long_range_safe_damage
        - wall_break_to_create_safe_angle
      cannot_fulfill:
        - body_on_safe_or_base_anchor
      needs_teammate_support:
        - anti_aggro
        - lane_control_after_walls_open
      false_positive: 只会开墙但没有 follow-up safe DPS 时价值不足
    - mode: Bounty_or_Knockout
      can_fulfill:
        - long_range_chip
        - intermittent_11_tile_range_opening_with_Rocket_No_4_Buffie
        - wall_break_snowball
        - force_split_with_super
      cannot_fulfill:
        - reliable_close_range_duel
      needs_teammate_support:
        - bush_check_or_peel
      false_positive: "Rocket No. 4 的 11 格只是每 6 秒一发；长线图若敌方有高机动接近和队友保护不足，Brock 仍会变成暴露点"
    - mode: Brawl Ball
      can_fulfill:
        - break_goal_wall
        - create_scoring_window
        - conditional_takeoff_and_landing_knockback_defense
      cannot_fulfill:
        - primary_ball_carrier
      needs_teammate_support:
        - scorer_or_tank_pressure
      false_positive: 破门不等于能推进，必须有队友把窗口转成进球

  failure_modes:
    - id: slow_projectile_into_mobility
      active_when: 敌方有 Stu/Max/Mortis/Leon 等高机动或多接近路线
      exposed_by: PLP counteredBy 与 Fandom 慢弹道说明
      mitigation: Rocket Laces、队友 peel、选择长线且入口单一地图
      bp_use: must_avoid_or_needs_protection
    - id: low_health_ambush
      active_when: 草丛、侧墙、刺客或坦克能低成本贴脸
      exposed_by: Fandom tips 与 PLP notes
      mitigation: Shield Gear、视野队友、保墙/开墙计划
      bp_use: false_positive_filter
    - id: overbreak_helps_enemy
      active_when: 开墙后敌方远程或突进收益大于我方
      exposed_by: BP 地图建模与决策规范
      mitigation: 只开关键墙，并确认 follow-up
      bp_use: terrain_state_plan_check
    - id: charged_range_is_intermittent
      active_when: "候选评估把 Rocket No. 4 Buffie 的单发 11 格射程当成持续对线能力，或 Brock 被迫先清线消耗充能发"
      exposed_by: "[[sources/Fandom-Brock|Fandom-Brock]] current six-second charge-bar mechanic"
      mitigation: "只把充能发算作开局/卡位资源，并按 9 格基础射程审计其余时间"
      bp_use: "range_false_positive_filter"
    - id: super_channel_commitment_and_laces_cancel
      active_when: "Brock 施放 Super 期间无法攻击/装填，被击退、拉、眩晕或主动用 Rocket Laces 时剩余轰炸被取消"
      exposed_by: "[[sources/Fandom-Brock|Fandom-Brock]] current Rocket Rain and Rocket Laces interaction"
      mitigation: "先逼掉控制，用 More Rockets Buffie 移速调整轨迹，不要无计划地叠加 Laces"
      bp_use: "super_resource_commitment_check"

  conditional_matchup_seeds:
    - target: 8-Bit_or_Pam_or_Nita_or_Hank
      direction: subject_favored
      source: "[[sources/PLP-Brock|PLP-Brock]]"
      mechanism: 长射程与溅射惩罚低机动或站位笨重目标
      active_when: 开阔长线、对方缺接近压力、Brock 可保持距离
      fails_when: 敌方有硬开或 Brock 被迫中距离对枪
      bp_use: response_pick_or_lane_pressure_candidate
    - target: Emz_or_Spike_or_Mr_P_or_Shelly
      direction: subject_favored
      source: "[[sources/PLP-Brock|PLP-Brock]]"
      mechanism: Brock 可用长射程、溅射和开墙惩罚依赖中距离、墙体、召唤物或固定防守位置的目标
      active_when: 地图允许 Brock 先开距离或先改图，目标必须守矿/球门/金库路线
      fails_when: 草丛、墙角或目标队友让 Brock 被迫进入中近距离
      bp_use: map_conditioned_response_not_unconditional_counter
    - target: Stu_or_Max_or_Leon_or_Mortis_or_Edgar
      direction: target_favored
      source: "[[sources/PLP-Brock|PLP-Brock]]"
      mechanism: 高机动缩短距离，惩罚 Brock 慢弹道和低血量
      active_when: 地图给出侧路、草丛或多接近路线
      fails_when: 地图长线开阔且 Brock 有队友 peel
      bp_use: must_avoid_or_ban_reason_if_plan_depends_on_Brock
    - target: Crow_or_Cordelius_or_Bibi
      direction: target_favored
      source: "[[sources/PLP-Brock|PLP-Brock]]"
      mechanism: 毒、领域隔离、加速身体或击退接触会破坏 Brock 的安全距离和慢装填节奏
      active_when: Brock 需要独立守路，且敌方有草/墙/侧路让这些目标选择 first contact
      fails_when: 地图像 Bridge Too Far 这类长直线隔离路，接近路线过于明确且 Brock 有 Rocket Laces
      bp_use: false_positive_filter_for_named_counter_edges

  slot_notes:
    slot_1: "只在 Heist 长线或选择性开墙能立即转化时先手；不得用 Rocket No. 4 的单发 11 格虚构持续射程优势。"
    slot_2_3: "可建立远程开墙或跟随式 Super 逼位计划；需要 anti-aggro，也要预先决定 Laces 是保命还是为 Super 转位。"
    slot_4_5: "适合修复己方缺远程/开墙的问题；若选 Rocket No. 4，需确认 6 秒充能节奏真能换到目标位。"
    slot_6: "敌方缺高机动和远程答案时，可用打库、精确开墙或单发超距离消耗惩罚；不能把 Laces 当无限击退。"
```

## 关联页面

- [[sources/Fandom-Brock|Fandom 来源摘要: Brock]]
- [[sources/PLP-Brock|PLP 来源摘要: Brock]]
