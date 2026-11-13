# Supercell 来源摘要：2026 年 11 月更新

- 来源：[Supercell 官方更新说明](https://supercell.com/en/games/brawlstars/blog/game-updates/release-notes-november-2026/)；2026-11-03 发布，2026-11-04 抓取。
- 官方完整 raw：[[../../raw/sources/supercell/release-notes-november-2026-2026-11-04.html|官方原始页面]]；受影响英雄 Fandom 和 PLP 双源于 11 月 4 日采集。
- usable_for：版本数值、断点账本；not_usable_for：实测胜率、强度榜、无条件 BP 结论。
- Fandom 资料可能滞后，个别描述与 infobox 不一致；Draco 官方 Super 标量与逐弹/距离模型不能直接对应。

## balance_patch_manifest

```json
{
  "balance_patch_manifest": {
    "schema": "balance_breakpoint_manifest.v1",
    "patch_id": "2026-11-03-release",
    "effective_order": 6,
    "effective_at": "2026-11-03",
    "scope": [
      "ranked",
      "power_level_11_normalized"
    ],
    "source_refs": [
      "[[sources/Supercell-Release-Notes-November-2026]]"
    ],
    "notes": [
      "Official 3 November release notes; patch values P1; 11-level normalization x2. No Brawl Arena scaling.",
      "One-off and resource-gated packets are one-packet threshold comparisons, never repeated-shot claims.",
      "Draco 1120→1620 is official, but Fandom delivery is variable 81 per projectile; excluded pending equivalence."
    ],
    "changes": [
      {
        "id": "hank_body_health",
        "type": "target_state",
        "change_class": "breakpoint_supported",
        "brawler": "Hank",
        "state_id": "body",
        "stat": "health",
        "old": 5500,
        "new": 6000,
        "power_level": 1,
        "active_when": "body health"
      },
      {
        "id": "shade_body_health",
        "type": "target_state",
        "change_class": "breakpoint_supported",
        "brawler": "Shade",
        "state_id": "body",
        "stat": "health",
        "old": 3700,
        "new": 3400,
        "power_level": 1,
        "active_when": "body health"
      },
      {
        "id": "cosmo_body_health",
        "type": "target_state",
        "change_class": "breakpoint_supported",
        "brawler": "Cosmo",
        "state_id": "body",
        "stat": "health",
        "old": 3400,
        "new": 3600,
        "power_level": 1,
        "active_when": "body health"
      },
      {
        "id": "shelly_main_full_connect",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Shelly",
        "packet_id": "main.full_connect",
        "old_damage": 1500,
        "new_damage": 1700,
        "power_level": 1,
        "packet_unit": "main.full_connect",
        "repeat_model": "identical",
        "active_when": "5 shells of one main attack all hit"
      },
      {
        "id": "shelly_super_full_connect",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Shelly",
        "packet_id": "super.full_connect",
        "old_damage": 2880,
        "new_damage": 3240,
        "power_level": 1,
        "packet_unit": "super.full_connect",
        "repeat_model": "one_off",
        "active_when": "9 shells of one normal Super all hit; excludes Hypercharge"
      },
      {
        "id": "ziggy_main_impact",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Ziggy",
        "packet_id": "main.impact",
        "old_damage": 950,
        "new_damage": 1050,
        "power_level": 1,
        "packet_unit": "main.impact",
        "repeat_model": "identical",
        "active_when": "direct hit without Great Ziggini bonus"
      },
      {
        "id": "melodie_main_impact",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Melodie",
        "packet_id": "main.impact",
        "old_damage": 460,
        "new_damage": 500,
        "power_level": 1,
        "packet_unit": "main.impact",
        "repeat_model": "identical",
        "active_when": "direct projectile; orbiting notes excluded"
      },
      {
        "id": "melodie_main_orbit_note",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Melodie",
        "packet_id": "main.orbit_note",
        "old_damage": 920,
        "new_damage": 1000,
        "power_level": 1,
        "packet_unit": "main.orbit_note",
        "repeat_model": "resource_gated",
        "active_when": "one orbiting note contact; requires note; no repeated-count claim"
      },
      {
        "id": "maisie_main_impact",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Maisie",
        "packet_id": "main.impact",
        "old_damage": 1500,
        "new_damage": 1360,
        "power_level": 1,
        "packet_unit": "main.impact",
        "repeat_model": "identical",
        "active_when": "one direct hit without Pinpoint Precision"
      },
      {
        "id": "squeak_main_impact",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Squeak",
        "packet_id": "main.impact",
        "old_damage": 1160,
        "new_damage": 1280,
        "power_level": 1,
        "packet_unit": "main.impact",
        "repeat_model": "identical",
        "active_when": "one sticky bomb explosion without Chain Reaction"
      },
      {
        "id": "damian_main_regular_punch",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Damian",
        "packet_id": "main.regular_punch",
        "old_damage": 700,
        "new_damage": 800,
        "power_level": 1,
        "packet_unit": "main.regular_punch",
        "repeat_model": "resource_gated",
        "active_when": "normal punch only; charged punch changes cycle"
      },
      {
        "id": "damian_main_fire_punch",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Damian",
        "packet_id": "main.fire_punch",
        "old_damage": 800,
        "new_damage": 880,
        "power_level": 1,
        "packet_unit": "main.fire_punch",
        "repeat_model": "resource_gated",
        "active_when": "charged direct punch only; excludes delayed explosion"
      },
      {
        "id": "pierce_main_last_ammo",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Pierce",
        "packet_id": "main.last_ammo",
        "old_damage": 1500,
        "new_damage": 1400,
        "power_level": 1,
        "packet_unit": "main.last_ammo",
        "repeat_model": "resource_gated",
        "active_when": "last ammo shot only; requires last-ammo state"
      },
      {
        "id": "gus_gadget_knockback_spirit",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Gus",
        "packet_id": "gadget.knockback_spirit",
        "old_damage": 540,
        "new_damage": 260,
        "power_level": 1,
        "packet_unit": "gadget.knockback_spirit",
        "repeat_model": "resource_gated",
        "active_when": "one spirit explosion triggered by gadget; spirit and cooldown required"
      },
      {
        "id": "darryl_super_impact",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Darryl",
        "packet_id": "super.impact",
        "old_damage": 660,
        "new_damage": 720,
        "power_level": 1,
        "packet_unit": "super.impact",
        "repeat_model": "one_off",
        "active_when": "one Super contact; no repeat assumption"
      },
      {
        "id": "shade_hardened_hoodie",
        "type": "defense_modifier",
        "change_class": "breakpoint_supported",
        "brawler": "Shade",
        "modifier_id": "hardened_hoodie",
        "state_id": "body",
        "stat": "damage_reduction",
        "old": 0.3,
        "new": 0.2,
        "active_when": "Star Power active during Super"
      },
      {
        "id": "draco_dragon_solo",
        "type": "defense_modifier",
        "change_class": "breakpoint_supported",
        "brawler": "Draco",
        "modifier_id": "dragon_solo",
        "state_id": "body",
        "stat": "damage_reduction",
        "old": 0.2,
        "new": 0.25,
        "active_when": "Super dragon form only"
      },
      {
        "id": "draco_17",
        "type": "other",
        "change_class": "source_conflict",
        "brawler": "Draco",
        "label": "Super damage 1120→1620",
        "reason": "Official scalar conflicts with Fandom per projectile 81, variable range and revised delivery; no equivalent fixed packet proven."
      },
      {
        "id": "shade_18",
        "type": "other",
        "change_class": "temporal_survival_excluded",
        "brawler": "Shade",
        "label": "Jump Scare shield 1000→400",
        "reason": "Decays every 0.5s; value depends on max health and timing."
      },
      {
        "id": "amber_19",
        "type": "other",
        "change_class": "temporal_survival_excluded",
        "brawler": "Amber",
        "label": "Super damage over time 480→400",
        "reason": "DoT application and time sequence."
      },
      {
        "id": "amber_20",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "brawler": "Amber",
        "label": "Fire Starters barrel health 1300→1000",
        "reason": "deployable, not roster target"
      },
      {
        "id": "nori_21",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "brawler": "Nori",
        "label": "Super per fish 4%→3%",
        "reason": "percentage health and fish sequence"
      },
      {
        "id": "squeak_22",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "brawler": "Squeak",
        "label": "Chain Reaction bonus 15%→10%",
        "reason": "target-count conditional; rounding unverified"
      },
      {
        "id": "ziggy_23",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "brawler": "Ziggy",
        "label": "The Great Ziggini 18%→7%",
        "reason": "previous hit state and fractional damage rounding unverified"
      },
      {
        "id": "remaining_utility_and_arena",
        "type": "other",
        "change_class": "non_breakpoint",
        "brawler": "multiple",
        "label": "Other utility, cooldown, charge, projectile size, speed, reworks and Brawl Arena-only scaling",
        "reason": "No static ranked fixed-packet transition; full inventory in official raw."
      },
      {
        "id": "mandy_hard_candy_removed",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "brawler": "Mandy",
        "label": "Hard Candy 50% Focus damage reduction removed with Gobstopper rework",
        "reason": "Pre-patch state removed from current profile; v1 cannot represent disappeared loadout with correct before/after availability, so no invented differential."
      },
      {
        "id": "mr_p_service_bell_buffie",
        "type": "other",
        "change_class": "temporal_survival_excluded",
        "brawler": "Mr. P",
        "label": "new Service Bell Buffie shield 1070 at P1",
        "reason": "new decaying barrier without previous counterpart; not static survival"
      },
      {
        "id": "buffie_nov_new_reworks",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "brawler": "multiple",
        "label": "Mr. P/Lou/Gale/Mandy/Chester/Berry new Buffies and reworks",
        "reason": "new conditional damage, summon, healing, damage reduction debuff, duration, or multi-stage attacks; no matching pre/post stable packet or time-sequence model."
      },
      {
        "id": "squeak_super_one_blob",
        "type": "damage_packet",
        "change_class": "breakpoint_supported",
        "brawler": "Squeak",
        "packet_id": "super.one_blob",
        "old_damage": 1000,
        "new_damage": 1100,
        "power_level": 1,
        "packet_unit": "one_secondary_blob",
        "repeat_model": "one_off",
        "active_when": "one Super secondary blob hits, excluding other blobs"
      },
      {
        "id": "squeak_super_multiblob",
        "type": "other",
        "change_class": "unsupported_mechanic",
        "brawler": "Squeak",
        "label": "Super multiple secondary blobs",
        "reason": "spatially variable multi-blob hits; single blob audited separately"
      }
    ]
  }
}
```

## version_fold_ledger

本块是本次更新的并入账本：官方说明中每个受影响英雄的改动原文与处置状态，以及地图池、新英雄、排位规则等环境项。字段与状态取值见维护 skill 的 `references/version-update.md`；`rows` 为官方原文，不改写。

```json
{
  "version_fold_ledger": {
    "schema": "brawlstar.version_fold_ledger.v1",
    "patch_id": "2026-11-03-release",
    "effective_at": "2026-11-03",
    "official_source": "https://supercell.com/en/games/brawlstars/blog/game-updates/release-notes-november-2026/",
    "raw": "raw/sources/supercell/release-notes-november-2026-2026-11-04.html",
    "upstream": {
      "fandom_version_history_revision": 222450
    },
    "brawlers": [
      {
        "brawler": "Amber",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Gadget - Dancing Flames cooldown increased from 14s to 20s",
          "Gadget - Fire Starters cooldown increased from 24s to 28s",
          "Gadget - Fire Starters barrel health reduced from 1300 to 1000",
          "Super damage over time reduced from 480 to 400",
          "Hypercharge Super radius reduced from 1600 to 1200"
        ],
        "fold": "numbers_only",
        "note": "Fire Starters 28s、Dancing Flames 20s、Super DoT 400、Hyper 半径 1200 已并入；11/11 单火苗 180 与 Super 回充 40 保留。"
      },
      {
        "brawler": "Angelo",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Main Attack time to fully charge reduced by 10%"
        ],
        "fold": "numbers_only",
        "note": "蓄满时间相对缩短 10%；Fandom 11-04 仍写 2.25 秒且未给新绝对值，未编造秒数。"
      },
      {
        "brawler": "Ash",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Super charge gained from Super reduced by 40%",
          "Super charge rate reduced by 15%"
        ],
        "fold": "model_changed",
        "note": "Super 自 Super 充能 -40%、Super 充能率 -15% 已并入 resource/cycle 说明；无可用绝对充能值。"
      },
      {
        "brawler": "Berry",
        "kinds": [
          "buffie_rework"
        ],
        "direction": "new_kit",
        "rows": [
          "Gadget 1: Friendship Is Great",
          "Berry swipes his tail, knocking back enemies and healing nearby allies for 520 health.",
          "Buffied: Drops an ice cream puddle under each healed ally.",
          "Gadget 2: Secret Formula (was Healthy Additives - Rework)",
          "Berry throws an extra scoop of ice cream with a longer lasting puddle. Main attacks landing in it make the puddle bigger. Consumes ammo.",
          "Buffied: Main attacks landing in the Gadget puddle will bounce onward.",
          "Star Power 1: Floor Is Fine",
          "Berry gains 50% increased reload speed while standing on his own melted ice cream.",
          "Buffied: Allies standing on Berry's ice cream also reload 20% faster.",
          "Star Power 2: Sticky Toppings (Rework)",
          "Berry's main attack slows enemies by 10% for 1 second on initial impact.",
          "Buffied: Berry gains a 10% movement speed boost when slowing enemies with his melted ice cream.",
          "Hypercharge: Double Scoops",
          "Sweet Swirl drops double the scoops of ice cream!",
          "Buffied: Berry's main attack splits into two after the first hit, leaving smaller, shorter-lasting puddles on each side."
        ],
        "fold": "model_changed",
        "note": "Secret Formula 替代 Healthy Additives，Friendship/Floor/Sticky/Double Scoops 与 11/11 群疗修复已并入；12 秒旧口径移除。"
      },
      {
        "brawler": "Brock",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Hypercharge rate reduced by 28%",
          "Star Power - More Rockets Buffie movement speed reduced from 30% to 20%",
          "Star Power - Rocket No. 4 Buffie time for extra range shot increased from 6s to 8s"
        ],
        "fold": "model_changed",
        "note": "Rocket No.4 8s、More Rockets 20%、Hyper 充能率 -28% 已并入；旧 6s/30% 口径清除。"
      },
      {
        "brawler": "Buster",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Trait Super charge near allies increased by 10%"
        ],
        "fold": "numbers_only",
        "note": "Trait 靠近队友充能 +10% 已并入 team_support；无数值表。"
      },
      {
        "brawler": "Chester",
        "kinds": [
          "buffie_rework"
        ],
        "direction": "new_kit",
        "rows": [
          "Base Kit Changes",
          "Chester can now always see what his next Super will be.",
          "Gadget 1: Prankster's Surprise (Rework)",
          "Chester hides a jack-in-the-box. The box jumps out and explodes at enemies within 2 tiles, randomly fearing, slowing, or damaging in an area.",
          "Buffied: Throw an extra fake box and hide them faster.",
          "Gadget 2: Candy Beans",
          "Chester gets a random buff.",
          "Buffied: Defeating an enemy refunds 50% of the Gadget cooldown.",
          "Star Power 1: Bell'O'Mania",
          "The first bell of Chester's attack sequence deals 150% damage.",
          "Buffied: The first bell also gains the effect of Chester's next Super: an extra 50% damage, slow, poison, or heal.",
          "Star Power 2: Jester's Privilege (Rework - was Sneak Peek)",
          "Hits from Chester's 4-bell attack give 30% extra Super charge.",
          "Buffied: After using his Super, Chester's next attack fires four bells.",
          "Hypercharge: Crunchy, Chewy, Gooey",
          "Chester throws a sweet that explodes and deals damage, spreads a poison cloud, then leaves a slowing area for a few seconds.",
          "Buffied: Chester's attack fires double the bells (2/4/6/8 instead of 1/2/3/4), each dealing 65% damage."
        ],
        "fold": "model_changed",
        "note": "下一个 Super 可见、Prankster 2 格随机控制、Bell'O'Mania/Jester's Privilege/Candy Beans Buffie/Hyper 已并入；11/11 盒子 1800 与超充普攻回充 -35% 保留。"
      },
      {
        "brawler": "Chuck",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Main Attack reload speed reduced from 2000 to 1800",
          "Super no longer loses unused charges on death"
        ],
        "fold": "model_changed",
        "note": "装填 1.8s、死亡保留未用 Super 充能已并入；旧 2s/清空口径清除。"
      },
      {
        "brawler": "Colette",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Hypercharge Super second projectile Super charge rate reduced by 75%"
        ],
        "fold": "numbers_only",
        "note": "Hyper Super 第二弹 Super 充能率 -75% 已并入；第二弹伤害比例仍按来源冲突处理。"
      },
      {
        "brawler": "Cosmo",
        "kinds": [
          "balance",
          "new_hypercharge"
        ],
        "direction": "mixed",
        "rows": [
          "Health increased from 3400 to 3600",
          "Gadget - Telescope Trap cooldown increased from 20s to 24s",
          "Gadget - Telescope Trap size reduced from 1300 to 1000",
          "Cosmo (COSMIC CAPTURE): The hyper projectile now homes in on its target and roots it for 2 seconds."
        ],
        "fold": "model_changed",
        "note": "Telescope Trap 24s/尺寸 1000、COSMIC CAPTURE 追踪+root 2s 已并入；Health 3600 保留。"
      },
      {
        "brawler": "Damian",
        "kinds": [
          "balance"
        ],
        "direction": "adjust",
        "rows": [
          "Super jump speed reduced from 3000 to 2400",
          "Main Attack regular punch damage increased from 700 to 800",
          "Main Attack fire punch damage increased from 800 to 880"
        ],
        "fold": "numbers_only",
        "note": "Super 跳跃速度 2400、普攻/火焰拳 800/880 已并入；高血与短手模型不变。"
      },
      {
        "brawler": "Darryl",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Super damage increased from 660 to 720",
          "Super no longer loses unused charges on death"
        ],
        "fold": "model_changed",
        "note": "Super 伤害 720、死亡保留未用充能已并入；滚动/护盾模型不变。"
      },
      {
        "brawler": "Draco",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Updated Draco super to be more consistent damage application.",
          "Super damage increased from 1120 to 1620",
          "Super damage reduction increased from 20% to 25%"
        ],
        "fold": "model_changed",
        "note": "Super 伤害应用更一致、官方 1120→1620、减伤 25% 已并入；逐弹 81×4 冲突保留，不生成固定斩杀线。"
      },
      {
        "brawler": "Gale",
        "kinds": [
          "buffie_rework"
        ],
        "direction": "new_kit",
        "rows": [
          "Gadget 1: North Wind Wall (Rework)",
          "Gale throws down a temporary wind wall that redirects enemy projectiles passing through it.",
          "Buffied: Allied projectiles that pass through the wall gain 30% projectile speed.",
          "Gadget 2: Twister",
          "Gale uses his snow blower to create a tornado that pushes away opponents trying to pass through.",
          "Buffied: Allies who pass through the tornado gain 20% movement speed for 2 seconds.",
          "Star Power 1: Blustery Blow",
          "Gale's Super stuns enemies for 1.25 seconds if they are pushed against obstacles.",
          "Buffied: Also deals 440 damage when stunning enemies.",
          "Star Power 2: Freezing Snow",
          "Gale's snowballs also slow opponents for 0.5 seconds.",
          "Buffied: Slows enemies by up to 50%, the closer they are to Gale.",
          "Hypercharge: Raging Blizzard",
          "Gale's Super is slightly wider and fires twice, pushing enemies even further away.",
          "Buffied: Gale fires an extra, larger snowball shortly after his attack."
        ],
        "fold": "model_changed",
        "note": "North Wind Wall/Twister/Blustery/Freezing/Hyper 重做已并入；11/11 最终 26s、偏转 20%、芭菲弹速 20% 保留。"
      },
      {
        "brawler": "Gus",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Max number of spirits allowed on the map reduced from 10 to 3",
          "Super charge rate reduced by 8%",
          "Gadget - Knockback Spirit cooldown increased from 18s to 26s",
          "Gadget - Knockback Spirit damage reduced from 540 to 260",
          "Star Power - Healing Bonanza bonus healing reduced from 75% to 50%",
          "Star Power - Healing Bonanza Buffie spirit movement speed reduced by 50%",
          "Hypercharge Buffie projectile size reduced by 15%"
        ],
        "fold": "model_changed",
        "note": "spirits 上限 3、Super 充能 -8%、Knockback 26s/260、Health Bonanza 50%/-50%、Hyper 弹体 -15% 已并入。"
      },
      {
        "brawler": "Hank",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Health increased from 5500 to 6000"
        ],
        "fold": "numbers_only",
        "note": "Health 6000 已在 profile 与 PL11 12000 口径；模型不变。"
      },
      {
        "brawler": "Kit",
        "kinds": [
          "balance"
        ],
        "direction": "adjust",
        "rows": [
          "Super damage is now more consistent, landing at 0.75s and 1.5s instead of 1s and 2s"
        ],
        "fold": "model_changed",
        "note": "Super 伤害 0.75s/1.5s 落地已并入 burst；engage 模型不变。"
      },
      {
        "brawler": "Lou",
        "kinds": [
          "buffie_rework"
        ],
        "direction": "new_kit",
        "rows": [
          "Gadget 1: Ice Block (Rework)",
          "Lou encases himself in an ice block, becoming invulnerable and unable to move for 2 seconds. Activating the Gadget again ends the ice block early.",
          "Buffied: Activating it also spawns a slippery ice area around Lou for 2 seconds that follows him, dealing 600 damage per second to opponents standing on it and building up their freeze meter.",
          "Gadget 2: Avalanche (new name)",
          "Lou lobs a large snowball that deals 500 damage and builds up 50% freeze where it lands.",
          "Buffied: The snowball leaves an ice patch that makes the ground slippery for 2 seconds.",
          "Star Power 1: Cold Snap (Rework)",
          "Lou deals 25% more damage to frozen or stunned enemies, including stuns that didn't come from Lou.",
          "Buffied: When their freeze ends, enemies shatter and deal 400 damage around them.",
          "Star Power 2: Hypothermia",
          "Opponents lose up to 50% of their damage based on how frozen they are from Lou's attacks.",
          "Buffied: The outer edge of Lou's Super becomes a ring of ice shards that deals 40 extra damage and freezes faster.",
          "Hypercharge: Slushie Storm",
          "Lou's Super instantly freezes enemies in the area.",
          "Buffied: Lou's attacks create a slippery area under them as they travel."
        ],
        "fold": "model_changed",
        "note": "Ice Block 2s、Avalanche 500/40%、Cold Snap 任意 frozen/stunned +25%、Hypothermia 芭菲 40、Hyper Slushie 已并入；11/11 40% 保留。"
      },
      {
        "brawler": "Maisie",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Main Attack damage reduced from 1500 to 1360"
        ],
        "fold": "numbers_only",
        "note": "Main Attack 1360（PL11 2720）已并入；Finish Them/Shove 模型不变。"
      },
      {
        "brawler": "Mandy",
        "kinds": [
          "buffie_rework"
        ],
        "direction": "new_kit",
        "rows": [
          "Base Kit Changes",
          "Mandy's old “In My Sights” Star Power is now part of her base kit, increasing her main attack projectile speed while Focused.",
          "Gadget 1: Caramelize (Rework)",
          "Mandy fires a caramelized candy that slows enemies hit for 2 seconds. The closer the target, the stronger the slow. It is now aimable and uses ammo.",
          "Buffied: Mandy gains a speed boost proportional to the slow applied.",
          "Gadget 2: Cookie Crumbs",
          "Mandy fires a candy that pierces through enemies and walls. It is now aimable and uses ammo.",
          "Buffied: Hitting a Brawler through a wall refunds 50% of the Gadget cooldown.",
          "Star Power 1: In My Sights (Rework)",
          "Each enemy hit while Focused extends Mandy's range by 1 tile until focus is broken.",
          "Buffied: Mandy stays Focused for 0.75 seconds after moving.",
          "Star Power 2: Gobstopper (Rework)",
          "Mandy's Super is 20% bigger.",
          "Buffied: Mandy's Super winds up 50% faster while Focused.",
          "Hypercharge: Sugar For All!",
          "Mandy fires her Super in three different directions.",
          "Buffied: Mandy stays Focused for the whole Hypercharge, even while moving, and her camera zooms out."
        ],
        "fold": "model_changed",
        "note": "基础 kit 专注弹速、Caramelize/Cookie 可瞄耗弹、In My Sights/Gobstopper/Hyper 已并入；11/11 25/10%、返冷 30% 保留。"
      },
      {
        "brawler": "Max",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Trait Super charge rate from moving reduced by 23%",
          "Star Power - Super Charged shield duration reduced from 4s to 3s",
          "Gadget - Sneaky Sneakers cooldown increased from 18s to 24s",
          "Gadget - Sneaky Sneakers duration reduced from 3s to 2s"
        ],
        "fold": "model_changed",
        "note": "移动充能 -23%、Super Charged 护盾 3s、Sneaky 24s/2s 已并入；旧 4s/3s/18s 口径清除。"
      },
      {
        "brawler": "Melodie",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Main Attack damage increased from 460 to 500",
          "Main Attack note damage increased from 920 to 1000",
          "Super no longer loses unused charges on death"
        ],
        "fold": "model_changed",
        "note": "主攻/环绕音 500/1000、死亡保留未用 Super 充能已并入；三段 dash 模型不变。"
      },
      {
        "brawler": "Mr. P",
        "kinds": [
          "buffie_rework"
        ],
        "direction": "new_kit",
        "rows": [
          "Gadget 1: Service Bell",
          "Mr. P buffs his current Porter, increasing its damage by 114 and its health by 740. It no longer has a range limit.",
          "Buffied: The buffed Porter and Mr. P both get a shield of 1070. It can also be used without a Porter to shield Mr. P.",
          "Gadget 2: Porter Reinforcements",
          "Mr. P launches a Porter-filled suitcase that deals 760 damage and spawns a mini-Porter where it lands.",
          "Buffied: Spawns an additional Porter for each enemy hit by the attack.",
          "Star Power 1: Handle With Care",
          "Every 4 seconds, the explosion damage of Mr. P's next overstuffed suitcase is increased by 40%.",
          "Buffied: The explosion triggers a second time, dealing 50% damage.",
          "Star Power 2: Revolving Door",
          "Robo-Porters from the home base have 20% more health and deal 30% more damage.",
          "Buffied: Mr. P's suitcase now heals Porters it hits for 420.",
          "Hypercharge: Super Porters! Assemble!",
          "Mr. P's home base spawns much stronger Porters, and he can have two Super Porters active at the same time.",
          "Buffied: After exploding, overstuffed suitcases bounce back towards Mr. P 3 times, exploding again each time."
        ],
        "fold": "model_changed",
        "note": "Service Bell/Porter Reinforcements/Handle With Care/Revolving Door/Hyper 重做已并入；11/11 耗弹 26s 保留。"
      },
      {
        "brawler": "Nori",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Super damage per fish reduced from 4% to 3%"
        ],
        "fold": "numbers_only",
        "note": "每鱼 Super 伤害 +3% 已并入；巨鱼绝对伤害按 P11 基础 3250 与满鱼 +30% 表述，不沿用旧 3500。"
      },
      {
        "brawler": "Pierce",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Main Attack last shot damage reduced from 1500 to 1400"
        ],
        "fold": "numbers_only",
        "note": "最后一发 1400（PL11 2800）已并入；弹壳循环模型不变。"
      },
      {
        "brawler": "R-T",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Main Attack projectile size increased by 15%"
        ],
        "fold": "numbers_only",
        "note": "主攻弹体尺寸 +15% 已并入；raw 未给绝对值，不编造格数。"
      },
      {
        "brawler": "Rico",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Gadget - Multiball Buffie slow reduced from 30% to 20%",
          "Star Power - Robo Retreat movement speed reduced from 35% to 25%",
          "Star Power - Robo Retreat Buffie max movement speed reduced from 50% to 40%"
        ],
        "fold": "numbers_only",
        "note": "Multiball 减速 20%、Robo Retreat 25/40% 已并入；旧 30/35/60% 口径清除。"
      },
      {
        "brawler": "Shade",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Health reduced from 3700 to 3400",
          "Super charge rate reduced by 12%",
          "Super duration reduced from 6s to 4s",
          "Trait Super charge from area reduced by 13%",
          "Gadget - Jump Scare cooldown increased from 18s to 24s",
          "Gadget - Jump Scare shield reduced from 1000 to 400",
          "Star Power - Hardened Hoodie shield reduced from 30% to 20%"
        ],
        "fold": "model_changed",
        "note": "Health 3400、Super 4s/-12%、Trait 面积 -13%、Jump Scare 24s/400 盾、Hoodie 20% 已并入。"
      },
      {
        "brawler": "Shelly",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Main Attack damage increased from 300 to 340",
          "Super damage increased from 320 to 360"
        ],
        "fold": "numbers_only",
        "note": "Main 340/Super 360 与全中包 1700/3240 已并入；近距离模型不变。"
      },
      {
        "brawler": "Squeak",
        "kinds": [
          "balance"
        ],
        "direction": "adjust",
        "rows": [
          "Main Attack damage increased from 1160 to 1280",
          "Super damage increased from 1000 to 1100",
          "Star Power - Chain Reaction bonus damage reduced from 15% to 10%"
        ],
        "fold": "numbers_only",
        "note": "Main 1280/Super 1100、Chain Reaction 10% 已并入；多 blob 不可合并机制保留。"
      },
      {
        "brawler": "Surge",
        "kinds": [
          "balance"
        ],
        "direction": "adjust",
        "rows": [
          "Hypercharge Super no longer gives an immediate upgrade to level 5",
          "Main Attack unload speed increased from 470 to 400",
          "Gadget - Power Shield cooldown reduced from 22s to 18s",
          "Gadget - Power Shield Buffie cooldown refund reduced from 50% to 30%"
        ],
        "fold": "model_changed",
        "note": "Hyper 不再直升 5、卸弹 400ms、Power Shield 18s/30% 返冷已并入；Stage 模型不变。"
      },
      {
        "brawler": "Vince",
        "kinds": [
          "new_hypercharge"
        ],
        "direction": "new_kit",
        "rows": [
          "Vince (BUG SWARM): Vince's Super is always at max power and releases Hypercharged caterpillars around him."
        ],
        "fold": "model_changed",
        "note": "BUG SWARM 最大威力 Super + 4 只 Hyper 毛毛虫已并入，并建成完整 bp_ready profile；11/11 衰减 +30% 保留。"
      },
      {
        "brawler": "Wendy",
        "kinds": [
          "balance"
        ],
        "direction": "nerf",
        "rows": [
          "Main Attack projectile size reduced by 20%",
          "Gadget - Wind-Powered range reduced from 15 to 10",
          "Star Power - Slowing Shield slow potency reduced from 20% to 15%"
        ],
        "fold": "model_changed",
        "note": "主攻 800、弹体 1.34 格（-20%）、Wind-Powered 3.33 格、Slowing Shield 15% 已并入；11/11 自盾 38% 保留。"
      },
      {
        "brawler": "Ziggy",
        "kinds": [
          "balance"
        ],
        "direction": "buff",
        "rows": [
          "Main Attack damage increased from 950 to 1050",
          "Starpower - The Great Ziggini bonus damage reduced from 18% to 7%"
        ],
        "fold": "numbers_only",
        "note": "Main 1050、Great Ziggini 7% 已并入；storm/slow 模型不变。"
      }
    ],
    "environment": [
      {
        "id": "new_brawlers",
        "kind": "new_brawler",
        "status": "deferred",
        "rows": [
          "Thunder Frogs - Legendary - Artillery",
          "Rey - Mythic - Marksman",
          "Ruby - Mythic - Damage Dealer"
        ],
        "note": "Thunder Frogs、Rey、Ruby 仍属预发布/未入 roster；2026-11-11 账本已把 Thunder Frogs 与 Rey 标为 deferred，待 roster 身份、发布状态与排位资格核实后建模。"
      },
      {
        "id": "new_maps",
        "kind": "map_rotation",
        "status": "done",
        "rows": [
          "Framework - Hotzone",
          "Sectioned - Hotzone",
          "Sunken harbor - Hotzone",
          "Human Nature - Brawl Ball",
          "Passing Through - Brawl Ball",
          "Front Tackle - Brawl Ball",
          "Printstream - Heist",
          "Fires Across - Heist",
          "On the Lookout - Heist",
          "Emotional Detachment - Gem Grab",
          "Don't Leaf Me - Gem Grab",
          "Ravenous Rapids - Gem Grab",
          "Sound Waves - Knockout",
          "Dry Run - Knockout",
          "Pincer Movement - Knockout",
          "Endothermic Shift - Bounty",
          "Eye of the Beholder - Bounty",
          "Sudden Movement - Bounty"
        ],
        "note": "已核对 Fandom Ranked Season 50（revid 221755，2026-11-13）：18 张社区地图不在当前 Ranked 池；地图池已更新为 Season 50。社区地图轮换本身仍不生成 map fit。"
      },
      {
        "id": "ranked_refresh",
        "kind": "ranked_rules",
        "status": "done",
        "rows": [
          "Ranked now requires Power 11 Brawlers at every rank, up from Power 9 in Bronze through Diamond.",
          "Diamond now needs 12 Brawlers, the same as Mythic, increased from 9.",
          "To make up for the higher Brawler requirements, the number of free maxed Brawlers increased from 3 to 6 each season.",
          "Ranked now unlocks at 5,000 Trophies, increased from 1,000.",
          "Players who already unlocked Ranked keep their access, and unlock a Chaos Drop at 5,000 Trophies instead.",
          "Brawl Arena still unlocks at 1,000 Trophies.",
          "No Ranked teams at Masters I and above.",
          "Best-of-three Elo now depends on rounds won: you gain extra for an Epic Win (2-0) and lose less for a Close Match (1-2).",
          "Higher Elo gains in the early and middle ranks, so progression feels better and more players reach Pro as the median Elo floor rises.",
          "The season reset now drops you 2 ranks, reduced from 6. No changes to the boost.",
          "Updated grid layout so you can see more Brawlers at once, with Brawler tiles that now show Gadgets and Star Powers.",
          "Added Brawler filtering, an option to turn favorites sorting on or off, class sorting as the new default, and Trophy sorting so you can show off your most-played Brawlers.",
          "Players who own fewer than 30 Brawlers get power level sorting by default.",
          "Alongside pick suggestions, you can now make ban suggestions: after banning a Brawler, selecting another Brawler will suggest it as a ban.",
          "Players can offer to swap pick order early in the Draft phase.",
          "The final preparation screen got a full visual overhaul, including a 3D map preview in the background.",
          "Besides changing your loadout and swapping Brawlers, you can now also change your Skin.",
          "Added quick chat during final preparation, so you can tell teammates what position you'll play, or send Pins and quick chat callouts to teammates and opponents."
        ],
        "note": "已把全段位 Power 11、Diamond 12 英雄、Ranked 5000 奖杯解锁、赛季重置 2 段、选人交换顺位等规则写入 wiki/concepts/Ranked.md；BP skill 不依赖在线 UI 顺位。"
      }
    ],
    "excluded": [
      {
        "scope": "Brawl Arena Only",
        "brawlers": [
          "8-Bit",
          "Chuck",
          "Doug",
          "Fang",
          "Gigi",
          "Gray",
          "Janet",
          "Mandy",
          "Najia",
          "Nori",
          "Ollie",
          "Piper",
          "Starr Nova",
          "Stu"
        ],
        "reason": "仅 Brawl Arena 成长系数，不影响排位。"
      }
    ]
  }
}
```
