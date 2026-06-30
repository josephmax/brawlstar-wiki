# Melodie

## 基本信息

- 稀有度：Mythic
- 定位：Assassin
- 类型：音符叠层 / 三段冲刺目标刺客

## 来源摘要

- Fandom：[[sources/Fandom-Melodie|Fandom 来源摘要: Melodie]]
- PLP：[[sources/PLP-Melodie|PLP 来源摘要: Melodie]]
- PLP 推荐模式：Brawl Ball, Heist, Bounty

## 角色定位总结

Melodie 的 BP 价值来自先用 8 格普攻叠 orbiting notes，再用三段 Super 把音符半径、Interlude 护盾和 Fast Beats 移速转成突进、得分或打库窗口。她不是无资源刺客；没有音符时伤害偏低，直线冲刺也容易被自动瞄准、控制和墙水地形打断。

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
    effective_range: "long_setup_short_finish; 8 格普攻叠音符，主要击杀来自 2.17 格 orbiting notes 贴身命中"
    projectile_reliability: "medium; 主弹低伤但用于叠资源，贴身音符稳定性取决于走位和绕圈方向"
    burst: "high_with_three_notes; 三音符加 Super 穿身可快速打残后排"
    sustained_dps: "medium; 1.5 秒装填，音符持续 8 秒，资源断档后输出下降"
    objective_damage: "high_conditional_heist; 三段 dash 可快速接触 safe，但要先有音符和生存窗口"
    mobility: "very_high_with_super; 三段 5.33 格 dash 可分次用于进场、追击、得分或撤退"
    survivability: "medium_resource_based; 3800 HP，Interlude 根据音符提供衰减护盾，护盾时效短"
    engage: "high_when_notes_and_super_ready; 需要先叠音符再 dash 进场"
    disengage: "medium_high_with_remaining_dash; Super 未用完时可撤，三段用尽后危险"
    anti_aggro: "medium; 可先 dash 避开区域 Super 再回身，但怕硬控和近战爆发"
    anti_tank: "medium_if_notes_stacked; 音符伤害高但要持续贴近，高身体/控制会反打"
    wall_break: "none"
    throw_or_wall_bypass: "none; Super 不能当稳定越墙，水和墙会中断 dash 路径"
    area_control: "low_medium; orbiting notes 威慑贴身区，不是持久封路"
    scouting_or_vision: "low"
    team_support: "low"
    crowd_control: "none"

  build_switches:
    - build: "Interlude / Fast Beats / Shield, Damage"
      source: "[[sources/PLP-Melodie|PLP-Melodie]]"
      changes_capabilities:
        - "用音符数量转护盾，保护 dash 进场和 safe/goal 接触"
        - "Fast Beats 让三音符状态同时提供追击、躲线和持球速度"
      enables:
        - "Brawl Ball 三段 dash 带球/自传得分"
        - "Heist 远距离进库与短时间 safe burst"
        - "Bounty 后手切孤立低血远程"
      mitigates_failure_modes:
        - "dash_into_contact_without_survival"
        - "straight_dash_autoaim_punish"
      best_when: "Melodie 能安全叠到 2-3 个音符，且目标路线允许 dash 后贴身输出"
      poor_when: "地图水墙密、敌方控制/击退密集，或目标有近战反杀"
      bp_use: "default_plp_resource_assassin_build"
    - build: "Perfect Pitch / Fast Beats or Extended Mix / Shield, Damage"
      source: "[[sources/Fandom-Melodie|Fandom-Melodie]]"
      changes_capabilities:
        - "提高音符半径与旋转速度，扩大贴身输出命中窗口"
      enables:
        - "面对会保持短距离的目标时增加音符扫中概率"
      mitigates_failure_modes:
        - "notes_miss_during_dash_path"
      best_when: "敌方缺硬控且 Melodie 需要靠音符范围补击杀"
      poor_when: "进场后敌人贴脸，扩大半径反而让音符绕过目标"
      bp_use: "mechanical_variant_not_default"

  map_feature_hooks:
    - id: "brawl_ball_three_dash_score_route"
      map_feature_type: "flank_score_route"
      uses_feature_by: "Super 三段 dash 不耗 ammo，可带球、自传或跨越中场后仍保留攻击资源"
      objective_conversion: "把侧草/中路赢线直接转成进球窗口"
      active_when: "球门有破墙/控人或侧路草能保护第一段接近"
      fails_if: "球门屏障未处理、敌方击退/眩晕守门，或 dash 直线被预判"
      example_maps: ["[[entities/maps/Center Stage|Center Stage]]", "[[entities/maps/Sneaky Fields|Sneaky Fields]]", "[[entities/maps/Triple Dribble|Triple Dribble]]", "[[entities/maps/Pinball Dreams|Pinball Dreams]]"]
      bp_use: "Brawl Ball scorer/tempo pick"
    - id: "heist_dash_safe_entry_with_notes"
      map_feature_type: "safe_entry_after_resource_stack"
      uses_feature_by: "先叠音符，再用三段 Super 从远处接近金库并靠 Interlude 护盾承受防守火力"
      objective_conversion: "把一次路线突破转成 safe burst 或迫使双人回防"
      active_when: "侧路或中草能让 Melodie 叠资源并进入金库半场"
      fails_if: "水/墙中断 dash、敌方基地有近战反打，或 Melodie 无音符进库"
      example_maps: ["[[entities/maps/Hot Potato|Hot Potato]]", "[[entities/maps/Pit Stop|Pit Stop]]", "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"]
      bp_use: "Heist 条件突袭 DPS；需要 route validation"
    - id: "bounty_backline_dash_after_note_stack"
      map_feature_type: "last_pick_backline_pressure"
      uses_feature_by: "长线先叠音符，等后排交资源后用 zig-zag dash 切入"
      objective_conversion: "Bounty 中删除低血远程或迫使其退出星线"
      active_when: "敌方后排孤立且没有 Gale/Tara/Bibi 类保护"
      fails_if: "Melodie 直线 dash 被 autoaim，或地图墙水让三段位移断裂"
      example_maps: ["[[entities/maps/Layer Cake|Layer Cake]]", "[[entities/maps/Hideout|Hideout]]", "[[entities/maps/Shooting Star|Shooting Star]]"]
      bp_use: "高风险后手反长线，不适合早手"
    - id: "open_lane_zigzag_anti_marksman_entry"
      map_feature_type: "anti_marksman_pressure"
      uses_feature_by: "通过非直线 dash 和 Fast Beats 速度躲开线性普攻，迫使 marksman 交撤退资源"
      objective_conversion: "打开边路线权、打断 safe lane 或压缩 Bounty/Knockout 空间"
      active_when: "敌方主要输出是线性弹道，且没有近身 bodyguard"
      fails_if: "dash 路径被控制、陷阱或范围伤害覆盖"
      example_maps: ["[[entities/maps/Bridge Too Far|Bridge Too Far]]", "[[entities/maps/Out in the Open|Out in the Open]]", "[[entities/maps/Flaring Phoenix|Flaring Phoenix]]"]
      bp_use: "response pick into isolated linear range"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "三段 dash 带球、自传、追球和终结得分"
        - "叠音符后清守门人"
      cannot_fulfill:
        - "独自解决闭门墙体"
      needs_teammate_support:
        - "破门、控人或吸引守门控制"
      false_positive: "会 dash 不等于有进球路径；球门屏障和控制必须先处理"
    - mode: "Heist"
      can_fulfill:
        - "快速接触 safe 并用音符打短爆发"
        - "迫使防守回头处理后场"
      cannot_fulfill:
        - "在无资源时做稳定远程 safe DPS"
      needs_teammate_support:
        - "边路线权、探草或主 race DPS"
      false_positive: "三段 dash 如果被墙水切断，会变成无目标接近"
    - mode: "Bounty"
      can_fulfill:
        - "最后手惩罚无 peel 后排"
        - "用机动逼长线放弃安全角度"
      cannot_fulfill:
        - "早手承担保星主线"
      needs_teammate_support:
        - "视野、补伤和反控制"
      false_positive: "Bounty 中失败进场会直接送星"

  failure_modes:
    - id: "notes_not_stacked_before_entry"
      active_when: "Melodie 无 2-3 个音符就 dash 进场"
      exposed_by: "main attack low damage; notes are main damage"
      mitigation: "先安全叠资源，再决定是否开 Super"
      bp_use: "resource_gate_before_engage"
    - id: "straight_dash_autoaim_punish"
      active_when: "对 Piper、Mandy、Brock 等线性弹道目标直线 dash"
      exposed_by: "Fandom tips warn against straight dash into projectile line"
      mitigation: "zig-zag dash 或等敌方 ammo/控制交掉"
      bp_use: "execution_filter"
    - id: "water_wall_dash_interrupt"
      active_when: "地图水墙多，Super 路径被打断或被迫绕线"
      exposed_by: "Fandom tips warn against many water/wall maps"
      mitigation: "只在路线连续且目标可达时选"
      bp_use: "map_route_check"
    - id: "interlude_shield_decay"
      active_when: "Melodie 过早开盾，接触时护盾已衰减"
      exposed_by: "Interlude shield decays every 0.35s"
      mitigation: "贴近窗口再开，或保留 dash 撤退"
      bp_use: "resource_timing_check"

  conditional_matchups:
    - target: ["Sprout", "Dynamike", "Ziggy", "Brock", "Mandy", "Piper"]
      direction: "subject_favored"
      source: "[[sources/PLP-Melodie|PLP-Melodie]]"
      mechanism: "叠音符后多段 dash 能穿过线性弹道和墙边站位，逼低血后排失去安全距离"
      active_when: "目标孤立、缺 bodyguard，Melodie 已有音符和 Super"
      fails_when: "目标有控制保护、墙水断路，或 Melodie 直线 dash 被命中"
      bp_use: "last_pick_or_response_backline_pressure"
    - target: ["Bolt", "Spike"]
      direction: "subject_favored"
      source: "[[sources/PLP-Melodie|PLP-Melodie]]"
      mechanism: "高速贴身和 orbiting notes 可绕开固定弹道/区域节奏，在目标交资源后收割"
      active_when: "目标没有控制留给 dash 接触"
      fails_when: "区域伤害覆盖 Melodie 路径或目标有队友保护"
      bp_use: "resource_window_punish"
    - target: ["Sandy", "Tara", "Gale", "Bibi"]
      direction: "target_favored"
      source: "[[sources/PLP-Melodie|PLP-Melodie]]"
      mechanism: "隐蔽、拉人、击退、减速或近战反打能破坏 Melodie 的 dash 路径和音符接触"
      active_when: "他们守住球门、草口、zone 入口或后排身边"
      fails_when: "控制交掉且 Melodie 从侧角进入"
      bp_use: "requires_control_bait_or_ban"
    - target: ["Finx", "Lola", "R-T", "Pearl"]
      direction: "target_favored"
      source: "[[sources/PLP-Melodie|PLP-Melodie]]"
      mechanism: "更稳定的中远程压力、分身/形态或高爆发能在 Melodie 叠资源前惩罚她"
      active_when: "地图给他们安全角度或 bodyguard 站位"
      fails_when: "Melodie 已有三音符和 dash 资源，且目标站位孤立"
      bp_use: "avoid_as_early_pick_into_stable_midrange"

  slot_notes:
    slot_1: "不建议早手；被控制、近战反打和地图路线针对后会很难进场"
    slot_2_3: "可在 Brawl Ball/Heist 构建目标突袭计划，但后续要补破门或 safe DPS"
    slot_4_5: "看到敌方后排缺 peel、球门控制不足或 safe 防守薄弱时价值高"
    slot_6: "最佳惩罚位；专门打无控制的远程/投掷/支援站位"
```

## 关联页面

- [[sources/Fandom-Melodie|Fandom 来源摘要: Melodie]]
- [[sources/PLP-Melodie|PLP 来源摘要: Melodie]]
