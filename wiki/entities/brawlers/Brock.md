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
  profile_status: reviewed
  source_quality:
    fandom: direct_raw_capture_2026-06-30-v2
    plp: direct_raw_capture_2026-06-29
    user_notes: none

  capability_vector:
    effective_range: long
    projectile_reliability: medium; 火箭弹速慢，需要预判，打固定目标更稳定
    burst: high_when_ammo_or_super_available
    sustained_dps: medium; 慢装填，需要 Reload Gear 或弹药管理
    objective_damage: high_in_heist_when_safe_angle_exists
    mobility: conditional_escape_or_reposition_with_Rocket_Laces
    survivability: low_base_health; Shield Gear 可缓解但不能替代保护
    engage: low
    disengage: medium_with_Rocket_Laces
    anti_aggro: conditional; Rocket Laces 可击退/跳走，但不是稳定硬控
    anti_tank: medium_if_range_kept
    wall_break: high; Super 与 Rocket Fuel 都能改图
    throw_or_wall_bypass: medium; Super 可越墙轰炸
    area_control: medium_high; 溅射、火焰地面和 Super 逼位
    scouting_or_vision: low
    team_support: terrain_transform_and_long_range_pressure
    terrain_destruction: high

  build_switches:
    - build: Rocket Laces / More Rockets / Shield + Reload
      source: "[[sources/PLP-Brock|PLP-Brock]]"
      changes_capabilities:
        - 提高反突进自保和装填稳定性
        - 增强 Super 覆盖和持续轰炸压力
      enables:
        - long_range_pressure
        - anti_aggro_escape
        - safer_first_pick_on_open_or_heist_maps
      mitigates_failure_modes:
        - low_health_ambush
        - reload_vulnerability
      poor_when:
        - draft 需要精确开关键墙而不是保命
      bp_use: 默认竞技 build 候选，不直接等于最终推荐
    - build: Rocket Fuel wall-break variant
      source: "[[sources/Fandom-Brock|Fandom-Brock]]"
      changes_capabilities:
        - 提供可控开墙，不必先攒 Super
      enables:
        - wall_break_transform
        - goal_barrier_opening
        - safe_angle_creation
      mitigates_failure_modes:
        - 被投掷或墙体掩护低成本卡住
      poor_when:
        - 开墙会让敌方远程或突进更受益
      bp_use: 地图状态需要主动改图时的 build requirement

  map_feature_hooks:
    - map_feature_type: long_sightline
      uses_feature_by: 远程火箭压线、低承诺消耗和安全目标输出
      objective_conversion: Bounty/Knockout 减员压力；Heist 远程打库
      active_when: 视线长、接近路径单一、敌方缺高机动突脸
      fails_if: 敌方有多条接近路线、草丛伏击、或高机动持续压近
      example_maps:
        - Shooting Star
        - Out in the Open
        - Bridge Too Far
      bp_use: required_capabilities.long_range_pressure
    - map_feature_type: wall_break_transform
      uses_feature_by: Super 或 Rocket Fuel 破关键墙
      objective_conversion: 打开金库角度、球门通路或反投掷角度
      active_when: 我方阵容能利用开墙后的长线
      fails_if: 过度开墙反而帮助敌方射程或突进
      example_maps:
        - Safe Zone
        - Shooting Star
        - Brawl Ball goal_wall_maps
      bp_use: terrain_state_plan.transform

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
        - wall_break_snowball
        - force_split_with_super
      cannot_fulfill:
        - reliable_close_range_duel
      needs_teammate_support:
        - bush_check_or_peel
      false_positive: 长线图若敌方有高机动接近和队友保护不足，Brock 会变成暴露点
    - mode: Brawl Ball
      can_fulfill:
        - break_goal_wall
        - create_scoring_window
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
      exposed_by: 地图因素 BP 表达规范
      mitigation: 只开关键墙，并确认 follow-up
      bp_use: terrain_state_plan_check

  conditional_matchup_seeds:
    - target: 8-Bit_or_Pam_or_Nita
      direction: subject_favored
      source: "[[sources/PLP-Brock|PLP-Brock]]"
      mechanism: 长射程与溅射惩罚低机动或站位笨重目标
      active_when: 开阔长线、对方缺接近压力、Brock 可保持距离
      fails_when: 敌方有硬开或 Brock 被迫中距离对枪
      bp_use: response_pick_or_lane_pressure_seed
    - target: Stu_or_Max_or_Mortis
      direction: target_favored
      source: "[[sources/PLP-Brock|PLP-Brock]]"
      mechanism: 高机动缩短距离，惩罚 Brock 慢弹道和低血量
      active_when: 地图给出侧路、草丛或多接近路线
      fails_when: 地图长线开阔且 Brock 有队友 peel
      bp_use: must_avoid_or_ban_reason_if_plan_depends_on_Brock

  slot_notes:
    slot_1: 只在地图/模式基本面很强且敌方低成本反制面窄时可先手；Heist 长线图优先级更高。
    slot_2_3: 可作为回答低机动前排或建立远程开墙计划的一手，但需要搭配 anti-aggro。
    slot_4_5: 适合修复己方缺远程/开墙的问题，同时检查别把刺客 last pick 口子留给敌方。
    slot_6: 如果敌方三人缺高机动和远程答案，可作为惩罚性长线/打库选择。
```

## 关联页面

- [[sources/Fandom-Brock|Fandom 来源摘要: Brock]]
- [[sources/PLP-Brock|PLP 来源摘要: Brock]]
