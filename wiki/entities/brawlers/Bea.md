# Bea

## 基本信息

- 稀有度：Epic
- 定位：Marksman
- 类型：单发长线、Supercharged 节奏、slow 反冲脸

## 来源摘要

- Fandom：[[sources/Fandom-Bea|Fandom 来源摘要: Bea]]
- PLP：[[sources/PLP-Bea|PLP 来源摘要: Bea]]
- PLP 推荐模式：Brawl Ball、Hot Zone

## 角色定位总结

Bea 是用 10 格单发和 Supercharged 下一发建立威慑的 Marksman。她只有 1 格 ammo，命中敌方 Brawler 或 event boss 才会给下一发充能；命中 safe、IKE、箱子或召唤物不会充能。Super `Iron Hive` 以 7 枚无人机造成伤害和 3 秒 slow，适合让下一发更容易命中并阻止坦克推进。PLP 默认 `Rattled Hive / Honeycomb / Shield, Damage`，强化远距离墙后扫射和 Supercharged 时的 30% shield。BP 里 Bea 是开阔长线和反坦线的节奏点，但低血、单发、无位移让她非常吃保护。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "very_long_single_shot; 普攻 10 格，Super wide cone 辅助 slow"
    projectile_reliability: "medium_high_on_open_lane_medium_low_vs_dash; 单发命中决定节奏，Super slow 后更稳定"
    burst: "high_if_supercharged_hits; 普通 800，Supercharged 2200，miss 后节奏断"
    sustained_dps: "low_medium; reload 0.9 秒但只有 1 ammo，不能持续泼射"
    objective_damage: "low_heist; 打 safe/召唤物不充能，目标伤害不稳定"
    mobility: "low; 无位移"
    survivability: "low_medium; 2800 HP，Honeycomb 在 Supercharged 持有时给 30% shield"
    engage: "low; 靠长线压制和 slow 开窗口，不主动开团"
    disengage: "medium_with_super_or_honey_molasses; Super/Honey Molasses slow 可阻止追击"
    anti_aggro: "medium_high_if_slow_ready; slow 和高伤 Supercharged 惩罚坦克，但怕被先手贴脸"
    anti_tank: "high_on_open_lane; slow + Supercharged 单发持续威胁高血量推进"
    wall_break: "none"
    throw_or_wall_bypass: "gadget_only; Rattled Hive 蜜蜂可越墙，普攻不能"
    area_control: "medium; slow cone 和 Honey Molasses 可控 chokepoint"
    scouting_or_vision: "medium; Super cone 和 Rattled Hive 可探草/墙后"
    team_support: "medium; slow 让队友跟伤并保护长线"
    spawnable_or_pet: "honey_molasses_beehive; slow puddle 由 1000 HP hive 维持且衰减"
    crowd_control: "high_slow; Super 和 Honey Molasses 都能 slow"
    source_trace:
      - "[[sources/Fandom-Bea|Fandom-Bea]]"
      - "[[sources/PLP-Bea|PLP-Bea]]"

  build_switches:
    - build: "Rattled Hive / Honeycomb / Shield, Damage"
      source: "[[sources/PLP-Bea|PLP-Bea]]"
      changes_capabilities:
        - "Rattled Hive 4 只蜜蜂向外旋转，距离越远伤害越高，可越墙探草/打 thrower"
        - "Honeycomb 让 Bea 持有 Supercharged 时获得 30% shield，提高长线对枪容错"
        - "Shield/Damage gear 补低血和一发高伤窗口"
      enables:
        - "Brawl Ball 长线 slow 后收球路"
        - "Hot Zone 开阔入口反坦"
        - "墙后/草后远距离扫射"
      mitigates_failure_modes:
        - "low_health_one_ammo_pressure"
        - "supercharged_window_too_fragile"
      best_when: "地图有开阔长线，队友能保护 Bea 不被第一时间贴脸"
      poor_when: "敌方有多刺客/传送/高速草路，或地图墙太多导致普攻线断"
      bp_use: "default_plp_long_lane_build"
    - build: "Honey Molasses / Insta Beaload variant"
      source: "[[sources/Fandom-Bea|Fandom-Bea]]"
      changes_capabilities:
        - "Honey Molasses 4 格 slow puddle 可放墙后控制 chokepoint 或紧急防身"
        - "Insta Beaload 给 miss 的 Supercharged shot 一次第二机会"
      enables:
        - "固定入口反推进"
        - "提高关键高伤单发稳定性"
      mitigates_failure_modes:
        - "supercharged_miss_loses_tempo"
        - "assassin_crosses_open_lane"
      best_when: "地图 chokepoint 明确，队伍需要 slow 区而不是 Rattled Hive poke"
      poor_when: "敌方可快速打掉 hive，或 Bea 更需要 Honeycomb shield 存活"
      bp_use: "choke_control_or_accuracy_variant"

  map_feature_hooks:
    - id: "brawl_ball_super_slow_and_supercharge_hold"
      map_feature_type: "ball_lane_slow_and_long_shot"
      uses_feature_by: "Super cone slow 让持球者/守门人减速，Bea 保持 Supercharged 单发威胁"
      route_or_position: "Brawl Ball 中路长线、门前退防线、侧路持球推进线"
      objective_conversion: "阻止冲门、逼掉球或让队友跟伤收门前目标"
      active_when: "球路经过开阔射线，Bea 有保护者挡住刺客侧切"
      fails_if: "敌方从草/墙后先手贴 Bea，或她把 Supercharged 打在非英雄目标上断节奏"
      example_maps:
        - "[[entities/maps/Backyard Bowl|Backyard Bowl]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_slow_and_long_lane_pick"
    - id: "hot_zone_honeycomb_long_lane_slow"
      map_feature_type: "zone_open_lane_anti_tank"
      uses_feature_by: "10 格普攻、Super slow 和 Honeycomb shield 让 Bea 在开阔区口惩罚坦克进区"
      route_or_position: "Hot Zone 开阔入口、区边长线、敌方回区路径"
      objective_conversion: "阻止高血量 body 进区，或把其压低交给队友"
      active_when: "区口不是完全墙后，Bea 能连续看见进区目标"
      fails_if: "敌方 thrower/assassin 从墙后绕开长线，或 speed boost 直接越过 slow 窗口"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.open_zone_anti_tank_lane"
    - id: "open_lane_supercharged_pick"
      map_feature_type: "very_long_lane_single_shot_pick"
      uses_feature_by: "命中英雄后保留 Supercharged 高伤下一发，逼长线目标不能轻易 peek"
      route_or_position: "Bounty/Knockout 长线、Gem Grab 侧线、开阔中线"
      objective_conversion: "制造 first pick、压退低血长手、保护 objective 线"
      active_when: "目标必须在开阔处露头，且 Bea 有队友处理近身路线"
      fails_if: "地图墙体太多，目标用召唤物/安全目标吸收普通命中，或 Bea 死亡丢失充能"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Hideout|Hideout]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "candidate_eval.long_lane_supercharged_pick"
    - id: "rattled_hive_wall_thrower_or_bush_check"
      map_feature_type: "wall_or_bush_long_distance_gadget_check"
      uses_feature_by: "Rattled Hive 越墙飞行并随距离增伤，可扫墙后 thrower 或检查草后目标"
      route_or_position: "墙后投掷位、草边、Hot Zone/Brawl Ball 侧路"
      objective_conversion: "逼墙后目标换位、揭示草中 ambush、为下一发 Supercharged 创造射线"
      active_when: "Bea 可从安全距离释放完整 gadget，目标无法在蜜蜂释放前打断她"
      fails_if: "蜜蜂被墙/目标站位规避，或 Bea 在释放中被 stun/pull/knockback"
      example_maps:
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
      bp_use: "map_bp_factors.wall_bush_gadget_check"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "Super slow 阻止持球推进"
        - "Supercharged 单发打低守门/进攻者"
        - "长线保护中路"
      cannot_fulfill:
        - "主 scorer"
        - "独自防草内刺客"
      needs_teammate_support:
        - "近身保护、持球者、破墙/清草"
      false_positive: "Bea 的 slow 很强，但她没有位移；门前被贴脸时不能单独守球"
    - mode: "Hot Zone"
      can_fulfill:
        - "开阔区口反坦"
        - "Super slow 和 Honey Molasses 控入口"
        - "Supercharged 高伤压低 body"
      cannot_fulfill:
        - "单人站区承伤"
        - "墙后 thrower 对抗"
      needs_teammate_support:
        - "站区者、反刺客、草区侦测"
      false_positive: "Hot Zone 价值来自开阔射线；墙多或刺客侧路开放时需要换人或补保护"

  failure_modes:
    - id: "one_ammo_low_health_no_escape"
      active_when: "敌方刺客/高速坦克从草或墙后先手贴 Bea"
      exposed_by: "[[sources/Fandom-Bea|Fandom-Bea]] low health, one ammo, no escape tips"
      mitigation: "配 close-range protector，保留 Super/Honey Molasses，避免无视野侧路"
      bp_use: "draft_requires_bodyguard"
    - id: "supercharge_requires_brawler_hit"
      active_when: "Bea 把命中打在 safe、IKE、箱子、召唤物或小兵上，下一发没有 Supercharged"
      exposed_by: "Fandom notes only enemy Brawlers/event bosses charge the next shot"
      mitigation: "BP 中不要把她当 Heist/objective DPS；长线优先找英雄命中"
      bp_use: "objective_damage_false_positive_filter"
    - id: "supercharged_miss_or_death_loses_tempo"
      active_when: "Supercharged shot miss，或 Bea 死亡导致充能消失"
      exposed_by: "Fandom Supercharge and Insta Beaload second chance rules"
      mitigation: "用 Super slow 后再出高伤，或在命中率关键图考虑 Insta Beaload"
      bp_use: "burst_reliability_gate"
    - id: "rattled_hive_release_interrupted"
      active_when: "Bea 释放 Rattled Hive 期间被击杀、眩晕、拉拽或击退"
      exposed_by: "Fandom notes gadget release can be interrupted before all bees launch"
      mitigation: "从安全距离/墙后释放，别把 gadget 当近身瞬发保命"
      bp_use: "gadget_window_check"

  conditional_matchups:
    - target: ["Piper", "Jae-Yong", "Gale", "Lola"]
      direction: "subject_favored"
      source: "[[sources/PLP-Bea|PLP-Bea]]"
      mechanism: "Bea 的 Supercharged 单发和 slow 能惩罚需要开阔射线或固定支援位的长线目标"
      active_when: "Bea 有同等或更好长线角度，并有队友挡住侧切"
      fails_when: "Piper outrange/开阔首击，或支援位被刺客保护反开 Bea"
      bp_use: "long_lane_pressure_response"
    - target: ["Squeak", "Lumi", "Pierce", "Griff"]
      direction: "subject_favored"
      source: "[[sources/PLP-Bea|PLP-Bea]]"
      mechanism: "在开阔路径上，slow 和 Supercharged 高伤会限制中距控制/输出的站位与推进"
      active_when: "地图给 Bea 视野，目标需要穿过她的射线接近 objective"
      fails_when: "目标躲在墙后或用召唤/区域先逼 Bea 换位"
      bp_use: "open_lane_answer_to_midrange_control"
    - target: ["Bibi", "Rosa", "Trunk", "Bolt"]
      direction: "target_favored"
      source: "[[sources/PLP-Bea|PLP-Bea]]"
      mechanism: "高速坦克/body 能利用草路或墙体吃一发后贴脸，迫使 Bea 单 ammo 断节奏"
      active_when: "地图侧草开放，Bea 没有 slow 或保护者"
      fails_when: "Bea 提前 Super slow，队友集火，且坦克必须走开阔长线"
      bp_use: "avoid_without_peel_or_open_lane"
    - target: ["Damian", "Gray", "Ollie", "Sandy"]
      direction: "target_favored"
      source: "[[sources/PLP-Bea|PLP-Bea]]"
      mechanism: "传送、控制、草区遮蔽或突进可绕过 Bea 的长线，直接攻击她低血无位移短板"
      active_when: "他们能选择第一接触或用 smoke/teleport/控制打断 Bea 的节奏"
      fails_when: "草被检查，Bea 有 slow/teammate peel，且他们必须从正面进入"
      bp_use: "draft_requires_vision_and_bodyguard"

  slot_notes:
    slot_1: "只在开阔长线、反坦需求明确且队友可保护侧路时早手"
    slot_2_3: "作为反坦/长线层选出后，需要补草区侦测和近身保护"
    slot_4_5: "看到敌方缺突进或依赖中距 body 进 objective 时可响应"
    slot_6: "最后手适合惩罚无刺客、无墙后绕线的长线阵容"
```

## 关联页面

- [[sources/Fandom-Bea|Fandom 来源摘要: Bea]]
- [[sources/PLP-Bea|PLP 来源摘要: Bea]]
