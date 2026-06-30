# Kenji

## 基本信息

- 稀有度：Legendary
- 定位：Assassin
- 类型：dash/slash 循环 / 生命偷取 / Super 免疫切入

## 来源摘要

- Fandom：[[sources/Fandom-Kenji|Fandom 来源摘要: Kenji]]
- PLP：[[sources/PLP-Kenji|PLP 来源摘要: Kenji]]
- PLP 推荐模式：Brawl Ball, Hot Zone

## 角色定位总结

Kenji 的核心是 dash 与 slash 交替：dash 用来接近、带球和穿过敌人，slash 用 135 度近身弧形打更高伤害并触发 35% 伤害吸血。Super `Slashimi` 越过障碍投鱼、让 Kenji 短时消失并清除负面效果，再在落点打十字双斩；它既是击杀工具，也是躲 Frank/Shelly/Buzz 等关键爆发和控制的资源。风险在于他需要近身和中心命中，Super 后回到原位会暴露，连续 chip 会阻止 `Nigiri Nemesis` 盾刷新，也会让 Hosomaki 的时机变难。

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
    effective_range: "short_with_long_super; dash 2.67 格，slash 3.67 格，Super 7.33 格并越障碍投放"
    projectile_reliability: "high_at_close_medium_on_super_center; dash/slash 稳定，Super 十字中心可被非对角移动规避"
    burst: "high_if_super_or_slash_chain_hits; 双斩每段 1300，slash 1000 并吸血"
    sustained_dps: "medium_high; 1 秒装填，非常快，但必须贴近"
    objective_damage: "low_to_medium; 主要服务 Ball/Zone/Gem pick，不是 Heist race"
    mobility: "very_high; Very Fast 基础移速，dash 攻击，Super 期间 8000 移速/消失"
    survivability: "high_when_dealing_damage; 35% 伤害吸血，Hosomaki 回近 3 秒内损失 50%，Nigiri 下一击 60% 减伤"
    engage: "high; dash、Super 越障碍落点和 Hyper pull 可强开"
    disengage: "medium; Super 免疫/清负面但回原位，dash 可后撤"
    anti_aggro: "medium_high; Super 可躲重击/控制，slash 吸血反打"
    anti_tank: "conditional; 能 kite/吸血，但重坦硬控和 shotgun 会惩罚近身"
    wall_break: "none"
    throw_or_wall_bypass: "high_super_only; Super 鱼可越障碍打墙后目标，本体 dash 不穿墙"
    area_control: "medium_with_hyper; Hyper 5 格 pull 到 Super 中心，常规只是 pick 区域"
    scouting_or_vision: "low"
    team_support: "low_to_medium; 主要通过击杀/牵制创造空间"
    spawnable_or_pet: "none"
    crowd_control: "medium_with_hyper; Hyper Super 拉人 1 秒，常规无硬控"
    source_trace:
      - "[[sources/Fandom-Kenji|Fandom-Kenji]]"
      - "[[sources/PLP-Kenji|PLP-Kenji]]"

  build_switches:
    - build: "Hosomaki Healing / Nigiri Nemesis / Shield, Damage"
      source: "[[sources/PLP-Kenji|PLP-Kenji]]"
      changes_capabilities:
        - "Hosomaki Healing 即刻回复最近 3 秒损失生命的 50%，支持吃爆发后继续贴身"
        - "Nigiri Nemesis 5 秒未受伤后下一次敌方攻击减伤 60%，对高伤长手开局换血尤其关键"
        - "Shield/Damage 提升进场第一轮容错和低血击杀确认"
      enables:
        - "Brawl Ball dash dribble"
        - "Hot Zone 近身清区"
        - "Super 躲关键控制后反打"
      mitigates_failure_modes:
        - "chip_breaks_approach"
        - "burst_after_super_return"
      best_when: "敌方需要站目标点或守球路，且没有连续 chip 让 Nigiri 永久离线"
      poor_when: "敌方有 Gale/Otis/Shelly/Surge 等低成本反突进链"
      bp_use: "default_plp_sustain_assassin_build"
    - build: "Dashi Dash / Studied the Blade variant"
      source: "[[sources/Fandom-Kenji|Fandom-Kenji]]"
      changes_capabilities:
        - "Dashi Dash 3 秒内所有攻击都变 dash，可快速到矿/区/球或追残血"
        - "Studied the Blade 让 Super 斩击长度 +30%，提高墙后/远点命中"
      enables:
        - "开局 tempo"
        - "追击低血长手"
        - "更远 Super pick"
      mitigates_failure_modes:
        - "cannot_reach_objective_first"
        - "super_slice_short_by_spacing"
      best_when: "需要开局抢点或地图有稳定 Super 十字角"
      poor_when: "敌方爆发很高且 Kenji 更需要 Hosomaki/Nigiri 生存"
      bp_use: "tempo_or_super_range_variant"

  map_feature_hooks:
    - id: "brawl_ball_dash_dribble_and_super_score"
      map_feature_type: "ball_dash_tempo_and_goal_pick"
      uses_feature_by: "dash 攻击可带球位移，Super 可免疫关键伤害并在门前打十字清守门人"
      route_or_position: "中路开球、侧草推进、球门前 defender 站位和 overtime 直线"
      objective_conversion: "抢第一球、清守门人、或用 Super timing 创造进球窗口"
      active_when: "球路有草墙或敌方守门人缺硬反突进"
      fails_if: "Gale/Otis/Shelly/Darryl 等守门控制未交，或 Super 后回原位被围杀"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      bp_use: "slot_task.ball_dash_scorer_or_disarm"
    - id: "hot_zone_slash_sustain_and_super_clear"
      map_feature_type: "zone_close_clear_with_invulnerability"
      uses_feature_by: "dash/slash 吸血进区，Super 消失躲爆发并打十字，Hyper 可把敌人拉向中心"
      route_or_position: "单区入口、区边墙、敌方站区 body 的脚下"
      objective_conversion: "把敌方站区者打出区或击杀，给己方 body 踩区"
      active_when: "敌方必须近距离站区，Kenji 有 Super/Hosomaki 或 Nigiri"
      fails_if: "敌方从区外 long range/thrower 清 Kenji，或控制链覆盖 Super 回点"
      example_maps:
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "candidate_eval.zone_clear_assassin_not_primary_body"
    - id: "gem_carrier_super_pick_or_escape"
      map_feature_type: "carrier_pick_or_dash_retreat"
      uses_feature_by: "Super 越障碍打 carrier，dash 可作为持宝撤退移动，Hosomaki 保命"
      route_or_position: "宝石矿侧墙、carrier 倒计时撤退线、己方半场回撤路线"
      objective_conversion: "击杀 carrier、逼掉宝，或自己持宝后用 dash/Super 拉开距离"
      active_when: "目标被墙/草压住，Kenji 可预判十字中心或 Hyper pull"
      fails_if: "carrier 有召唤物/控制保镖，或 Kenji 作为主 carrier 被持续 chip"
      example_maps:
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      bp_use: "map_bp_factors.carrier_assassination_or_escape"
    - id: "thrower_pocket_super_over_wall_pick"
      map_feature_type: "over_wall_assassin_super"
      uses_feature_by: "Slashimi 鱼可越障碍投到墙后，对 Grom/Sprout/Squeak 等口袋位造成双斩威胁"
      route_or_position: "Knockout/Bounty 墙袋、Layer Cake 分层墙、Gem Fort 中央墙后"
      objective_conversion: "逼投掷离开口袋，或在缩圈/星差时拿首杀"
      active_when: "Kenji 有 Super，目标缺近身 bodyguard，队友能压逃跑路线"
      fails_if: "目标非对角移动躲十字，或墙袋旁有 Shelly/Jacky/Gale 反开"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
        - "[[entities/maps/New Horizons|New Horizons]]"
      bp_use: "slot_task.wall_pocket_assassination"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "dash 带球和抢中路"
        - "Super 清守门人或躲关键控制"
        - "Hyper 拉人团灭窗口"
      cannot_fulfill:
        - "稳定破门"
        - "无 Super 正面进多控球门"
      needs_teammate_support:
        - "破墙/射门跟进、反控制、远程压低守门人"
      false_positive: "Kenji 能带球并不等于能穿过硬控守门线"
    - mode: "Hot Zone"
      can_fulfill:
        - "近身清区和吸血续战"
        - "Super 免疫关键爆发"
      cannot_fulfill:
        - "长期主站区 body"
        - "处理区外 thrower/long range"
      needs_teammate_support:
        - "站区前排、区外长手、探草/反投掷"
      false_positive: "Kenji 清区后仍需要队友实际踩区"
    - mode: "Gem Grab"
      can_fulfill:
        - "carrier assassination"
        - "dash 撤退/追击"
      cannot_fulfill:
        - "稳定主 carrier 与远程控矿"
      needs_teammate_support:
        - "主 carrier、视野、反召唤物"
      false_positive: "Super 过墙击杀依赖中心命中，不应无条件当作 carrier counter"

  failure_modes:
    - id: "super_center_can_be_dodged"
      active_when: "Kenji Super 预判明显，目标按非对角方向移动离开十字"
      exposed_by: "[[sources/Fandom-Kenji|Fandom-Kenji]] counterplay notes"
      mitigation: "用 Hyper pull、墙角、队友 slow/控制，或只打被目标任务固定的敌人"
      bp_use: "skillshot_finish_reliability"
    - id: "post_super_return_punish"
      active_when: "Kenji Super 后回到原位，原位被预瞄或控制覆盖"
      exposed_by: "Fandom Super returns Kenji to original position"
      mitigation: "Super 前保留下一个 dash、选择安全原位、或让队友压住回点"
      bp_use: "engage_exit_plan_gate"
    - id: "chip_breaks_nigiri_and_hosomaki_timing"
      active_when: "敌方持续小伤害阻止 Nigiri 刷新，且 Kenji 等太久才按 Hosomaki"
      exposed_by: "Fandom notes chip prevents shield and affects healing timing"
      mitigation: "用墙草重置 5 秒，及时按 Hosomaki，或不进持续 poison/area comp"
      bp_use: "sustain_resource_check"
    - id: "hard_anti_aggro_guard"
      active_when: "Gale/Otis/Shelly/Surge/Jacky 等守入口"
      exposed_by: "[[sources/PLP-Kenji|PLP-Kenji]] target_favored signal and Fandom anti-control tips"
      mitigation: "等控制交掉、绕另一侧、或选后排而非正面 body"
      bp_use: "avoid_without_control_bait"

  conditional_matchups:
    - target: ["Grom", "Brock", "Squeak", "Penny", "Gray"]
      direction: "subject_favored"
      source: "[[sources/PLP-Kenji|PLP-Kenji]]"
      mechanism: "dash 压缩距离、Super 越墙落点和吸血能惩罚低机动墙后/长线目标"
      active_when: "目标缺 bodyguard，Kenji 有 Super 或 dash 链，并能避开第一轮预瞄"
      fails_when: "目标口袋旁有硬控或召唤物挡中心命中"
      bp_use: "response_pick_into_wall_or_range_control"
    - target: ["Poco", "Sandy", "Mortis"]
      direction: "subject_favored"
      source: "[[sources/PLP-Kenji|PLP-Kenji]]"
      mechanism: "Kenji 的吸血、Hosomaki 和 Super 免疫能在近身资源战中 out-tempo 低 burst 支援或镜像刺客"
      active_when: "目标需要靠近目标点，且 Kenji 可先手叠伤害/吸血"
      fails_when: "Poco/Sandy 队友提供强反突进，或 Mortis 只打 Kenji 后排队友"
      bp_use: "tempo_duel_or_support_punish"
    - target: ["Gale", "Otis", "Surge", "Shelly"]
      direction: "target_favored"
      source: "[[sources/PLP-Kenji|PLP-Kenji]]"
      mechanism: "推离、沉默、阶段爆发和 shotgun 近身惩罚 Kenji 必须接触的输出模式"
      active_when: "他们守区口、球门或 Kenji Super 回点"
      fails_when: "关键控制已交，Kenji 用 Super 躲第一爆发并从另一角度切后排"
      bp_use: "avoid_primary_engage_into_hard_peel"
    - target: ["Moe", "Jacky", "Nita", "Darryl"]
      direction: "target_favored"
      source: "[[sources/PLP-Kenji|PLP-Kenji]]"
      mechanism: "钻地/近身范围伤害、召唤物 body 或滚入 burst 能在 Kenji 贴脸时反打"
      active_when: "目标任务迫使 Kenji 进入他们的短手范围或召唤物区"
      fails_when: "Kenji 只打后排、先清召唤物，或队友控制住 body"
      bp_use: "requires_body_clear_or_last_pick_caution"

  slot_notes:
    slot_1: "Brawl Ball/Hot Zone 强图可早手，但会暴露给硬反突进"
    slot_2_3: "适合作为速度/清区核心，后续补长手和反控制"
    slot_4_5: "看到敌方墙后/长手缺保镖时可响应"
    slot_6: "最后手惩罚无硬控阵容很强；多控多 shotgun 时不要硬锁"
```

## 关联页面

- [[sources/Fandom-Kenji|Fandom 来源摘要: Kenji]]
- [[sources/PLP-Kenji|PLP 来源摘要: Kenji]]
