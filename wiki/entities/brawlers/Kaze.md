# Kaze

## 基本信息

- 稀有度：Ultra Legendary
- 定位：Assassin
- 类型：双形态刺客 / 风暴遮蔽 / 标记延迟爆发

## 来源摘要

- Fandom：[[sources/Fandom-Kaze|Fandom 来源摘要: Kaze]]
- PLP：[[sources/PLP-Kaze|PLP 来源摘要: Kaze]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Heist, Hot Zone, Bounty, Knockout

## 角色定位总结

Kaze 是双形态刺客：geisha 形态移速高、短 dash 接 2 格环形斩击，并可用 `Fan Storm` 给团队制造遮蔽、边缘伤害和 `Gratuity Included` 的初始弹药削减；ninja 形态移速较慢但有 6.67 格双刀和 9 格 Super 标记 dash，2.5 秒后引爆高伤害。她的 BP 价值来自“先用 geisha 走位/风暴压缩视野，再切 ninja 进场标记关键目标”。风险是她并不真的穿墙/过水，geisha dash 撞墙/水会提前斩击，ninja Super 也不能越墙/水；一旦被迫正面撞坦克或吃硬控，短手和延迟爆发会被惩罚。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "short_geisha_mid_ninja; geisha 斩击 2.67 格，ninja 双刀 6.67 格，ninja Super dash 9 格"
    projectile_reliability: "mode_dependent; geisha 依赖贴近和 Strike Spot，ninja 双刀远端伤害衰减，mark 爆发有 2.5 秒延迟"
    burst: "high_if_strike_spot_or_mark_converts; Strike Spot 双倍伤害，ninja mark 引爆高伤害"
    sustained_dps: "medium_high_when_form_cycle_managed; geisha 1 秒装填，ninja 1.9 秒装填"
    objective_damage: "conditional; Heist 依赖近身/双刀和进库路线，不是远程安全 race"
    mobility: "very_high_in_geisha_and_super; geisha 基础 very fast，攻击 dash；ninja Super 高速 9 格"
    survivability: "medium_with_gracious_host; 4100 HP，切回 geisha 可回复 30% 最大生命"
    engage: "high_with_speed_or_invisibility; Gracious Host speed、Hensojutsu invis、ninja Super 标记进场"
    disengage: "medium; geisha 高速和切形态回血能撤，但无硬免伤"
    anti_aggro: "medium; Fan Storm 遮蔽/弹药削减可打断进场，但贴脸坦克仍危险"
    anti_tank: "low_to_medium; 可 kite/mark，但正面撞高血短手风险高"
    wall_break: "none"
    throw_or_wall_bypass: "low; Super/Fan Storm 可越墙投放，Kaze 自身 dash 不能越墙/水"
    area_control: "medium_high; Fan Storm 5 秒遮蔽、边缘持续伤害、中心 ammo tax"
    scouting_or_vision: "medium; Storm 改写敌方视野，Hensojutsu 隐身接近"
    team_support: "medium; Fan Storm 让己方在风暴内隐蔽，Gratuity Included 削初始 ammo"
    spawnable_or_pet: "storm_area; geisha Super 生成 5 秒风暴区域"
    crowd_control: "medium; Advanced Techniques Strike Spot slow，Gratuity Included 初始 ammo removal"
    source_trace:
      - "[[sources/Fandom-Kaze|Fandom-Kaze]]"
      - "[[sources/PLP-Kaze|PLP-Kaze]]"

  build_switches:
    - build: "Gracious Host / Gratuity Included / Shield, Damage, Health"
      source: "[[sources/PLP-Kaze|PLP-Kaze]]"
      changes_capabilities:
        - "Gracious Host 切 ninja 给 30% 移速 2.5 秒，切 geisha 回复 30% 最大生命"
        - "Gratuity Included 让 Fan Storm 初始中心命中的敌人损失约三分之一 ammo，并把 ninja gadget 效果延长 50%"
        - "Health/Shield/Damage 支持短手切入、撤退回血和 mark 击杀确认"
      enables:
        - "全模式 flex assassin"
        - "Hot Zone/Brawl Ball 风暴遮蔽和 ammo tax"
        - "Gem/Bounty/Knockout 后排标记"
      mitigates_failure_modes:
        - "form_commitment_punished"
        - "delayed_mark_no_finish"
      best_when: "地图有草墙遮蔽、目标需要守点/持球/守宝，Kaze 能选择进场形态"
      poor_when: "敌方有多名近身 burst、硬控 body 或能无视风暴的范围伤害"
      bp_use: "default_plp_dual_aspect_assassin_build"
    - build: "Hensojutsu / Advanced Techniques variant"
      source: "[[sources/Fandom-Kaze|Fandom-Kaze]]"
      changes_capabilities:
        - "Hensojutsu 切 ninja 给短隐身，切 geisha 给 3.33 格 dash"
        - "Advanced Techniques 让 geisha Strike Spot 命中 slow 2.5 秒，ninja mark 击杀后溅射"
      enables:
        - "最后手绕视野刺杀"
        - "短手追击 slow"
        - "多目标收割"
      mitigates_failure_modes:
        - "target_kites_mark_window"
        - "approach_seen_too_early"
      best_when: "需要更强接近/收割而非团队风暴 ammo tax"
      poor_when: "队伍依赖 Gracious Host 的回血/移速容错"
      bp_use: "stealth_or_slow_last_pick_variant"

  map_feature_hooks:
    - id: "gem_carrier_ninja_mark_pick"
      map_feature_type: "carrier_assassin_mark_window"
      uses_feature_by: "geisha 形态高速靠近或 Fan Storm 遮蔽，切 ninja Super 穿过 carrier 标记并引爆"
      route_or_position: "宝石矿侧草、carrier 倒计时撤退线、中心墙边侧入口"
      objective_conversion: "逼 carrier 掉宝、打断倒计时或迫使保护者交控制"
      active_when: "carrier 路线可预测，Kaze 能从草墙/风暴侧翼进场"
      fails_if: "carrier 有 Bull/Bibi/Chester/Jacky 等近身保镖，或 mark 后 2.5 秒内被治疗/护盾救下"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.carrier_assassination_window"
    - id: "brawl_ball_storm_ammo_tax_and_dash_pick"
      map_feature_type: "ball_lane_concealment_and_disarm_pressure"
      uses_feature_by: "Fan Storm 遮蔽门前/中路，Gratuity Included 削初始 ammo，ninja dash 标记聚集防守者"
      route_or_position: "中路球权、侧草推进、球门前三格和 overtime 直线"
      objective_conversion: "削防守弹药、隐藏推进路线或标记守门人创造射门窗口"
      active_when: "敌方必须聚集守门或抢中路，Kaze 队友能跟进射门"
      fails_if: "敌方有击退/眩晕守门，或 Kaze dash 被墙/水提前截断"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_lane_assassin_window"
    - id: "hot_zone_fan_storm_entry_blind"
      map_feature_type: "zone_sight_denial_and_ammo_tax"
      uses_feature_by: "Fan Storm 让敌方在区内看不到外部英雄/投射物，中心命中初始削 ammo"
      route_or_position: "单区中心、区口草边、敌方回区 chokepoint"
      objective_conversion: "让敌方进区前失去视野/弹药，给己方 zone body 抢时间"
      active_when: "区口半径能覆盖多人，己方已有真正站区英雄"
      fails_if: "敌方用 thrower/范围伤害从风暴外清区，或没人利用风暴踩区"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "map_bp_factors.zone_sight_denial"
    - id: "knockout_bounty_storm_cover_mark_finish"
      map_feature_type: "late_round_cover_and_mark_pick"
      uses_feature_by: "Fan Storm 切断视野后切 ninja 标记低血长手，Hyper 可让低血目标即时吃 mark 伤害"
      route_or_position: "Knockout 缩圈路径、Bounty 长线侧草、墙边残局撤退线"
      objective_conversion: "把空间领先转成首杀/收尾，或用风暴保护队友穿线"
      active_when: "目标缺近身保镖，Kaze 有形态切换资源和后续撤退线"
      fails_if: "敌方保持分散，坦克守入口，或 mark 后 Kaze 无法离开爆发范围"
      example_maps:
        - "[[entities/maps/Out in the Open|Out in the Open]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
      bp_use: "slot_task.late_round_assassin_finish"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier 刺杀和倒计时追击"
        - "Fan Storm 保护撤退或遮蔽矿区"
      cannot_fulfill:
        - "长期安全主 carrier"
        - "正面远程控矿"
      needs_teammate_support:
        - "稳定 carrier、探草、反坦/硬控补伤害"
      false_positive: "Kaze 能制造掉宝窗口，但 mark 延迟和短手风险要求队友能接宝/收尾"
    - mode: "Brawl Ball"
      can_fulfill:
        - "门前 ammo tax"
        - "标记守门人和短时 scorer 威胁"
      cannot_fulfill:
        - "稳定破门"
        - "正面硬推双坦"
      needs_teammate_support:
        - "破墙/射门位、反击退、站线 body"
      false_positive: "Kaze 的风暴和 dash 是窗口工具，不等于无条件进球"
    - mode: "Hot Zone"
      can_fulfill:
        - "风暴遮蔽和初始削 ammo"
        - "侧翼收割进区者"
      cannot_fulfill:
        - "单人长期站区"
        - "从风暴外处理投掷火力"
      needs_teammate_support:
        - "站区前排、持续输出、反 thrower"
      false_positive: "Fan Storm 不是墙，敌方仍可用范围/投掷清区"
    - mode: "Bounty/Knockout/Heist"
      can_fulfill:
        - "风暴掩护穿线和残局收尾"
        - "Heist 近身 safe 窗口或逼回防"
      cannot_fulfill:
        - "稳定远程星差保护"
        - "无路线时主 safe DPS"
      needs_teammate_support:
        - "开路/长线火力、落点清控、目标 race 支援"
      false_positive: "Kaze 的 Heist/Bounty 价值依赖进场路线和保命，不是纯面板输出"

  failure_modes:
    - id: "dash_does_not_cross_walls_or_water"
      active_when: "BP 把 Kaze 当作地形穿越刺客"
      exposed_by: "[[sources/Fandom-Kaze|Fandom-Kaze]] notes geisha dash is cut short by walls/water and ninja Super cannot cross walls/water"
      mitigation: "只按草墙接近/风暴遮蔽建模，不把水或墙当可穿路线"
      bp_use: "map_route_hard_gate"
    - id: "mark_damage_delayed"
      active_when: "ninja Super 标记后敌方还有治疗、护盾、撤退或反杀窗口"
      exposed_by: "Fandom mark detonates after 2.5 seconds"
      mitigation: "选择低血/无保镖目标，或用 Hyper threshold/队友伤害提前确认"
      bp_use: "candidate_eval.finish_window"
    - id: "storm_ammo_tax_requires_initial_center_hit"
      active_when: "Fan Storm 只擦边或敌方后续走入风暴"
      exposed_by: "Gratuity Included only removes ammo from initially caught center targets"
      mitigation: "对进区/守门聚集点预判中心落点，不把边缘伤害当 ammo tax"
      bp_use: "area_control_precision_check"
    - id: "short_range_body_counter"
      active_when: "Kaze 必须正面接触高血短手或硬控"
      exposed_by: "short geisha range and PLP counteredBy body list"
      mitigation: "最后手选进无保镖后排；先用风暴/队友逼控制"
      bp_use: "avoid_front_to_front_body_fight"

  conditional_matchups:
    - target: ["Mr. P", "Jessie", "Sprout", "Ziggy", "Dynamike", "Grom"]
      direction: "subject_favored"
      source: "[[sources/PLP-Kaze|PLP-Kaze]]"
      mechanism: "风暴遮蔽、短隐身/移速切换和 ninja mark 能惩罚低机动召唤/投掷/墙后控制"
      active_when: "目标缺 bodyguard，墙草给 Kaze 接近，且 mark 后能完成击杀或逼退"
      fails_when: "召唤物拖住路线，投掷口有坦克保护，或 Kaze dash 被地形截断"
      bp_use: "last_pick_into_unprotected_control"
    - target: ["Piper", "Brock"]
      direction: "subject_favored"
      source: "[[sources/PLP-Kaze|PLP-Kaze]]"
      mechanism: "Fan Storm 切断视野并让 Kaze/队友穿线，ninja Super 可在长手被迫守目标时标记收尾"
      active_when: "长手没有近身 peel，Kaze 从侧草/风暴进入而非正面直走"
      fails_when: "地图完全开阔，长手有陷阱/击退队友，或 Kaze 无法在 mark 前离开火线"
      bp_use: "assassin_answer_to_isolated_marksman"
    - target: ["Chester", "Bull", "Sam", "Rosa", "Bibi"]
      direction: "target_favored"
      source: "[[sources/PLP-Kaze|PLP-Kaze]]"
      mechanism: "近身爆发、高血 body、击退或回复循环会吃掉 Kaze 的短手进场并反杀"
      active_when: "他们守球门、safe、热区或 Kaze 的 dash 终点"
      fails_when: "Kaze 只标记后排并用风暴隔离 body，或队友先压低坦克"
      bp_use: "avoid_as_frontline_answer"
    - target: ["Sandy", "Trunk", "Doug"]
      direction: "target_favored"
      source: "[[sources/PLP-Kaze|PLP-Kaze]]"
      mechanism: "团队隐蔽、路线 body、复活/高血续航会削弱 Kaze 标记和风暴窗口的确定性"
      active_when: "目标队伍能把 Kaze 进场变成前排换血或二次生命交换"
      fails_when: "Kaze 等复活/隐身资源结束后切后排，或己方有反坦 burst 跟进"
      bp_use: "requires_burst_followup_and_target_selection"

  slot_notes:
    slot_1: "PLP 标为多模式通用，但不宜盲早手；被近身 body/硬控后手惩罚明显"
    slot_2_3: "可围绕风暴遮蔽和刺杀窗口建队，后续必须补站区/破门/远程"
    slot_4_5: "看到后排缺保镖、投掷口暴露时价值高"
    slot_6: "最适合最后手惩罚无保镖长手或控制；遇到多坦多控应避选"
```

## 关联页面

- [[sources/Fandom-Kaze|Fandom 来源摘要: Kaze]]
- [[sources/PLP-Kaze|PLP 来源摘要: Kaze]]

## 战斗断点输入

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "Kaze",
    "target_states": [
      {
        "id": "geisha_aspect",
        "entity_class": "brawler_body",
        "roster_target": false,
        "health": {"amount": 4100, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-Kaze|Fandom-Kaze]]"
      },
      {
        "id": "ninja_aspect",
        "entity_class": "brawler_alternate_form",
        "roster_target": true,
        "health": {"amount": 4100, "at_power_level": 1, "scaling": "standard"},
        "state_rule": "形态切换不增加第二条可连续消耗的血池",
        "source_ref": "[[sources/Fandom-Kaze|Fandom-Kaze]]"
      }
    ],
    "damage_packets": [],
    "defense_modifiers": []
  }
}
```
