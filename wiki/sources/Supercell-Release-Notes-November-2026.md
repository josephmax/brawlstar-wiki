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
