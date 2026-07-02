# Lumi

## 基本信息

- 稀有度：Mythic
- 定位：Damage Dealer
- 类型：双锤召回 / 穿墙回收伤害 / root 控场

## 来源摘要

- Fandom：[[sources/Fandom-Lumi|Fandom 来源摘要: Lumi]]
- PLP：[[sources/PLP-Lumi|PLP 来源摘要: Lumi]]
- PLP 推荐模式：Gem Grab, Brawl Ball, Hot Zone, Heist

## 角色定位总结

Lumi 的 BP 价值来自两段式弹药循环：前两次攻击把 morning star 丢到场上，第三次“召回”让双锤从场地任意位置飞回本体，召回阶段能穿墙/穿地形、伤害更高，并在 `Half-Time` 下 slow 1 秒。Super `Blast Beat` 是三段瞬发圆形爆炸，第三段 root 敌人 1-1.7 秒，阻止正常移动但不阻止攻击。她不是传统装填英雄，输出稳定性取决于锤子落点、回收路径和敌方是否能趁回收前突脸。

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
    effective_range: "long_recall_geometry; 前掷 8 格，召回无长度上限且可穿墙"
    projectile_reliability: "medium; 前掷需预判，召回路径更可靠但依赖锤子落点和本体移动"
    burst: "high_if_throw_plus_recall_or_super_chain; 召回 900x2，Super 三段 1000/1200/1400"
    sustained_dps: "stateful; 不是普通 reload，必须管理 2 个锤子和召回节奏"
    objective_damage: "medium_high; Heist 可用双锤召回和 Super 打固定 safe"
    mobility: "low; 无位移，靠 slow/ice/root 自保"
    survivability: "low_to_medium; 3500 HP，靠控场防突进"
    engage: "medium; Super root 或 Grim and Frostbitten 限路后接回收"
    disengage: "medium_high_with_ice_or_root; 滑地、slow 和 root 能阻止短手追击"
    anti_aggro: "high_if_maces_held_close; 近墙短回收、冰面和 root 可反制跳脸"
    anti_tank: "medium; root/slow 能拖坦，但他们仍可攻击"
    wall_break: "none"
    throw_or_wall_bypass: "high_recall_and_super; 召回锤可穿墙，Super 爆炸可穿墙但不破墙"
    area_control: "high; Grim and Frostbitten 2.33 格冰面，Hit the Lights/42% Burnt 火区，Super 三段区域"
    scouting_or_vision: "medium; 火/冰区域限制草口和逃路"
    team_support: "medium; root/slow 为队友创造命中窗口"
    spawnable_or_pet: "mace_state; 锤子落点是后续区域/召回几何核心"
    crowd_control: "high; Half-Time slow，Grim and Frostbitten 滑地，Super 第三段 root"
    source_trace:
      - "[[sources/Fandom-Lumi|Fandom-Lumi]]"
      - "[[sources/PLP-Lumi|PLP-Lumi]]"

  build_switches:
    - build: "Grim and Frostbitten / Half-Time / Shield, Damage"
      source: "[[sources/PLP-Lumi|PLP-Lumi]]"
      changes_capabilities:
        - "Grim and Frostbitten 在锤子/本体位置生成 3.9 秒冰面，半径 2.33 格，用于卡区口和防跳脸"
        - "Half-Time 让召回锤命中 slow 30% 持续 1 秒，提高回收命中和队友跟伤"
        - "Shield/Damage 提高低血量远程的站线与爆发确认"
      enables:
        - "Gem/Ball/Zone 的路线 slow"
        - "Heist fixed target burst"
        - "反刺客短回收"
      mitigates_failure_modes:
        - "maces_far_away_vs_assassin"
        - "recall_path_not_converting"
      best_when: "地图有可让召回穿墙的角度，或目标任务迫使敌方经过锤子落点"
      poor_when: "敌方能从多角度突脸，或用长手/投掷在锤子回收前压低 Lumi"
      bp_use: "default_plp_recall_control_build"
    - build: "Hit the Lights / 42% Burnt variant"
      source: "[[sources/Fandom-Lumi|Fandom-Lumi]]"
      changes_capabilities:
        - "Hit the Lights 在锤子位置留 3.9 秒火区，限制逃路"
        - "42% Burnt 让 Super 爆炸后留 4 秒火区，强化 Hot Zone/Heist 区域伤害"
      enables:
        - "逃路封锁"
        - "固定目标/区口持续伤害"
      mitigates_failure_modes:
        - "rooted_target_still_attacks"
        - "enemy_walks_out_after_first_hit"
      best_when: "队伍更需要 area damage 而不是 ice slow"
      poor_when: "敌方突进太强，需要 Grim and Frostbitten 的防身冰面"
      bp_use: "area_damage_variant"

  map_feature_hooks:
    - id: "gem_recall_through_wall_carrier_pressure"
      map_feature_type: "gem_wall_recall_pressure"
      uses_feature_by: "前掷锤子控矿，移动到侧角后召回穿墙打 carrier/护送者并 slow"
      route_or_position: "宝石矿侧墙、carrier 退线、中心墙后低血藏点"
      objective_conversion: "逼 carrier 停步或掉宝，保护己方拾宝和撤退"
      active_when: "锤子落点和 Lumi 位置能夹住撤退路径"
      fails_if: "carrier 有近身保镖，或 Lumi 为了召回走进突脸范围"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
      bp_use: "map_bp_factors.recall_wall_pressure_on_carrier"
    - id: "hot_zone_grim_frostbitten_entry_slow"
      map_feature_type: "zone_ice_entry_control"
      uses_feature_by: "Grim and Frostbitten 在区口或锤子落点铺冰，Super 第三段 root 区内目标"
      route_or_position: "单区入口、区边墙、敌方回区必经线"
      objective_conversion: "延迟敌方进区并为队友击杀 root/slow 目标"
      active_when: "区口半径可被锤子冰面覆盖，己方能站区"
      fails_if: "敌方从冰面外远程清区，或 root 后仍用攻击反杀"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "map_bp_factors.zone_entry_slow_and_root"
    - id: "brawl_ball_root_and_recall_lane"
      map_feature_type: "ball_lane_root_and_pickup_denial"
      uses_feature_by: "Super 第三段 root 停住持球/守门移动，召回锤穿墙打门前或球落点"
      route_or_position: "中路球权、门前防守人、侧草推进线和 overtime 直线"
      objective_conversion: "阻止持球移动、压守门人或在球落点制造 slow/伤害"
      active_when: "敌方必须沿直线推进或守门，队友能接球/射门"
      fails_if: "敌方仍可攻击阻止射门，或 Lumi 没有锤子路径覆盖球路"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_movement_denial"
    - id: "heist_recall_and_blast_beat_safe_burst"
      map_feature_type: "safe_fixed_target_recall_burst"
      uses_feature_by: "fixed safe 易吃前掷/召回和 Super 三段，火区变体可附加区域 tick"
      route_or_position: "safe 正线、侧墙回收线、敌方基地入口"
      objective_conversion: "把一次锤子循环和 Super 转成 safe burst 或防守压退"
      active_when: "Lumi 能站到安全召回角且队友保护她不被突脸"
      fails_if: "敌方 race 更快，或刺客在锤子远离本体时接近"
      example_maps:
        - "[[entities/maps/Bridge Too Far|Bridge Too Far]]"
        - "[[entities/maps/Kaboom Canyon|Kaboom Canyon]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
      bp_use: "candidate_eval.heist_recall_burst_with_anti_dive_check"

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - "矿区穿墙召回压力"
        - "carrier 退线 slow/root"
      cannot_fulfill:
        - "主 carrier"
        - "无锤子路径时控矿"
      needs_teammate_support:
        - "carrier、视野、反突进"
      false_positive: "Lumi 的穿墙来自召回路径，不是前掷或本体能穿墙"
    - mode: "Brawl Ball/Hot Zone"
      can_fulfill:
        - "区口/球路 slow 与 root"
        - "反跳脸短回收"
      cannot_fulfill:
        - "主 scorer 或站区 body"
        - "root 后阻止敌方攻击"
      needs_teammate_support:
        - "前排、射门位、击杀跟进"
      false_positive: "root 阻止移动但不阻止攻击，不能当作 stun 使用"
    - mode: "Heist"
      can_fulfill:
        - "固定 safe 的前掷/召回/Super burst"
      cannot_fulfill:
        - "被突脸时稳定 race"
      needs_teammate_support:
        - "防突进、开线、另一路 race"
      false_positive: "锤子离本体越远，Lumi 越怕刺客趁回收前进场"

  failure_modes:
    - id: "mace_state_mismanaged"
      active_when: "两把锤都在远处，刺客跳脸或目标已经离开召回路径"
      exposed_by: "[[sources/Fandom-Lumi|Fandom-Lumi]] attack state and tips"
      mitigation: "面对刺客把锤子打近墙，保留短回收和冰面"
      bp_use: "resource_state_check"
    - id: "root_is_not_silence_or_stun"
      active_when: "队伍以为 Blast Beat 第三段会阻止敌方攻击"
      exposed_by: "Fandom root note says rooted enemies can still attack and use dashes/charges"
      mitigation: "把 root 用于阻止移动/拾球/撤退，击杀靠队友或 safe angle"
      bp_use: "cc_false_positive_filter"
    - id: "long_recall_travel_time"
      active_when: "锤子跨场召回，伤害到达太晚"
      exposed_by: "maces have no recall length limit but take more time"
      mitigation: "只在预判撤退线或固定目标时用远召回，近身对抗用短路径"
      bp_use: "timing_reliability_check"
    - id: "low_health_into_long_range_or_dot"
      active_when: "Lumi 被 Crow/Janet/Bea/Barley 等持续压线，无法站到召回角"
      exposed_by: "3500 HP and PLP target_favored signals"
      mitigation: "用墙角、Shield gear、队友 peel，不在开阔图无掩护早手"
      bp_use: "map_openness_filter"

  conditional_matchups:
    - target: ["Meg", "Mr. P", "Pam", "Gene"]
      direction: "subject_favored"
      source: "[[sources/PLP-Lumi|PLP-Lumi]]"
      mechanism: "召回穿墙和 Super root 能惩罚阵地/召唤/支援站位，绕过前排或宠物干扰"
      active_when: "他们必须围绕矿区、区口或 safe 站位，Lumi 有回收角"
      fails_when: "召唤物或前排直接压 Lumi 本体，或队伍无收割跟进"
      bp_use: "anti_anchor_recall_pressure"
    - target: ["Nani", "Glowy", "Sprout", "Piper"]
      direction: "subject_favored"
      source: "[[sources/PLP-Lumi|PLP-Lumi]]"
      mechanism: "长线前掷和穿墙召回能打到撤退/墙后长手，Half-Time slow 帮队友接伤害"
      active_when: "目标需要躲墙或沿固定射线撤退，Lumi 能夹住路径"
      fails_when: "目标保持最大射程并有突进队友逼 Lumi 放弃锤子角"
      bp_use: "long_lane_recall_answer"
    - target: ["Bolt", "Damian", "Barley", "Bo"]
      direction: "target_favored"
      source: "[[sources/PLP-Lumi|PLP-Lumi]]"
      mechanism: "高速接触、墙后控制、投掷或地雷会阻止 Lumi 安全布锤/召回"
      active_when: "地图有墙袋或突进路线，Lumi 低血量被迫移动"
      fails_when: "锤子短路径守入口，队友清 pocket 或探雷"
      bp_use: "must_answer_route_or_wall_pressure"
    - target: ["Bea", "Janet", "Crow", "Finx"]
      direction: "target_favored"
      source: "[[sources/PLP-Lumi|PLP-Lumi]]"
      mechanism: "长线 burst、空中/视野控制、毒伤或 projectile-field 对抗会压制 Lumi 的站位节奏"
      active_when: "他们能从召回路径外持续 chip 或改变投射物交易"
      fails_when: "Lumi 用墙角回收打固定目标，或队友先给视野/控制"
      bp_use: "avoid_open_lane_without_peel"

  slot_notes:
    slot_1: "不宜在多突进/开阔长线盲早手；锤子状态会被针对"
    slot_2_3: "可作为 Gem/Ball/Zone/Heist 的路径控制与固定目标伤害核心"
    slot_4_5: "看到敌方阵地/墙后站位多时可响应"
    slot_6: "最后手惩罚缺突进、缺持续 chip 的阵容最稳"
```

## 关联页面

- [[sources/Fandom-Lumi|Fandom 来源摘要: Lumi]]
- [[sources/PLP-Lumi|PLP 来源摘要: Lumi]]
