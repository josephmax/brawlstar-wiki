# Supercell 来源摘要：Maintenance - August 4, 2026

## 来源信息

- 标题：Release Notes June 2026 - Maintenance - August 4
- 官方来源：[Supercell Release Notes June 2026（顶部 August 4 maintenance）](https://supercell.com/en/games/brawlstars/blog/release-notes/release-notes-june-2026/)
- 页面显示更新日期：2026-08-03
- 生效日期：2026-08-04
- 读取日期：2026-08-10
- 上游 raw：[[../../raw/sources/supercell/maintenance-august-4-2026-2026-08-10|maintenance-august-4-2026-2026-08-10]]
- source_quality：official_direct_capture
- source_type：maintenance / balance_changes / nanopower_balance / bug_fixes

## 可用范围

- usable_for: canonical_patch_ledger, affected_brawler_index, current_mechanics_refresh, breakpoint_manifest, build_resource_delta, event_power_delta
- not_usable_for: long_term_meta_strength, unconditional_counter_claim, direct_pick_priority, NanoPower_changes_as_base_ranked_mechanics

## 变更范围

- 常规调整共 8 位英雄：`Crow`、`Griff`、`Starr Nova`、`Damian`、`Max`、`Bolt`、`8-Bit`、`Surge`，全部为削弱。
- NanoPower 调整涉及 22 位英雄、23 项活动能力变化；这些变化只保留在来源层，不写成普通 Ranked 基础机制。
- 受影响的 8 位常规英雄已刷新 2026-08-10 Fandom direct raw 和 canonical Fandom source summary，用来核对当前机制。

## 断点审计 Manifest

```json
{
  "balance_patch_manifest": {
    "schema": "balance_breakpoint_manifest.v1",
    "patch_id": "2026-08-04-maintenance",
    "effective_order": 3,
    "effective_at": "2026-08-04",
    "scope": ["ranked", "power_level_11_normalized", "nanopower_event_excluded"],
    "source_refs": ["[[sources/Supercell-Maintenance-August-4-2026|Maintenance - August 4, 2026]]"],
    "changes": [
      {"id":"crow_one_dagger","type":"damage_packet","change_class":"breakpoint_supported","brawler":"Crow","packet_id":"main.one_dagger_direct","old_damage":380,"new_damage":320,"power_level":1,"packet_unit":"dagger_impact","repeat_model":"identical","active_when":"一枚匕首直接命中；不含毒 tick、Carrion Crow、Hypercharge return 或三枚全中假设"},
      {"id":"crow_slowing_toxin_damage","type":"other","change_class":"source_conflict","brawler":"Crow","reason":"官方写 800->600，但 2026-08-10 Fandom structured fields 为 direct 960 + poison 160，数值语义/Power Level 未闭合，暂不建立 scalar packet"},
      {"id":"griff_piggy_bank_radius","type":"other","change_class":"non_breakpoint","brawler":"Griff","reason":"爆炸半径与 Buffie 半径倍率改变地形/命中可靠性，不是伤害—生存标量"},
      {"id":"griff_keep_the_change_spread","type":"other","change_class":"non_breakpoint","brawler":"Griff","reason":"散布变化影响命中完整度，不进入静态 packet 除法"},
      {"id":"starr_nova_body_health","type":"target_state","change_class":"breakpoint_supported","brawler":"Starr Nova","state_id":"body","stat":"health","old":4000,"new":3700,"power_level":1},
      {"id":"starr_nova_reload","type":"other","change_class":"non_breakpoint","brawler":"Starr Nova","reason":"reload 1400->1600 是时间轴输出变化"},
      {"id":"starr_nova_floaty_decay","type":"other","change_class":"temporal_survival_excluded","brawler":"Starr Nova","reason":"Floaty Time 的衰减率与 10s->7s 时长需要时间轴/晶体状态模型"},
      {"id":"starr_nova_power_level_maximum","type":"other","change_class":"unsupported_mechanic","brawler":"Starr Nova","reason":"每次命中叠层 5%->4%、上限 30%->20% 需要顺序与资源状态模型"},
      {"id":"damian_fire_punch","type":"damage_packet","change_class":"breakpoint_supported","brawler":"Damian","packet_id":"main.fire_punch","old_damage":1000,"new_damage":800,"power_level":1,"packet_unit":"empowered_punch_impact","repeat_model":"resource_gated","active_when":"强化攻击已充满并直接命中；不含后续 explosion"},
      {"id":"damian_chain_explosion","type":"damage_packet","change_class":"breakpoint_supported","brawler":"Damian","packet_id":"main.explosion","old_damage":1000,"new_damage":800,"power_level":11,"packet_unit":"explosion_impact","repeat_model":"resource_gated","active_when":"强化攻击标记后爆炸命中；官方值按 Power 11 记账，与当前 Fandom P1 400 对齐"},
      {"id":"damian_speaker_bounce","type":"damage_packet","change_class":"breakpoint_supported","brawler":"Damian","packet_id":"super.speaker_inner_collision","old_damage":800,"new_damage":400,"power_level":1,"packet_unit":"collision","repeat_model":"one_off","active_when":"目标从 Mosh Pit 内侧触发单个 speaker，speaker 随后破碎"},
      {"id":"damian_speaker_health","type":"other","change_class":"unsupported_mechanic","brawler":"Damian","reason":"2000->1500 属于 temporary spawnable health，不进入 brawler roster target denominator"},
      {"id":"max_phase_shifter_window","type":"other","change_class":"non_breakpoint","brawler":"Max","reason":"第二段 dash 窗口 3s->2s 是时机/位移资源变化"},
      {"id":"max_super_charge_rate","type":"other","change_class":"non_breakpoint","brawler":"Max","reason":"opaque charge-rate unit 92->80，不等同离散伤害包"},
      {"id":"bolt_overdrive_reduction","type":"defense_modifier","change_class":"breakpoint_supported","brawler":"Bolt","modifier_id":"overdrive_damage_reduction","state_id":"body","stat":"damage_reduction","old_ratio":0.40,"new_ratio":0.30,"active_when":"Bolt 的 4 秒 Overdrive Super 生效"},
      {"id":"bolt_trait_super_charge","type":"other","change_class":"non_breakpoint","brawler":"Bolt","reason":"移动充 Super 减少 23% 是资源时间变化"},
      {"id":"8bit_super_charge_rate","type":"other","change_class":"non_breakpoint","brawler":"8-Bit","reason":"opaque charge-rate unit 99->80，不等同离散伤害包"},
      {"id":"8bit_extra_credits_cooldown","type":"other","change_class":"non_breakpoint","brawler":"8-Bit","reason":"Gadget cooldown 15s->18s 是资源频率变化"},
      {"id":"8bit_plugged_in_ally_speed","type":"other","change_class":"non_breakpoint","brawler":"8-Bit","reason":"Buffied ally speed 15%->10% 是移动/团队资源变化"},
      {"id":"surge_unload_time","type":"other","change_class":"non_breakpoint","brawler":"Surge","reason":"main attack unload 400->470 是时间与命中完整度变化"},
      {"id":"surge_power_shield_ammo","type":"other","change_class":"non_breakpoint","brawler":"Surge","reason":"Power Shield reload 2->1 ammo 是构筑资源变化"},
      {"id":"nanopower_balance_set","type":"other","change_class":"unsupported_mechanic","reason":"23 项 NanoPower 变化均属于限时活动能力；包含条件化 summon HP、临时最大生命、范围、充能、冷却和治疗，不能提升为普通 Ranked 基础机制或简单 EHP"}
    ]
  }
}
```

## 稳定层更新

- `Crow`：当前单枚普通匕首为 P1 `320`；主攻击仍承担 poison tag / anti-heal / reveal，但 raw burst 与斩杀余量下降。
- `Griff`：Piggy Bank 基础爆炸半径缩小，Buffie 的 bonus radius 提高到 30%；稳定 BP 语义改为更依赖贴准关键墙位。`Keep the Change` 散布进一步变宽，仍偏近身/固定目标，而不是长线命中修复。
- `Starr Nova`：当前 P1 生命 `3700`、装填 `1.6s`；`Floaty Time` 最长 7 秒；`Power Level: Maximum!` 每层 4%、最高 20%。
- `Damian`：强化拳当前 P1 `800`；爆炸当前 P1 `400`（P11 `800`）；speaker bounce 当前 P1 `400`；speaker health `1500`。能力类型没有消失，但跳入后的伤害与边界耐久下降。
- `Max`：Buffied Phase Shifter 第二段窗口为 2 秒；Super 循环变慢，但速度支援能力类型未变。
- `Bolt`：官方把 Overdrive 减伤改为 30%，移动充 Super 也下降；当前 Fandom 说明段仍写 40%，以官方 ledger 更新稳定事实并保留来源冲突。
- `8-Bit`：Extra Credits cooldown 18 秒；Buffied Plugged In 队友加速 10%；Super 循环变慢。
- `Surge`：普通攻击卸弹更慢，Power Shield 只回 1 ammo；反近身能力仍在，但三发后的资源回补显著收紧。

## 来源冲突与排除

- `Crow`：官方 `Slowing Toxin 800 -> 600` 与当前 Fandom structured fields 的 `direct 960 + poison 160` 不能直接对齐；暂不写入 damage packet。
- `Bolt`：Fandom 2026-08-10 capture 的说明段仍写 40% Overdrive damage reduction，官方明确是 30%。
- `Damian`：当前 Fandom Super quote 仍写 speaker 800 damage，但 infobox `Super=400` 与官方 `800 -> 400` 对齐；稳定 profile 使用 400，并保留 quote stale 记录。
- NanoPower 调整不进入普通 Ranked runtime；Tara Shadow health、Frank HP buff、Sirius Shadow health 等也不进入 roster brawler denominator。

## 关联页面

- [[sources/Fandom-Crow|Fandom 来源摘要: Crow]]
- [[sources/Fandom-Griff|Fandom 来源摘要: Griff]]
- [[sources/Fandom-Starr-Nova|Fandom 来源摘要: Starr Nova]]
- [[sources/Fandom-Damian|Fandom 来源摘要: Damian]]
- [[sources/Fandom-Max|Fandom 来源摘要: Max]]
- [[sources/Fandom-Bolt|Fandom 来源摘要: Bolt]]
- [[sources/Fandom-8-Bit|Fandom 来源摘要: 8-Bit]]
- [[sources/Fandom-Surge|Fandom 来源摘要: Surge]]
- [[concepts/伤害与生存断点|伤害与生存断点]]
