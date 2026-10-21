# Direct Raw Capture: PLP Ollie

- Title: Best build for Ollie | Brawl Stars loadout, gears & counters | PL Prodigy
- URL: https://powerleagueprodigy.com/ollie
- Capture date: 2026-10-21
- Correction note: nested `build` fields are preserved explicitly.
- Source type: third-party competitive guide
- Capture method: public Next.js page payload + metadata via curl
- Capture boundary: structured guide/loadout/mode/matchup fields only; page HTML and marketing UI omitted.
- Payload sourceUpdatedAt: unknown
- Meta description: Best Ollie Brawl Stars build: use Renegade Star Power, Regulate Gadget, and Shield and Damage gears. See counters, matchup advice, and loadout choices. Best modes: Bounty and Knockout.

## Guide Fields

```json
{
  "key": "OLLIE",
  "internalName": "OLLIE",
  "name": "Ollie",
  "slug": "ollie",
  "id": 16000090,
  "description": "Ollie rides his customized hoverboard around Starr Park, grinding rails and causing trouble! A fan of old school hip hop, Ollie blasts his favorite tunes wherever he goes. His music is infectious... literally. Brawlers can't help but dance when they hear it.",
  "catalog_class": "Tank",
  "catalog_rarity": "Mythic",
  "gadget": {
    "id": 23000885,
    "slot": 1,
    "code": "GADGET_1",
    "label": "Regulate",
    "name": "Regulate",
    "slug": "regulate",
    "description": "Ollie jumps and does a rad kickflip, hypnotizing all enemies where he lands for 1 seconds.",
    "descriptionHtml": "Ollie jumps and does a rad kickflip, hypnotizing all enemies where he lands for 1 seconds.",
    "iconUrl": "https://cdn.brawlify.com/gadgets/regular/23000885.png",
    "tooltipNotes": [
      "Use gadget 1 when assassin pressure is absent."
    ],
    "recommended": true,
    "guideHighlighted": false,
    "rawChoice": "BOTH",
    "defaultDecisionRequired": true,
    "options": [
      {
        "id": 23000885,
        "slot": 1,
        "code": "GADGET_1",
        "label": "Regulate",
        "name": "Regulate",
        "slug": "regulate",
        "description": "Ollie jumps and does a rad kickflip, hypnotizing all enemies where he lands for 1 seconds.",
        "descriptionHtml": "Ollie jumps and does a rad kickflip, hypnotizing all enemies where he lands for 1 seconds.",
        "iconUrl": "https://cdn.brawlify.com/gadgets/regular/23000885.png",
        "tooltipNotes": [
          "Use gadget 1 when assassin pressure is absent."
        ],
        "recommended": true,
        "guideHighlighted": false
      },
      {
        "id": 23000886,
        "slot": 2,
        "code": "GADGET_2",
        "label": "All Eyez On Me",
        "name": "All Eyez On Me",
        "slug": "all-eyez-on-me",
        "description": "Ollie's next attack will hypnotize any enemies hit for 1 seconds.",
        "descriptionHtml": "Ollie's next attack will hypnotize any enemies hit for 1 seconds.",
        "iconUrl": "https://cdn.brawlify.com/gadgets/regular/23000886.png",
        "tooltipNotes": [
          "Use gadget 2 into assassins."
        ],
        "recommended": true,
        "guideHighlighted": false
      }
    ]
  },
  "starPower": {
    "id": 23000884,
    "slot": 2,
    "code": "STAR_POWER_2",
    "label": "Renegade",
    "name": "Renegade",
    "slug": "renegade",
    "description": "After dashing forward with his Super, Ollie gains a 3000 decaying shield over 4 seconds.",
    "descriptionHtml": "After dashing forward with his Super, Ollie gains a 3000 decaying shield over 4 seconds.",
    "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000884.png",
    "tooltipNotes": [],
    "recommended": true,
    "guideHighlighted": false,
    "rawChoice": "2",
    "defaultDecisionRequired": false,
    "options": [
      {
        "id": 23000883,
        "slot": 1,
        "code": "STAR_POWER_1",
        "label": "Kick, Push",
        "name": "Kick, Push",
        "slug": "kick-push",
        "description": "While near walls Ollie kicks off his hoverboard and gains 20% extra movement speed.",
        "descriptionHtml": "While near walls Ollie kicks off his hoverboard and gains 20% extra movement speed.",
        "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000883.png",
        "tooltipNotes": [],
        "recommended": false,
        "guideHighlighted": false
      },
      {
        "id": 23000884,
        "slot": 2,
        "code": "STAR_POWER_2",
        "label": "Renegade",
        "name": "Renegade",
        "slug": "renegade",
        "description": "After dashing forward with his Super, Ollie gains a 3000 decaying shield over 4 seconds.",
        "descriptionHtml": "After dashing forward with his Super, Ollie gains a 3000 decaying shield over 4 seconds.",
        "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000884.png",
        "tooltipNotes": [],
        "recommended": true,
        "guideHighlighted": false
      }
    ]
  },
  "gears": [
    {
      "id": 62000004,
      "code": "SHIELD",
      "label": "Shield",
      "name": "Shield",
      "slug": "shield",
      "description": "Gain a 900-health consumable shield. The shield regenerates over 10 seconds while at full health.",
      "rarity": "super-rare",
      "iconUrl": "https://raw.githubusercontent.com/Brawlify/CDN/master/gears/regular/62000004.png",
      "tooltipNotes": []
    },
    {
      "id": 62000002,
      "code": "DAMAGE",
      "label": "Damage",
      "name": "Damage",
      "slug": "damage",
      "description": "Deal 15% extra damage while below 50% health.",
      "rarity": "super-rare",
      "iconUrl": "https://raw.githubusercontent.com/Brawlify/CDN/master/gears/regular/62000002.png",
      "tooltipNotes": []
    },
    {
      "id": 62000001,
      "code": "HEALTH",
      "label": "Health",
      "name": "Health",
      "slug": "health",
      "description": "Recover health 50% more effectively.",
      "rarity": "super-rare",
      "iconUrl": "https://raw.githubusercontent.com/Brawlify/CDN/master/gears/regular/62000001.png",
      "tooltipNotes": []
    }
  ],
  "notes": [],
  "notesRaw": "",
  "modes": [
    {
      "code": "BOUNTY",
      "label": "Bounty"
    },
    {
      "code": "KNOCKOUT",
      "label": "Knockout"
    }
  ],
  "modesRaw": null,
  "counters": [],
  "countersRaw": "",
  "avoid": [],
  "avoidRaw": "",
  "sourceRow": null,
  "gearsRaw": null,
  "guideHref": "/ollie",
  "hasLegacyGuide": false,
  "legacySlug": "",
  "legacyGuideHref": ""
}
```

## Matchup Fields

```json
{
  "countersThese": [
    {
      "key": "ZIGGY",
      "id": 16000098,
      "name": "Ziggy",
      "slug": "ziggy",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000098.png"
    },
    {
      "key": "NANI",
      "id": 16000036,
      "name": "Nani",
      "slug": "nani",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000036.png"
    },
    {
      "key": "TICK",
      "id": 16000022,
      "name": "Tick",
      "slug": "tick",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000022.png"
    },
    {
      "key": "NORI",
      "id": 16000107,
      "name": "Nori",
      "slug": "nori",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000107.png"
    },
    {
      "key": "GROM",
      "id": 16000048,
      "name": "Grom",
      "slug": "grom",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000048.png"
    },
    {
      "key": "KIT",
      "id": 16000076,
      "name": "Kit",
      "slug": "kit",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000076.png"
    },
    {
      "key": "COSMO",
      "id": 16000109,
      "name": "Cosmo",
      "slug": "cosmo",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000109.png"
    },
    {
      "key": "RUFFS",
      "id": 16000044,
      "name": "Ruffs",
      "slug": "ruffs",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000044.png"
    }
  ],
  "counteredBy": [
    {
      "key": "MEEPLE",
      "id": 16000089,
      "name": "Meeple",
      "slug": "meeple",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000089.png"
    },
    {
      "key": "CARL",
      "id": 16000025,
      "name": "Carl",
      "slug": "carl",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000025.png"
    },
    {
      "key": "DOUG",
      "id": 16000071,
      "name": "Doug",
      "slug": "doug",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000071.png"
    },
    {
      "key": "EDGAR",
      "id": 16000043,
      "name": "Edgar",
      "slug": "edgar",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000043.png"
    },
    {
      "key": "WENDY",
      "id": 16000108,
      "name": "Wendy",
      "slug": "wendy",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000108.png"
    },
    {
      "key": "PEARL",
      "id": 16000072,
      "name": "Pearl",
      "slug": "pearl",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000072.png"
    },
    {
      "key": "BROCK",
      "id": 16000003,
      "name": "Brock",
      "slug": "brock",
      "imageUrl": "/brawlers/Brock.webp"
    },
    {
      "key": "GUS",
      "id": 16000061,
      "name": "Gus",
      "slug": "gus",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000061.png"
    }
  ]
}
```
