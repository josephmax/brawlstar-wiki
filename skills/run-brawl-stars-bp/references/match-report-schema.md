# Human BP Match Report Template

Use this template for every `match-<map>.md` report. The report is for humans, not parsers.

Hard rules:

- Write plain Markdown only. Do not use YAML blocks, JSON blocks, raw structured logs, or `match_header`.
- Do not include `favored_side`, win probability, confidence score, judge-side draft evaluation, or any side preference.
- Do not include token tables full of `null`. Add `Execution Metadata` only when real metrics or a real failure state was captured.
- Record both `strategy_bias` values in `Match Summary`.
- Use `state_handoff_to_next_turn`, not pressure language. The handoff may state visible facts and open structural questions, but must not tell the next player what to pick.
- Copy, normalize, and lightly format player-submitted reasons. Do not add independent BP analysis.

## Match Summary

Start every report with:

- Map and mode.
- Blue strategy bias and red strategy bias.
- Ban format: simultaneous bans, duplicates allowed.
- Pick order.
- Final drafts.
- Duplicate bans, if any.
- One neutral sentence summarizing how the draft unfolded. This must describe sequence, not quality.

## Ban Phase

Use two short lists:

### Blue Bans

For each ban:

- `Brawler`: player-submitted intent; what route it removes; what plan it protects; risk if open.

### Red Bans

Same shape as Blue Bans.

End the section with:

- Duplicated bans.
- Unavailable pool after bans.

## Draft Timeline

Use one subsection per pick turn:

### Blue Slot 1 - `Pick`
### Red Slots 2-3 - `Pick + Pick`
### Blue Slots 4-5 - `Pick + Pick`
### Red Slot 6 - `Pick`

Each subsection must include:

- Visible state: own picks, enemy picks, unavailable pool.
- Player submitted reason.
- What the pick says it covers: enemy picks, map factors, or objective duties named by the player.
- Required build(s).
- Rejected options and the player-submitted reason.
- State handoff to next turn: visible facts and remaining structural questions only.

For the last turn, replace state handoff with "Final visible state".

## Player Final Statements

Record only what players submitted:

### Blue Player

- Comp.
- Submitted win condition.
- Submitted key risks.
- Submitted uncertainties.

### Red Player

Same shape.

End with:

- Judge note: no judge draft evaluation was added.

## Stable Knowledge Refs

Copy refs from player submissions when available. Do not invent refs during report writing.

## Execution Metadata

Omit this section unless at least one of these is true:

- real token usage was captured by tooling;
- real wall-clock timestamps were captured;
- a player agent failed, timed out, or hit quota;
- the judge continued locally after a player failure and the user allowed that continuation.

When included, keep it short:

- Player execution: real subagents or local continuation.
- Captured metrics: token usage, timestamps, or failure reason.
- Missing metrics: one sentence explaining why they were unavailable. Never estimate tokens.
