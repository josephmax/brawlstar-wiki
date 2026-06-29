# User Note: BP Slot Perspective Correction

- Date: 2026-06-29
- Type: player correction / BP pick order model / local maintainer note

## Note Summary

The maintainer corrected a draft-slot schema mistake: slot 4 and slot 5 should not be described as knowing enemy slots 1-3.

In the standard six-pick draft order:

```text
1
2-3
4-5
6
```

the team with slot 4 and slot 5 is the same team that picked slot 1. Therefore, from that team's perspective, slots 4 and 5 know:

- own slot 1
- enemy slots 2 and 3

They do not know "enemy 1-3"; enemy slot 1 does not exist from their perspective.

## Durable Principle

BP slot reasoning must separate global chronological slot numbers from team-relative perspective. Every pick should record:

- global slot number
- team side
- known own picks
- known enemy picks
- remaining enemy response slots

This prevents incorrect assumptions about information state and last-pick pressure.
