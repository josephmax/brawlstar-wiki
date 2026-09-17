# Direct Raw Capture: Fandom Wendy

- Title: Wendy
- URL: https://brawlstars.fandom.com/wiki/Wendy
- Capture date: 2026-09-17
- Correction note: captured manually via the same MediaWiki API channel as `capture_brawler_sources.py` because Wendy is absent from the default roster manifest used by that script.
- Source last edited: 2026-09-16T20:35:03Z (revid 219087)
- Capture method: Fandom MediaWiki API revisions content via curl
- Capture boundary: selected hero mechanics and BP-relevant tips excerpts; cosmetic/voice/skin sections omitted.
- Full source wikitext length at capture: 14082 characters

## Infobox Fields

- Title: Blows you away
- PrestigeTitle: Go Green!
- Rarity: Mythic
- Class: Support
- MovementSpeed: 800 (Fast)
- HealthLabel: Health
- Health: 2500
- AttackLabel: Damage
- Attack: 1000
- AttackLabel2: Shield Health on herself
- Attack2: 300
- AttackLabel3: Shield Health on allies
- Attack3: 760
- AttackRange: 8 (Long)
- Reload: 1.45 seconds (Fast)
- AttackSuperCharge: 17%
- SuperLabel: Health
- Super: 2500
- SuperRange: 5 (Normal)
- Gadget1Name: Wind-Powered (cooldown 18 seconds)
- Gadget2Name: Green Grenade (cooldown 18 seconds)
- StarPower2Name: Solar Shield
- StarPower2Label: Health
- StarPower2: 1080
- HyperchargeMultiplier: 30%

## Selected Wikitext Excerpts

### Lead excerpt

Wendy is a Mythic Brawler who has the second-lowest health and a moderate damage output, but has a fast movement and reload speed, a long range, and immense survivability thanks to her attack, Super, and Trait. She was the 106th Brawler added to the game. Her Traits allow her to move over water, and to charge her Super from enemies damaging her shield.

### Trait: Shield Damage

It takes 6.67x of the shield's max health of damage to charge her Super completely, and all damage is calculated after shielding and other effects. Wendy also spawns with a shield already active, which is equal to 40% of her maximum health. This shield does not decay, but can only be replenished with her main attack.

### Attack: Blow Dryer

Wendy fires a blast dealing 2000 damage and giving herself 600 shield. When hitting a teammate, Wendy gives them 1520 shield. (infobox Power 1 values: damage 1000, self shield 300, ally shield 760)

Wendy fires a blast that deals moderate damage to enemies, has a long range, and provides herself a consumable shield that is 30% of the damage. However, upon firing the attack on allies, she instead provides them a shield that is 30.4% of her max original health. Wendy's shield on herself does not decay, but her allies' decay for 5% health every 0.5 seconds, similar to other consumable shields. If an attack deals more damage than the shield's current health, the shield disappears and Wendy and her allies with the shield is damaged by the remaining damage. Colette's attack and Super will deal damage based on the Brawler's max health when this shield is active. The shield on allies does stack, up to 160% of Wendy's original max HP.

### Super: Planet Protector

Wendy lobs a wind turbine that covers a 6-tile radius. The turbine passively reduces all damage Wendy and her allies take by 60% by redirecting the damage to the Super instead.

### Star Power: Solar Shield

Quote: "Wendy's shield generator gains an additional 1200 health." Body: "This Star Power increases the shield generator's health by 24%." Infobox value: 1080.

### Hypercharge: Green Energy

When activated, Wendy's Planet Protector has 1000 more HP and absorbs 90% damage from attacks. She also gains a 20% speed boost, and a 5% damage and shield boost.

### Tips / Other

You can essentially treat Wendy's shield on herself as bonus health: it doesn't decrease automatically, and is used in place of the 5000 base health, although also doesn't increase automatically. Therefore, Wendy when she spawns should be considered as if she has 7000 HP.

### History (2026 entries relevant to balance)

- 01/09/26: Super charge from hits increased to 6 hits (from 5); Trait shield-damage Super charge decreased to 30% (from 50%); Super turret health decreased to 2500 (from 3500); turret damage redirection decreased to 60% (from 75%); every Brawler's movement speed was increased, increasing Wendy's movement speed to 800 (from 770); Green Energy Hypercharge added.
- 16/09/26: health increased to 2500 (from 2000); Trait shield-damage Super charge decreased to 15% (from 30%); max shield health decreased to 40% of her max HP (from 100%); provided shield health given with her main attack decreased to 300 (from 580); Solar Shield generator health bonus decreased to 1080 (from 1800); Green Energy Hypercharge generator health bonus decreased to 1000 (from 2000).

## Source Conflicts To Preserve

- Solar Shield bonus health: maintenance note (Version History/2026) says `1000 -> 600`; this individual page History says `1800 -> 1080`, the Star Power quote says `1200`, and the body text expresses it as `24%` of generator health. The values do not reconcile under a single Power Level; keep the individual page as current-state evidence and preserve the conflict.
- Trait shield-damage Super charge `30% -> 15%` appears in this page's 16/09 History but is absent from the maintenance balance index.
- Maintenance index phrasing "Hypercharge - turret health 4500 -> 3500" corresponds to this page's decomposition: base turret 2500 + Green Energy bonus (2000 -> 1000).

## Raw Use Boundary

- Use this page for Wendy's post-2026-09-16 current state values.
- Power Level of infobox numbers follows the wiki's standard Power 1 convention; PL11 doubles standard scalars.
