# Fandom 来源摘要: Release Notes August 2026

## 来源信息

- 标题：Version History/2026 — Release Notes August 2026
- 来源：[Fandom: Version History/2026](https://brawlstars.fandom.com/wiki/Version_History/2026)（section 1）
- 读取日期：2026-09-03
- Section revid at capture: 217944
- 上游 raw：[[../../raw/sources/fandom/systems/release-notes-august-2026-2026-09-03.md|release-notes-august-2026-2026-09-03]]
- source_quality：direct_raw_capture_patch_notes
- source_type：monthly_release_notes / balance_change_index

## 可用范围

- usable_for：patch_balance_manifest、release_state_tracking、new_brawler_inventory、hypercharge_and_buffie_intake_queue
- not_usable_for：current_meta_strength、runtime_recommendation、Brawl Arena（维护者决定：本库不追踪 Brawl Arena）

## 页面核心内容

- 新英雄（第 107、108 位，均为 Mythic）：`Cosmo`（Controller）、`Vince`（Damage Dealer）。两者 PLP guide 2026-09-03 仍为 404，按 roster 规则不进入 BP 英雄集合，只入 ingest 队列。
- 新极限充能：`Nori (MASTER FISHERMAN)`——入水时把范围内敌人拉入再造成范围伤害；`Wendy (GREEN ENERGY)`——提高护盾发生器耐久并为 Wendy 与范围内队友吸收 90% 伤害。
- 新芭菲（6 人）：`Poco`、`El Primo`、`Amber`、`Gus`、`Chuck`、`Shade`。Poco / El Primo / Amber / Gus / Chuck / Shade 同时带基础技能 rework（Gadget / Star Power / Hypercharge 级别），Chuck 另有全 Super 重做（4 充能、开局满 Super、取消自动充能、取消插杆击退）。
- 平衡性调整：19 人 Buff、12 人 Nerf（含 Wendy 发布后首次削弱：发生器 3500→2500、减伤 75%→60%、受盾伤充能 50%→30%、Super 充能率 -20%；Nori：Sushi Snack 冷却 12→18s、生命 3800→3500、斩击伤害 1100→1000）。
- `Brawl Arena Only` 缩放调整存在但被本库边界排除，不记录、不进入 manifest。

## 与本地 wiki 的意义

- `Wendy` 从 `FutureUpdate` 转为 released（页面 2026-09-02 仍活跃编辑）；发布后数值与 [[sources/Supercell-Wendy-Announcement-June-2026|Wendy Announcement]] 的预发布值在本期削弱前一致（发生器 3500 / 75%），预发布冲突就此闭合，以发布后状态重建 source summary。
- `Nori` 的 Hypercharge（MASTER FISHERMAN）与三项削弱补入其来源页与实体页当前数值输入。
- 六个新芭菲与相关 rework 折叠进对应英雄实体页的稳定字段（build_switches / capability / failure_modes），数值变化走本 manifest 与断点审计。
- Roster 影响见 [[sources/Brawler-Roster|Brawler Roster]] 与新 manifest：released roster 105 → 108。

## balance_patch_manifest

```json
{
  "balance_patch_manifest": {
    "schema": "balance_breakpoint_manifest.v1",
    "patch_id": "2026-08-release-notes",
    "effective_order": 4,
    "effective_at": "2026-08-06",
    "scope": ["ranked", "power_level_11_normalized"],
    "source_refs": [
      "[[sources/Fandom-Release-Notes-August-2026|Release Notes August 2026]]"
    ],
    "notes": [
      "effective_at 为 Windstock 赛季上线观察日期（2026-08-06，二手来源），Fandom 版本页未标注确切上线日。",
      "Brawl Arena Only 缩放调整按维护者边界排除，不入账。",
      "六个新芭菲属于新增 loadout 选项而非既有输入变化，不入 before/after 账本；效果折叠进实体稳定字段。"
    ],
    "changes": [
      {"id": "nori_main_slash", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Nori", "packet_id": "main.slash_impact", "old_damage": 1100, "new_damage": 1000, "power_level": 1, "packet_unit": "slash_impact", "repeat_model": "identical", "active_when": "主攻击单次斩击命中；链首账目，1100 为发布值"},
      {"id": "bo_main_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Bo", "packet_id": "main.impact", "old_damage": 640, "new_damage": 700, "power_level": 1, "packet_unit": "impact", "repeat_model": "identical", "active_when": "单枚箭命中"},
      {"id": "janet_main_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Janet", "packet_id": "main.impact", "old_damage": 1000, "new_damage": 1100, "power_level": 1, "packet_unit": "impact", "repeat_model": "identical", "active_when": "单发普攻命中"},
      {"id": "bea_super_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Bea", "packet_id": "super.impact", "old_damage": 100, "new_damage": 130, "power_level": 1, "packet_unit": "impact", "repeat_model": "resource_gated", "active_when": "Super 命中一次；未假设多段"},
      {"id": "jessie_turret_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Jessie", "packet_id": "super.turret_bolt_impact", "old_damage": 260, "new_damage": 300, "power_level": 1, "packet_unit": "turret_bolt_impact", "repeat_model": "identical", "active_when": "Scrappy 单发 bolt 命中；attacker 为 summon，不改变英雄分母"},
      {"id": "tara_black_portal_shadow_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Tara", "packet_id": "super.black_portal_shadow_impact", "old_damage": 800, "new_damage": 1000, "power_level": 1, "packet_unit": "shadow_impact", "repeat_model": "resource_gated", "active_when": "Black Portal shadow 单次命中；attacker 为 summon"},
      {"id": "leon_clone_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Leon", "packet_id": "gadget.clone_projectile_impact", "old_damage": 200, "new_damage": 800, "power_level": 1, "packet_unit": "clone_projectile_impact", "repeat_model": "resource_gated", "active_when": "Clone Projector 分身单发命中；attacker 为 summon"},
      {"id": "dynamike_fidget_spinner_explosion", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Dynamike", "packet_id": "gadget.fidget_spinner_explosion", "old_damage": 1200, "new_damage": 1400, "power_level": 1, "packet_unit": "explosion_impact", "repeat_model": "one_off", "active_when": "Fidget Spinner 单次旋转爆炸命中"},
      {"id": "lumi_main_recall_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Lumi", "packet_id": "main.recall_impact", "old_damage": 900, "new_damage": 800, "power_level": 1, "packet_unit": "recall_impact", "repeat_model": "identical", "active_when": "主攻击回收段单次命中"},
      {"id": "rico_bouncy_castle_split_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Rico", "packet_id": "gadget.bouncy_castle_split_impact", "old_damage": 980, "new_damage": 900, "power_level": 1, "packet_unit": "split_projectile_impact", "repeat_model": "resource_gated", "active_when": "Bouncy Castle 分裂弹单枚命中；未假设全中"},
      {"id": "chuck_super_dash_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Chuck", "packet_id": "super.dash_impact", "old_damage": 1750, "new_damage": 800, "power_level": 1, "packet_unit": "dash_impact", "repeat_model": "one_off", "active_when": "Super 冲撞命中一次；重做后最多 4 充能，多次冲撞不自动连算"},
      {"id": "melodie_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Melodie", "state_id": "body", "stat": "health", "old": 3800, "new": 4000, "power_level": 1},
      {"id": "hank_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Hank", "state_id": "body", "stat": "health", "old": 5200, "new": 5500, "power_level": 1},
      {"id": "chuck_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Chuck", "state_id": "body", "stat": "health", "old": 4700, "new": 4400, "power_level": 1},
      {"id": "nori_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Nori", "state_id": "body", "stat": "health", "old": 3800, "new": 3500, "power_level": 1},
      {"id": "jacky_hardy_hard_hat", "type": "defense_modifier", "change_class": "breakpoint_supported", "brawler": "Jacky", "modifier_id": "hardy_hard_hat", "state_id": "body", "stat": "damage_reduction", "old": 0.20, "new": 0.25, "active_when": "装备 Hardy Hard Hat Star Power"},
      {"id": "meg_force_field", "type": "defense_modifier", "change_class": "breakpoint_supported", "brawler": "Meg", "modifier_id": "force_field_out_of_mecha", "state_id": "body", "stat": "damage_reduction", "old": 0.40, "new": 0.30, "active_when": "离开机甲后的护盾窗口"},
      {"id": "chuck_super_shield", "type": "defense_modifier", "change_class": "breakpoint_supported", "brawler": "Chuck", "modifier_id": "super_dash_shield", "state_id": "body", "stat": "damage_reduction", "old": 0.50, "new": 0.35, "active_when": "Super 冲撞生效期间；与其他 DR 的叠加关系待复核"},
      {"id": "wendy_generator_health", "type": "other", "change_class": "non_breakpoint", "brawler": "Wendy", "reason": "发生器耐久 3500->2500 属 deployable durability，不进英雄分母；Hypercharge GREEN ENERGY 再提高耐久的具体值未在本期标注"},
      {"id": "wendy_generator_damage_reduction", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Wendy", "reason": "发生器承担伤害 75%->60% 是范围内多目标伤害分担/redirect 模型，不是单目标静态 DR 叠加"},
      {"id": "wendy_super_charge_rates", "type": "other", "change_class": "non_breakpoint", "brawler": "Wendy", "reason": "Super 充能率 -20%、受盾伤充能 50%->30% 属资源时间变化"},
      {"id": "ash_tank_trait_charge", "type": "other", "change_class": "non_breakpoint", "brawler": "Ash", "reason": "Tank Trait 受伤充 Super -15% 属资源时间变化"},
      {"id": "max_hyper_buffie_super_charge", "type": "other", "change_class": "non_breakpoint", "brawler": "Max", "reason": "Hyper Buffie 命中充能 7%->6% 属资源时间变化"},
      {"id": "max_gadget_cooldowns", "type": "other", "change_class": "non_breakpoint", "brawler": "Max", "reason": "Phase Shifter 与 Sneaky Sneakers 冷却 15s->18s"},
      {"id": "max_super_charge_rate", "type": "other", "change_class": "non_breakpoint", "brawler": "Max", "reason": "Super 充能率 -8%，opaque 单位"},
      {"id": "brock_hyper_buffie_side_rockets", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Brock", "reason": "Buffie 侧向小火箭伤害 60%->40% 是主火箭的伴随倍率，需与主包组合"},
      {"id": "rico_robo_retreat_buffie_speed", "type": "other", "change_class": "non_breakpoint", "brawler": "Rico", "reason": "Star Buffie Robo Retreat 极限移速 60%->50% 属机动数值"},
      {"id": "rico_multiball_cooldown", "type": "other", "change_class": "non_breakpoint", "brawler": "Rico", "reason": "Multiball Launcher 冷却 19s->22s"},
      {"id": "meg_toolbox_cooldown", "type": "other", "change_class": "non_breakpoint", "brawler": "Meg", "reason": "Tool Box 冷却 22s->25s"},
      {"id": "griff_coin_shower_cooldown", "type": "other", "change_class": "non_breakpoint", "brawler": "Griff", "reason": "Coin Shower 冷却 15s->18s"},
      {"id": "griff_super_charge_from_super", "type": "other", "change_class": "non_breakpoint", "brawler": "Griff", "reason": "Super 命中回充 88->70，opaque 单位"},
      {"id": "ruffs_super_charge_rate", "type": "other", "change_class": "non_breakpoint", "brawler": "Ruffs", "reason": "Super 充能率 -20%，opaque 单位"},
      {"id": "colette_super_charge_rate", "type": "other", "change_class": "non_breakpoint", "brawler": "Colette", "reason": "Super 充能率 +10%，opaque 单位"},
      {"id": "ziggy_super_charge_rate", "type": "other", "change_class": "non_breakpoint", "brawler": "Ziggy", "reason": "Super 充能率 +6%，opaque 单位"},
      {"id": "eve_super_charge_from_super", "type": "other", "change_class": "non_breakpoint", "brawler": "Eve", "reason": "Super 命中回充 +17%，opaque 单位"},
      {"id": "eve_hatchling_count", "type": "other", "change_class": "non_breakpoint", "brawler": "Eve", "reason": "Super 孵化数 3->4 改变召唤体数量模型，非标量包"},
      {"id": "clancy_reload", "type": "other", "change_class": "non_breakpoint", "brawler": "Clancy", "reason": "装填 2000->1800 属攻击频率"},
      {"id": "clancy_token_thresholds", "type": "other", "change_class": "non_breakpoint", "brawler": "Clancy", "reason": "Stage 2 tokens 6->5、Stage 3 tokens 21->24 属阶段资源"},
      {"id": "maisie_projectile_speed", "type": "other", "change_class": "non_breakpoint", "brawler": "Maisie", "reason": "弹速 3000->3200"},
      {"id": "bolt_acceleration", "type": "other", "change_class": "non_breakpoint", "brawler": "Bolt", "reason": "加速度 -15% 属机动数值"},
      {"id": "lola_super_ego_speed_match", "type": "other", "change_class": "non_breakpoint", "brawler": "Lola", "reason": "Super Ego 移速改为与本体现值一致"},
      {"id": "jaeyong_main_heal", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Jae-Yong", "reason": "主攻击治疗 650->750 是治疗量，不入静态 EHP"},
      {"id": "buster_utility_belt_heal", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Buster", "reason": "Utility Belt 治疗 450->600 是治疗量"},
      {"id": "buster_blockbuster_bonus", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Buster", "reason": "Blockbuster 加成 15%->20% 是条件伤害倍率"},
      {"id": "tara_shadow_health", "type": "other", "change_class": "non_breakpoint", "brawler": "Tara", "reason": "shadow 生命 3400->4000 / 3000->4000 属 summon durability，不进英雄分母"},
      {"id": "tara_healing_shadow_heal", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Tara", "reason": "Healing Shade 治疗 400->600 是治疗量"},
      {"id": "shade_spooky_speedster", "type": "other", "change_class": "non_breakpoint", "brawler": "Shade", "reason": "Spooky Speedster 移速 15%->20% 属机动数值"},
      {"id": "chuck_super_model_rework", "type": "other", "change_class": "non_breakpoint", "brawler": "Chuck", "reason": "Super 改为 4 充能、开局满 Super、取消自动充能与插杆击退；充能模型变化使旧连续冲撞假设全部失效"},
      {"id": "chuck_main_attack_rework", "type": "other", "change_class": "non_breakpoint", "brawler": "Chuck", "reason": "射程 20->18、弹速 1750->2700、伤害衰减移除"},
      {"id": "poco_gadget_sp_reworks", "type": "other", "change_class": "non_breakpoint", "brawler": "Poco", "reason": "Tuning Fork / Protective Tunes / Da Capo! 重做为脉冲治疗、净化区域与常驻治疗基线；旧 before/after 不可比，效果折叠进实体字段"},
      {"id": "el_primo_gadget_reworks", "type": "other", "change_class": "non_breakpoint", "brawler": "El Primo", "reason": "Suplex Supplement / Asteroid Belt 重做为抓取投掷与拦截投射物；行为重做"},
      {"id": "amber_gadget_sp_reworks", "type": "other", "change_class": "non_breakpoint", "brawler": "Amber", "reason": "Fire Starters 改为 3500 耐久油桶、Wild Flames 黏滞油迹、Scorching Siphon 改触发条件；Super 不再清除旧油"},
      {"id": "gus_gadget2_rework", "type": "other", "change_class": "non_breakpoint", "brawler": "Gus", "reason": "Gadget 2 重做为 Knockback Spirit（击退灵体，末端转为治疗灵）"},
      {"id": "shade_kit_adjustments", "type": "other", "change_class": "non_breakpoint", "brawler": "Shade", "reason": "Jump Scare 重做为短跳恐惧、Hypercharge The Frightener 重做为墙内回血"}
    ]
  }
}
```

## 关联页面

- [[sources/Fandom-Release-Notes-June-2026|Fandom 来源摘要: Release Notes June 2026]]
- [[sources/Fandom-Maintenance-July-8-2026|Fandom 来源摘要: Maintenance - July 8, 2026]]
- [[sources/Supercell-Maintenance-August-4-2026|Supercell 来源摘要: Maintenance - August 4, 2026]]
- [[sources/Brawler-Roster|Brawler Roster]]
- [[sources/Fandom-Wendy|Fandom 来源摘要: Wendy]]
- [[sources/Fandom-Nori|Fandom 来源摘要: Nori]]
