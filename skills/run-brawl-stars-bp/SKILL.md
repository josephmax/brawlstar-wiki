---
name: run-brawl-stars-bp
description: Use when running Brawl Stars Ranked BP simulations, judge-led red/blue drafts, batch map matches, tournament-style ban/pick reports, or subagent player coordination from this vault.
---

# Run Brawl Stars BP

## Core Principle

Act as a neutral_recorder and deal_cards_only coordinator, not a drafter, analyst, coach, or evaluator. The judge owns orchestration, hidden-state discipline, simultaneous bans, randomize_strategy_bias assignment before spawning players, turn prompts, metrics capture when tooling exposes it, and neutral human_readable_report assembly. Player agents use `brawl-stars-bp-slot-decision` for all BP reasoning.

Use `no_judge_draft_evaluation`: do not judge whether a ban/pick is good, do not add matchup analysis, do not repair player logic, and do not decide the favored side. Record player conclusions and reasons as submitted.

Read `references/match-report-schema.md` before writing a match report or prompting player agents. Use `scripts/render_match_report.py` when a durable report is requested; it is the fixed Markdown template.

## Required Inputs

Before normalizing match config or relaying ban/pick state, resolve user-facing brawler names through `wiki/concepts/英雄名称归一化.md`; do not copy or maintain a local alias table. Ambiguous names from that page require confirmation rather than judge-side repair.

Normalize each match:

```yaml
match_config:
  map:
  mode:
  blue_model:
  red_model:
  blue_strategy_bias: conservative | balanced | aggressive | high_variance | random
  red_strategy_bias: conservative | balanced | aggressive | high_variance | random
  ban_count_per_side: 3
  pick_order: [blue_slot1, red_slot2_3, blue_slot4_5, red_slot6]
  output_path:
```

If the user does not specify models, record the actual model if visible; otherwise write `unknown_model_in_current_environment`. If the user does not specify strategy bias, randomly assign one per side before bans and record it. Use the exact assigned value in every prompt for that side. Use `balanced` only when the user explicitly asks for deterministic or balanced runs.

## Judge Workflow

1. Read `references/match-report-schema.md` and the user-provided match list/config. Do not read map, brawler, matchup, or BP runtime pages to form your own BP opinion.
2. Start `match_metrics`: wall-clock time, judge model, player model names if visible, and subagent ids.
3. Run `simultaneous_ban_phase`.
4. Run pick turns in strict order: blue slot 1, red slots 2-3, blue slots 4-5, red slot 6.
5. Write the match report using the human Markdown template by copying, normalizing, and lightly formatting player-submitted conclusions. Do not add independent BP analysis.
6. Update `wiki/index.md` and `wiki/log.md` when reports are durable wiki artifacts.

## simultaneous_ban_phase

Ban phase is simultaneous.

- Spawn or prompt blue and red ban decisions without revealing the other side's bans.
- Enforce `no_sequential_ban_information`: neither side can see the other side's bans before submitting all ban slots.
- Red and blue bans may duplicate. Do not repair duplicates into unique global bans.
- After both sides return, combine bans as:

```yaml
ban_phase:
  blue_bans: []
  red_bans: []
  duplicated_bans: []
  unavailable_pool: unique(blue_bans + red_bans)
```

Use the unique set only for later pick availability. Preserve duplicate bans in the report because duplicate bans are a meaningful signal.

## Turn Prompt Contract

Every player-agent prompt must include:

- map, mode, side, global slot, current picks, own bans, enemy bans, unavailable pool
- `strategy_bias`; style_bias_assigned_at_spawn, then left fixed for that player. The judge must choose this before the player sees the prompt.
- any user-provided strength/meta context; otherwise tell the player to determine or mark `unknown` through its own BP skill process
- the fixed output schema for this exact turn
- metrics request: token usage only if visible; otherwise wall-clock time and failure state if available. Do not force null token tables into the final report.

Do not ask red slot 2-3 before blue slot 1 is known. Do not ask blue slot 4-5 before red slot 2-3 is known. Do not ask red slot 6 before blue slot 4-5 is known.

Use `do_not_validate_style_compliance`: after the player returns, do not score whether it behaved conservative/aggressive/high-variance enough. Record the assigned bias in the header and the returned decision in the turn body.

## Strategy Bias Assignment

Bias is a player prompt parameter, not a judge scoring rubric.

| bias | Use when | Candidate preference |
| --- | --- | --- |
| `conservative` | robust baseline or ladder-safe drafts | stable duties, low exposure, flexible builds, fewer all-in tanks/assassins |
| `balanced` | deterministic baseline or user-requested balanced simulation | map duties first, then matchup and strength context |
| `aggressive` | pressure-testing answers | route-based engage, last-pick punish, tank/assassin if support and escape conditions exist |
| `high_variance` | data diversity / stress tests | allows volatile picks when failure modes are explicit and not hard-gated |

When batch-running maps, randomize biases across matches unless the user specifies otherwise. Record both side biases in Match Summary. Do not hide or later change the assigned bias.

Suggested helper:

```python
from scripts.render_match_report import assign_strategy_bias

blue_strategy_bias = assign_strategy_bias()
red_strategy_bias = assign_strategy_bias()
```

## Metrics

For each turn, record all available metrics internally:

```yaml
turn_metrics:
  actor:
  model:
  started_at:
  ended_at:
  elapsed_ms:
  token_usage:
    input:
    output:
    total:
    unavailable_reason:
  evidence_metrics:
    files_read:
    pages_read_count:
    commands_run:
    index_hits_used:
```

If exact token usage is unavailable, say so directly only in Execution Metadata when a metadata section is otherwise useful. Never estimate tokens. Do not add per-turn token rows full of `null`.

## Report Assembly

The final report is human-facing Markdown, not a raw log. It must contain:

- Match Summary
- Ban Phase
- Draft Timeline
- Player Final Statements
- Stable Knowledge Refs
- optional Execution Metadata

Do not include YAML blocks, raw structured logs, `match_header`, `Final Draft Evaluation`, `Draft Evaluation`, `favored_side`, or judge-side lane/win analysis.

Use `state_handoff_to_next_turn` for visible state passed forward. The handoff may say what is now visible and which structural questions remain open; it must not interpret another player's hidden intention or recommend the next pick.

## Failure Rules

- If a player agent fails, times out, or hits quota, mark that turn as `judge_continuation_after_player_failure` and explain why.
- Do not backfill missing player decisions as if they came from a player.
- If player-agent quota is unavailable and the user required subagents, stop after writing partial reports or ask to resume after quota resets.
- If continuing locally is explicitly allowed, clearly label local turns in `turn_metrics.actor`; otherwise do not replace player reasoning with judge reasoning.
