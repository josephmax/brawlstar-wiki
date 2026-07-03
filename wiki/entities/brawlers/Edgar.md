# Edgar

## 基本信息

- 稀有度：Epic
- 定位：Assassin
- 类型：跳跃进场 / 贴身爆发 / 自回复刺客

## 来源摘要

- Fandom：[[sources/Fandom-Edgar|Fandom 来源摘要: Edgar]]
- PLP：[[sources/PLP-Edgar|PLP 来源摘要: Edgar]]
- PLP 推荐模式候选：Gem Grab, Brawl Ball, Heist, Hot Zone, Knockout

## 角色定位总结

Edgar 的核心不是“刺客克制后排”，而是用自动充能 Super 和 `Let's Fly` 找到一次可确认的贴脸窗口。只要路线明确、敌方控制完整、或目标身边有击退/沉默/反突进，他就会从高上限切入手变成送资源的假阳性。BP 中应把 Edgar 当作后手惩罚工具、足球得分窗口工具和短时间 safe / gem / zone 压力工具，而不是稳定先手。

## BP 建模

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "[[sources/Fandom-Edgar|Fandom-Edgar]] direct_raw_capture_2026-06-30"
    plp: "[[sources/PLP-Edgar|PLP-Edgar]] direct_raw_capture_2026-06-30"
    user_notes: "本地 BP 规则要求按高水平对局处理短手路线和控制反制"

  capability_vector:
    effective_range: "short; 普攻 2 格，必须贴脸才能完成主要伤害"
    projectile_reliability: "贴脸快速双拳，接近后可靠；接近前几乎没有远程消耗"
    burst: "高；极快装填和 unload，Hard Landing 可补落地范围伤害"
    sustained_dps: "高但只在贴脸持续接触时成立；safe 或坦克目标可被快速打穿"
    objective_damage: "条件性高；Heist 只有在能接触金库并存活数秒时成立"
    mobility: "Super 可跳过障碍并短暂免伤，落地后加速；Let's Fly 可抓人或墙体形成第二段位移"
    survivability: "低基础血量加普攻回血；Hardcore/Shield gear 可提高第一次承伤，但不能解决控制链"
    engage: "强制跳入单点目标，适合惩罚无 peel 后排、投掷、低弹药高伤目标"
    disengage: "有限；进场 Super 用掉后主要靠击杀、回血、速度和 Let's Fly 第二段撤出"
    anti_aggro: "不是常规 anti-aggro；可在敌方弹药不足时反杀慢 unload 近战"
    anti_tank: "条件性；能用回血和高 unload 打慢出手坦克，但怕爆发、击退、控制和满弹药近战"
    wall_break: "无"
    throw_or_wall_bypass: "Super/Let's Fly 可越过障碍接近墙后目标"
    area_control: "低；Hard Landing 只提供落地点短暂威胁"
    scouting_or_vision: "无稳定探草，只能以身位试探"
    team_support: "无直接团队增益"
    spawnable_or_pet: "无"
    crowd_control: "无硬控；威慑来自贴脸秒杀"
    terrain_creation: "无"
    terrain_destruction: "无"

  build_switches:
    - build: "Let's Fly / Hard Landing / Shield + Damage"
      source: "[[sources/PLP-Edgar|PLP-Edgar]] + [[sources/Fandom-Edgar|Fandom-Edgar]]"
      changes_capabilities:
        - "Let's Fly 把 Edgar 从等待自动 Super 的单进场点变成双跳进出或更远距离追击"
        - "Hard Landing 增加落地斩杀线，适合打投掷、远程和低血量目标"
        - "Shield/Damage 提升第一次贴脸承伤和残局爆发"
      enables:
        - "Brawl Ball 自传球/跳球制造得分窗口"
        - "Gem Grab 跳矿或追 gem carrier 后快速撤出"
        - "Heist 接触金库后的短时间爆发"
      mitigates_failure_modes:
        - "partially_mitigates_entry_distance"
        - "partially_mitigates_first_contact_burst"
      best_when: "敌方缺击退、沉默、硬控或反突进，且地图有墙/草/球权/目标让 Edgar 的进场能转成得分、击杀或目标伤害"
      poor_when: "敌方仍有 Shelly/Gale/Otis/Surge/Maisie/R-T 这类低成本反进场，或地图是 Dry Season / Bridge Too Far 这类长线明确路线"
      bp_use: "后手惩罚、slot_6 高上限、Brawl Ball scorer pressure、anti-thrower route pick"

  map_feature_hooks:
    - id: "brawl_ball_jump_score_window"
      map_feature_type: "score_window"
      example_maps:
        - "[[entities/maps/Center Stage|Center Stage]]"
        - "[[entities/maps/Sneaky Fields|Sneaky Fields]]"
        - "[[entities/maps/Triple Dribble|Triple Dribble]]"
      route_or_position: "中路抢球后自传球接 Super，或从侧草/墙边跳到球门前"
      objective_conversion: "把一次赢线或敌方控制真空转成直接射门窗口"
      active_when: "敌方缺连续击退/控制，球门屏障可被绕过或队友已制造破门/控人窗口"
      fails_if: "敌方保留 knockback、stun、silence、slow 或多目标爆发；我方没有球权跟进"
      bp_use: "Brawl Ball 后手补 scorer；也用于惩罚敌方无 anti-aggro 草侧路阵容"
    - id: "grass_or_wall_route_assassin"
      map_feature_type: "route_based_assassin"
      example_maps:
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Belle's Rock|Belle's Rock]]"
      route_or_position: "侧草、墙后短路或投掷口袋边缘，等待 Super / Let's Fly 接近后排"
      objective_conversion: "Gem Grab 逼退 gem carrier；Knockout/Bounty 把墙后投掷或孤立远程变成击杀"
      active_when: "墙草仍在、敌方探草/击退不足、目标无法在落地后第一时间拉开"
      fails_if: "敌方持续扫草、开墙、抱团保护，或 chokepoint 被范围技能预封"
      bp_use: "不能早手裸选；适合作为 slot_6 惩罚投掷/远程无保护阵容"
    - id: "heist_contact_dps"
      map_feature_type: "objective_access"
      example_maps:
        - "[[entities/maps/Pit Stop|Pit Stop]]"
        - "[[entities/maps/Hot Potato|Hot Potato]]"
        - "[[entities/maps/Safe(r) Zone|Safe(r) Zone]]"
      route_or_position: "通过墙、草或队友压线接触金库，利用极快装填连续打库"
      objective_conversion: "一次进库成功可造成高爆发 safe damage 并迫使回防"
      active_when: "敌方防守缺瞬间控制，金库附近有可接近路线，队友能吸引火力或同步压线"
      fails_if: "金库路线为长线隔离、跨水但手短无锚点，或敌方能低成本击退/秒杀"
      bp_use: "Heist 条件适配；在 Safe Zone / Bridge Too Far 这类路线明确图要强制走 false_positive_filter"
    - id: "gem_mine_jump_or_chase"
      map_feature_type: "gem_mine_access"
      example_maps:
        - "[[entities/maps/Hard Rock Mine|Hard Rock Mine]]"
        - "[[entities/maps/Gem Fort|Gem Fort]]"
        - "[[entities/maps/Double Swoosh|Double Swoosh]]"
      route_or_position: "跳矿、侧路追 gem carrier、倒计时用侧草切断撤退"
      objective_conversion: "抢宝石或打断敌方倒计时，而不是长时间站中"
      active_when: "敌方 gem carrier 缺位移/控制且我方能接住撤退路线"
      fails_if: "Edgar 被迫承担稳定 mid carrier，或敌方有持续探草和反突进"
      bp_use: "Gem Grab comeback / chase tool，不能替代稳定中路"

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - "scoring_window_creator"
        - "side_grass_scorer_pressure"
        - "anti_thrower_or_backline_dive"
      cannot_fulfill:
        - "稳定清球、破门或持续中路控场"
        - "在敌方控制完整时正面持球硬冲"
      needs_teammate_support:
        - "破门/强控/扫草其一"
        - "能惩罚敌方反突进交技能后的队友"
      false_positive: "只看机动性会高估；必须确认进球路径和敌方控制冷却"
    - mode: "Gem Grab"
      can_fulfill:
        - "侧路追击 gem carrier"
        - "倒计时翻盘进场"
        - "短时间抢矿后撤"
      cannot_fulfill:
        - "长期稳定持宝石"
        - "无视野情况下独立控中"
      needs_teammate_support:
        - "中路稳定火力和探草"
        - "跳入后能接应撤退或补伤害"
      false_positive: "Gem Grab 不是默认强；只有路线/倒计时/目标脆弱时才成立"
    - mode: "Heist"
      can_fulfill:
        - "短窗口高 safe DPS"
        - "逼迫敌方回防"
      cannot_fulfill:
        - "隔水远程打库"
        - "三路隔离图独立赢长线"
      needs_teammate_support:
        - "开路、吸火或同步压线"
        - "防止敌方反推我方金库"
      false_positive: "会跳不等于能打库；短手必须证明目标访问和生存"
    - mode: "Knockout"
      can_fulfill:
        - "最后手刺杀无保护投掷/远程"
        - "利用墙草制造一次击杀确认"
      cannot_fulfill:
        - "开阔长线低承诺换血"
        - "在敌方保留 peel 时先手进场"
      needs_teammate_support:
        - "压血、消耗敌方控制、保留接应路线"
      false_positive: "Belle's Rock 类墙图也要确认入口没有被控；不能把刺客克投掷写成无条件"

  failure_modes:
    - id: "control_or_knockback_stops_entry"
      active_when: "敌方有 Shelly/Gale/Otis/Surge/Maisie/R-T/Chester 等反进场，且技能可留给 Edgar"
      exposed_by: "[[sources/Fandom-Edgar|Fandom-Edgar]] 低血量、短射程和必须贴脸输出"
      mitigation: "只在敌方控制交掉后进场，或作为最后手确认敌方无法补 peel"
      bp_use: "must_avoid / false_positive_filter"
    - id: "open_lane_no_route"
      active_when: "Dry Season、Shooting Star、Bridge Too Far 等长线开阔或三路隔离图"
      exposed_by: "Edgar 攻击距离极短，接近前无远程压力"
      mitigation: "不早选；只有敌方三远程无保护且队友能开路时考虑"
      bp_use: "map_hard_gate"
    - id: "one_way_dive_no_exit"
      active_when: "Super 用于进场后无法击杀或被多人集火"
      exposed_by: "Super 是主要进出资源；Let's Fly 不能替代所有撤退路线"
      mitigation: "保留第二段位移或只打低弹药孤立目标"
      bp_use: "candidate_eval.must_avoid"
    - id: "objective_access_false_positive"
      active_when: "Heist 水域/障碍看似可越过，但过后打不到库或站不住"
      exposed_by: "[[entities/maps/Safe Zone|Safe Zone]] / [[entities/maps/Bridge Too Far|Bridge Too Far]] 的短手假阳性规则"
      mitigation: "要求队友压线、近库墙角锚点或已确认敌方基地清理不足"
      bp_use: "map_factor_false_positive_check"

  conditional_matchup_seeds:
    - target: ["Dynamike", "Grom", "Sprout", "Squeak"]
      direction: "subject_favored"
      source: "[[sources/PLP-Edgar|PLP-Edgar]]"
      mechanism: "Super/Let's Fly 绕过墙体保护并贴脸击杀缺近战自保的投掷"
      active_when: "墙草或侧路给接近路线，敌方投掷无队友 peel，地图不是单入口被预封"
      fails_when: "Belle's Rock 窄口被控、墙被敌方用于预判、或投掷身边有 Gale/Shelly/Otis 保护"
      bp_use: "slot_6 response pick；不能作为 slot_1 泛用反投掷"
    - target: ["Mandy", "Amber", "Poco", "Meg"]
      direction: "subject_favored"
      source: "[[sources/PLP-Edgar|PLP-Edgar]]"
      mechanism: "对低机动或低瞬间反突进目标，Edgar 可越过射程差直接贴脸爆发"
      active_when: "目标孤立、弹药不足、或地图墙草让 Edgar 不需要横穿开阔区"
      fails_when: "目标有队友保护、可在开阔长线提前消耗、或有足够 burst/slow 打断"
      bp_use: "惩罚无保护后排；多用于 4-5/6 位"
    - target: ["Cordelius", "Shelly", "Gale", "Otis", "Chester", "Maisie", "R-T", "Surge"]
      direction: "target_favored"
      source: "[[sources/PLP-Edgar|PLP-Edgar]]"
      mechanism: "这些英雄用沉默、击退、爆发、位移或反坦克控制低成本破坏 Edgar 的贴脸窗口"
      active_when: "反制技能可保留给 Edgar，且 Edgar 没有第二目标或队友同步压制"
      fails_when: "控制已交、目标低弹药且孤立、或 Edgar 用最后手只需完成一次换人/进球"
      bp_use: "ban_reason / must_avoid / enemy_response_prediction"
    - target: ["Pam", "Rosa", "Ash", "Frank", "8-Bit"]
      direction: "volatile"
      source: "[[sources/Fandom-Edgar|Fandom-Edgar]]"
      mechanism: "Edgar 可利用快速 unload 和回血打慢出手高血量目标，但吃满伤害会被反杀"
      active_when: "敌方攻击前摇长、弹药不足、Edgar 可绕身位并持续命中"
      fails_when: "敌方有控制、队友补伤害、或 Edgar 贴脸后无法规避高额爆发"
      bp_use: "不是无条件 anti-tank；只作为局部近战窗口判断"

  slot_notes:
    slot_1: "不适合作稳定一抢；除非地图明确奖励 Brawl Ball scorer 且高优先反制已被 ban"
    slot_2_3: "可用于回答敌方单后排/投掷，但要预留队友处理 Gale/Otis/Shelly/Surge 类自然回应"
    slot_4_5: "适合在已知敌方 2-3 位缺 peel 时锁定惩罚路线，同时补足球得分或 Gem Grab comeback"
    slot_6: "最适合的顺位；最后确认敌方无反进场、地图有路线、目标能被一次进场转化为击杀/进球/打库"
```

## 关联页面

- [[sources/Fandom-Edgar|Fandom 来源摘要: Edgar]]
- [[sources/PLP-Edgar|PLP 来源摘要: Edgar]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
