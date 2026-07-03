# Shelly

## 基本信息

- 稀有度：Starting Brawler
- 定位：Damage Dealer
- 类型：近身霰弹 / 反坦击退 / Brawl Ball 破门

## 来源摘要

- Fandom：[[sources/Fandom-Shelly|Fandom 来源摘要: Shelly]]
- PLP：[[sources/PLP-Shelly|PLP 来源摘要: Shelly]]
- PLP 推荐模式：Gem Grab、Brawl Ball、Hot Zone

## 角色定位总结

Shelly 是以近身霰弹和 `Super Shell` 反突进为核心的 Damage Dealer。普攻射出 5 枚弹丸，标称射程较长，但有效伤害高度依赖近距离多弹命中；Super 射出更大散射、穿透敌人、击退并破坏障碍，近身可造成高伤。PLP 默认 `Fast Forward / Band-Aid / Shield, Damage, Speed, Gadget Cooldown`，让她靠草口、墙边和 Super 反制坦克/刺客，在 Brawl Ball 中破门或击退守门人。误用点是把她当稳定长手：开阔长线、投掷/持续 poke、召唤物和多角度控制都会让 Shelly 难以靠近。

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
    effective_range: "short_to_mid; 标称 7.67 格，但高伤需要多弹近身命中"
    projectile_reliability: "high_close_low_range; 近身霰弹稳定，远距单弹伤害低"
    burst: "very_high_close_range; 普攻 + Super 近距离可瞬间压低坦克/刺客"
    sustained_dps: "medium; 1.5 秒 reload，Fast Forward 可瞬间回满弹药"
    objective_damage: "medium_close_range; 可打 safe/目标但需要贴近，不是远程 race"
    mobility: "medium_with_fast_forward; 3.33 格 dash 并回满弹，不能穿墙/水"
    survivability: "medium_with_band_aid; 3900 HP，Band-Aid 充满后低于 40% 回 30% 生命"
    engage: "medium; 草丛/墙边/Fast Forward 进场"
    disengage: "high_with_super; Super 击退、破墙，Shell Shock 变体 slow"
    anti_aggro: "very_high_if_super_ready; Super 击退/打断并可取消多个敌方 Super wind-up"
    anti_tank: "very_high_close_range; 坦克进入近身半径会吃多弹和击退"
    wall_break: "high_super; Super Shell 破坏障碍，但弹丸破墙后消失"
    throw_or_wall_bypass: "none"
    area_control: "medium_bush_control; 扫草、破墙和击退控制草口"
    scouting_or_vision: "medium_bush_sweep; 宽散射可扫草但不持续显形"
    team_support: "medium; 击退/破门/破墙为队友创造进攻窗口"
    spawnable_or_pet: "none"
    crowd_control: "knockback_and_slow_variant; Super 击退，Shell Shock 让命中目标 slow 2 秒"
    source_trace:
      - "[[sources/Fandom-Shelly|Fandom-Shelly]]"
      - "[[sources/PLP-Shelly|PLP-Shelly]]"

  build_switches:
    - build: "Fast Forward / Band-Aid / Shield, Damage, Speed, Gadget Cooldown"
      source: "[[sources/PLP-Shelly|PLP-Shelly]]"
      changes_capabilities:
        - "Fast Forward 朝目标方向 dash 3.33 格并瞬间回满弹药，不能穿墙/水且会被 stun/pull/knockback 取消"
        - "Band-Aid 15 秒充满后，Shelly 低于 40% 血时回复 30% 最大生命"
        - "Speed gear 与草图结合，支持草口进场和反突进"
      enables:
        - "Brawl Ball 破门/反 scorer"
        - "Hot Zone / Gem Grab 草口反坦"
        - "近身 burst race"
      mitigates_failure_modes:
        - "needs_super_before_tank_contact"
        - "low_damage_at_range"
      best_when: "地图有草或墙让 Shelly 选择第一接触，且敌方有坦克/刺客/持球路线"
      poor_when: "地图开阔、敌方有持续 poke/投掷/多角度控制，Shelly 无法安全接近"
      bp_use: "default_plp_anti_tank_bush_build"
    - build: "Clay Pigeons / Shell Shock variant"
      source: "[[sources/Fandom-Shelly|Fandom-Shelly]]"
      changes_capabilities:
        - "Clay Pigeons 让接下来 3 次攻击射程 10 格、散射减半且弹速更快"
        - "Shell Shock 让 Super 命中目标 slow 2 秒，便于接 Clay Pigeons 或队友追击"
      enables:
        - "中距离收割被击退目标"
        - "对逃跑长手的追击"
        - "Super 后循环再充能"
      mitigates_failure_modes:
        - "target_escapes_after_knockback"
        - "shelly_cannot_reach_open_lane"
      best_when: "敌方会在中距离 kite Shelly，队伍需要 Super 后的远距补枪"
      poor_when: "Shelly 更需要 Fast Forward 位移或 Band-Aid 生存来通过草口"
      bp_use: "range_finish_or_slow_variant"

  map_feature_hooks:
    - id: "brawl_ball_super_goal_wallbreak_and_peel"
      map_feature_type: "goal_wall_break_and_carrier_disarm"
      uses_feature_by: "Super 破门前墙、击退守门人/持球者，并可在射门时清出路径"
      route_or_position: "球门前墙、门口三格、 midfield ball、侧草进攻线"
      objective_conversion: "永久打开门、逼掉守门人、或让持球者掉球后反击"
      active_when: "Shelly 有 Super 或能靠草口充 Super，队伍有 scorer 跟上"
      fails_if: "破墙后长线利于敌方，或 Shelly Super 弹丸被墙吃掉导致伤害不足"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
      bp_use: "slot_task.ball_wallbreak_and_disarm"
    - id: "bush_choke_close_range_tank_gate"
      map_feature_type: "bush_choke_anti_tank"
      uses_feature_by: "草口隐藏第一接触，近身霰弹和 Super 惩罚坦克/刺客进线"
      route_or_position: "Center Stage 中草、Sneaky Fields 侧草、Gem Grab 侧草入口"
      objective_conversion: "守住草区入口、阻止坦克推进、保护 carrier 或球权"
      active_when: "敌方必须进入草口或短线目标，Shelly 有 Super/Speed gear"
      fails_if: "草被清掉、敌方远程/投掷从外部压制，或 Shelly 无 Super 被先手 burst"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "map_bp_factors.bush_anti_tank_gate"
    - id: "hot_zone_super_knockback_body_clear"
      map_feature_type: "zone_body_knockback_clear"
      uses_feature_by: "Super 击退站区坦克并破坏周边掩体，Band-Aid 支持短时间站区"
      route_or_position: "单热区入口、区内短手接触点、墙边草口"
      objective_conversion: "把站区 body 打出区外或打断进区 Super，转换成区时"
      active_when: "敌方站区方式依赖短手身体或可被击退路线"
      fails_if: "敌方投掷/长手从区外清 Shelly，或 Shelly 破墙后失去接近路径"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "candidate_eval.zone_anti_tank_knockback"
    - id: "gem_carrier_anti_aggro_peel"
      map_feature_type: "carrier_peel_and_bush_sweep"
      uses_feature_by: "Super 击退追击者，宽散射扫草，Fast Forward 可重装弹药反打"
      route_or_position: "carrier 倒计时退线、宝石矿侧草、己方半区入口"
      objective_conversion: "保护 carrier、打断突进、或用 Super 反杀追击者"
      active_when: "敌方赢法是短手/刺客追 carrier，Shelly 有 Super 或草口伏击"
      fails_if: "敌方用长手 chip/投掷先压低 Shelly，或从多角度夹击"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "candidate_eval.carrier_anti_aggro_peel"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "Super 破门"
        - "击退持球者/守门人"
        - "草口反坦和 close-range scorer escort"
      cannot_fulfill:
        - "稳定远程控球"
        - "无 Super 时硬解多控制防守"
      needs_teammate_support:
        - "scorer、控球、破墙后长线压制"
      false_positive: "Shelly 破门很强，但破墙后也可能让敌方长手更舒服"
    - mode: "Hot Zone"
      can_fulfill:
        - "击退站区短手"
        - "草口 anti-tank gate"
        - "Band-Aid 短时站区"
      cannot_fulfill:
        - "长时间单人站区"
        - "清投掷 pocket"
      needs_teammate_support:
        - "区外长手、投掷处理、视野/草控制"
      false_positive: "Shelly 能清 body，不等于能长期控区"
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier 反突进保护"
        - "扫草和侧草威慑"
        - "Super 打断追击"
      cannot_fulfill:
        - "安全主 carrier"
        - "开阔中线 poke"
      needs_teammate_support:
        - "主 carrier、长手控矿、投掷处理"
      false_positive: "Gem 图如果没有草/短线，Shelly 的有效射程会暴露"

  failure_modes:
    - id: "low_damage_at_range"
      active_when: "Shelly 在开阔长线只命中少量弹丸"
      exposed_by: "[[sources/Fandom-Shelly|Fandom-Shelly]] Buckshot spread and close-range damage dependency"
      mitigation: "只在草/墙/短路可接近时选，或用 Clay Pigeons 变体处理中距离"
      bp_use: "effective_range_false_positive_filter"
    - id: "needs_super_before_tank_contact"
      active_when: "Bull、El Primo、Rosa 等高 burst/高血量目标先贴脸，Shelly Super 未充好"
      exposed_by: "Fandom warns Shelly should have Super charged before facing tanks"
      mitigation: "前期用安全距离充 Super，或让队友控线/减速后再接触"
      bp_use: "anti_tank_resource_gate"
    - id: "wallbreak_backfires"
      active_when: "Shelly Super 破坏过多墙/草，让敌方长手获得开阔射线"
      exposed_by: "Fandom strategy note to be mindful that destroying too many walls/bushes can disadvantage her"
      mitigation: "定义要破的门墙/关键墙，避免无目标开图"
      bp_use: "terrain_transform_check"
    - id: "fast_forward_route_blocked_or_cancelled"
      active_when: "Fast Forward 被 stun/pull/knockback 取消，或撞墙/水中断"
      exposed_by: "Fandom Fast Forward mechanics"
      mitigation: "只用在已确认路线和控制已交的时机，不把它当跨地形工具"
      bp_use: "mobility_route_gate"
    - id: "band_aid_overkill_failure"
      active_when: "Shelly 被单帧高伤直接击杀，Band-Aid 无法触发"
      exposed_by: "Fandom Band-Aid notes high-damage defeat can prevent activation"
      mitigation: "避免把 Band-Aid 当作硬复活，仍需控制距离和队友保护"
      bp_use: "survivability_false_positive_filter"

  conditional_matchups:
    - target: ["Jacky", "Rosa", "Frank", "El Primo"]
      direction: "subject_favored"
      source: "[[sources/PLP-Shelly|PLP-Shelly]]"
      mechanism: "近身多弹、Super 击退/打断和 Shell Shock 变体 slow 惩罚必须靠身体进场的坦克"
      active_when: "Shelly 有 Super 或草口伏击，目标必须走进近身半径"
      fails_when: "Shelly Super 未充好、被控制打断，或目标有队友远程先压低 Shelly"
      bp_use: "anti_tank_response_pick"
    - target: ["Edgar", "Bibi", "Sam", "Mortis"]
      direction: "subject_favored"
      source: "[[sources/PLP-Shelly|PLP-Shelly]]"
      mechanism: "突进/近战目标进入霰弹半径后会被击退、爆发和 Fast Forward reload 反打"
      active_when: "入口可预判，Shelly 保留 Super/弹药，队友能补伤"
      fails_when: "刺客从多角度 bait Super，或 Sam/Bibi 先打掉 Band-Aid 再二次进场"
      bp_use: "anti_assassin_if_resource_ready"
    - target: ["Stu", "Crow", "Surge", "Spike"]
      direction: "target_favored"
      source: "[[sources/PLP-Shelly|PLP-Shelly]]"
      mechanism: "机动、毒伤、阶段控制和远距 burst 能在 Shelly 靠近前消耗她或打断进场"
      active_when: "地图开阔或草被清，Shelly 只能远距少弹命中"
      fails_when: "Shelly 从草口拿到第一接触，或 Clay Pigeons/Shell Shock 先命中"
      bp_use: "avoid_open_lane_or_no_super"
    - target: ["Lola", "Gale", "Tara", "Nita"]
      direction: "target_favored"
      source: "[[sources/PLP-Shelly|PLP-Shelly]]"
      mechanism: "分身/击退/拉人/熊体和中距控制会消耗 Shelly 进场资源，并让 Super 不一定命中真目标"
      active_when: "他们有墙/召唤物/bodyguard 或控制可覆盖 Shelly 的草口"
      fails_when: "Shelly 保持 Super 等真身/核心 body 进入近身，队友先清召唤物"
      bp_use: "requires_body_clear_or_control_bait"

  slot_notes:
    slot_1: "只有明确草口/短线/反坦任务时可早手；开阔图早拿会被长手后手惩罚"
    slot_2_3: "适合作为 Brawl Ball 破门和反坦计划的一环，后续补远程控图"
    slot_4_5: "看到敌方坦克/刺客/持球短手后，Shelly 是强响应，但要确认 Super 资源路径"
    slot_6: "最后手可硬惩罚无长手保护的短手阵容，或解决明确门墙；不能补稳定 poke"
```

## 关联页面

- [[sources/Fandom-Shelly|Fandom 来源摘要: Shelly]]
- [[sources/PLP-Shelly|PLP 来源摘要: Shelly]]
