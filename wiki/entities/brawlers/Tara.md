# Tara

## 基本信息

- 稀有度：Mythic
- 定位：Damage Dealer
- 类型：聚怪开团、探草和召唤物压制英雄

## 攻击特征

- 主攻击 `Triple Tarot` 一次发出三张可穿透卡牌，远端容易命中一到两张，近距离爆发更高。
- 装填较慢，Super 前需要谨慎保存弹药，否则拉到人也可能无法完成击杀。
- 穿透让 Tara 能惩罚抱团、召唤物后站位和门前防守堆叠。

## 超级技能特征

- Super `Gravity` 会把范围内敌人向中心拉拢，随后爆炸、击退并破坏中心附近障碍。
- `Psychic Enhancer` 可短时让全队看见草里或隐身敌人。
- `Support From Beyond` 召唤三个低血影子，可追击、挡单体弹道或压迫安全输出位。
- `Healing Shade` 提供跟随治疗，但治疗特效可能暴露草丛站位。

## 角色定位总结

Tara 的 BP 价值是“把敌方分散站位强行变成可被惩罚的团战窗口”。她不是稳定长线，也不是纯坦克答案；她需要地图目标让敌人必须靠近宝石矿、球门、草丛或窄口，并需要队友能在 Gravity 命中后立刻转换击杀、进球或控矿。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-06-30-v2
    plp: direct_raw_capture_2026-06-30
    user_notes: none

  capability_vector:
    effective_range: mid_long_with_close_burst
    projectile_reliability: medium; 三张卡有扩散和穿透，近中距离更稳定，纯开阔远线不稳定
    burst: high_after_Gravity_or_close_three_card_hits
    sustained_dps: medium_low_reload
    objective_damage: medium_conditional; Support From Beyond/Black Portal 可给 Heist safe 短窗口伤害
    mobility: low
    survivability: medium_low; 依赖 Super、召唤物或 Healing Shade 保护
    engage: high_when_Super_charged
    disengage: medium; Super 可向身后扔来拉开追击者
    anti_aggro: conditional_high_with_Gravity_ready
    anti_tank: medium; 拉近后伤害高，但高血量目标需要队友接伤害
    wall_break: conditional_with_Super_center_or_Hypercharge
    throw_or_wall_bypass: low
    area_control: medium_high_with_Gravity_threat
    scouting_or_vision: high_with_Psychic_Enhancer_or_shadows
    team_support: medium; 视野、召唤物挡枪、Healing Shade、聚怪开团
    spawnable_or_pet: high
    crowd_control: high_with_pull
    terrain_destruction: conditional_with_Super

  build_switches:
    - build: Support From Beyond / Healing Shade / Shield + Damage + Speed
      source: "[[sources/PLP-Tara|PLP-Tara]] / [[sources/Fandom-Tara|Fandom-Tara]]"
      changes_capabilities:
        - Support From Beyond 提供三具影子，用于挡单体弹道、逼退长手或短窗口打库
        - Healing Shade 把 Gravity 后续转换成团队续航
        - Speed gear 强化草图中的侧压和 Super 角度
      enables:
        - gem_grab_teamfight_swing
        - brawl_ball_goal_pull
        - single_target_ammo_tax
      mitigates_failure_modes:
        - Tara 直接走脸前被长手消耗
        - 队友缺少拉中后的续航
      poor_when:
        - 敌方范围/穿透/召唤物清理太强，影子无法接近或挡枪
      bp_use: 默认竞技 build；适合 Gem Grab/Brawl Ball 目标区会聚集的局
    - build: Psychic Enhancer vision_variant
      source: "[[sources/Fandom-Tara|Fandom-Tara]]"
      changes_capabilities:
        - 给全队短时显形草丛和隐身目标
        - 把草图伏击从猜测变成可处理路线
      enables:
        - bush_scouting
        - anti_stealth_or_ambush_plan
      mitigates_failure_modes:
        - 草丛侧路绕后威胁 gem carrier 或球路
      poor_when:
        - 地图缺草或队友不能利用显形开团/扫草
      bp_use: Double Swoosh、Sneaky Fields、Center Stage、Ring of Fire 等草图的 build requirement
    - build: Black Portal offensive_shadow_variant
      source: "[[sources/Fandom-Tara|Fandom-Tara]]"
      changes_capabilities:
        - Gravity 后生成攻击影子，用于追击低血、探草或给 Heist safe 附加伤害
      enables:
        - post_pull_cleanup
        - bush_probe
        - short_heist_burst
      mitigates_failure_modes:
        - Gravity 命中后敌人残血逃离
      poor_when:
        - 队伍更需要 Healing Shade 的续航来保目标
      bp_use: 需要更强进攻转换而非续航时的条件 build

  map_feature_hooks:
    - map_feature_type: gem_mine_gravity_swing
      uses_feature_by: 在宝石矿、中心入口或倒计时撤退路线上用 Gravity 拉多人或拉 carrier
      objective_conversion: 造成 gem drop、打断倒计时、把中路小优势转成团灭窗口
      active_when: 敌方必须靠近矿区或中心墙角，Tara 有 Super 且队友能接范围伤害
      fails_if: 敌方分散站位、用召唤物/墙体拖 Super，或 Tara 装填不足无法补伤害
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Double Swoosh
      bp_use: map_bp_factors.gem_teamfight_or_carrier_pull
    - map_feature_type: brawl_ball_goal_pull_and_wallbreak
      uses_feature_by: Gravity 把门前防守/持球人拉到一起，并用爆炸中心破坏关键门墙或制造射门线
      objective_conversion: 得分窗口、反推进、门前团灭
      active_when: 球路经过门前 choke 或草口，队友有射门/范围伤害跟进
      fails_if: 敌方拆散站位、先骗 Super，或开墙结果更利于敌方远程反打
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Pinball Dreams
        - Triple Dribble
      bp_use: slot_task.scoring_window_creator
    - map_feature_type: bush_vision_and_ambush_control
      uses_feature_by: Psychic Enhancer 揭示草中/隐身敌人，影子可探路或挡第一发单体弹道
      objective_conversion: 保护 gem carrier、抢球、避免草丛侧压和倒计时伏击
      active_when: 地图草丛连接目标区，敌方依赖隐蔽接近或 side flank
      fails_if: 敌方用范围清理影子、草被烧掉后 Tara 缺长线，或队友不能利用显形反打
      example_maps:
        - Double Swoosh
        - Sneaky Fields
        - Center Stage
        - Ring of Fire
        - Hard Rock Mine
      bp_use: required_capabilities.bush_reveal_or_anti_stealth
    - map_feature_type: central_congestion_teamwipe_combo
      uses_feature_by: 在中路抱团、门前推进或层口争夺时用 Gravity 聚怪接队友范围技能
      objective_conversion: 团灭、星差反转、球权或矿区重置
      active_when: 敌方为了目标必须多人站近，且我方有 Squeak/Barley/Spike/Colt/Pearl 等后续范围伤害
      fails_if: 敌方三线分散、Tara Super 未充好，或没有队友跟伤害
      example_maps:
        - Triple Dribble
        - Gem Fort
        - Layer Cake
      bp_use: candidate_eval.combo_teamfight_swing

  objective_contracts:
    - mode: Gem Grab
      can_fulfill:
        - mine_teamfight_swing
        - carrier_pull_or_countdown_break
        - bush_vision_support
      cannot_fulfill:
        - passive_long_range_carrier
        - solo_mid_without_super_cycle
      needs_teammate_support:
        - followup_damage_after_pull
        - side_lane_control_until_super_is_ready
      false_positive: 没有 Super 的 Tara 只是中距离慢装填英雄，不能当稳定中路先手
    - mode: Brawl Ball
      can_fulfill:
        - goal_pull
        - wallbreak_score_window
        - anti_scorer_pull
      cannot_fulfill:
        - primary_ball_carrier
        - reliable_wallbreak_without_super
      needs_teammate_support:
        - scorer_or_ball_handler
        - range_or_area_followup
      false_positive: 只看击杀不够；Gravity 必须转换成射门、抢球或反推进
    - mode: Heist
      can_fulfill:
        - short_shadow_safe_burst_if_safe_is_clear
        - pull_defenders_or_bodyguards
      cannot_fulfill:
        - stable_remote_safe_DPS
      needs_teammate_support:
        - primary_safe_race
        - lane_control_to_keep_shadows_on_safe
      false_positive: Support From Beyond 打库只在 safe 附近没有敌人吸引影子时成立

  failure_modes:
    - id: no_super_low_threat_window
      active_when: Tara 未充好 Gravity，或开团前弹药不足
      exposed_by: Fandom 慢装填与 Super 依赖
      mitigation: 队友帮忙控线充 Super，保留三发弹药再开团
      bp_use: tempo_and_slot_risk
    - id: open_long_range_kite
      active_when: Piper/Mandy/Belle/Nani 等在纯开阔长线保持距离，Tara 无法进入 Super 范围
      exposed_by: PLP matchup seed 与长线地图模型
      mitigation: 草丛/墙体路线、Speed gear、队友压迫或避免早手暴露
      bp_use: false_positive_filter
    - id: summon_clear_or_body_block
      active_when: Penny/Nita/Emz/Sandy 等用范围、召唤物或持续控制快速清影子并拖 Super
      exposed_by: PLP counteredBy 与 Fandom 影子低血机制
      mitigation: 先用视野或队友清资源，再用 Gravity 打真实目标
      bp_use: must_answer_resource_before_tara_plan
    - id: healing_shade_reveals_position
      active_when: 草图中 Healing Shade 的治疗效果暴露 Tara 或队友位置
      exposed_by: Fandom Recommended Build tips
      mitigation: 根据草控需求改用 Black Portal 或谨慎放 Super
      bp_use: build_requirement_check

  conditional_matchup_seeds:
    - target: Nani_or_Tick_or_Mandy_or_Piper_or_Belle
      direction: subject_favored
      source: "[[sources/PLP-Tara|PLP-Tara]]"
      mechanism: Support From Beyond 可挡单体弹道或迫使脆弱长手/投掷转火，Gravity 命中后可直接把远程拖入队友爆发
      active_when: 地图有草墙路线或目标迫使长手靠近矿区/门前，Tara 有 Super 或召唤物可启动
      fails_when: 地图纯开阔且对手保持极限距离，或召唤物被范围技能立即清掉
      bp_use: response_pick_into_fragile_range_when_route_exists
    - target: Lou_or_Meg_or_Jae_yong
      direction: subject_favored
      source: "[[sources/PLP-Tara|PLP-Tara]]"
      mechanism: Gravity 能打断目标区控制/团队节奏并把多个站点身体拉进范围伤害
      active_when: 敌方为了站圈、推进或护 carrier 必须聚在中距离
      fails_when: 对方分散站位并用长手先压 Tara，或 Tara 队友没有范围 follow-up
      bp_use: teamfight_swing_response
    - target: Penny_or_Nita_or_Emz_or_Sandy
      direction: target_favored
      source: "[[sources/PLP-Tara|PLP-Tara]]"
      mechanism: 召唤物、炮台、范围喷射或视野/控场能吸收 Tara 资源，清掉影子并阻止她安全靠近 Super 范围
      active_when: 地图有目标区拥挤或草墙保护这些资源，Tara 队伍缺清召唤物/开墙
      fails_when: Tara 先用 Gravity 命中真实目标，或队友提前清掉资源
      bp_use: must_answer_spawnable_or_area_before_tara
    - target: Damian_or_Shade_or_Edgar_or_Janet
      direction: target_favored
      source: "[[sources/PLP-Tara|PLP-Tara]]"
      mechanism: 高机动、特殊路线或空中/墙体路径能让 Tara 难以把 Gravity 留给真实接触点
      active_when: 地图有侧路、草墙或跳跃路线，且 Tara 被迫先交 Super 或被分散牵制
      fails_when: 进入路线单一，Psychic Enhancer/队友视野锁住 first contact
      bp_use: avoid_without_route_vision_or_peel

  slot_notes:
    slot_1: 不宜在纯长线图早手；只有 Gem/Ball 草墙目标明确且队伍可围绕 Gravity 转换时才稳。
    slot_2_3: 适合作为回答敌方长手/投掷或建立团队开团计划的一手，但要配实际 follow-up。
    slot_4_5: 用来修补缺探草、缺强控得分或缺 carrier 翻盘的问题，同时检查敌方 6 位是否能用召唤/范围/机动拆她。
    slot_6: 敌方三人缺显形、缺分散能力、门前或矿区必须聚集时，Tara 可以作为高收益团战惩罚。
```

## 关联页面

- [[sources/Fandom-Tara|Fandom 来源摘要: Tara]]
- [[sources/PLP-Tara|PLP 来源摘要: Tara]]
