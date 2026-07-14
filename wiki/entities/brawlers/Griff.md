# Griff

## 基本信息

- 稀有度：Epic
- 定位：Controller
- 类型：近中距离高爆发 / Piggy Bank 开墙 / Super 区域压制

## 来源摘要

- Fandom：[[sources/Fandom-Griff|Fandom 来源摘要: Griff]]
- PLP：[[sources/PLP-Griff|PLP 来源摘要: Griff]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Heist, Hot Zone

## 角色定位总结

Griff 的 BP 价值来自近中距离高额输出、Super 宽扇形压制和 `Piggy Bank` 的延迟破墙/击退。他的普攻名义上是长射程，但三波硬币完整卸完需要约 1 秒，远端很容易只打出部分伤害；真正强势的是敌方身体、坦克或目标位必须进入中近距离时，Griff 可以用普攻+Super 快速清人。Fandom 明确提示 Griff 在 Heist、Brawl Ball、Hot Zone 都能利用 Piggy Bank 和 Super 转目标，但也强调他在长距离对抗中受慢 unload 限制。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Griff|Fandom-Griff]]"
    plp: "[[sources/PLP-Griff|PLP-Griff]]"
    user_notes: none

  capability_vector:
    effective_range: long_nominal_but_best_mid_close
    projectile_reliability: medium; 普攻三波卸载慢，远端不稳定，近身多硬币命中很强
    burst: very_high_at_close_or_with_super
    sustained_dps: medium_high_if_target_stays_in_range
    objective_damage: high_heist_if_lane_win_or_safe_access
    mobility: low
    survivability: medium; Business Resilience 战斗中持续按缺失血量回血
    engage: low_medium; 主要守目标和惩罚进入者
    disengage: medium_with_Piggy_Bank_knockback_or_super_burst
    anti_aggro: high_if_entry_is_visible_and_ammo_available
    anti_tank: high; 近距离普攻和 Super 可快速处理身体
    wall_break: high_with_Piggy_Bank
    throw_or_wall_bypass: low; Piggy Bank lob is delayed utility, not sustained thrower pressure
    area_control: medium_high_with_super_or_Coin_Shower
    scouting_or_vision: low
    team_support: wallbreak_and_anti_body_space_creation
    spawnable_or_pet: Piggy_Bank_temporary_destructible_gadget
    crowd_control: Piggy_Bank_knockback
    terrain_destruction: Piggy_Bank_wall_break

  build_switches:
    - build: "Piggy Bank / Business Resilience / Shield, Damage"
      source: "[[sources/PLP-Griff|PLP-Griff]]"
      changes_capabilities:
        - "Piggy Bank 2.5 秒延迟后破墙、击退并造成范围伤害，适合门墙、safe 墙和敌方 cover"
        - "Business Resilience 每 2 秒回复缺失生命的一部分，让 Griff 能在目标位持续换血"
        - "Shield/Damage 提高中近距离反打容错和斩杀线"
      enables:
        - "Brawl Ball goal_wall_open"
        - "Heist safe_lane_pressure"
        - "Hot Zone zone_clear"
        - "anti_tank_mid_control"
      mitigates_failure_modes:
        - "low_mobility_under_pressure"
        - "close_body_trade"
      best_when: "敌方必须进入中近距离目标线，或地图有关键墙体可用 Piggy Bank 转换"
      poor_when: "敌方在极远开阔长线风筝，或 Piggy Bank 破墙后对面远程更受益"
      bp_use: default_wallbreak_anti_body_build
    - build: "Coin Shower zone or fixed-target variant"
      source: "[[sources/Fandom-Griff|Fandom-Griff]]"
      changes_capabilities:
        - "Coin Shower 在目标区域持续 5 秒造成伤害，Buffie 下半径逐渐扩大"
      enables:
        - "Hot Zone zone clear"
        - "Heist fixed defender or safe-area pressure"
      mitigates_failure_modes:
        - "direct_line_blocked"
      best_when: "地图目标点固定且不需要 Piggy Bank 破墙"
      poor_when: "比赛胜负取决于开关键墙或击退突进者"
      bp_use: fixed_area_control_variant

  map_feature_hooks:
    - map_feature_type: heist_piggy_bank_safe_lane_and_burst
      uses_feature_by: "Piggy Bank 可破 safe 侧墙/击退防守者，普攻和 Super 在接近后转高额 safe 或防守伤害"
      route_or_position: "safe wall、side lane、defender path、enemy safe corner"
      objective_conversion: "打开打库角度、逼回防、在边路赢线后把中近距离输出转成 safe damage"
      active_when: "Griff 能安全接近 safe lane，或队友提供开线/控线让他到达输出距离"
      fails_if: "敌方远程 race 更快，或破墙后敌方长手比我方更受益"
      example_maps:
        - Hot Potato
        - Pit Stop
        - Bridge Too Far
        - Kaboom Canyon
      bp_use: candidate_eval.heist_wallbreak_and_midrange_safe_pressure
    - map_feature_type: brawl_ball_piggy_bank_goal_open_and_burst
      uses_feature_by: "Piggy Bank 打开门墙或击退门前目标，Super/普攻清持球者和守门身体"
      route_or_position: "goal wall、goal-front defender、midfield ball lane、side grass push"
      objective_conversion: "开门、清守门员、制造射门窗口或防守持球推进"
      active_when: "队友有 scorer，Griff 有弹药/Super 或 Piggy Bank 可处理关键墙"
      fails_if: "破门路线被对方更快利用，或高机动 scorer 从侧路绕过 Griff 的爆发带"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
        - Pinball Dreams
      bp_use: slot_task.goal_wallbreak_and_anti_body_burst
    - map_feature_type: hot_zone_super_or_coin_shower_zone_clear
      uses_feature_by: "Super 宽扇形和 Coin Shower/Piggy Bank 可清站区身体、破隐藏点或封回区路线"
      route_or_position: "zone center、zone entrance、wall-adjacent hiding spot、re-entry path"
      objective_conversion: "把敌方身体推出/打出圈，拆掉掩体，给己方队友站区时间"
      active_when: "Griff 能在中近距离攻击 zone，队友负责稳定站区"
      fails_if: "敌方投掷/长手从圈外先推 Griff，或 Griff 被迫一个人站圈承受三人火力"
      example_maps:
        - Dueling Beetles
        - Open Business
        - Ring of Fire
        - Parallel Plays
      bp_use: map_bp_factors.zone_clear_and_wallbreak_support
    - map_feature_type: gem_mid_super_area_and_anti_body
      uses_feature_by: "Super 可覆盖 gem mine 或 carrier 退线，普攻近中距离爆发处理追击身体"
      route_or_position: "gem mine、center fort doorway、carrier countdown retreat、side grass mouth"
      objective_conversion: "保护 carrier、清矿区身体、迫使敌方 gem holder 离开安全路线"
      active_when: "Griff 不需要自己长期 carrier，且敌方必须进入中距离矿区/草口"
      fails_if: "敌方用极远长手或投掷压制 Griff，或召唤物/地雷让他先花弹药"
      example_maps:
        - Hard Rock Mine
        - Gem Fort
        - Double Swoosh
        - Crystal Arcade
      bp_use: map_bp_factors.midrange_anti_body_carrier_protection

  objective_contracts:
    - mode: Gem Grab
      can_fulfill:
        - "mine_entry_anti_body"
        - "carrier_retreat_super_pressure"
        - "wall_or_cover_clear_with_Piggy_Bank"
      cannot_fulfill:
        - "pure_long_range_mid_into_open_snipers"
        - "primary_carrier_under_multi_angle_pressure"
      needs_teammate_support:
        - "carrier_or_long_range_anchor"
        - "vision_or_spawnable_clear"
      false_positive: "Griff 的中近距离强，不等于能在开阔矿图当稳定长手 mid"
    - mode: Brawl Ball
      can_fulfill:
        - "goal_wallbreak"
        - "ball_carrier_burst"
        - "goal_defender_clear"
      cannot_fulfill:
        - "reliable_primary_scorer_without_speed_or_dash"
      needs_teammate_support:
        - "scorer_or_pass_receiver"
        - "anti_thrower_or_long_range_cover"
      false_positive: "开门本身不是进球，必须有队友把几何改变转化成射门"
    - mode: Heist
      can_fulfill:
        - "safe_lane_wallbreak"
        - "midrange_safe_damage_after_lane_win"
        - "defense_against_tank_safe_entry"
      cannot_fulfill:
        - "remote_open_lane_race"
      needs_teammate_support:
        - "primary_safe_DPS_or_lane_pressure"
        - "cover_against_long_range_or_thrower"
      false_positive: "Heist 价值取决于能否接近 safe lane，不能只看 PLP 模式标签"
    - mode: Hot Zone
      can_fulfill:
        - "zone_clear"
        - "anti_body_damage"
        - "cover_wallbreak_or_area_gadget"
      cannot_fulfill:
        - "solo_zone_body_without_support"
        - "long_range_open_duel"
      needs_teammate_support:
        - "zone_holder"
        - "range_or_thrower_answer"
      false_positive: "Griff 清区很强，但 Business Resilience 不是让他单人硬站三人火力"

  failure_modes:
    - id: slow_unload_long_range_tax
      active_when: "敌方在远端开阔长线换血，Griff 三波硬币难以完整命中"
      exposed_by: "[[sources/Fandom-Griff|Fandom-Griff]] slow unload and long-range struggle"
      mitigation: "选择中近距离目标图，或通过墙/草/队友压线缩短距离"
      bp_use: false_positive_filter.nominal_range_not_true_sniper
    - id: piggy_bank_delay_or_overbreak
      active_when: "Piggy Bank 2.5 秒延迟被躲开，或破墙让敌方长手/突进获得更好路线"
      exposed_by: "[[sources/Fandom-Griff|Fandom-Griff]] Piggy Bank delay and wallbreak"
      mitigation: "破墙前指定受益方、墙位和 follow-up，不把 Piggy Bank 当免费开图"
      bp_use: terrain_state_plan_check
    - id: low_mobility_kite_pressure
      active_when: "Stu、Crow、Colt、Spike、Bo 等在 Griff 有效范围外持续移动、减速或布雷"
      exposed_by: "[[sources/PLP-Griff|PLP-Griff]] target_favored list"
      mitigation: "用墙体/队友限制路线，或后手确认敌方缺风筝空间"
      bp_use: candidate_eval.mobility_and_range_check
    - id: resource_or_spawnable_ammo_tax
      active_when: "敌方炮台、地雷、召唤物或替身让 Griff 的慢 unload 打到错误资源"
      exposed_by: "PLP target_favored includes Bo and Fandom notes on obstacles/area control"
      mitigation: "队友先清资源，或用 Piggy Bank/Super 同时处理资源与真实目标"
      bp_use: enemy_resource_filter

  conditional_matchup_seeds:
    - target: Nita_or_Poco_or_Colette_or_Janet
      direction: subject_favored
      source: "[[sources/PLP-Griff|PLP-Griff]]"
      mechanism: "Griff 的中近距离爆发、宽 Super 和开墙能力能惩罚固定支援、资源位或需要进入目标区域的中等身板"
      active_when: "目标必须守矿区、球路、热区或 safe 防守线，且无法在远端白打 Griff"
      fails_when: "召唤物/队友保护吃掉 Griff 弹药，或目标从极远角度持续输出"
      bp_use: midrange_burst_response_to_static_control
    - target: Sam_or_Rosa_or_Darryl_or_Bull
      direction: subject_favored
      source: "[[sources/PLP-Griff|PLP-Griff]] / [[sources/Fandom-Griff|Fandom-Griff]]"
      mechanism: "近距离多硬币命中和 Super burst 对进入 safe、球门或热区的身体目标伤害极高，Piggy Bank 可击退或拆掩体"
      active_when: "身体目标必须走可见入口，Griff 有弹药和距离，队友能补控制"
      fails_when: "他们从草/墙先手贴脸并逼 Griff 空弹，或有强控制保护进场"
      bp_use: anti_body_if_entry_visible
    - target: Surge_or_Spike_or_Bo_or_Buzz_or_Colt_or_Fang_or_Stu_or_Crow
      direction: target_favored
      source: "[[sources/PLP-Griff|PLP-Griff]]"
      mechanism: "升级/减速/地雷/射程/突进/毒和高机动会让 Griff 难以保持中近距离完整 unload，并惩罚他低机动站位"
      active_when: "地图给他们开阔 kite、侧草突进或资源预铺，Griff 无法先破关键墙或逼近"
      fails_when: "墙体/队友控制限制他们路线，Griff 只在目标点反打进入者"
      bp_use: must_answer_kite_or_resource_before_griff
    - target: Goal_wall_or_safe_wall_or_zone_cover
      direction: subject_favored
      source: "[[sources/Fandom-Griff|Fandom-Griff]]"
      mechanism: "Piggy Bank 可延迟破墙并 knockback，直接改变球门、金库和热区掩体状态"
      active_when: "破墙后我方 scorer、safe DPS 或 zone holder 更受益"
      fails_when: "开墙同时给敌方长手/突进更清晰路线"
      bp_use: terrain_state_plan.objective_wallbreak

  slot_notes:
    slot_1: "只有地图目标天然进入中近距离、且敌方难以用极远长手风筝时才早手；否则名义长射程会被惩罚。"
    slot_2_3: "适合作为目标图 anti-body 和开墙计划手，但队伍要补 scorer、carrier 或站区主体。"
    slot_4_5: "看到敌方坦克/身体或固定目标位后，Griff 可后手压制；同时避免敌方最后手拿高机动/远程资源。"
    slot_6: "最适合惩罚已经暴露的低机动身体阵容或补关键 Piggy Bank 地形转换。"
```

## 关联页面

- [[sources/Fandom-Griff|Fandom 来源摘要: Griff]]
- [[sources/PLP-Griff|PLP 来源摘要: Griff]]
- [[sources/BSC-2026-July-Observed-Map-Fit-Review|BSC 2026 July 地图适配复核]]
