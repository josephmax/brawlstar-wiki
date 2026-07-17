# Fandom 来源摘要: Release Notes June 2026

## 来源信息

- 标题：Version History/2026 - Release Notes June 2026
- 来源：Fandom Version History/2026
- 读取日期：2026-06-30
- 上游 raw：[[../../raw/sources/fandom/systems/release-notes-june-2026-2026-06-30|release-notes-june-2026-2026-06-30]]
- source_quality：direct_raw_capture_from_fandom_version_history
- source_type：patch_notes / balance_changes / version_context

## 可用范围

- usable_for: version_audit, build_candidate_changes, ability_rework_detection, BP impact hypotheses, matchup_threshold_watchlist, current_model_evidence_when_qualitative
- not_usable_for: long_term_meta_strength, unconditional_counter_claim, direct_pick_priority_without_map_and_draft_context

## BP 读取边界

本来源不应被当作数值清单直接灌入英雄页。进入 BP 知识层时，只保留满足以下任一条件的变化：

- 改变 build 的功能和使用场景。
- 改变某个英雄的关键失败条件，例如反突、保命、开墙、控场、召唤物耐久或资源循环。
- 改变地图职责的执行方式，例如 Brawl Ball 得分窗口、Heist safe access、Hot Zone 站圈/清圈、Gem carrier retreat。
- 改变已存在条件化对位边的成立条件或失效条件。

普通血量、伤害、冷却、弹速变化如果暂时不能推导出明确 BP 后果，只进入观察名单，不反写成稳定结论。

数值变化现在允许进入下方 patch manifest 和生成式 breakpoint audit；这仍不等于自动写入稳定 BP 对位或强度结论。

## 断点审计 Manifest

```json
{
  "balance_patch_manifest": {
    "schema": "balance_breakpoint_manifest.v1",
    "patch_id": "2026-06-ranked-balance",
    "effective_order": 1,
    "effective_at": "2026-06-29",
    "scope": ["ranked", "power_level_11_normalized"],
    "source_refs": ["[[sources/Fandom-Release-Notes-June-2026|Release Notes June 2026]]"],
    "changes": [
      {"id": "piper_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Piper", "state_id": "body", "stat": "health", "old": 2500, "new": 2800, "power_level": 1},
      {"id": "piper_main_max_range", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Piper", "packet_id": "main.max_range_impact", "old_damage": 1700, "new_damage": 1800, "power_level": 1, "packet_unit": "impact", "repeat_model": "identical", "active_when": "最大伤害距离命中；不代表所有距离"},
      {"id": "mandy_main_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Mandy", "packet_id": "main.impact", "old_damage": 1300, "new_damage": 1400, "power_level": 1, "packet_unit": "impact", "repeat_model": "identical", "active_when": "单枚普攻命中"},
      {"id": "mandy_hard_candy", "type": "defense_modifier", "change_class": "breakpoint_supported", "brawler": "Mandy", "modifier_id": "hard_candy", "state_id": "body", "stat": "damage_reduction", "old": 0.40, "new": 0.50, "active_when": "保持 Focus 且装备 Hard Candy"},
      {"id": "gale_super_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Gale", "packet_id": "super.one_wind_impact", "old_damage": 600, "new_damage": 800, "power_level": 1, "packet_unit": "impact", "repeat_model": "resource_gated", "active_when": "一次 Super 风命中；Hypercharge 双风命中数另算"},
      {"id": "lawrie_plug_projectile", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Larry & Lawrie", "reason": "150->200 是 Lawrie 每枚插头，不是英雄本体一次 Super 总伤害；召唤物多弹序列另建 packet"},
      {"id": "lawrie_health", "type": "other", "change_class": "non_breakpoint", "brawler": "Larry & Lawrie", "reason": "3000->3300 属于 summon durability，不进入英雄数量分母"},
      {"id": "sprout_main_explosion", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Sprout", "packet_id": "main.explosion", "old_damage": 1040, "new_damage": 1100, "power_level": 1, "packet_unit": "explosion", "repeat_model": "identical", "active_when": "Seed Bomb 单次爆炸命中"},
      {"id": "grigri_health", "type": "other", "change_class": "non_breakpoint", "brawler": "Juju", "reason": "3600->4000 属于 summon durability，不进入英雄数量分母"},
      {"id": "gray_main_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Gray", "packet_id": "main.impact", "old_damage": 1160, "new_damage": 1280, "power_level": 1, "packet_unit": "impact", "repeat_model": "identical", "active_when": "单发普攻命中；Grand Piano 同步引用该伤害但属于 Gadget 条件"},
      {"id": "starr_nova_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Starr Nova", "state_id": "body", "stat": "health", "old": 3700, "new": 4000, "power_level": 1},
      {"id": "starr_nova_sword", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Starr Nova", "packet_id": "super_form.sword_impact", "old_damage": 1000, "new_damage": 1100, "power_level": 1, "packet_unit": "impact", "repeat_model": "resource_gated", "active_when": "7 秒 Super 剑形态内攻击命中"},
      {"id": "carl_pickaxe_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Carl", "packet_id": "main.one_impact", "old_damage": 740, "new_damage": 820, "power_level": 1, "packet_unit": "impact", "repeat_model": "identical", "active_when": "去程或回程的一次命中；完整 ammo 双命中不自动假设"},
      {"id": "rt_split_impact", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "R-T", "packet_id": "main.split_eat_static_impact", "old_damage": 740, "new_damage": 1240, "power_level": 1, "packet_unit": "one_body_impact", "repeat_model": "resource_gated", "active_when": "分体形态头或腿的一次范围命中；双端同时命中另建组合包"},
      {"id": "mortis_creature", "type": "other", "change_class": "source_conflict", "brawler": "Mortis", "reason": "patch 与技能 quote 支持 760->700，但当前 infobox/prose 仍保留旧比例派生值，待统一后再计算"},
      {"id": "mortis_combo_spinner_multiplier", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Mortis", "reason": "半血以下 50%->30% 是条件倍率，需与当前基础包和目标当前血量序列组合"},
      {"id": "colette_mass_tax", "type": "defense_modifier", "change_class": "breakpoint_supported", "brawler": "Colette", "modifier_id": "mass_tax_during_super", "state_id": "body", "stat": "damage_reduction", "old": 0.75, "new": 0.60, "active_when": "正在执行 Super；不与结束后的 30% 状态叠加"},
      {"id": "crow_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Crow", "state_id": "body", "stat": "health", "old": 3000, "new": 2800, "power_level": 1},
      {"id": "crow_one_dagger", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Crow", "packet_id": "main.one_dagger_direct", "old_damage": 320, "new_damage": 420, "power_level": 1, "packet_unit": "dagger_impact", "repeat_model": "identical", "active_when": "一枚匕首直接命中，不含毒 tick、Carrion Crow 与全三枚命中假设"},
      {"id": "crow_poison_duration", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Crow", "reason": "4->3 tick 且重复命中只刷新毒，不适用简单重复包除法"},
      {"id": "crow_hyper_return_multiplier", "type": "other", "change_class": "source_conflict", "brawler": "Crow", "reason": "patch 记 -30%->-40%，当前英雄 raw 仍写 30% less"},
      {"id": "leon_lollipop_health", "type": "other", "change_class": "non_breakpoint", "brawler": "Leon", "reason": "1500->1000 属于 deployable durability，不进入英雄数量分母"},
      {"id": "chester_candy_popper", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Chester", "packet_id": "super.candy_popper_explosion", "old_damage": 1880, "new_damage": 1600, "power_level": 1, "packet_unit": "explosion", "repeat_model": "resource_gated", "active_when": "随机抽到 Candy Popper 并命中"},
      {"id": "chester_candy_beans_multiplier", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Chester", "reason": "25%->20% 是随机四选一临时伤害倍率，不能当常驻包"},
      {"id": "mina_attack_three", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Mina", "reason": "2000->1800 只影响三段连招第三段，必须按有序 cycle 模拟"},
      {"id": "najia_hyper_snake_health", "type": "other", "change_class": "non_breakpoint", "brawler": "Najia", "reason": "2000->1500 属于 summon durability，不进入英雄数量分母"},
      {"id": "bolt_max_speed_damage", "type": "other", "change_class": "source_conflict", "brawler": "Bolt", "reason": "patch after 为 760，当前 2026-07-17 Fandom raw 为 740"},
      {"id": "bolt_super_tick", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Bolt", "reason": "550->700 为持续火道 tick；需驻留时间轴，不能用简单 shots-to-kill"},
      {"id": "spike_one_spike", "type": "other", "change_class": "source_conflict", "brawler": "Spike", "reason": "patch after 为 560，当前 2026-07-17 Fandom raw 为 540；且实际命中根数取决于角度/体型"},
      {"id": "griff_coin_shower", "type": "other", "change_class": "source_conflict", "brawler": "Griff", "reason": "patch/prose 支持 300 基准，当前 infobox 为 320；持续 6 秒需时间轴"},
      {"id": "damian_speaker", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Damian", "packet_id": "super.speaker_inner_collision", "old_damage": 600, "new_damage": 800, "power_level": 1, "packet_unit": "collision", "repeat_model": "one_off", "active_when": "目标从圈内碰到 speaker；speaker 随后破碎"},
      {"id": "damian_hyper_fire", "type": "other", "change_class": "temporal_survival_excluded", "brawler": "Damian", "reason": "400->600 为最多 3 tick 的 Hypercharge 火区，需要驻留时间轴"}
    ]
  }
}
```

## 关键内容

- 新英雄预告：`Nori`、`Wendy`。截至 2026-07-11，`Nori` 已于 7 月 9 日开放 Training Cave 与早期解锁并补齐 [[sources/Fandom-Nori|Fandom direct source]]；`Wendy` 仍为 future-only，见 [[sources/Fandom-Wendy|Fandom future page]] 与 [[sources/Supercell-Wendy-Announcement-June-2026|Supercell announcement]]。发布状态以 [[sources/Brawler-Roster|Brawler Roster]] 为准。
- 新 Buffies / rework：`Rico`、`Brock`、`8-Bit`、`Meg`、`Max`、`Surge`。
- 普通平衡变化：`Piper`、`Mandy`、`Gale`、`Tara`、`Shelly`、`Dynamike`、`Larry & Lawrie`、`Sprout`、`Barley`、`Juju`、`Gray`、`Starr Nova`、`Buzz`、`Lou`、`Carl`、`Pearl`、`R-T` 等加强；`Mortis`、`Colette`、`Crow`、`Leon`、`Chester`、`Edgar`、`Mina`、`Ruffs`、`Meeple`、`Shade`、`Lumi`、`Najia`、`Pierce`、`Bolt` 等削弱；`Spike`、`Griff`、`Damian` 有 mixed changes。
- `Brawl Arena Only` 变化单独标注；默认不进入 Ranked BP 结论。

## 本地 ingest 结果

- 版本 BP 影响评估：[[syntheses/2026-06-30版本BP影响评估|2026-06-30 版本 BP 影响评估]]
- 只有产生定性 BP 影响的条目才允许直接更新对应英雄页或地图页的稳定 BP 字段；运行时索引由 compile 重新生成。本次先标记需要逐页复核的候选主体：`Rico`、`Brock`、`8-Bit`、`Meg`、`Max`、`Surge`、`Bolt`、`Damian`、`Spike`。
- `Meeple`、`Colette`、`Crow`、`Mortis`、`Edgar`、`Chester`、`R-T`、`Griff`、`Leon`、`Lumi`、`Najia`、`Pierce`、`Mina` 等变化目前只保留为版本审计或观察材料；尚未证明会改变常见高水平 BP 的定性判断。
- BP 运行时默认读取稳定 BP 页面，不临场叠加本来源。

## 关联页面

- [[sources/Brawler-Roster|Brawler Roster]]
- [[sources/Fandom-Nori|Fandom 来源摘要: Nori]]
- [[sources/Fandom-Wendy|Fandom 来源摘要: Wendy]]
- [[sources/Supercell-Wendy-Announcement-June-2026|Supercell 来源摘要: Wendy Announcement]]
- [[sources/Fandom-Maintenance-July-8-2026|Fandom 来源摘要: Maintenance - July 8, 2026]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/2026-06-30版本BP影响评估|2026-06-30 版本 BP 影响评估]]
