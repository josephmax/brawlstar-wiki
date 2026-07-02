# Finx

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：投射物速度控制 / 回溯换位控制英雄

## 来源摘要

- Fandom：[[sources/Fandom-Finx|Fandom 来源摘要: Finx]]
- PLP：[[sources/PLP-Finx|PLP 来源摘要: Finx]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Heist, Hot Zone

## 角色定位总结

Finx 的 BP 价值来自 Time Warp 对投射物速度的改写：友方穿过 Time Warp 的投射物速度提高，敌方投射物速度大幅降低，Finx 自己的攻击穿过 Time Warp 后还获得伤害和充能增益。他可以在长线、热区、宝石矿和金库 lane 中改变 projectile duel 的节奏。核心风险是规则边界很硬：Time Warp 不影响“英雄自身作为 projectile/位移”的攻击，No Escape 会 stun 目标但同时让目标免伤，Back to the Finxture 的回溯点对敌我可见且可被预判。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "long_mid; 8.33 格三并行 projectile，中间弹 900，两侧弹 450"
    projectile_reliability: "medium_high_with_time_warp; 手动瞄准斜角更可靠，Time Warp 可提高己方 projectile 速度"
    burst: "medium_high_with_backtrack_ammo; Back to the Finxture 可回到 3 秒前位置和 ammo，形成六发连打窗口"
    sustained_dps: "high_if_landing_spread; 1.3 秒 very fast reload，Super 区内 projectile 获得 25% 伤害/充能提升"
    objective_damage: "conditional; Heist 依赖长线 projectile boost 和安全回溯，不是直接 safe burst"
    mobility: "medium_high; 770 fast，Back to the Finxture 提供 3 秒位置回溯"
    survivability: "medium; 3700 HP，依赖回溯、射程和 Time Warp 降速来保命"
    engage: "medium; No Escape 可 2 秒控制但免伤，主要用于阻断路线而非集火"
    disengage: "high_with_back_to_the_finxture; 可诱敌后回到 3 秒前点位"
    anti_aggro: "conditional; 回溯能躲刺客第一跳，但 Time Warp 不影响很多自身位移攻击"
    anti_tank: "medium; reload tax 与 projectile slow 可拖前排支援，但缺百分比/硬爆发"
    wall_break: "none"
    throw_or_wall_bypass: "low; Super 可影响 throw projectiles 速度，但不能自己隔墙输出"
    area_control: "high_projectile_field; 3 格 Time Warp 区域持续 7 秒"
    scouting_or_vision: "conditional; Vision/Speed gear 可在草图增强 lane 控制，但无内建 reveal"
    team_support: "high_for_projectile_comps; 友方 projectile 穿过 Time Warp 后速度提高"
    spawnable_or_pet: "none"
    crowd_control: "medium; No Escape stun 2 秒但目标免伤，Hieroglyph Halt 减敌方 reload 25%"
    source_trace:
      - "[[sources/Fandom-Finx|Fandom-Finx]]"
      - "[[sources/PLP-Finx|PLP-Finx]]"

  build_switches:
    - build: "Back To The Finxture / Hieroglyph Halt / Shield, Damage, Vision, Speed"
      source: "[[sources/PLP-Finx|PLP-Finx]]"
      changes_capabilities:
        - "Back To The Finxture 回到 3 秒前位置和 ammo，用于连打六发、骗刺客或逃出短手接触"
        - "Hieroglyph Halt 让被 Finx 攻击命中的敌人 reload 降低 25% 持续 3 秒"
        - "Vision/Speed gears 表示草图可用，但必须落到具体草路和目标职责"
      enables:
        - "长线 projectile duel 改写"
        - "Gem/Hot Zone 中路 reload tax"
        - "Brawl Ball 路线 stall 和逃生"
      mitigates_failure_modes:
        - "assassin_first_contact"
        - "enemy_reload_race"
      best_when: "我方有 projectile 队友可利用 Time Warp，敌方主要输出也是 projectile"
      poor_when: "敌方主要是突进/近身/自体位移攻击，或 No Escape 免伤会破坏我方集火节奏"
      bp_use: "default_plp_projectile_control_build"
    - build: "No Escape / Primer variants"
      source: "[[sources/Fandom-Finx|Fandom-Finx]]"
      changes_capabilities:
        - "No Escape 让下一次攻击 stun 2 秒，但目标免疫所有伤害，适合作为位移/持球/进圈中断"
        - "Primer 通过加速 projectile 命中延长 Super 时长，适合围绕 Time Warp 持续打 projectile duel"
      enables:
        - "Brawl Ball 持球 stall"
        - "Hot Zone 入口延迟"
        - "长线 Time Warp 续场"
      mitigates_failure_modes:
        - "needs_hard_stop_without_kill_commit"
      best_when: "目标收益是拖时间、断动作或保护队友，而不是立刻击杀"
      poor_when: "队友准备爆发集火；No Escape 免伤会让伤害穿过去"
      bp_use: "stall_or_projectile_field_variant"

  map_feature_hooks:
    - id: "time_warp_projectile_lane_duel"
      map_feature_type: "projectile_speed_control_lane"
      uses_feature_by: "Time Warp 加速己方 projectile、降低敌方 projectile 速度，Finx 自身穿区攻击增伤/增充能"
      route_or_position: "Bounty/Knockout 长线、开阔侧路、或队友 projectile 需要经过的射线"
      objective_conversion: "改写长线命中窗口，保护 star/space lead，或让队友更容易先手命中"
      active_when: "双方主要威胁都是 projectile，且 Finx 能把 Time Warp 放在实际弹道路径上"
      fails_if: "敌方用突进、自体位移、近身或墙后 lingering area 绕过 projectile 速度规则"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "map_bp_factors.projectile_duel_modifier"
    - id: "gem_mid_reload_tax_and_backtrack"
      map_feature_type: "gem_mid_projectile_control_and_escape"
      uses_feature_by: "三并行 projectile 控中，Hieroglyph Halt 降 reload，Backtrack 让 Finx 诱敌后回撤"
      route_or_position: "宝石矿中路、中心堡垒入口、侧草到矿的交叉线"
      objective_conversion: "保护矿区访问、拖慢敌方火力循环，并给 carrier 争取撤退空间"
      active_when: "Finx 不做主 carrier，而是作为中路控制和回溯诱敌"
      fails_if: "敌方直接用 Rosa/Mortis/Mico 等不受 Time Warp 影响的进场贴脸"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.gem_mid_control_with_backtrack_escape"
    - id: "brawl_ball_no_escape_stall_and_lane_tempo"
      map_feature_type: "ball_lane_stall_without_damage"
      uses_feature_by: "No Escape 可冻结持球/防守者 2 秒，但目标免伤且球会穿过"
      route_or_position: "中路球权、侧草推进、球门前最后一段路线"
      objective_conversion: "拖住持球、延迟防守动作、或让队友重新站位"
      active_when: "目标收益是 stall/断动作，而不是马上击杀被冻结目标"
      fails_if: "队友误把 No Escape 当集火窗口，或免伤让敌方保住关键血量"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.ball_stall_with_immunity_warning"
    - id: "heist_or_hot_zone_time_warp_team_projectile_anchor"
      map_feature_type: "team_projectile_anchor"
      uses_feature_by: "Time Warp 为队友 safe/zone projectile 提速，同时让敌方 projectile 进入区时显著变慢"
      route_or_position: "金库 lane、热区边缘、L 墙支援口袋或队友射线交汇点"
      objective_conversion: "提高我方 projectile race/站圈命中率，并降低敌方远程清点效率"
      active_when: "我方阵容有 Colt/Piper/Byron 等 projectile 队友，敌方也依赖 projectile 进攻"
      fails_if: "敌方用近身前排、召唤物、投掷 lingering area 或不受影响的位移攻击"
      example_maps:
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
        - "[[entities/maps/Safe Zone|Safe Zone]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "candidate_eval.team_projectile_field_anchor"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "中路 projectile 控制"
        - "reload tax 和回溯逃生"
        - "辅助 carrier 撤退"
      cannot_fulfill:
        - "主 carrier 默认职责"
        - "硬反近身/自体位移刺客"
      needs_teammate_support:
        - "carrier、反突进、清召唤物或前排"
      false_positive: "Time Warp 强在 projectile duel；遇到近身/位移阵容时需要额外防线"
    - mode: "Brawl Ball"
      can_fulfill:
        - "球路 stall"
        - "Time Warp 改写远程防守"
        - "Backtrack 诱敌后撤"
      cannot_fulfill:
        - "稳定破门或直接 scorer"
        - "No Escape 后立刻集火被冻结目标"
      needs_teammate_support:
        - "scorer、破门/强控、近身防守者"
      false_positive: "No Escape 是暂停按钮，不是爆发按钮"
    - mode: "Heist"
      can_fulfill:
        - "队友 projectile 提速辅助 race"
        - "长线 safe lane 控制"
      cannot_fulfill:
        - "像 Colette/Bull 那样直接爆库"
        - "独自守近身进库"
      needs_teammate_support:
        - "真正 safe DPS、反入侵、开线"
      false_positive: "Heist 适配依赖队友 projectile 和 lane 状态，不是单人 objective burst"
    - mode: "Hot Zone"
      can_fulfill:
        - "Time Warp 站圈支援"
        - "reload tax 和 projectile slow"
      cannot_fulfill:
        - "主站圈身体"
        - "清墙后投掷/近身前排"
      needs_teammate_support:
        - "站圈身体、反坦/反刺客、投掷处理"
      false_positive: "Finx 在圈旁很有用，但圈内身体仍要别人承担"

  failure_modes:
    - id: "time_warp_does_not_affect_self_projectile_engage"
      active_when: "敌方主威胁是 Mortis、Kenji、Mico、El Primo、Fang、Bull、Darryl 等自身位移/接触类攻击"
      exposed_by: "[[sources/Fandom-Finx|Fandom-Finx]] Time Warp exception list"
      mitigation: "补硬控/前排/击退，或把 Finx 留作 projectile 阵容回答而非反刺客"
      bp_use: "hard_gate_against_non_projectile_engage"
    - id: "no_escape_immunity_breaks_focus_fire"
      active_when: "Finx 用 No Escape 后队友准备集火被冻结目标"
      exposed_by: "[[sources/Fandom-Finx|Fandom-Finx]] No Escape makes enemies impervious to damage"
      mitigation: "只用来断动作、拖球路、等 cooldown，而不是当作伤害确认"
      bp_use: "control_window_false_positive_filter"
    - id: "backtrack_marker_pre_aimed"
      active_when: "敌方看到 Back to the Finxture 回溯点并预瞄"
      exposed_by: "Fandom notes the shadow hitbox is visible to everyone unless hidden in bushes"
      mitigation: "在草中或安全墙后设置回溯点，避免回到敌方 burst 区"
      bp_use: "escape_route_check"
    - id: "projectile_speed_boost_disrupts_allies_or_lingering_attacks"
      active_when: "队友习惯未提速弹道，或敌方 Emz 等 lingering attack 因减速覆盖更久"
      exposed_by: "Fandom tips warn Time Warp can mess up teammate aim and lingering attacks may cover an area longer"
      mitigation: "只在队友能利用提速的射线放 Super，避免给 lingering area 增值"
      bp_use: "team_synergy_and_enemy_attack_type_check"

  conditional_matchups:
    - target: ["Piper", "Gigi", "Nani", "Byron", "Mandy"]
      direction: "subject_favored"
      source: "[[sources/PLP-Finx|PLP-Finx]]"
      mechanism: "Time Warp 改写 projectile 速度，Finx 和队友的弹道更快，敌方长线 projectile 更难命中"
      active_when: "长线对枪经过 Time Warp 区，敌方主要输出是 projectile 而不是 dive"
      fails_when: "敌方拿到更安全 off-angle，或 Finx 被非 projectile engage 逼离区域"
      bp_use: "projectile_lane_response"
    - target: ["Jae-Yong", "Squeak", "Meg"]
      direction: "subject_favored"
      source: "[[sources/PLP-Finx|PLP-Finx]]"
      mechanism: "reload tax、Time Warp projectile slow 和三弹压线能拖慢支援/控制/目标区身体的节奏"
      active_when: "目标必须在中路、矿、圈或球路附近持续交火"
      fails_when: "Meg/队友用身体直接走进近身，或 Squeak 从安全墙后持续施压"
      bp_use: "mid_control_and_reload_tax"
    - target: ["Crow", "Tara", "Nita", "Sandy"]
      direction: "target_favored"
      source: "[[sources/PLP-Finx|PLP-Finx]]"
      mechanism: "poison/anti-heal、pull、summon bodies、隐蔽和草控可以绕过或稀释 Finx 的 projectile field"
      active_when: "他们控制草口、召唤物挡线，或迫使 Finx 回溯点暴露"
      fails_when: "视野清楚，summon 被清，Finx 用 Time Warp 只打远程 lane"
      bp_use: "requires_vision_and_body_clear"
    - target: ["Damian", "Rosa", "Poco", "Emz"]
      direction: "target_favored"
      source: "[[sources/PLP-Finx|PLP-Finx]]"
      mechanism: "墙压、前排身体、团队续航或 lingering area 让 Finx 的 projectile slow 难以转成击杀"
      active_when: "目标区需要站人或墙后控制，Finx 缺前排/开墙/爆发跟进"
      fails_when: "队友提供真实 DPS 和站圈身体，Finx 只承担 projectile field 支援"
      bp_use: "avoid_as_only_zone_or_sustain_answer"

  slot_notes:
    slot_1: "只有当地图和我方前两手明显奖励 projectile field 时才早手；否则容易被近身/召唤物低成本回答"
    slot_2_3: "适合与长线 projectile 队友一起建立 lane 计划，并让后续补前排或反突进"
    slot_4_5: "看到敌方主要是 projectile 长手/支援时，Finx 可以作为节奏改写和 reload tax 补位"
    slot_6: "可最后手惩罚缺突进的长线阵容；不能用来单独解决 tank、assassin 或 sustain shell"
```

## 关联页面

- [[sources/Fandom-Finx|Fandom 来源摘要: Finx]]
- [[sources/PLP-Finx|PLP 来源摘要: Finx]]
