# Nori

## 基本信息

- 稀有度：Legendary
- 定位：Assassin
- 类型：双形态近远切换 / 鱼资源成长 Super / hook 跳墙机动 / root CC

## 来源摘要

- Fandom：[[sources/Fandom-Nori|Fandom 来源摘要: Nori]]
- PLP：[[sources/PLP-Nori|PLP 来源摘要: Nori]]
- PLP 推荐模式：Hot Zone, Heist, Bounty
- 8/4 补丁 fix：[[sources/Supercell-Maintenance-August-4-2026|Maintenance - August 4, 2026]]

## 角色定位总结

Nori 的核心是 tap/hold 双形态切换：tap 打近身弧形 AOE（1100，可一次收多条鱼），hold 充能钩子突进（720，钩墙位移、满充跳墙、钩敌低伤）。鱼资源（上限 10 条）驱动 Super `Catch of the Day` 的成长——消耗全部鱼，每条 +5% 坑半径 / +4% 巨鱼伤害，即使空命中也消耗。Gadget `Gonna Need a Bigger Net` 提供 1.25 秒 root，是反刺客开团的硬 CC；`Sushi Snack` 用鱼换即时治疗。风险在于充能期不能回血、被 stun 取消，Super 空放会浪费鱼资源，且缺 strength profile 档位导致 runtime tier 未知。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-07-11"
    plp: "direct_raw_capture_2026-08-11"
    patch_fix: "supercell_maintenance_2026-08-04"
    user_notes: "none"
    reviewed_against:
      - "[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]"
      - "[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]"
      - "[[syntheses/条件化对位模型|条件化对位模型]]"
    gap_note: "strength profile 无 Nori 档位（iKaoss11 July 输入早于 Nori 发布）；runtime compile 时 tier=unknown，需玩家补强度输入后才能进 runtime 池排序"

  capability_vector:
    effective_range: "dual_form; tap melee 8.33 格弧形 AOE，hold hook 13.33-16.67 格充能突进，满充可跳墙"
    projectile_reliability: "medium; tap 弧形稳定多目标，hook 需充能预判且可被墙/miss 取消"
    burst: "high_with_fish_super; tap 1100 AOE 多目标，满鱼 Super 巨鱼 1750+ 成长，hook+tap 链可秒脆皮"
    sustained_dps: "medium; 装填 0.1s（ammo-bar 充能型，满充 2s），tap 可连续挥杆但 hold 充能期不能回血"
    objective_damage: "medium_high; PLP 推荐 Heist，Super 成长巨鱼可打库，hook 可改路线接近金库"
    mobility: "very_high; Very Fast 820 基础，hook 拉墙位移，满充跳墙，His Mother's Son 命中后 984"
    survivability: "medium_high; 3800 血，Sushi Snack 鱼换治疗，Super 落地后消失躲爆发，root 可断开团"
    engage: "high; hook 突进 + root + Super 水坑区域接管"
    disengage: "medium; hook 拉墙后撤，Super 消失躲关键技能，但回点在坑中心"
    anti_aggro: "high; root 1.25s 断刺客/突进，Super 水坑封路线，tap AOE 清近身"
    anti_tank: "conditional; tap AOE 和 Super 成长可压中血，但纯坦硬控会惩罚充能期"
    wall_break: "none"
    throw_or_wall_bypass: "high; 满充 hook 跳墙，Super 跳向目标点落地，可越障碍投放"
    area_control: "high; Super 水坑 360° 范围 + 成长半径，封区/封路/封球门"
    scouting_or_vision: "low"
    team_support: "medium; root 可保 carrier，Super 水坑可掩护队友进区"
    spawnable_or_pet: "none"
    crowd_control: "high; Gonna Need a Bigger Net root 1.25s 是核心 CC"
    terrain_creation: "medium; Super 水坑是临时区域，不造墙但改变路线"
    terrain_destruction: "none"
    source_trace:
      - "[[sources/Fandom-Nori|Fandom-Nori]]"
      - "[[sources/PLP-Nori|PLP-Nori]]"

  build_switches:
    - build: "Sushi Snack / Big Haul / Health, Shield"
      source: "[[sources/PLP-Nori|PLP-Nori]]"
      changes_capabilities:
        - "Sushi Snack 吃最多 3 条鱼每条治疗 1000（PLP）/ 700（Fandom Infobox），提供进场后续战"
        - "Big Haul Super 命中每敌收 3 鱼，加速 Super 成长循环，PLP 标注为推荐优于 His Mother's Son"
        - "Health+Shield 提升进场第一轮容错和低血确认"
      enables:
        - "Hot Zone 水坑清区 + 续航"
        - "Heist Super 成长打库循环"
        - "Bounty root 确认击杀"
      mitigates_failure_modes:
        - "charge_cannot_regen"
        - "super_whiff_consumes_fish"
      best_when: "敌方需要站目标点，Nori 可叠鱼后用成长 Super 接管区域"
      poor_when: "敌方有连续 stun/knock 打断充能，或长手在 Nori 充能期压血"
      bp_use: "default_plp_sustain_and_super_growth_build"
    - build: "Gonna Need a Bigger Net / His Mother's Son variant"
      source: "[[sources/Fandom-Nori|Fandom-Nori]]"
      changes_capabilities:
        - "Bigger Net 800 伤 + 1.25s root（PLP）/ 480（Fandom Infobox），反刺客开团"
        - "His Mother's Son 命中 +20% 移速 1s（820→984），增强 hook 追击和撤退"
      enables:
        - "反刺客断开团"
        - "高机动追击/脱战"
      mitigates_failure_modes:
        - "hard_dive_before_charge"
      best_when: "敌方有 Stu/Surge/Damian 等突进核心需要 root 断"
      poor_when: "更需要 Super 成长循环而非单次 root"
      bp_use: "anti_dive_or_mobility_variant"

  map_feature_hooks:
    - id: "hot_zone_fish_super_zone_takeover"
      map_feature_type: "zone_clear_with_growing_aoe"
      uses_feature_by: "叠鱼后 Super 水坑 360° 成长范围清区，root 封进场，tap AOE 清残血"
      route_or_position: "单区入口、区边墙、敌方站区 body 脚下"
      objective_conversion: "把敌方站区者打出区或击杀，给己方 body 踩区"
      active_when: "Nori 有鱼资源，敌方必须近距离站区"
      fails_if: "敌方从区外 long range/thrower 清 Nori，或控制链覆盖 Super 落点"
      example_maps:
        - "[[entities/maps/Ring of Fire|Ring of Fire]]"
        - "[[entities/maps/Dueling Beetles|Dueling Beetles]]"
        - "[[entities/maps/Open Business|Open Business]]"
      bp_use: "candidate_eval.zone_clear_assassin_with_growing_aoe"
    - id: "heist_super_growth_safe_damage"
      map_feature_type: "objective_damage_with_fish_investment"
      uses_feature_by: "叠满鱼后 Super 巨鱼成长伤害打库，hook 改路线接近金库，tap AOE 清守库"
      route_or_position: "金库侧墙、中路 hook 角度、Super 落点覆盖金库"
      objective_conversion: "成长 Super 巨鱼高伤 + 多次循环打库"
      active_when: "Nori 可安全叠鱼，敌方守库缺近身反制"
      fails_if: "守库有硬控/shotgun 惩罚 Super 落点，或 Nori 无法在打库前叠鱼"
      example_maps:
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Pit Stop|Pit Stop]]"
      bp_use: "slot_task.heist_growth_super_cycle"
    - id: "wall_hook_assassination_and_escape"
      map_feature_type: "hook_mobility_over_walls"
      uses_feature_by: "满充 hook 跳墙接近墙后目标或撤退，root 确认击杀，Super 越障碍投放"
      route_or_position: "墙后草丛、Knockout 墙袋、carrier 撤退线的侧墙"
      objective_conversion: "越过障碍击杀墙后目标，或 hook 拉墙脱战"
      active_when: "地图有可跳的墙，目标在墙后缺 bodyguard"
      fails_if: "墙旁有硬控/shotgun 反开，或 hook 充能期被打断"
      example_maps:
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
        - "[[entities/maps/Layer Cake|Layer Cake]]"
        - "[[entities/maps/Hideout|Hideout]]"
      bp_use: "slot_task.wall_pocket_hook_assassination"

  objective_contracts:
    - mode: "Hot Zone"
      can_fulfill:
        - "成长 Super 水坑清区"
        - "root 封进场"
        - "tap AOE 清近身站区者"
      cannot_fulfill:
        - "长期主站区 body（3800 血不够扛持续 chip）"
        - "处理区外 thrower/long range"
      needs_teammate_support:
        - "站区前排、区外长手、探草/反投掷"
      false_positive: "Nori 清区后仍需要队友实际踩区，Super 空放会浪费鱼"
    - mode: "Heist"
      can_fulfill:
        - "成长 Super 巨鱼打库"
        - "hook 改路线接近金库"
        - "tap AOE 清守库"
      cannot_fulfill:
        - "无鱼时 Super 伤害低（1250 基础）"
        - "扛硬控守库"
      needs_teammate_support:
        - "反控制、吸引守库火力、打库跟进"
      false_positive: "PLP 推荐 Heist 但 Nori 需要先叠鱼才有打库价值，不能当无脑首抢"
    - mode: "Bounty"
      can_fulfill:
        - "root 确认击杀"
        - "hook 追击残血"
        - "Super 水坑封路线拿星"
      cannot_fulfill:
        - "长线对枪"
        - "无 Super 时正面换血"
      needs_teammate_support:
        - "长手压血、视野、反狙击"
      false_positive: "Bounty 的 Nori 依赖 root+hook 链，不是长线输出"
    - mode: "Brawl Ball"
      can_fulfill:
        - "root 断带球"
        - "hook 突进攻门"
        - "Super 水坑封球门"
      cannot_fulfill:
        - "稳定持球推进（充能期不能回血）"
        - "扛守门爆发"
      needs_teammate_support:
        - "主 carrier、反控制、射门跟进"
      false_positive: "Nori 在球模式更适合断球和清守门人，不是主持球手"

  failure_modes:
    - id: "charge_cannot_regen"
      active_when: "Nori hold 充能期间无法自然回血，被持续 chip 压血"
      exposed_by: "[[sources/Fandom-Nori|Fandom-Nori]] Hold Attack notes: cannot heal from auto-regeneration while charging"
      mitigation: "用 Sushi Snack 补血、草丛重置、或避免在敌方视野内长充能"
      bp_use: "sustain_resource_check"
    - id: "charge_cancelled_by_cc"
      active_when: "Nori 充能期被 stun/push/knock 打断，hook 资源浪费"
      exposed_by: "[[sources/Fandom-Nori|Fandom-Nori]] Hold Attack notes: stunned/pushed/knocked back cancels attack"
      mitigation: "等敌方关键控制交掉再充能，或用 tap 形态规避充能期"
      bp_use: "must_avoid_charging_into_cc_chain"
    - id: "super_whiff_consumes_fish"
      active_when: "Nori Super 落点预判错误或目标撤离，巨鱼空命中但仍消耗全部鱼"
      exposed_by: "[[sources/Fandom-Nori|Fandom-Nori]] Super notes: consumes all fish even if attack hits no enemies"
      mitigation: "用 root/tap 先固定目标再投 Super，或保留鱼等确认落点"
      bp_use: "super_investment_gate"
    - id: "hard_dive_before_charge"
      active_when: "Stu/Surge/Damian 等突进在 Nori 充能前强开"
      exposed_by: "[[sources/PLP-Nori|PLP-Nori]] countered_by includes Damian, Surge"
      mitigation: "保留 Bigger Net root 断开团，或选后排让队友先吃第一轮"
      bp_use: "anti_dive_root_reserve"

  conditional_matchups:
    - target: ["Stu", "Gus", "8-Bit", "Pierce", "Bo", "Finx", "Lumi", "Sirius"]
      direction: "subject_favored"
      source: "[[sources/PLP-Nori|PLP-Nori]]"
      mechanism: "Nori 的 hook 突进 + root + 成长 Super 能惩罚中低速长手/控场/召唤物；8-Bit/Lumi/Sirius 缺机动难以躲水坑，Stu/Gus/Bo/Finx/Pierce 的技能可被 root 断"
      active_when: "目标缺 bodyguard，Nori 有 hook/root 资源，并能避开第一轮预瞄"
      fails_when: "目标有硬控保镖挡 hook，或 Nori 充能期被打断"
      bp_use: "response_pick_into_mid_speed_control_or_summons"
    - target: ["Bolt", "Starr Nova", "Pam", "Otis", "Chester", "Angelo", "Surge", "Damian"]
      direction: "target_favored"
      source: "[[sources/PLP-Nori|PLP-Nori]]"
      mechanism: "Bolt/Starr Nova 长线爆发惩罚 Nori 充能期；Pam 续航 out-sustain；Otis 沉默断充能；Chester 随机 Super 不可预判；Angelo 长线 poke；Surge 阶段成长反打；Damian 突进 burst"
      active_when: "他们守区口、长线或预瞄 Nori 充能窗口"
      fails_when: "关键爆发/控制已交，Nori 用 root 断或 Super 躲第一轮后从另一角度切"
      bp_use: "avoid_into_long_burst_or_silence_chain"

  slot_notes:
    slot_1: "Hot Zone/Heist 强图可早手，但会暴露给 Bolt/Starr Nova 长线；缺 strength 档位时谨慎首抢"
    slot_2_3: "适合作为 hook/root 核心或成长 Super 打库/清区手，后续补长手和反控制"
    slot_4_5: "看到敌方中速长手/控场缺保镖时可响应；Damian/Surge/Otis 已暴露时避免"
    slot_6: "最后手惩罚无长线爆发的阵容很强；Bolt/Starr Nova/Pam 在场时不要硬锁"
```

## 关联页面

- [[sources/Fandom-Nori|Fandom 来源摘要: Nori]]
- [[sources/PLP-Nori|PLP 来源摘要: Nori]]
- [[sources/Supercell-Maintenance-August-4-2026|Maintenance - August 4, 2026]]
