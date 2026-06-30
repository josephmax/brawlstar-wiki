# Eve

## 基本信息

- 稀有度：Mythic
- 定位：Damage Dealer
- 类型：水域路线 / 超远程压线 / hatchling 召唤物骚扰

## 来源摘要

- Fandom：[[sources/Fandom-Eve|Fandom 来源摘要: Eve]]
- PLP：[[sources/PLP-Eve|PLP 来源摘要: Eve]]
- PLP 推荐模式候选：Heist, Bounty, Knockout

## 角色定位总结

Eve 的核心价值是“水域或障碍让她拥有别人没有的站位，同时用超远程普攻和 hatchling 迫使敌方交弹药/让位”。她不是普通投掷，也不是所有水图自动强；如果水域不能提供有效输出角度、逃生路线或目标压力，她只是一个低血量、慢 unload、怕突进的远程输出。

## 与其他英雄的区别

- 不同于 `Angelo`：Eve 的水域价值更依赖持续站位和 hatchling 压力，而不是单发蓄力爆发。
- 不同于 `Mr. P`：Eve 的召唤物来自巢蛋与 Star Power 触发，压制节奏更依赖放置距离和敌方清召唤物效率。
- 不同于 `Piper` / `Mandy`：Eve 的长线收益会被水域路线和召唤物放大，但正面对枪爆发和命中稳定性不等同于纯狙。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Eve|Fandom-Eve]] direct_raw_capture_2026-06-30-v2"
    plp: "[[sources/PLP-Eve|PLP-Eve]] direct_raw_capture_2026-06-30"
    user_notes: "本地 BP 规则要求水域能力必须绑定路线、目标收益和失效条件"

  capability_vector:
    effective_range: "very_long; 9.33 格普攻，适合长线消耗和隔水压制"
    projectile_reliability: "中等；三枚蛋有顺序和大小差异，Unnatural Order 提高第一发大蛋即时命中价值"
    burst: "中低；非贴脸爆发英雄，主要靠持续消耗和 hatchling 补压力"
    sustained_dps: "中等；Reload gear 可提高长线持续输出"
    objective_damage: "条件性；Heist 更偏低承诺压线和 hatchling 牵制，不是顶级 safe melt"
    mobility: "Trait 可在水上移动；Gotta Go 可跳墙/跳水域边缘并留下 hatchling"
    survivability: "低血量；水域可让短手无法触达，但怕远程、召唤物清理和强突进"
    engage: "弱直接 engage；通过水域站位和 hatchling 逼走位"
    disengage: "中等；水域站位和 Gotta Go 提供逃离角度"
    anti_aggro: "条件性强；大水域让普通短手无法接近，但没有水或被远程压制时很脆"
    anti_tank: "弱到中；可以用距离和 hatchling 消耗，但慢 unload 怕贴脸高爆发"
    wall_break: "无"
    throw_or_wall_bypass: "Super 可越过障碍放巢蛋；Gotta Go 可跳过墙"
    area_control: "中等；巢蛋和 hatchling 逼迫敌方清理或走位"
    scouting_or_vision: "hatchling 可间接探草/探位，但不是稳定 reveal"
    team_support: "Motherly Love 可把 hatchling 转为治疗，属于小范围条件支援"
    spawnable_or_pet: "强；Super、Happy Surprise、Hypercharge 都能制造 hatchling 压力"
    crowd_control: "无硬控；控制来自召唤物追击和站位压缩"
    terrain_creation: "无"
    terrain_destruction: "无"

  build_switches:
    - build: "Gotta Go / Unnatural Order / Quadruplets + Reload"
      source: "[[sources/PLP-Eve|PLP-Eve]] + [[sources/Fandom-Eve|Fandom-Eve]]"
      changes_capabilities:
        - "Gotta Go 提供保命跳跃和额外 hatchling，可在水域/墙边重置距离"
        - "Unnatural Order 让最大蛋先出，提高即时远程消耗和开枪威慑"
        - "Quadruplets 增加 Super hatchling 数量，Reload 提高长线持续压制"
      enables:
        - "水域图隔水站位"
        - "Heist/Bounty/Knockout 低承诺消耗"
        - "对单体远程制造 hatchling 清理税"
      mitigates_failure_modes:
        - "partially_mitigates_slow_unload"
        - "partially_mitigates_dive_through_reposition"
      best_when: "地图水域提供有效输出角度，敌方缺快速清 hatchling 或缺能跨水/强突进的答案"
      poor_when: "水域不影响主战场、敌方有 Penny/Sandy/Rosa/Bibi/Chuck 等能清召唤物或强进场的结构"
      bp_use: "水域长线先手、Heist/Bounty/Knockout 条件核心、anti-short-range route denial"
    - build: "Motherly Love / Happy Surprise"
      source: "[[sources/Fandom-Eve|Fandom-Eve]]"
      changes_capabilities:
        - "Motherly Love 把下一次 Super hatchling 改为治疗，服务站位续航"
        - "Happy Surprise 对单体远程增加额外 hatchling 清理税"
      enables:
        - "保护长线队友或热区/淘汰阵地"
      mitigates_failure_modes:
        - "partially_mitigates_low_team_sustain"
      best_when: "敌方缺 AoE 清理，且我方需要巢蛋提供队伍续航或持续骚扰"
      poor_when: "敌方能快速摧毁巢蛋或用范围伤害免费清 hatchling"
      bp_use: "build branch；不是默认竞技推荐，但可解释特定阵容的支援价值"

  map_feature_hooks:
    - id: "water_crossing_with_range"
      map_feature_type: "river_crossing"
      example_maps:
        - "[[entities/maps/Safe Zone|Safe Zone]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      route_or_position: "站在水域或跨水绕到普通英雄无法站住的位置，用 9.33 格射程继续压线"
      objective_conversion: "Safe Zone / Safe(r) Zone 可绕过普通路线限制并形成远程打库或防守角度；New Horizons 可从角落水域制造非正面压力"
      active_when: "水域位置能影响金库、长线对枪或 Knockout 空间，且敌方不能同样跨水追击"
      fails_if: "水域只在边角且不能影响主战场，或敌方有更强远程/跨水/突进答案"
      bp_use: "map_factor_fit；同时触发 false_positive_filter，不能把 water_crossing 单独加分"
    - id: "long_range_hatchling_tax"
      map_feature_type: "long_sightline_plus_spawnable"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"
      route_or_position: "长线低承诺消耗，巢蛋放在敌方必须清理但不容易无损处理的位置"
      objective_conversion: "Bounty/Knockout 中迫使敌方交弹药清 hatchling，从而降低其换血或进场节奏"
      active_when: "敌方是单体远程、清召唤物效率低、且 Eve 能保持距离"
      fails_if: "敌方有 Penny/Sandy/Rosa/Lumi 等范围清理，或能直接突破 Eve 慢 unload"
      bp_use: "回答纯长线和单体狙；也可作为 ban/pick 的召唤物税判断"
    - id: "safe_zone_remote_and_water_angle"
      map_feature_type: "objective_access"
      example_maps:
        - "[[entities/maps/Safe Zone|Safe Zone]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
      route_or_position: "利用水域/长线绕开普通步行路线，保持远程压力而不是贴脸进库"
      objective_conversion: "Heist 中提供低承诺路线权和召唤物牵制，帮助队友争取 safe DPS 时间"
      active_when: "长线或跨水站位能持续影响金库路线，队友有真正 safe damage"
      fails_if: "需要 Eve 独自承担主要 safe melt，或三路隔离导致她无法支援崩线队友"
      bp_use: "Heist 条件适配；需要队友补 sustained safe DPS"
    - id: "anti_short_range_lake_anchor"
      map_feature_type: "short_range_denial"
      example_maps:
        - "[[entities/maps/Safe Zone|Safe Zone]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
        - "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"
      route_or_position: "站在足够大的水域或水域边缘，让 Edgar/Mortis/El Primo/Mico 类普通短手无法直接触达"
      objective_conversion: "把敌方进场路线变成绕路或交位移，从而保护长线站位"
      active_when: "水域足够大且 Eve 不需要离开水域去拿目标"
      fails_if: "敌方有跳跃/钩子/隐身/长线 burst，或目标逼迫 Eve 离开水域"
      bp_use: "anti-aggro 条件边；不能泛化到所有地图"

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - "water_route_lane_control"
        - "remote_angle_pressure"
        - "hatchling_distraction_for_safe_race"
      cannot_fulfill:
        - "单独承担高速拆库主 DPS"
        - "在无水/无长线角度时强行走短路进库"
      needs_teammate_support:
        - "真正 sustained safe DPS"
        - "能守住敌方反推路线的防守点"
      false_positive: "可过水如果不能形成打库角度或防守收益，就不是强适配"
    - mode: "Bounty"
      can_fulfill:
        - "low_commitment_poke"
        - "single_target_hatchling_tax"
        - "water_or_range_survival_space"
      cannot_fulfill:
        - "快速连杀或强制开团"
        - "在被突进贴脸后独立自保"
      needs_teammate_support:
        - "反突进 peel"
        - "能开墙或保护长线的队友"
      false_positive: "长线图也要看敌方清 hatchling 和突进能力"
    - mode: "Knockout"
      can_fulfill:
        - "space_control_from_water_angle"
        - "巢蛋逼迫敌方交弹药"
        - "残局远程压血"
      cannot_fulfill:
        - "硬开团或稳定收割"
        - "墙被打开后抗住高机动强切"
      needs_teammate_support:
        - "开墙/反突进/补斩杀"
      false_positive: "如果水域不影响中心空间，Eve 只是低血长手，优先级下降"

  failure_modes:
    - id: "slow_unload_into_dive"
      active_when: "敌方 Edgar/Leon/Mortis/Crow/Kenji/Buzz/Mico 等能跨过距离或绕过水域"
      exposed_by: "[[sources/Fandom-Eve|Fandom-Eve]] 提到 Eve 慢 unload 且怕高 burst 贴脸"
      mitigation: "选择有足够水域、队友 peel 或 Gotta Go 可撤的地图"
      bp_use: "must_avoid / needs_protection"
    - id: "water_without_objective_pressure"
      active_when: "候选地图只有边角水域，不能影响 safe、星差、中心空间或 gem route"
      exposed_by: "[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]] 的 water false positive 规则"
      mitigation: "要求水域站位能转化为目标访问、低承诺输出或撤退安全"
      bp_use: "map_factor_false_positive_check"
    - id: "hatchlings_cleared_for_free"
      active_when: "敌方有范围伤害、炮台、召唤物、穿透或站位可无损清巢蛋"
      exposed_by: "[[sources/Fandom-Eve|Fandom-Eve]] 巢蛋需 5 秒孵化，提前被摧毁则无 hatchling"
      mitigation: "巢蛋放置在敌方必须走位处理的位置，或只作为消耗弹药工具"
      bp_use: "candidate_eval.spawnable_value"
    - id: "low_health_long_range_mirror"
      active_when: "敌方长线命中更稳定且可以越过 hatchling 直接打 Eve"
      exposed_by: "Eve 血量 3100，长线对枪容错低"
      mitigation: "利用水域角度和队友火力交叉，而不是纯正面对狙"
      bp_use: "must_avoid_against_sniper_core"

  conditional_matchup_seeds:
    - target: ["Piper", "Mandy", "Bea", "Bonnie", "Byron"]
      direction: "subject_favored"
      source: "[[sources/PLP-Eve|PLP-Eve]] + [[sources/Fandom-Eve|Fandom-Eve]]"
      mechanism: "Eve 用水域站位和 hatchling 清理税干扰单体远程的低承诺换血"
      active_when: "地图提供水域/侧角，敌方缺范围清召唤物，Eve 不需要正面吃完整狙击线"
      fails_when: "地图纯开阔无水域价值，目标命中更稳定，或敌方队友能免费清 hatchling"
      bp_use: "response to single-target marksman；不是无条件狙击 counter"
    - target: ["Shelly", "Meg", "Rosa", "El Primo", "Mortis", "Edgar"]
      direction: "volatile"
      source: "[[sources/PLP-Eve|PLP-Eve]] + [[sources/Fandom-Eve|Fandom-Eve]]"
      mechanism: "足够大的水域让普通短手难以触达 Eve，但一旦离水或被强进场贴脸，Eve 慢 unload 会失效"
      active_when: "水域直接参与主战场，短手没有跳跃/钩子/隐身或队友开路"
      fails_when: "短手拥有跨距手段、草墙逼迫 Eve 离水、或目标模式要求 Eve 站到陆地"
      bp_use: "map-dependent anti-aggro；BP 输出必须引用具体地图 feature"
    - target: ["Penny", "Sandy", "Rosa", "Bibi", "Chuck", "Lumi", "Alli"]
      direction: "target_favored"
      source: "[[sources/PLP-Eve|PLP-Eve]]"
      mechanism: "这些英雄通过范围清理、持续压迫、强进场或路线改写降低 Eve 的水域/召唤物收益"
      active_when: "他们能接触巢蛋、清 hatchling，或逼 Eve 离开安全水域"
      fails_when: "地图水域隔绝他们的主路线，或队友压制使其不能追 Eve"
      bp_use: "enemy_response_prediction / must_avoid"
    - target: ["Grom", "Rico", "Jessie"]
      direction: "volatile"
      source: "[[sources/PLP-Eve|PLP-Eve]]"
      mechanism: "Eve 可用水域/长线避免部分常规路线，但这些英雄也可能通过特殊弹道、弹墙或炮台清理 hatchling"
      active_when: "Eve 有隔水角度且不会被弹墙/炮台逼离"
      fails_when: "墙体角度让对方绕过水域打到 Eve，或召唤物被快速清掉"
      bp_use: "map geometry check before accepting PLP seed"

  slot_notes:
    slot_1: "只在地图水域/长线是硬职责且敌方低成本答案被 ban 时可早手；否则容易被后手范围清理或突进惩罚"
    slot_2_3: "适合回答敌方短手或单体远程，但要补队友 peel 和 safe DPS / 斩杀"
    slot_4_5: "在已知敌方缺跨水答案或清 hatchling 时提高价值；同时要防 slot_6 补强突进"
    slot_6: "可作为地图特化最后手，确认水域直接影响目标且敌方剩余池无法高效追击/清召唤物"
```

## 关联页面

- [[sources/Fandom-Eve|Fandom 来源摘要: Eve]]
- [[sources/PLP-Eve|PLP 来源摘要: Eve]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
