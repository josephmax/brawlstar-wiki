# Mandy

## 基本信息

- 稀有度：Epic
- 定位：Marksman
- 类型：专注超远程狙击 / 直线斩杀

## 来源摘要

- Fandom：[[sources/Fandom-Mandy|Fandom 来源摘要: Mandy]]
- PLP：[[sources/PLP-Mandy|PLP 来源摘要: Mandy]]
- PLP 推荐模式：Bounty, Knockout

## 角色定位总结

Mandy 的 BP 价值来自 12 格 Focus 射程、In My Sights 的弹速修正、Cookie Crumbs 的墙后惩罚，以及 Sugar Ray 的超长直线收割。她适合把 Bounty/Knockout 的“先拿空间、逼对手分散、在窄线里一枪改局”做极致；弱点是专注需要站定，Super 可被打断，且 3000 HP 对刺客和高压长线都很脆。

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
    effective_range: "very_long; 9 格基础射程，站定 0.45 秒后 Focus 到 12 格，Super 40 格穿墙直线"
    projectile_reliability: "medium_high_with_in_my_sights; Focus 弹速星徽提高命中，未专注或被迫移动时可靠性下降"
    burst: "high_pick_burst; Power 11 普攻单发 2800，未带盾/减伤的基础血量 <=5600 为两发线、<=8400 为三发线；Sugar Ray 直线伤害可跨屏收割或逼退低血"
    sustained_dps: "medium; 1.5 秒装填和单发节奏，适合稳定换血而非近距离持续战"
    objective_damage: "conditional_heist_lane; Safe Zone 等直线角度可用 Super 打 safe，但不是 PLP 主模式"
    mobility: "low; 专注和 Super 都要求站位纪律"
    survivability: "low_medium_conditional; Power 11 本体 6000 HP，Hard Candy Focus 状态按 50% 减伤为 12000 EHP，叠满 Shield gear 为 13800；移动会立刻失去 Focus 与该承伤线"
    engage: "low; 主要通过射程先手压线，不主动进场"
    disengage: "low_medium; Caramelize 可拖接近，但没有位移"
    anti_aggro: "low; 贴脸后只能靠 slow、队友和提前击杀"
    anti_tank: "medium_on_open_lanes; 长线能消耗前排，近身后会崩"
    wall_break: "none"
    throw_or_wall_bypass: "high_for_pick; Cookie Crumbs 下一发穿墙，Super 天然穿透墙体/敌人"
    area_control: "medium; Super 直线威慑窄口和撤退线，但没有持续地面控制"
    scouting_or_vision: "medium_with_vision_gear; 长线和 Vision gear 可跟踪草后撤退目标"
    team_support: "low; 通过长线压制间接保护队友"
    crowd_control: "conditional; Caramelize 下一发提供 2.5 秒 slow"

  build_switches:
    - build: "Cookie Crumbs / In My Sights / Shield, Damage"
      source: "[[sources/PLP-Mandy|PLP-Mandy]]"
      changes_capabilities:
        - "把墙后残血、掩体后复位和 Knockout 缩圈前躲墙目标纳入击杀线"
        - "In My Sights 修正 Focus 弹速，是默认远程可靠性来源"
      enables:
        - "Bounty/Knockout 中穿墙收割和远程对狙"
      mitigates_failure_modes:
        - "wall_cover_breaks_line"
        - "low_health_needs_extra_survival"
      best_when: "地图有长线和少量墙体，敌方会用掩体回避 Mandy 射线"
      poor_when: "敌方有稳定 dive、Buster 屏障或水域/off-angle 长手压 Mandy"
      bp_use: "default_plp_sniper_build"
    - build: "Caramelize / In My Sights / Shield, Vision"
      source: "[[sources/Fandom-Mandy|Fandom-Mandy]]"
      changes_capabilities:
        - "把单发从纯伤害改成反接近和窄口控制"
      enables:
        - "开阔图减速前排、迫使突进者交资源、追踪草后撤退"
      mitigates_failure_modes:
        - "focused_immobility_dive_window"
      best_when: "敌方需要经过开阔窄口接近，且我方已有穿墙/收割手段"
      poor_when: "敌方主要躲在墙后，Mandy 需要 Cookie Crumbs 打掩体后目标"
      bp_use: "anti_approach_variant"
    - build: "Cookie Crumbs or Caramelize / Hard Candy / Shield"
      source: "[[sources/Fandom-Mandy|Fandom-Mandy]]"
      changes_capabilities:
        - "Hard Candy 在 Mandy 保持 Focus 时提供 50% shield，把可预判的单线换血变成更耐久的静态长线锚点"
        - "放弃 In My Sights 会失去 Focus 弹速修正，因此耐久提升不等于命中可靠性提升"
      enables:
        - "在固定长线或回合末 choke 中持有 Focus 并承受一次远程换血"
      mitigates_failure_modes:
        - "focused_immobility_dive_window"
      best_when: "敌方压力来自可预判的单线远程伤害，Mandy 能在安全掩体后保持 Focus"
      poor_when: "敌方用投掷、侧角、持续区域伤害或 dive 强迫 Mandy 移动，护盾会随 Focus 一起消失"
      bp_use: "conditional_focus_hold_variant_not_default_projectile_build"

  map_feature_hooks:
    - id: "bounty_open_sightline_star_pick"
      map_feature_type: "open_sniper_bounty"
      uses_feature_by: "Focus 12 格和 In My Sights 在开阔长线低承诺换血，Sugar Ray 惩罚直线站位"
      objective_conversion: "先拿星或血量优势后，Mandy 可以用射程保星并压制落后方进场"
      active_when: "地图主矛盾是长线对枪，敌方缺强突进或墙后口袋"
      fails_if: "敌方投掷口袋完整、墙体遮断长线，或 Mandy 被迫频繁移动导致不能 Focus"
      example_maps: ["[[entities/maps/Shooting Star|Shooting Star]]", "[[entities/maps/Dry Season|Dry Season]]", "[[entities/maps/Hideout|Hideout]]", "[[entities/maps/Layer Cake|Layer Cake]]"]
      bp_use: "Bounty 长线核心或回答短手前排"
    - id: "knockout_round_end_sugar_ray_choke"
      map_feature_type: "knockout_choke_and_round_close"
      uses_feature_by: "保留 Super，在缩圈、窄口或低血撤退线上跨屏穿墙收割"
      objective_conversion: "Knockout 中一发 Sugar Ray 可把空间优势转成不可复活击杀"
      active_when: "敌方必须经过可预判直线，或低血躲在墙后"
      fails_if: "Super 被 stun/knockback/pull 打断，或敌方分散不给直线"
      example_maps: ["[[entities/maps/Out in the Open|Out in the Open]]", "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]", "[[entities/maps/New Horizons|New Horizons]]", "[[entities/maps/Belle's Rock|Belle's Rock]]"]
      bp_use: "Knockout 终结窗口；需要队友给视野或逼路线"
    - id: "cookie_crumbs_wall_pick_or_recovery_punish"
      map_feature_type: "limited_wall_pick"
      uses_feature_by: "Cookie Crumbs 穿墙补掉躲墙目标，迫使投掷/低血远程不能安全复位"
      objective_conversion: "拆掉敌方用墙体保命的习惯后，长线阵容可继续推进空间"
      active_when: "墙体数量有限且目标会在固定墙后回位"
      fails_if: "敌方有持续投掷压 Mandy，或 Buster/屏障类工具吃掉直线"
      example_maps: ["[[entities/maps/Belle's Rock|Belle's Rock]]", "[[entities/maps/Layer Cake|Layer Cake]]", "[[entities/maps/Gem Fort|Gem Fort]]"]
      bp_use: "回答墙后低血，不等于处理完整投掷体系"
    - id: "heist_cross_map_sugar_ray_safe_angle"
      map_feature_type: "remote_safe_damage_angle"
      uses_feature_by: "在固定直线角度用 Sugar Ray 同时穿过防守位和 safe"
      objective_conversion: "补充低承诺金库伤害，或迫使敌方分散防线"
      active_when: "地图存在可重复对 safe 的直线，且 Mandy 不会被侧路 dive"
      fails_if: "safe 角度被河道/墙体错开，或敌方 Heist race 更快"
      example_maps: ["[[entities/maps/Safe Zone|Safe Zone]]", "[[entities/maps/Bridge Too Far|Bridge Too Far]]", "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"]
      bp_use: "Heist 附加角度，不作为主 safe DPS"

  objective_contracts:
    - mode: "Bounty"
      can_fulfill:
        - "开阔长线保星、穿墙收残、逼敌方分散"
      cannot_fulfill:
        - "处理多路近身或持续墙后投掷"
      needs_teammate_support:
        - "反刺客、开墙或探草队友"
      false_positive: "射程长不代表能无视投掷口袋和 dive"
    - mode: "Knockout"
      can_fulfill:
        - "第一波远程压血，缩圈前用 Super 结束回合"
      cannot_fulfill:
        - "独自守住被强开的侧路"
      needs_teammate_support:
        - "peel、视野、逼路线或补伤"
      false_positive: "Sugar Ray 需要直线和时机；敌方分散时威慑大于实际击杀"
    - mode: "Heist"
      can_fulfill:
        - "特定直线角度打 safe 或穿过防守位"
      cannot_fulfill:
        - "承担持续 safe race"
      needs_teammate_support:
        - "主 safe DPS、侧路防突进"
      false_positive: "不能因为 Super 可打库就把 Mandy 当 Heist 核心"

  failure_modes:
    - id: "focused_immobility_dive_window"
      active_when: "Mandy 为了 12 格射程站定，敌方用 dash、jump、侧草或水域 off-angle 接近"
      exposed_by: "Focus requires standing still; low HP"
      mitigation: "保留 Caramelize、队友 peel、选择开阔可视路线；Hard Candy 的 50% Focus shield 只缓解可预判换血，不能解决被迫移动或贴脸"
      bp_use: "check_enemy_engage_before_pick"
    - id: "super_cancelled_by_cc"
      active_when: "敌方有 stun、pull、knockback 或快速贴身打断 0.75 秒前摇"
      exposed_by: "Sugar Ray can be cancelled by stun/pull/knockback"
      mitigation: "在草外安全位、队友控线后开 Super"
      bp_use: "do_not_rely_on_super_when_interrupts_are_live"
    - id: "wall_pocket_thrower_or_barrier_screen"
      active_when: "敌方投掷安全口袋完整，或 Buster 屏障/召唤物吸收直线"
      exposed_by: "linear marksman kit with limited anti-pocket tools"
      mitigation: "Cookie Crumbs 只补单点，队伍仍需开墙/突进/反投掷"
      bp_use: "must_answer_wall_pocket"
    - id: "enemy_spreads_no_lineup"
      active_when: "敌方分散站位且不给 Super 直线"
      exposed_by: "Sugar Ray is line-based"
      mitigation: "用长线先压血，等待 choke/缩圈/目标线"
      bp_use: "avoid_overvaluing_multi_hit_super"

  conditional_matchups:
    - target: ["El Primo", "Jacky", "Frank", "Clancy"]
      direction: "subject_favored"
      source: "[[sources/PLP-Mandy|PLP-Mandy]]"
      mechanism: "开阔长线让 Mandy 在前排接近前反复压血，Caramelize 可拖慢最后接近"
      active_when: "地图缺连续掩体，队友能阻止前排直接贴脸"
      fails_when: "目标通过草墙/跳板/队友控制接近 Mandy"
      bp_use: "anti_frontline_on_open_maps"
    - target: ["Meg", "Poco", "Lola", "Chuck"]
      direction: "subject_favored"
      source: "[[sources/PLP-Mandy|PLP-Mandy]]"
      mechanism: "Mandy 射程和 Super 能惩罚中距离支援、召唤/身体推进或固定路线"
      active_when: "目标需要走直线或站在可预判路线里输出/支援"
      fails_when: "目标获得墙体保护，或能用队友强开解除 Mandy 距离"
      bp_use: "pick_into_predictable_midrange_or_route"
    - target: ["Angelo", "Eve", "Najia", "Pearl"]
      direction: "target_favored"
      source: "[[sources/PLP-Mandy|PLP-Mandy]]"
      mechanism: "水域/off-angle、长线对狙或高压单发会让 Mandy 站定 Focus 的窗口变危险"
      active_when: "地图允许这些目标从侧角或更安全长线压 Mandy"
      fails_when: "Mandy 有掩体、队友压住侧角，或 Cookie/Super 先拿击杀"
      bp_use: "avoid_blind_sniper_mirror"
    - target: ["Darryl", "Damian", "Buster", "Sprout"]
      direction: "target_favored"
      source: "[[sources/PLP-Mandy|PLP-Mandy]]"
      mechanism: "dive、屏障或墙后投掷能绕开或吸收 Mandy 的直线价值"
      active_when: "地图有墙体口袋、侧路突进或屏障推进"
      fails_when: "墙体被打开、突进路线被 slow/peel 控住"
      bp_use: "requires_peel_or_wallbreak_before_lock"

  slot_notes:
    slot_1: "只在开阔 Bounty/Knockout 且 ban 掉主要 dive/投掷回答时考虑"
    slot_2_3: "可作为长线基本面，但需要队伍后续补 peel 和墙体答案"
    slot_4_5: "看到敌方缺突进、缺投掷或站位直线后价值更高"
    slot_6: "惩罚无位移、固定路线、低血后排或前排过多的阵容"
```

## 关联页面

- [[sources/Fandom-Mandy|Fandom 来源摘要: Mandy]]
- [[sources/PLP-Mandy|PLP 来源摘要: Mandy]]

## 战斗断点输入

```json
{
  "combat_breakpoint_profile": {
    "schema": "brawler_breakpoint_profile.v1",
    "brawler": "Mandy",
    "target_states": [
      {
        "id": "body",
        "entity_class": "brawler_body",
        "roster_target": true,
        "health": {"amount": 3000, "at_power_level": 1, "scaling": "standard"},
        "source_ref": "[[sources/Fandom-Mandy|Fandom-Mandy]]"
      }
    ],
    "damage_packets": [
      {
        "id": "main.impact",
        "ability_kind": "main_attack",
        "packet_unit": "impact",
        "delivery_variant": "impact",
        "repeat_model": "identical",
        "damage": {"amount": 1400, "at_power_level": 1, "scaling": "standard"},
        "active_when": "单枚普攻命中；Focused 只改变射程，不改变此伤害",
        "source_conflict_status": "none",
        "source_ref": "[[sources/Fandom-Mandy|Fandom-Mandy]]"
      }
    ],
    "defense_modifiers": [
      {
        "id": "hard_candy",
        "source_kind": "star_power",
        "loadout_group": "star_power",
        "applies_to_states": ["body"],
        "effect": {"type": "damage_reduction", "ratio": 0.50},
        "active_when": "Mandy 保持 Focus",
        "sequence_validity": "开始移动并失去 Focus 时立即失效",
        "source_ref": "[[sources/Fandom-Mandy|Fandom-Mandy]]"
      }
    ]
  }
}
```
