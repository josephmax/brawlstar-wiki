# Colette

## 基本信息

- 稀有度：Epic
- 定位：Damage Dealer
- 类型：当前生命值百分比压制 / Push It 目标位移

## 来源摘要

- Fandom：[[sources/Fandom-Colette|Fandom 来源摘要: Colette]]
- PLP：[[sources/PLP-Colette|PLP 来源摘要: Colette]]
- PLP 推荐模式：Heist, Brawl Ball, Gem Grab, Hot Zone

## 角色定位总结

Colette 的 BP 价值来自两条线：对 Brawler 用当前生命值百分比削血，对 safe / IKE / spawnable 等 special target 用固定高额伤害；Super 则按最大生命值往返结算，并可用 `Push It` 把目标推到最远点和短暂打断。她能稳定惩罚高血量目标、Brawl Ball 防守者和 Heist safe，但不是纯收割手：敌人血量越低，普通攻击越接近最低伤害；Super 冲入高爆发或控制链也会直接变成送位。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-17"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "long_mid; 8.67 格直线 projectile，Super 11 格往返"
    projectile_reliability: "medium_high_on_linear_lanes; 单发直线，命中率依赖路线和墙体"
    burst: "high_vs_high_hp_or_special_targets; 两普攻加 Super 可击杀多数无盾/无回复目标"
    sustained_dps: "medium; 1.6 秒装填，伤害随目标当前血量下降；普通攻击每发只充 22.5% Super，默认要命中 5 发；Gotcha! 最多三发各 25%，随后一发普通攻击累计也只有 97.5%，不能恢复固定 4 发循环"
    objective_damage: "very_high_in_heist; safe 作为 special target，Super 往返和 Hypercharge 可造成大额固定伤害"
    mobility: "conditional; Super 快速往返、可过水，但会撞墙停止并回起点"
    survivability: "low_medium; Power 11 本体 7200 HP，Mass Tax 在 Super 中 60% 减伤对应 18000 EHP，叠满 Shield gear 为 20250；这是短暂往返窗口且不能与 Super 后 30% 护盾叠加"
    engage: "medium; Super 可冲线和位移目标，但需要确认 burst/CC"
    disengage: "medium; Super 返回原点，可拾宝/穿水后回撤"
    anti_aggro: "high_vs_high_hp_body; Push It 打断和百分比削血克制前排"
    anti_tank: "high; 当前血量百分比 + 最大血量 Super 是核心职责"
    wall_break: "none"
    throw_or_wall_bypass: "conditional; Super 可过水但不能穿墙，Na-ah Buffie 才可穿墙/穿透"
    area_control: "medium; Push It 可移走球门/热区/金库防守者"
    scouting_or_vision: "low"
    team_support: "damage setup; 把高血量目标压到队友可收割线"
    spawnable_or_pet: "medium_damage_to_special_targets"
    crowd_control: "medium_high_with_push_it_or_na_ah; Push It 推人/打断，当前 Fandom 机制页把 0.5 秒 charm 归于 Na-ah"
    source_trace:
      - "[[sources/Fandom-Colette|Fandom-Colette]]"
      - "[[sources/PLP-Colette|PLP-Colette]]"

  build_switches:
    - build: "Na-ah! / Push It / Shield, Damage"
      source: "[[sources/PLP-Colette|PLP-Colette]]"
      changes_capabilities:
        - "Na-ah! 提供 0.5 秒 hypnotize，用于短暂拉近目标或打断路线；本身不造成伤害、消耗 ammo 且冷却 22 秒"
        - "Push It 保证 Super 命中的目标被带到最大距离并短暂 stun，常用于防守、进球窗口和确认两段 Super"
        - "Shield/Damage gears 改善低血量生存和最低伤害收割线"
      enables:
        - "Brawl Ball 防守者位移和持球打断"
        - "Hot Zone 把目标推出圈"
        - "Heist 推开防守者或把 safe Super 两段确认"
      mitigates_failure_modes:
        - "super_only_hits_once_or_misses_return"
        - "target_holds_objective_position"
      best_when: "敌方有高血量身体、守门/站圈/守库目标，且 Colette 能安全打到第一发"
      poor_when: "敌方以召唤物、投掷、分身或多角度低血量 poke 稀释 Colette 的目标选择"
      bp_use: "default_plp_percent_damage_and_displacement_build"
    - build: "Gotcha! / Mass Tax / Shield, Damage"
      source: "[[sources/Fandom-Colette|Fandom-Colette]]"
      changes_capabilities:
        - "Gotcha! 让接下来最多三发攻击按伤害 80% 回血，并把这三发的 Super 充能提高到每发 25%；三发后接一发普通攻击累计 97.5%，仍不能把下一次 Super 当作固定四发资源"
        - "Mass Tax 在 Super 中给 60% 减伤，并在命中后给 30% 短盾"
      enables:
        - "Heist 反复 Super safe 后存活"
        - "长线消耗和低血续航"
      mitigates_failure_modes:
        - "dies_during_super_commit"
        - "chip_pressure_before_percent_damage_converts"
      best_when: "目标是反复打 safe 或需要 Colette 独自扛一段消耗"
      poor_when: "模式需要 Push It 的位移/打断来创造目标收益"
      bp_use: "heist_or_sustain_variant"

  map_feature_hooks:
    - id: "heist_special_target_super_burst"
      map_feature_type: "special_target_safe_damage"
      uses_feature_by: "safe 作为 special target，Colette Super 往返固定伤害；Hypercharge 可进一步放大"
      route_or_position: "safe 直线、金库前入口、或可过水往返的打库路径"
      objective_conversion: "把一次 Super 转成高额 safe burst，并用 Push It/Mass Tax处理防守者"
      active_when: "Colette 已有 Super，或能在该 lane 安全完成 5 发有效命中；Gotcha! 只能减少前三发的充能缺口，且直线路径不被墙体阻断"
      fails_if: "墙体挡住 Super、敌方 burst/CC 守住路径，或 race 需要更稳定远程 DPS"
      example_maps:
        - "[[entities/maps/Safe Zone|Safe Zone]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
      bp_use: "required_capabilities.heist_percent_or_special_target_burst"
    - id: "brawl_ball_push_it_goal_clear"
      map_feature_type: "goal_defender_displacement"
      uses_feature_by: "Push It 把目标推到 Super 最远点并打断持球/防守动作"
      route_or_position: "球门前防守线、持球者推进路线、或 overtime 开阔门口"
      objective_conversion: "清守门人、让敌方掉球，或把前排推出得分线"
      active_when: "队友有 scorer/射门角度，Colette Super 路径不会被墙挡住"
      fails_if: "目标被推到 Colette 普攻射程外后反打，或敌方硬控打断 Super"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.goal_clear_and_ball_disarm"
    - id: "hot_zone_push_it_zone_clear"
      map_feature_type: "zone_body_displacement"
      uses_feature_by: "百分比伤害压前排，Push It 把站圈者推出圈边"
      route_or_position: "单圈入口、zone 中心身体、或墙边站圈路线"
      objective_conversion: "把高血量站圈目标削血并移出热区，争取计分反转"
      active_when: "敌方依赖 tank/body 站圈且 Colette 队友能接清"
      fails_if: "敌方投掷/召唤物在墙后控圈，或 Colette 冲入后被多目标集火"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "map_bp_factors.zone_body_removal"
    - id: "gem_mid_anti_body_and_emergency_carrier"
      map_feature_type: "gem_mid_percent_damage_and_dash_retrieve"
      uses_feature_by: "对高血量中路/护送者稳定削血，Super 可拾宝后回到原点"
      route_or_position: "宝石矿中路、carrier 撤退线、或高血量 bodyguard 的入口"
      objective_conversion: "压低前排保护 carrier，或主 carrier 倒下后用 Super 抢回宝石"
      active_when: "队伍有常规 carrier，Colette 主要负责反前排和应急拾宝"
      fails_if: "她被要求长期持宝，或敌方召唤物/墙后控制阻断主目标"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "candidate_eval.anti_body_with_emergency_carrier"

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - "special target safe burst"
        - "Super 往返打库"
        - "Push It 推开防守者或 Mass Tax 扛伤"
      cannot_fulfill:
        - "穿墙打库"
        - "无 Super 时稳定远程 race"
      needs_teammate_support:
        - "开线、治疗/保护、压住反杀点"
      false_positive: "Colette Heist 很强，但路径被墙或控制堵住时爆发无法转化"
    - mode: "Brawl Ball"
      can_fulfill:
        - "清守门人"
        - "打断持球和反前排"
        - "把高血量 scorer 推出得分线"
      cannot_fulfill:
        - "稳定破门"
        - "独自 carry 进球"
      needs_teammate_support:
        - "scorer、破门、补伤"
      false_positive: "Push It 创造窗口，真正进球还要靠队友和球门状态"
    - mode: "Hot Zone"
      can_fulfill:
        - "反站圈身体"
        - "Push It 赶人出圈"
      cannot_fulfill:
        - "独自长期站圈"
        - "清墙后投掷"
      needs_teammate_support:
        - "站圈者、反投掷、清召唤物"
      false_positive: "反 tank 不等于控圈；还要有人站住点"
    - mode: "Gem Grab"
      can_fulfill:
        - "反高血量护送"
        - "应急拾宝返回"
      cannot_fulfill:
        - "安全常规 carrier"
        - "处理所有召唤物/墙控"
      needs_teammate_support:
        - "主 carrier、探草、清召唤物"
      false_positive: "Super 抢宝是应急工具，不应当作默认 carrier 计划"

  failure_modes:
    - id: "super_cycle_is_not_a_fixed_four_hits"
      active_when: "阵容把 Colette 的下一次 Super 当成四次命中后的固定资源，包括误以为 Gotcha! 三发加一发普通攻击即可充满"
      exposed_by: "[[sources/Fandom-Colette|Fandom-Colette]] 普攻每发 22.5%；Gotcha! 只有最多三发各 25%，三发后接一发普通攻击累计 97.5%"
      mitigation: "无既有充能时按 5 次有效命中预算 Super；Gotcha! 只用于续航和缩小充能缺口，不用它承诺四发循环"
      bp_use: "resource_tracking.super_cycle_by_build"
    - id: "low_health_target_damage_floor"
      active_when: "敌人已低血，Colette 普攻只打最低伤害而无法立刻收割"
      exposed_by: "[[sources/Fandom-Colette|Fandom-Colette]] current-health scaling"
      mitigation: "用 Damage gear、Na-ah!、队友收割或保留 Super 完成最后一段"
      bp_use: "candidate_eval.finish_damage_check"
    - id: "super_path_burst_or_cc"
      active_when: "Colette Super 路径经过 Bull、Edgar、Shelly、Buzz、Nani、Emz 等 burst/CC 位置"
      exposed_by: "Fandom warns high burst can defeat Colette during Super commit"
      mitigation: "先耗 ammo/控制，使用 Mass Tax，或只用 Push It 打断安全目标"
      bp_use: "hard_gate_before_super_commit"
    - id: "push_it_displaces_out_of_followup"
      active_when: "Push It 把远程目标推离 Colette 和队友可追击范围"
      exposed_by: "Fandom warns Push It can push outranging targets out of range"
      mitigation: "只在目标收益是清门/推出圈/保证两段命中时用"
      bp_use: "objective_conversion_filter"
    - id: "summon_or_wall_control_target_dilution"
      active_when: "敌方用 Mr. P、Larry & Lawrie、Eve、Tara 等召唤/墙控稀释 Colette 的单目标节奏"
      exposed_by: "[[sources/PLP-Colette|PLP-Colette]] target-favored signal list"
      mitigation: "补清召唤物、开墙或改用更稳定 area damage"
      bp_use: "must_answer_body_block_and_wall_control"

  conditional_matchups:
    - target: ["Mico", "El Primo", "R-T"]
      direction: "subject_favored"
      source: "[[sources/PLP-Colette|PLP-Colette]]"
      mechanism: "百分比伤害和 Push It 让高血量/近身目标在进入目标区前被稳定削血或推走"
      active_when: "目标必须进球门、热区、safe 防守或宝石中路，Colette 有射线"
      fails_when: "目标从墙草突脸且 Colette Super 会被 burst/CC 惩罚"
      bp_use: "anti_body_or_anti_tank_response"
    - target: ["Jae-Yong", "Gray", "Sprout", "Mandy", "Brock"]
      direction: "subject_favored"
      source: "[[sources/PLP-Colette|PLP-Colette]]"
      mechanism: "长射程 chip、Na-ah! 拉近和 Super 往返可惩罚缺持续回复或站位固定的支援/控制/长手"
      active_when: "目标没有召唤物挡线，Colette 可用 Super 或队友完成收割"
      fails_when: "目标拥有更安全墙后角度，或 Push It 把目标推出追击范围"
      bp_use: "poke_then_displace_pick_window"
    - target: ["Damian", "Mr. P", "Willow", "Larry & Lawrie", "Eve"]
      direction: "target_favored"
      source: "[[sources/PLP-Colette|PLP-Colette]]"
      mechanism: "墙后控制、召唤物、mind control 或额外 bodies 会阻断 Colette 直线和单目标百分比节奏"
      active_when: "墙体/水域/召唤物让 Colette 无法稳定打到真正目标"
      fails_when: "队友清 bodies/开墙，Colette 只用 Super 处理高价值目标"
      bp_use: "must_answer_wall_or_body_block"
    - target: ["Tara", "Crow", "Lola"]
      direction: "target_favored"
      source: "[[sources/PLP-Colette|PLP-Colette]]"
      mechanism: "pull, poison anti-heal, clone/body pressure, or split angles punish Colette's Super path and low health"
      active_when: "他们能预判 Colette 冲刺路线或从多个角度消耗她"
      fails_when: "关键控制已交，Colette 用 Mass Tax/Push It 只处理前排目标"
      bp_use: "avoid_without_control_bait_or_clean_lane"

  slot_notes:
    slot_1: "Heist 或高前排模式可早手，但要准备回答召唤物和墙后控制"
    slot_2_3: "适合在敌方先出 tank/body 后补，直接定义反前排职责"
    slot_4_5: "看到球门/热区/safe 有明确位移收益时，Colette 的 Push It 价值上升"
    slot_6: "可惩罚高血量目标和无 body-block 的后排；不能修补队伍缺 area clear"
```

## 关联页面

- [[sources/Fandom-Colette|Fandom 来源摘要: Colette]]
- [[sources/PLP-Colette|PLP 来源摘要: Colette]]

## 战斗断点输入

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "Colette",
    "target_states": [
      {
        "id": "body",
        "entity_class": "brawler_body",
        "roster_target": true,
        "health": {"amount": 3600, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-Colette|Fandom-Colette]]"
      }
    ],
    "damage_packets": [],
    "defense_modifiers": [
      {
        "id": "mass_tax_during_super",
        "source_kind": "star_power",
        "loadout_group": "mass_tax_phase",
        "applies_to_states": ["body"],
        "effect": {"type": "damage_reduction", "ratio": 0.60},
        "active_when": "Colette 正在执行 Super 往返",
        "sequence_validity": "Super 结束时失效；不与命中后的 30% 护盾叠加",
        "source_ref": "[[sources/Fandom-Colette|Fandom-Colette]]"
      },
      {
        "id": "mass_tax_post_super",
        "source_kind": "star_power",
        "loadout_group": "mass_tax_phase",
        "applies_to_states": ["body"],
        "effect": {"type": "damage_reduction", "ratio": 0.30},
        "active_when": "Super 命中过目标且 Super 已结束后的最多 3 秒",
        "sequence_validity": "与 during-Super 60% 状态互斥",
        "source_ref": "[[sources/Fandom-Colette|Fandom-Colette]]"
      }
    ],
    "excluded_temporal_defenses": [
      {
        "id": "gotcha_overheal_buffie",
        "reason": "最多 1000 的护盾每 0.15 秒衰减 50；没有命中时间轴时不能当静态 EHP",
        "source_ref": "[[sources/Fandom-Colette|Fandom-Colette]]"
      }
    ]
  }
}
```
