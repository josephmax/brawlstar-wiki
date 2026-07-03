# Sprout

## 基本信息

- 稀有度：Mythic
- 定位：Artillery
- 类型：投掷封路与地形改写英雄

## 攻击特征

- 主攻击 `Seed Bomb` 会越过障碍并在落地、碰到敌人或弹墙后爆炸。
- 弹墙会增加实际威胁距离，但弹道有空中延迟，近身或高机动目标会显著降低命中率。
- `Overgrowth` 周期性扩大爆炸半径，让 Sprout 更容易命中窄口、墙角和聚集目标。

## 超级技能特征

- Super `Hedge` 会生成临时墙体，阻挡路径和非投掷弹道，并能连接附近墙体或水域。
- Hedge 可用于封锁 choke、切断逃跑路线、保护撤退，也能在 Brawl Ball 中阻挡射门路线。
- `Transplant` 可以销毁现有 Hedge 并立刻重新获得 Super，支持连续封路。

## 角色定位总结

Sprout 是“墙后投掷 + 临时改图”的控制位。他的价值不在正面 DPS，而在把地图路线改成敌方必须绕路、聚集或暴露身位的形状。BP 中必须同时检查墙体是否能保住、敌方是否有开墙/跳跃/刺客路线，以及这次封路能否转成星差、球门防守或宝石区控制。

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: direct_raw_capture_2026-06-30
    plp: direct_raw_capture_2026-06-30
    user_notes: none

  capability_vector:
    effective_range: long_after_landing_or_wall_bounce
    projectile_reliability: medium; 对固定窄口和墙角强，对贴脸、高速和多路线目标弱
    burst: medium; Overgrowth 和 Hypercharge Thorns 能提高区域伤害但不等于稳定秒杀
    sustained_dps: medium_low; 普攻伤害中等，主要靠安全位置和路线税累积
    objective_damage: low; 不是稳定 Heist safe DPS
    mobility: low
    survivability: low_medium; Garden Mulcher/Photosynthesis 可在草墙图提高容错
    engage: low
    disengage: medium_with_Hedge_route_block
    anti_aggro: conditional; Hedge 和墙弹能拖近身，但被贴脸或开墙后很脆
    anti_tank: low_medium; 更偏封路和拖延，不是硬反坦输出
    wall_break: none
    throw_or_wall_bypass: very_high
    area_control: high_with_Hedge_and_Overgrowth
    scouting_or_vision: low; 可用弹跳/爆炸试探草边但不提供真实视野
    team_support: high_route_denial_and_goal_block
    crowd_control: path_blocking_not_status_cc
    terrain_creation: very_high

  build_switches:
    - build: Transplant / Overgrowth / Super Charge + Shield + Damage or Gadget Cooldown
      source: "[[sources/PLP-Sprout|PLP-Sprout]] / [[sources/Fandom-Sprout|Fandom-Sprout]]"
      changes_capabilities:
        - Transplant 让 Hedge 从一次封路变成可重复的地形状态计划
        - Overgrowth 提高窄口、墙角和多人聚集时的命中质量
        - Super Charge/Gadget Cooldown 提高连续封路频率
      enables:
        - repeated_choke_lock
        - knockout_space_denial
        - brawl_ball_goal_block
      mitigates_failure_modes:
        - 单次 Hedge 被绕开或时间结束
        - 普攻半径不足导致窄口压制不稳定
      poor_when:
        - 敌方已经有低成本开墙、跳跃或多路线刺客，Hedge 无法形成真实路线税
      bp_use: 默认竞技 build；选 Sprout 前必须确认封路能转成目标收益
    - build: Garden Mulcher / Photosynthesis bush_survival_variant
      source: "[[sources/Fandom-Sprout|Fandom-Sprout]]"
      changes_capabilities:
        - 提高草丛附近自保和被 poke 后的续航
        - 允许 Sprout 在草墙连接处更久保留 thrower pocket
      enables:
        - bush_wall_pocket_hold
        - longer_retreat_after_lead
      mitigates_failure_modes:
        - 低血量被长线 chip 赶出口袋
      poor_when:
        - 地图缺少可用草丛，或主要问题是必须连续封路
      bp_use: 草墙图或需要防守领先时的 build requirement

  map_feature_hooks:
    - map_feature_type: thrower_pocket_and_choke_lock
      uses_feature_by: 从墙后投掷并用 Hedge 封窄口，让敌方只能绕路或聚集通过
      objective_conversion: Knockout/Bounty 压缩空间、保星、制造第一减员窗口
      active_when: 墙体完整，入口有限，敌方缺开墙或安全跳脸
      fails_if: 墙体被打开、刺客有多路线接近，或队友无法惩罚被封路后的聚集
      example_maps:
        - Belle's Rock
        - Layer Cake
        - Gem Fort
        - Hard Rock Mine
      bp_use: must_answer_or_pick_thrower_pocket_control
    - map_feature_type: brawl_ball_goal_block_and_route_denial
      uses_feature_by: Hedge 临时挡住球路、门前通道或持球推进线，Transplant 支持连续防守
      objective_conversion: 阻止射门、拖延进攻回合、迫使敌方先交开墙/无敌盾
      active_when: 球门或推进路线依赖窄口，Sprout 队友能接住被拖慢的持球人
      fails_if: 敌方有低成本破门、无敌盾撞墙、跳跃进球，或我方没有反推进输出
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Pinball Dreams
        - Triple Dribble
      bp_use: slot_task.goal_block_and_route_tax
    - map_feature_type: gem_mine_entrance_block
      uses_feature_by: Hedge 阻断中心入口或 carrier 追击路线，Seed Bomb 继续压入口
      objective_conversion: 控制宝石矿访问、保护倒计时撤退、制造敌方重进场成本
      active_when: 宝石矿周边有少数入口或墙体可连接 Hedge，队伍能守住侧草
      fails_if: 敌方从侧草绕开、开墙移除中心掩体，或 Sprout 被迫离开 thrower pocket
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Double Swoosh
      bp_use: map_bp_factors.mine_access_denial

  objective_contracts:
    - mode: Knockout_or_Bounty
      can_fulfill:
        - wall_pocket_pressure
        - choke_lock
        - retreat_after_lead
      cannot_fulfill:
        - open_map_marksman_duel
        - self_peel_against_route_assassin
      needs_teammate_support:
        - anti_aggro_or_wallbreak_ban
        - followup_damage_when_enemy_is_forced_through_choke
      false_positive: 墙多不等于 Sprout 必强；若敌方能开墙或跳脸，Sprout 口袋会变成陷阱
    - mode: Brawl Ball
      can_fulfill:
        - goal_block
        - lane_delay
        - defensive_route_denial
      cannot_fulfill:
        - primary_scorer
        - reliable_ball_carry
      needs_teammate_support:
        - scorer_or_wallbreak
        - anti_tank_or_knockback
      false_positive: 挡门只是在防守端拖时间，阵容仍必须有得分窗口
    - mode: Hot Zone
      can_fulfill:
        - narrow_entry_delay_if_map_has_choke
      cannot_fulfill:
        - primary_zone_body
        - broad_zone_clear
      needs_teammate_support:
        - actual_zone_presence
        - anti_dive
      false_positive: Fandom 明确提示 Sprout 的窄攻击和低伤害让他通常不是 Hot Zone 优先替代

  failure_modes:
    - id: wallbreak_or_jump_removes_pocket
      active_when: 敌方 Brock/Colt/Ruffs/Nani 或跳跃/穿墙英雄能低成本移除或绕过 Hedge
      exposed_by: Fandom Hedge 可被 wall-breaking abilities 摧毁，Belle's Rock/Layer Cake 地图规则
      mitigation: ban/answer 开墙，或只在敌方无路线工具时后手
      bp_use: must_avoid_or_plan_protection
    - id: close_contact_after_missed_bomb
      active_when: Mortis/Fang/Edgar/Darryl/Sam 等通过墙草或队友压迫贴到 Sprout
      exposed_by: Fandom 提到 Seed Bomb 近身难命中且有空中延迟
      mitigation: 用 Hedge 锁单一路线，搭配 knockback/slow/anti-aggro 队友
      bp_use: false_positive_filter_for_thrower_pick
    - id: no_objective_conversion
      active_when: Sprout 只是隔墙打伤害，但队伍没有拿星、守门、控矿或站点转换
      exposed_by: BP objective_contract
      mitigation: 在 draft 中补 scorer、carrier、zone body 或 long-range finisher
      bp_use: role_coverage_check
    - id: open_long_map_after_overbreak
      active_when: 墙体被过度打开，地图转成纯远程对枪
      exposed_by: BP 地图建模与决策规范中的 terrain_state_plan
      mitigation: 保墙、选择性封路，或避免在纯开阔图早手暴露 Sprout
      bp_use: terrain_state_plan_check

  conditional_matchup_seeds:
    - target: Belle_or_Bea_or_Penny_or_Gus_or_Amber
      direction: subject_favored
      source: "[[sources/PLP-Sprout|PLP-Sprout]]"
      mechanism: Sprout 可从墙后用 Seed Bomb 和 Hedge 压缩固定长线/炮台/支援位置，让目标无法用直线火力交换
      active_when: 地图有稳定墙后口袋，目标缺开墙、跳脸或投掷反制
      fails_when: 地图被开成纯长线，或目标有队友清 Sprout 口袋
      bp_use: wall_pocket_response_into_static_range
    - target: Spike_or_Tara_or_Eve
      direction: subject_favored
      source: "[[sources/PLP-Sprout|PLP-Sprout]]"
      mechanism: Hedge 阻断中距离控制位的重进场或撤退路线，投掷可以越过其正面控制区
      active_when: 目标必须守入口、矿区或球路，且没有自由水路/侧路直接绕开 Hedge
      fails_when: Eve 或队友从特殊路线换角，Tara 持 Super 开团，或 Spike 队友先压出 Sprout
      bp_use: conditional_control_mirror_pick
    - target: Mortis_or_Fang_or_Darryl_or_Edgar
      direction: target_favored
      source: "[[sources/PLP-Sprout|PLP-Sprout]]"
      mechanism: 突进/滚入/跳入能绕过投掷弹道延迟，贴脸后 Sprout 缺少稳定自保伤害
      active_when: 地图给墙草路线或敌方队友能逼出 Hedge/Transplant
      fails_when: 接近路线单一、Hedge 能锁入口，且 Sprout 队友有稳定 anti-aggro
      bp_use: must_answer_assassin_route_before_sprout
    - target: Carl_or_Gray_or_Sam_or_Ash
      direction: target_favored
      source: "[[sources/PLP-Sprout|PLP-Sprout]]"
      mechanism: Hook、portal、速度前压或高血量路线压力能越过/压穿 Sprout 的口袋控制
      active_when: 目标能从侧角或墙体缺口接触 Sprout，且 Sprout 队友无法立刻 punish
      fails_when: 地图 choke 被 Hedge 连续封住，目标每次进入都被队友集火
      bp_use: route_based_false_positive_filter

  slot_notes:
    slot_1: 只在墙体价值极稳定且敌方低成本开墙/刺客答案被 ban 或代价高时先手。
    slot_2_3: 适合作为回答敌方固定长线/控制位的地图 pick，同时建立 Knockout/Bounty 保空间计划。
    slot_4_5: 用来保护己方 1 位路线、封敌方 2-3 位入口，但必须提前检查敌方 6 位刺客/开墙惩罚。
    slot_6: 敌方三人已经缺开墙、缺跳脸、缺投掷镜像时，可以高上限封死口袋或门前路线。
```

## 关联页面

- [[sources/Fandom-Sprout|Fandom 来源摘要: Sprout]]
- [[sources/PLP-Sprout|PLP 来源摘要: Sprout]]
