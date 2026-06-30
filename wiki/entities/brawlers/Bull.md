# Bull

## 基本信息

- 稀有度：Rare
- 定位：Tank
- 类型：近身霰弹 / 冲锋破墙 / Heist 接触爆发

## 来源摘要

- Fandom：[[sources/Fandom-Bull|Fandom 来源摘要: Bull]]
- PLP：[[sources/PLP-Bull|PLP 来源摘要: Bull]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Hot Zone, Heist

## 角色定位总结

Bull 的 BP 价值来自“能否把自己送到目标脸上”。他贴脸霰弹和 Berserker 在 Heist 打库、Brawl Ball 破门/自传球、草丛伏击里很有上限，但在开阔图或敌方有击退、反坦、沉默、减速时很容易变成给对面充 Super 的短手。Bull 不是泛用前排；他是需要路线、草墙、入库角度和控制真空的目标接触型坦克。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Bull|Fandom-Bull]] direct_raw_capture_2026-06-30-v2"
    plp: "[[sources/PLP-Bull|PLP-Bull]] direct_raw_capture_2026-06-30"
    user_notes: "按高水平 BP 处理：短手必须证明路线、目标收益和反制资源状态"

  capability_vector:
    effective_range: "短到中；5.33 格霰弹只有贴脸才有最大价值"
    projectile_reliability: "贴脸可靠，远端散弹价值快速下降"
    burst: "极高贴脸爆发；Berserker 低血时把 safe/body DPS 拉满"
    sustained_dps: "条件性高；必须保持近身接触"
    objective_damage: "高；Heist 能接触 safe 时是核心卖点"
    mobility: "Super 长距离冲锋、破墙并越过水/障碍路线；Stomper 可停止冲锋并转为近身控制"
    survivability: "高血量，T-Bone Missile 治疗，Tough Guy 可低血护盾；但冲锋中不免伤"
    engage: "强但路线可读；依赖草、墙、Super 或敌方站位错误"
    disengage: "Super 可逃跑，但会破坏墙体并可能冲到危险位置"
    anti_aggro: "贴脸霰弹能惩罚部分刺客/前排，但怕控制链和高 burst"
    anti_tank: "对短手有高贴脸伤害，但被更稳定反坦/击退克制"
    wall_break: "Super 破坏路径障碍，可打开金库或球门角度"
    throw_or_wall_bypass: "Super 可穿越障碍接近目标"
    area_control: "低；主要是身体压迫和路径破坏"
    scouting_or_vision: "无稳定探草"
    team_support: "破墙可服务队友，T-Bone 仅自保"
    spawnable_or_pet: "无"
    crowd_control: "Super 击退；Stomper 可转为近身减速/控制窗口"
    terrain_creation: "无"
    terrain_destruction: "强；冲锋开墙会永久改变地图"

  build_switches:
    - build: "T-Bone Missile / Berserker / Health + Damage"
      source: "[[sources/PLP-Bull|PLP-Bull]] + [[sources/Fandom-Bull|Fandom-Bull]]"
      changes_capabilities:
        - "T-Bone Missile 让 Bull 进库或进草后多活一轮，适合 Heist 持续打库"
        - "Berserker 在低血时翻倍装填，打 safe 或近身 body 的窗口非常高"
        - "Health/Damage 服务前排承伤和低血爆发"
      enables:
        - "Heist 短窗口 safe melt"
        - "Brawl Ball 破墙/自传球"
        - "Hot Zone / Gem Grab 草口身体压迫"
      mitigates_failure_modes:
        - "partially_mitigates_focus_fire_during_contact"
        - "partially_mitigates_low_health_safe_race"
      best_when: "地图有金库屏障、草路、短入口或球门墙，敌方反坦资源不足"
      poor_when: "地图开阔、敌方有 Maisie/Shelly/Colette/Lou/Otis/Surge 等稳定反制，或开墙会帮敌方长手"
      bp_use: "Heist access pick、Brawl Ball wallbreak/scorer、last-pick tank route punish"
    - build: "Stomper / Tough Guy"
      source: "[[sources/Fandom-Bull|Fandom-Bull]]"
      changes_capabilities:
        - "Stomper 让冲锋不再必须全程走完，可停在目标旁边转贴脸击杀"
        - "Tough Guy 增强低血承伤，适合需要持续站住而不是纯 race 的局面"
      enables:
        - "停止错误冲锋"
        - "抓侧路或防守反打"
      mitigates_failure_modes:
        - "mitigates_overcharge_into_bad_position"
      best_when: "需要精确停在目标身边或地图容易让长距离冲锋送进危险区"
      poor_when: "Heist 主要任务是远距离冲到 safe，且敌方没有守库身体"
      bp_use: "control/survival branch"

  map_feature_hooks:
    - id: "heist_super_to_safe_burst"
      map_feature_type: "objective_access"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
      route_or_position: "金库屏障、斜草或侧路入库口，用 Super 破墙并贴库输出"
      objective_conversion: "把一次蓄满 Super 转成高额 safe damage，同时开出队友打库线"
      active_when: "敌方缺守库击退/反坦，Bull 能接触 safe 至少数秒"
      fails_if: "Super 入口被控、safe 旁有 Shelly/Colette/Lou/Otis，或开墙反而让敌方远程 race 更快"
      bp_use: "candidate_eval.heist_contact_dps"
    - id: "brawl_ball_wallbreak_self_pass"
      map_feature_type: "score_window"
      example_maps:
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
      route_or_position: "球门墙、侧草推进线或中路球权，踢球后冲锋跟球"
      objective_conversion: "打开球门或自传球制造直接得分窗口"
      active_when: "破墙后我方 scorer/远程更受益，敌方没有保留击退和硬控"
      fails_if: "Super 破坏己方关键墙、敌方开阔图更强，或 Bull 只击退敌方持球者帮对面开门"
      bp_use: "slot_task.goal_wallbreak_and_scorer"
    - id: "grass_choke_tank_entry"
      map_feature_type: "grass_route"
      example_maps:
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
      route_or_position: "斜草、侧草或热区入口 chokepoint"
      objective_conversion: "从草口逼退长手、守圈或迫使 gem carrier 后撤"
      active_when: "敌方缺探草/扫草，队友能跟随 Bull 的身体压迫"
      fails_if: "草被清、入口被 slow/stun/anti-tank 覆盖，或 Bull 被迫横穿开阔区"
      bp_use: "map_bp_factors.grass_body_entry"
    - id: "terrain_transform_risk"
      map_feature_type: "wall_break_transform"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
      route_or_position: "safe wall、球门墙、中心堡垒墙或 trick-shot 墙"
      objective_conversion: "选择性破墙可打开目标；错误破墙会拆掉己方路线/掩体"
      active_when: "我方后续能利用开放线，且敌方不会因此获得更强远程"
      fails_if: "开墙让敌方 marksman/scorer 接管，或移除 Bull 自己需要的接近墙"
      bp_use: "terrain_state_plan.check_before_pick"

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - "contact_safe_dps"
        - "safe_wall_break_route"
        - "defender_recall_pressure"
      cannot_fulfill:
        - "远程低承诺打库"
        - "三路长线隔离中稳定守一路"
      needs_teammate_support:
        - "开路前的线权或探草"
        - "防止敌方远程 race 反超"
      false_positive: "会冲锋不等于能打库；必须证明入库后能活并输出"
    - mode: "Brawl Ball"
      can_fulfill:
        - "wallbreak_score_window"
        - "self_pass_scorer"
        - "goal_front_body_pressure"
      cannot_fulfill:
        - "稳定远程清球"
        - "无脑破墙后仍保证防守"
      needs_teammate_support:
        - "控人/补射/远程接管开放线"
      false_positive: "破门收益必须大于帮敌方打开射门线的风险"
    - mode: "Hot Zone"
      can_fulfill:
        - "zone_entry_body"
        - "grass_choke_pressure"
        - "反投掷/炮台的贴脸清点"
      cannot_fulfill:
        - "圈外远程清场"
        - "被多重 slow/control 覆盖时单独进圈"
      needs_teammate_support:
        - "探草、清场或控制跟进"
      false_positive: "站圈身体如果不能接近入口，只会给对面充资源"
    - mode: "Gem Grab"
      can_fulfill:
        - "侧草压迫"
        - "保护/追击 gem carrier"
      cannot_fulfill:
        - "稳定中路持宝石"
        - "无视远程消耗穿越开阔中线"
      needs_teammate_support:
        - "稳定 mid 和视野控制"
      false_positive: "高血量不等于适合拿宝石；Bull 更适合侧压和反切"

  failure_modes:
    - id: "open_lane_kited"
      active_when: "Shooting Star、Dry Season、Bridge Too Far 等长线开阔或三路隔离场景"
      exposed_by: "[[sources/Fandom-Bull|Fandom-Bull]] 贴脸才有最大伤害"
      mitigation: "只在草墙/入库路线存在时选，或作为最后手惩罚无反坦阵容"
      bp_use: "map_hard_gate"
    - id: "anti_tank_control_chain"
      active_when: "敌方有 Maisie/Shelly/Colette/Lou/Otis/Surge/Charlie"
      exposed_by: "[[sources/PLP-Bull|PLP-Bull]] counteredBy signal + 本地条件化对位规则"
      mitigation: "ban 关键反制、等待资源交出，或用队友先开路"
      bp_use: "must_avoid / ban_reason"
    - id: "wallbreak_backfires"
      active_when: "Bull 的 Super 打开己方防守墙、球门墙或让敌方长线更强"
      exposed_by: "[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]] terrain_state_plan"
      mitigation: "明确要开的墙和后续受益方；必要时使用 Stomper 精确停位"
      bp_use: "terrain_state_plan_check"
    - id: "super_path_predictable"
      active_when: "冲锋路径长且直，敌方能预站终点或用控制覆盖"
      exposed_by: "Super 不是免伤位移且路径会破墙"
      mitigation: "从草/侧路起手，或配合队友控制让终点安全"
      bp_use: "candidate_eval.route_safety"

  conditional_matchup_seeds:
    - target: ["Sprout", "Grom", "Poco", "Gus"]
      direction: "subject_favored"
      source: "[[sources/PLP-Bull|PLP-Bull]]"
      mechanism: "Bull 通过草墙路线或 Super 穿墙把低近战自保的控制/支援拉入贴脸霰弹区"
      active_when: "地图提供接近路线，目标缺 hard peel，Bull 进场后能持续接触"
      fails_when: "墙口被控制覆盖、队友保护目标，或 Bull 被开阔线提前消耗"
      bp_use: "last_pick_route_punish"
    - target: ["Buzz", "Buster", "Bibi", "Sam"]
      direction: "volatile"
      source: "[[sources/PLP-Bull|PLP-Bull]]"
      mechanism: "Bull 的贴脸爆发能赢部分近身 body trade，但对方也可能用控制、屏障、位移或弹药状态反打"
      active_when: "Bull 有先手草口/终点优势或目标资源已交"
      fails_when: "对方保留 stun/screen/knockback 或多角度队友跟伤害"
      bp_use: "close_body_trade_check"
    - target: ["Maisie", "Shelly", "Stu", "Charlie", "Colette", "Lou", "Otis", "Surge"]
      direction: "target_favored"
      source: "[[sources/PLP-Bull|PLP-Bull]]"
      mechanism: "击退、百分比伤害、沉默、冻结/减速、位移和反突进技能能阻断 Bull 的接触窗口"
      active_when: "这些资源能留给 Bull 的入场或 safe 终点"
      fails_when: "资源被 bait，Bull 从侧草进场，或目标被队友先压低"
      bp_use: "must_avoid_or_ban_reason_for_bull_plan"
    - target: ["Heist safe", "Goal wall", "Zone entry"]
      direction: "subject_favored"
      source: "[[sources/Fandom-Bull|Fandom-Bull]]"
      mechanism: "Super 破墙和近身霰弹可直接转换目标压力"
      active_when: "目标入口被墙/草保护且敌方无法立即控制 Bull"
      fails_when: "目标已被远程 race 接管，或开墙帮助敌方多于我方"
      bp_use: "objective_specific_route_edge"

  slot_notes:
    slot_1: "只在 Heist/Brawl Ball 地图明确奖励入库或破门且主要反坦已被 ban 时考虑；否则早手容易被低成本反制"
    slot_2_3: "可作为地图计划手，围绕 safe access 或 goal wallbreak 建队，但要补探草和反控制"
    slot_4_5: "适合在已知敌方缺反坦/控制时压目标路线，也可回答投掷/支援口袋"
    slot_6: "最适合用于惩罚敌方无反坦、无探草、无守库控制的阵容，要求能明确转化为打库/得分/站圈"
```

## 关联页面

- [[sources/Fandom-Bull|Fandom 来源摘要: Bull]]
- [[sources/PLP-Bull|PLP 来源摘要: Bull]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
