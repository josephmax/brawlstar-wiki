# Bonnie

## 基本信息

- 稀有度：Epic
- 定位：Marksman
- 类型：双形态远程压制 / 跳入爆发英雄

## 来源摘要

- Fandom：[[sources/Fandom-Bonnie|Fandom 来源摘要: Bonnie]]
- PLP：[[sources/PLP-Bonnie|PLP 来源摘要: Bonnie]]
- PLP 推荐模式：Heist, Bounty, Knockout

## 角色定位总结

Bonnie 的 BP 价值来自 Clyde 炮台形态的长射程高血量压线，以及 Super 发射后切成 Bonnie 形态的短程爆发。`Sugar Rush` 和 `Black Powder` 是默认竞技逻辑：前者补炮台形态慢移速/装填，后者把 Star Launcher 距离从 7.33 提到 10，放大跨墙、打库和收割窗口。风险在于形态切换高度承诺：跳入后射程短、血量上限低、装填慢，回 Clyde 的 0.5 秒转换会被眩晕/击退/拉扯取消。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"

  capability_vector:
    effective_range: "stateful; Clyde 9 格 long，Black Powder Super 10 格，Bonnie 形态 5 格 normal"
    projectile_reliability: "medium_high_in_clyde; 单发高速长牙稳定，Bonnie 形态三弹小范围适合近身"
    burst: "high_after_star_launcher; 落地伤害 + 三发满 ammo 近身爆发"
    sustained_dps: "medium_high_in_clyde; Clyde 1 秒装填，Sugar Rush 降到 0.769 秒；Bonnie 形态 2 秒慢装填"
    objective_damage: "high_if_super_reaches_safe; Fandom notes Super + 三 ammo 可对 safe/IKE 打出大窗口"
    mobility: "stateful; Clyde slow，Sugar Rush 补速；Bonnie 形态 very fast，Super 可飞越障碍"
    survivability: "stateful; Clyde 5000 HP 厚，Bonnie 形态 3100 HP 且短射程"
    engage: "high_with_star_launcher; 可越墙/水飞入，但落点承诺大"
    disengage: "medium_if_clyde_super_available; Bonnie 形态 Super 可回 Clyde 并治疗，但会被控制取消"
    anti_aggro: "medium; Clyde 高血量长线先消耗，Bonnie 形态可反杀短手，但怕硬控和爆发"
    anti_tank: "conditional; 长线消耗 + 跳入爆发可惩罚笨重目标，不能跳进多前排"
    wall_break: "none"
    throw_or_wall_bypass: "high_with_star_launcher; Super 飞越障碍并落地范围伤害"
    area_control: "medium; 落地 2.33 格范围和 Hypercharge stun 有区域窗口"
    scouting_or_vision: "low"
    team_support: "low; 主要是输出/收割，不提供常规团队 buff"
    spawnable_or_pet: "none"
    crowd_control: "conditional; Crash Test 击退，Hypercharge 起飞和落地 1 秒 stun"
    source_trace:
      - "[[sources/Fandom-Bonnie|Fandom-Bonnie]]"
      - "[[sources/PLP-Bonnie|PLP-Bonnie]]"

  build_switches:
    - build: "Sugar Rush / Black Powder / Shield, Damage"
      source: "[[sources/PLP-Bonnie|PLP-Bonnie]]"
      changes_capabilities:
        - "Sugar Rush 在 Clyde 形态提高 30% 移速和装填 5 秒，减少炮台形态被动挨打"
        - "Black Powder 把 Star Launcher 距离提升到 10 格，让跨墙打库/收割范围更实用"
        - "Shield/Damage gears 支持 Clyde 长线对枪和 Bonnie 形态爆发转换"
      enables:
        - "Bounty/Knockout 长线压制后跳入收割"
        - "Heist 跨墙跳 safe 打爆发"
        - "对低机动前排的双阶段压制"
      mitigates_failure_modes:
        - "clyde_slow_mobility"
        - "star_launcher_range_shortfall"
      best_when: "地图给 Clyde 长线先充 Super，且跳入目标后有明确击杀/打库/撤退收益"
      poor_when: "敌方有稳定控制守落点，或 Bonnie 跳入后必须面对多人集火"
      bp_use: "default_plp_dual_form_build"
    - build: "Crash Test / Wisdom Tooth variants"
      source: "[[sources/Fandom-Bonnie|Fandom-Bonnie]]"
      changes_capabilities:
        - "Crash Test 只在 Bonnie 形态提供 2 格冲刺、击退和伤害"
        - "Wisdom Tooth 让 Clyde 单发命中后分裂，但 Fandom tips 认为实际命中收益很弱"
      enables:
        - "近身形态的短距离反打或追击"
      mitigates_failure_modes:
        - "needs_close_form_knockback"
      best_when: "Bonnie 形态会频繁留场且需要击退"
      poor_when: "多数竞技场景 Bonnie 更常需要 Sugar Rush/Black Powder 的稳定形态价值"
      bp_use: "niche_close_form_variant"

  map_feature_hooks:
    - id: "bounty_knockout_clyde_long_lane_pressure"
      map_feature_type: "long_sightline_stateful_marksman"
      uses_feature_by: "Clyde 9 格单发、5000 HP 和 Sugar Rush 让 Bonnie 能先用长线换血充 Super"
      route_or_position: "Bounty/Knockout 长线、少墙中路、或可安全蓄 Super 的边线"
      objective_conversion: "低承诺拿星/压空间，并保留 Star Launcher 收割或撤退威胁"
      active_when: "敌方无法用更长线或投掷持续逼 Bonnie 移位"
      fails_if: "Angelo/Najia 等更安全 off-angle 或 thrower wall pressure 让 Clyde 无法站住"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Dry Season|Dry Season]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "required_capabilities.long_range_pressure_with_engage_threat"
    - id: "heist_black_powder_safe_jump_burst"
      map_feature_type: "safe_entry_jump_burst"
      uses_feature_by: "Black Powder Star Launcher 10 格飞越障碍，落地后满三 ammo 可对 safe 打爆发"
      route_or_position: "金库屏障、侧路草后、safe 角落或越墙进库点"
      objective_conversion: "把 Super 充能转成一次高爆发 safe 窗口或强制回防"
      active_when: "Bonnie 已充 Super，敌方基地缺近身爆发/控制，队友能同时施压另一线"
      fails_if: "落点被 Pearl/Colette/Edgar/控制守住，或敌方 race 快到无须回防"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Safe Zone|Safe Zone]]"
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
      bp_use: "candidate_eval.heist_entry_burst_with_landing_risk"
    - id: "gem_or_ball_star_launcher_pick_window"
      map_feature_type: "objective_carrier_or_scorer_dive_window"
      uses_feature_by: "Star Launcher 越墙落地伤害和 Bonnie 形态高移速，可追 carrier、清防守者或切断球路"
      route_or_position: "宝石 carrier 撤退路、中心堡垒角、侧草球路或球门前防守点"
      objective_conversion: "强制 gem drop、打断倒计时、或为 scorer 清出短窗口"
      active_when: "目标血线已被 Clyde 压低，Bonnie 跳入后能一轮击杀或马上回 Clyde"
      fails_if: "目标有 bodyguard、击退/眩晕，或 Bonnie 形态 5 格射程无法碰到后续目标"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
      bp_use: "slot_task.objective_pick_window_not_primary_carrier"
    - id: "knockout_wall_bypass_last_pick_engage"
      map_feature_type: "wall_or_water_bypass_engage"
      uses_feature_by: "Star Launcher 飞越障碍 1.2 秒，落地范围伤害后切近身形态"
      route_or_position: "墙后低血量目标、中心掩体边、或 Knockout 缩圈前的逃生线"
      objective_conversion: "把长线压制后的残血目标转成击杀，或迫使敌方提前交控制"
      active_when: "敌方无稳定落点控制，Bonnie 队伍能在她跳入时交叉跟伤害"
      fails_if: "跳入多人、落点被预瞄、回 Clyde 过程被控制取消"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
        - "[[entities/maps/Out in the Open|Out in the Open]]"
      bp_use: "candidate_eval.last_pick_engage_after_poke"

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - "Black Powder 跳 safe burst"
        - "Clyde 长线赢线后打库"
        - "迫使敌方回防落点"
      cannot_fulfill:
        - "无 Super 时稳定接触被墙保护的 safe"
        - "跳入多人防守仍稳定存活"
      needs_teammate_support:
        - "另一线 race 压力、落点清控、治疗或跟进伤害"
      false_positive: "Heist 价值是 Super 窗口，不是全程稳定远程打库"
    - mode: "Bounty"
      can_fulfill:
        - "Clyde 长线低承诺换血"
        - "高血量抗狙一部分单发压力"
        - "Super 收割残血或退出危险线"
      cannot_fulfill:
        - "与更长线/更安全 off-angle 无条件对狙"
        - "跳入后保星"
      needs_teammate_support:
        - "远程交叉火力、反刺客和落点保护"
      false_positive: "Bonnie 有跳入威胁，但 Bounty 死亡成本要求 Super 必须有击杀或安全回形态"
    - mode: "Knockout"
      can_fulfill:
        - "长线压空间"
        - "最后手越墙击杀窗口"
        - "残局用形态切换追击"
      cannot_fulfill:
        - "单独清墙后投掷"
        - "跳入控制密集阵容"
      needs_teammate_support:
        - "开墙/反投掷、落点夹击、保命支援"
      false_positive: "Star Launcher 能进场不等于能活着回来；落点控制是核心过滤器"

  failure_modes:
    - id: "clyde_slow_lane_tax"
      active_when: "Bonnie 在 Clyde 形态被更长线、投掷或 off-angle 持续逼位"
      exposed_by: "[[sources/Fandom-Bonnie|Fandom-Bonnie]] Clyde slow speed and one-ammo attack"
      mitigation: "用 Sugar Rush、队友交叉火力或选择不被投掷口袋压制的长线"
      bp_use: "long_lane_matchup_filter"
    - id: "star_launcher_landing_commitment"
      active_when: "Bonnie Super 跳入敌方多人、控制点或高爆发守点"
      exposed_by: "Fandom notes landing changes her to low-health short-range Bonnie form"
      mitigation: "只跳残血/孤立目标或 safe，提前确认回 Clyde/队友跟进"
      bp_use: "engage_window_hard_gate"
    - id: "return_to_clyde_cancelled"
      active_when: "Bonnie 形态尝试回 Clyde 时被 stun、knockback 或 pull 打断"
      exposed_by: "[[sources/Fandom-Bonnie|Fandom-Bonnie]] Clyde Super cancellation note"
      mitigation: "在控制资源已交后变回，或用墙/队友 cover 转形态"
      bp_use: "resource_timing_check"
    - id: "bonnie_form_short_range_reload_trap"
      active_when: "Bonnie 形态用完三发后仍被迫追击或逃跑"
      exposed_by: "Bonnie form has 5 range and 2 second reload from [[sources/Fandom-Bonnie|Fandom-Bonnie]]"
      mitigation: "保留 ammo 用于确认击杀，不把 Bonnie 当持续短手前排"
      bp_use: "avoid_overcommit_after_jump"

  conditional_matchups:
    - target: ["El Primo", "Frank", "Jacky", "Buzz"]
      direction: "subject_favored"
      source: "[[sources/PLP-Bonnie|PLP-Bonnie]]"
      mechanism: "Clyde 长线和高血量可先消耗笨重近战，Star Launcher 可在其低血量或交位移后反向收割"
      active_when: "接近路线开阔，Bonnie 保持 Clyde 距离并有 Super/Black Powder 作为重定位"
      fails_when: "目标从草墙或跳跃直接贴脸，或 Bonnie 跳入后吃控制/爆发"
      bp_use: "anti_frontline_with_distance_and_super"
    - target: ["Jae-Yong", "Meg", "Poco", "Kenji"]
      direction: "subject_favored"
      source: "[[sources/PLP-Bonnie|PLP-Bonnie]]"
      mechanism: "长线压制和跳入爆发能惩罚低爆发支援、状态型身体或资源已交的近身目标"
      active_when: "目标需要进入 Bonnie 的长线或被队友先压血，Bonnie 跳入能一轮确认"
      fails_when: "支援壳体有硬控/身体保护，Meg 机甲或 Kenji 先手贴到 Bonnie"
      bp_use: "poke_then_commit_response"
    - target: ["Edgar", "Pearl", "Leon", "Colette"]
      direction: "target_favored"
      source: "[[sources/PLP-Bonnie|PLP-Bonnie]]"
      mechanism: "跳脸、隐身、近中距离爆发或百分比伤害能惩罚 Clyde 慢速和 Bonnie 跳入后的低血量"
      active_when: "他们能选择第一接触或守住 Bonnie 的落点/回形态窗口"
      fails_when: "Bonnie 保持长线，队友提供 peel，或他们关键进场资源已交"
      bp_use: "requires_peel_before_bonnie_lock"
    - target: ["Angelo", "Najia", "Willow", "Grom"]
      direction: "target_favored"
      source: "[[sources/PLP-Bonnie|PLP-Bonnie]]"
      mechanism: "更安全的长线/侧角度、控制接管或墙后投掷会让 Clyde 难以站住，并预瞄 Bonnie 的落点"
      active_when: "地图给他们水/墙/远程角度，Bonnie 缺开墙或落点保护"
      fails_when: "墙体被打开，Bonnie 先用 Sugar Rush 压线并只跳已无控制的残血目标"
      bp_use: "must_answer_range_or_wall_control"

  slot_notes:
    slot_1: "Heist/Bounty/Knockout 长线图可早手，但要准备回答更长线、投掷和落点控制"
    slot_2_3: "适合建立长线加跳入威胁，让后续补开墙、反刺客或打库 race"
    slot_4_5: "看到敌方缺落点控制或缺 burst 时，可补 Bonnie 作为跳入惩罚位"
    slot_6: "最适合惩罚低机动、低控制或已暴露落点弱点的阵容；不能修复队伍缺稳定控图的问题"
```

## 关联页面

- [[sources/Fandom-Bonnie|Fandom 来源摘要: Bonnie]]
- [[sources/PLP-Bonnie|PLP 来源摘要: Bonnie]]
