# Amber

## 基本信息

- 稀有度：Legendary
- 定位：Controller
- 类型：持续火线、燃油控区、草丛清除

## 来源摘要

- Fandom：[[sources/Fandom-Amber|Fandom 来源摘要: Amber]]
- PLP：[[sources/PLP-Amber|PLP 来源摘要: Amber]]
- PLP 推荐模式：Gem Grab、Brawl Ball、Heist、Hot Zone

## 角色定位总结

Amber 是用持续喷火和燃油地形把路线变成高成本区域的 Controller。她的主攻击是一整条可持续 4 秒的火流，适合压住中近距离入口和逼迫敌人绕路；Super 会留下可长期存在的燃油，点燃后造成持续灼烧并烧毁草丛。PLP 默认 `Fire Starters / Wild Flames / Vision, Shield, Reload`，强调用速度和双燃油池循环抢区域视野。BP 中要把 Amber 当作“控路和草区处理器”，而不是即时爆发英雄：空弹、被长手 outrange、或被突脸贴身时，她的防守窗口会变脆。

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
    effective_range: "long_mid_stream; 主攻击 8.33 格，持续火流有轻微 spread 和 travel delay"
    projectile_reliability: "high_on_constrained_routes_medium_vs_dash; 连续喷射容错高，但要预判移动方向"
    burst: "medium_low_immediate; Dancing Flames 和点燃燃油可爆发，默认主攻击没有硬控瞬秒"
    sustained_dps: "high_if_ammo_managed; 40 flame ammo 长时间压线，空弹后恢复慢"
    objective_damage: "medium_high_with_fire_starters_or_dancing_flames; Heist 可用持续火线和固定目标 gadget"
    mobility: "medium_with_fire_starters; 默认 720 移速，gadget 3 秒 +100 speed 并铺燃油"
    survivability: "medium_low; 3400 HP，依靠距离、燃油墙和 Shield gear"
    engage: "medium; 通过燃油封路逼近，不是硬开团"
    disengage: "medium_with_fire_wall; 点燃燃油和 Fire Starters 可阻止追击路线"
    anti_aggro: "medium; 燃油墙/Dancing Flames 能惩罚刺客，但近身无 stun/knockback"
    anti_tank: "medium_high_if_distance_held; 连续火线和燃油穿越税能磨高血量"
    wall_break: "bush_destroy_only; 点燃燃油可烧草，不破墙"
    throw_or_wall_bypass: "super_lob; Super 可越墙投掷燃油，主攻击不能越墙"
    area_control: "very_high; 持久燃油、火墙、双 puddle 和草丛清除"
    scouting_or_vision: "high_with_vision_gear_and_bush_burn; Vision gear 配持续命中，燃油点火清草"
    team_support: "medium_high; 把敌人赶出 chokepoint 和队友射线"
    spawnable_or_pet: "none"
    crowd_control: "soft_area_denial; 没有 slow/stun，靠灼烧路径成本"
    source_trace:
      - "[[sources/Fandom-Amber|Fandom-Amber]]"
      - "[[sources/PLP-Amber|PLP-Amber]]"

  build_switches:
    - build: "Fire Starters / Wild Flames / Vision, Shield, Reload"
      source: "[[sources/PLP-Amber|PLP-Amber]]"
      changes_capabilities:
        - "Fire Starters 提供 3 秒移速和沿途燃油，帮助抢线和铺设回撤火墙"
        - "Wild Flames 允许两个 Super 燃油池，并在燃油附近每秒充能 Super"
        - "Vision gear 让持续火线命中后服务草区侦测，Reload gear 缓解空弹风险"
      enables:
        - "Gem Grab 矿区燃油控制"
        - "Brawl Ball 侧路火墙和草区清理"
        - "Heist safe race/防守燃油区"
        - "Hot Zone 入口持续税"
      mitigates_failure_modes:
        - "ammo_empty_after_overcommit"
        - "bush_route_unchecked"
        - "single_oil_pool_cycle_too_slow"
      best_when: "地图有固定入口、草边或 objective 区域可被燃油长期占住"
      poor_when: "敌方全长手从燃油外输出，或刺客能越过燃油直接贴身"
      bp_use: "default_plp_area_control_build"
    - build: "Dancing Flames / Scorchin' Siphon variant"
      source: "[[sources/Fandom-Amber|Fandom-Amber]]"
      changes_capabilities:
        - "Dancing Flames 在身边生成 3 个火球，适合防突脸或 Heist 固定目标贴身输出"
        - "Scorchin' Siphon 在燃油附近提高 reload，适合围绕已铺 Super 控线"
      enables:
        - "刺客近身惩罚"
        - "固定目标额外伤害"
        - "站在燃油边缘持续压线"
      mitigates_failure_modes:
        - "close_range_no_instant_stop"
        - "ammo_management_failure"
      best_when: "敌方会主动贴 Amber，或模式需要固定目标伤害"
      poor_when: "队伍更需要 Fire Starters 的开局抢线和大范围铺油"
      bp_use: "anti_aggro_or_heist_variant"

  map_feature_hooks:
    - id: "gem_mine_fluid_burn_and_vision"
      map_feature_type: "mine_area_oil_control_and_bush_reveal"
      uses_feature_by: "Super 燃油长期覆盖矿区/退线，点燃时烧草并用 Vision gear 追踪目标"
      route_or_position: "宝石矿、矿区侧草、carrier 倒计时退线"
      objective_conversion: "阻止敌方收宝或回矿，逼 carrier 绕进队友射线"
      active_when: "敌方需要穿过矿区或草边拿宝，Amber 可避免提前误点燃燃油"
      fails_if: "敌方长手在燃油外控矿，或 Gray/Edgar 等直接绕开火线贴身"
      example_maps:
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.mine_oil_control_and_vision"
    - id: "hot_zone_oil_wall_entry_tax"
      map_feature_type: "zone_entry_persistent_firewall"
      uses_feature_by: "双燃油池和点火威胁把区口变成穿越税，持续火线补压进入者"
      route_or_position: "Hot Zone 区口、侧草入口、敌方回区路径"
      objective_conversion: "延迟回区、分割前后排、让己方站区者少吃正面压力"
      active_when: "区口固定且燃油可安全铺下，Amber 有队友保护避免被 dive"
      fails_if: "敌方 thrower/long range 从区外打 Amber，或刺客越过燃油直接开她"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Open Business|Open Business]]"
        - "[[entities/maps/Parallel Plays|Parallel Plays]]"
      bp_use: "map_bp_factors.zone_entry_firewall"
    - id: "brawl_ball_firewall_lane_and_bush_burn"
      map_feature_type: "ball_lane_firewall_and_grass_clear"
      uses_feature_by: "燃油/主火线清理门前草和侧路，Fire Starters 可快速铺出回防火墙"
      route_or_position: "中场侧路、门前草、持球推进路径"
      objective_conversion: "迫使 defender 离开草位，保护己方持球推进或切断敌方反推"
      active_when: "球路经过草口/窄口，Amber 有时间先铺油再点燃"
      fails_if: "敌方破墙后从开阔长线消耗，或近身 scorer 在 Amber 空弹时冲门"
      example_maps:
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
        - "[[entities/maps/Pinball Dreams|Pinball Dreams]]"
      bp_use: "slot_task.ball_lane_control_and_bush_burn"
    - id: "heist_fire_starters_safe_race_or_defense"
      map_feature_type: "fixed_target_fire_stream_and_oil_path"
      uses_feature_by: "Fire Starters 路线和持续火线可转化为 safe 压力，也能在防守端烧掉进 safe 路线"
      route_or_position: "safe 入口、safe 侧草、lane win 后进 safe 角度"
      objective_conversion: "形成一段 burst/race 窗口，或把敌方近战 safe hitter 逼出输出位"
      active_when: "Amber 能保留足够 ammo 靠近 safe，且敌方无法立即 outrange 或贴脸打断"
      fails_if: "空弹后被反打，或敌方远程 race 在 Amber 接近前已经启动"
      example_maps:
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
      bp_use: "candidate_eval.heist_fire_stream_variant"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "矿区燃油控路"
        - "草丛清理和 Vision reveal"
        - "中距持续压血"
      cannot_fulfill:
        - "安全主 carrier"
        - "开阔长线对狙"
      needs_teammate_support:
        - "carrier、长手反压、近身保护"
      false_positive: "燃油控矿需要预铺和点火节奏；被迫贴脸或空弹时会掉节奏"
    - mode: "Brawl Ball"
      can_fulfill:
        - "火墙切断回防"
        - "清门前草"
        - "持续压守门位"
      cannot_fulfill:
        - "主 scorer"
        - "硬控掉球"
      needs_teammate_support:
        - "持球者、破门、即时 CC"
      false_positive: "Amber 可以让路线昂贵，但没有 knockback/stun 直接阻止持球冲门"
    - mode: "Heist"
      can_fulfill:
        - "持续火线打 safe"
        - "Dancing Flames/Fire Starters 固定目标窗口"
        - "防守近战 safe hitter"
      cannot_fulfill:
        - "远程无风险 race"
        - "单独处理所有 dive"
      needs_teammate_support:
        - "赢线和保护进 safe 路线"
      false_positive: "Heist 价值取决于她能否进入射程并管理 ammo，不是默认高安全 DPS"
    - mode: "Hot Zone"
      can_fulfill:
        - "区口燃油封锁"
        - "草边 reveal/清草"
        - "持续火线逼离站区"
      cannot_fulfill:
        - "单人吃全部长线火力站区"
        - "被刺客贴脸后自救"
      needs_teammate_support:
        - "站区 body、anti-dive、远程补伤"
      false_positive: "燃油是区域威胁，不是硬控；高机动英雄可能直接越过"

  failure_modes:
    - id: "ammo_empty_after_overcommit"
      active_when: "Amber 长按主攻击清空 40 flame ammo 后仍在敌方射线内"
      exposed_by: "[[sources/Fandom-Amber|Fandom-Amber]] full ammo stream and slow full reload"
      mitigation: "分段喷射，保留回防弹药，Reload gear 或 Scorchin' Siphon 只在燃油计划成立时选"
      bp_use: "resource_management_gate"
    - id: "close_range_no_hard_stop"
      active_when: "Edgar、Gray、Melodie 等越过燃油直接贴 Amber"
      exposed_by: "Fandom notes she has no immediate damage/stun/slow/knockback at close range"
      mitigation: "配 peel，或在预期被贴时切 Dancing Flames/站燃油边"
      bp_use: "anti_aggro_false_positive_filter"
    - id: "long_range_outpoke"
      active_when: "Brock、Bea、Byron、Piper、Crow 等在 Amber 射程外或燃油外持续消耗"
      exposed_by: "[[sources/PLP-Amber|PLP-Amber]] target_favored signals"
      mitigation: "用墙/草/燃油逼走位，或避免在纯开阔长线早选"
      bp_use: "range_gate_for_early_pick"
    - id: "oil_timing_and_water_interrupt"
      active_when: "燃油被过早点燃、落点被水体切断，或没有队友把敌人逼进火线"
      exposed_by: "Super fluid persists until ignited and is interrupted by lakes"
      mitigation: "把燃油放在敌方必经路径旁而非自己攻击线正前，水图检查可连接区域"
      bp_use: "map_feature_execution_check"

  conditional_matchups:
    - target: ["Charlie", "Shelly", "Emz", "Tara"]
      direction: "subject_favored"
      source: "[[sources/PLP-Amber|PLP-Amber]]"
      mechanism: "持续火线和燃油区可迫使中近距控制位离开草口/目标边缘，减少她们开团角度"
      active_when: "Amber 保持 6-8 格距离，目标必须穿过 chokepoint 或草边"
      fails_when: "目标从墙后/草里先手贴身，或 Amber 弹药已空"
      bp_use: "midrange_area_control_response"
    - target: ["Max", "Nita", "Surge", "Melodie"]
      direction: "subject_favored"
      source: "[[sources/PLP-Amber|PLP-Amber]]"
      mechanism: "燃油墙增加高速推进和召唤/形态压线的穿越成本，连续火线可跟踪跑位"
      active_when: "地图路线被油区收窄，Amber 有队友处理第一波突进"
      fails_when: "Max/Melodie 直接越过燃油贴后排，或 Nita Bear 吸收火线导致 Amber 空弹"
      bp_use: "route_tax_into_speed_or_pet_pressure"
    - target: ["Lou", "Brock", "Bea", "Byron", "Piper", "Crow"]
      direction: "target_favored"
      source: "[[sources/PLP-Amber|PLP-Amber]]"
      mechanism: "长手 poke、slow 或持续 debuff 可在 Amber 铺油/点火前消耗她，并限制她进入 8.33 格"
      active_when: "地图开阔，Amber 缺墙体和草路接近"
      fails_when: "Amber 能用燃油封住目标撤退线并得到队友长线压制"
      bp_use: "avoid_open_long_lane_without_support"
    - target: ["Gray", "Edgar"]
      direction: "target_favored"
      source: "[[sources/PLP-Amber|PLP-Amber]]"
      mechanism: "传送或跳脸可以绕过燃油穿越税，直接攻击 Amber 低血和无硬控短板"
      active_when: "他们有 Super/墙角/草位进入，且 Amber 没有 Dancing Flames 或队友 peel"
      fails_when: "Amber 预铺火墙并由队友控制落点"
      bp_use: "draft_requires_peel_or_gadget_answer"

  slot_notes:
    slot_1: "有固定 chokepoint、草区和可保护 Amber 的队友计划时可早手"
    slot_2_3: "作为控区层选出后，需要补长手或 anti-dive，不要让她单吃开阔长线"
    slot_4_5: "看到敌方中近距阵地或草口依赖时响应价值高"
    slot_6: "最后手可针对缺长手/缺突进的路线阵容，或补 Heist/Hot Zone 区域税"
```

## 关联页面

- [[sources/Fandom-Amber|Fandom 来源摘要: Amber]]
- [[sources/PLP-Amber|PLP 来源摘要: Amber]]
