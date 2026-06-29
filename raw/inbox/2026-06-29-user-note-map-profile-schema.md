# User Note: Map Profile Needs Tactical Feature Schema

- Date: 2026-06-29
- Type: player experience / BP knowledge model / local maintainer note

## Original Concern

The maintainer pointed out that the current `map_profile` abstraction in Canonical Input is too coarse. Fields such as `open`, `mixed`, `wall_density`, or `water_value` do not carry enough information for real Ban Pick reasoning.

## Safe Zone Example

Using Safe Zone as the example:

- The map has a river. Brawlers that can cross water, such as Angelo and Eve, are naturally less likely to be trapped at home.
- Long-range brawlers can sometimes pressure the safe without crossing the river, such as Grom.
- Water-crossing alone is not sufficient. Short-range brawlers that can cross, such as Shade or the maintainer's example of 阿尔缇, may still suffer badly unless the current draft gives them high tactical value.
- If the enemy does not split lanes, the middle becomes crowded. This increases the value of brawlers that punish congestion, such as Jessie, Belle, Mandy, and the maintainer's example of 皮尔斯.
- There is a corner terrain near the safe that can help some brawlers survive repeatedly after crossing into the enemy base, such as Mico, Rico, and Berry.

## Durable Principle

Map modeling should not stop at coarse tags. It should express concrete terrain features as tactical affordances:

- what route a feature opens or closes
- which capabilities can use that route
- which capabilities are false positives
- what objective payoff the route creates
- what local combat pattern the feature rewards
- how the feature changes draft value under specific lane and comp states

The schema should connect map geometry to brawler capabilities, conditional matchups, and draft decisions.
