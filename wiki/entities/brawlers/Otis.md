# Otis

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：远程输出与禁言控场英雄

## 攻击特征

- 主攻击是三枚长距离颜料弹
- 伤害稳定，适合持续压线
- 更偏通过命中和节奏去建立控场

## 超级技能特征

- Super 会让目标短时间无法攻击
- 目标也不能使用 Super、Gadget 或 Hypercharge
- 这是非常强的节奏打断和单点封锁工具

## 适合场景

- 需要压制关键输出位的对局
- 需要打断对方连招或进场的模式
- 适合在团战前先削弱对手反打能力

## 角色定位总结

Otis 是靠远程输出和禁言 Super 改写对手操作空间的 Mythic Controller，强点是“让对手暂时做不了事”。

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
    projectile_reliability: medium_high; 多发颜料弹有轻微散布，Ink Refills 提高命中与 DPS
    burst: medium_after_mute_or_with_Phat_Splatter
    sustained_dps: high_with_Ink_Refills
    objective_damage: high_conditional_in_Heist_with_Ink_Refills_and_Phat_Splatter
    mobility: low
    survivability: medium; 依赖距离、Shield/Speed Gear 和 Super 威慑
    engage: medium; Super 命中后可强行封锁目标操作
    disengage: low_medium; 主要靠沉默迫使对方停手
    anti_aggro: high_if_Super_available
    anti_tank: high_if_mute_hits_entry
    wall_break: low
    throw_or_wall_bypass: medium_with_Phat_Splatter_puddle
    area_control: medium_high
    scouting_or_vision: medium_with_Vision_or_Phat_Splatter
    team_support: single_target_shutdown_and_choke_denial
    crowd_control: high; mute prevents attack/Super/Gadget/Hypercharge

  build_switches:
    - build: Phat Splatter / Ink Refills / Shield + Speed + Damage + Vision + Super Charge
      source: "[[sources/PLP-Otis|PLP-Otis]]"
      changes_capabilities:
        - 增强持续 DPS、Super 充能和安全区/金库压力
        - 提供绕墙/地面区域伤害候选
      enables:
        - anti_aggro_shutdown
        - heist_safe_damage
        - hot_zone_choke_control
        - brawl_ball_defense
      mitigates_failure_modes:
        - 纯靠 Super 命中导致输出不足
        - 草丛或侧路信息不足
      poor_when:
        - 敌方主要威胁是长距离投掷或绕墙输出，Otis 无法接近目标
      bp_use: 默认竞技 build 候选；Gear 根据地图草丛/站圈/伤害需求切换
    - build: Dormant Star chokepoint variant
      source: "[[sources/Fandom-Otis|Fandom-Otis]]"
      changes_capabilities:
        - 把 Super 变成可预置的 choke blocker
      enables:
        - brawl_ball_goal_choke_denial
        - hot_zone_entry_tax
        - heist_entry_route_delay
      mitigates_failure_modes:
        - 需要提前封路线但 Otis 不能直接命中进场者
      poor_when:
        - 队友不能跟进触发后的目标，或地图缺关键窄口
      bp_use: 地图有明确 choke/入口时的条件 build

  map_feature_hooks:
    - map_feature_type: lane_funnel_or_choke
      uses_feature_by: Dormant Star 或 Super 封住进场、传球、站圈入口
      objective_conversion: 阻断 Brawl Ball 进球窗口、Hot Zone 进圈、Heist 入库
      active_when: 地图目标通路窄，敌方依赖突进或 Super 进场
      fails_if: 敌方能远程绕墙消耗，或触发后我方无法跟进击杀
      example_maps:
        - Parallel Plays
        - Brawl Ball goal_choke_maps
      bp_use: must_answer_route_or_choke_denial
    - map_feature_type: base_entry_route
      uses_feature_by: Super 沉默入库 aggro，Ink Refills + Phat Splatter 反打
      objective_conversion: Heist 防入库，同时可转安全输出
      active_when: 敌方依赖 Bull/Edgar/Buzz/Darryl/Fang 等进场打库
      fails_if: 敌方 safe damage 来自长线/投掷而非近身入库
      example_maps:
        - Pit Stop
        - Safe Zone
        - Hot Potato
      bp_use: anti_aggro_heist_defender
    - map_feature_type: grass_anchor
      uses_feature_by: Phat Splatter 覆盖草丛，Vision Gear 或沉默暴露目标
      objective_conversion: 降低伏击/Speed Gear 进场收益
      active_when: 草丛是主要接近路线
      fails_if: 敌方能烧草、投掷或远程无视草丛对线
      example_maps:
        - Double Swoosh
        - Sneaky Fields
      bp_use: vision_tax_and_anti_aggro_candidate

  objective_contracts:
    - mode: Heist
      can_fulfill:
        - defend_enemy_entry_route
        - mute_aggro_near_safe
        - conditional_safe_dps_with_Ink_Refills
      cannot_fulfill:
        - long_range_safe_angle_like_marksman
      needs_teammate_support:
        - wallbreak_or_lane_pressure_if_enemy_plays_long
      false_positive: 如果敌方主要是远程打库，Otis 的 anti-aggro 价值会下降
    - mode: Brawl Ball
      can_fulfill:
        - anti_scorer_defense
        - pass_or_dash_denial
        - chokepoint_block
      cannot_fulfill:
        - primary_scorer
      needs_teammate_support:
        - scorer_or_wallbreak_to_convert_defense_into_goal
      false_positive: 防守强不等于阵容有进球窗口
    - mode: Hot Zone
      can_fulfill:
        - zone_clear
        - entry_denial
        - anti_tank_or_anti_assassin_zone_defense
      cannot_fulfill:
        - pure_body_on_zone_against_throwers
      needs_teammate_support:
        - thrower_answer_or_wallbreak
      false_positive: 被投掷隔墙清圈时，Otis 可能站不住圈

  failure_modes:
    - id: mute_misses_or_no_followup
      active_when: Super 未命中，或命中后队友无法补伤害/控目标
      exposed_by: Fandom Super 机制
      mitigation: Super Charge Gear、先用控线逼位、搭配爆发队友
      bp_use: candidate_eval.required_support
    - id: outranged_by_throwers_or_wall_control
      active_when: 敌方 Barley/Larry_and_Lawrie/Willow 等能隔墙压制，Otis 无法直接命中
      exposed_by: PLP counteredBy
      mitigation: 开墙、绕侧路、或让队友回答投掷
      bp_use: must_answer_or_avoid
    - id: defensive_value_without_win_condition
      active_when: Otis 只负责防突进，但我方缺 safe DPS/进球/站圈转换
      exposed_by: BP DSL objective_contract 要求
      mitigation: 与 scorer、safe DPS 或 zone body 搭配
      bp_use: role_coverage_check

  conditional_matchup_seeds:
    - target: Chuck_or_Sam_or_Rosa_or_Bibi
      direction: subject_favored
      source: "[[sources/PLP-Otis|PLP-Otis]]"
      mechanism: Otis 的 mute 会阻止进场英雄攻击、接 Super/Gadget 或完成目标动作
      active_when: 目标需要近身或技能连段转化为进球/打库/站圈
      fails_when: Otis 没有 Super、被先手逼退，或目标由队友保护进入
      bp_use: response_pick_seed_against_entry_plan
    - target: Barley_or_Larry_and_Lawrie_or_Willow
      direction: target_favored
      source: "[[sources/PLP-Otis|PLP-Otis]]"
      mechanism: 投掷/绕墙控制让 Otis 难以用直线射程和 Super 接触目标
      active_when: 墙体完整、敌方有安全口袋、我方缺开墙或刺客
      fails_when: 地图被开墙或 Otis 队友能处理投掷口袋
      bp_use: avoid_or_must_pair_with_thrower_answer

  slot_notes:
    slot_1: 在 Heist/Brawl Ball/Hot Zone 若地图进场路线明确，可以作为稳定 anti-aggro 控制先手；纯长线图不宜裸先。
    slot_2_3: 很适合回答敌方坦克、刺客、Chuck/Sam 类进场计划，同时建立防守基本面。
    slot_4_5: 用于修补己方缺 anti-aggro 或站圈清圈的问题，但要补投掷答案。
    slot_6: 如果敌方三人已暴露近身进场且缺投掷/长线保护，Otis 可作为高收益惩罚位。
```

## 关联页面

- [[sources/Fandom-Otis|Fandom 来源摘要: Otis]]
- [[sources/PLP-Otis|PLP 来源摘要: Otis]]
