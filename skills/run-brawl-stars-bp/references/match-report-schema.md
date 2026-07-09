# Human BP Match Report Template

Use this Chinese template for every `match-<map>.md` report. The report is for humans, not parsers.

Hard rules:

- Write plain Markdown only. Do not use YAML blocks, JSON blocks, raw structured logs, or `match_header`.
- Do not include `favored_side`, win probability, confidence score, judge-side draft evaluation, or any side preference.
- Do not include token tables full of `null`. Add `执行元数据` only when real metrics or a real failure state was captured.
- Record both `strategy_bias` values in `对局摘要`, plus `strength_weight` when present.
- Use `state_handoff_to_next_turn`, not pressure language. The handoff may state visible facts and open structural questions, but must not tell the next player what to pick.
- Copy, normalize, and lightly format player-submitted report summaries. Do not add independent BP analysis.
- `玩家最终陈述` must come from player-submitted `post_draft_review` / `final_draft_review` after all six picks are locked. If it is missing, write `final_draft_review_missing` instead of synthesizing win condition, risks, or builds from judge-side reasoning.
- Keep audit detail out of the human report. Fields such as `construct_direction`, `why_now`, candidate shortlists, `missing_required_capabilities`, and `adjudication` details belong in `.decision-log.md`.
- Human reports must use Chinese concept summaries, not raw runtime ids. Do not print underscore-heavy labels such as map hook ids, failure ids, or build ids in the report.
- Do not expose prior player reasoning during the match. The next turn receives visible picks, bans, and unavailable pool only; report summaries are final-report material, not turn input.

## 对局摘要

Start every report with:

- 地图 / 模式.
- 蓝方 and 红方 strategy bias.
- 强度权重 when present.
- 禁用格式: simultaneous bans.
- 选择顺序.
- 最终阵容.

## 禁用阶段

Use two short lists:

### 蓝方禁用

For each ban:

- `Brawler`: player-submitted report summary; two or three priority factors; one risk summary.

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
- Player submitted `report_summary`.
- Player submitted `priority_factors`.
- Player submitted `risk_summary`.
- Player submitted `build_summary`.
- Rejected options and the player-submitted reason, if present.

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
