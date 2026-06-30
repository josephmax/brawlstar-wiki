# Glowy

## 基本信息

- 稀有度：Mythic
- 定位：Support
- 类型：牵线治疗/伤害支援 / 恐惧反突进控制

## 来源摘要

- Fandom：[[sources/Fandom-Glowy|Fandom 来源摘要: Glowy]]
- PLP：[[sources/PLP-Glowy|PLP 来源摘要: Glowy]]
- PLP 推荐模式候选：Hot Zone, Bounty, Knockout

## 角色定位总结

Glowy 的 BP 价值来自双牵线：对敌人造成持续伤害，对队友提供治疗，Super 则用减速和恐惧打断正面进入。她不是独立 carry，而是把队友的站点/对枪能力放大；线会被距离和视线阻断，飞行目标也会暂停部分效果，所以地图墙体、队友站位和敌方突进路径决定她是稳定支援还是低伤害负担。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Glowy|Fandom-Glowy]]"
    plp: "[[sources/PLP-Glowy|PLP-Glowy]]"
    user_notes: none

  capability_vector:
    effective_range: mid_long_tether_range
    projectile_reliability: medium; 需要维持距离和视线，墙体阻断会让牵线闪烁
    burst: low_medium; Super 提供控制而非单人爆发
    sustained_dps: medium_if_enemy_tether_is_maintained
    objective_damage: low_direct_heist_value
    mobility: conditional_dash_with_Slippery_Savior
    survivability: medium_with_self_heal_from_Parasitism_and_team_heal_cycle
    engage: low; control_entry_with_super_if_team_follows
    disengage: medium_with_fear_slow_or_dash_heal
    anti_aggro: high_if_fear_cone_hits_front_facing_entry
    anti_tank: conditional_sustain_and_damage_debuff; needs_team_damage
    wall_break: none
    throw_or_wall_bypass: none
    area_control: medium_with_super_cone_and_tether_zone
    scouting_or_vision: low
    team_support: high; healing_tether_damage_buff_or_damage_debuff_builds
    spawnable_or_pet: none
    crowd_control: slow_and_fear
    terrain_creation: none

  build_switches:
    - build: More Lumens / Parasitism / Shield, Damage
      source: "[[sources/PLP-Glowy|PLP-Glowy]]"
      changes_capabilities:
        - More Lumens 提高短时间牵线 tick 频率，增强对线和站点换血
        - Parasitism 让敌方牵线回补 Glowy，自身更能维持支援位置
        - Shield/Damage 让中线支援不至于被第一波 poke 赶走
      enables:
        - hot_zone_sustain_anchor
        - bounty_knockout_trade_support
        - anti_aggro_fear_window
      mitigates_failure_modes:
        - support_low_self_sustain
        - short_trade_without_tether_value
      poor_when:
        - 墙体/距离让牵线反复断开，或队友无法在 Glowy 控制窗口内输出
      bp_use: default_support_trade_build
    - build: Biotic Ecosystem team-swing variant
      source: "[[sources/Fandom-Glowy|Fandom-Glowy]]"
      changes_capabilities:
        - 同时连敌人和队友时降低敌方伤害并提高队友伤害，提升前排或站点队友的换血质量
      enables:
        - bodyguard_lane
        - zone_teamfight_swing
      mitigates_failure_modes:
        - teammate_cannot_convert_tether
      poor_when:
        - 队伍没有稳定站点/前排，或地图让双牵线难以同时维持
      bp_use: teamfight_variant_when_comp_has_body_to_buff

  map_feature_hooks:
    - map_feature_type: hot_zone_tether_sustain_and_fear_entry
      uses_feature_by: 治疗/伤害牵线配合 Super 恐惧，可在热区入口延长队友站圈时间并阻止突进
      objective_conversion: 把敌方进圈变成被减速/恐惧的失败接触，同时让己方身体继续计分
      active_when: 队伍有真实 zone body，Glowy 能在墙边或中距离维持视线
      fails_if: 墙体阻断牵线、敌方从多角度进入，或 Glowy 被要求自己站圈吃第一波
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.zone_sustain_and_fear_entry
    - map_feature_type: knockout_bounty_tether_trade_support
      uses_feature_by: 长中距离牵线让队友赢 poke 交换，Super 恐惧可保护回合/星数领先
      objective_conversion: 保血量领先、拖缩圈、阻止刺客进入低血后排
      active_when: 地图有可维持视线的中长线，且队友能利用治疗或伤害 debuff 稳定换血
      fails_if: 敌方投掷/墙控打断视线，或纯长狙距离让 Glowy 无法保持牵线
      example_maps:
        - Belle's Rock
        - New Horizons
        - Shooting Star
        - Dry Season
      bp_use: candidate_eval.round_trade_support
    - map_feature_type: brawl_ball_fear_disarm_or_push_support
      uses_feature_by: Super 的减速/恐惧可让持球者或防守者离开路线，牵线治疗护送 scorer
      objective_conversion: 清中场球权、保护持球推进或把门前防守者赶出射门角度
      active_when: 队友有 scorer/破门/突进，Glowy 只负责控制和治疗窗口
      fails_if: 队伍没有射门转化，或敌方从侧草绕过 Glowy 的正面恐惧锥
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_support_control_with_followup
    - map_feature_type: line_of_sight_tether_break_filter
      uses_feature_by: 地图墙体既可保护 Glowy，也会切断她的牵线；需要把站位写进 pick 逻辑
      objective_conversion: 只在牵线能稳定作用于矿区、热区或回合路线时给 Glowy 计入支援价值
      active_when: Glowy 能沿墙边保持队友/敌人的可见线，或队友主动站在牵线半径内
      fails_if: 墙袋太深、目标频繁绕角、或敌方投掷把 Glowy 从支援位赶走
      example_maps:
        - Hard Rock Mine
        - Open Business
        - Belle's Rock
        - Ring of Fire
      bp_use: false_positive_filter.support_requires_los

  objective_contracts:
    - mode: Hot Zone
      can_fulfill:
        - sustain_zone_body
        - fear_entry
        - damage_debuff_or_team_buff_trade
      cannot_fulfill:
        - solo_zone_body
        - long_range_clear_without_teammate
      needs_teammate_support:
        - durable_zone_holder
        - area_clear_or_wall_control
      false_positive: Glowy 支援强不代表她能自己站圈
    - mode: Bounty_or_Knockout
      can_fulfill:
        - trade_support
        - anti_dive_peel
        - round_lead_sustain
      cannot_fulfill:
        - primary_long_range_pick_damage
      needs_teammate_support:
        - marksman_or_burst_to_convert_tether_advantage
        - wall_control_answer
      false_positive: 开阔长线如果牵线距离不足，Glowy 会被纯狙击体系压出价值区
    - mode: Brawl Ball
      can_fulfill:
        - fear_or_slow_ball_route
        - heal_scorer_or_body_push
      cannot_fulfill:
        - primary_scorer
        - goal_wallbreak
      needs_teammate_support:
        - scorer
        - wallbreak_or_hard_displacement
      false_positive: 恐惧只是窗口，不能替代射门路径

  failure_modes:
    - id: line_of_sight_or_range_break
      active_when: 墙体、绕角或距离让敌方/队友牵线闪烁并中断效果
      exposed_by: Fandom 牵线距离和视线规则
      mitigation: 只在有稳定支援位和队友站位纪律的地图使用
      bp_use: map_geometry_filter
    - id: flying_target_pause_or_fear_immunity
      active_when: 敌方飞行/滞空目标绕过牵线伤害或不吃正面恐惧窗口
      exposed_by: Fandom 对 flying target 的规则说明
      mitigation: 不把 Glowy 当作唯一 anti-air/anti-jump 答案
      bp_use: enemy_capability_filter
    - id: dash_heal_interrupted
      active_when: Slippery Savior dash 被墙、水、眩晕或路径打断，导致治疗不触发
      exposed_by: Fandom gadget 说明
      mitigation: dash 只作为明确路线的保命/补血工具，不当无条件解控
      bp_use: resource_tracking.mobility_reliability
    - id: support_without_followup
      active_when: Glowy 恐惧或牵线产生优势，但队友没有爆发、身体或站点转化
      exposed_by: Support 定位与牵线机制
      mitigation: 先确认队伍有 scorer、zone body 或长线输出核心
      bp_use: comp_dependency_check

  conditional_matchup_seeds:
    - target: El_Primo_or_Mico_or_Stu_or_Alli_or_Shade_or_Buzz_or_Sam
      direction: subject_favored
      source: "[[sources/PLP-Glowy|PLP-Glowy]]"
      mechanism: 恐惧/减速和敌方牵线能阻止近身或移动型目标完成第一波接触，队友再利用控制窗口补伤害
      active_when: 目标从正面或固定入口进入，Glowy 保留 Super 或牵线位置
      fails_when: 目标从侧草/墙后绕入，或 Glowy 的队友无法在恐惧期间击杀
      bp_use: anti_aggro_support_response
    - target: Jae-Yong
      direction: subject_favored
      source: "[[sources/PLP-Glowy|PLP-Glowy]]"
      mechanism: Glowy 的持续牵线和治疗回补能把节奏支援对局拖成持续换血，削弱 Jae-yong 依赖节奏窗口的推进
      active_when: 双方围绕热区/回合空间打正面交换，Glowy 的队友输出更稳定
      fails_when: Jae-yong 让队友快速换线或绕开 Glowy 的牵线范围
      bp_use: support_tempo_matchup
    - target: Gale_or_Sandy_or_Willow_or_Lou_or_Lumi_or_Emz_or_Sirius_or_Jessie
      direction: target_favored
      source: "[[sources/PLP-Glowy|PLP-Glowy]]"
      mechanism: 击退/隐蔽/墙控/冰冻/区域压制/召唤物会打断 Glowy 的牵线站位或让她的支援窗口无法转化
      active_when: 地图有墙袋、草丛、热区入口或召唤物锚点保护这些资源
      fails_when: 资源被清、视线打开，且 Glowy 能站在队友身后持续牵线
      bp_use: must_answer_control_or_spawnable_before_glowy
    - target: Flying_or_airborne_entry
      direction: target_favored
      source: "[[sources/Fandom-Glowy|Fandom-Glowy]]"
      mechanism: 飞行目标会暂停牵线伤害或绕开正面恐惧，让 Glowy 的 anti-aggro 价值下降
      active_when: 对方有跳跃/滞空进入并能落在 Glowy 或核心队友身边
      fails_when: 落点被队友控制覆盖，或 Glowy 只负责治疗不是反跳核心
      bp_use: anti_aggro_false_positive_filter

  slot_notes:
    slot_1: 不适合盲目先手；只有 Hot Zone/回合图明确需要支援 sustain，且敌方反支援资源不宽时才考虑。
    slot_2_3: 可作为队伍站点或长线核心的放大器，但必须同步锁定一个真实输出/身体。
    slot_4_5: 适合回答已暴露的正面突进或低爆发支援壳，注意不要给敌方最后手拿墙控/召唤物清牵线。
    slot_6: 当敌方缺绕后、墙控和飞行进场时，Glowy 可以作为高质量保护与反突进 last pick。
```

## 关联页面

- [[sources/Fandom-Glowy|Fandom 来源摘要: Glowy]]
- [[sources/PLP-Glowy|PLP 来源摘要: Glowy]]
