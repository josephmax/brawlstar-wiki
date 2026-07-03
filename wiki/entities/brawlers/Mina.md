# Mina

## 基本信息

- 稀有度：Mythic
- 定位：Damage Dealer
- 类型：三段连段 / 位移控制输出

## 来源摘要

- Fandom：[[sources/Fandom-Mina|Fandom 来源摘要: Mina]]
- PLP：[[sources/PLP-Mina|PLP 来源摘要: Mina]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Heist, Hot Zone, Bounty, Knockout

## 角色定位总结

Mina 是连段型机动输出。她的三段普攻分别提供长线 poke、中距离补伤和短宽高伤害穿透，并且每次攻击都会按移动方向 dash；Super 提供宽弹道击飞/拉近，Windmill 可短时间挡投射物，Zum Zum Zum 用第三段命中回血。BP 中她更像“可用位移和控制赢 lane 的中短线 carry”，但必须管理 1.35 秒连段计时、第三段 0.5 秒前摇和错误方向 dash 的风险。

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
    effective_range: "variable; 第 1 段 8 格，第 2 段 6 格，第 3 段 4.67 格宽锥形穿透"
    projectile_reliability: "medium; 前两段线性，第三段有 0.5 秒前摇但宽且穿透"
    burst: "high_if_combo_lands; Super 击飞后接第一段或第三段可完成爆发"
    sustained_dps: "medium_high; 1.4 秒快装填，但连段断裂会回到低伤第一段"
    objective_damage: "medium_high_conditional_heist; 第三段和快速连段能打库，但要赢线接触目标"
    mobility: "high_but_directional; 每次攻击按移动方向 dash，站定可不 dash"
    survivability: "medium; 3600 HP，Zum Zum Zum 第三段回血，Windmill 保护关键前摇"
    engage: "medium_high; dash + Super 可压 marksman 或切失位目标"
    disengage: "medium; dash 可撤，但错误面向会送到近战面前"
    anti_aggro: "medium_high_with_super; Super 击飞/Blown Away root 可阻止刺客贴近"
    anti_tank: "medium; 第三段高伤和 Super 控制可打前排，但点脸 Super 可能失效"
    wall_break: "none"
    throw_or_wall_bypass: "partial_super_width; Super 宽到可影响墙后近点，但不能穿墙"
    area_control: "medium; 第三段穿透锥形和 Super 宽弹道可惩罚拥挤入口"
    scouting_or_vision: "low"
    team_support: "low"
    crowd_control: "high_with_super; 击飞使目标不能行动，Blown Away 追加 1.5 秒 root"

  build_switches:
    - build: "Windmill / Zum Zum Zum / Health, Shield, Damage"
      source: "[[sources/PLP-Mina|PLP-Mina]]"
      changes_capabilities:
        - "Windmill 用 1.5 秒投射物屏障保护推进或第三段前摇"
        - "Zum Zum Zum 让第三段多目标命中转成回血，支持中线续航"
      enables:
        - "开阔 lane 对 marksman 推进"
        - "Gem/Zone/Ball 中路连段控线"
        - "Heist 单路线权后打库"
      mitigates_failure_modes:
        - "attack3_windup_interrupt"
        - "projectile_lane_denial"
      best_when: "敌方主要靠投射物、线性远程或中距离控制赢线"
      poor_when: "敌方可穿墙、近身 stat check 或能等 Windmill 结束再接触"
      bp_use: "default_plp_lane_carry_build"
    - build: "Capo-What? / Blown Away / Shield, Damage"
      source: "[[sources/Fandom-Mina|Fandom-Mina]]"
      changes_capabilities:
        - "命中 Super 后回满 Super，并用 root 延长控制"
      enables:
        - "对刺客/marksman 连续控制，或在 narrow choke 打连续拾取"
      mitigates_failure_modes:
        - "assassin_contact_without_root"
      best_when: "敌方必须穿过可预判窄口，且 Mina 可以安全命中 Super"
      poor_when: "目标能贴脸让 Super 拉扯失效，或控制期间队友无法跟伤"
      bp_use: "control_chain_variant"

  map_feature_hooks:
    - id: "open_lane_windmill_marksman_push"
      map_feature_type: "projectile_lane_screen"
      uses_feature_by: "Windmill 挡投射物，Mina 用普攻 dash 和变量射程推进 lane"
      objective_conversion: "把开阔路线的远程劣势转成过线、压 safe 或拿星空间"
      active_when: "敌方主要伤害为可被 Windmill 吸收的投射物"
      fails_if: "敌方攻击可穿墙/越屏障，或近战直接穿过 Windmill 接触"
      example_maps: ["[[entities/maps/Bridge Too Far|Bridge Too Far]]", "[[entities/maps/Shooting Star|Shooting Star]]", "[[entities/maps/Out in the Open|Out in the Open]]"]
      bp_use: "response_pick_into_projectile_lane"
    - id: "combo_dash_mid_objective_control"
      map_feature_type: "mixed_mid_and_choke"
      uses_feature_by: "三段连段在中线从 poke 过渡到宽锥形穿透，dash 负责 dodge 与压身位"
      objective_conversion: "Gem/Zone/Ball 中把入口控制转成拾宝、站圈或持球推进"
      active_when: "路线有中距离接触且敌方需要争同一入口"
      fails_if: "Mina 连段计时断裂，或错误方向 dash 进高爆发近战"
      example_maps: ["[[entities/maps/Hard Rock Mine|Hard Rock Mine]]", "[[entities/maps/Gem Fort|Gem Fort]]", "[[entities/maps/Dueling Beetles|Dueling Beetles]]", "[[entities/maps/Center Stage|Center Stage]]"]
      bp_use: "mid_lane_damage_control"
    - id: "super_launch_or_root_pick_window"
      map_feature_type: "choke_control_and_pick"
      uses_feature_by: "Super 击飞并拉近目标，Blown Away 可追加 root，保护 Mina 或队友完成击杀"
      objective_conversion: "Knockout/Bounty 中抢第一击杀，Brawl Ball/Hot Zone 中阻止进场"
      active_when: "目标经过窄口或要强行接触 Mina"
      fails_if: "Super 点脸不产生有效拉扯，或击飞期间地面伤害无法接上"
      example_maps: ["[[entities/maps/Flaring Phoenix|Flaring Phoenix]]", "[[entities/maps/Belle's Rock|Belle's Rock]]", "[[entities/maps/Layer Cake|Layer Cake]]", "[[entities/maps/Open Business|Open Business]]"]
      bp_use: "control_pick_or_anti_engage"
    - id: "heist_lane_combo_after_win"
      map_feature_type: "lane_win_to_safe_pressure"
      uses_feature_by: "赢下隔离/边路后用快速连段和第三段高伤害进入 safe pressure"
      objective_conversion: "Heist 中把 lane win 转成打库窗口"
      active_when: "Mina 能独立守一路或队友提供开线"
      fails_if: "敌方远程 race 更快，或 Mina 被迫把 ammo 用于逃跑而非打库"
      example_maps: ["[[entities/maps/Bridge Too Far|Bridge Too Far]]", "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]", "[[entities/maps/Hot Potato|Hot Potato]]"]
      bp_use: "conditional_heist_lane_carry"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "中路/侧路控线、用 dash 避弹、第三段穿透惩罚入口"
      cannot_fulfill:
        - "无保护长期当唯一 carrier"
      needs_teammate_support:
        - "探草、反投掷或稳定载宝位"
      false_positive: "机动输出不等于 carrier 安全"
    - mode: "Brawl Ball"
      can_fulfill:
        - "用 Super/root 阻止 scorer，或 dash 过线制造推进"
      cannot_fulfill:
        - "单独破门"
      needs_teammate_support:
        - "破门/强控/真实 scorer"
      false_positive: "dash 会改善推进，但错误方向会直接送球权"
    - mode: "Heist"
      can_fulfill:
        - "赢线后打库，Windmill 保护开阔 lane 推进"
      cannot_fulfill:
        - "隔墙或远程低承诺打库"
      needs_teammate_support:
        - "开墙、边路保护或主 safe DPS"
      false_positive: "Mina 需要目标访问，不是纯远程 Heist carry"
    - mode: "Hot Zone"
      can_fulfill:
        - "中短线进圈、Super 阻进、第三段回血续航"
      cannot_fulfill:
        - "单独顶住高爆发多人集火"
      needs_teammate_support:
        - "站圈身体或区域控制"
      false_positive: "击飞期间免疫地面伤害，队友跟伤时机要等落地"
    - mode: "Bounty/Knockout"
      can_fulfill:
        - "用 Windmill 抢线和 Super/root 打关键 pick"
      cannot_fulfill:
        - "在完全开阔远程图替代极长线"
      needs_teammate_support:
        - "补长线、视野或开墙"
      false_positive: "Mina 有 8 格第一段，但核心伤害更靠中短线接触"

  failure_modes:
    - id: "combo_timer_or_ammo_break"
      active_when: "1.35 秒内没接下一段，或被偷/耗掉 ammo"
      exposed_by: "attack sequence resets if timer expires"
      mitigation: "保留三 ammo 或等敌方关键技能交掉再连段"
      bp_use: "resource_gate"
    - id: "attack3_windup_interrupt"
      active_when: "第三段 0.5 秒前摇被控制或爆发打断"
      exposed_by: "Fandom notes Windmill can protect Attack 3 windup"
      mitigation: "用 Windmill、墙角或队友控线保护第三段"
      bp_use: "execution_and_build_check"
    - id: "bad_dash_into_tank"
      active_when: "攻击时面向错误，把 Mina dash 到 Bull/Shelly/Darryl 等高爆发面前"
      exposed_by: "attacks dash in movement direction; Fandom warning"
      mitigation: "站定不 dash，或只用侧向 dash dodge"
      bp_use: "avoid_into_close_burst_without_route"
    - id: "pointblank_super_failure"
      active_when: "目标已经贴脸，Super 拉扯/击飞价值下降"
      exposed_by: "Fandom warns point-blank Super can become useless into jump-in targets"
      mitigation: "提前用 Super、选择 Blown Away root，或配队友 peel"
      bp_use: "anti_engage_timing_check"

  conditional_matchups:
    - target: ["Dynamike", "Ziggy", "Squeak", "Tick"]
      direction: "subject_favored"
      source: "[[sources/PLP-Mina|PLP-Mina]]"
      mechanism: "dash + Windmill 可穿过投射物/控制窗口，第三段和 Super 惩罚墙口或低血控制位"
      active_when: "Mina 有连段资源且目标缺近身保护"
      fails_when: "目标在深墙后，或 Mina 必须穿过不可挡的区域伤害"
      bp_use: "response_pick_against_control_pocket"
    - target: ["Jessie", "Lou", "Griff", "Bo"]
      direction: "subject_favored"
      source: "[[sources/PLP-Mina|PLP-Mina]]"
      mechanism: "Windmill 和 dash 降低线性/中距离控制命中率，Super/root 可打断固定站位"
      active_when: "目标需要站在中线、矿区或球路入口"
      fails_when: "召唤物/地雷/高爆发先限制 Mina 连段"
      bp_use: "mid_control_duel_candidate"
    - target: ["Gale", "Damian", "Buster", "Nita"]
      direction: "target_favored"
      source: "[[sources/PLP-Mina|PLP-Mina]]"
      mechanism: "击退/控制、墙后压力、屏障或召唤物会切断 Mina 连段和 dash 路线"
      active_when: "他们守在 Mina 必须进入的 choke 或目标区"
      fails_when: "Mina 用 Windmill/Blown Away 先骗出控制并绕侧接触"
      bp_use: "requires_control_bait_or_clear"
    - target: ["Trunk", "8-Bit", "Bolt", "Glowy"]
      direction: "target_favored"
      source: "[[sources/PLP-Mina|PLP-Mina]]"
      mechanism: "高身体、稳定 DPS 或范围控制能在 Mina 连段完成前承受并反压"
      active_when: "地图让他们正面守目标而不必追 Mina"
      fails_when: "Mina 能反复侧 dash、Super 控制并由队友补伤"
      bp_use: "avoid_raw_front_to_back_without_support"

  slot_notes:
    slot_1: "可在明确 lane 需要 Windmill 反投射物时较早选，但要看敌方剩余控制"
    slot_2_3: "适合补中路线权和反接近控制"
    slot_4_5: "看到敌方缺硬控或 relies on projectile lanes 时更稳"
    slot_6: "可惩罚无近战反打的中线控制/远程，但需要玩家能执行连段"
```

## 关联页面

- [[sources/Fandom-Mina|Fandom 来源摘要: Mina]]
- [[sources/PLP-Mina|PLP 来源摘要: Mina]]
