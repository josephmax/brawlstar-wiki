# Human BP Match Report Template

Use this Chinese template for every `match-<map>.md` report. The report is for humans, not parsers.

Hard rules:

- Write plain Markdown only. Do not use YAML blocks, JSON blocks, raw structured logs, or `match_header`.
- Do not include `favored_side`, win probability, confidence score, judge-side draft evaluation, or any side preference.
- Do not include token tables full of `null`. Add `执行元数据` only when real metrics or a real failure state was captured.
- Record both `strategy_bias` values in `对局摘要`.
- Use `state_handoff_to_next_turn`, not pressure language. The handoff may state visible facts and open structural questions, but must not tell the next player what to pick.
- Copy, normalize, and lightly format player-submitted report summaries. Do not add independent BP analysis.
- 选择时间线 content (选择摘要 / 关键因素 / 主要风险 / 构筑提示 / 查验选项) comes from each side's player log (`{PLAYER_LOG_PATH}`, appended per turn with the full `examined_options`), which the judge reads after the match — not from per-turn traces, which are intentionally lean (`decision` / `key_reason` / `confidence` / `retrieval`). If a player log entry lacks a field, write `examined_options_missing` instead of reconstructing.
- `玩家最终陈述` must come from player-submitted `post_draft_review` / `final_draft_review` after all six picks are locked. If it is missing, write `final_draft_review_missing` instead of synthesizing win condition, risks, or builds from judge-side reasoning.
- Keep audit detail out of the human report. Fields such as `construct_direction`, `why_now`, candidate shortlists, `missing_required_capabilities`, and `adjudication` details belong in `.decision-log.md`.
- Human reports must use Chinese concept summaries, not raw runtime ids. Do not print underscore-heavy labels such as map hook ids, failure ids, or build ids in the report.
- Do not expose prior player reasoning during the match. The next turn receives visible picks, bans, and unavailable pool only; report summaries are final-report material, not turn input.

## 对局摘要

Start every report with:

- 地图 / 模式.
- 蓝方 and 红方 strategy bias.
- 禁用格式: simultaneous bans.
- 选择顺序.
- 最终阵容.

## 禁用阶段

Use two short lists:

### 蓝方禁用

For each ban:

- `Brawler`: player-submitted report summary; two or three priority factors; one risk summary.

Optionally (when the player recorded the audit inventory in its player log's ban entry), show the ban hand's `examined_options`（查验选项）: every candidate examined during the ban turn, why each was examined, and the verdict. If present, render it as a compact list; if missing, write `examined_options_missing` instead of reconstructing.

### 红方禁用

Same shape as 蓝方禁用.

End the section with:

- Unavailable pool after bans.

## 选择时间线

Use one subsection per pick turn:

### 蓝方 1 楼 - `Pick`
### 红方 2-3 楼 - `Pick + Pick`
### 蓝方 4-5 楼 - `Pick + Pick`
### 红方 6 楼 - `Pick`

Each subsection must include:

- Visible state: own picks, enemy picks, unavailable pool.
- Player submitted `report_summary`（from the player log per-turn entry）.
- Player submitted `priority_factors`.
- Player submitted `risk_summary`.
- Player submitted `build_summary`.
- Player submitted `examined_options` (查验选项, from the player log): for each option examined this hand, its `why_examined`（为什么查它）, `evidence_used`（评判证据）, `verdict`（selected/rejected/deferred）and one-line `verdict_reason`, in the player's recorded ranking order. This is the decision-optimization surface: it shows the examined set and why each option was looked at, not just the final pick. If the player did not record `examined_options` in the log, write `examined_options_missing` instead of reconstructing the list.
- Rejected options and the player-submitted reason, if present (derivable from `examined_options` with `verdict: rejected`).

## 玩家最终陈述

Record only what players submitted:

### 蓝方

- Comp.
- Submitted `final_draft_review.win_condition`.
- Submitted `final_draft_review.play_pattern`.
- Submitted `final_draft_review.primary_risks`.
- Submitted `final_draft_review.risk_mitigation`.
- Submitted `final_draft_review.role_build_plan` for each brawler. Each note should explain this brawler's job in the match and the star power / gadget / gear direction that supports that job.

### 红方

Same shape.

## 稳定知识引用

Copy refs from player submissions when available. Do not invent refs during report writing.

## 执行元数据

Omit this section unless at least one of these is true:

- real token usage was captured by tooling;
- real wall-clock timestamps were captured;
- a player agent failed, timed out, or hit quota;

When included, keep it short:

- Player execution: real subagents or failure-handling continuation.
- Captured metrics: token usage, timestamps, or failure reason.
- Missing metrics: one sentence explaining why they were unavailable. Never estimate tokens.
