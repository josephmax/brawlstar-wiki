# Squeak

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：延迟粘弹 / chokepoint 控制 / Windup 长线补刀

## 来源摘要

- Fandom：[[sources/Fandom-Squeak|Fandom 来源摘要: Squeak]]
- PLP：[[sources/PLP-Squeak|PLP 来源摘要: Squeak]]
- PLP 推荐模式：Hot Zone、Bounty、Knockout

## 角色定位总结

Squeak 是用 `Sticky Blomb` 延迟爆炸封路的 Controller。普攻会粘在目标或障碍物上，1.15 秒后造成 2.67 格范围伤害；爆炸可伤害墙后目标，但没有即时 burst。Super 会落地后分出 6 个固定 60 度角的小粘弹，适合封 chokepoint 或安全区。PLP 默认 `Windup / Chain Reaction / Shield, Damage`，强调长线补刀和 grouped target 伤害；Hot Zone 里则要考虑 PLP 注记的 `Residue` 变体，用 6 秒揭草/slow 区域服务站区。

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
    effective_range: "long_control; 普攻 7.67 格，Windup 下一发 15.33 格"
    projectile_reliability: "medium_on_routes_low_vs_dash; 1.15 秒延迟，命中后靠路线限制转化"
    burst: "low_immediate_medium_delayed; 可多 blomb 叠目标瞬爆，但不能即时防守"
    sustained_dps: "low_medium; 2.1 秒 slow reload，强调布区而非连发"
    objective_damage: "situational_super_burst; Super 可对 safe/固定目标多 blob 命中"
    mobility: "low; 无位移"
    survivability: "medium_low; 3800 HP，需要距离和队友覆盖近身"
    engage: "low; 通过预铺区域逼退，不主动开团"
    disengage: "medium_with_residue_or_super; slow/reveal 区和 Super 封路能拖追击"
    anti_aggro: "medium_if_route_closed; 延迟爆炸对固定入口有效，但怕即时 burst"
    anti_tank: "medium; 大范围粘弹可逼坦克绕路，但缺硬控和即时伤害"
    wall_break: "none"
    throw_or_wall_bypass: "high_area; 爆炸可伤害墙后目标，粘弹可贴障碍"
    area_control: "very_high; 普攻/Super/Residue 封 chokepoint、草区和目标点"
    scouting_or_vision: "high_with_residue; Residue 6 秒揭草并 slow"
    team_support: "medium; 延迟区把敌人赶进队友射线"
    spawnable_or_pet: "sticky_blombs_limited; 地图上 Sticky Blomb 上限 10 个"
    crowd_control: "slow_variant; Residue slow 1.05 秒，Super Sticky 4 秒 slow"
    source_trace:
      - "[[sources/Fandom-Squeak|Fandom-Squeak]]"
      - "[[sources/PLP-Squeak|PLP-Squeak]]"

  build_switches:
    - build: "Windup / Chain Reaction / Shield, Damage"
      source: "[[sources/PLP-Squeak|PLP-Squeak]]"
      changes_capabilities:
        - "Windup 让下一发射程翻倍到 15.33 格并提高 50% 伤害"
        - "Chain Reaction 对爆炸半径内每个敌方 Brawler 线性增加 15% 伤害，至少命中一个 Brawler 时有额外收益"
      enables:
        - "Bounty / Knockout 长线补刀"
        - "grouped target 惩罚"
        - "跨线支援和回合开局区域压迫"
      mitigates_failure_modes:
        - "low_range_finish_without_windup"
        - "grouped_targets_survive_single_blomb"
      best_when: "敌方必须站在 choke、墙边或回合末固定区域，且 Squeak 能安全预瞄"
      poor_when: "敌方高速突进、分散站位或能在延迟爆炸前离开"
      bp_use: "default_plp_long_control_build"
    - build: "Residue / Super Sticky variant"
      source: "[[sources/Fandom-Squeak|Fandom-Squeak]] / [[sources/PLP-Squeak|PLP-Squeak]]"
      changes_capabilities:
        - "Residue 爆炸后留下 2.5 格半径区域，6 秒揭草并在接触时 slow 1.05 秒"
        - "Super Sticky 让 Super 次级粘弹爆炸命中后 slow 4 秒"
      enables:
        - "Hot Zone 草边 reveal"
        - "Brawl Ball / Gem Grab 入口 slow"
        - "反突进路线拖延"
      mitigates_failure_modes:
        - "assassin_enters_from_bush"
        - "delayed_damage_dodged"
      best_when: "地图有草口/区口必须被持续标记或 slow"
      poor_when: "队伍更需要 Windup 远程补刀，或敌方没有草/固定入口"
      bp_use: "hot_zone_or_bush_control_variant"

  map_feature_hooks:
    - id: "hot_zone_residue_choke_slow"
      map_feature_type: "zone_choke_reveal_and_slow"
      uses_feature_by: "Residue 或 Super Sticky 在区口形成揭草/slow 区，普攻延迟爆炸封站位"
      route_or_position: "Hot Zone 区口、草边、敌方回区路径"
      objective_conversion: "延迟进区、暴露草口、让队友集火被 slow 目标"
      active_when: "敌方必须从固定入口进区，Squeak 可安全预铺"
      fails_if: "敌方从区外长手/投掷清 Squeak，或机动直接越过爆炸时间"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.zone_choke_reveal_slow"
    - id: "bounty_knockout_windup_finish_lane"
      map_feature_type: "long_lane_delayed_finish"
      uses_feature_by: "Windup 超长射程和 Chain Reaction 让 Squeak 可从安全线补低血目标"
      route_or_position: "Bounty/Knockout 长线、回合末退线、墙边探头位"
      objective_conversion: "补 first pick、迫使低血目标离开掩体、保护星/回合优势"
      active_when: "目标血量低或必须留在固定位置，且没有立即突进压力"
      fails_if: "Windup 盲投落点不可见，目标有位移或 Squeak 被近身"
      example_maps:
        - "[[entities/maps/Shooting Star|Shooting Star]]"
        - "[[entities/maps/Hideout|Hideout]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "slot_task.long_range_finish_and_area_denial"
    - id: "gem_mine_blomb_and_carrier_denial"
      map_feature_type: "mine_and_carrier_route_denial"
      uses_feature_by: "Sticky Blomb 可贴宝石、墙或 carrier 退线，迫使敌人绕路"
      route_or_position: "宝石矿、carrier 倒计时退线、矿区侧墙"
      objective_conversion: "阻止收宝、保护 carrier、或让敌方进入队友火线"
      active_when: "矿区/退线可被延迟爆炸覆盖，队友能惩罚绕路"
      fails_if: "敌方短手直接贴 Squeak 或 long range 从爆炸外打他"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.mine_delayed_area_denial"
    - id: "heist_super_blob_safe_burst"
      map_feature_type: "fixed_target_multi_blob_burst"
      uses_feature_by: "Super 直接落在固定 safe 上可让多枚次级 blomb 附着/爆炸，形成集中伤害"
      route_or_position: "safe 正面、safe 旁墙、lane win 后 Super 投掷角"
      objective_conversion: "把 Super cycle 转成 safe 伤害，同时封防守者路线"
      active_when: "Squeak 能攒 Super 并安全投到 safe，敌方无法立即近身"
      fails_if: "Squeak 缺爆发被防守者贴脸，或 Super pattern 只打到少量 blob"
      example_maps:
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
      bp_use: "candidate_eval.heist_super_burst_variant"

  objective_contracts:
    - mode: "Hot Zone"
      can_fulfill:
        - "区口延迟爆炸封路"
        - "Residue 揭草/slow"
        - "Super Sticky 变体慢速入口"
      cannot_fulfill:
        - "单人站区 body"
        - "即时阻止近身 scorer"
      needs_teammate_support:
        - "站区前排、反突进、长线收割"
      false_positive: "Squeak 控区强，但没有即时击退/眩晕，不能独自防冲脸"
    - mode: "Bounty"
      can_fulfill:
        - "Windup 长线补刀"
        - "回合/星数优势时封退线"
      cannot_fulfill:
        - "开阔对狙稳定命中"
        - "被刺客压近后自救"
      needs_teammate_support:
        - "视野、反刺客、第一击杀输出"
      false_positive: "Windup 射程很远但落点不可见；不要把它当稳定 sniper"
    - mode: "Knockout"
      can_fulfill:
        - "末圈封路"
        - "墙边/草边延迟爆炸"
        - "Super 多点逼位"
      cannot_fulfill:
        - "即时守门/保命"
        - "单独清高速突进"
      needs_teammate_support:
        - "近身保护和击杀收尾"
      false_positive: "延迟伤害需要队友压住敌方走位才会转击杀"

  failure_modes:
    - id: "delayed_damage_no_immediate_stop"
      active_when: "敌方持球、刺客或坦克已经贴脸，需要立刻掉球/击退/眩晕"
      exposed_by: "[[sources/Fandom-Squeak|Fandom-Squeak]] 1.15 秒普攻延迟和 Brawl Ball tips"
      mitigation: "让队友承担即时 peel，Squeak 负责提前封路"
      bp_use: "anti_aggro_false_positive_filter"
    - id: "slow_reload_and_blomb_cap"
      active_when: "Squeak 连续乱铺导致 10 个 Sticky Blomb 上限覆盖旧 blomb，且 2.1 秒 reload 无法补"
      exposed_by: "Fandom Super limit of 10 Sticky Blombs and slow reload"
      mitigation: "按目标路线精确放置，保留一发给真实入口"
      bp_use: "resource_management_check"
    - id: "close_burst_punishes_delay"
      active_when: "Spike、Edgar、Buzz、El Primo、Shelly、Darryl、Bull 等从草或墙后贴脸"
      exposed_by: "Fandom notes high-burst Brawlers can eliminate Squeak due to delay"
      mitigation: "配反突进队友、Residue 揭草、保持开阔距离"
      bp_use: "draft_requires_peel"
    - id: "windup_snipe_overvalued"
      active_when: "BP 计划把 Windup 当作跨图稳定命中工具"
      exposed_by: "Fandom warns Windup range can make landing point unseen and should be used carefully"
      mitigation: "用于低血补刀、固定目标或开局区域压迫，不用于无信息盲狙"
      bp_use: "long_range_reliability_gate"

  conditional_matchups:
    - target: ["Gene", "Jae-Yong", "Berry", "Ruffs"]
      direction: "subject_favored"
      source: "[[sources/PLP-Squeak|PLP-Squeak]]"
      mechanism: "延迟区域和 Windup 可以逼低爆发支援离开治疗/拉人/增益站位"
      active_when: "目标需要站在固定支援线或 objective edge，Squeak 有安全距离"
      fails_when: "支援队伍有刺客贴 Squeak 或直接从开阔长线消耗他"
      bp_use: "area_control_into_support_shell"
    - target: ["Lola", "Mandy", "Maisie", "Meg"]
      direction: "subject_favored"
      source: "[[sources/PLP-Squeak|PLP-Squeak]]"
      mechanism: "粘弹可迫使长线或阵地输出换位，Chain Reaction 惩罚 grouped body"
      active_when: "地图有墙角/矿区/区口让目标必须停留或绕路"
      fails_when: "目标在完全开阔处 outrange，或 Meg 直接用 body 压 Squeak"
      bp_use: "delayed_area_response_to_static_damage"
    - target: ["Bolt", "Bibi", "Edgar", "Ollie"]
      direction: "target_favored"
      source: "[[sources/PLP-Squeak|PLP-Squeak]]"
      mechanism: "高速进场、坦克控制或近身爆发能在延迟爆炸前逼出击杀"
      active_when: "他们有草/墙/位移路线并能选择第一接触"
      fails_when: "Residue 先揭示路线，队友提供硬 peel，Squeak 已预铺终点"
      bp_use: "avoid_without_peel_or_route_lock"
    - target: ["Rosa", "Bull", "Trunk", "Willow"]
      direction: "target_favored"
      source: "[[sources/PLP-Squeak|PLP-Squeak]]"
      mechanism: "坦克身体、路线压迫、或 Willow 远程投掷/Hex 能绕开 Squeak 的延迟区"
      active_when: "目标有 sustain/控制或能从墙后压 Squeak"
      fails_when: "Squeak 与队友形成交叉火力并把他们赶进固定 choke"
      bp_use: "requires_frontline_and_control_answer"

  slot_notes:
    slot_1: "Hot Zone/Bounty/Knockout 有明确 choke 和反突进队友时可早手"
    slot_2_3: "作为控图层时要补即时 peel，不要让 Squeak 单独防 scorer/assassin"
    slot_4_5: "看到敌方低机动支援或固定站位输出时响应价值高"
    slot_6: "最后手可封死单一入口或长线低血目标，但不能补队伍缺即时控制"
```

## 关联页面

- [[sources/Fandom-Squeak|Fandom 来源摘要: Squeak]]
- [[sources/PLP-Squeak|PLP 来源摘要: Squeak]]
