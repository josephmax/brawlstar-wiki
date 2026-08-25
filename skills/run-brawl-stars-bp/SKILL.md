---
name: run-brawl-stars-bp
description: Use when running Brawl Stars Ranked BP simulations, judge-led red/blue drafts, batch map matches, tournament-style ban/pick reports, or subagent player coordination from this vault.
---

# Run Brawl Stars BP

## Core Principle

Act as a neutral_recorder and deal_cards_only coordinator, not a drafter, analyst, coach, or evaluator. The judge owns orchestration, hidden-state discipline, simultaneous bans, randomize_strategy_bias assignment before spawning players, turn prompts, metrics capture when tooling exposes it, and neutral human_readable_report assembly. Player agents use `brawl-stars-bp-slot-decision` for all BP reasoning.

Use `no_judge_draft_evaluation`: do not judge whether a ban/pick is good, do not add matchup analysis, do not repair player logic, and do not decide the favored side. Record player conclusions and reasons as submitted.

Read `references/match-report-schema.md` before writing a match report or prompting player agents. Use `scripts/render_match_report.py` when a durable report is requested; it is the fixed Markdown template.

There is no judge-side deterministic drafter in the 0.x tool contract. To run a simulated match, the judge coordinates match-scoped player subagents through `brawl-stars-bp-slot-decision`; that player-side skill queries `runtime_bp_index` only through `query_runtime_facts.py` and `hydrate_runtime_facts.py`. Scripts may coordinate state and render reports, but they must not choose bans/picks or emit decision-shaped fields on behalf of the player.

Use `no_judge_local_continuation`: do not replace a player subagent with the judge/current LLM for normal simulations. Local continuation is allowed only for an explicitly labeled smoke test when the user permits it. If the user requires subagents and player-agent quota or tooling is unavailable, stop with a partial/failure report instead of finishing the draft locally.

When the user needs a decision audit, keep it separate from the human match report. The audit should record each ban/pick turn's visible input state, neutral fact-tool calls, retrieved map/entity/relation fact summaries, and the player-authored reasoning that converted those facts into a choice. Do not log or expect tool-produced `judgment_brief`, `candidate_shortlist`, `capability_gate`, `ban_purposes`, or final recommendations; those are LLM-authored reasoning artifacts when present.

The primary decision audit section must be `decision_audit_narrative`: Chinese causal prose, not a raw parameter dump. It should answer the user's practical questions before any table appendix:

- Ban phase: "红/蓝方因为决策风格是 X，地图是 Y，先按自己的 `side_asymmetric_ban_strategy` 判断 slot 权力；蓝方围绕 `first_pick_initiative` 保护 1 楼先机，红方围绕 `last_counter_leverage` 保留 6 楼 counter 杠杆；随后发起 ban位压力查询前12个热门英雄；召回规模是 N fragments / K KB；考虑到地图目标、关键威胁、可回答性和自身风格，最后选出了 A、B、C。"
- Pick turns: "后手/先手 X 楼根据已知的 bans、已选英雄和完整不可用池，针对性地查询了某类事实窗口，并用 `exclude-id` / `relation-target` 表达可见状态；召回 N 个候选 / K KB；在候选中考虑地图职责、关系边、失败模式、配装要求和 strategy_bias 后，最后选出了 A 或 A+B。"
- Final draft: "6 个位置都选出完毕后，红/蓝方根据已知完整阵容，确认获胜条件和打法为 X，主要风险为 Y，对应出装为 Z。"

Every turn's narrative must also enumerate `examined_options` from the player log: 本手查验了哪些选项、每个选项为什么进入候选池（`why_examined`）、被什么证据评判（`evidence_used`）、最终 verdict 与一句理由，以及查验顺序（ranking）。This is the decision-optimization surface: it shows the examined set and the reason each option was looked at, not just the final choice. The full list lives in the player log — per-turn traces intentionally do not carry it. If a player did not record `examined_options` in the log, mark the audit as incomplete instead of reconstructing the list.

Tables may follow as evidence appendix, but the audit must not rely on truncated return snippets. Include every turn's query focus, recalled candidate count, `fragments_returned`, `payload_kb`, and a short summary of recalled entity/relation information.

The narrative must be sourced from player-submitted lean per-turn traces (`decision` + `key_reason` + `confidence` + `retrieval`) plus each side's **player log** (`{PLAYER_LOG_PATH}`, appended every turn with the full `examined_options` and retrieval audit) and `post_draft_review` / `final_draft_review`, not reconstructed by the judge after the fact. The judge reads both player logs after the match and assembles the verbose `.decision-log.md` from them. If a player did not submit those fields or the log is missing, mark the audit as incomplete (`player_log_missing`) instead of filling the gap.

## Required Inputs

Before normalizing match config or relaying ban/pick state, resolve user-facing brawler names through `wiki/concepts/英雄名称归一化.md`; do not copy or maintain a local alias table. Ambiguous names from that page require confirmation rather than judge-side repair.

Normalize each match:

```yaml
match_config:
  map:
  mode:
  blue_model:
  red_model:
  blue_subagent_id:
  red_subagent_id:
  blue_strategy_bias: conservative | balanced | aggressive | high_variance | random
  red_strategy_bias: conservative | balanced | aggressive | high_variance | random
  ban_count_per_side: 3
  pick_order: [blue_slot1, red_slot2_3, blue_slot4_5, red_slot6]
  output_path:
```

If the user does not specify models, record the actual model if visible; otherwise write `unknown_model_in_current_environment`. If the user does not specify strategy bias, randomly assign one per side before bans and record it. Use the exact assigned value in every prompt for that side. Use `balanced` only when the user explicitly asks for deterministic or balanced runs.

## Player Agent Lifecycle

For every simulated match, create exactly two match-scoped player subagents before the ban phase: one blue player and one red player. Each player subagent lives for the whole match and is reused for that side's ban, pick turns, and final draft review. Close both player subagents after the match report and decision log are assembled.

- Do not spawn a fresh player for each turn; that loses side-local memory and weakens the game-theoretic simulation.
- Do not reuse a player subagent across different matches; a new match gets new blue/red players and new hidden state.
- Assign `strategy_bias` once before spawning each player. Pass it in the initial prompt and repeat it unchanged in every later turn prompt.
- Pass the default `decision_effort_policy` at spawn, including the slot baseline table and strategy-bias adjustment rules. Later prompts may state the current slot baseline, but must not redefine the player's style.
- The judge may keep subagent ids, timestamps, and failure states in `match_metrics`; do not expose one player's hidden reasoning to the other player.
- If a player subagent fails mid-match, record the failure for that side. Do not silently replace it with another agent unless the report marks the replacement and the new agent receives only visible state plus that side's already locked public picks/bans.

## Judge Workflow

1. Read `references/match-report-schema.md` and the user-provided match list/config. Do not read map, brawler, matchup, or BP runtime pages to form your own BP opinion.
2. Start `match_metrics`: wall-clock time, judge model, player model names if visible, and subagent ids.
3. Spawn the match-scoped blue and red player subagents with fixed `strategy_bias`, the runtime-index path, and default effort policy.
4. Run `simultaneous_ban_phase` by prompting both match-scoped player subagents in parallel without revealing the other side's bans.
5. Run pick turns in strict order on the same two player subagents: blue slot 1, red slots 2-3, blue slots 4-5, red slot 6.
6. Run `post_draft_review` on the same two player subagents after all six picks are locked. This cannot change picks; it confirms full-draft win condition, play pattern, risks, mitigation, and role/build plan. Each side also appends its final review to its own player log.
7. Read both player logs (`{PLAYER_LOG_PATH}` for blue and red) — the full per-turn `examined_options`, verdicts, retrieval audit, and final review recorded there.
8. Write the match report using the human Markdown template by copying, normalizing, and lightly formatting player-submitted conclusions. Assemble the verbose `.decision-log.md` from the player logs. Do not add independent BP analysis.
9. Close both match-scoped player subagents and record closure/failure in metrics when available.
10. Update `wiki/index.md` and `wiki/log.md` when reports are durable wiki artifacts.

## simultaneous_ban_phase

Ban phase is simultaneous.

- Prompt the already-spawned blue and red match-scoped player subagents without revealing the other side's bans.
- Enforce `no_sequential_ban_information`: neither side can see the other side's bans before submitting all ban slots.
- Require each side to submit `side_asymmetric_ban_strategy` in its ban trace. Blue must reason from `first_pick_initiative`, including `protect_first_pick` and `ban_overlap_risk`; red must reason from `last_counter_leverage`, including `deny_blue_safe_opener` and `preserve_red6_counter_pool`.
- Do not normalize both sides into the same "top map power" ban objective. The judge passes the side and slot-power framing to the player, but the player still uses neutral fact tools and writes the interpretation itself.
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

**Use the canonical template in `references/turn-prompt-template.md` verbatim for every player-agent prompt.** Fill only the 对局信息 (match-info) block; keep the 要求 and 输出契约 sections fixed. Do not add strategy hints, query suggestions, opponent analysis, or reasoning prompts to the template.

The input layer to the player is exactly one thing: match information. Everything else — environment evidence, mechanism facts, skill references — is retrieved by `brawl-stars-bp-slot-decision` itself. Judge-added reasoning duplicates the skill's job and is forbidden.

Every player-agent prompt must include:

- map, mode, side, global slot, current picks, own bans, enemy bans, unavailable pool
- `strategy_bias`; style_bias_assigned_at_spawn, then left fixed for that player. The judge must choose this before the player sees the prompt.
- `decision_effort_policy`: normal runtime effort has only `low=24` and `high=32`. The judge provides the slot baseline and the fixed `strategy_bias`; the player chooses the final effort or explicit per-hand `--limit` while keeping fact tools neutral.
- any user-provided environment/meta context (high-rank pickrate data if supplied); otherwise the player relies on its own BP skill process and marks the environment slot as empty
- the fixed output schema from the canonical template (精简 trace: decision / key_reason / confidence / retrieval). 决策阶段每手只返回选中项与关键理由；详细思考过程（examined_options 全量、查验排序、证据、verdict）追加写入选手日志 `{PLAYER_LOG_PATH}`，裁判整局结束后读取双方日志生成详细 decision log。

Do not ask red slot 2-3 before blue slot 1 is known. Do not ask blue slot 4-5 before red slot 2-3 is known. Do not ask red slot 6 before blue slot 4-5 is known.

Use `visible_state_only_between_players`: the next player sees only public bans, public picks, unavailable pool, map/mode, fixed strategy settings, and user-provided constraints. Do not pass previous-turn `report_summary`, `priority_factors`, `candidate_comparison`, `selected_reason`, hidden plans, or audit narrative to the other side. A player subagent may remember its own prior hidden reasoning because it lives for the match, but that memory is side-local.

Use `do_not_validate_style_compliance`: after the player returns, do not score whether it behaved conservative/aggressive/high-variance enough. Record the assigned bias in the header and the returned decision in the turn body.

Default slot effort baseline:

| turn | effort |
| --- | --- |
| ban phase | `low` |
| blue slot 1 | `low` |
| red slots 2-3 | `low` |
| blue slots 4-5 | `high` |
| red slot 6 | `high` |
| post draft review | selected hydration only |

Strategy bias may raise but should not hide the slot baseline: `conservative` and `balanced` keep the baseline; `aggressive` uses `high` for ban, blue 4-5, red 6, and route / punish probes; `high_variance` uses `high` for all broad fact windows. The player may still set an explicit query `--limit` for a single hand when it needs finer recall control.

## post_draft_review

After red slot 6 returns, ask both sides for a `final_draft_review` using the complete visible draft. The judge may pass full picks, bans, unavailable pool, map, mode, and that side's selected brawlers. The review must return:

- `full_draft_read`
- `win_condition`
- `play_pattern`
- `primary_risks`
- `risk_mitigation`
- `role_build_plan` for every selected brawler
- `cannot_change_picks: true`

This review cannot change picks, bans, or previous decisions. If a review is missing, the final report and decision log must say `final_draft_review_missing`; do not synthesize it from judge-side analysis.

## Player Log Contract

Each player gets a side-local log file at spawn (`{PLAYER_LOG_PATH}`, e.g. `outputs/bp-simulations/match-<map>.blue.player-log.md` / `...red.player-log.md`), passed in every 对局信息 block. The player appends a section per own turn (ban / slot1 / slot2_3 / slot4_5 / slot6) with `decision`, `key_reason`, `side_asymmetric_ban_strategy` (ban only), `confidence`, `retrieval`, and the full `examined_options` list — every option seriously inspected with `why_examined`, `evidence_used`, `verdict`, `verdict_reason`, and the ranking order in which they were considered — plus the final review. The player log is the only place the full thinking process is recorded: it is written every turn (append, never overwrite), and the judge must not ask the player to repeat it in chat. After the match the judge reads both logs and assembles the verbose `.decision-log.md`. If a log is missing or a field is absent, mark `player_log_missing` / `examined_options_missing` instead of reconstructing.

## Strategy Bias Assignment

Bias is a player prompt parameter, not a judge scoring rubric.

| bias | Use when | Candidate preference |
| --- | --- | --- |
| `conservative` | robust baseline or ladder-safe drafts | stable duties, low exposure, flexible builds, fewer all-in tanks/assassins |
| `balanced` | deterministic baseline or user-requested balanced simulation | map duties first, then matchup and comp context |
| `aggressive` | pressure-testing answers | route-based engage, last-pick punish, tank/assassin if support and escape conditions exist |
| `high_variance` | data diversity / stress tests | allows volatile picks when failure modes are explicit and not hard-gated |

When batch-running maps, randomize biases across matches unless the user specifies otherwise. Record both side biases in `对局摘要`. Do not hide or later change the assigned bias.

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

If exact token usage is unavailable, say so directly only in `执行元数据` when a metadata section is otherwise useful. Never estimate tokens. Do not add per-turn token rows full of `null`.

## Report Assembly

The final report is Chinese human-facing Markdown, not a raw log. It must contain:

- 对局摘要
- 禁用阶段
- 选择时间线
- 玩家最终陈述
- 稳定知识引用
- optional 执行元数据

Do not include YAML blocks, raw structured logs, `match_header`, `Final Draft Evaluation`, `Draft Evaluation`, `favored_side`, judge-side lane/win analysis, duplicate-ban callouts, generic local-run uncertainty, judge notes, or sequence filler. The report should show both sides' ban slots, but it should not spend attention on whether bans duplicated.

Human report prose must use Chinese concepts. Do not print internal map hook ids, failure ids, build ids, `construct_direction`, `why_now`, score fields, or underscore-heavy runtime labels in the report. Those remain in `.decision-log.md`.

In `玩家最终陈述`, include per-brawler role/build notes: each selected brawler gets a short responsibility sentence and the star power / gadget / gear direction that supports that responsibility. This comes from the player-side `report_summary` and `build_summary`; the judge may format it but must not add independent analysis.

Use `state_handoff_to_next_turn` for visible state passed forward. The handoff may say what is now visible and which structural questions remain open; it must not interpret another player's hidden intention or recommend the next pick. During the match, the next player sees only visible picks, bans, and unavailable pool; do not pass prior player `report_summary`, `priority_factors`, `construct_direction`, or audit reasons as input. Those reasons are for the final report and decision log only.

## Failure Rules

- If a player agent fails, times out, or hits quota, mark that turn as `judge_continuation_after_player_failure` and explain why.
- Do not backfill missing player decisions as if they came from a player.
- If player-agent quota is unavailable and the user required subagents, stop after writing partial reports or ask to resume after quota resets.
- If continuing locally is explicitly allowed for a smoke test, clearly label local turns in `turn_metrics.actor`; otherwise do not replace player reasoning with judge reasoning.
- Always close match-scoped player subagents after the match is complete, failed, or abandoned. If closing fails or is unavailable, record the cleanup failure in execution metadata rather than silently ignoring it.
