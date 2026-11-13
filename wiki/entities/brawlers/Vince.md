---
title: Vince
type: brawler
status: bp_ready
updated: 2026-11-13
sources:
  - "[[Fandom-Vince]]"
  - "[[PLP-Vince]]"
---

# Vince

![[../../../raw/assets/brawlers/vince.webp]]

## 基本信息

- 稀有度：Mythic
- 定位：Damage Dealer
- 类型：毛毛虫收集成长 / Super 标记增伤 / 防守型长手中单

## 来源摘要

- Fandom：[[sources/Fandom-Vince|Fandom 来源摘要: Vince]]
- PLP：[[sources/PLP-Vince|PLP 来源摘要: Vince]]
- 对位参考：[[sources/User-Note-Matchup-Review-2026-10-28|用户逐项复核]]

## 角色定位总结

Vince 是靠地图上周期性出现的毛毛虫叠收藏、再用 Super 标记敌人并放大普攻伤害的防守型长手。他的强势窗口在 10 条以上毛毛虫：Super 从单发变成 5 发并附带回弹，20 条以上再获得 7 发与减速；20 条后继续收集仍会提高标记增伤，并作为死亡损失一半收藏的缓冲。基础普攻和低收藏 Super 都不高，且完全没有位移，必须靠站位、队友控制和 Hypercharge 的四只毛毛虫拖住突进。

## 已描述的机制

- Trait：附近周期性生成毛毛虫，最多 5 只同时存在；普攻命中或走过会收集为飞蛾。死亡损失 50% 收藏（向下取整），收集 99 条后停止生成。
- 普攻 Espresso Shot：8.33 格长直线咖啡弹，Power 1 伤害 1100，装填 1.45 秒；可轻微擦墙，但不是稳定穿墙输出。
- Super Barista Barrage：5/10/20 条飞蛾时升级为 3/5/7 发。命中施加 10 秒毛毛虫标记，使 Vince 的普攻按收藏数获得额外伤害（每蛾 +4.5%）；5+ 命中回 1 发弹药，10+ 弹射到附近敌人，20+ 追加减速。Super 可穿透英雄和环境，但不能作用于 Heist Safe。
- Hypercharge BUG SWARM：Super 始终按最高阶段结算，并在身边释放 4 只 Hypercharged 毛毛虫。毛毛虫 2200 HP、每只 500 伤害、每秒损失 13% 生命，最多持续 8 秒；被摧毁后转为收藏飞蛾。2026-11-11 维护将生成数由 6 降至 4，并提高宠物生命衰减速度 30%。

## 妙具与星辉

- Hot Coffee：越墙投掷范围咖啡，伤害等同无收藏普攻，消耗 1 发弹药，射程比普攻多 1 格；可顺带收集毛毛虫。
- Metamothosis：把附近毛毛虫全部转为飞蛾，每条额外多 1 条；冷却 13 秒。
- Come to Papa：毛毛虫缓慢向 Vince 移动；会暴露 Vince 的大致位置。
- Bug Bandage：每次收集毛毛虫治疗 1080（Power 1），包括 Metamothosis 与 Hyper 毛毛虫转化。

## 使用边界

Vince 的排位资格已由 Fandom 当前页面与 2026-11 版本记录支持，但基础强度依赖对手给时间叠收藏。Fandom 明确把他列为 Knockout 强项、Heist 弱项；Hot Zone 取决于地图开阔度。PLP 只给出 Knockout 候选，不能把单一第三方模式列表当成全部排位适配。

## 资源引用

应用资源目录使用 `brawler:vince` 头像，以及以上英文能力名称对应的妙具、星辉资源。本库保存上述 Fandom 肖像原图，出处见 [[新英雄头像与发布状态复核-2026-10]]。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  review_gate: reviewed_with_fandom_plp_and_november_ledger
  source_quality:
    fandom: "[[sources/Fandom-Vince|Fandom-Vince]] direct_raw_capture_2026-11-13"
    plp: "[[sources/PLP-Vince|PLP-Vince]] direct_raw_capture_2026-11-13"
    user_notes: "[[sources/User-Note-Matchup-Review-2026-10-28|用户逐项复核]]"

  capability_vector:
    effective_range: "long; 普攻 8.33 格，Super 9 格，Hot Coffee 约 9.33 格越墙投掷"
    projectile_reliability: "medium; 单发直线弹体可轻微擦墙，Super 穿透英雄和环境；命中依赖预判，但没有 Pierce 式弹壳循环"
    burst: "low_base_high_late; Power 1 普攻 1100、Super 400 + 每蛾 20；10+ 蛾的 5 发 Super 与 20+ 蛾标记后才进入高爆发区间"
    sustained_dps: "medium; 1.45 秒装填，收集毛毛虫与进攻共用弹药；20 蛾后继续收集仍提高标记增伤"
    objective_damage: "low; Super 不作用于 Safe，不能承担 Heist race 或稳定目标 DPS"
    mobility: "low; 750 基础移速，无 dash、跳跃或传送"
    survivability: "low_medium; Power 1 本体 3400、Power 11 6800；Bug Bandage 每次收集治疗 1080（P1），死亡损失 50% 收藏"
    engage: "low; 主要靠防守、标记和队友先手，不主动进场"
    disengage: "low; 无位移，只能靠 Hot Coffee 越墙补伤、队友控制或 Hyper 毛毛虫挡路"
    anti_aggro: "low_without_hyper; Hyper BUG SWARM 的 4 只毛毛虫可挡弹、干扰刺客并反打，但不能当作常驻保命"
    anti_tank: "conditional_late; 20+ 蛾标记后普攻增伤可压高血目标，低收藏阶段会被坦克直接贴脸"
    wall_break: "none"
    throw_or_wall_bypass: "high_for_super_and_hot_coffee; Super 穿墙，Hot Coffee 越墙投掷；普攻只有轻微擦墙"
    area_control: "medium_at_10_plus_moths; 5 发 Super 弹射与 20+ 蛾减速可封 choke；低收藏阶段 area 价值低"
    scouting_or_vision: "low; 毛毛虫可见，反而会提示 Vince 的位置"
    team_support: "medium; Super 标记只放大 Vince 自己的普攻，团队价值来自减速、Hyper 毛毛虫挡路和防守站位"
    spawnable_or_pet: "hyper_caterpillars_temporary; 4 只 2200 HP、500 伤害、每秒 13% 生命衰减，最多 8 秒，摧毁后转为飞蛾"
    crowd_control: "slow_at_20_plus_moths; 20+ 蛾 Super 命中减速，Hyper 毛毛虫可身体阻挡"
    terrain_creation: "none"
    terrain_destruction: "none"
    source_trace:
      - "[[sources/Fandom-Vince|Fandom-Vince]]"
      - "[[sources/PLP-Vince|PLP-Vince]]"
      - "[[sources/Supercell-Release-Notes-November-2026|Release Notes November 2026]]"
      - "[[sources/Supercell-Maintenance-November-11-2026|Maintenance November 11 2026]]"

  build_switches:
    - build: "Come To Papa / Metamothosis / Shield, Damage"
      source: "[[sources/PLP-Vince|PLP-Vince]]"
      changes_capabilities:
        - "Come To Papa 让毛毛虫主动靠近，降低在开阔图来回收集的走位成本，但会暴露 Vince 的大致位置"
        - "Metamothosis 一次收取附近全部毛毛虫并额外 +1/条，适合被压时快速把收藏推到 10/20 阈值"
        - "Shield/Damage 提高低血长手的对拼容错与 20+ 蛾标记后的斩杀"
      enables:
        - "Knockout 防守回合叠收藏"
        - "Gem Grab 侧路反 carrier"
        - "Hot Zone 开阔图远程压区"
      mitigates_failure_modes:
        - "slow_start_before_10_moths"
        - "ammo_competition_collection"
      best_when: "地图开阔、敌方缺强突进，Vince 能在队友身后稳定收集到 10/20 蛾"
      poor_when: "敌方有 Cordelius/Mortis/Damian/El Primo 等直接贴脸，或 Amber/8-Bit/Pierce 从更稳定长线压血"
      bp_use: "default_plp_stockpile_build"
    - build: "Bug Bandage / Metamothosis / Shield, Healing"
      source: "[[sources/Fandom-Vince|Fandom-Vince]]"
      changes_capabilities:
        - "Bug Bandage 把每次收集转成 1080（P1）治疗，适合被 chip 后继续留在场上叠收藏"
        - "Healing gear 缩短脱战回复时间；Shield 保住低血本体"
        - "Metamothosis 仍是快速跨过 5/10/20 阈值的主要资源工具"
      enables:
        - "防守型 Knockout/Bounty 长局"
        - "Gem Grab 保护己方 carrier 的续航"
      mitigates_failure_modes:
        - "death_halves_moths"
        - "low_self_sustain"
      best_when: "敌方以 chip/长线消耗为主，Vince 需要靠治疗维持收藏与站位"
      poor_when: "敌方爆发足以在一个 dive 窗口内直接击杀，治疗来不及兑现"
      bp_use: "sustain_variant_into_chip"
    - build: "Hot Coffee / Metamothosis / Shield, Damage"
      source: "[[sources/Fandom-Vince|Fandom-Vince]]"
      changes_capabilities:
        - "Hot Coffee 越墙范围伤害并多 1 格射程，作为第四发攻击收割或清 choke"
        - "不消耗额外弹药的说法与当前 Fandom 正文冲突；按正文实际消耗 1 发弹药处理，不把 Hot Coffee 当免费第四发"
      enables:
        - "墙后残血收割"
        - "Bounty/Knockout choke 范围补伤"
      mitigates_failure_modes:
        - "no_wall_finish"
      best_when: "敌方躲在单格墙后或必须经过窄口，Vince 已有 Super 标记"
      poor_when: "队伍更需要 Metamothosis 快速叠收藏，或 Vince 弹药已经紧张"
      bp_use: "wall_finish_variant"

  map_feature_hooks:
    - id: "knockout_open_choke_moth_collection"
      map_feature_type: "knockout_open_choke_stockpile"
      uses_feature_by: "在开阔长线用普攻安全收集毛毛虫，叠到 10/20 蛾后用 Super 标记和弹射封 choke"
      route_or_position: "Out in the Open 长线、Belle's Rock 侧墙、New Horizons 中央掩体后"
      objective_conversion: "把 Knockout 的防守回合转成 20+ 蛾高增伤反打，或在不暴露本体的情况下用 Super 减速拿首杀"
      active_when: "敌方缺直接 dive，Vince 有队友保护收集路线，且地图允许他从长线撤到掩体后"
      fails_if: "敌方 Mortis/Cordelius/Damian 直接进场，或 Vince 在 10 蛾前被迫接团"
      example_maps:
        - "[[entities/maps/Out in the Open|Out in the Open]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "map_bp_factors.stockpile_knockout_defense"
    - id: "hot_zone_open_ring_of_fire_stack"
      map_feature_type: "open_hot_zone_long_lane"
      uses_feature_by: "Ring of Fire 这类开阔热区允许 Vince 在区外收集并远程压区，20+ 蛾 Super 减速可拖回区者"
      route_or_position: "Ring of Fire 外圈长线、Open Business 侧路、Dueling Beetles 边线"
      objective_conversion: "用长线伤害逼敌方晚进区，再以减速 Super 拖住回区路线"
      active_when: "地图开阔、敌方短手必须穿过 Vince 的射线，且队友能站圈"
      fails_if: "地图是 Parallel Plays 这类闭合热区，敌方可从墙后直接贴脸并打断收集"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
      bp_use: "map_bp_factors.open_zone_stockpile_pressure"
    - id: "gem_grab_carrier_assassination"
      map_feature_type: "gem_carrier_mark_and_slow"
      uses_feature_by: "Super 穿透墙体标记 carrier，10+ 蛾弹射与 20+ 蛾减速让 Vince 能远程打断撤退"
      route_or_position: "Gem Fort 中央墙、Hard Rock Mine 侧路、Double Swoosh 矿区入口"
      objective_conversion: "保护己方 carrier，或在敌方 carrier 倒计时撤退线上用标记+减速逼掉宝石"
      active_when: "Vince 已有 10+ 蛾，敌方 carrier 必须经过可预判直线，队友能接住减速窗口"
      fails_if: "Vince 自己被要求拿宝石，或敌方用召唤物吸收 Super 标记"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "slot_task.carrier_defense_not_carrier"

  objective_contracts:
    - mode: "Knockout"
      can_fulfill:
        - "防守回合叠收藏到 10/20 蛾"
        - "Super 穿墙标记、弹射和减速拿首杀"
        - "Hyper 毛毛虫挡路与反刺客"
      cannot_fulfill:
        - "无位移先手开团"
        - "0-5 蛾阶段的正面爆发"
      needs_teammate_support:
        - "前排或控制队友保护收集路线"
        - "视野与墙后安全位"
      false_positive: "Fandom 把 Knockout 列为强项，但前提是敌方给时间和空间叠收藏；纯开放狙击镜像里 Vince 仍会被先手压低"
    - mode: "Hot Zone"
      can_fulfill:
        - "开阔图长线压区"
        - "20+ 蛾减速拖回区者"
        - "Hyper 毛毛虫干扰站区 body"
      cannot_fulfill:
        - "闭合墙图的近距离自保"
        - "主站区 body"
      needs_teammate_support:
        - "实际站区 body"
        - "反 dive 与墙后投掷处理"
      false_positive: "Hot Zone 适配高度依赖地图；Ring of Fire 开阔可用，Parallel Plays 闭合会暴露低机动和低血"
    - mode: "Gem Grab"
      can_fulfill:
        - "远程标记敌方 carrier"
        - "保护己方 carrier 的防守火力"
        - "20+ 蛾 Super 减速撤退线"
      cannot_fulfill:
        - "主 carrier"
        - "被多路 dive 时的自保"
      needs_teammate_support:
        - "真正拿宝石的 carrier"
        - "反刺客前排"
      false_positive: "Fandom 明确说 Vince 擅长杀 carrier 和防守，但自己是差 carrier；不能把击杀能力写成持宝能力"
    - mode: "Bounty"
      can_fulfill:
        - "长线 chip 与 Super 标记"
        - "防守星差时的远程减速"
        - "Bug Bandage 续航变体"
      cannot_fulfill:
        - "稳定首发开火权"
        - "被 dive 时的自保"
      needs_teammate_support:
        - "前排 peel"
        - "更稳定的远程首手"
      false_positive: "Bounty 未出现在 PLP 推荐模式中；Vince 的 8.33 格射程和慢启动使他更像后手防守，而不是稳定星源"
    - mode: "Brawl Ball"
      can_fulfill:
        - "远程补伤和 Super 减速"
        - "防守门前 choke"
      cannot_fulfill:
        - "主 scorer 或持球推进"
        - "近距离反突进"
      needs_teammate_support:
        - "scorer 与 wallbreak"
        - "强 anti-dive 前排"
      false_positive: "Fandom 把 Brawl Ball 列为高强化模式下的弱项；Vince 没有位移和进球工具，不能当 ball handler"
    - mode: "Heist"
      can_fulfill:
        - "防守端用长线标记压入库者"
        - "Hot Coffee 清墙后残血"
      cannot_fulfill:
        - "对 Safe 的稳定伤害（Super 对 Safe 无效）"
        - "主 safe race"
      needs_teammate_support:
        - "真正 safe DPS"
        - "前排与反 dive"
      false_positive: "Fandom 明确把 Heist 列为 Vince 的弱项；把 Super 标记当成 safe 伤害是机制误读"

  failure_modes:
    - id: "slow_start_before_10_moths"
      active_when: "Vince 在 0-9 蛾阶段被迫接团，Super 只有 1-3 发且普攻标记增伤不足"
      exposed_by: "Fandom Super stages at 5/10/20 moths and low base damage"
      mitigation: "用防守站位和队友视野拖到 10 蛾，再决定是否用 Super 开团；不要把低收藏 Super 当爆发"
      bp_use: "resource_threshold_gate"
    - id: "death_halves_moths"
      active_when: "Vince 被刺客或长线先手击杀，死亡损失 50% 收藏并重置 10/20 阈值"
      exposed_by: "Trait loses 50% moths on defeat, rounded down"
      mitigation: "优先 Shield/Healing 与队友 peel；用 20+ 蛾的额外收藏做缓冲，避免把全部资源压在一次推进"
      bp_use: "stockpile_risk_check"
    - id: "ammo_competition_collection"
      active_when: "Vince 需要同时用弹药清线、收集毛毛虫和打 Super 标记，导致收藏或输出其中一项断档"
      exposed_by: "Fandom tips: ammo is used for offence and caterpillar collection"
      mitigation: "用 Metamothosis 一次收取多只，或站位让一发普攻同时命中敌人和毛毛虫"
      bp_use: "resource_tracking.ammo_vs_collection"
    - id: "hyper_only_self_peel"
      active_when: "敌方 dive 在 Vince 没有 Hypercharge 时进场；Vince 无位移，只能靠队友或 Hot Coffee 反打"
      exposed_by: "no mobility tool; Hyper caterpillars are the main anti-aggro resource"
      mitigation: "保留 Hyper 或前排 peel；不要把 4 只毛毛虫当成常驻护盾"
      bp_use: "draft_requires_peel"
    - id: "summon_absorbs_super_mark"
      active_when: "敌方用 porter、turret、hatchling 等召唤物挡在 Vince 与真实目标之间"
      exposed_by: "Fandom: Super mark cannot bounce from summons and is absorbed by them"
      mitigation: "先清召唤物或换角度；不要把 20+ 蛾 Super 浪费在 body-block 上"
      bp_use: "false_positive_filter.spawnable_block"

  conditional_matchups:
    - target: ["Lumi", "Meeple", "Otis", "Griff", "Maisie", "Penny", "Bo", "Pearl"]
      direction: "subject_favored"
      source: "[[sources/PLP-Vince|PLP-Vince]]"
      mechanism: "Vince 的长线普攻与 Super 标记能惩罚中距离站位和固定目标；10+ 蛾后的弹射与 20+ 蛾减速会压缩他们的撤退路线"
      active_when: "Vince 已叠到 10+ 蛾，敌方必须经过可预判直线或站在目标点附近"
      fails_when: "Vince 在低收藏阶段被先手，或敌方用召唤物/墙体吸收 Super"
      bp_use: "stockpile_range_response"
    - target: ["Cordelius", "Mortis", "Damian", "El Primo"]
      direction: "target_favored"
      source: "[[sources/PLP-Vince|PLP-Vince]]"
      mechanism: "直接 dive、暗影领域或跳墙进场绕过 Vince 的收藏节奏，贴上后低血无位移本体很难自保"
      active_when: "敌方有墙草接近路线，Vince 没 Hyper 或队友 peel，且收藏未到 10 蛾"
      fails_when: "Vince 提前叠到 20 蛾、Hyper 毛毛虫挡路，或队友控制先打断进场"
      bp_use: "avoid_without_peel"
    - target: ["Amber", "8-Bit", "Pierce", "Sirius"]
      direction: "target_favored"
      source: "[[sources/PLP-Vince|PLP-Vince]]"
      mechanism: "更稳定或更长的持续火力在 Vince 叠收藏前压血；Amber 火线、8-Bit 持续 DPS、Pierce 弹壳循环会逼 Vince 放弃收集"
      active_when: "地图是长线或半开阔，Vince 必须暴露在火力下才能收毛毛虫"
      fails_when: "Vince 有墙后安全收集位，或队友先压退长手"
      bp_use: "avoid_open_lane_without_cover"

  slot_notes:
    slot_1: "不建议盲先手；Vince 的低收藏阶段和零位移会被敌方第一轮 draft 直接针对。"
    slot_2_3: "只在 Knockout/开阔 Hot Zone 且队友能保护收集路线时作为防守核心，后续补站区或反 dive。"
    slot_4_5: "看到敌方中距离、固定目标或缺乏 dive 时可响应；同时检查敌方是否还有 Cordelius/Mortis/Damian 这类最后手。"
    slot_6: "最适合作为反制敌方无 dive 长线阵容的最后一手，用 20+ 蛾标记和 Hyper 毛毛虫封住正面推进。"
```

## 关联页面

- [[sources/Fandom-Vince|Fandom 来源摘要: Vince]]
- [[sources/PLP-Vince|PLP 来源摘要: Vince]]
