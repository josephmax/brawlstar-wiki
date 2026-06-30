# Kit

## 基本信息

- 稀有度：Legendary
- 定位：Support
- 类型：自动充能跳跃 / 附身治疗 / 隐身单抓

## 来源摘要

- Fandom：[[sources/Fandom-Kit|Fandom 来源摘要: Kit]]
- PLP：[[sources/PLP-Kit|PLP 来源摘要: Kit]]
- PLP 推荐模式候选：Gem Grab, Knockout

## 角色定位总结

Kit 是双态支援/刺杀英雄。常态短手、非常快装填，Super 自动充能；跳到敌人身上会短暂 stun 并持续低伤害，但 Kit 自己不能移动/攻击，适合孤立目标而不是跳进三人堆。跳到队友身上则进入附身形态，Kit 免疫伤害、治疗双方，并用远程越墙 yarn balls 输出；`Overly Attached` 把附身时间从 8 秒延长到 13 秒。BP 中 Kit 的关键问题是“有没有可靠载体/孤立目标”，而不是单独看跳跃距离。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Kit|Fandom-Kit]]"
    plp: "[[sources/PLP-Kit|PLP-Kit]]"
    user_notes: none

  capability_vector:
    effective_range: short_alone_long_thrower_when_attached
    projectile_reliability: high_short_claw; medium_attached_yarn_balls_with_delay
    burst: medium_on_isolated_enemy_jump; high_with_attached_yarn_followup
    sustained_dps: low_medium_alone; conditional_high_with_good_teammate_carrier
    objective_damage: low; objective value comes from sustain, pick, and route pressure
    mobility: high_with_super_jump_and_detach_dash
    survivability: low_alone_3100_hp; invulnerable_while_attached_to_ally
    engage: high_on_isolated_enemy_or_ally_carrier
    disengage: medium_with_super_detach_or_cardboard_box
    anti_aggro: conditional_with_jump_stun_or_tank_attach
    anti_tank: low_alone; high_support_if_attached_to_tank_with_Cheeseburger_variant
    wall_break: none
    throw_or_wall_bypass: high_when_attached_yarn_balls_over_obstacles
    area_control: medium_when_attached
    scouting_or_vision: medium_with_Cardboard_Box_stealth_route
    team_support: very_high_attached_heal_and_Cheeseburger_variant
    spawnable_or_pet: none
    crowd_control: enemy_super_stun
    terrain_destruction: none

  build_switches:
    - build: "Cardboard Box / Overly Attached / Shield, Damage"
      source: "[[sources/PLP-Kit|PLP-Kit]]"
      changes_capabilities:
        - "Cardboard Box 给 3 秒隐身并在静止时加速自动 Super 充能，适合单抓或回合前储 Super"
        - "Overly Attached 延长附身队友时间，提升治疗和越墙 yarn ball 输出窗口"
        - "Shield/Damage 弥补常态低血和单抓斩杀线"
      enables:
        - "Gem Grab carrier sustain"
        - "Knockout isolated pick"
        - "stealth route setup"
      mitigates_failure_modes:
        - "low_base_health_when_alone"
        - "super_cycle_wait_time"
      best_when: "队伍有可靠载体或敌方有孤立长手/投掷目标"
      poor_when: "敌方有强群控、反跳、沉默、茧、拉人或坦克爆发等资源等 Kit 落点"
      bp_use: default_stealth_attach_build
    - build: "Cheeseburger tank-attach variant"
      source: "[[sources/Fandom-Kit|Fandom-Kit]] / [[sources/PLP-Kit|PLP-Kit]]"
      changes_capabilities:
        - "Cheeseburger 只能在附身形态使用，为 Kit 和载体立刻治疗 30% 最大生命"
        - "PLP notes 标注有坦克队友时可考虑 Gadget 2"
      enables:
        - "tank_push_sustain"
        - "Brawl Ball_or_zone_body_support"
      mitigates_failure_modes:
        - "carrier_focus_fire"
      best_when: "队友有 Draco、Frank、Hank、El Primo、Bull、Darryl 等高血载体并能转化推进"
      poor_when: "队伍没有载体或敌方有反坦/沉默/击退能直接拆推进"
      bp_use: teammate_dependent_sustain_variant

  map_feature_hooks:
    - map_feature_type: gem_attach_carrier_sustain_or_pick
      uses_feature_by: "附身队友持续按最大生命治疗，同时用 yarn balls 越墙压矿区或追击 carrier"
      route_or_position: "gem mine、center fort doorway、carrier countdown retreat、side grass chase"
      objective_conversion: "保护己方 carrier、逼敌方 carrier 退线、或用隐身/Super 单抓孤立目标"
      active_when: "己方有可承载 Kit 的 carrier/body，或敌方 carrier 缺队友保护"
      fails_if: "Kit 被要求自己长期带宝石，或敌方控制保留给载体"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Double Swoosh
      bp_use: map_bp_factors.carrier_sustain_or_isolated_pick
    - map_feature_type: knockout_cardboard_box_isolated_pick_or_attach_trade
      uses_feature_by: "Cardboard Box 加速 Super 并提供隐身接近，附身队友可在回合里提供长时间治疗和越墙火力"
      route_or_position: "wall edge、side grass、late-round choke、low-health retreat"
      objective_conversion: "抓孤立长手/投掷，或附身队友把 HP lead 转成回合优势"
      active_when: "目标孤立，敌方缺 Gale/Charlie/Cordelius 等硬反制，Kit 能安全充到 Super"
      fails_if: "目标身边有队友，Kit 跳上后无法移动/攻击并被集火"
      example_maps:
        - Belle's Rock
        - New Horizons
        - Layer Cake
        - Shooting Star
      bp_use: slot_task.round_isolated_pick_or_sustain
    - map_feature_type: tank_attach_push_support
      uses_feature_by: "Kit 附身高血队友后治疗并越墙输出，Cheeseburger 可补一波大治疗"
      route_or_position: "goal route、zone entrance、safe entry、midfield body push"
      objective_conversion: "让坦克/身体推进更久，给进球、站区或金库入口制造持续压力"
      active_when: "队伍有真实载体且载体路线能转化目标，敌方反坦资源已被处理"
      fails_if: "Poco/反坦/控制壳比 Kit sustain 更稳定，或载体进场后被沉默/击退/茧隔离"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Ring of Fire
        - Open Business
      bp_use: candidate_eval.teammate_carrier_sustain_not_solo_pick
    - map_feature_type: stealth_route_backline_punish
      uses_feature_by: "Cardboard Box 隐身和自动 Super 让 Kit 可从草/墙边接近脆弱后排"
      route_or_position: "side bush、thrower pocket edge、long-lane flank、carrier retreat"
      objective_conversion: "逼出后排资源、击杀孤立目标或让敌方阵型回撤"
      active_when: "地图有侧路，目标缺近身保镖，Kit 的 Super 不会被目标移动 Super 取消"
      fails_if: "目标留有位移 Super、无敌盾或控制，或队友距离太近保护被跳目标"
      example_maps:
        - Double Swoosh
        - Center Stage
        - Sneaky Fields
        - Belle's Rock
      bp_use: slot_task.stealth_backline_punish_with_cancel_check

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier_sustain"
        - "isolated_carrier_pick"
        - "attached_wall_pressure"
      cannot_fulfill:
        - "primary_carrier_when_alone"
      needs_teammate_support:
        - "carrier_or_tank_body"
        - "anti_control_on_attach_target"
      false_positive: "Kit 强在附身保护 carrier，不是自己低血拿宝石站中路"
    - mode: "Knockout"
      can_fulfill:
        - "isolated_target_stun"
        - "round_sustain_on_teammate"
        - "attached_yarn_over_wall"
      cannot_fulfill:
        - "jump_into_grouped_team"
      needs_teammate_support:
        - "focus_fire_after_stun"
        - "safe_carrier_for_attach"
      false_positive: "跳到敌方身上时 Kit 不能移动/攻击；如果目标旁边有人会被反打"
    - mode: "Brawl Ball_or_Hot Zone"
      can_fulfill:
        - "tank_push_sustain"
        - "ball_or_zone_body_healing"
        - "enemy_carrier_stun_if_isolated"
      cannot_fulfill:
        - "primary_scorer_or_zone_body_alone"
      needs_teammate_support:
        - "tank_or_scorer_carrier"
        - "anti_knockback_or_anti_control"
      false_positive: "该分支高度依赖队友载体，PLP 默认模式并不把它列为主推荐"

  failure_modes:
    - id: jump_on_grouped_enemy
      active_when: "Kit 跳到敌人身上但目标附近有队友，Kit 1.5 秒不能移动/攻击"
      exposed_by: "[[sources/Fandom-Kit|Fandom-Kit]] Super tips"
      mitigation: "只跳孤立目标、低血目标或有队友立即跟伤的目标"
      bp_use: target_selection_gate
    - id: moving_super_cancel_or_pull_along
      active_when: "Kit 跳到正在使用位移 Super 的 Buzz、Fang、Chuck、Berry、Darryl、Bull 等目标"
      exposed_by: "[[sources/Fandom-Kit|Fandom-Kit]] Super cancellation warning"
      mitigation: "记录目标位移资源，等其交出后再跳"
      bp_use: resource_tracking.enemy_super_state
    - id: no_teammate_carrier
      active_when: "队伍没有高血/安全载体，Kit 的 Overly Attached 和 Cheeseburger 无法转化目标"
      exposed_by: "[[sources/Fandom-Kit|Fandom-Kit]] tank synergy tips and PLP notes"
      mitigation: "只在已有 carrier/body 或后手确认孤立目标时选"
      bp_use: team_comp_hard_gate
    - id: hard_control_answers_attach_or_jump
      active_when: "Lou、Cordelius、Charlie、Tara、Gale、Frank 等保留控制处理 Kit 或载体"
      exposed_by: "[[sources/PLP-Kit|PLP-Kit]] counteredBy list"
      mitigation: "先逼出控制，或让 Kit 附身目标避开控制入口"
      bp_use: must_answer_control_before_kit

  conditional_matchup_seeds:
    - target: Colt_or_Brock_or_Dynamike_or_Belle_or_Grom_or_Squeak_or_Mr_P_or_Angelo
      direction: subject_favored
      source: "[[sources/PLP-Kit|PLP-Kit]]"
      mechanism: "Cardboard Box 隐身、自动充能 Super 和跳跃 stun 可以惩罚孤立长手/投掷/资源位"
      active_when: "目标缺队友保护，Kit 有 Super 或即将充好，并能从草/墙路接近"
      fails_when: "目标抱团、保留位移/控制，或开阔长线在 Kit 接近前压低他"
      bp_use: isolated_backline_punish
    - target: Lou_or_Cordelius_or_Charlie_or_Bull_or_Tara_or_Chester_or_Gale_or_Frank
      direction: target_favored
      source: "[[sources/PLP-Kit|PLP-Kit]]"
      mechanism: "控制、领域、茧、击退、爆发和高身体能阻止 Kit 跳入或拆掉其附身载体"
      active_when: "这些资源能保存给 Kit 或他的载体路线"
      fails_when: "资源已被逼出，Kit 只附安全队友远程输出"
      bp_use: must_answer_control_or_body_before_kit
    - target: Tank_teammate
      direction: subject_favored
      source: "[[sources/Fandom-Kit|Fandom-Kit]] / [[sources/PLP-Kit|PLP-Kit]]"
      mechanism: "附身高血队友提供持续百分比治疗、免疫本体伤害和越墙 yarn ball 输出"
      active_when: "队友路线可转化进球、站区、carrier 保护或回合推进"
      fails_when: "敌方反坦/控制直接阻断载体，或 Kit 需要自己创造目标"
      bp_use: teammate_synergy_edge
    - target: Poco_sustain_shell
      direction: target_favored
      source: "[[sources/PLP-Kit|PLP-Kit]]"
      mechanism: "PLP avoid 标注 Poco，说明对面群体 sustain 可能降低 Kit 单抓/附身交易的击杀收益"
      active_when: "Poco 队友能抱团、回血并保护 Kit 想跳的目标"
      fails_when: "Kit 只打孤立后排或附身高压载体绕开 Poco 治疗核心"
      bp_use: avoid_into_group_sustain_without_burst

  slot_notes:
    slot_1: "不适合盲先手，除非己方已锁定强载体或地图/模式明确奖励附身 sustain。"
    slot_2_3: "可与坦克、carrier 或强回合队友形成计划，但需要避免对方后手拿硬控。"
    slot_4_5: "看到敌方孤立长手/投掷且缺保护时可作为惩罚 pick，同时检查目标位移 Super。"
    slot_6: "最适合最后手确认敌方缺控制、缺抱团保护后，用隐身/跳跃或附身队友打高上限。"
```

## 关联页面

- [[sources/Fandom-Kit|Fandom 来源摘要: Kit]]
- [[sources/PLP-Kit|PLP 来源摘要: Kit]]
