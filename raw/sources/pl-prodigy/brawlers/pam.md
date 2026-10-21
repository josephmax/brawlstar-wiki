# Direct Raw Capture: PLP Pam

- Title: Best build for Pam | Brawl Stars loadout, gears & counters | PL Prodigy
- URL: https://powerleagueprodigy.com/pam
- Capture date: 2026-10-21
- Correction note: nested `build` fields are preserved explicitly.
- Source type: third-party competitive guide
- Capture method: public Next.js page payload + metadata via curl
- Capture boundary: structured guide/loadout/mode/matchup fields only; page HTML and marketing UI omitted.
- Payload sourceUpdatedAt: unknown
- Meta description: Best Pam Brawl Stars build: use Mama's Hug Star Power, Scrapsucker Gadget, and Damage and Super Turret gears. See counters, matchup advice, and loadout choices. Best modes: Gem Grab and Hot Zone.

## Guide Fields

```json
{
  "key": "PAM",
  "internalName": "PAM",
  "name": "Pam",
  "slug": "pam",
  "id": 16000016,
  "description": "Pam handles an enormous workload at the junkyard and always gets it done! It's just a shame it keeps her away from her daughter, Jessie...",
  "catalog_class": "Support",
  "catalog_rarity": "Epic",
  "gadget": {
    "id": 23000404,
    "slot": 2,
    "code": "GADGET_2",
    "label": "Scrapsucker",
    "name": "Scrapsucker",
    "slug": "scrapsucker",
    "description": "Each hit from Pam's next attack removes 25% of opposing Brawlers' maximum ammo. Pam reclaims 50% of the ammo for herself.",
    "descriptionHtml": "Each hit from Pam's next attack removes 25% of opposing Brawlers' maximum ammo. Pam reclaims 50% of the ammo for herself.",
    "iconUrl": "https://cdn.brawlify.com/gadgets/regular/23000404.png",
    "tooltipNotes": [],
    "recommended": true,
    "guideHighlighted": false,
    "rawChoice": "2",
    "defaultDecisionRequired": false,
    "options": [
      {
        "id": 23000257,
        "slot": 1,
        "code": "GADGET_1",
        "label": "Pulse Modulator",
        "name": "Pulse Modulator",
        "slug": "pulse-modulator",
        "description": "Pam triggers her turret to emit a pulse that heals allies inside the turret's range, including herself, for 2000 health.",
        "descriptionHtml": "Pam triggers her turret to emit a pulse that heals allies inside the turret's range, including herself, for 2000 health.",
        "iconUrl": "https://cdn.brawlify.com/gadgets/regular/23000257.png",
        "tooltipNotes": [],
        "recommended": false,
        "guideHighlighted": false
      },
      {
        "id": 23000404,
        "slot": 2,
        "code": "GADGET_2",
        "label": "Scrapsucker",
        "name": "Scrapsucker",
        "slug": "scrapsucker",
        "description": "Each hit from Pam's next attack removes 25% of opposing Brawlers' maximum ammo. Pam reclaims 50% of the ammo for herself.",
        "descriptionHtml": "Each hit from Pam's next attack removes 25% of opposing Brawlers' maximum ammo. Pam reclaims 50% of the ammo for herself.",
        "iconUrl": "https://cdn.brawlify.com/gadgets/regular/23000404.png",
        "tooltipNotes": [],
        "recommended": true,
        "guideHighlighted": false
      }
    ]
  },
  "starPower": {
    "id": 23000092,
    "slot": 1,
    "code": "STAR_POWER_1",
    "label": "Mama's Hug",
    "name": "Mama's Hug",
    "slug": "mamas-hug",
    "description": "Whenever Pam hits enemy Brawlers with Scrapstorm, she heals herself and nearby friendly Brawlers for 100 health.",
    "descriptionHtml": "Whenever Pam hits enemy Brawlers with Scrapstorm, she heals herself and nearby friendly Brawlers for 100 health.",
    "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000092.png",
    "tooltipNotes": [],
    "recommended": true,
    "guideHighlighted": false,
    "rawChoice": "1",
    "defaultDecisionRequired": false,
    "options": [
      {
        "id": 23000092,
        "slot": 1,
        "code": "STAR_POWER_1",
        "label": "Mama's Hug",
        "name": "Mama's Hug",
        "slug": "mamas-hug",
        "description": "Whenever Pam hits enemy Brawlers with Scrapstorm, she heals herself and nearby friendly Brawlers for 100 health.",
        "descriptionHtml": "Whenever Pam hits enemy Brawlers with Scrapstorm, she heals herself and nearby friendly Brawlers for 100 health.",
        "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000092.png",
        "tooltipNotes": [],
        "recommended": true,
        "guideHighlighted": false
      },
      {
        "id": 23000139,
        "slot": 2,
        "code": "STAR_POWER_2",
        "label": "Mama's Squeeze",
        "name": "Mama's Squeeze",
        "slug": "mamas-squeeze",
        "description": "Healing turret now also damages enemies for 1000 damage per second.",
        "descriptionHtml": "Healing turret now also damages enemies for 1000 damage per second.",
        "iconUrl": "https://cdn.brawlify.com/star-powers/regular/23000139.png",
        "tooltipNotes": [],
        "recommended": false,
        "guideHighlighted": false
      }
    ]
  },
  "gears": [
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
      "id": 62000016,
      "code": "MYTHIC",
      "label": "Super Turret",
      "name": "Super Turret",
      "slug": "super-turret",
      "description": "Increase the healing of Pam's turret by 20%.",
      "rarity": "mythic",
      "iconUrl": "https://raw.githubusercontent.com/Brawlify/CDN/master/gears/regular/62000016.png",
      "tooltipNotes": []
    }
  ],
  "notes": [],
  "notesRaw": "",
  "modes": [
    {
      "code": "GEM_GRAB",
      "label": "Gem Grab"
    },
    {
      "code": "HOT_ZONE",
      "label": "Hot Zone"
    }
  ],
  "modesRaw": null,
  "counters": [],
  "countersRaw": "",
  "avoid": [],
  "avoidRaw": "",
  "sourceRow": null,
  "gearsRaw": null,
  "guideHref": "/pam",
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
      "key": "NORI",
      "id": 16000107,
      "name": "Nori",
      "slug": "nori",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000107.png"
    },
    {
      "key": "SQUEAK",
      "id": 16000047,
      "name": "Squeak",
      "slug": "squeak",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000047.png"
    },
    {
      "key": "GRAY",
      "id": 16000064,
      "name": "Gray",
      "slug": "gray",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000064.png"
    },
    {
      "key": "JACKY",
      "id": 16000034,
      "name": "Jacky",
      "slug": "jacky",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000034.png"
    },
    {
      "key": "BYRON",
      "id": 16000042,
      "name": "Byron",
      "slug": "byron",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000042.png"
    },
    {
      "key": "KIT",
      "id": 16000076,
      "name": "Kit",
      "slug": "kit",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000076.png"
    },
    {
      "key": "MEEPLE",
      "id": 16000089,
      "name": "Meeple",
      "slug": "meeple",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000089.png"
    },
    {
      "key": "SHELLY",
      "id": 16000000,
      "name": "Shelly",
      "slug": "shelly",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000000.png"
    }
  ],
  "counteredBy": [
    {
      "key": "AMBER",
      "id": 16000040,
      "name": "Amber",
      "slug": "amber",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000040.png"
    },
    {
      "key": "JUJU",
      "id": 16000087,
      "name": "Juju",
      "slug": "juju",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000087.png"
    },
    {
      "key": "SHADE",
      "id": 16000086,
      "name": "Shade",
      "slug": "shade",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000086.png"
    },
    {
      "key": "LARRYLAWRIE",
      "id": 16000077,
      "name": "Larry & Lawrie",
      "slug": "larrylawrie",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000077.png"
    },
    {
      "key": "NITA",
      "id": 16000008,
      "name": "Nita",
      "slug": "nita",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000008.png"
    },
    {
      "key": "SIRIUS",
      "id": 16000102,
      "name": "Sirius",
      "slug": "sirius",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000102.png"
    },
    {
      "key": "EMZ",
      "id": 16000030,
      "name": "Emz",
      "slug": "emz",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000030.png"
    },
    {
      "key": "ASH",
      "id": 16000051,
      "name": "Ash",
      "slug": "ash",
      "imageUrl": "https://cdn.brawlify.com/brawlers/borders/16000051.png"
    }
  ]
}
```
