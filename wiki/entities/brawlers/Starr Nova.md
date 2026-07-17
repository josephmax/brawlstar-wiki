# Starr Nova

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：高速穿透骚扰 / Super 剑形态 / Floaty Time 路线工具

## 来源摘要

- Fandom：[[sources/Fandom-Starr-Nova|Fandom 来源摘要: Starr Nova]]
- PLP：[[sources/PLP-Starr-Nova|PLP 来源摘要: Starr Nova]]
- PLP 推荐模式：Gem Grab、Brawl Ball、Hot Zone、Heist

## 角色定位总结

Starr Nova 是速度极快、射击卸弹极快的 Assassin / harasser。普通形态用两段穿透 sparkles 持续骚扰和给队友治疗（PLP 默认 `Mystical Starr Technique`），Super 向前 dash 并进入 7 秒剑形态：移速提高 25%，近身 135 度剑弧瞬时命中，并按造成伤害的 30% 自疗。她不适合无脑冲进人群；Fandom 明确提示剑形态治疗不如 Edgar/Mortis/Kenji，通常更像扰乱和收割工具。`Floaty Time` 可放 3000 HP 晶体，4.33 格内队友可飞越障碍，但飞行期间不能攻击或用 Super/Gadget/Hypercharge，放在目标 choke 会坑队友。

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
    effective_range: "mid_piercing; 普通攻击 5.67 格，两段高速穿透 sparkles"
    projectile_reliability: "high_in_range; Fandom 称 projectile speed 极快，几乎难躲"
    burst: "medium_high_in_sword_form; 剑形态以 1100 基础伤害瞬时宽弧命中，Power Level 变体可叠伤害"
    sustained_dps: "medium; 1.4 秒 fast reload，但普通形态单发伤害中等"
    objective_damage: "situational_heist; PLP 标 Heist，但需要安全接近或扰乱防守"
    mobility: "very_high; 820 基础移速，Super dash，剑形态 +25% speed"
    survivability: "medium_with_sword_lifesteal; 4000 HP，剑形态 1100 基础伤害同时按命中伤害自疗 30%，提高单目标拉扯但不足以承受多人集火"
    engage: "high_if_route_protected; Super dash 或 Shining Starr teleport 可接近后排"
    disengage: "high_with_super_or_floaty; Super 可逃离，Floaty Time 可跨障碍撤退"
    anti_aggro: "medium; 高速 strafe 可绕刺客，但被 burst/outrange 会倒"
    anti_tank: "low_medium; 剑形态可扰乱但治疗不足以正面打坦克群"
    wall_break: "none"
    throw_or_wall_bypass: "mobility_route_only; Floaty Time 让队友飞越障碍但不能行动"
    area_control: "low_medium; 更多是移动扰乱，不是稳定区域封锁"
    scouting_or_vision: "medium_bush_check; 极速普通攻击可扫草"
    team_support: "medium_with_mystical; Mystical Starr Technique 让普通攻击命中队友按伤害 40% 治疗，并少量推进 Super 循环"
    spawnable_or_pet: "floaty_crystal; 3000 HP 晶体，最高 10 秒并逐秒衰减"
    crowd_control: "none_direct; 依赖路线压力和目标扰乱"
    source_trace:
      - "[[sources/Fandom-Starr-Nova|Fandom-Starr-Nova]]"
      - "[[sources/PLP-Starr-Nova|PLP-Starr-Nova]]"

  build_switches:
    - build: "Floaty Time / Mystical Starr Technique / Shield, Damage"
      source: "[[sources/PLP-Starr-Nova|PLP-Starr-Nova]]"
      changes_capabilities:
        - "Floaty Time 放置 4.33 格飞行区，让 Starr Nova 和队友越过障碍，但飞行时不能攻击/用技能"
        - "Mystical Starr Technique 让普通攻击治疗队友 40% 伤害，并少量充 Super；它不作用于剑形态攻击"
        - "Shield/Damage gear 提高 mid-range harass 和剑形态容错"
      enables:
        - "Gem carrier 逃生/支援治疗"
        - "Brawl Ball 越墙路线或假冲锋骗弹药"
        - "Hot Zone / Heist 侧翼扰乱"
      mitigates_failure_modes:
        - "short_range_outburst"
        - "ally_route_needs_escape"
      best_when: "地图有可利用墙/水/障碍撤退点，且 Floaty 不会放在队友必须攻击的目标点"
      poor_when: "敌方可立即打掉晶体或用硬控取消 Super dash"
      bp_use: "default_plp_route_and_harass_build"
    - build: "Shining Starr / Power Level: Maximum! variant"
      source: "[[sources/Fandom-Starr-Nova|Fandom-Starr-Nova]]"
      changes_capabilities:
        - "Shining Starr projectile 可伤敌/治疗队友，并在命中前二次使用瞬移到 projectile"
        - "Power Level: Maximum! 让剑形态命中目标后每次 +5% 剑伤害，最高 +30%"
      enables:
        - "背后奇袭/重定位"
        - "剑形态多目标收割"
      mitigates_failure_modes:
        - "floaty_crystal_destroyed"
        - "lack_of_sword_burst"
      best_when: "敌方后排保护薄且队伍需要更强收割，而不是团队越障/治疗"
      poor_when: "敌方有硬控/坦克守点，传送终点会被直接爆发"
      bp_use: "ambush_or_damage_variant"

  map_feature_hooks:
    - id: "gem_floaty_escape_and_carrier_support"
      map_feature_type: "carrier_route_escape_and_heal"
      uses_feature_by: "Floaty Time 提供越障撤退区，普通攻击可给队友治疗"
      route_or_position: "carrier 倒计时退线、宝石矿侧墙、己方半区安全墙后"
      objective_conversion: "让 carrier 脱离追击或让队友跨墙撤退，同时用高速 poke 干扰追击"
      active_when: "晶体放在目标旁侧安全点，而不是矿区正中 choke"
      fails_if: "晶体被秒清、飞行期间队友不能攻击导致目标失守"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "candidate_eval.carrier_route_escape_support"
    - id: "brawl_ball_super_dash_and_floaty_lane"
      map_feature_type: "ball_route_mobility_pressure"
      uses_feature_by: "Super dash、剑形态 speed 和 Floaty 越障可制造侧路压力或假冲锋骗弹药"
      route_or_position: "中场球权、侧墙通道、门前侧翼或回防路线"
      objective_conversion: "逼 defender 转身、抢球后撤、或让 scorer 获得越墙路线"
      active_when: "队友能在 Floaty 外恢复攻击并转成射门，Starr Nova 不需要一人打穿三人"
      fails_if: "Floaty 放在门前让队友无法攻击，或 Super dash 被控制取消"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_route_harass_and_escape"
    - id: "hot_zone_sword_form_side_harass"
      map_feature_type: "zone_side_harass_not_primary_body"
      uses_feature_by: "高速普通形态和剑形态扰乱侧翼，逼低血控制位离开区边"
      route_or_position: "Hot Zone 侧墙、草边、敌方回区侧线"
      objective_conversion: "让敌方后排/支援无法自由站区，给真正站区 body 创造空间"
      active_when: "Starr Nova 从侧翼进入且有队友站区/补伤害"
      fails_if: "她被要求单人站区，或冲入人群治疗不足"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "candidate_eval.zone_side_harass"
    - id: "heist_backline_distraction_route"
      map_feature_type: "safe_lane_distraction_and_endpoint_access"
      uses_feature_by: "Super dash / Shining Starr teleport / Floaty route 可绕过部分防守线，普通攻击持续骚扰"
      route_or_position: "safe 侧墙、lane win 后防守背线、敌方 safe 旁撤退点"
      objective_conversion: "吸引防守弹药、打开队友 safe race，或在残局打 safe chip"
      active_when: "路线终点可撤退，敌方缺硬控守入口"
      fails_if: "终点被坦克/控制守住，或 Starr Nova 被要求正面打 safe race"
      example_maps:
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
      bp_use: "candidate_eval.heist_distraction_route"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier 逃生路线辅助"
        - "高速穿透 poke / 治疗队友"
        - "后排骚扰"
      cannot_fulfill:
        - "安全主 carrier"
        - "正面站矿 body"
      needs_teammate_support:
        - "主 carrier、前排/控区、硬控"
      false_positive: "Floaty 能逃生但飞行时不能攻击，不能放在队友需要开火的矿区核心"
    - mode: "Brawl Ball"
      can_fulfill:
        - "侧路路线压力"
        - "假冲锋骗弹药"
        - "剑形态扰乱守门"
      cannot_fulfill:
        - "稳定破门"
        - "一人硬冲整队"
      needs_teammate_support:
        - "scorer、破墙/控制、守门"
      false_positive: "她是路线扰乱，不是无条件 scorer"
    - mode: "Hot Zone"
      can_fulfill:
        - "侧翼骚扰"
        - "低血控制位压迫"
      cannot_fulfill:
        - "主站区 body"
        - "抗住坦克群"
      needs_teammate_support:
        - "站区者、长线补伤、硬控"
      false_positive: "剑形态治疗不够支撑冲人群；必须有队友转换空间"
    - mode: "Heist"
      can_fulfill:
        - "侧路扰乱防守"
        - "endpoint access / safe chip"
      cannot_fulfill:
        - "稳定主 safe DPS"
        - "正面打穿坦克防线"
      needs_teammate_support:
        - "race DPS、开路、 endpoint peel"
      false_positive: "PLP Heist 适配需要地图路线，不等于直接打库强"

  failure_modes:
    - id: "super_dash_cancelled"
      active_when: "Starr Nova 在 Super dash 中被 stun、knockback 或 pull"
      exposed_by: "[[sources/Fandom-Starr-Nova|Fandom-Starr-Nova]] Super cancellation note"
      mitigation: "等控制交掉或从侧翼使用，不把 dash 当无敌进场"
      bp_use: "engage_sequence_check"
    - id: "sword_form_not_crowd_dive"
      active_when: "计划让 Starr Nova 冲入多名敌人中心靠吸血硬打"
      exposed_by: "Fandom tips warn healing is weaker than Edgar/Mortis/Kenji and crowd dives fail"
      mitigation: "4000 HP 与 1100 基础剑伤提高单目标续航，但不改变多人集火门槛；仍用她骚扰、收割或扰乱后排，由队友提供 burst/控制"
      bp_use: "anti_tank_and_crowd_false_positive"
    - id: "floaty_disables_ally_actions"
      active_when: "Floaty Time 放在重要目标点或 choke，队友飞行时不能攻击/用技能"
      exposed_by: "Fandom Floaty Time mechanics and tips"
      mitigation: "把晶体放在旁侧撤退/跨墙点，避免覆盖队伍必须开火的位置"
      bp_use: "map_hook_sabotage_filter"
    - id: "outranged_or_burst_down"
      active_when: "敌方长手/高爆发在她 5.67 格外处理 Starr Nova"
      exposed_by: "Fandom tips advise outranging or bursting her down"
      mitigation: "用墙/侧翼/Floaty route 接近，并避免正面开阔线"
      bp_use: "range_and_burst_warning"

  conditional_matchups:
    - target: ["Jae-Yong", "Poco", "Ziggy"]
      direction: "subject_favored"
      source: "[[sources/PLP-Starr-Nova|PLP-Starr-Nova]]"
      mechanism: "高速穿透 poke、队友治疗和侧翼扰乱惩罚低爆发支援/控制位"
      active_when: "Starr Nova 能保持 5.67 格内外拉扯，目标缺硬控 bodyguard"
      fails_when: "目标有坦克保护或开阔长线先把 Starr Nova 打退"
      bp_use: "harass_response_into_low_burst_support"
    - target: ["Sprout", "Squeak", "Piper", "Tick", "Dynamike"]
      direction: "subject_favored"
      source: "[[sources/PLP-Starr-Nova|PLP-Starr-Nova]]"
      mechanism: "Super dash、Floaty/teleport 路线和高移速可压迫脆弱墙控/长线后排"
      active_when: "地图有侧路或墙边 route，后排没有近身保镖"
      fails_when: "thrower pocket 有坦克守点或控制能取消 dash"
      bp_use: "last_pick_backline_harass"
    - target: ["Damian", "Trunk", "Nita", "Ash"]
      direction: "target_favored"
      source: "[[sources/PLP-Starr-Nova|PLP-Starr-Nova]]"
      mechanism: "墙控/高血量/body 或 summon 能吸收骚扰并惩罚她短射程"
      active_when: "他们守住路线终点或能在 Starr Nova 进场时提供 body block"
      fails_when: "Starr Nova 只打侧翼低血目标并由队友先清 body"
      bp_use: "avoid_into_body_or_wall_control"
    - target: ["Crow", "Sandy", "Bibi", "Rosa"]
      direction: "target_favored"
      source: "[[sources/PLP-Starr-Nova|PLP-Starr-Nova]]"
      mechanism: "poison/reveal、隐蔽、速度和高血量近身会破坏 Starr Nova 的安全骚扰节奏"
      active_when: "他们控制草口或能让她剑形态被包夹"
      fails_when: "Floaty/side route 让她安全撤退且队友补足伤害"
      bp_use: "requires_escape_route_and_team_damage"

  slot_notes:
    slot_1: "不宜无脑早手；需要地图有可利用的侧路/障碍和队伍能转换她制造的混乱"
    slot_2_3: "可作为机动骚扰和路线工具，后续补主输出/站区/守门"
    slot_4_5: "看到无保护后排或低爆发支援时响应价值高"
    slot_6: "最后手可惩罚缺硬控的后排阵容，但不能补主坦/主控区"
```

## 关联页面

- [[sources/Fandom-Starr-Nova|Fandom 来源摘要: Starr Nova]]
- [[sources/PLP-Starr-Nova|PLP 来源摘要: Starr Nova]]

## 战斗断点输入

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "Starr Nova",
    "target_states": [
      {
        "id": "body",
        "entity_class": "brawler_body",
        "roster_target": true,
        "health": {"amount": 4000, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-Starr-Nova|Fandom-Starr-Nova]]"
      }
    ],
    "damage_packets": [
      {
        "id": "main.one_projectile",
        "ability_kind": "main_attack",
        "packet_unit": "projectile_impact",
        "delivery_variant": "impact",
        "repeat_model": "identical",
        "damage": {"amount": 480, "at_power_level": 1, "scaling": "standard"},
        "active_when": "普通形态的一枚 projectile 命中；一个 ammo 有两枚，未假设同时命中",
        "source_conflict_status": "none",
        "source_ref": "[[sources/Fandom-Starr-Nova|Fandom-Starr-Nova]]"
      },
      {
        "id": "super_form.sword_impact",
        "ability_kind": "transformed_main_attack",
        "packet_unit": "impact",
        "delivery_variant": "impact",
        "repeat_model": "resource_gated",
        "damage": {"amount": 1100, "at_power_level": 1, "scaling": "standard"},
        "active_when": "7 秒 Super 剑形态内攻击命中",
        "source_conflict_status": "none",
        "source_ref": "[[sources/Fandom-Starr-Nova|Fandom-Starr-Nova]]"
      }
    ],
    "defense_modifiers": []
  }
}
```
