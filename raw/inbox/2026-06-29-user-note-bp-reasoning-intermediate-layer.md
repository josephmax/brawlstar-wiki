# User Note: BP Reasoning Needs a Conditional Intermediate Layer

- Date: 2026-06-29
- Type: player experience / BP knowledge model / local maintainer note

## Note Summary

The maintainer clarified that the ideal knowledge base should support tactical simulation and Ban Pick reasoning around an explicit intermediate layer.

Every BP step should carry map, mode, matchup, team plan, and execution conditions, then quickly produce a few currently optimal decisions with reasons. Quantitative scoring can come later; the immediate need is a qualitative structure that helps LLM reasoning stay grounded.

The missing layer is an abstraction between raw hero facts and final draft advice:

- map structure should activate or deactivate matchup relationships
- brawler abilities should be represented as tactical capabilities, not just role labels
- counter relationships should become conditional matchup edges
- draft evaluation should explain win conditions, exposed weaknesses, role coverage, and likely response paths

## Durable Principle

The knowledge base should not store static counter claims as final BP truth. It should store conditional intermediate artifacts that let an LLM reason through each draft state.

Useful BP output should answer:

- What conditions are active on this map and mode?
- Which matchup edges are activated or disabled?
- What is each team's current win condition?
- What role or threat is currently missing?
- Which picks or bans are best now, and why?
- What enemy response becomes natural after this decision?
