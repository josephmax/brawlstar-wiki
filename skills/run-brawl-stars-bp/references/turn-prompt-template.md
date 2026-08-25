# Turn Prompt Template (Canonical)

This file is the single source of truth for every player-agent prompt in a BP match. The judge copies this template verbatim per turn and fills only the 对局信息 (match-info) block. Nothing else is added: no strategy hints, no query suggestions, no analysis of the opponent, no reasoning prompts. The player agent runs `brawl-stars-bp-slot-decision` on its own.

## Why this shape

- The decision skill's context input is exactly one layer: match information. Everything else (environment evidence, mechanism facts, brawler/map pages, skill references) is retrieved by the skill itself.
- Any judge-added reasoning ("you need to answer X", "check bucket Y", "think about Z") is duplicated decision logic and degrades both speed and quality. It is forbidden.
- The output contract is deliberately two-lane to keep every turn fast and cheap:
  - **返回给裁判（每手）**：只回 `decision` + `key_reason`（每项一句最强依据）+ `confidence` + `retrieval`（一行）。上下文最小化，不展开未选理由。
  - **选手日志（每手）**：详细思考过程全部**追加写入本侧选手日志文件** `{PLAYER_LOG_PATH}` —— 本手查了哪些选项、为什么查（`why_examined`）、证据（`evidence_used`）、查验结果排序、verdict、被否决/推迟项。裁判整局结束后分别读取蓝/红两份日志，据此汇总 verbose decision log。日志是唯一完整思考记录，选手不得只在回复里简述。
- 这样每手决策只生成几行文本（快、省 token），而完整审计不丢失：它落在选手日志里，由裁判在最后一次性读取汇总，不需要选手在每手或 final review 重复叙述。

## Player-agent spawn prompt (turn 1: ban phase)

```text
你是《荒野乱斗》Ranked BP 模拟的{蓝方|红方}选手（贯穿整局），使用本仓库的 `brawl-stars-bp-slot-decision` skill 做 BP 推理。工作目录：{REPO_ROOT}。

【对局信息】
- 地图: {MAP}
- 模式: {MODE}
- 阵营: {blue|red}
- 策略偏置: {bias}（本局固定不变）
- 本手: ban 阶段（{3} ban）
- 已 ban: 无（同时禁用，双方互相不可见）
- 不可用池: 无
- 已选: 无
- runtime index: {INDEX_PATH}（已编译，覆盖本图）
- 环境证据: 内嵌于 runtime index（`environment_evidence`，含 `ladder_anchor` / `monthly_finals`），经 hydrate_runtime_facts.py 读取；不存在独立环境工具
- 跨手缓存目录: {CACHE_DIR}（整局复用；query/hydrate 传 --cache-dir，同参数查询命中缓存，环境证据随 index 缓存，hydrate 批量用重复 --include-id + --summary）
- 选手日志: {PLAYER_LOG_PATH}（每手决策完成后，把详细思考过程【追加】写入此文件：查验了哪些选项、每项为什么被查、关键证据、查验结果排序、verdict 与一句理由；裁判整局结束后读取此文件生成详细决策日志）

【要求】
使用 `brawl-stars-bp-slot-decision` skill 的 decide 模式完成本手决策。按 skill 自身流程检索与推理。每手决策后先追加选手日志，再返回精简 trace。

【输出契约（精简 trace）】
yaml:
  side: {blue|red}
  slot: ban|slot1|slot2_3|slot4_5|slot6
  strategy_bias: {bias}
  decision: 3 个 ban 英雄列表
  key_reason: 每 ban 的关键理由（一句，机制或环境最强依据）
  side_asymmetric_ban_strategy: 一句（first_pick_initiative / last_counter_leverage 视角的 ban 目标）
  confidence: high|medium|medium-low|low
  retrieval: 一行概括实际查询
详细思考过程已写入 {PLAYER_LOG_PATH}，本手不在此展开。
用中文。
```

## Turn prompt for pick turns (slots 1-6)

Same template, with the 对局信息 block updated:

```text
你是本局{蓝方|红方}选手，继续使用 `brawl-stars-bp-slot-decision` skill 完成本手决策。

【对局信息】
- 地图: {MAP}
- 模式: {MODE}
- 阵营: {blue|red}
- 策略偏置: {bias}（本局固定不变）
- 本手: {blue slot 1 | red slots 2-3 | blue slots 4-5 | red slot 6}
- 已 ban: 我方 {list} / 对方 {list}
- 不可用池: {unique union of both bans}
- 已选: 我方 {list} / 对方 {list}
- runtime index: {INDEX_PATH}
- 环境证据: 内嵌于 runtime index（`environment_evidence`，含 `ladder_anchor` / `monthly_finals`），经 hydrate_runtime_facts.py 读取；不存在独立环境工具
- 跨手缓存目录: {CACHE_DIR}（整局复用；query/hydrate 传 --cache-dir，同参数查询命中缓存，环境证据随 index 缓存，hydrate 批量用重复 --include-id + --summary）
- 选手日志: {PLAYER_LOG_PATH}（每手决策完成后，把详细思考过程【追加】写入此文件：查验了哪些选项、每项为什么被查、关键证据、查验结果排序、verdict 与一句理由；裁判整局结束后读取此文件生成详细决策日志）

【要求】
使用 `brawl-stars-bp-slot-decision` skill 的 decide 模式完成本手决策。按 skill 自身流程检索与推理。每手决策后先追加选手日志，再返回精简 trace。

【输出契约（精简 trace）】
yaml:
  side: {blue|red}
  slot: slot1|slot2_3|slot4_5|slot6
  strategy_bias: {bias}
  decision: pick 英雄列表
  key_reason: 每 pick 的关键理由（一句，机制或环境最强依据）
  confidence: high|medium|medium-low|low
  retrieval: 一行概括实际查询
详细思考过程已写入 {PLAYER_LOG_PATH}，本手不在此展开。
用中文。
```

## What the judge must never add

- ❌ "先读 SKILL.md 的 X 章节"（skill 自己会读）
- ❌ "查 bucket Y / 用 --include-id Z"（查询策略是 skill 的职责）
- ❌ "你需要应对对方的 X"（阵型诊断是 skill 的职责）
- ❌ "你的反制池还剩..."（side-local memory 是 player 自己的）
- ❌ "思考：..." 或任何推理引导
- ❌ 上一手对方的 trace / report_summary / audit（`visible_state_only_between_players`）

The judge passes only what is in the 对局信息 block, plus the fixed 要求 and 输出契约 sections.

## Match-scoped player lifecycle

- Spawn two player agents before the ban phase (blue and red). Reuse the same agent for that side's ban, all pick turns, and final review (`send_message` continuation for later turns).
- Assign `strategy_bias` once at spawn; repeat it unchanged in every later prompt.
- Ban phase: prompt both agents in parallel, revealing no bans. After both return, merge: `unavailable = unique(blue_bans + red_bans)`.
- Pick order is strict: blue slot 1 → red slots 2-3 → blue slots 4-5 → red slot 6. Each later turn sees only public bans, picks, and the unavailable pool.
- After slot 6, run final_draft_review on the same two agents (cannot change picks).
- Do not expose one player's hidden reasoning to the other.

## Judge operation steps (standalone runnable)

Follow these steps exactly; they do not depend on any prior conversation.

1. **Prepare**: ensure the runtime index exists for the map (run `skills/brawl-stars-bp-slot-decision/scripts/compile_runtime_index.py --repo . --output <path>` if missing). Record `INDEX_PATH`.
2. **Match config**: choose map/mode (from `wiki/syntheses/Ranked-Season-47-地图Map-Profile总览.md` for the current pool), assign `strategy_bias` per side (random or user-specified), record both.
3. **Spawn**: create two player agents (blue, red) using the spawn prompt above with the 对局信息 block filled. Spawn both before the ban phase.
4. **Ban phase**: send the spawn prompt to both agents in parallel. Do not reveal bans between them. After both return, compute `unavailable = unique(blue_bans + red_bans)` and record duplicated bans.
5. **Pick order** (strict, using the pick-turn prompt with updated 对局信息 each time):
   - blue slot 1: sees unavailable pool, no picks yet.
   - red slots 2-3: sees unavailable + blue slot 1 pick.
   - blue slots 4-5: sees unavailable + blue slot1 + red picks 2-3.
   - red slot 6: sees unavailable + all five picks.
6. **Final review**: after slot 6, send both agents a final_draft_review request (win condition, play pattern, risks, mitigation, role/build plan). Cannot change picks. Each side also appends its final review to its own player log.
7. **Report**: assemble the human report per `match-report-schema.md`, copying player-submitted summaries (the lean per-turn traces plus the player logs). Then read both player logs (`{PLAYER_LOG_PATH}` blue and red) and assemble the verbose `.decision-log.md` from the per-turn examined_options, verdicts, and retrieval audit recorded there. The judge copies/normalizes the logs; it does not reconstruct decisions.

## Player log contract

- Path: the judge assigns one side-local log file per player at spawn, e.g. `outputs/bp-simulations/match-<map>.blue.player-log.md` and `...red.player-log.md`. The path is passed in every 对局信息 block.
- Content per turn: append a section for each own turn (ban / slot1 / slot2_3 / slot4_5 / slot6) with `decision`, `key_reason`, `side_asymmetric_ban_strategy` (ban only), `confidence`, `retrieval`, and the full `examined_options` list — every option seriously inspected, with `why_examined`, `evidence_used`, `verdict` (selected/rejected/deferred), `verdict_reason`, and the ranking order in which they were considered. The log may also record the full reasoning depth of the standalone trace, including `evidence_roles` (mechanism / ladder_anchor / monthly_finals / environment_unverified) and `bias_effect` (which candidates the strategy bias excluded or prioritized). Also append the final review.
- The player log is the only place the full thinking process is recorded. The player must write it every turn (append, never overwrite); the judge must not ask the player to repeat it in chat, and must not reconstruct it if the log is missing (mark `player_log_missing`).

## Complete worked example (ban phase prompt, blue side)

```text
你是《荒野乱斗》Ranked BP 模拟的蓝方选手（贯穿整局），使用本仓库的 `brawl-stars-bp-slot-decision` skill 做 BP 推理。工作目录：/Users/bytedance/Desktop/stock/vaults/brawlstar。

【对局信息】
- 地图: Belle's Rock
- 模式: Knockout
- 阵营: blue
- 策略偏置: conservative（本局固定不变）
- 本手: ban 阶段（3 ban）
- 已 ban: 无（同时禁用，双方互相不可见）
- 不可用池: 无
- 已选: 无
- runtime index: /tmp/rt-final.json（已编译，覆盖本图）
- 环境证据: 内嵌于 runtime index（`environment_evidence`，含 `ladder_anchor` / `monthly_finals`），经 hydrate_runtime_facts.py 读取；不存在独立环境工具
- 跨手缓存目录: /tmp/bp-cache-blue（整局复用；query/hydrate 传 --cache-dir，同参数查询命中缓存，环境证据批量用 --hero x N + --summary）
- 选手日志: /tmp/bp-cache-blue/player-log.md（每手决策完成后，把详细思考过程【追加】写入此文件：查验了哪些选项、每项为什么被查、关键证据、查验结果排序、verdict 与一句理由；裁判整局结束后读取此文件生成详细决策日志）

【要求】
使用 `brawl-stars-bp-slot-decision` skill 的 decide 模式完成本手决策。按 skill 自身流程检索与推理。每手决策后先追加选手日志，再返回精简 trace。

【输出契约（精简 trace）】
yaml:
  side: blue
  slot: ban
  strategy_bias: conservative
  decision: 3 个 ban 英雄列表
  key_reason: 每 ban 的关键理由（一句）
  side_asymmetric_ban_strategy: 一句
  confidence: high|medium|medium-low|low
  retrieval: 一行概括实际查询
详细思考过程已写入 /tmp/bp-cache-blue/player-log.md，本手不在此展开。
用中文。
```

A pick-turn prompt differs only in the 对局信息 block: 已 ban / 不可用池 / 已选 are filled with current public state, and 本手 becomes the slot name.
