# User Note: Preserve BP Reasoning as DSL

- Date: 2026-06-29
- Type: player experience / BP knowledge model / local maintainer note

## Original Concern

The maintainer asked how the current Ban Pick reasoning should be abstracted into a suitable DSL or document so that another LLM can understand it reliably.

The concern is that the short-term chat context may disappear, and the high-value modeling work around conditional matchup, slot strategy, hard gates, and draft reasoning should not remain trapped in session memory.

## Note Summary

The BP model needs a durable execution contract, not only a prose summary.

The desired artifact should let another LLM:

- receive a structured draft state
- identify active mode, map, ban, pick, matchup, build, and slot conditions
- avoid treating static counter tables as final truth
- assume high-level rational play rather than low-rank noise
- combine hard threat gates with current-slot capability needs
- output a small set of best pick or ban decisions with reasons, risks, and likely enemy response

## Durable Principle

The knowledge base should preserve BP reasoning as a reusable schema plus execution procedure. The schema should be readable as Markdown, but strict enough that a future LLM can follow the same decision path without relying on this chat history.
