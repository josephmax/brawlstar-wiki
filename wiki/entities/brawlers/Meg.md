# Meg

## 基本信息

- 稀有度：Legendary
- 定位：Tank
- 类型：机甲形态中线控制 / 目标区前排

## 来源摘要

- Fandom：[[sources/Fandom-Meg|Fandom 来源摘要: Meg]]
- PLP：[[sources/PLP-Meg|PLP 来源摘要: Meg]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Hot Zone, Heist

## 角色定位总结

Meg 的 BP 价值是形态节奏：本体很脆但移动快、射程长，机甲形态提供身体、宽弹幕和有资源门槛的近身 swing。她适合需要“站住中线/热区/球门前”的地图，也能在 Heist 用机甲期打出可观 safe 压力。风险在于变身 1 秒窗口可被打断，机甲破掉后本体容易被收割；机甲普攻每枚命中只提供 2.703% Super 充能，不能把 Heavy Metal 回血、偷 ammo 或 swing 驱赶当作每轮目标战都有的循环。

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
    effective_range: "long_stateful; 本体 9 格低伤 poke，机甲 7.33 格宽弹幕负责中线压制"
    projectile_reliability: "medium_high_in_mecha; 宽弹幕和 swing 对中近距离可靠，远距离单点精度一般"
    burst: "medium; 机甲 Super swing 近身爆发高，本体爆发低"
    sustained_dps: "high_in_mecha; 机甲 1.1 秒装填和多弹幕适合持续压目标区，本体输出较低"
    objective_damage: "high_when_mecha_online; Heist 和目标区推进依赖机甲 uptime"
    mobility: "stateful; 本体 very fast，机甲 normal，整体不是突进位"
    survivability: "stateful_high_if_mecha; 本体 2400 HP 很脆，机甲 3700 HP 加 Jolting Volts 提高站场"
    engage: "medium; 通过机甲身体和范围 swing 推进，不靠瞬间位移"
    disengage: "low_after_mecha_break; 机甲破后本体易被追死"
    anti_aggro: "medium_high_in_mecha; 宽弹幕和进机甲时的范围伤害/击退提供稳定防线；Mecha Super swing、Heavy Metal 回血和偷 ammo 受每枚命中 2.703% Super 充能约束，是低频资源"
    anti_tank: "medium; 机甲持续火力可磨前排，但怕高爆发贴脸和控制链"
    wall_break: "none"
    throw_or_wall_bypass: "none"
    area_control: "high_in_mecha; 宽弹幕和 swing 能守入口、热区和球门"
    scouting_or_vision: "low"
    team_support: "conditional; Jolting Volts Buffie 可同时治疗机甲与附近队友，Heavy Metal Buffie 可从被 Super 命中的敌人偷取 ammo"
    spawnable_or_pet: "none; Toolbox 不再部署 reload turret，而是弹射当前机甲并开始回充 Super"
    crowd_control: "conditional; 进入机甲时会范围伤害并击退，充能后的 Mecha Super swing 可驱赶近身，Hypercharge 还会短暂减速附近敌人；不能假设每轮目标战都有 swing"

  build_switches:
    - build: "Jolting Volts / Heavy Metal / Shield, Damage"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      changes_capabilities:
        - "Jolting Volts 延长机甲 uptime；Buffie 还会治疗附近队友并把持续时间从 5 秒延长到 6 秒"
        - "Heavy Metal 让 Mecha Super 每命中一个敌人回复 1200 生命；Buffie 还会从每个被命中的敌人偷取 1 ammo，但机甲普攻每枚命中只充 2.703% Super，这属于需要预先积累的关键目标战资源"
      enables:
        - "Hot Zone/Brawl Ball 的目标区身体"
        - "Heist 的机甲期 safe 压力"
        - "Gem Grab 中线控场"
        - "目标区团队治疗和前排 ammo 压制"
      mitigates_failure_modes:
        - "mecha_uptime_taxed_by_poke"
        - "mecha_ammo_pressure_during_objective_fight"
        - "slow_mecha_super_cycle"
      best_when: "地图奖励站点、守入口或持续目标压力"
      poor_when: "敌方能用墙后投掷、召唤物或高爆发近身持续打断机甲循环，或 BP 计划依赖每轮目标战重复获得 Mecha Super"
      bp_use: "default_plp_mecha_control_build"
    - build: "Toolbox / Force Field or Heavy Metal / Shield, Damage"
      source: "[[sources/Fandom-Meg|Fandom-Meg]]"
      changes_capabilities:
        - "Toolbox 让 Meg 主动弹出并向前发射机甲，沿途和爆炸时造成伤害，随后在 6 秒内回充 Super"
        - "Force Field 在离开机甲后提供 40% 护盾；Buffie 在护盾期间再提供 20% 移速"
      enables:
        - "把即将失效的机甲转成直线伤害并计划性重进机甲"
        - "Heist/Hot Zone 中的短暂离甲换位和第二轮机甲压力"
      mitigates_failure_modes:
        - "base_form_collapse_after_mecha_destroyed"
        - "bad_mecha_position_without_reset"
      best_when: "机甲可沿明确路线命中目标，且 Meg 能靠护盾/队友覆盖度过 6 秒回充窗口"
      poor_when: "敌方能在本体期立即爆发收割，或弹射路线没有目标且会无意义放弃机甲身体"
      bp_use: "planned_mecha_reset_variant"

  map_feature_hooks:
    - id: "hot_zone_mecha_mid_body_control"
      map_feature_type: "single_zone_body_and_entry_control"
      uses_feature_by: "机甲身体站圈、宽弹幕守入口，Jolting Volts 延长站圈时间；已充好的 swing 用于关键清圈而不是默认反复驱赶"
      objective_conversion: "Hot Zone 单圈图中把站住中心转成持续计分"
      active_when: "入口清晰、敌方必须穿过 choke 进圈，队友能帮 Meg 清投掷/召唤物"
      fails_if: "敌方墙后投掷或召唤物反复消耗机甲、变身窗口被打断，或阵容把低频 swing 误当作每轮都有的清圈资源"
      example_maps: ["[[entities/maps/Dueling Beetles|Dueling Beetles]]", "[[entities/maps/Ring of Fire|Ring of Fire]]", "[[entities/maps/Open Business|Open Business]]", "[[entities/maps/Parallel Plays|Parallel Plays]]"]
      bp_use: "Hot Zone 中心身体核心"
    - id: "brawl_ball_mecha_goal_defense_and_push_body"
      map_feature_type: "goal_entry_pressure_and_anti_aggro"
      uses_feature_by: "机甲在球门前抗伤并用宽弹幕守门；进入机甲时的范围伤害/击退可打断持球推进，已充好的 swing 配合 Heavy Metal 回血/偷 ammo 只用于关键接触"
      objective_conversion: "把人数/血量优势转成持球推进或防守清球"
      active_when: "队伍有破门、得分手或控人，Meg 负责站住球门区域"
      fails_if: "敌方用投掷/召唤物绕过机甲、机甲破后本体被连续击杀，或连续推进要求 Meg 在未重新充好 swing 时反复缴械持球人"
      example_maps: ["[[entities/maps/Center Stage|Center Stage]]", "[[entities/maps/Sneaky Fields|Sneaky Fields]]", "[[entities/maps/Triple Dribble|Triple Dribble]]", "[[entities/maps/Pinball Dreams|Pinball Dreams]]"]
      bp_use: "足球前排/防守核心；仍需 scoring tool"
    - id: "heist_mecha_safe_lane_uptime"
      map_feature_type: "safe_dps_after_lane_win"
      uses_feature_by: "机甲期宽弹幕和持续输出赢边路后打 safe，Jolting Volts 延长 safe pressure"
      objective_conversion: "把机甲上线期转成金库 race 领先"
      active_when: "Meg 能安全变身并靠队友赢线，敌方缺快速清机甲资源"
      fails_if: "本体期被压死，或敌方 race 更快且无须处理 Meg"
      example_maps: ["[[entities/maps/Hot Potato|Hot Potato]]", "[[entities/maps/Pit Stop|Pit Stop]]", "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]", "[[entities/maps/Bridge Too Far|Bridge Too Far]]"]
      bp_use: "Heist 条件 safe pressure，依赖机甲上线"
    - id: "gem_mid_mecha_control_with_carrier_warning"
      map_feature_type: "gem_mine_mid_control"
      uses_feature_by: "机甲站中线和入口，宽弹幕压缩敌方拾宝空间"
      objective_conversion: "控制宝石矿和撤退半径，但不建议在机甲破坏风险高时做唯一 carrier"
      active_when: "队伍有独立 carrier 或能保护本体重置"
      fails_if: "Meg 机甲破后携带宝石，或敌方侧草/投掷持续逼退中心"
      example_maps: ["[[entities/maps/Gem Fort|Gem Fort]]", "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]", "[[entities/maps/Double Swoosh|Double Swoosh]]"]
      bp_use: "Gem Grab 中线身体；carrier 职责需谨慎分配"

  objective_contracts:
    - mode: "Hot Zone"
      can_fulfill:
        - "机甲站圈、用宽弹幕守入口，并把已充好的范围 swing 用于关键清圈"
      cannot_fulfill:
        - "独自处理墙后投掷/炮台体系"
      needs_teammate_support:
        - "清投掷、开墙、治疗或区域控制"
      false_positive: "Meg 能站圈，但机甲循环被断或 BP 高估低频 swing 的清圈次数时，计分能力会迅速下降"
    - mode: "Brawl Ball"
      can_fulfill:
        - "球门防守、前排推进、吸收火力，以及有资源时的一次 swing 清球"
      cannot_fulfill:
        - "单独破门或稳定 carry 进球"
      needs_teammate_support:
        - "scorer、破门/强控、清投掷"
      false_positive: "有身体不等于有得分路径；有 Mecha Super 机制也不等于每轮防守都有 swing"
    - mode: "Heist"
      can_fulfill:
        - "机甲上线后边路压制和 safe DPS"
      cannot_fulfill:
        - "本体期稳定打库或远程低承诺打库"
      needs_teammate_support:
        - "帮 Meg 安全变身、赢线和防快攻"
      false_positive: "Heist 价值高度依赖机甲 uptime，不是开局就稳定 race"
    - mode: "Gem Grab"
      can_fulfill:
        - "中线站位、入口压制、保护 carrier 撤退路线"
      cannot_fulfill:
        - "在高风险机甲破坏阶段做唯一 carrier"
      needs_teammate_support:
        - "独立载宝位、探草和反投掷"
      false_positive: "中线身体强不代表载宝安全"

  failure_modes:
    - id: "mecha_transform_cancel_window"
      active_when: "Meg 开 Super 变身时处于敌方 stun、knockback、pull 或爆发范围"
      exposed_by: "Super has 1 second delay and can be cancelled"
      mitigation: "在墙后、安全血量或队友控线后变身"
      bp_use: "resource_timing_check"
    - id: "base_form_collapse_after_mecha_destroyed"
      active_when: "机甲被打掉后，本体 2400 HP 被追击"
      exposed_by: "stateful HP and no hard escape"
      mitigation: "Force Field、提前用 Toolbox 计划性弹射并选择安全回充路线、队友 peel、避免本体携带关键目标"
      bp_use: "avoid_as_sole_carrier_or_last_body"
    - id: "thrower_spawnable_or_close_swarm_tax"
      active_when: "敌方用 Nita、Larry & Lawrie、Damian、Lumi 或墙后投掷持续消耗机甲"
      exposed_by: "PLP counteredBy and no wall bypass"
      mitigation: "补开墙、清召唤物或反投掷"
      bp_use: "must_answer_before_picking_meg"
    - id: "open_sniper_kiting_before_mecha_online"
      active_when: "本体期无法安全充 Super 或走到目标区"
      exposed_by: "base form low HP and low damage"
      mitigation: "靠掩体、队友压线或选择中短线目标图"
      bp_use: "avoid_if_mecha_access_is_unreliable"
    - id: "slow_mecha_super_cycle"
      active_when: "BP 计划依赖 Mecha Super 反复 swing、Heavy Metal 回血或 Buffie 偷 ammo，但机甲普攻每枚命中只充 2.703% Super，下一次 swing 无法在目标战前稳定上线"
      exposed_by: "[[sources/Fandom-Meg|Fandom-Meg]] 当前 Mecha attack Super charge rate"
      mitigation: "把已充好的 swing 留给持球、站圈或贴脸关键窗口，用 Jolting Volts/队友控制维持其余时间，不把重复 swing 计入阵容基本面"
      bp_use: "resource_availability_and_repeat_control_check"

  conditional_matchups:
    - target: ["Nani", "Piper", "Byron", "Glowy"]
      direction: "subject_favored"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      mechanism: "机甲身体和宽弹幕能在目标区逼迫脆长手后退，使其难以只靠单发 poke 控目标"
      active_when: "Meg 已机甲上线且地图目标要求对方靠近中线/热区/球门"
      fails_when: "地图极开阔，Meg 在本体期就被压死，或长手能从安全 off-angle 持续风筝"
      bp_use: "mid_control_into_fragile_range"
    - target: ["Jae-Yong", "Squeak", "Sprout", "Bolt"]
      direction: "subject_favored"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      mechanism: "机甲能吃支援/控制型低爆发输出并持续推进，迫使对手交资源处理身体"
      active_when: "墙体不让投掷免费输出，且 Meg 有队友保护机甲路径"
      fails_when: "投掷口袋完整，或 Squeak/Sprout 等能从墙后反复消耗无代价"
      bp_use: "body_pressure_response"
    - target: ["Rosa", "Bibi", "Edgar"]
      direction: "target_favored"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      mechanism: "高近身爆发、草丛接近或贴脸连击能绕过 Meg 的中距离压制，并在机甲破后收本体"
      active_when: "草墙路线或球门/zone 入口让目标能贴到 Meg"
      fails_when: "Meg 已有充好的 swing/Heavy Metal 资源、队友控制和开阔视野提前消耗"
      bp_use: "requires_peel_and_grass_control"
    - target: ["Nita", "Larry & Lawrie", "Damian", "Lumi", "Sirius"]
      direction: "target_favored"
      source: "[[sources/PLP-Meg|PLP-Meg]]"
      mechanism: "召唤物、墙后控制或持续区域压力会税掉机甲血量和变身空间"
      active_when: "地图有墙后口袋或中心入口拥挤，Meg 必须先处理附加目标"
      fails_when: "队友能快速清召唤物/开墙，Meg 可直接站住目标区"
      bp_use: "do_not_pick_without_clear_plan"

  slot_notes:
    slot_1: "Hot Zone 或 Brawl Ball 中线/球门图可早手，但要准备回答投掷与召唤物，并且不能把低频 Mecha Super 当作每轮目标战的固定控制"
    slot_2_3: "适合建立目标区身体核心，让后续补开墙、清草、得分或 safe DPS"
    slot_4_5: "看到敌方缺反前排、缺墙后消耗时价值更稳；若阵容需要重复缴械/清圈，还要另补稳定控制"
    slot_6: "惩罚脆长手或低爆发支援阵容，但不能修补队伍缺开墙/缺清召唤物的问题"
```

## 关联页面

- [[sources/Fandom-Meg|Fandom 来源摘要: Meg]]
- [[sources/PLP-Meg|PLP 来源摘要: Meg]]

## 战斗断点输入

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "Meg",
    "target_states": [
      {
        "id": "meg",
        "entity_class": "brawler_body",
        "roster_target": true,
        "health": {"amount": 2400, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-Meg|Fandom-Meg]]"
      },
      {
        "id": "mecha",
        "entity_class": "brawler_alternate_form",
        "roster_target": false,
        "health": {"amount": 3700, "at_power_level": 1, "scaling": "standard"},
        "state_rule": "独立形态血池，不与 Meg 本体相加",
        "source_ref": "[[sources/Fandom-Meg|Fandom-Meg]]"
      }
    ],
    "damage_packets": [],
    "defense_modifiers": [
      {
        "id": "force_field_post_mecha",
        "source_kind": "star_power",
        "loadout_group": "star_power",
        "applies_to_states": ["meg"],
        "effect": {"type": "damage_reduction", "ratio": 0.40},
        "active_when": "Mecha 被摧毁后的 5 秒，且 Meg 尚未再次进入 Mecha",
        "sequence_validity": "只保护脱甲后的 Meg，不保护 Mecha",
        "source_ref": "[[sources/Fandom-Meg|Fandom-Meg]]"
      }
    ]
  }
}
```
