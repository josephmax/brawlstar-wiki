# Gray

## 基本信息

- 稀有度：Mythic
- 定位：Support
- 类型：传送门路线改写 / 拉人 / 条件开墙支援

## 来源摘要

- Fandom：[[sources/Fandom-Gray|Fandom 来源摘要: Gray]]
- PLP：[[sources/PLP-Gray|PLP 来源摘要: Gray]]
- PLP 推荐模式候选：Hot Zone, Bounty, Knockout

## 角色定位总结

Gray 的 BP 价值来自“把地图路线改写成我方可用、敌方不舒服的路径”。他的传送门能让队友绕过正面火力、快速进出目标点或把短手送到敌方后排；`Walking Cane` 能拉关键目标、打断持球或把低血量目标拉出掩体。Gray 不是单纯长手，也不是无条件开墙英雄；错误传送会把队友送进高爆发近战面前。

## 与其他英雄的区别

- 不同于 `Max`：Gray 不是全队加速，而是固定点到点传送，收益更依赖地图路线和落点安全。
- 不同于 `Gene`：Gray 的拉人来自 Gadget 且距离/弹道条件不同，核心仍是团队路线调度。
- 不同于 `Brock` / `Colt`：Gray 的 `Grand Piano` 可破墙，但不是稳定开图主轴；开墙前必须判断谁更受益。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Gray|Fandom-Gray]] direct_raw_capture_2026-06-30"
    plp: "[[sources/PLP-Gray|PLP-Gray]] direct_raw_capture_2026-06-30"
    user_notes: "本地 BP 规则要求传送门必须绑定路线、落点安全和目标收益"

  capability_vector:
    effective_range: "long; 9 格直线普攻，适合低承诺点射但弹道细且有延迟"
    projectile_reliability: "中低到中；需要预判，近距离或被高机动贴脸时命中不稳定"
    burst: "中等；2-3 发命中可收低血量，Walking Cane 可补确认"
    sustained_dps: "中等；装填快但单发命中要求高"
    objective_damage: "低到条件性；Heist 价值来自传送队友进库，不是自身拆库"
    mobility: "传送门为 Gray 和队友提供固定点位移；自身没有自由 dash"
    survivability: "中低；Fake Injury + Shield gear 可让满血第一下减伤，传送门可撤退"
    engage: "中等；传送门可送自己/队友切入，Walking Cane 拉目标"
    disengage: "强于普通长手；门可作为撤退路线，但落点可被预判"
    anti_aggro: "条件性；拉人和传送撤退可反制部分进场，但怕高爆发落点蹲守"
    anti_tank: "弱到中；能拉/风筝慢目标，但缺高额持续反坦"
    wall_break: "条件性；Grand Piano 可破障碍并击退，但要服务地形状态计划"
    throw_or_wall_bypass: "传送门绕过墙/窄口；Walking Cane 可拉墙后低血量"
    area_control: "低；主要是路线控制而非大范围封区"
    scouting_or_vision: "无稳定探草"
    team_support: "高；传送门、New Perspective 治疗、Hypercharge 护盾都服务队友进出"
    spawnable_or_pet: "无"
    crowd_control: "Walking Cane 拉人；Grand Piano 击退"
    terrain_creation: "传送门创造路线，不创造实体地形"
    terrain_destruction: "Grand Piano 条件破墙"

  build_switches:
    - build: "Walking Cane / Fake Injury / Shield + Damage + Gadget Cooldown"
      source: "[[sources/PLP-Gray|PLP-Gray]] + [[sources/Fandom-Gray|Fandom-Gray]]"
      changes_capabilities:
        - "Walking Cane 把 Gray 从点射支援变成可抓低血量、拉球、拉 gem carrier 的控制点"
        - "Fake Injury + Shield gear 提高长线第一下承伤，支持 Bounty/Knockout 保命"
        - "Gadget Cooldown 增加拉人/断球回合数"
      enables:
        - "Knockout / Bounty 低承诺消耗后抓低血"
        - "Brawl Ball 断球或拉出守门者"
        - "Hot Zone 把队友送入/撤出关键区域"
      mitigates_failure_modes:
        - "partially_mitigates_long_range_trade"
        - "partially_mitigates_target_escape"
      best_when: "敌方关键目标需要被拉出掩体，或地图正面路线被墙/窄口限制而传送能创造安全落点"
      poor_when: "敌方有 Mr. P/Gus/Tara/Nani/Stu/R-T 等能占落点、召唤物耗门、或远程 punish Gray 的工具"
      bp_use: "路线改写支援、response pick、slot_4_5 补路线/抓点"
    - build: "Grand Piano / New Perspective"
      source: "[[sources/Fandom-Gray|Fandom-Gray]]"
      changes_capabilities:
        - "Grand Piano 提供定点伤害、击退和破墙"
        - "New Perspective 让队友过门回血，增强团队撤退/再次进场"
      enables:
        - "选择性开墙回答投掷/口袋"
        - "Hot Zone 或 Heist 传送门续航"
      mitigates_failure_modes:
        - "partially_mitigates_wall_pocket"
      best_when: "关键墙体保护敌方投掷或阻断目标路线，且开墙后我方长线/路线更受益"
      poor_when: "开墙会让敌方远程或刺客更容易惩罚我方"
      bp_use: "terrain_state_plan branch；不是默认开图方案"

  map_feature_hooks:
    - id: "portal_objective_route"
      map_feature_type: "objective_access"
      example_maps:
        - "[[entities/maps/Safe Zone|Safe Zone]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
      route_or_position: "把传送门放在接近敌方目标或可撤退的位置，让高爆发队友缩短进库/换线成本"
      objective_conversion: "Heist 中把 Griff/Leon/Shelly/Buzz/Darryl/8-Bit 等队友送到 safe 附近输出，或快速撤出防守火力"
      active_when: "敌方缺落点清理，队友能把传送转换为 safe damage，且门口不被持续火力覆盖"
      fails_if: "门口被 Nani/Shelly/Bull/Frank 等高爆发守住，或三路隔离导致门无法救崩线"
      bp_use: "team_support objective route；要求 candidate_eval 同时检查队友输出"
    - id: "knockout_portal_pickoff"
      map_feature_type: "route_based_pickoff"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      route_or_position: "用门绕过中心墙/窄口，或把自己送到能收低血量投掷/远程的位置"
      objective_conversion: "Knockout 中把低血量目标变成可确认击杀，同时保留撤退门"
      active_when: "敌方缺落点控制，Gray 有 2-3 发弹药，目标无法立即集火门口"
      fails_if: "敌方高爆发近战蹲门，或墙被打开后门路线失去低风险价值"
      bp_use: "response to wall pocket / late pick finisher"
    - id: "walking_cane_key_target_pull"
      map_feature_type: "key_target_displacement"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      route_or_position: "入口、球门前、宝石矿边或墙后低血量目标"
      objective_conversion: "拉出 gem carrier、拉断持球者、拉墙后投掷，直接制造目标回合"
      active_when: "目标路径可预判，墙体/入口让对方退路有限，队友能跟伤害"
      fails_if: "敌方有召唤物挡弹、目标高机动、或拉人后我方无法击杀"
      bp_use: "slot_4_5/6 的关键目标回答"
    - id: "selective_wall_transform"
      map_feature_type: "wall_break_transform"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
      route_or_position: "用 Grand Piano 打开保护投掷/侧墙口袋/球门屏障附近的关键墙"
      objective_conversion: "拆掉敌方口袋或打开进球/长线角度"
      active_when: "开墙后我方远程或传送路线明显受益，敌方不能反过来接管开放地形"
      fails_if: "己方也依赖墙体生存，或 Pinball Dreams 这类墙本身是己方得分资源"
      bp_use: "terrain_state_plan_check"

  objective_contracts:
    - mode: "Knockout"
      can_fulfill:
        - "portal_pickoff"
        - "low_commitment_poke"
        - "wall_pocket_answer_with_route_or_piano"
      cannot_fulfill:
        - "独立站前排吃技能"
        - "在落点被守住时强行传送进场"
      needs_teammate_support:
        - "能守门口或跟进传送击杀的队友"
        - "开墙/保墙计划明确"
      false_positive: "门不是安全承诺；落点被高爆发覆盖时会直接送人"
    - mode: "Bounty"
      can_fulfill:
        - "长线低承诺点射"
        - "保星撤退门"
        - "拉出低血量或关键星目标"
      cannot_fulfill:
        - "替代极长射程主狙"
        - "无视召唤物/远程压制"
      needs_teammate_support:
        - "更稳定长线或探草"
        - "能保护 Gray 满血减伤节奏"
      false_positive: "Shooting Star / Dry Season 这类极长线图要确认 Gray 射程和命中能跟上对方主狙"
    - mode: "Hot Zone"
      can_fulfill:
        - "把队友送入热区或从 L 墙支援口袋撤出"
        - "拉出圈内关键目标"
        - "通过传送改变支援角度"
      cannot_fulfill:
        - "单独持续站圈"
        - "替代大范围清圈"
      needs_teammate_support:
        - "站圈身体、治疗或范围清圈"
      false_positive: "如果队友不能利用门，Gray 的热区价值只剩点射和偶发拉人"

  failure_modes:
    - id: "portal_exit_camped"
      active_when: "敌方高爆发、控制或召唤物能蹲传送出口"
      exposed_by: "[[sources/Fandom-Gray|Fandom-Gray]] 提到误传到 Darryl/Colt/Fang/Shelly/Nani 等高伤目标前会被惩罚"
      mitigation: "手动瞄准门位，确认落点不被覆盖，或把门用于撤退而非进攻"
      bp_use: "candidate_eval.must_avoid"
    - id: "thin_projectile_misses_mobility"
      active_when: "敌方 Stu/Max/Mortis/Sam 等高机动目标能横移躲 Gray 细弹道"
      exposed_by: "[[sources/Fandom-Gray|Fandom-Gray]] 建议瞄准而非 auto aim"
      mitigation: "选在窄口、墙边或队友控制后拉人/点射"
      bp_use: "matchup_false_positive_filter"
    - id: "route_support_without_user"
      active_when: "我方队友没有能利用传送的爆发、站圈或拆库任务"
      exposed_by: "Gray 的主要收益来自传送队友而非自身数值"
      mitigation: "只在 draft 已有可送入目标的队友时提高优先级"
      bp_use: "duty_coverage_check"
    - id: "wall_break_backfires"
      active_when: "Grand Piano 打开墙后敌方长手/刺客比我方更受益"
      exposed_by: "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]] 地形状态计划"
      mitigation: "先定义要开的墙和后续站位，再决定 build"
      bp_use: "terrain_state_plan_check"

  conditional_matchup_seeds:
    - target: ["Sprout", "Grom", "Dynamike", "Squeak"]
      direction: "subject_favored"
      source: "[[sources/PLP-Gray|PLP-Gray]]"
      mechanism: "Gray 用传送门绕过墙体或用 Walking Cane 拉出投掷，减少正面穿口成本"
      active_when: "墙体保护投掷但门能创造侧角，敌方无高爆发守门，Gray 有弹药确认击杀"
      fails_when: "传送出口被守、投掷身边有近战/控制、或墙被开后 Gray 没有路线优势"
      bp_use: "anti-thrower response；更适合 4-5/6 位"
    - target: ["Carl", "Emz", "Bo", "Lou"]
      direction: "subject_favored"
      source: "[[sources/PLP-Gray|PLP-Gray]]"
      mechanism: "拉人和传送可打乱这些英雄依赖距离、站位或区域技能的节奏"
      active_when: "目标站位可被拉出安全区，队友能跟上集火"
      fails_when: "目标有召唤物挡弹、队友保护或 Gray 拉人后无斩杀"
      bp_use: "key_target_pull / zone_position_punish"
    - target: ["Mr. P", "Gus", "Tara", "Nani", "Sam", "R-T", "Lola", "Stu"]
      direction: "target_favored"
      source: "[[sources/PLP-Gray|PLP-Gray]]"
      mechanism: "召唤物、护盾、长线爆发、高机动或形态压制会降低 Gray 点射/拉人/传送门收益"
      active_when: "这些英雄能守门、挡弹、追击 Gray 或让他无法保持满血减伤"
      fails_when: "地图窄口让 Walking Cane 命中更稳定，或他们缺队友保护被拉出后可被秒"
      bp_use: "enemy_response_prediction / ban_reason"
    - target: ["Gem carrier", "Ball carrier"]
      direction: "subject_favored"
      source: "[[sources/Fandom-Gray|Fandom-Gray]]"
      mechanism: "Walking Cane 可拉敌方持球者或宝石持有者，改变目标位置"
      active_when: "目标靠墙/入口/球门前移动且队友能跟伤害"
      fails_when: "目标有位移、召唤物挡线，或拉人后我方阵型无法承接"
      bp_use: "objective-specific response edge"

  slot_notes:
    slot_1: "不宜无脑一抢；只有地图明确需要路线支援且我方能围绕传送门建队时才考虑"
    slot_2_3: "可作为 plan-building 支援，配一个能吃门收益的拆库/站圈/刺杀队友"
    slot_4_5: "很适合补路线缺口或回答敌方墙后投掷/关键目标，但要防 slot_6 选高爆发蹲门"
    slot_6: "可用作最后手惩罚无落点控制的投掷/远程阵容，或用 Walking Cane 专门回答球/宝石关键目标"
```

## 关联页面

- [[sources/Fandom-Gray|Fandom 来源摘要: Gray]]
- [[sources/PLP-Gray|PLP 来源摘要: Gray]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
