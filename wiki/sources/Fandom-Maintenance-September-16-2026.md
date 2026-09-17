# Fandom 来源摘要: Maintenance - September 16, 2026

## 来源信息

- 标题：Version History/2026 — Maintenance - September 16th
- 来源：[Fandom: Version History/2026](https://brawlstars.fandom.com/wiki/Version_History/2026)（section "Maintenance - September 16th"）
- 读取日期：2026-09-17
- Section revid at capture: 219043（页面修订 2026-09-16T09:12:51Z）
- 上游 raw：[[../../raw/sources/fandom/systems/maintenance-september-16-2026-2026-09-17.md|maintenance-september-16-2026-2026-09-17]]
- 受影响英雄当前态 raw：Wendy / Willow / Juju / Ollie / Belle / El Primo / R-T / Chuck 共 8 人于 2026-09-17 重抓（Wendy 经同一 MediaWiki API 通道手动抓取，脚本默认 roster 不含她）
- source_quality：direct_raw_capture_patch_notes
- source_type：maintenance_balance_change_index

## 可用范围

- usable_for：patch_balance_manifest、affected_brawler_index、post_patch_current_value_verification
- not_usable_for：current_meta_strength、runtime_recommendation、tier_or_pick_priority

## 页面核心内容

2026-09-16 维护补丁，削弱 9 人（Shade、Gus、El Primo、Amber、Nori、Wendy、Meg、Colette、Brock），增强 9 人（Poco、Chuck、Ollie、Trunk、Willow、Juju、Pam、Belle、R-T），另有战斗相关 bug fix（respawn shield 在 dash/jump 时移除、Showdown 变形不再误得 respawn shield、Eve 极限充能 Super 修复为 4 孵化等）。

与本地 wiki 的消费关系：

- 可计算断点变化集中在：Wendy / Willow / Juju 血量、Ollie / Belle 主攻包、El Primo（Meteor Rush Buffie 护盾减伤）、R-T（Recording 分体头/腿减伤）。
- R-T 的 Recording 维护索引只写头部 `20% -> 25%`；个人页 direct raw 显示分体腿替代值同步 `29%->50%` 变为 `29%->55%`（2026-07-17 旧 raw 可证改前态），两行均入账。
- Wendy 存在三处来源差异，详见下方 manifest notes 与各排除行。
- 全英雄移速上调（Wendy 页 History 记录 770→800，2026-09-01 生效）不属于本补丁，不入账；涉及英雄页的移速文案按当前 raw 校准。

## balance_patch_manifest

```json
{
  "balance_patch_manifest": {
    "schema": "balance_breakpoint_manifest.v1",
    "patch_id": "2026-09-16-maintenance",
    "effective_order": 5,
    "effective_at": "2026-09-16",
    "scope": ["ranked", "power_level_11_normalized"],
    "source_refs": [
      "[[sources/Fandom-Maintenance-September-16-2026|Maintenance - September 16, 2026]]"
    ],
    "notes": [
      "R-T Recording：维护索引只给 20%->25%（头部）；个人页 direct raw（revid 219087）显示分体腿替代减伤 29%->50% 变为 29%->55%，与头部同步 +5 个百分点。以个人页为准拆成两行 supported。",
      "Wendy 出生护盾是 barrier_hp 比例值，v1 账本行只接受 damage_reduction，故记为 unsupported 排除；其当前值已按 profile 更新（40% max = 1000/P1），当前态矩阵会反映。",
      "Wendy Solar Shield 发生器加成数值多口径：维护索引 1000->600、个人页 History 1800->1080、页面引语 1200、正文 24%。各口径无法在同一 Power Level 下对齐，记 source_conflict 排除。",
      "Wendy Trait 受盾伤充能 30%->15% 出现在个人页 16/09 History，维护索引未列；按个人页入排除行。",
      "维护索引 'Hypercharge - turret health 4500->3500' 与个人页分解一致：基础炮台 2500 + GREEN ENERGY 加成 2000->1000。",
      "Amber Fire Starters 油桶耐久维护索引 1750->1300 与 8 月 notes 的 3500 为同一值在不同 Power Level（PL1 x2 = PL11）；行内 power_level 标注为 1。",
      "全英雄移速上调（2026-09-01 生效，Wendy 770->800）不属于本补丁链，不入账。"
    ],
    "changes": [
      {"id": "wendy_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Wendy", "state_id": "body", "stat": "health", "old": 2000, "new": 2500, "power_level": 1, "active_when": "本体基础血量；PL11 对应 4000->5000"},
      {"id": "willow_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Willow", "state_id": "body", "stat": "health", "old": 3300, "new": 3600, "power_level": 1, "active_when": "本体基础血量；PL11 对应 6600->7200"},
      {"id": "juju_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Juju", "state_id": "body", "stat": "health", "old": 3100, "new": 3500, "power_level": 1, "active_when": "本体基础血量；PL11 对应 6200->7000"},
      {"id": "ollie_main_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Ollie", "packet_id": "main.impact", "old_damage": 900, "new_damage": 1000, "power_level": 1, "packet_unit": "soundwave_impact", "repeat_model": "identical", "active_when": "单发音波命中单个目标；穿透不改变单体包"},
      {"id": "belle_main_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Belle", "packet_id": "main.impact", "old_damage": 1040, "new_damage": 1140, "power_level": 1, "packet_unit": "bolt_impact", "repeat_model": "identical", "active_when": "主弹直接命中单个目标；弹跳为伴随半伤包"},
      {"id": "el_primo_meteor_rush_buffie_shield", "type": "defense_modifier", "change_class": "breakpoint_supported", "brawler": "El Primo", "modifier_id": "meteor_rush_buffie_shield", "state_id": "body", "stat": "damage_reduction", "old": 0.20, "new": 0.15, "active_when": "装备 Meteor Rush 星徽与 Star Buffie，Super 落地后 3 秒窗口内"},
      {"id": "rt_recording_split_head", "type": "defense_modifier", "change_class": "breakpoint_supported", "brawler": "R-T", "modifier_id": "recording_split_head", "state_id": "split_head_full_health", "stat": "damage_reduction", "old": 0.20, "new": 0.25, "active_when": "分体形态且装备 Recording"},
      {"id": "rt_recording_split_legs", "type": "defense_modifier", "change_class": "breakpoint_supported", "brawler": "R-T", "modifier_id": "recording_split_legs", "state_id": "split_legs", "stat": "damage_reduction", "old": 0.50, "new": 0.55, "active_when": "分体形态且装备 Recording；替代腿内置 29% 而非相加"},
      {"id": "wendy_spawn_shield_ratio", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Wendy", "reason": "出生护盾从 100% max health 降至 40%（PL1 2000->1000；PL11 4000->2000），是 barrier_hp 比例值，v1 账本行只接受 damage_reduction；profile 当前值已同步，出生时点有效血量 8000->7000（PL11）"},
      {"id": "wendy_attack_self_shield", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Wendy", "reason": "普攻自盾 580->300（PL1）随攻击循环时序变化；队友盾 760（PL1）本次未变"},
      {"id": "wendy_trait_super_charge", "type": "other", "change_class": "non_breakpoint", "brawler": "Wendy", "reason": "Trait 受盾伤充能 30%->15% 属资源时间变化；来源为个人页 History，维护索引未列"},
      {"id": "wendy_solar_shield_generator_bonus", "type": "other", "change_class": "source_conflict", "brawler": "Wendy", "reason": "发生器耐久加成削弱数值多口径：维护索引 1000->600、个人页 History 1800->1080、引语 1200、正文 24%；deployable durability 本不入英雄分母，冲突保留不统一"},
      {"id": "wendy_green_energy_turret_bonus", "type": "other", "change_class": "non_breakpoint", "brawler": "Wendy", "reason": "GREEN ENERGY 炮台加成 2000->1000（PL1），维护索引表述为含基础的 4500->3500；deployable durability"},
      {"id": "wendy_wind_powered_water_jump", "type": "other", "change_class": "non_breakpoint", "brawler": "Wendy", "reason": "Wind-Powered 可跳上水面，行为变化无数值"},
      {"id": "shade_hyper_buffie_bonus_damage", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Shade", "reason": "Hypercharge Buffie 附加伤害 75%->30% 是主包伴随倍率，需与主包组合"},
      {"id": "shade_super_charge_near_enemies", "type": "other", "change_class": "non_breakpoint", "brawler": "Shade", "reason": "近敌 Super 充能 -15%，opaque 单位"},
      {"id": "shade_long_arms_cooldown", "type": "other", "change_class": "non_breakpoint", "brawler": "Shade", "reason": "Long arms 冷却 18s->20s"},
      {"id": "shade_jump_scare_fear_radius", "type": "other", "change_class": "non_breakpoint", "brawler": "Shade", "reason": "恐惧半径 1000->600"},
      {"id": "gus_knockback_spirit_cooldown", "type": "other", "change_class": "non_breakpoint", "brawler": "Gus", "reason": "Knockback Spirit 冷却增至 18s；来源未给 from 值，链条不连续，不入 supported"},
      {"id": "gus_health_bonanza_healing", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Gus", "reason": "Health Bonanza 治疗加成 100%->75% 是治疗量"},
      {"id": "el_primo_asteroid_belt_cooldown", "type": "other", "change_class": "non_breakpoint", "brawler": "El Primo", "reason": "Asteroid Belt 冷却 16s->20s"},
      {"id": "el_primo_asteroid_belt_super_charge", "type": "other", "change_class": "non_breakpoint", "brawler": "El Primo", "reason": "Asteroid Belt 命中充 Super -50%，opaque 单位"},
      {"id": "el_primo_meteor_rush_speed_duration", "type": "other", "change_class": "non_breakpoint", "brawler": "El Primo", "reason": "Meteor Rush 加速 4s->3s"},
      {"id": "amber_fire_starters_barrel_health", "type": "other", "change_class": "non_breakpoint", "brawler": "Amber", "reason": "Fire Starters 油桶耐久 1750->1300（PL1，等于 PL11 3500->2600）；deployable durability"},
      {"id": "amber_wild_flames_oil_duration", "type": "other", "change_class": "non_breakpoint", "brawler": "Amber", "reason": "Wild Flames 油迹持续 3s->1s"},
      {"id": "amber_hyper_buffie_burn_damage", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Amber", "reason": "Buffie 灼烧 500->240 是 DoT，需时间序列建模"},
      {"id": "nori_main_charge_time", "type": "other", "change_class": "non_breakpoint", "brawler": "Nori", "reason": "主攻击最大蓄力时间 +25%"},
      {"id": "nori_hypercharge_rate", "type": "other", "change_class": "non_breakpoint", "brawler": "Nori", "reason": "极限充能速率 50->28，opaque 单位"},
      {"id": "meg_repurpose_knockback", "type": "other", "change_class": "non_breakpoint", "brawler": "Meg", "reason": "Repurpose 投射物击退移除（仅爆炸保留击退），行为变化"},
      {"id": "colette_hyper_buffie_second_projectile", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Colette", "reason": "Buffie 第二弹伤害 50%->35% 是主包伴随倍率"},
      {"id": "brock_rocket_laces_cooldown", "type": "other", "change_class": "non_breakpoint", "brawler": "Brock", "reason": "Rocket Laces 冷却 20s->22s"},
      {"id": "brock_super_charge_from_super", "type": "other", "change_class": "non_breakpoint", "brawler": "Brock", "reason": "Super 命中回充 80->70，opaque 单位"},
      {"id": "poco_tuning_fork_healing", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Poco", "reason": "Tuning Fork 治疗 500->700 是治疗量"},
      {"id": "poco_da_capo_healing", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Poco", "reason": "Da Capo! 治疗 320->400 是治疗量"},
      {"id": "chuck_pit_stop_slow_duration", "type": "other", "change_class": "non_breakpoint", "brawler": "Chuck", "reason": "Pit Stop 减速 1s->2s，控制效果"},
      {"id": "chuck_pit_stop_slow_potency", "type": "other", "change_class": "non_breakpoint", "brawler": "Chuck", "reason": "Pit Stop 减速强度 20%->30%，控制效果"},
      {"id": "chuck_pit_stop_buffie_area_damage", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Chuck", "reason": "Pit Stop Buffie 区域伤害 100->400，direct raw 显示 4 秒内至多 4 跳，是时间序列 DoT 区，不做静态包"},
      {"id": "trunk_ant_speed", "type": "other", "change_class": "non_breakpoint", "brawler": "Trunk", "reason": "蚁上移速 25%->30%，机动数值"},
      {"id": "trunk_super_charge_rate", "type": "other", "change_class": "non_breakpoint", "brawler": "Trunk", "reason": "Super 充能 70->75，opaque 单位"},
      {"id": "willow_reload", "type": "other", "change_class": "non_breakpoint", "brawler": "Willow", "reason": "装填 2000->1800 属攻击频率"},
      {"id": "juju_super_charge_rate", "type": "other", "change_class": "non_breakpoint", "brawler": "Juju", "reason": "Super 充能 65->75，opaque 单位"},
      {"id": "pam_turret_health", "type": "other", "change_class": "non_breakpoint", "brawler": "Pam", "reason": "炮台耐久 3040->3300 属 summon durability，不进英雄分母"},
      {"id": "pam_super_healing", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Pam", "reason": "Super 治疗 500->600 是治疗量"},
      {"id": "pam_hypercharge_turret_health", "type": "other", "change_class": "non_breakpoint", "brawler": "Pam", "reason": "极限充能炮台耐久 4200->4500 属 summon durability"},
      {"id": "respawn_shield_dash_fix", "type": "other", "change_class": "non_breakpoint", "reason": "Respawn shield 使用 dash/jump 时移除；影响 respawn 护盾窗口有效性，不改变任何静态输入"},
      {"id": "eve_hypercharge_hatchling_fix", "type": "other", "change_class": "non_breakpoint", "reason": "Eve 极限充能 Super 修复为 4 孵化，对齐 8 月账本的 3->4 行"}
    ]
  }
}
```

## 关联页面

- [[sources/Fandom-Release-Notes-June-2026|Fandom 来源摘要: Release Notes June 2026]]
- [[sources/Fandom-Maintenance-July-8-2026|Fandom 来源摘要: Maintenance - July 8, 2026]]
- [[sources/Supercell-Maintenance-August-4-2026|Supercell 来源摘要: Maintenance - August 4, 2026]]
- [[sources/Fandom-Release-Notes-August-2026|Fandom 来源摘要: Release Notes August 2026]]
- [[entities/brawlers/Wendy|Wendy]]、[[entities/brawlers/Willow|Willow]]、[[entities/brawlers/Juju|Juju]]、[[entities/brawlers/Ollie|Ollie]]、[[entities/brawlers/Belle|Belle]]、[[entities/brawlers/El Primo|El Primo]]、[[entities/brawlers/R-T|R-T]]、[[entities/brawlers/Chuck|Chuck]]
