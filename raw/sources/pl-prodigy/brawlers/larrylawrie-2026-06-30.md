# Direct Raw Capture: PLP Larry & Lawrie

- Title: Best build for Larry & Lawrie | Brawl Stars loadout, gears & counters | PL Prodigy
- URL: https://powerleagueprodigy.com/larrylawrie
- Capture date: 2026-06-30
- Correction note: nested `build` fields are preserved explicitly.
- Source type: third-party competitive guide
- Capture method: public Next.js page payload + metadata via curl
- Capture boundary: structured guide/loadout/mode/matchup fields only; page HTML and marketing UI omitted.
- Payload sourceUpdatedAt: 2026-05-25T17:15:02Z
- Meta description: Best Larry & Lawrie Brawl Stars build: use Protocol Assist Star Power, Order Fall Back Gadget, and Shield and Damage gears. See counters, matchup advice, and loadout choices. Best modes: Brawl Ball and Hot Zone.

## Guide Fields

```json
{
  "key": "LARRYLAWRIE",
  "internalName": "LARRY & LAWRIE",
  "name": "Larry & Lawrie",
  "slug": "larrylawrie",
  "id": 16000077,
  "description": "Larry sells tickets to Starr Park visitors under the watchful eye of his twin, Lawrie. Larry loves rules, they make life easier! Lawrie doesn't love rules so much as enforcing them. They make a good team.",
  "catalog_class": "Artillery",
  "catalog_rarity": "Epic",
  "gadget": {
    "slot": 2,
    "code": "GADGET_2",
    "label": "Order Fall Back",
    "iconUrl": "/icons/substitute/23000662.png",
    "id": 23000662,
    "rawChoice": "2",
    "defaultDecisionRequired": false,
    "options": [
      {
        "slot": 1,
        "code": "GADGET_1",
        "label": "Order: Swap",
        "iconUrl": "/icons/substitute/23000661.png",
        "id": 23000661,
        "tooltipNotes": []
      },
      {
        "slot": 2,
        "code": "GADGET_2",
        "label": "Order: Fall Back",
        "iconUrl": "/icons/substitute/23000662.png",
        "id": 23000662,
        "tooltipNotes": []
      }
    ],
    "tooltipNotes": []
  },
  "starPower": {
    "slot": 2,
    "code": "STAR_POWER_2",
    "label": "Protocol Assist",
    "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000660.png",
    "id": 23000660,
    "rawChoice": "2",
    "defaultDecisionRequired": false,
    "options": [
      {
        "slot": 1,
        "code": "STAR_POWER_1",
        "label": "Protocol Protect",
        "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000659.png",
        "id": 23000659,
        "tooltipNotes": []
      },
      {
        "slot": 2,
        "code": "STAR_POWER_2",
        "label": "Protocol Assist",
        "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000660.png",
        "id": 23000660,
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
  "notes": [],
  "notesRaw": "",
  "modes": [
    {
      "code": "BRAWL_BALL",
      "label": "Brawl Ball"
    },
    {
      "code": "HOT_ZONE",
      "label": "Hot Zone"
    }
  ],
  "modesRaw": "BRAWLBALL HOTZONE",
  "counters": [],
  "countersRaw": "",
  "avoid": [],
  "avoidRaw": "",
  "sourceRow": 56,
  "gearsRaw": "SHIELD DAMAGE",
  "guideHref": "/larrylawrie",
  "hasLegacyGuide": false,
  "legacySlug": "",
  "legacyGuideHref": ""
}
```

## Matchup Fields

```json
{
  "name": "Larry & Lawrie",
  "slug": "larrylawrie",
  "countersThese": [
    {
      "key": "SPROUT",
      "name": "Sprout",
      "slug": "sprout",
      "id": 16000037,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.682
    },
    {
      "key": "JAEYONG",
      "name": "Jae-Yong",
      "slug": "jaeyong",
      "id": 16000093,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.668
    },
    {
      "key": "RUFFS",
      "name": "Ruffs",
      "slug": "ruffs",
      "id": 16000044,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.659
    },
    {
      "key": "NANI",
      "name": "Nani",
      "slug": "nani",
      "id": 16000036,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.65
    },
    {
      "key": "SQUEAK",
      "name": "Squeak",
      "slug": "squeak",
      "id": 16000047,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.65
    },
    {
      "key": "MANDY",
      "name": "Mandy",
      "slug": "mandy",
      "id": 16000065,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.649
    },
    {
      "key": "BELLE",
      "name": "Belle",
      "slug": "belle",
      "id": 16000046,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.641
    },
    {
      "key": "MEG",
      "name": "Meg",
      "slug": "meg",
      "id": 16000052,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.628
    }
  ],
  "counteredBy": [
    {
      "key": "SAM",
      "name": "Sam",
      "slug": "sam",
      "id": 16000060,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.661
    },
    {
      "key": "EDGAR",
      "name": "Edgar",
      "slug": "edgar",
      "id": 16000043,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.66
    },
    {
      "key": "BIBI",
      "name": "Bibi",
      "slug": "bibi",
      "id": 16000026,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.647
    },
    {
      "key": "DAMIAN",
      "name": "Damian",
      "slug": "damian",
      "id": 16000104,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.636
    },
    {
      "key": "TRUNK",
      "name": "Trunk",
      "slug": "trunk",
      "id": 16000096,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.597
    },
    {
      "key": "BOLT",
      "name": "Bolt",
      "slug": "bolt",
      "id": 16000106,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.592
    },
    {
      "key": "ROSA",
      "name": "Rosa",
      "slug": "rosa",
      "id": 16000024,
      "source": "data",
      "matchupTier": "global-best-modes",
      "winRate": 0.588
    },
    {
      "key": "SHADE",
      "name": "Shade",
      "slug": "shade",
      "id": 16000086,
      "source": "data",
      "matchupTier": "direct-weighted-best-modes",
      "winRate": 0.584,
      "directSampleCount": 627
    }
  ]
}
```
