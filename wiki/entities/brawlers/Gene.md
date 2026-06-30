# Gene

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 来源：神话控制型英雄

## 攻击特征

- 主攻击是会分裂的魔法烟雾
- 近中远距离表现不同
- 更适合稳定压线、骚扰和控图

## 超级技能特征

- Super `Magic Hand` 会把命中的敌人拉到自己身边
- 可以打断敌人动作，强制改变对手站位
- 很适合配合队友完成击杀

## 适合场景

- 控图和反开团
- 需要拉人制造人数优势的对局
- 队友能快速接伤害的阵容
- 对手站位分散或保护薄弱的场景

## 模式适配修正

- 在目标型模式里，Gene 的价值更偏向“拉人制造减员”而不是自己承担推进职责
- 一条来自用户经验的修正指出：在 `Brawl Ball` 中，不应把 Gene 当成理想的持球推进核心
- 更合理的理解是：他通过拉人或抓失位来创造进球窗口，再让更适合推进的队友完成推进

## 角色定位总结

Gene 是中距离控制核心，最强之处不是单纯输出，而是用拉人改写战局节奏。

## 与其他英雄的区别

- 不同于 `Byron`：Byron 偏续航和治疗，Gene 偏强制位移和开团
- 不同于 `Max`：Max 偏团队加速，Gene 偏单点控制
- 不同于 `Mortis`：Mortis 是切入刺客，Gene 是站位改写型控制

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-06-30-v2
    plp: direct_raw_capture_2026-06-29
    user_notes: gene_brawl_ball_role_correction

  capability_vector:
    effective_range: variable_mid_to_very_long_chip
    projectile_reliability: medium; 主弹慢，分裂弹可远距骚扰和探草
    burst: low_without_pull_followup
    sustained_dps: low_medium; 慢装填且更偏控制
    objective_damage: low
    mobility: low
    survivability: medium_with_Shield_and_positioning
    engage: high_when_Magic_Hand_hits_key_target
    disengage: medium_with_Lamp_Blowout
    anti_aggro: conditional; Lamp Blowout 可推开近身，Super 可抓单
    anti_tank: low_medium; 依赖拉人后队友集火
    wall_break: conditional; Super 拉人会破坏目标穿过的障碍
    throw_or_wall_bypass: high_for_pull; Magic Hand 可穿墙
    area_control: medium_with_split_attack_and_vision
    scouting_or_vision: high_with_split_projectiles_and_Vision_Gear
    team_support: high; Magic Puffs 治疗与拉人创造减员

  build_switches:
    - build: Vengeful Spirits / Magic Puffs / Shield + Vision + Talk to the Hand
      source: "[[sources/PLP-Gene|PLP-Gene]]"
      changes_capabilities:
        - 提高开阔图远距骚扰和探草能力
        - 强化队友续航和 Super 命中窗口
      enables:
        - pickoff_plan
        - vision_tax_payment
        - long_range_pull_threat
      mitigates_failure_modes:
        - 缺少直接输出时通过队友续航和视野换时间
      poor_when:
        - 我方阵容没有拉人后的爆发 follow-up
      bp_use: Bounty/Knockout 控制与抓单默认 build 候选
    - build: Lamp Blowout anti-aggro variant
      source: "[[sources/Fandom-Gene|Fandom-Gene]]"
      changes_capabilities:
        - 提高被刺客/坦克贴脸后的脱身能力
      enables:
        - anti_aggro_peel
        - pull_then_push_reset
      mitigates_failure_modes:
        - 被 Edgar/Mortis/Mico 等贴脸秒杀
      poor_when:
        - 地图开阔且需要 Vengeful Spirits 提供远程压力
      bp_use: 敌方已暴露突进威胁时的 build requirement

  map_feature_hooks:
    - map_feature_type: long_lane_chip_pull_vision
      uses_feature_by: 分裂弹远距消耗、Vision Gear 探草、Magic Hand 威慑关键站位
      objective_conversion: Bounty/Knockout 抓高价值目标，Gem Grab 抓 gem carrier 或保护中线
      active_when: 队友能接伤害，地图允许 Gene 安全蓄 Super
      fails_if: 敌方长狙压制 Gene 射程，或召唤物/墙角低成本挡手
      example_maps:
        - Shooting Star
        - Out in the Open
        - Hideout
      bp_use: pickoff_control_and_vision_support
    - map_feature_type: wall_pocket_magic_hand_pick
      uses_feature_by: Magic Hand 穿墙拉出躲墙目标
      objective_conversion: 把投掷/控场位从安全口袋转成可击杀目标
      active_when: 拉中后队友能立刻集火
      fails_if: 拉到的是召唤物、敌方有反开团、或己方缺爆发
      example_maps:
        - Belle's Rock
        - Layer Cake
        - Gem Fort
      bp_use: must_answer_thrower_pocket_candidate
    - map_feature_type: gem_carrier_countdown_pull
      uses_feature_by: 分裂弹和 Vision Gear 找到 carrier 退路线，Magic Hand 抓宝石位或保护者
      objective_conversion: 打断倒计时、迫使掉宝、或让己方重新进入宝石矿
      active_when: 敌方 carrier 需要经过中心入口、侧草或墙边撤退，队友可立刻补伤害
      fails_if: carrier 有召唤物/坦克身体挡手，或拉中后己方没有爆发完成击杀
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Double Swoosh
      bp_use: map_bp_factors.carrier_pull_and_countdown_break

  objective_contracts:
    - mode: Bounty_or_Knockout
      can_fulfill:
        - low_commitment_chip
        - key_target_pull
        - support_sustain
        - vision_control
      cannot_fulfill:
        - primary_burst_damage
        - hard_tank_body
      needs_teammate_support:
        - burst_followup
        - anti_sniper_or_anti_dive_cover
      false_positive: 只有拉人威胁但没有 follow-up 时，Gene 不能单独完成减员
    - mode: Gem Grab
      can_fulfill:
        - mid_control_support
        - punish_exposed_gem_carrier
        - countdown_pickoff
      cannot_fulfill:
        - guaranteed_safe_gem_carrier
      needs_teammate_support:
        - side_lane_pressure
        - secure_pick_after_pull
      false_positive: Spirit Slap 可能让低血宝石位在远处掉宝，需谨慎
    - mode: Brawl Ball
      can_fulfill:
        - pull_to_create_scoring_window
        - disrupt_enemy_defender
      cannot_fulfill:
        - primary_ball_carrier
        - direct_scoring_threat
      needs_teammate_support:
        - scorer_or_wallbreak
      false_positive: 不能把 Gene 当作持球推进核心

  failure_modes:
    - id: pull_without_followup
      active_when: 队友无法接伤害，或拉中目标后反被敌方前排/控制反打
      exposed_by: Fandom Super 机制与用户经验修正
      mitigation: 搭配爆发队友，或只拉高价值且可击杀目标
      bp_use: candidate_eval.required_support
    - id: outranged_or_poked_out
      active_when: 敌方 Piper/Mandy/Brock 等长线能在 Gene 蓄 Super 前压低血量
      exposed_by: PLP counteredBy
      mitigation: 视野、墙体、队友长线回应或 ban/pick 处理
      bp_use: must_answer_long_range_pressure
    - id: dive_pressure_without_Lamp_Blowout
      active_when: 敌方 Mico/Stu/Edgar/Mortis 等能贴脸，且 Gene 没有推开或队友保护
      exposed_by: Fandom Gadget 机制与 PLP counteredBy
      mitigation: Lamp Blowout、队友 peel、选择接近路线少的地图
      bp_use: build_requirement_or_avoid

  conditional_matchup_seeds:
    - target: Fang_or_Buzz_or_Carl
      direction: subject_favored
      source: "[[sources/PLP-Gene|PLP-Gene]]"
      mechanism: Gene 可用拉人、推开或队友集火打断进场节奏
      active_when: Gene 有队友 follow-up，敌方进场路径可预判
      fails_when: 目标能绕侧路贴脸，或 Gene 没有 Lamp Blowout/保护
      bp_use: response_pick_seed_against_linear_engage
    - target: Barley_or_Sprout_or_Squeak_or_Rico
      direction: subject_favored
      source: "[[sources/PLP-Gene|PLP-Gene]]"
      mechanism: Magic Hand 穿墙威胁会把墙后控场/弹墙位从安全口袋拉成可集火目标
      active_when: 地图墙体给 Gene 拉手机会，且己方有爆发或控制接拉
      fails_when: 目标有召唤物挡手、口袋过深、或 Gene 被长线压到无法攒 Super
      bp_use: wall_pocket_answer_seed
    - target: Piper_or_Mandy_or_Brock
      direction: target_favored
      source: "[[sources/PLP-Gene|PLP-Gene]]"
      mechanism: 极长射程在 Gene 拉人前消耗或逼退站位
      active_when: 地图长线开阔，Gene 缺掩体和队友压制
      fails_when: Gene 可借墙体、视野或队友压力安全攒 Super
      bp_use: avoid_first_pick_on_pure_long_range_maps
    - target: Mico_or_Stu_or_Eve_or_Mr_P
      direction: target_favored
      source: "[[sources/PLP-Gene|PLP-Gene]]"
      mechanism: 跳跃/机动/水域角度或 porter 身体会让 Gene 的慢弹道和单次拉手更难稳定命中核心目标
      active_when: 地图给目标侧路、跳墙、隔水或召唤物挡手，Gene 无法用队友先清资源
      fails_when: 路线被视野锁住，或 Gene 保留 Lamp Blowout / Magic Hand 等关键资源等真正进场
      bp_use: must_answer_mobility_or_body_block_before_gene

  slot_notes:
    slot_1: 不宜在纯长线且敌方有多个自然长狙答案时裸先；可在 Bounty/Knockout 需要控制和支援时作为可延展先手。
    slot_2_3: 适合回答敌方短手/进场计划，并与爆发队友成组建立抓单路线。
    slot_4_5: 适合修复己方缺控制/续航/探草的问题，但要防敌方 6 位补长狙或刺客。
    slot_6: 如果敌方三人缺召唤物、长线压制或贴脸答案，Gene 可以作为拉人惩罚位。
```

## 关联页面

- [[sources/Fandom-Gene|Fandom 来源摘要: Gene]]
- [[sources/PLP-Gene|PLP 来源摘要: Gene]]
- [[sources/User-Note-Gene-in-Brawl-Ball|用户经验来源摘要: Gene 在 Brawl Ball 中的模式适配修正]]
