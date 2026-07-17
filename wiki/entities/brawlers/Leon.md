# Leon

## 基本信息

- 稀有度：Legendary
- 定位：Assassin
- 类型：隐身信息差 / 单点爆发 / 机动收割

## 来源摘要

- Fandom：[[sources/Fandom-Leon|Fandom 来源摘要: Leon]]
- PLP：[[sources/PLP-Leon|PLP 来源摘要: Leon]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Hot Zone, Bounty, Knockout

## 角色定位总结

Leon 的 BP 价值不是“射程很长”，而是用远距离蹭 Super 后通过隐身制造低信息进场、撤退或偷目标窗口。他擅长单抓、偷球、追击高价值目标和把敌方后排逼出安全站位；但他装填偏慢、非穿透、一次通常只处理一个目标，怕范围探草、召唤物、控制、近身爆发和能够让隐身价值下降的阵容。

## 与其他英雄的区别

- 不同于 `Crow`：Leon 的核心是隐身接近后的单点爆发，不是持续毒压制。
- 不同于 `Sandy`：Leon 的隐身主要服务自己或 Lollipop Drop 小范围团队隐蔽，不是大范围团战工具。
- 不同于 `Edgar`：Leon 没有直接跳到目标身上的按钮，必须先用信息差和路线靠近。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-17"
    plp: "[[sources/PLP-Leon|PLP-Leon]] direct_raw_capture_2026-06-30"
    user_notes: "本地 BP 规则要求隐身价值绑定视野、路线、目标和敌方探测/控制条件"

  capability_vector:
    effective_range: "mixed; 9.67 格可蹭血充能，但主要伤害随距离衰减，近身爆发才是核心"
    projectile_reliability: "中等；扇形飞刀可扫草/蹭血，但远端伤害低且非穿透"
    burst: "高；近距离四刀全中伤害高，适合隐身后单点击杀"
    sustained_dps: "中低；装填 1.9 秒，连续多目标处理能力弱"
    objective_damage: "条件性；Heist 可隐身绕后偷库，但稳定性取决于路线和防守"
    mobility: "Very Fast；Smoke Trails 提高隐身期间移速，Hypercharge 可攻击不破隐"
    survivability: "中等偏条件；Invisiheal 可用 Super 恢复；Lollipop Drop 只有 2000 HP 且每秒衰减 200，隐蔽空间是短时、可清除资源"
    engage: "强但需要 Super/草/障碍铺垫；不是无条件强开"
    disengage: "强；Super 可撤退、绕路和带高星/宝石保命"
    anti_aggro: "中等；近身爆发能反杀部分脆皮刺客，但怕控制和更硬近战"
    anti_tank: "弱到中；缺持续反坦，打高血量目标容易弹药不足"
    wall_break: "无"
    throw_or_wall_bypass: "无真正越墙；靠隐身绕路而不是穿墙"
    area_control: "低；Lollipop Drop 是隐蔽锚点，不是大范围封区"
    scouting_or_vision: "中等；飞刀散布和 clone 可探草/骗弹，但没有真实 reveal"
    team_support: "条件性；Lollipop Drop 让队友在范围内隐形，但低耐久与持续衰减使其不能长期守点"
    spawnable_or_pet: "Clone Projector 产生可骗弹/探路的 clone"
    crowd_control: "无硬控"
    terrain_creation: "Lollipop Drop 创建 4.33 格隐身区域锚点；2000 HP、每秒衰减 200，可被迅速清除"
    terrain_destruction: "无"

  build_switches:
    - build: "Lollipop Drop / Smoke Trails / Shield + Damage"
      source: "[[sources/PLP-Leon|PLP-Leon]] + [[sources/Fandom-Leon|Fandom-Leon]]"
      changes_capabilities:
        - "Lollipop Drop 给我方 4.33 格小范围隐身锚点，可保护长线、偷球或制造侧路不确定性；当前 2000 HP 且每秒衰减 200，不能当作持久掩体"
        - "Smoke Trails 提高隐身接近和抢球速度，适合 Brawl Ball / Bounty / Knockout"
        - "Shield/Damage 提高第一次接触容错和斩杀线"
      enables:
        - "Brawl Ball 偷球和快速进球"
        - "Bounty/Knockout 单抓和保星撤退"
        - "Gem Grab gem carrier 逃生或倒计时追击"
      mitigates_failure_modes:
        - "partially_mitigates_approach_distance"
        - "partially_mitigates_low_survivability_on_first_contact"
      best_when: "敌方缺持续探草/召唤物/范围控制，且地图有草墙路线或长线能让 Leon 安全蹭 Super"
      poor_when: "敌方有 Tara/Nita/Bull/Gale/Chester/Bolt/Damian/Trunk 等反隐身、召唤物、近身爆发或控制"
      bp_use: "隐身路线核心、slot_6 惩罚后排、Brawl Ball scorer / Gem Grab chase"
    - build: "Clone Projector / Invisiheal"
      source: "[[sources/Fandom-Leon|Fandom-Leon]]"
      changes_capabilities:
        - "Clone Projector 可骗弹、探草、干扰追击"
        - "Invisiheal 把 Super 转成撤退和续航工具，适合高价值持宝石/高星场景"
      enables:
        - "保命撤退"
        - "Bounty/Gem Grab 高资源携带"
      mitigates_failure_modes:
        - "partially_mitigates_focus_fire_after_engage"
      best_when: "我方需要 Leon 保星/保宝石或敌方会预扫草但缺硬 reveal"
      poor_when: "敌方能持续命中或用范围技能打出隐身轨迹"
      bp_use: "defensive branch；用于解释为什么同一英雄在不同 slot 可承担不同任务"

  map_feature_hooks:
    - id: "bush_and_lollipop_information_gap"
      map_feature_type: "vision_tax"
      example_maps:
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
      route_or_position: "草丛边缘或 Lollipop Drop 范围内隐藏真实站位，迫使敌方消耗弹药探点"
      objective_conversion: "Gem Grab 压缩 gem carrier 撤退半径；Brawl Ball/Ring of Fire 制造抢球或进圈伏击"
      active_when: "敌方缺稳定探草、召唤物或范围扫点，Leon 能先用远端蹭出 Super，且 Lollipop 的短寿命足够覆盖本次目标窗口"
      fails_if: "草被烧/扫掉，敌方有 Tara/Nita/Penny/Sandy 类持续探点，或能迅速清掉 2000 HP、持续衰减的 Lollipop"
      bp_use: "vision_tax / flank_pressure；必须和地图草线绑定"
    - id: "brawl_ball_stealth_score"
      map_feature_type: "scoring_window"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
      route_or_position: "隐身绕到球门前、侧草抢球、或 Smoke Trails 快速穿过空档"
      objective_conversion: "把敌方防守信息差转成偷球、传球接应或直接射门窗口"
      active_when: "敌方防线缺反隐身/击退，球门墙体状态不阻断射门或队友已提供破门/控人"
      fails_if: "持球会暴露 Leon，敌方守门控制完整，或墙体使隐身到位也无法射门"
      bp_use: "Brawl Ball scorer pressure；不等同于纯击杀优势"
    - id: "bounty_knockout_single_pick"
      map_feature_type: "low_commitment_pickoff"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"
      route_or_position: "远端飞刀蹭 Super 后隐身接近孤立远程或低血量目标"
      objective_conversion: "Bounty 拿星后撤；Knockout 删除一个无保护目标"
      active_when: "敌方三远程无 peel、缺召唤物探路，且 Leon 有撤退路线"
      fails_if: "地图极开阔导致接近路径被预判，或敌方有近身爆发/控制守目标"
      bp_use: "高风险后手；不作为开阔图早手基本面"
    - id: "heist_backline_safe_sneak"
      map_feature_type: "objective_backstab"
      example_maps:
        - "[[entities/maps/Safe Zone|Safe Zone]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
      route_or_position: "隐身绕过防线进入敌方金库侧或迫使多人回防"
      objective_conversion: "给金库制造短窗口伤害或牵制防守，配合队友 safe DPS"
      active_when: "敌方缺基地清理/召唤物探路，且 Leon 能接近 safe 后安全输出数轮"
      fails_if: "敌方防守站位能覆盖入口，或 Leon 需要独自承担主要拆库"
      bp_use: "Heist 条件机会；通常不是一抢理由"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "倒计时追击 gem carrier"
        - "高宝石撤退与 Invisiheal 保命"
        - "侧草信息差压缩敌方中路"
      cannot_fulfill:
        - "长期稳定 mid carrier"
        - "无探草支援时独立清所有草"
      needs_teammate_support:
        - "中路稳定火力和探草"
        - "能在 Leon 单抓后接管宝石矿"
      false_positive: "隐身不能替代视野；如果敌方持续扫草，Leon 追击价值下降"
    - mode: "Brawl Ball"
      can_fulfill:
        - "偷球、隐身接应、快速得分"
        - "用 Lollipop Drop 制造侧路站位不确定性"
      cannot_fulfill:
        - "稳定破门"
        - "被控时正面硬带球"
      needs_teammate_support:
        - "破门/控人/击退之一"
        - "中路清球和防反打"
      false_positive: "持球会暴露；必须先有球权窗口或队友控人"
    - mode: "Bounty"
      can_fulfill:
        - "单抓孤立远程"
        - "拿星后隐身/Invisiheal 撤退"
        - "用 clone 或 Lollipop 消耗敌方探点资源"
      cannot_fulfill:
        - "多目标连续清场"
        - "纯长线稳定主狙"
      needs_teammate_support:
        - "远程压血和逼技能"
        - "保护 Leon 隐身路径"
      false_positive: "Shooting Star / Dry Season 这类开阔图只有在敌方无 peel 时才考虑 Leon 后手"
    - mode: "Knockout"
      can_fulfill:
        - "最后手单抓无保护目标"
        - "隐身绕路制造残局"
      cannot_fulfill:
        - "先手吃控制开团"
        - "穿透处理多人抱团"
      needs_teammate_support:
        - "压低目标血量或逼出探测技能"
      false_positive: "敌方抱团和召唤物会显著削弱隐身价值"
    - mode: "Hot Zone"
      can_fulfill:
        - "Lollipop Drop 保护圈边站位"
        - "草丛伏击和侧路切入"
      cannot_fulfill:
        - "单独持续站圈"
        - "大范围清圈"
      needs_teammate_support:
        - "站圈身体、治疗或范围控制"
      false_positive: "Ring of Fire 类图先问草控/探草；Leon 不能替代区域控制"

  failure_modes:
    - id: "lollipop_anchor_is_fragile"
      active_when: "阵容依赖 Lollipop Drop 长期保护圈边、长线或球路，但敌方可从安全距离持续打锚点"
      exposed_by: "[[sources/Fandom-Leon|Fandom-Leon]] Lollipop Drop 只有 2000 HP 且每秒衰减 200"
      mitigation: "把它当一次隐蔽/提速窗口，放在敌方射线外或配合立即推进；不要把 Leon 计作长期团队隐身核心"
      bp_use: "resource_and_anchor_durability_check"
    - id: "revealed_or_swept_path"
      active_when: "敌方有范围扫草、召唤物、炮台或持续弹幕覆盖 Leon 隐身路线"
      exposed_by: "[[sources/Fandom-Leon|Fandom-Leon]] 隐身受近距离探测和受伤短暂显形影响"
      mitigation: "利用草/墙起 Super，等待敌方探点资源交掉，或改用 Lollipop 控局"
      bp_use: "vision_tax / must_avoid"
    - id: "single_target_only"
      active_when: "敌方抱团、召唤物多或需要同时清多人"
      exposed_by: "[[sources/Fandom-Leon|Fandom-Leon]] Leon 通常不适合一次消灭多个目标"
      mitigation: "只用于单抓孤立目标；队友补范围和清召唤物"
      bp_use: "role_gap_check"
    - id: "reload_after_failed_burst"
      active_when: "目标 survive 第一轮近身爆发或 Leon 弹药不足"
      exposed_by: "Leon 装填 1.9 秒，非持续 brawler"
      mitigation: "先远程蹭血再进场，或等队友补斩杀"
      bp_use: "candidate_eval.must_avoid"
    - id: "objective_visibility_breaks_stealth"
      active_when: "Gem Grab 拿宝石、Brawl Ball 持球等会短暂暴露 Leon"
      exposed_by: "[[sources/Fandom-Leon|Fandom-Leon]] 说明拾取目标/持球会暴露位置"
      mitigation: "把隐身用于接近或撤退，不把持球隐身当作完全安全"
      bp_use: "mode_fit_false_positive"

  conditional_matchup_seeds:
    - target: ["Piper", "Colt", "Bonnie", "Mandy", "Dynamike", "Mr. P"]
      direction: "subject_favored"
      source: "[[sources/PLP-Leon|PLP-Leon]]"
      mechanism: "Leon 用远端蹭 Super 后隐身接近，惩罚缺探测/低近战自保的远程或投掷"
      active_when: "地图有草墙路线或敌方三远程无 peel，Leon 能在第一轮爆发内完成击杀"
      fails_when: "敌方抱团、保留控制/召唤物探路，或开阔长线让接近路径完全可读"
      bp_use: "slot_6 punish / response to unprotected backline"
    - target: ["Gray", "Chuck", "Ziggy"]
      direction: "subject_favored"
      source: "[[sources/PLP-Leon|PLP-Leon]]"
      mechanism: "隐身绕路可打断依赖路线/站位的支援或输出核心"
      active_when: "目标门/轨道/输出点附近缺守点，Leon 能绕到近身"
      fails_when: "目标有队友蹲点或召唤物挡路，Leon 无法安全接近"
      bp_use: "route-disruption response"
    - target: ["Bolt", "Gale", "Chester", "Bull", "Damian", "Tara", "Trunk", "Nita"]
      direction: "target_favored"
      source: "[[sources/PLP-Leon|PLP-Leon]]"
      mechanism: "这些英雄用控制、爆发、召唤物、范围探点或近战反杀削弱 Leon 隐身进场"
      active_when: "他们能守关键目标或持续暴露 Leon 路线"
      fails_when: "技能已交、目标孤立且 Leon 只需单次击杀/偷球"
      bp_use: "must_avoid / enemy_response_prediction"
    - target: ["Gem carrier", "High bounty target", "Ball carrier"]
      direction: "volatile"
      source: "[[sources/Fandom-Leon|Fandom-Leon]]"
      mechanism: "Leon 可隐身接近高价值目标或自己带资源撤退，但目标交互会暴露位置"
      active_when: "敌方探点不足且 Leon 有撤退路线"
      fails_when: "拾取/持球暴露后敌方有控制、召唤物或范围伤害覆盖"
      bp_use: "objective-specific chase or escape edge"

  slot_notes:
    slot_1: "只有在地图极奖励草/信息差且主要反制被 ban 时才考虑；否则容易被后手探测和控制压低价值"
    slot_2_3: "可作为半计划英雄，逼敌方支付探草/反隐身税，但队伍要补稳定目标职责"
    slot_4_5: "适合回答敌方 2-3 位后排无保护或缺草控的结构，同时补 Brawl Ball/Gem Grab 目标威胁"
    slot_6: "最强顺位；最后确认敌方没有 Gale/Tara/Nita/Bull/Chester 类自然回答后，用隐身单抓或偷目标高维压制"
```

## 关联页面

- [[sources/Fandom-Leon|Fandom 来源摘要: Leon]]
- [[sources/PLP-Leon|PLP 来源摘要: Leon]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
