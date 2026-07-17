# Fandom 来源摘要: Maintenance - July 8, 2026

## 来源信息

- 标题：Version History/2026 - Maintenance - July 8
- Fandom 来源：[Version History/2026](https://brawlstars.fandom.com/wiki/Version_History/2026)
- 官方交叉核验：[Supercell Release Notes June 2026（顶部 July 8 maintenance）](https://supercell.com/en/games/brawlstars/blog/release-notes/release-notes-june-2026/)
- 读取日期：2026-07-10
- 上游 raw：[[../../raw/sources/fandom/systems/maintenance-july-8-2026-2026-07-10|maintenance-july-8-2026-2026-07-10]]
- source_quality：direct_raw_capture_with_official_cross_check
- source_type：maintenance / balance_changes / bug_fixes

## 可用范围

- usable_for: affected_brawler_index, current_mechanics_refresh, build_resource_delta, breakpoint_watchlist, bugfix_revalidation
- not_usable_for: long_term_meta_strength, unconditional_counter_claim, direct_pick_priority, unresolved_conflicting_labels

## 平衡调整范围

- Buff：`Jacky`、`Bonnie`、`Jessie`。
- Nerf：`8-Bit`、`Surge`、`Brock`、`Meg`、`Crow`、`Colette`、`Starr Nova`、`Max`。
- 已按维护 skill 补抓并刷新上述 11 位英雄的 2026-07-10 Fandom direct raw 与 canonical Fandom source summary。

## 断点审计 Manifest

```json
{
  "balance_patch_manifest": {
    "schema": "balance_breakpoint_manifest.v1",
    "patch_id": "2026-07-08-maintenance",
    "effective_order": 2,
    "effective_at": "2026-07-08",
    "scope": ["ranked", "power_level_11_normalized"],
    "source_refs": ["[[sources/Fandom-Maintenance-July-8-2026|Maintenance - July 8, 2026]]"],
    "changes": [
      {"id": "jacky_body_health", "type": "target_state", "change_class": "breakpoint_supported", "brawler": "Jacky", "state_id": "body", "stat": "health", "old": 5000, "new": 5200, "power_level": 1},
      {"id": "bonnie_clyde_main", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Bonnie", "packet_id": "main.clyde_impact", "old_damage": 1120, "new_damage": 1220, "power_level": 1, "packet_unit": "impact", "repeat_model": "identical", "active_when": "Clyde 形态单发命中；Bonnie 形态三枚 grenade 未改"},
      {"id": "8bit_extra_credits_bounce", "type": "other", "change_class": "unsupported_mechanic", "brawler": "8-Bit", "reason": "75%->60% 是后续目标弹射倍率，不是首目标固定伤害包；需 18 beam 与目标链模型"},
      {"id": "surge_buffied_hyper_second_shot", "type": "other", "change_class": "unsupported_mechanic", "brawler": "Surge", "reason": "70%->50% 是 Hypercharge+Buffie 第二发相对倍率，需与当前第一发和弹道组合"},
      {"id": "surge_hyper_radial_projectile", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Surge", "packet_id": "hyper.super_radial_projectile", "old_damage": 1000, "new_damage": 800, "power_level": 1, "packet_unit": "projectile_impact", "repeat_model": "one_off", "active_when": "Hypercharge Super 落地的单枚径向 projectile 命中"},
      {"id": "crow_one_dagger", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Crow", "packet_id": "main.one_dagger_direct", "old_damage": 420, "new_damage": 380, "power_level": 1, "packet_unit": "dagger_impact", "repeat_model": "identical", "active_when": "一枚匕首直接命中，不含毒 tick、Carrion Crow 与全三枚命中假设"},
      {"id": "starr_nova_main_projectile", "type": "damage_packet", "change_class": "breakpoint_supported", "brawler": "Starr Nova", "packet_id": "main.one_projectile", "old_damage": 540, "new_damage": 480, "power_level": 1, "packet_unit": "projectile_impact", "repeat_model": "identical", "active_when": "普通形态一枚 projectile 命中；每 ammo 两枚，未假设全中"}
    ]
  }
}
```

### 数值断点层，不自动提升为 BP 结论

- `Jacky` 血量、`Bonnie` 普攻伤害、`Crow` 普攻伤害和 `Starr Nova` 普攻伤害进入上方 `balance_breakpoint_manifest.v1`，由断点脚本比较前后离散击杀线；`Jessie` 弹速和充能补偿不属于静态伤害—生存公式。
- 这些条目可以进入当前 `combat_breakpoint_profile` 与生成审计，但不能仅凭跨线自动写成永久 BP 强度、地图适配或无条件对位。

### 需要复核稳定 BP 字段

- `8-Bit`：弹药夹生成从 3 秒变 5 秒，削弱炮台作为团队 ammo resource 的频率；当前 Fandom 页仍确认 Extra Credits 可主动瞄准并与普攻并行、弹跳伤害逐次衰减。
- `Surge`：Power Shield 冷却与 Hypercharge 范围/伤害被削；当前 Fandom 页确认 Power Surge 已改为临时提高 Super charge rate，Serve Ice Cold 为开局自带 Super，旧“临时升阶”描述已过时。
- `Brock`：Rocket No. 4 Buffie 的额外射程等待变长；当前 Fandom 页仍确认 Rocket Laces 可瞄准、双端击退/伤害，Rocket Fuel 负责定点开墙。补丁的 Gadget 命名不一致，不能据此删除稳定击退机制。
- `Meg`：Toolbox 回机甲时间变长，Jolting Volts 额外治疗时长缩短，机甲 Super 循环减慢；这些改变资源窗口，不取消团队治疗、进机甲范围压迫或 ammo steal 等能力类型。
- `Colette`：官方索引把 0.5 秒 charm 标为 `Gotcha!`，当前 Fandom 页则明确放在 `Na-ah!`；稳定层只能采用当前机制页并保留冲突，不复制错误标签。
- `Max`：Hyper Buffie 的每次命中团队充 Super 从 8% 变 7%；能力类型仍是 team tempo / shield / Super-resource support，但资源效率下降。

## Bug Fix 影响边界

- `Rico`、`Sirius`、`Starr Nova` 的修复会改变特定资源循环或复制体阈值，后续应结合各自当前 Fandom 页复核。
- `Mortis`、`Crow`、`Byron` 是伤害计算纠正，默认先放版本观察，不自动翻转 matchup。
- `Larry & Lawrie`、`Jacky` / `Sprout`、`Emz` 的项目依赖 Nano 活动；不能写成普通 Ranked 基础机制。

## 已确认的来源冲突

- `Colette`：官方维护索引写 `Gotcha!`，Fandom 当前页写 `Na-ah!`。
- `Brock`：官方维护索引写不存在的 `Rocket Barrage Gadget`；当前页的 Gadget 为 Rocket Laces / Rocket Fuel，Rocket Barrage 是 Hypercharge。
- `Starr Nova`：官方说明仍需 10 hits；Fandom History 出现 10 -> 12 hits 的冲突记录。
- `Surge`：个体 History 漏记三项 Hypercharge nerf。
- `Meg`：个体 History 以 hit count / 99% 表述部分变化，官方索引未逐字确认。

## 关联页面

- [[sources/Fandom-8-Bit|Fandom 来源摘要: 8-Bit]]
- [[sources/Fandom-Surge|Fandom 来源摘要: Surge]]
- [[sources/Fandom-Brock|Fandom 来源摘要: Brock]]
- [[sources/Fandom-Meg|Fandom 来源摘要: Meg]]
- [[sources/Fandom-Colette|Fandom 来源摘要: Colette]]
- [[sources/Fandom-Max|Fandom 来源摘要: Max]]
- [[sources/Brawler-Roster|Brawler Roster]]
