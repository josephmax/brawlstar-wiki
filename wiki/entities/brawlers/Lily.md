# Lily

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：短程背刺 / Shadow Realm 突袭

## 来源摘要

- Fandom：[[sources/Fandom-Lily|Fandom 来源摘要: Lily]]
- PLP：[[sources/PLP-Lily|PLP 来源摘要: Lily]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Hot Zone, Heist

## 角色定位总结

Lily 是强条件刺客：她用 6 格 Trait 在墙后、草内或近距离压迫中充 Super，再靠 Vanish 和 Flourish 突然改变站位。她的强度来自“接近路线 + 命中确认 + 逃生资源”同时成立，而不是短手本身。Spiky 提供击杀阈值，Vigilance 提供运动模式中的追击/抢线，Repot 则把 Super 从命中传送改成越墙落点工具。

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
    effective_range: "short; 主攻击 2 格，击杀依赖 Super/Vanish/草墙路线把距离问题消掉"
    projectile_reliability: "high_at_contact; 贴身后输出可靠，Super 未命中则没有传送收益"
    burst: "high; Flourish 命中后接 Spiky 和双 ammo 可快速击杀低中血后排"
    sustained_dps: "medium_high_at_melee; 0.8 秒装填但只有 2 ammo，长时间站撸仍怕高身体"
    objective_damage: "conditional_heist; Vanish 可绕过防线摸 safe，但缺少稳定远程打库"
    mobility: "very_high_when_resources_ready; Vanish、Super teleport、Repot 和 Hypercharge 共同提供突袭角度"
    survivability: "medium_resource_based; 4200 HP 加 Vanish 逃生，gadget 用掉后容错急降"
    engage: "high_conditional; 需要 trait 充能、草墙路线或 Repot 落点"
    disengage: "medium_high_with_vanish; 没有 Vanish 时短手撤退差"
    anti_aggro: "low_medium; 可用 Vanish 躲技能，但不适合正面接高爆发近战"
    anti_tank: "low; 对高血量和近战反打英雄不稳定"
    wall_break: "none"
    throw_or_wall_bypass: "conditional; Repot 可把 Super 越墙投到落点，Hypercharge 可弹墙并拉入 Shadow Realm"
    area_control: "low; 主要是目标删除，不是持续封区"
    scouting_or_vision: "medium_high; trait 可侦测 6 格内草丛/隐身敌人，Super 满后会失去该侦测收益"
    team_support: "low; 通过击杀后排和逼走威胁间接服务队友"
    crowd_control: "conditional_hypercharge; Shadow Realm 限制双方 Super/Gadget/Hypercharge 使用"

  build_switches:
    - build: "Vanish / Spiky / Shield, Damage, Gadget Cooldown"
      source: "[[sources/PLP-Lily|PLP-Lily]]"
      changes_capabilities:
        - "最大化突袭、逃生和单杀阈值"
        - "Gadget Cooldown 提高一局内可执行的隐身进场次数"
      enables:
        - "Gem carrier 暗杀与撤退"
        - "Heist 绕防线摸 safe"
        - "Knockout/Bounty 中最后手切后排"
      mitigates_failure_modes:
        - "open_lane_no_approach"
        - "super_hit_no_escape"
      best_when: "敌方后排缺 peel，地图有草、墙或侧路让 Lily 蓄 Super 和接近"
      poor_when: "敌方有 Bull、Bibi、Chester、Nita、Tara 等近身反打或显形/召唤物压力"
      bp_use: "default_assassin_build"
    - build: "Vanish / Vigilance / Speed, Gadget Cooldown"
      source: "[[sources/Fandom-Lily|Fandom-Lily]]"
      changes_capabilities:
        - "提高有敌人在 trait 范围内时的追击、抢球和草图移动速度"
      enables:
        - "Brawl Ball 中侧草拿球、追传球线、逼防守者交资源"
      mitigates_failure_modes:
        - "short_range_cannot_stay_connected"
      best_when: "地图目标奖励移动和侧路节奏，击杀阈值不是唯一问题"
      poor_when: "目标是秒杀高价值后排或摸 safe，需要 Spiky 阈值"
      bp_use: "movement_mode_variant"
    - build: "Repot / Spiky / Shield, Damage"
      source: "[[sources/Fandom-Lily|Fandom-Lily]]"
      changes_capabilities:
        - "把 Super 改成越墙落点和小范围命中工具"
      enables:
        - "墙后投掷口袋、Belle's Rock 类棋盘墙、Gem Fort 中心墙的后排威胁"
      mitigates_failure_modes:
        - "route_blocked_by_wall"
      best_when: "Lily 已能稳定充 Super，且目标躲在可预测墙后"
      poor_when: "没有 Super 充能环境，或敌方有高爆发近身反打"
      bp_use: "wall_pocket_punish_variant"

  map_feature_hooks:
    - id: "bush_trait_scout_and_vanish_entry"
      map_feature_type: "grass_flank_and_scout"
      uses_feature_by: "trait 侦测草内敌人，Vanish 穿过危险视野区后从侧草发起贴身"
      objective_conversion: "Gem Grab/Hot Zone/Brawl Ball 中把探草与侧压转成载宝威胁、进圈清人或持球突破"
      active_when: "草丛连接目标区，且敌方缺持续扫草或显形"
      fails_if: "草被烧掉、敌方召唤物/范围控制占草，或 Lily Vanish 进入后没有出口"
      example_maps: ["[[entities/maps/Double Swoosh|Double Swoosh]]", "[[entities/maps/Center Stage|Center Stage]]", "[[entities/maps/Ring of Fire|Ring of Fire]]", "[[entities/maps/Sneaky Fields|Sneaky Fields]]"]
      bp_use: "草图最后手或中后手刺客；同时承担探草价值"
    - id: "wall_backline_or_thrower_pocket_assassin_route"
      map_feature_type: "route_based_assassin_into_wall_pocket"
      uses_feature_by: "Vanish 越过视野压力，Flourish 或 Repot 切入墙后投掷/狙击位置"
      objective_conversion: "Knockout/Bounty 中删除安全口袋目标，Gem Grab 中打开中心入口"
      active_when: "敌方后排依赖墙体或静态站位，且没有近战保护"
      fails_if: "墙后口袋有 Tara/Nita/Bibi/Bull 等反切，或 Lily Super 未命中后无法撤出"
      example_maps: ["[[entities/maps/Belle's Rock|Belle's Rock]]", "[[entities/maps/Layer Cake|Layer Cake]]", "[[entities/maps/Gem Fort|Gem Fort]]", "[[entities/maps/Hideout|Hideout]]"]
      bp_use: "回答投掷/静态后排，但必须验证路线"
    - id: "gem_carrier_shadow_pick"
      map_feature_type: "gem_carrier_chase"
      uses_feature_by: "Vanish 靠近载宝位，Flourish 命中后贴身爆发，击杀后用剩余资源撤离"
      objective_conversion: "直接打断倒计时或抢回宝石"
      active_when: "敌方 carrier 后撤路线经过草/墙，且队友能压住其他两人"
      fails_if: "carrier 周围有硬反切、召唤物阻路或 Lily 没有满 ammo"
      example_maps: ["[[entities/maps/Gem Fort|Gem Fort]]", "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]", "[[entities/maps/Double Swoosh|Double Swoosh]]"]
      bp_use: "Gem Grab 翻盘窗口；不要当稳定中路"
    - id: "heist_vanish_safe_entry_window"
      map_feature_type: "safe_entry_after_lane_or_bush"
      uses_feature_by: "Vanish 绕过中路视野，Spiky 突袭 safe 或防守位"
      objective_conversion: "把一次隐身进库转成 safe damage 或迫使敌方回防"
      active_when: "敌方缺基地清理，侧路/草带能通往金库"
      fails_if: "防守方有近战反打、召唤物堵位或可持续扫描"
      example_maps: ["[[entities/maps/Hot Potato|Hot Potato]]", "[[entities/maps/Pit Stop|Pit Stop]]", "[[entities/maps/Safe Zone|Safe Zone]]"]
      bp_use: "Heist 条件后手，不等同于稳定打库核心"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "侧路探草和逼退 carrier"
        - "倒计时阶段用 Vanish/Flourish 执行载宝暗杀"
      cannot_fulfill:
        - "长期站中路收宝石"
      needs_teammate_support:
        - "中路控矿者、显形/扫草或压线队友"
      false_positive: "Lily 能杀 carrier，但没有中线控制时很难稳定到达 carrier"
    - mode: "Brawl Ball"
      can_fulfill:
        - "侧草持球、切传球线、删除防守后排"
      cannot_fulfill:
        - "独自破门或正面顶球门"
      needs_teammate_support:
        - "破门、控人或能接 Lily 制造的人数差"
      false_positive: "短手刺客不等于天然 scorer；需要球路和退路"
    - mode: "Hot Zone"
      can_fulfill:
        - "从草/墙后切掉圈外支援，短时间清圈"
      cannot_fulfill:
        - "持续站圈抗伤害"
      needs_teammate_support:
        - "站圈身体、区域控制或治疗"
      false_positive: "进圈击杀后没有站圈队友时，Lily 的价值会断掉"
    - mode: "Heist"
      can_fulfill:
        - "隐身进库、偷防守位、迫使回防"
      cannot_fulfill:
        - "在开阔路线上稳定远程打库"
      needs_teammate_support:
        - "边路线权、清基地和 safe DPS 补充"
      false_positive: "一次摸库不能替代整局 race DPS"

  failure_modes:
    - id: "vanish_cooldown_overextension"
      active_when: "Vanish 用于进场后没有保留撤退或第二波资源"
      exposed_by: "Vanish 持续 3 秒且冷却长"
      mitigation: "只在击杀确认、目标价值或队友跟进明确时进场"
      bp_use: "resource_timing_check"
    - id: "short_range_open_lane"
      active_when: "地图开阔且没有草墙路线"
      exposed_by: "主攻击 2 格"
      mitigation: "等最后手惩罚无 peel 后排，或不选"
      bp_use: "avoid_blind_pick_on_open_maps"
    - id: "anti_assassin_body_or_spawnable_tracking"
      active_when: "敌方有近战反打、召唤物、显形或群控守后排"
      exposed_by: "PLP counteredBy: Chester, Bull, Tara, Nita, Ash, Sam, Bibi"
      mitigation: "后手确认目标孤立，或队友先清召唤物/反切"
      bp_use: "counter_screen_before_pick"
    - id: "super_miss_or_no_ammo_confirm"
      active_when: "Flourish 未命中，或 Lily 没有满 ammo 就进场"
      exposed_by: "Super miss gives no teleport; tips mention full ammo before Super"
      mitigation: "使用 Repot 落点、等目标卡墙，或先充满 ammo"
      bp_use: "execution_reliability_filter"

  conditional_matchups:
    - target: ["Sprout", "Dynamike", "Grom", "Piper", "Ziggy", "Squeak"]
      direction: "subject_favored"
      source: "[[sources/PLP-Lily|PLP-Lily]]"
      mechanism: "这些后排/投掷/控制位怕 Lily 绕过视野后贴身；Vanish 消除接近成本，Flourish 提供击杀确认"
      active_when: "有草墙路线，目标缺近身保护，Lily 有 Super 或 Vanish"
      fails_when: "目标身边有反刺客，或地图开阔让 Lily 进场前被消耗"
      bp_use: "last_pick_punish_backline"
    - target: ["Jae-Yong", "Poco"]
      direction: "subject_favored"
      source: "[[sources/PLP-Lily|PLP-Lily]]"
      mechanism: "低爆发支援位一旦被 Lily 贴身，很难在单人窗口内把 Lily 推走"
      active_when: "支援位脱离队友或为了给支援站位靠前"
      fails_when: "目标身边有硬控/坦克，或 Lily 被迫先交 Vanish"
      bp_use: "punish_unprotected_support"
    - target: ["Chester", "Bull", "Bibi", "Sam", "Ash", "Damian"]
      direction: "target_favored"
      source: "[[sources/PLP-Lily|PLP-Lily]]"
      mechanism: "近战爆发、高身体或反突进技能能把 Lily 的贴身窗口反杀"
      active_when: "目标守在 Lily 必须进入的草口、球门或 zone 入口"
      fails_when: "目标已残血、技能交掉，或 Lily 能从背后切孤立目标"
      bp_use: "do_not_draft_lily_as_primary_answer"
    - target: ["Tara", "Nita"]
      direction: "target_favored"
      source: "[[sources/PLP-Lily|PLP-Lily]]"
      mechanism: "显形、召唤物、拉扯和反打能降低 Lily 的隐身接近与爆发可靠性"
      active_when: "Tara/Nita 有资源守后排或占住草口"
      fails_when: "召唤物被清，目标孤立且 Lily 有完整资源"
      bp_use: "requires_team_clear_or_late_pick"

  slot_notes:
    slot_1: "除非地图极端草墙且队伍已经准备围绕刺客打，否则不早手"
    slot_2_3: "可作为草图侧路计划，但仍要看敌方是否能用近战/召唤物回答"
    slot_4_5: "最佳区间；看到敌方后排、投掷或支援缺 peel 后再锁"
    slot_6: "高价值惩罚位；用于删除已暴露的无保护后排或 carrier"
```

## 关联页面

- [[sources/Fandom-Lily|Fandom 来源摘要: Lily]]
- [[sources/PLP-Lily|PLP 来源摘要: Lily]]
