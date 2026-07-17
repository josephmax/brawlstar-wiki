# Ruffs

## 基本信息

- 稀有度：Mythic
- 定位：Support
- 类型：弹墙压线、团队增益与选择性开墙支援

## 攻击特征

- 主攻击 `Double-Barrel Laser` 发射两道平行激光，射程长、装填快，并可在墙上独立反弹。
- 弹墙让 Ruffs 在封闭路线中能安全打到掩体后的目标，但激光很窄，面对高机动或宽范围压制时需要手动瞄准和队友保护。
- 低血量意味着他更依赖距离、沙包、墙角和队友占位，而不是单人硬站目标区。

## 超级技能特征

- Super `Supply Drop` 落地造成伤害和击退，并留下队友可拾取的强化：提升伤害并增加最大生命。
- `Take Cover` 生成三个沙包，可挡非穿透/非弹墙的窄弹道。
- `Air Superiority` 让 Supply Drop 破坏障碍并增加落地伤害，是 Brawl Ball 破门、反投掷和地形转换的关键 build。
- `Field Promotion` 在慢节奏模式中可长期提高队友最大生命，但会暴露隐身或草中位置。

## 角色定位总结

Ruffs 是“长线支援 + 可选择开墙 + 团队强化”的功能位。他的 BP 价值不是自己成为最高输出，而是让队友的长线、前排或目标位获得额外血量/伤害，同时用弹墙、沙包和 Super 落点改变局部对位。选他时必须确认队友能吃到强化并把它转成星差、进球、站圈或 safe race。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-07-17
    plp: direct_raw_capture_2026-06-30
    user_notes: none

  capability_vector:
    effective_range: long
    projectile_reliability: medium_high_with_bounce_angles; 激光窄但射程长、装填快、可弹墙
    burst: medium; Supply Drop/Air Superiority 提供短窗口爆发
    sustained_dps: medium_high_if_lines_available
    objective_damage: medium_supportive; 可 buff safe DPS 或用 Air Support/Super 辅助，不是单独主 race
    mobility: low
    survivability: low_base_health_but_medium_with_Take_Cover_or_range
    engage: low
    disengage: medium_with_sandbags_or_knockback
    anti_aggro: conditional; 沙包/击退/队友 buff 可拖近身，但怕穿透、弹墙、投掷和硬突进
    anti_tank: medium_with_buffed_teammates_and_wallbreak
    wall_break: high_with_Air_Superiority
    throw_or_wall_bypass: medium; 弹墙和 Super 落点可打掩体后目标
    area_control: medium_with_supply_drop_or_air_support
    scouting_or_vision: low
    team_support: very_high; 伤害/生命强化、沙包和开墙稳定存在；完整队友 Hypercharge 充能只来自 Ruffs 自己的 Hypercharged Supply Drop，当前 35% 充能倍率使其是稀缺窗口而非每个补给包的常驻效果
    spawnable_or_pet: sandbags_as_temporary_cover
    crowd_control: knockback_on_supply_drop_or_air_support
    terrain_destruction: high_with_Air_Superiority

  build_switches:
    - build: Take Cover / Air Superiority / Shield + Damage
      source: "[[sources/PLP-Ruffs|PLP-Ruffs]] / [[sources/Fandom-Ruffs|Fandom-Ruffs]]"
      changes_capabilities:
        - Take Cover 改善对 sniper-heavy 阵容的站线容错
        - Air Superiority 把 Supply Drop 变成开墙、破门和反投掷工具
        - Shield/Damage 提高低血长线的容错和交易质量
      enables:
        - bounce_lane_support
        - selective_wallbreak
        - teammate_buff_snowball
      mitigates_failure_modes:
        - 低血量被单体长线消耗
        - 队伍缺少低成本开墙
      poor_when:
        - 敌方主要用投掷/穿透/弹墙绕开沙包，或队友无法安全拾取补给
      bp_use: 默认竞技 build；适合大多数需要支援、开墙或挡线的 draft
    - build: Field Promotion Knockout_or_slow_mode_variant
      source: "[[sources/PLP-Ruffs|PLP-Ruffs]] / [[sources/Fandom-Ruffs|Fandom-Ruffs]]"
      changes_capabilities:
        - 慢节奏中持续提高队友最大生命，特别保护低血长手/投掷
      enables:
        - knockout_survival_buffer
        - long_lane_teammate_protection
      mitigates_failure_modes:
        - 低血队友被一发或两发长线击杀
      poor_when:
        - Brawl Ball 等快节奏模式中队友难以长期站在 Ruffs 附近，或队伍需要 Air Superiority 开墙
      bp_use: Knockout/Bounty 慢节奏且不缺开墙时的 build requirement
    - build: Air Support choke_or_safe_pressure_variant
      source: "[[sources/Fandom-Ruffs|Fandom-Ruffs]]"
      changes_capabilities:
        - 对最近敌人周围连续落弹，可迫使目标离开 choke 或给 Heist safe 附加伤害
      enables:
        - choke_displacement
        - auxiliary_safe_pressure
      mitigates_failure_modes:
        - Ruffs 主攻击无法直接命中墙后或角落目标
      poor_when:
        - 更需要 Take Cover 抵挡 sniper 或保护低血队友
      bp_use: 对方固定站口袋/安全线时的条件 Gadget

  map_feature_hooks:
    - map_feature_type: bounce_wall_corridor_pressure
      uses_feature_by: 利用墙体反弹双激光，从安全角度打到走廊、侧墙或投掷口袋后方
      objective_conversion: 线权、保星、控矿和边路防守
      active_when: 墙体完整且反弹角度能打到目标，敌方没有投掷或穿透绕开 Ruffs
      fails_if: 地图被开成纯长线、敌方有稳定投掷/弹墙反制，或 Ruffs 需要站到危险角度才有线
      example_maps:
        - Belle's Rock
        - Layer Cake
        - Pinball Dreams
        - Hard Rock Mine
        - Gem Fort
      bp_use: candidate_eval.bounce_wall_support_lane
    - map_feature_type: supply_drop_buff_long_lane_core
      uses_feature_by: 把补给包给低血长手、投掷或主输出，让其多吃一发并提升伤害
      objective_conversion: Bounty/Knockout 保星、长线对枪、回合领先后撤退
      active_when: 队友能安全拾取补给，并且 buff 后可以继续站线或保 lead
      fails_if: 队友拿不到补给、死亡会丢 buff，或敌方用投掷/刺客直接越过沙包打 Ruffs
      example_maps:
        - Shooting Star
        - Dry Season
        - Out in the Open
        - Belle's Rock
        - Layer Cake
      bp_use: map_bp_factors.long_lane_buff_snowball
    - map_feature_type: air_superiority_goal_or_pocket_wallbreak
      uses_feature_by: Air Superiority Supply Drop 破坏关键墙体，打断门前/口袋防守并改变 terrain_state
      objective_conversion: Brawl Ball 破门、反投掷、打开长线或清除守点掩体
      active_when: 某一面墙保护敌方门前、投掷或中心口袋，开墙后我方远程/得分手更受益
      fails_if: 开墙帮助敌方远程接管，或我方阵容本身依赖这面墙生存
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
        - Pinball Dreams
        - Belle's Rock
        - Gem Fort
      bp_use: terrain_state_plan.selective_wallbreak_support
    - map_feature_type: heist_buffed_lane_and_safe_support
      uses_feature_by: 给主要 safe DPS 或防守身体补血量/伤害，Air Support 或 Super 作为辅助打库/驱赶入口
      objective_conversion: 提高 lane race、保住弱侧、延长己方 DPS 对 safe 的输出时间
      active_when: 我方已有主 safe DPS，Ruffs 负责 buff、弹墙支援和开墙/驱赶
      fails_if: 队伍缺主 DPS，或 Ruffs 被要求单独赢 isolated Heist lane
      example_maps:
        - Bridge Too Far
        - Kaboom Canyon
        - Hot Potato
        - Safe Zone
      bp_use: candidate_eval.heist_support_buff_not_primary_race

  objective_contracts:
    - mode: Bounty_or_Knockout
      can_fulfill:
        - buff_low_health_long_lane_core
        - Take_Cover_sniper_tax
        - bounce_wall_pressure
      cannot_fulfill:
        - solo_open_lane_hard_carry_without_teammate_conversion
        - reliable_anti_thrower_without_Air_Superiority_or_route
      needs_teammate_support:
        - teammate_who_can_use_supply_drop
        - anti_thrower_or_vision
      false_positive: Ruffs 自己低血，补给包价值必须转给能赢线的队友
    - mode: Brawl Ball
      can_fulfill:
        - selective_goal_wallbreak
        - knockback_or_drop_disarm
        - buff_scorer_or_defender
      cannot_fulfill:
        - primary_ball_carrier
        - reliable_grass_scout
      needs_teammate_support:
        - scorer_or_goal_pressure
        - anti_grass_or_anti_tank
      false_positive: 开门只在我方有得分后续时有价值，否则可能帮敌方远程
    - mode: Heist_or_Hot Zone_or_Gem Grab
      can_fulfill:
        - support_main_DPS_or_zone_body
        - selective_wallbreak_or_bounce_lane
        - sandbag_projectile_tax
      cannot_fulfill:
        - primary_zone_body
        - primary_safe_race_alone
      needs_teammate_support:
        - actual_objective_body_or_safe_DPS
        - thrower_or_dive_answer
      false_positive: PLP 全模式适配不能理解为无条件强；Ruffs 必须有队友把 buff 转成目标收益

  failure_modes:
    - id: low_health_and_sandbag_bypass
      active_when: 敌方有投掷、穿透、弹墙、召唤物或强突进能绕过 Take Cover
      exposed_by: Fandom Take Cover 只挡非穿透/非弹墙窄弹道
      mitigation: 使用距离、墙角、队友 peel 或改成开墙/反投掷计划
      bp_use: false_positive_filter
    - id: buff_without_conversion
      active_when: 队友无法安全拾取补给，或拾取后不能转成线权/目标输出
      exposed_by: Fandom Supply Drop buff 机制与 BP objective_contract
      mitigation: 优先搭配长线核心、safe DPS、站圈身体或高价值 carrier
      bp_use: role_coverage_check
    - id: terrain_transform_backfires
      active_when: Air Superiority 开墙后敌方远程/突进比我方更受益
      exposed_by: BP 地图建模与决策规范与 Brawl Ball/Knockout map rules
      mitigation: 只开关键墙，或在 draft 中确认我方有开墙后的远程/得分后续
      bp_use: terrain_state_plan_check
    - id: support_tempo_too_slow
      active_when: 快节奏进球、站圈或 safe race 不给 Ruffs 连续发包/站位时间
      exposed_by: Fandom buff 需拾取且死亡/进球会丢失
      mitigation: 选择即时开墙/沙包价值，或避免把 Ruffs 当作唯一节奏来源
      bp_use: slot_fit_risk
    - id: hypercharge_transfer_not_baseline
      active_when: 阵容把“补给包充满队友 Hypercharge”当作每次 Super 都有的稳定团队循环
      exposed_by: "[[sources/Fandom-Ruffs|Fandom-Ruffs]] 只有 Ruffs 的 Hypercharged Supply Drop 才会充满拾取者 Hypercharge，Ruffs 当前 Hypercharge multiplier 为 35%"
      mitigation: 把普通补给只按伤害/最大生命增益结算；只有明确追踪到 Ruffs Hypercharge 时才预算一次队友 Hypercharge 转移
      bp_use: resource_tracking.ruffs_hypercharge_transfer

  conditional_matchup_seeds:
    - target: Cordelius_or_Gigi_or_Lola_or_Meg
      direction: subject_favored
      source: "[[sources/PLP-Ruffs|PLP-Ruffs]]"
      mechanism: 长射程弹墙、沙包挡线和补给 buff 可以让队友/自己在中长距离换血中压过这些需要接近或站位输出的目标
      active_when: 地图有墙角或长线让 Ruffs 安全支援，目标不能直接越过沙包碰到 Ruffs
      fails_when: Cordelius/高机动从草墙直接隔离，或 Lola/Meg 在队友保护下先逼退 Ruffs
      bp_use: support_lane_response_not_unconditional_counter
    - target: Darryl_or_Shelly_or_R-T_or_Maisie
      direction: subject_favored
      source: "[[sources/PLP-Ruffs|PLP-Ruffs]]"
      mechanism: 补给提高队友生存和伤害，Supply Drop 击退/开墙可打断直线进场或掩体站位
      active_when: 敌方需要穿过可见 route，Ruffs 队友能利用 buff 集火
      fails_when: 目标有多路线近身、穿透/范围清沙包，或 Ruffs 队伍缺实际 damage follow-up
      bp_use: team_buffed_anti_body_response
    - target: Barley_or_Larry_and_Lawrie_or_Sandy_or_Nita
      direction: target_favored
      source: "[[sources/PLP-Ruffs|PLP-Ruffs]]"
      mechanism: 投掷、沙暴/草控、召唤物和范围压力可以绕过沙包，消耗低血 Ruffs 并阻止队友安全拾取补给
      active_when: 墙体/草丛保护这些资源，Ruffs 没有 Air Superiority 清墙或队友先清资源
      fails_when: 关键墙被开，召唤物被清，Ruffs 只负责后排 buff 而不站危险点
      bp_use: must_answer_wall_or_spawnable_before_ruffs
    - target: Damian_or_Frank_or_Rosa_or_Ollie
      direction: target_favored
      source: "[[sources/PLP-Ruffs|PLP-Ruffs]]"
      mechanism: 高血量、控制或强目标身体能压缩 Ruffs 的低血站位，并让补给包节奏来不及改变第一波接触
      active_when: 模式目标要求近距离站点/推进，敌方能在沙包被绕开或清掉后开团
      fails_when: Ruffs 提前 buff 反坦队友，Air Superiority 打开路线并保持远程集火
      bp_use: avoid_support_without_body_answer

  slot_notes:
    slot_1: 可以在队友/地图职责明确会用到 buff、开墙或弹墙支援时先手；不要在缺目标核心时裸选。
    slot_2_3: 适合作为回答 sniper-heavy、门墙/投掷口袋或需要团队强化的成组 pick。
    slot_4_5: 用来补开墙、保护己方核心或给前两手加成，但必须避免被敌方 6 位投掷/刺客一手拆掉低血支援。
    slot_6: 敌方缺投掷、缺穿透且已经暴露固定长线/墙角对位时，Ruffs 可作为高质量支援惩罚。
```

## 关联页面

- [[sources/Fandom-Ruffs|Fandom 来源摘要: Ruffs]]
- [[sources/PLP-Ruffs|PLP 来源摘要: Ruffs]]
- [[entities/brawlers/Pam|Pam]]
- [[entities/brawlers/Poco|Poco]]
- [[entities/brawlers/Max|Max]]
