# Piper

## 基本信息

- 稀有度：Epic
- 定位：Marksman
- 来源：Epic 远程狙击英雄

## 攻击特征

- 主攻击是远距离单发狙击弹。
- 距离越远伤害越高，近距离命中价值明显下降。
- 装填很慢，空枪和被迫近身都会迅速降低价值。

## 超级技能特征

- Super 让 Piper 向后跳跃并丢下炸弹。
- 主要用途是脱离近身、重新找角度，也能破坏部分地形。
- `Auto Aimer` 提供短距离反突进窗口，`Snappy Sniping` 提高命中后的续航输出。

## 角色定位总结

Piper 是典型极长线狙击手。她的 BP 价值来自开阔地图的低承诺高伤害和对脆弱长手的压制，但所有结论都必须被地图开阔度、草丛、墙体、召唤物和敌方机动性重新条件化。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-06-30-v2
    plp: direct_raw_capture_2026-06-30
    user_notes: none

  capability_vector:
    effective_range: very_long
    projectile_reliability: high_on_open_lanes_medium_into_speed
    burst: high_at_max_range
    sustained_dps: low_medium; 很慢装填，依赖命中和 Snappy Sniping
    objective_damage: medium_conditional_in_heist; 更偏赢线和远程打库角度
    mobility: defensive_reposition_with_Super
    survivability: low_base_health_but_escape_resource_available
    engage: low
    disengage: high_if_Super_or_Auto_Aimer_available
    anti_aggro: conditional_with_Auto_Aimer_and_Super
    anti_tank: low_medium; 需要距离和队友控制
    wall_break: conditional_with_Super_bombs
    throw_or_wall_bypass: low
    area_control: low
    scouting_or_vision: low
    team_support: long_range_pick_pressure
    terrain_destruction: medium_with_Super

  build_switches:
    - build: Auto Aimer / Snappy Sniping / Shield + Damage
      source: "[[sources/PLP-Piper|PLP-Piper]] / [[sources/Fandom-Piper|Fandom-Piper]]"
      changes_capabilities:
        - Auto Aimer 提供近身推开和保命窗口
        - Snappy Sniping 奖励高命中长线压制
      enables:
        - long_range_star_pressure
        - anti_aggro_escape
        - heist_open_lane_poke
      mitigates_failure_modes:
        - close_range_collapse
        - very_slow_reload_after_hit
      poor_when:
        - 敌方主要威胁是召唤物、投掷或多角度机动，而不是单个近身目标
      bp_use: 默认竞技 build；适合长线对枪和自保
    - build: Homemade Recipe / Ambush burst variant
      source: "[[sources/Fandom-Piper|Fandom-Piper]]"
      changes_capabilities:
        - 提高远端单发命中和草丛爆发上限
      enables:
        - sniper_mirror_pick
        - bush_angle_burst
      mitigates_failure_modes:
        - 长线镜像中关键一枪命中率不足
      poor_when:
        - 地图草丛不可控，或必须保留 Auto Aimer 防突进
      bp_use: 极长线镜像或可控草角时的 build requirement

  map_feature_hooks:
    - map_feature_type: extreme_open_bounty_lane
      uses_feature_by: 在极开阔 Bounty/Knockout lane 用满距离高伤害拿星或逼退
      objective_conversion: first pick、保星、迫使敌方穿越开阔区
      active_when: 掩体少、草丛少、队友能保护侧路
      fails_if: 敌方有 Nani/Angelo/R-T 等更强镜像，或有墙体/召唤物挡枪
      example_maps:
        - Shooting Star
        - Dry Season
        - Out in the Open
        - Hideout
      bp_use: required_capabilities.extreme_range_star_pressure
    - map_feature_type: heist_open_safe_lane_snipe
      uses_feature_by: 用远程单发赢边路并从安全角度打库或防守入库者
      objective_conversion: Heist 远程 safe chip、迫使回防、保护己方 safe lane
      active_when: 边路直线长，敌方缺中心草/侧路突进压 Piper
      fails_if: race 需要更高持续 DPS，或敌方短手从草/墙直接贴近
      example_maps:
        - Bridge Too Far
        - Kaboom Canyon
        - Safe Zone
        - Hot Potato
      bp_use: candidate_eval.heist_open_lane_marksman
    - map_feature_type: super_escape_and_thin_wall_break
      uses_feature_by: Super 后跳保命并用炸弹破坏薄墙/门前墙，重置长线结构
      objective_conversion: Bounty 保命、Heist/Brawl Ball 选择性开墙、反投掷/短手掩体
      active_when: 开墙后我方远程更强，且 Piper 不会因此失去唯一保护
      fails_if: overbreak 帮助敌方突进或移除己方保命墙
      example_maps:
        - Dry Season
        - Shooting Star
        - Belle's Rock
        - Center Stage
      bp_use: terrain_state_plan.escape_or_transform

  objective_contracts:
    - mode: Bounty_or_Knockout
      can_fulfill:
        - extreme_range_pick
        - star_or_round_lead_protection
        - anti_open_lane_marksman_pressure
      cannot_fulfill:
        - stand_on_objective
        - reliable_close_range_duel_without_resource
      needs_teammate_support:
        - grass_check
        - anti_thrower_or_spawnable_clear
      false_positive: 地图只要有侧草或墙体口袋，Piper 就需要队友先处理接近路线
    - mode: Heist
      can_fulfill:
        - open_lane_safe_chip
        - lane_defense_against_midrange
        - selective_wall_break_with_Super
      cannot_fulfill:
        - fastest_primary_safe_race
      needs_teammate_support:
        - dedicated_safe_dps_or_body
        - center_bush_control
      false_positive: Heist 中 Piper 不是纯 DPS 机器，更像赢线和远程角度组件

  failure_modes:
    - id: close_range_damage_drop
      active_when: 敌方 Mortis/Max/Gray/Leon 等从侧路或墙草接近
      exposed_by: Fandom 距离增伤机制与 PLP counteredBy
      mitigation: Auto Aimer、Super、视野、队友 peel
      bp_use: must_avoid_or_needs_protection
    - id: wall_or_spawnable_blocks_single_shot
      active_when: Mr. P、Tick、墙体口袋或召唤物让 Piper 很慢装填被低成本消耗
      exposed_by: PLP counteredBy 与地图墙体模型
      mitigation: 开墙、队友清召唤物、换到开阔图
      bp_use: false_positive_filter
    - id: sniper_mirror_outscaled
      active_when: Nani/Angelo/R-T 等在同一开阔 lane 拥有更高爆发、角度或反射资源
      exposed_by: PLP counteredBy
      mitigation: Homemade Recipe、掩体节奏、队友交叉火力
      bp_use: matchup_and_build_check

  conditional_matchup_seeds:
    - target: Brock_or_Mandy_or_Belle_or_Byron
      direction: subject_favored
      source: "[[sources/PLP-Piper|PLP-Piper]]"
      mechanism: Piper 在纯开阔远端用高伤害单发和 Snappy reload 惩罚同类长线的低机动站位
      active_when: 地图开阔、Piper 有满距离角度、对方缺更安全掩体或召唤物
      fails_when: 对方有开墙/极远 Super/治疗队友，或 Piper 被迫移动丢失输出节奏
      bp_use: sniper_mirror_response_seed
    - target: Gene_or_Bea_or_Bonnie_or_Colt
      direction: subject_favored
      source: "[[sources/PLP-Piper|PLP-Piper]]"
      mechanism: 满距离伤害能在他们建立控制、支援或中距离 DPS 前先压低血量
      active_when: 目标需要走进 Piper 的长线才能发挥，且没有稳定突进保护
      fails_when: 目标通过墙体、召唤物或队友 speed/peel 缩短距离
      bp_use: long_lane_punish_seed
    - target: Nani_or_Angelo_or_R-T_or_Tick
      direction: target_favored
      source: "[[sources/PLP-Piper|PLP-Piper]]"
      mechanism: 更高爆发、特殊弹道、标记或投掷压力会让 Piper 的单发长线优势失效
      active_when: 地图允许他们从更安全角度输出或用召唤/墙体限制 Piper
      fails_when: Piper 有先手草角、Homemade Recipe 或队友先清投掷/标记资源
      bp_use: avoid_blind_sniper_mirror
    - target: Max_or_Mortis_or_Gray_or_Mr_P
      direction: target_favored
      source: "[[sources/PLP-Piper|PLP-Piper]]"
      mechanism: 速度、dash、传送或 porter 弹药税能越过/消耗 Piper 的单发节奏
      active_when: 地图有侧路、墙体、草丛或宠物线路，Piper 无法保持满距离
      fails_when: 地图极开阔且 Piper 持有 Auto Aimer/Super 与队友 peel
      bp_use: must_answer_mobility_or_body_tax

  slot_notes:
    slot_1: 只在 Shooting Star/Dry Season 这类开阔基本面极强时考虑；否则早手会暴露给机动、投掷和召唤物。
    slot_2_3: 适合建立长线基本面或回答低机动长手，但需要同时补草控。
    slot_4_5: 可作为敌方缺机动/缺投掷时的远程惩罚位，并检查敌方最后手是否有 Max/Mortis/Gray。
    slot_6: 如果敌方三人无法触碰开阔长线，Piper 是高质量收口 pick；否则要优先排除侧路风险。
```

## 关联页面

- [[sources/Fandom-Piper|Fandom 来源摘要: Piper]]
- [[sources/PLP-Piper|PLP 来源摘要: Piper]]
