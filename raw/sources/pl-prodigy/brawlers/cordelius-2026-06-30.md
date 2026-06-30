# Direct Raw Capture: PLP Cordelius

- Title: Best build for Cordelius | Brawl Stars loadout, gears & counters | PL Prodigy
- URL: https://powerleagueprodigy.com/cordelius
- Capture date: 2026-06-30
- Correction note: nested `build` fields are preserved explicitly.
- Source type: third-party competitive guide
- Capture method: public Next.js page payload + metadata via curl
- Capture boundary: structured guide/loadout/mode/matchup fields only; page HTML and marketing UI omitted.
- Payload sourceUpdatedAt: 2026-05-25T17:15:02Z
- Meta description: Best Cordelius Brawl Stars build: use Comboshrooms Star Power, Replanting Gadget, and Shield and Damage gears. See counters, matchup advice, and loadout choices. Best modes: Heist, Brawl Ball, and Gem Grab.

## Guide Fields

```json
{
  "key": "CORDELIUS",
  "internalName": "CORDELIUS",
  "name": "Cordelius",
  "slug": "cordelius",
  "id": 16000070,
  "description": "Gardener and caretaker of the Enchanted Forest. Obsesses over mushrooms and is hostile towards strangers.",
  "catalog_class": "Assassin",
  "catalog_rarity": "Legendary",
  "gadget": {
    "slot": 1,
    "code": "GADGET_1",
    "label": "Replanting",
    "iconUrl": "https://cdn.brawlify.com/gadgets/regular/23000587.png",
    "id": 23000587,
    "rawChoice": "BOTH",
    "defaultDecisionRequired": true,
    "options": [
      {
        "slot": 1,
        "code": "GADGET_1",
        "label": "Replanting",
        "iconUrl": "https://cdn.brawlify.com/gadgets/regular/23000587.png",
        "id": 23000587,
        "tooltipNotes": []
      },
      {
        "slot": 2,
        "code": "GADGET_2",
        "label": "Poison Mushroom",
        "iconUrl": "https://cdn.brawlify.com/gadgets/regular/23000588.png",
        "id": 23000588,
        "tooltipNotes": [
          "Generally prefer Poison Mushroom into aggressive enemy comps."
        ]
      }
    ],
    "tooltipNotes": []
  },
  "starPower": {
    "slot": 1,
    "code": "STAR_POWER_1",
    "label": "Comboshrooms",
    "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000585.png",
    "id": 23000585,
    "rawChoice": "1",
    "defaultDecisionRequired": false,
    "options": [
      {
        "slot": 1,
        "code": "STAR_POWER_1",
        "label": "Comboshrooms",
        "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000585.png",
        "id": 23000585,
        "tooltipNotes": []
      },
      {
        "slot": 2,
        "code": "STAR_POWER_2",
        "label": "Mushroom Kingdom",
        "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000586.png",
        "id": 23000586,
        "tooltipNotes": []
      }
    ],
    "tooltipNotes": []
  },
  "gears": [
    {
      "code": "SHIELD",
      "label": "Shield",
      "id": 62000004,
      "iconUrl": "https://raw.githubusercontent.com/Brawlify/CDN/master/gears/regular/62000004.png"
    },
    {
      "code": "DAMAGE",
      "label": "Damage",
      "id": 62000002,
      "iconUrl": "https://raw.githubusercontent.com/Brawlify/CDN/master/gears/regular/62000002.png"
    }
  ],
  "notes": [
    "GADGET 2 AGGRO"
  ],
  "notesRaw": "GADGET 2 AGGRO",
  "modes": [
    {
      "code": "HEIST",
      "label": "Heist"
    },
    {
      "code": "BRAWL_BALL",
      "label": "Brawl Ball"
    },
    {
      "code": "GEM_GRAB",
      "label": "Gem Grab"
    },
    {
      "code": "HOT_ZONE",
      "label": "Hot Zone"
    }
  ],
  "modesRaw": "HEIST BRAWLBALL GEMGRAB HOTZONE",
  "counters": [
    "CHUCK"
  ],
  "countersRaw": "CHUCK",
  "avoid": [],
  "avoidRaw": "",
  "sourceRow": 26,
  "gearsRaw": "SHIELD DAMAGE",
  "guideHref": "/cordelius",
  "hasLegacyGuide": true,
  "legacySlug": "cordelius",
  "legacyGuideHref": "/legacy/cordelius"
}
```

## Matchup Fields

```json
{
  "name": "Cordelius",
  "slug": "cordelius",
  "countersThese": [
    {
      "key": "TARA",
      "name": "Tara",
      "slug": "tara",
      "id": 16000017,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "SHELLY",
      "name": "Shelly",
      "slug": "shelly",
      "id": 16000000,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "ROSA",
      "name": "Rosa",
      "slug": "rosa",
      "id": 16000024,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "CHUCK",
      "name": "Chuck",
      "slug": "chuck",
      "id": 16000073,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "STU",
      "name": "Stu",
      "slug": "stu",
      "id": 16000045,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "COLETTE",
      "name": "Colette",
      "slug": "colette",
      "id": 16000039,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "BULL",
      "name": "Bull",
      "slug": "bull",
      "id": 16000002,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "FANG",
      "name": "Fang",
      "slug": "fang",
      "id": 16000054,
      "source": "legacy",
      "matchupTier": "manual"
    }
  ],
  "counteredBy": [
    {
      "key": "GALE",
      "name": "Gale",
      "slug": "gale",
      "id": 16000035,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "MAX",
      "name": "Max",
      "slug": "max",
      "id": 16000032,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "NITA",
      "name": "Nita",
      "slug": "nita",
      "id": 16000008,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "FRANK",
      "name": "Frank",
      "slug": "frank",
      "id": 16000020,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "GRIFF",
      "name": "Griff",
      "slug": "griff",
      "id": 16000050,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "CROW",
      "name": "Crow",
      "slug": "crow",
      "id": 16000012,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "AMBER",
      "name": "Amber",
      "slug": "amber",
      "id": 16000040,
      "source": "legacy",
      "matchupTier": "manual"
    },
    {
      "key": "SURGE",
      "name": "Surge",
      "slug": "surge",
      "id": 16000038,
      "source": "legacy",
      "matchupTier": "manual"
    }
  ]
}
```
