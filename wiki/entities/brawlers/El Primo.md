# El Primo

## 基本信息

- 稀有度：Rare
- 定位：Tank
- 类型：跳入开团 / 摔人位移 / 足球得分窗口

## 来源摘要

- Fandom：[[sources/Fandom-El-Primo|Fandom 来源摘要: El Primo]]
- PLP：[[sources/PLP-El-Primo|PLP 来源摘要: El Primo]]
- PLP 推荐模式候选：Brawl Ball, Heist

## 角色定位总结

El Primo 的核心不是“肉”，而是用受击充能和 Super 跳入把短手问题暂时解决。他在 Brawl Ball 的自传球、破门、击退防守者，Heist 的跳库和 Asteroid Belt 开墙中有明确目标价值；但在开阔图、无墙图、敌方反坦/沉默/高 DPS 充足时，Primo 会因为攻击极短、Super 轨迹可预判而失效。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-El-Primo|Fandom-El-Primo]] direct_raw_capture_2026-06-30-v2"
    plp: "[[sources/PLP-El-Primo|PLP-El-Primo]] direct_raw_capture_2026-06-30"
    user_notes: "近战坦克按高水平对局预设：路线、Super 充能、控制反制必须显式检查"

  capability_vector:
    effective_range: "very_short; 3 格拳击，必须进入近身"
    projectile_reliability: "近身持续命中可靠；远程完全无压力"
    burst: "中高；Super 落地 + El Fuego + 快速拳击可秒低血目标"
    sustained_dps: "高；0.8 秒装填但前提是贴身持续接触"
    objective_damage: "条件性；Heist 跳到 safe 后输出可观，El Fuego 增加固定目标伤害"
    mobility: "Super 长距离跳跃越墙并击退/破墙；Meteor Rush 提供落地后移速"
    survivability: "极高血量，受伤充 Super；但吃伤也会给对方充 Super"
    engage: "强；Super 可越过墙/水/屏障切入"
    disengage: "中等；Super 可逃跑，但通常是主要进场资源"
    anti_aggro: "可用 Suplex/Super 打断近身目标或持球者"
    anti_tank: "不稳定；能打慢目标，但怕 Bull/Shelly/Colette/Otis 等反坦"
    wall_break: "Super 与 Asteroid Belt 可破墙"
    throw_or_wall_bypass: "Super 跳跃越障碍"
    area_control: "中等；落地击退、Suplex 位移、Asteroid 迫使走位"
    scouting_or_vision: "Suplex 可探草但不是真 reveal"
    team_support: "通过摔人、破墙、击退为队友创造目标窗口"
    spawnable_or_pet: "无"
    crowd_control: "Super 击退，Suplex Supplement 摔人/位移，Asteroid knockback"
    terrain_creation: "无"
    terrain_destruction: "中等；Super/Asteroid 可打开目标墙"

  build_switches:
    - build: "Suplex Supplement / El Fuego / Shield + Damage"
      source: "[[sources/PLP-El-Primo|PLP-El-Primo]] + [[sources/Fandom-El-Primo|Fandom-El-Primo]]"
      changes_capabilities:
        - "Suplex Supplement 稳定打断持球、防守者、Frank/Carl 等慢 Super"
        - "El Fuego 增加落地后持续伤害和 Heist 固定目标伤害"
        - "Shield/Damage 增强入场承伤和贴脸斩杀线"
      enables:
        - "Brawl Ball 得分/断球/摔开守门"
        - "Heist 跳库和破墙协助队友"
        - "Hot Zone/Gem Grab 局部赶人和前排保护"
      mitigates_failure_modes:
        - "partially_mitigates_goal_defender"
        - "partially_mitigates_low_burst_after_jump"
      best_when: "地图给墙/草/球门/金库屏障，敌方缺持续反坦或没有保留控制给 Primo 落点"
      poor_when: "纯开阔长线、敌方 Colette/Otis/Clancy/Maisie/8-Bit 等能在跳前后稳定处理"
      bp_use: "Brawl Ball scorer/control、Heist jump-to-safe、objective displacement"
    - build: "Asteroid Belt / Meteor Rush"
      source: "[[sources/Fandom-El-Primo|Fandom-El-Primo]]"
      changes_capabilities:
        - "Asteroid Belt 定点破墙和逼走位，尤其用于足球破门或 Heist 开库墙"
        - "Meteor Rush 提高落地后追击、抢球和撤出速度"
      enables:
        - "选择性开墙"
        - "跳入后继续追击或自传球"
      mitigates_failure_modes:
        - "partially_mitigates_slow_post_jump_chase"
      best_when: "关键墙体阻挡进球/打库，且开墙后我方更受益"
      poor_when: "我方也依赖墙体接近或防守，开墙会帮敌方远程"
      bp_use: "terrain_state_plan branch"

  map_feature_hooks:
    - id: "brawl_ball_jump_score_and_suplex"
      map_feature_type: "score_window"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      route_or_position: "中路球权、侧草推进、球门前墙体或守门者身位"
      objective_conversion: "自传球接 Super、摔开防守者、击退持球者或破门"
      active_when: "Primo 已有 Super 或能安全受击充能，敌方无保留 knockback/silence"
      fails_if: "Super 轨迹被预判、持球暴露后被控，或破墙让敌方防守更强"
      bp_use: "slot_task.brawl_ball_scorer_and_displacement"
    - id: "heist_jump_to_safe_or_wallbreak"
      map_feature_type: "objective_access"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
      route_or_position: "safe 前屏障、侧路墙、斜草转入库口"
      objective_conversion: "越过防线直接贴库，或破开库墙让队友跟伤害"
      active_when: "Super 充能来源稳定且敌方守库缺反坦/击退"
      fails_if: "Primo 跳库后被 Colette/Shelly/Otis/8-Bit 秒处理，或没有队友同步 race"
      bp_use: "candidate_eval.heist_jump_access"
    - id: "zone_body_displacement"
      map_feature_type: "zone_presence"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      route_or_position: "热区入口、草口、远圈路线或站圈身体"
      objective_conversion: "用 Super/Suplex 把敌人赶出圈，或用高血量争取计分时间"
      active_when: "敌方缺 percent damage / slow / knockback，队友有清圈输出"
      fails_if: "Primo 单独站圈被远程消耗，或双圈图缺独立轮转职责"
      bp_use: "map_bp_factors.zone_body_with_displacement"
    - id: "wall_break_support_for_range"
      map_feature_type: "wall_break_transform"
      example_maps:
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
      route_or_position: "球门墙、safe wall、中心堡垒墙或敌方掩体"
      objective_conversion: "用 Super/Asteroid 打开队友远程线或清除敌方保护墙"
      active_when: "开墙后我方远程/安全 DPS 明确受益"
      fails_if: "开墙同时削弱 Primo 接近路线或让敌方远程接管"
      bp_use: "terrain_state_plan.selective_wallbreak"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "scoring_window_creator"
        - "ball_carrier_displacement"
        - "goal_wall_transform"
      cannot_fulfill:
        - "稳定远程清球"
        - "敌方控制完整时正面硬带球"
      needs_teammate_support:
        - "补清球、远程接管或控人"
      false_positive: "Primo 有 Super 才是得分威胁；无 Super 时短手问题很严重"
    - mode: "Heist"
      can_fulfill:
        - "jump_to_safe"
        - "safe_wallbreak_support"
        - "short_contact_damage"
      cannot_fulfill:
        - "低承诺远程 safe DPS"
        - "三路长线独立守路"
      needs_teammate_support:
        - "真正持续拆库或防反推队友"
      false_positive: "跳到 safe 不等于能活着输出；必须看守库控制和队友 race"
    - mode: "Hot Zone"
      can_fulfill:
        - "zone_body"
        - "displace_zone_holder"
        - "far_zone_jump"
      cannot_fulfill:
        - "圈外消耗和持续区域封锁"
      needs_teammate_support:
        - "清场、治疗或范围火力"
      false_positive: "高血量前排没有反控保护，会被 slow/percent damage 当充能资源"

  failure_modes:
    - id: "open_map_no_wall_route"
      active_when: "开阔长线图或墙草不能服务主目标"
      exposed_by: "[[sources/Fandom-El-Primo|Fandom-El-Primo]] 明确提示 Primo 在 open maps 中挣扎"
      mitigation: "只在有墙、草、球门、safe 屏障或受击充能窗口时选"
      bp_use: "map_hard_gate"
    - id: "anti_tank_or_silence_denies_jump"
      active_when: "敌方有 Colette/Otis/Clancy/8-Bit/Maisie/Shelly/Colt 等反坦或控制"
      exposed_by: "[[sources/PLP-El-Primo|PLP-El-Primo]] counteredBy signal"
      mitigation: "ban 核心反制或最后手确认敌方缺反坦"
      bp_use: "must_avoid / ban_reason"
    - id: "super_trajectory_readable"
      active_when: "Primo 从远距离直线跳入，目标有时间预判落点"
      exposed_by: "[[sources/Fandom-El-Primo|Fandom-El-Primo]] 建议长距离要提前预判且跳速可读"
      mitigation: "从草/短距离/队友控制后起跳，或用 Suplex 处理近身目标"
      bp_use: "candidate_eval.engage_reliability"
    - id: "wallbreak_backfires"
      active_when: "Asteroid/Super 打开己方需要的墙或让敌方远程进场"
      exposed_by: "Fandom 提示障碍物也可能是己方功能条件"
      mitigation: "提前定义墙体状态计划"
      bp_use: "terrain_state_plan_check"

  conditional_matchup_seeds:
    - target: ["Squeak", "Sprout", "Tick", "Grom", "Piper"]
      direction: "subject_favored"
      source: "[[sources/PLP-El-Primo|PLP-El-Primo]]"
      mechanism: "Super/Suplex 绕过或打断低近战自保后排，贴脸后快速拳击完成击杀"
      active_when: "地图有墙草、目标无 bodyguard，Primo 已充 Super 或能安全受击充能"
      fails_when: "目标有队友保护、入口被控、或地图开阔导致跳前被消耗"
      bp_use: "last_pick_backline_or_thrower_punish"
    - target: ["Poco", "Jae-yong", "Alli"]
      direction: "subject_favored"
      source: "[[sources/PLP-El-Primo|PLP-El-Primo]]"
      mechanism: "Primo 可以用高血量和位移强行压低爆发支援/机动目标的站位"
      active_when: "支援目标必须站在球门、safe、zone 或 carrier 路线上"
      fails_when: "支援被反坦保护或 Primo 无法接近核心位置"
      bp_use: "objective_body_pressure"
    - target: ["Clancy", "Colette", "Colt", "Nita", "Otis", "8-Bit", "Edgar", "Maisie"]
      direction: "target_favored"
      source: "[[sources/PLP-El-Primo|PLP-El-Primo]]"
      mechanism: "反坦 DPS、沉默、召唤物身体、爆发或近身机动会让 Primo 跳入后无法持续输出"
      active_when: "这些英雄能守落点或在 Primo 接近前持续削血"
      fails_when: "资源已交，目标孤立，或 Primo 只需一次摔人/进球窗口"
      bp_use: "must_avoid_or_enemy_response_prediction"
    - target: ["Bull", "Darryl", "Frank"]
      direction: "volatile"
      source: "[[sources/Fandom-El-Primo|Fandom-El-Primo]]"
      mechanism: "近战互打取决于站位、弹药、Super/ Suplex 时机和是否吃满对方爆发"
      active_when: "Primo 能用射程边缘、Super 击退或 Suplex 打断关键攻击"
      fails_when: "对方贴脸爆发/控制先手，或 Primo 被迫正面吃满伤害"
      bp_use: "close_tank_mirror_check"

  slot_notes:
    slot_1: "不适合普通一抢；只有足球/Heist 地图且主要反坦被 ban 时才可围绕他建队"
    slot_2_3: "可作为目标计划手，但要补远程清线、开墙收益和防反坦"
    slot_4_5: "适合在敌方 2-3 位缺反坦时压足球/Heist 目标，也可用 Suplex 处理关键持球者"
    slot_6: "最适合最后手惩罚无反坦、无击退、无沉默阵容，要求能明确转化为进球、打库或赶人"
```

## 关联页面

- [[sources/Fandom-El-Primo|Fandom 来源摘要: El Primo]]
- [[sources/PLP-El-Primo|PLP 来源摘要: El Primo]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
