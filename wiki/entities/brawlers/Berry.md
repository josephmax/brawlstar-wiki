# Berry

## 基本信息

- 稀有度：Epic
- 定位：Support
- 类型：越墙铺地治疗 / 控区支援 / 短距离 Super 进退场

## 来源摘要

- Fandom：[[sources/Fandom-Berry|Fandom 来源摘要: Berry]]
- PLP：[[sources/PLP-Berry|PLP 来源摘要: Berry]]
- PLP 推荐模式候选：Heist, Hot Zone

## 角色定位总结

Berry 的 BP 价值来自持续地面控制和治疗循环：普攻越墙生成 puddle，同时伤害敌人、治疗队友，并且实际治疗会给自己充能 Super。`Floor Is Fine` 让他站在自己 puddle 上获得装填收益，`Healthy Additives` 可以把下一块 puddle 延长到适合守点或 Heist 压库的时间。不要把 Berry 的 Super 当成通用绕图位移：Fandom 明确说明 Super dash 不能越墙或过水，且会被 stun/knockback 取消；它更像短距离进退场、救队友或沿路铺地工具。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Berry|Fandom-Berry]]"
    plp: "[[sources/PLP-Berry|PLP-Berry]]"
    user_notes: none

  capability_vector:
    effective_range: mid_thrower; 6.33 格越墙 puddle，靠地面持续收益而非远程爆发
    projectile_reliability: medium_on_fixed_routes; puddle 持续 6 秒适合预铺，直接追高速目标效率低
    burst: medium_with_super_hit_or_impact_stack
    sustained_dps: conditional; 基础 2.4 秒 very_slow reload，站在自身 puddle 后由 Floor_Is_Fine 改善
    objective_damage: conditional_heist_puddle_pressure_with_Healthy_Additives
    mobility: medium_short_dash_with_super; cannot_cross_walls_or_water
    survivability: low_base_health_but_self_heal_and_Friendship_knockback
    engage: medium_if_super_dash_reaches_fixed_target
    disengage: medium_with_super_dash_or_Friendship_knockback
    anti_aggro: medium_if_Friendship_available_and_route_is_predictable
    anti_tank: low_medium; 可拖慢和治疗队友，但自身不应单独正面抗高身体
    wall_break: none
    throw_or_wall_bypass: high_for_attack_lobs; none_for_super_route
    area_control: very_high_with_persistent_puddles
    scouting_or_vision: low; puddle 可试探草口但没有真实 reveal
    team_support: very_high_heal_over_time_and_emergency_heal
    spawnable_or_pet: none
    crowd_control: knockback_with_Friendship_is_Great
    terrain_creation: temporary_heal_damage_puddles
    terrain_destruction: none

  build_switches:
    - build: "Friendship Is Great / Floor Is Fine / Shield, Damage"
      source: "[[sources/PLP-Berry|PLP-Berry]]"
      changes_capabilities:
        - "Friendship Is Great 提供近身 knockback 和范围回血，让 Berry 在被切或救队友时有一次短 peel"
        - "Floor Is Fine 把站在自己 puddle 上的 reload 从 very_slow 修正为可持续控区节奏"
        - "Shield/Damage 弥补低血与收割阈值，但不改变他怕被强突进秒掉的本质"
      enables:
        - "Hot Zone 持续铺地与治疗"
        - "Heist 固定路线/金库附近 puddle 压力"
        - "队友站点或推进的续航支援"
      mitigates_failure_modes:
        - "very_slow_reload_without_puddle"
        - "first_contact_dive_pressure"
      best_when: "地图目标需要反复站点、回区或在固定入口交战，且 Berry 能安全站在 puddle 周边循环"
      poor_when: "敌方用高机动直接越过 puddle，或开阔图迫使 Berry 长距离裸走"
      bp_use: default_support_control_build
    - build: "Healthy Additives Heist/control variant"
      source: "[[sources/Fandom-Berry|Fandom-Berry]] / [[sources/PLP-Berry|PLP-Berry]]"
      changes_capabilities:
        - "下一次普攻 puddle 持续约 12 秒，适合覆盖 safe、热区入口或回防路线"
        - "Fandom tips 提到 Healthy Additives 配 Making a Mess 在 Heist 可造成高额固定目标收益"
      enables:
        - "long_puddle_safe_or_entry_pressure"
        - "zone_reentry_denial"
      mitigates_failure_modes:
        - "puddle_duration_too_short_for_objective"
      best_when: "敌方必须从同一入口回防或 safe 周边有可反复覆盖的固定位置"
      poor_when: "敌方分路打远程 race，Berry 无法把长 puddle 转成真实目标压力"
      bp_use: objective_duration_variant

  map_feature_hooks:
    - map_feature_type: hot_zone_puddle_sustain_and_entry_denial
      uses_feature_by: "越墙 puddle 覆盖区边和入口，同时治疗己方站区身体"
      route_or_position: "zone edge、L 墙支援位、草口回区线、敌方重复 re-entry choke"
      objective_conversion: "延长己方 zone time，逼敌方绕路或吃持续伤害进入圈"
      active_when: "队友有真实站区身体，Berry 能从墙后或边缘安全铺地，并能站在 puddle 上循环 reload"
      fails_if: "敌方从圈外长手/投掷清掉 Berry，或我方没有人站区导致治疗只变成空转"
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.zone_sustain_and_entry_tax
    - map_feature_type: heist_healthy_additives_safe_or_lane_control
      uses_feature_by: "长持续 puddle 可以覆盖 safe、defender path 或基地入口，Super 沿路铺地补短窗压力"
      route_or_position: "safe 侧墙、金库入口、defender 回防线、边路赢线后的投掷角"
      objective_conversion: "把 lane win 转成金库持续伤害、迫使防守者绕路或回身处理 Berry"
      active_when: "Berry 有安全投掷角且队友已有主 safe DPS，Berry 作为持续压力和防守路线干扰"
      fails_if: "把 Berry 当唯一 race 核心，或敌方远程 safe DPS 不需要穿过 puddle"
      example_maps:
        - Hot Potato
        - Pit Stop
        - Safe Zone
        - Safe(r) Zone
      bp_use: candidate_eval.heist_sustain_control_not_primary_race
    - map_feature_type: gem_mid_puddle_carrier_sustain
      uses_feature_by: "puddle 治疗己方 carrier/body，同时用地面伤害逼敌方远离矿区入口"
      route_or_position: "gem mine、center fort doorway、H 草入口、carrier countdown retreat"
      objective_conversion: "保护 carrier 换血、延迟敌方进矿、让倒计时撤退线有治疗锚点"
      active_when: "队伍有可靠 carrier 或中路身体，Berry 不需要自己拿大量宝石并暴露在正面"
      fails_if: "敌方用投掷/长线清 Berry 的支援位，或机动刺客绕过 puddle 直接切 carrier"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Double Swoosh
      bp_use: map_bp_factors.carrier_sustain_and_mine_entry_denial
    - map_feature_type: brawl_ball_friendship_knockback_support
      uses_feature_by: "Friendship knockback 和回血可以在门前/中场保护持球推进，Super dash 可短距离救球或铺进攻路线"
      route_or_position: "midfield ball、goal-front defender、side grass push、己方门前入口"
      objective_conversion: "击退持球者或门前防守，给 scorer 一次射门/接球窗口"
      active_when: "队友有 scorer 或 wallbreak，Berry 只负责支援和反突进"
      fails_if: "Berry 被要求自己成为主 scorer，或敌方保留 stun/knockback 取消 Super dash"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_support_peel_and_short_route

  objective_contracts:
    - mode: Heist
      can_fulfill:
        - "long_duration_puddle_on_safe_or_defender_path"
        - "support_healing_for_primary_safe_DPS"
        - "base_entry_disruption_with_super_trail"
      cannot_fulfill:
        - "solo_remote_safe_race"
        - "water_or_wall_crossing_entry"
      needs_teammate_support:
        - "primary_safe_DPS"
        - "lane_control_or_wall_cover_for_Berry"
      false_positive: "PLP Heist 信号必须落到 safe 角度和回防路线；Berry 自己不是通用打库核心"
    - mode: Hot Zone
      can_fulfill:
        - "zone_entry_denial"
        - "ally_body_sustain"
        - "puddle_reload_cycle"
      cannot_fulfill:
        - "solo_zone_body_without_teammate"
        - "open_lane_long_range_duel"
      needs_teammate_support:
        - "durable_zone_holder"
        - "anti_thrower_or_anti_dive"
      false_positive: "有治疗不等于能站区；必须有队友把治疗转成 zone time"
    - mode: Gem Grab
      can_fulfill:
        - "carrier_sustain"
        - "mine_entry_puddle_control"
        - "countdown_retreat_heal_anchor"
      cannot_fulfill:
        - "primary_carrier_under_dive_pressure"
      needs_teammate_support:
        - "actual_carrier_or_mid_body"
        - "vision_or_bush_control"
      false_positive: "Berry 支援矿区很强，但低血和慢 reload 不适合无保护拿宝石"

  failure_modes:
    - id: very_slow_reload_without_puddle
      active_when: "Berry 被迫离开自己 puddle，或地形/敌方压力让他无法站在安全铺地区"
      exposed_by: "[[sources/Fandom-Berry|Fandom-Berry]] reload and Floor Is Fine mechanics"
      mitigation: "只在能形成安全 puddle cycle 的地图和站位上选；队友补站点身体"
      bp_use: resource_tracking.puddle_reload_anchor
    - id: super_route_false_positive
      active_when: "把 Sweet Swirl 当成过墙/过水绕行，或在敌方控制资源未交时 dash"
      exposed_by: "[[sources/Fandom-Berry|Fandom-Berry]] Super cannot cross walls/water and can be cancelled"
      mitigation: "Super 只作为短距离进退、救援或铺地；先查 stun/knockback"
      bp_use: false_positive_filter.mobility_not_terrain_bypass
    - id: low_health_dive_pressure
      active_when: "刺客、高速身体或长手投掷直接接触 Berry，而 Friendship 或队友 peel 不可用"
      exposed_by: "2600 HP and PLP target_favored list"
      mitigation: "保留 knockback，选墙后支援位，或用队友控制覆盖侧路"
      bp_use: draft_requires_peel
    - id: puddle_no_stack_and_low_conversion
      active_when: "多个 puddle 叠在同一目标区但 tick 不叠加，或敌方快速离开地面区域"
      exposed_by: "[[sources/Fandom-Berry|Fandom-Berry]] puddle tick does not stack"
      mitigation: "分散铺路、覆盖入口和撤退线，而不是只叠一个点"
      bp_use: area_control_quality_gate

  conditional_matchup_seeds:
    - target: Jae_Yong_or_Poco_or_Gene
      direction: subject_favored
      source: "[[sources/PLP-Berry|PLP-Berry]]"
      mechanism: "Berry 的持续治疗和地面控制可拉长支援互换，让低爆发支援位很难从固定 objective 线上直接赶走己方 body"
      active_when: "战斗围绕热区、矿区或金库入口反复发生，Berry 队友有可被治疗的前排或 lane holder"
      fails_when: "对方支援配高爆发突进，或 Berry 被长线先处理"
      bp_use: support_shell_sustain_response
    - target: Sprout_or_Rico_or_Chuck_or_Najia
      direction: volatile
      source: "[[sources/PLP-Berry|PLP-Berry]]"
      mechanism: "Berry 可越墙铺地和治疗抗压，但 Sprout/Rico 的墙体几何、Chuck 的路线和 Najia 的毒区都会让地面价值高度依赖地图"
      active_when: "Berry 能覆盖他们必须经过的入口或支援己方处理路线"
      fails_when: "几何让对方从更安全角度输出，或固定路线绕开 Berry puddle"
      bp_use: map_geometry_check_before_accepting_candidate
    - target: Buzz_or_short_entry_body
      direction: subject_favored
      source: "[[sources/PLP-Berry|PLP-Berry]] / [[sources/Fandom-Berry|Fandom-Berry]]"
      mechanism: "Friendship knockback、队友回血和预铺 puddle 可惩罚单一路线的短手进场"
      active_when: "进场路线可预判，Berry 有 gadget 或队友能跟伤"
      fails_when: "Buzz/刺客从侧草或多角度进入，或先骗掉 Friendship 再开团"
      bp_use: anti_aggro_support_if_route_locked
    - target: Trunk_or_Bibi_or_Sam_or_Ash_or_Juju_or_Gray_or_Sirius_or_8_Bit
      direction: target_favored
      source: "[[sources/PLP-Berry|PLP-Berry]]"
      mechanism: "高身体、位移/控制、召唤物或稳定 DPS 会压缩 Berry 的铺地时间，并迫使低血支援先交自保资源"
      active_when: "他们能守住 zone、球路、矿区或金库入口，迫使 Berry 进入其有效范围"
      fails_when: "Berry 在墙后只治疗队友，并由队友先清掉身体/召唤层"
      bp_use: must_answer_body_or_resource_before_berry

  slot_notes:
    slot_1: "只在地图强奖励持续治疗控区，且敌方低成本突进/投掷反制面窄时早手；否则会暴露低血和慢 reload。"
    slot_2_3: "适合和站区身体、Heist 主 DPS 或中路 carrier 组成支援计划，但必须补 anti-dive。"
    slot_4_5: "可用来回答低爆发支援壳或固定路线阵容，同时检查敌方最后手是否能拿硬突进/投掷。"
    slot_6: "如果敌方三人缺远程清支援位和硬突进，Berry 可以作为高质量续航封口 pick。"
```

## 关联页面

- [[sources/Fandom-Berry|Fandom 来源摘要: Berry]]
- [[sources/PLP-Berry|PLP 来源摘要: Berry]]
