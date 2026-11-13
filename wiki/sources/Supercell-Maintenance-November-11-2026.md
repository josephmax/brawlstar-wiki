# Supercell：2026 年 11 月 11 日维护

- [官方公告](https://supercell.com/brawlstars/en/blog/game-updates/release-notes-november-2026/)：11 月 11 日追加在 11 月 3 日发行说明顶部；[11 月 13 日完整网页快照](../../raw/sources/supercell/maintenance-november-11-2026-11-13.html)。
- 前一期独立账本：[[Supercell-Release-Notes-November-2026]]。仅适用于本期排位机制与数值，不是胜率或选禁优先级。
- Wendy 的护盾是命中后回复，不与直击伤害合算。Amber 的公告标量是每秒伤害：前后个人页每秒 2100→1800、单火苗 210→180（PL1），不可将一次普攻当成一整秒全中。
- Gale 个人页风墙引语/正文与官方冷却、弹速有旧值交叉；采用官方 26 秒 / 20%，不以旧引语加码。预发布角色只记录官方行，不推定排位资格。

## 断点账本

PL11，满 Shield gear +900。对 108 名英雄、258 种防御状态比较两种独立攻击包；504 条命中数变化、179 条配装压力变化。Wendy 裸身目标中有 18 个由三发变四发，51 个由四发变五发。Amber 的次数单位是单枚火苗，不是弹仓或持续输出秒数。自盾比例从 30% 到 38% 不等于自盾绝对值增加八个百分点；个人页引语写 604，不能用公告取整百分比推断精确盾值。

全库逐英雄结构和对位归属清点：108 页中 107 份 BP-ready，Vince 仅有机制页；430 条条件对位展开为 1795 个目标引用，未知目标与缺必填字段均为 0。11 组重复方向、5 组同一主体下双向记录是复核线索，不代表已逐边裁定；未从断点自动改对位方向。11 月 3 日的 34 份历史处置仍未结清，与本期账本分开。

```json
{
  "balance_patch_manifest": {
    "schema": "balance_breakpoint_manifest.v1",
    "patch_id": "2026-11-11-maintenance",
    "effective_order": 7,
    "effective_at": "2026-11-11",
    "scope": [
      "ranked",
      "power_level_11_normalized"
    ],
    "source_refs": [
      "[[Supercell-Maintenance-November-11-2026]]"
    ],
    "changes": [
      {
        "id": "vince_0",
        "brawler": "Vince",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Hypercharged Super: Pet health decay increased by 30%",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "vince_1",
        "brawler": "Vince",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Hypercharged Super: Caterpillars spawned reduced from 6 → 4",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "chester_0",
        "brawler": "Chester",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Prankster’s Surprise Gadget: Box health reduced from 2250 → 1800",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "chester_1",
        "brawler": "Chester",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Buffied Hypercharged Main Attack: Super charge gained from projectiles reduced by 35% (matching the damage reduction)",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "lou_0",
        "brawler": "Lou",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Avalanche Gadget: Freeze application reduced from 50% → 40%",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "gale_0",
        "brawler": "Gale",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "North Wind Wall Gadget: Cooldown increased from 22 → 26 seconds",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "gale_1",
        "brawler": "Gale",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "North Wind Wall Gadget: Projectile redirection reduced from 30% → 20%",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "gale_2",
        "brawler": "Gale",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Buffied North Wind Wall Gadget: Projectile speed boost reduced from 30% → 20%",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "mr_p_0",
        "brawler": "Mr. P",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Porter Reinforcements Gadget now consumes ammo",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "mr_p_1",
        "brawler": "Mr. P",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Porter Reinforcements Gadget: Cooldown increased from 22 → 26 seconds",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "wendy_0",
        "brawler": "Wendy",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "packet_id": "main.impact",
        "old_damage": 1000,
        "new_damage": 800,
        "power_level": 1,
        "packet_unit": "blast_impact",
        "repeat_model": "identical",
        "active_when": "单发直击同一目标，不含队友盾与回盾"
      },
      {
        "id": "wendy_1",
        "brawler": "Wendy",
        "type": "other",
        "change_class": "temporal_survival_excluded",
        "label": "Shield gained from hitting enemies increased from 30% → 38% of Main Attack damage",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "amber_0",
        "brawler": "Amber",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "packet_id": "main.single_flame",
        "old_damage": 210,
        "new_damage": 180,
        "power_level": 1,
        "packet_unit": "flame",
        "repeat_model": "identical",
        "active_when": "每枚独立火苗命中；可能跨弹仓，不表示秒杀时间或持续全中"
      },
      {
        "id": "amber_1",
        "brawler": "Amber",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Super charge gained from her Super reduced from 53 → 40",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "mandy_0",
        "brawler": "Mandy",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Buffied Cookie Crumbs Gadget: Cooldown refund reduced from 50% → 30%",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "mandy_1",
        "brawler": "Mandy",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Cookie Crumbs Gadget now correctly grants Super charge",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "mandy_2",
        "brawler": "Mandy",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Caramelize Gadget: Maximum slow changed from a flat 350 → 25%; minimum slow changed from a flat 70 → 10%",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "mandy_3",
        "brawler": "Mandy",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Buffied Caramelize Gadget: Maximum speed boost changed from a flat 350 → 25%; minimum speed boost changed from a flat 70 → 10%",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      },
      {
        "id": "mandy_4",
        "brawler": "Mandy",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "label": "Caramelize Gadget now correctly grants Super charge.",
        "reason": "冷却、资源、召唤物、控制或时序效果，不能建模为重复英雄伤害包。"
      }
    ]
  }
}
```

## 逐英雄处置

```json
{
  "version_fold_ledger": {
    "schema": "brawlstar.version_fold_ledger.v1",
    "patch_id": "2026-11-11-maintenance",
    "effective_at": "2026-11-11",
    "official_source": "https://supercell.com/brawlstars/en/blog/game-updates/release-notes-november-2026/",
    "raw": "raw/sources/supercell/maintenance-november-11-2026-11-13.html",
    "upstream": {
      "fandom_version_history_revision": 222450
    },
    "brawlers": [
      {
        "brawler": "Vince",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Hypercharged Super: Pet health decay increased by 30%",
          "Hypercharged Super: Caterpillars spawned reduced from 6 → 4"
        ],
        "fold": "numbers_only",
        "note": "超充生成 4 只，宠物掉血加快；仅更新机制，不能据此开放顺位。"
      },
      {
        "brawler": "Chester",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Prankster’s Surprise Gadget: Box health reduced from 2250 → 1800",
          "Buffied Hypercharged Main Attack: Super charge gained from projectiles reduced by 35% (matching the damage reduction)"
        ],
        "fold": "model_changed",
        "note": "盒子是独立可破坏物；按放置时机和充能资源判断，不计为本体护盾。"
      },
      {
        "brawler": "Lou",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Avalanche Gadget: Freeze application reduced from 50% → 40%"
        ],
        "fold": "model_changed",
        "note": "Avalanche 为需弹药且需落点命中的 40% 冰冻量，不是敌人在冰面中就能瞬冻。"
      },
      {
        "brawler": "Gale",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "North Wind Wall Gadget: Cooldown increased from 22 → 26 seconds",
          "North Wind Wall Gadget: Projectile redirection reduced from 30% → 20%",
          "Buffied North Wind Wall Gadget: Projectile speed boost reduced from 30% → 20%"
        ],
        "fold": "model_changed",
        "note": "风墙不能载人越墙；26 秒冷却，偏转与芭菲加速各 20%，侧面射线不受正面墙保护。"
      },
      {
        "brawler": "Mr. P",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Porter Reinforcements Gadget now consumes ammo",
          "Porter Reinforcements Gadget: Cooldown increased from 22 → 26 seconds"
        ],
        "fold": "model_changed",
        "note": "增援消耗一格弹药，26 秒冷却；对手清掉小兵后不再假设有免费补压。"
      },
      {
        "brawler": "Wendy",
        "kinds": [
          "balance"
        ],
        "direction": "mixed",
        "rows": [
          "Main Attack: Damage reduced from 1000 → 800",
          "Shield gained from hitting enemies increased from 30% → 38% of Main Attack damage"
        ],
        "fold": "model_changed",
        "note": "直击 PL11 2000→1600；命中敌方自盾比例 30%→38%，非永久血量。"
      },
      {
        "brawler": "Amber",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Main Attack: Damage reduced from 2100 → 1800",
          "Super charge gained from her Super reduced from 53 → 40"
        ],
        "fold": "model_changed",
        "note": "单火苗 PL11 420→360，而非每枚 4200→3600；耗弹、追踪和油区回充分别处理。"
      },
      {
        "brawler": "Mandy",
        "kinds": [
          "balance"
        ],
        "direction": "mixed",
        "rows": [
          "Buffied Cookie Crumbs Gadget: Cooldown refund reduced from 50% → 30%",
          "Cookie Crumbs Gadget now correctly grants Super charge",
          "Caramelize Gadget: Maximum slow changed from a flat 350 → 25%; minimum slow changed from a flat 70 → 10%",
          "Buffied Caramelize Gadget: Maximum speed boost changed from a flat 350 → 25%; minimum speed boost changed from a flat 70 → 10%",
          "Caramelize Gadget now correctly grants Super charge.",
          "Mandy: Fixed Cookie Crumbs not granting Super charge on hit. It now charges her Super as intended."
        ],
        "fold": "model_changed",
        "note": "减速与自身增速改为距离相关百分比；饼干芭菲返冷 30%，两种妙具可充能。"
      },
      {
        "brawler": "Berry",
        "kinds": [
          "bug_fix"
        ],
        "direction": "adjust",
        "rows": [
          "Berry: Fixed an issue where his Super dash only healed one teammate when multiple teammates were standing close together. It now heals all nearby teammates again"
        ],
        "fold": "model_changed",
        "note": "冲刺经过聚集队友时可治疗多人，不是单目标治疗。"
      },
      {
        "brawler": "Buzz",
        "kinds": [
          "bug_fix"
        ],
        "direction": "adjust",
        "rows": [
          "Buzz: Fixed Reserve Buoy not stunning enemies after landing when activated during a regular Super dash. It now stuns as intended, while the next Gadget-charged Super will not",
          "Buzz: Fixed his Super stun incorrectly affecting other Brawlers during their own Super dashes, causing extended stuns or canceling their Supers (such as Berry, Colette, and Carl)"
        ],
        "fold": "model_changed",
        "note": "保留常规冲刺眩晕，区分妙具补充的下次 Super，不假设打断敌方 Super 冲刺。"
      },
      {
        "brawler": "Cordelius",
        "kinds": [
          "bug_fix"
        ],
        "direction": "adjust",
        "rows": [
          "Cordelius: Fixed Meg, Moe, and Draco leaving the Shadow Realm prematurely when their transformations ended, leaving Cordelius alone inside. They’ll now remain in the Shadow Realm as expected"
        ],
        "fold": "model_changed",
        "note": "变身结束不使 Meg、Moe、Draco 提前离开暗影领域。"
      },
      {
        "brawler": "Emz",
        "kinds": [
          "bug_fix"
        ],
        "direction": "adjust",
        "rows": [
          "Emz: Fixed her Hypercharged Super stunning enemies positioned against a wall. It will no longer unintentionally stun!"
        ],
        "fold": "model_changed",
        "note": "超充 Super 将人顶墙不附加眩晕；区分妙具效果。"
      }
    ],
    "environment": [
      {
        "id": "Thunder_Frogs",
        "kind": "new_brawler",
        "status": "deferred",
        "rows": [
          "Main Attack: Middle damage reduced from 1050 → 900",
          "Soothing Shock Gadget: Healing reduced from 2000 → 1500",
          "Leech Landing Star Power: Healing reduced from 75% → 50%"
        ],
        "note": "预发布调整已归档；待 roster 身份、发布状态与排位资格核实后建模。"
      },
      {
        "id": "Rey",
        "kind": "new_brawler",
        "status": "deferred",
        "rows": [
          "Queen’s Gambit Gadget: Cooldown increased from 15 → 18 seconds"
        ],
        "note": "预发布调整已归档；待 roster 身份、发布状态与排位资格核实后建模。"
      }
    ],
    "bug_fixes": [
      "Berry: Fixed an issue where his Super dash only healed one teammate when multiple teammates were standing close together. It now heals all nearby teammates again",
      "Mandy: Fixed Cookie Crumbs not granting Super charge on hit. It now charges her Super as intended.",
      "Buzz: Fixed Reserve Buoy not stunning enemies after landing when activated during a regular Super dash. It now stuns as intended, while the next Gadget-charged Super will not",
      "Buzz: Fixed his Super stun incorrectly affecting other Brawlers during their own Super dashes, causing extended stuns or canceling their Supers (such as Berry, Colette, and Carl)",
      "Cordelius: Fixed Meg, Moe, and Draco leaving the Shadow Realm prematurely when their transformations ended, leaving Cordelius alone inside. They’ll now remain in the Shadow Realm as expected",
      "Emz: Fixed her Hypercharged Super stunning enemies positioned against a wall. It will no longer unintentionally stun!"
    ],
    "excluded": []
  }
}
```
