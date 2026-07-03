# Byron

## 基本信息

- 稀有度：Mythic
- 定位：Support
- 来源：神话支援英雄

## 攻击特征

- 主攻击是超远距离药剂投射。
- 同一发攻击可以伤害敌人，也可以治疗友军。
- 装填速度快，适合在长时间拉扯中持续制造血量差。

## 超级技能特征

- Super 是一瓶范围药剂。
- 可以爆发治疗友军，也可以对敌人造成爆发伤害。
- `Malaise` 会让 Super 命中的敌人治疗效果下降，能反制治疗链和持续站场。

## 角色定位总结

Byron 是远程治疗、持续消耗和反治疗支援。他的强点不是自己完成击杀，而是让队友在长线或目标区反复多打一个血量循环。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-06-30
    plp: direct_raw_capture_2026-06-30
    user_notes: none

  capability_vector:
    effective_range: very_long
    projectile_reliability: medium_high_on_open_lines; 单发药剂需要瞄准但射程和快装填允许反复修正
    burst: medium_with_Super; 更偏血量 swing 而非单杀爆发
    sustained_dps: medium; 快装填和毒伤 tick 能稳定换血
    objective_damage: low_medium; Heist 主要是支援线权和补 safe chip，不是主 race
    mobility: low
    survivability: low_base_health_but_high_if_teammate_frontline_exists
    engage: low
    disengage: low; 依赖队友 peel 和站位
    anti_aggro: conditional; 可通过治疗队友和 Super burst 反打，但自身怕贴脸
    anti_tank: medium_with_Malaise_and_teammate_damage
    wall_break: none
    throw_or_wall_bypass: low; 普攻仍需要直线接触
    area_control: medium_with_Super_zone_and_heal_denial
    scouting_or_vision: low
    team_support: very_high; 远程治疗、续航、反治疗和血量 swing
    crowd_control: low; 主要是治疗削减而非位移控制

  build_switches:
    - build: Booster Shots / Malaise / Shield + Damage
      source: "[[sources/PLP-Byron|PLP-Byron]] / [[sources/Fandom-Byron|Fandom-Byron]]"
      changes_capabilities:
        - 提高多目标命中和团队血量 swing
        - Malaise 让敌方治疗链、坦克续航和目标区重进场贬值
      enables:
        - long_range_support_lane
        - anti_sustain_response
        - objective_body_sustain
      mitigates_failure_modes:
        - teammate_body_loses_long_trade
        - enemy_heal_chain_outlasts_poke
      poor_when:
        - 队友没有可治疗的前排/中排身体，或敌方能隔墙直接压 Byron
      bp_use: 默认竞技 build 候选；选 Byron 前必须确认队友能把治疗转换成线权
    - build: Shot In The Arm / Injection sustain-pierce variant
      source: "[[sources/Fandom-Byron|Fandom-Byron]]"
      changes_capabilities:
        - 提高自保或周期性穿透价值
        - 更适合敌我都围绕窄口和队友站位拉扯时
      enables:
        - self_sustain_in_poke_lane
        - grouped_lane_heal_or_damage
      mitigates_failure_modes:
        - Byron 被 poke 到无法站线
      poor_when:
        - 需要 Booster Shots 提供短窗口多目标 swing
      bp_use: 长线续航或窄口队友站位密集时的 build requirement

  map_feature_hooks:
    - map_feature_type: long_range_sustain_lane
      uses_feature_by: 超远程药剂同时治疗己方长线队友、消耗敌方长手
      objective_conversion: Bounty/Knockout 保血量和星/局面领先，减少队友回撤时间
      active_when: 地图开阔、有队友能站在 Byron 治疗线内，敌方缺低成本隔墙压制
      fails_if: 敌方投掷/召唤物阻断药剂线，或刺客能直接碰到 Byron
      example_maps:
        - Shooting Star
        - Dry Season
        - Out in the Open
        - Hideout
      bp_use: candidate_eval.long_range_support_and_star_lead
    - map_feature_type: zone_or_gem_sustain_anchor
      uses_feature_by: 在目标边缘给站圈/控矿队友续航，并用 Malaise 削弱敌方回复
      objective_conversion: Hot Zone 站圈时间、Gem Grab mine control 和 carrier 保护
      active_when: 我方有实际站圈/控矿身体，Byron 可以从后排持续打到队友
      fails_if: 我方只有三远程不站点，或墙体让 Byron 既打不到队友也打不到敌人
      example_maps:
        - Ring of Fire
        - Open Business
        - Gem Fort
        - Hard Rock Mine
      bp_use: map_bp_factors.support_sustain_anchor
    - map_feature_type: heist_lane_sustain_and_anti_body
      uses_feature_by: 支援己方 safe lane 远程/前排赢线，并用 Super/Malaise 反进入金库的身体
      objective_conversion: 保住防守线、延长己方 DPS 存活、附带远程打库 chip
      active_when: 队友是主要 safe DPS，Byron 负责让其赢长线或防坦克入库
      fails_if: 队伍缺主 safe DPS，或敌方远程 race 不需要进入 Byron 的治疗/伤害范围
      example_maps:
        - Bridge Too Far
        - Kaboom Canyon
        - Hot Potato
        - Safe Zone
      bp_use: candidate_eval.heist_support_not_primary_dps

  objective_contracts:
    - mode: Bounty_or_Knockout
      can_fulfill:
        - long_range_heal_support
        - low_commitment_chip
        - star_or_round_lead_sustain
      cannot_fulfill:
        - solo_first_pick_without_teammate_damage
        - close_range_self_peel
      needs_teammate_support:
        - reliable_damage_carry
        - anti_thrower_or_anti_dive
      false_positive: 队友不能利用治疗继续站线时，Byron 只是低血量长手
    - mode: Hot Zone_or_Gem Grab
      can_fulfill:
        - sustain_objective_body
        - punish_heal_or_tank_reentry_with_Malaise
        - support_carrier_or_zone_anchor
      cannot_fulfill:
        - primary_zone_body
        - reliable_bush_scout
      needs_teammate_support:
        - body_on_objective
        - bush_or_wall_control
      false_positive: 没有站点身体时，治疗价值无法转成分数
    - mode: Heist
      can_fulfill:
        - support_safe_lane_winner
        - anti_body_defense_near_safe
        - auxiliary_safe_chip
      cannot_fulfill:
        - primary_safe_race
      needs_teammate_support:
        - dedicated_safe_dps
        - lane_pressure_or_wallbreak
      false_positive: PLP 的 Heist 适配应理解为支援 lane/race，不是让 Byron 单独打库

  failure_modes:
    - id: low_health_direct_dive
      active_when: 敌方 Mortis/Leon/Chuck/Mico/Edgar 或侧草路线能直接碰到 Byron
      exposed_by: Fandom 低生命值字段与 PLP counteredBy
      mitigation: 队友 peel、视野、站位后撤、选择接近路线少的地图
      bp_use: must_avoid_or_needs_protection
    - id: no_body_to_heal
      active_when: 我方阵容没有前排/中排或稳定长线核心可以吃治疗
      exposed_by: Byron 机制定位
      mitigation: 与 Meg/Rosa/8-Bit/稳线 marksman 等可转换治疗的队友搭配
      bp_use: role_coverage_check
    - id: wall_or_thrower_denies_line
      active_when: 敌方 Barley/Willow/Sprout 等隔墙压制，Byron 直线药剂无法触达关键目标
      exposed_by: PLP counteredBy 与地图墙体模型
      mitigation: 开墙、刺客/投掷回答、换到开阔地图或长线 lane
      bp_use: false_positive_filter

  conditional_matchup_seeds:
    - target: Frank_or_Jacky_or_El_Primo_or_Buzz
      direction: subject_favored
      source: "[[sources/PLP-Byron|PLP-Byron]]"
      mechanism: 长射程毒伤和队友治疗能让直线进场身体在接触前被消耗，Malaise 降低其续航回合
      active_when: 进场路线可见，Byron 有队友身体可治疗并能集火
      fails_when: 目标从草/墙侧直接碰到 Byron，或队友没有伤害完成反打
      bp_use: anti_body_support_response
    - target: Max_or_Gale_or_R-T
      direction: subject_favored
      source: "[[sources/PLP-Byron|PLP-Byron]]"
      mechanism: Byron 在长换血中用治疗抵消 poke/控制收益，让队友保持线权
      active_when: 地图允许后排安全支援，且敌方不能隔墙切断 Byron
      fails_when: Max 速度带出多角度夹击，或 R-T/Gale 队友能直接压 Byron
      bp_use: sustain_answer_to_control_or_tempo
    - target: Barley_or_Willow_or_Sprout
      direction: target_favored
      source: "[[sources/PLP-Byron|PLP-Byron]]"
      mechanism: 投掷和墙后控制绕开 Byron 的直线治疗/伤害线，持续压低低血后排
      active_when: 墙体完整、投掷有安全口袋、我方缺开墙或 dive
      fails_when: 墙体打开或 Byron 队友能先清投掷口袋
      bp_use: must_answer_wall_control_before_byron
    - target: Poco_or_Rosa_or_Sandy_or_Lola
      direction: target_favored
      source: "[[sources/PLP-Byron|PLP-Byron]]"
      mechanism: 群体 sustain、草丛身体、隐蔽推进或分身火力会让 Byron 单体治疗/毒伤跟不上目标区节奏
      active_when: 目标图是 Hot Zone/Gem/Brawl Ball 草墙接触图，敌方能把战斗压成近距离团战
      fails_when: Byron 队伍有足够范围伤害、探草和 anti-tank，Malaise 命中关键回复目标
      bp_use: avoid_as_only_sustain_answer

  slot_notes:
    slot_1: 只在长线支援和可治疗队友价值很确定时先手；否则容易被投掷或刺客后手惩罚。
    slot_2_3: 适合围绕一个稳定 carry/body 建立续航计划，或回答敌方慢速前排。
    slot_4_5: 用来修补我方缺续航/反治疗的问题，但必须确认敌方 6 位没有免费 dive。
    slot_6: 如果敌方三人缺投掷、缺直达 Byron 的机动，且我方已有可治疗核心，可以作为高质量 sustain last pick。
```

## 关联页面

- [[sources/Fandom-Byron|Fandom 来源摘要: Byron]]
- [[sources/PLP-Byron|PLP 来源摘要: Byron]]
