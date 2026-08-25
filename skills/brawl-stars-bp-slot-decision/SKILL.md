---
name: brawl-stars-bp-slot-decision
description: Use when compiling or using a Brawl Stars Ranked Ban Pick runtime index, deciding a specific draft slot, evaluating bans or picks, comparing candidates, or checking map fit, hard gates, counter-picks, and strategy bias from this vault.
---

# Brawl Stars BP Slot Decision

## Core Boundary

This skill has two modes:

- `compile`: read stable entity facts plus the archived high-rank pickrate environment signals (`wiki/environment/current.json` pointer), then generate a `runtime_bp_index` with the environment evidence folded in as labeled per-brawler `environment_evidence`. There is no strength layer; the environment slot is `loaded` when the archive resolves and `empty` otherwise.
- `decide`: validate the compiled `runtime_bp_index`, query it through bundled tools, combine the returned fragments with current draft state and runtime decision rules, then return one ban or pick recommendation set.

The skill must not use the wiki's synthesis/topic discussion layer as a runtime dependency. Those pages are maintainer workspace, not player-facing knowledge. The skill is self-contained through its own references and stable entity pages.

## Mode Required Reads

### compile

Read:

- `skills/brawl-stars-bp-slot-decision/references/compile-knowledge.md`
- Relevant map pages under `wiki/entities/maps/`
- Relevant brawler pages under `wiki/entities/brawlers/`
- `wiki/concepts/英雄名称归一化.md` when user, judge, or external inputs contain brawler aliases, emoji, community nicknames, or non-canonical names

Output:

- `runtime_bp_index`

Use `scripts/compile_runtime_index.py` to generate a concrete runtime index:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/compile_runtime_index.py \
  --repo . \
  --map "Safe Zone" \
  --output outputs/runtime-bp-index/safe-zone-default.json
```

Use `scripts/bp_index.py` only as a locator for skill references and stable entity pages:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/bp_index.py \
  --repo . \
  --map "Safe Zone" \
  --brawler "Brock" \
  --enemy "Mortis" \
  --json
```

### decide

Read:

- `skills/brawl-stars-bp-slot-decision/references/runtime-decision-knowledge.md`
- The compiled `runtime_bp_index` through the neutral fact tools: `scripts/query_runtime_facts.py` and `scripts/hydrate_runtime_facts.py`
- Environment evidence embedded in the compiled index (per-brawler `environment_evidence`: `ladder_anchor` / `monthly_finals`, plus `environment_ladder` per-map rows), read through `hydrate_runtime_facts.py` as corroborating evidence for `evidence_roles` — never as a ranking or instruction
- Current BP state only as caller-side reasoning context. Convert unavailable entities to neutral `--exclude-id`, forced evidence targets to `--include-id`, and relation probes to `--relation-target` before calling tools.

Before deciding, run `runtime_index_precheck`. If no usable `runtime_bp_index` exists, acquire the compile lock and run a default `compile`; if another process is compiling the same index, poll with a bounded retry budget. Do not silently fall back to maintainer discussion pages.

Use the bundled precheck script for file/lock coordination:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/runtime_index_precheck.py \
  --repo . \
  --index-key "<runtime_index_key>" \
  --json
```

Interpret the status:

- `ready`: read `index_path` and continue `decide`.
- `compile_required`: this process owns `lock_path`; run `compile`, write `index_path`, then release the lock.
- `runtime_index_compile_failed`: stop and return failure instead of waiting forever or answering from memory.

After precheck returns `ready`, do not load the full JSON into the prompt. 工具只做事实召回：query tools must return compact map/entity facts, relation facts, source refs, and retrieval summaries. They must not output `judgment_brief`, `current_team_plan`, `candidate_shortlist`, `ability_gate`, `adjudication`, `ban_purposes`, `answers_enemy_picks`, or final recommendations.

Use the neutral fact-window tool first:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/query_runtime_facts.py \
  --index "<index_path>" \
  --map "Safe Zone" \
  --bucket response_pick \
  --effort low \
  --exclude-id "Brock" \
  --relation-target "8-Bit" \
  --json
```

`query_runtime_facts.py` uses neutral retrieval terms:

- `--include-id`: force an entity's facts into the returned fact window.
- `--exclude-id`: remove an entity from the returned fact window.
- `--relation-target`: return conditional relation facts involving that entity, without naming it as ally/enemy/counter/answer.
- `--bucket`: select a precompiled retrieval bucket by id. The id is an index partition, not a recommendation.
- `--effort`: recall budget preset. Use `low=24` for normal runtime decisions or `high=32` for high-leverage / high-uncertainty decisions; default is `low`.
- `--limit`: explicit override for returned entity fragments. Use only when the caller has a concrete reason to override `--effort`.
- `--summary`: emit an agent-readable summary table for debugging, audit drafting, or manual comparison. Prefer this over ad hoc `python3 -c` JSON parsing when the caller only needs to inspect candidates.
- `--cache-dir`: cross-query disk cache directory. Same index + parameters hit the cache (response carries `cache_hit: true`) and skip reloading the index. Reuse one cache dir across a whole match so repeated queries with the same map and parameters are served from disk. Applies to both `query_runtime_facts.py` and `hydrate_runtime_facts.py`; environment evidence travels inside the index and is cached with it.

For JSON consumers, read candidates from `runtime_fact_query.fact_window`. Each row includes map fit evidence, map hook IDs, matched capabilities, failure gates, build IDs, `runtime_card_counts`, and `relation_count` so callers do not need to sort or compare nested dictionaries. There is no strength or tier field anywhere in the fact window.

Hydrate details only for the few entities the LLM wants to inspect more deeply:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/hydrate_runtime_facts.py \
  --index "<index_path>" \
  --map "Safe Zone" \
  --include-id "Meg" \
  --include-id "Crow" \
  --json
```

Hydration JSON keeps `entities` as a dictionary keyed by brawler for backward compatibility, and also returns `entity_window` as a list for safe iteration. Each hydrated entity includes `relation_count`, `runtime_card_counts`, `retrieval_bucket_hits`, `candidate_map_fit`, `evidence_ref`, and `environment_evidence` (ladder / monthly dimensions folded in by compile; `null` dimension means `no_ladder_sample` / `no_monthly_sample`). The hydration body also carries `environment_ladder` (Legendary+ per-map rows for the current map, projected to the requested heroes). Use `--summary` when the caller wants a readable entity audit without writing parsing code.

Environment evidence is read from the compiled index only — hydrate several heroes in one call by repeating `--include-id`; there is no separate environment tool. When a hero's environment evidence was already hydrated in an earlier turn of the same match, reuse that result from context; do not re-query it.

There is no `--strength-weight` in this system: environment evidence is labeled corroboration, never a ranking, and map fit / matchup / failure evidence is the entire basis for candidate comparison.

## Input Contract

Normalize requests into one of these objects:

Before filling these objects, normalize brawler names through `wiki/concepts/英雄名称归一化.md`: canonical brawler page names pass through; `aliases` map automatically; `ambiguous` entries require user or judge confirmation instead of silent resolution.

```yaml
compile_input:
  patch_id:
  map_pool:
  available_brawlers:
  source_policy:
    read_stable_entities_only: true
```

Compile never takes a strength profile. When `wiki/environment/current.json` resolves, `manifest.pickrate_status` records `"loaded"` and the archived signals are folded into the index as labeled evidence; without it (or with `--no-environment`) the slot records `"empty"`. Environment evidence enters the index with provenance and still cannot change map fit or eligibility.

```yaml
decide_input:
  runtime_bp_index:
  map:
  mode:
  current_global_slot: 1 | 2 | 3 | 4 | 5 | 6
  draft_state:
    own_side:
    opposing_side:
    unavailable:
  candidate_pool:
  known_player_constraints:
  strategy_bias: conservative | balanced | aggressive | high_variance
```

If `map`, `mode`, or slot is missing, state the assumption. Ask only when the missing field changes the decision.

## Runtime Index Precheck

`decide` must not start from free-form wiki reads. It first checks whether the requested map, mode, pool, and patch are covered by a compiled runtime index.

Recommended index state files live under `outputs/runtime-bp-index/`:

```text
<runtime_index_key>.json
<runtime_index_key>.lock
```

The `runtime_index_key` should be derived from patch id, map pool id, available brawler pool, and environment slot status (`pickrate_status`). A supplied explicit `runtime_bp_index` can bypass file lookup if its manifest matches the current request.

Precheck behavior:

1. If a matching index exists and passes manifest validation, use it.
2. If no matching index exists, create `<runtime_index_key>.lock` with `state: compiling`, owner, and timestamp, then run `compile`.
3. If the lock already exists, do not start another compile. Poll for the matching index.
4. Poll at most 12 times, with a short delay between attempts. If the index appears and validates, continue `decide`.
5. If the lock is stale for more than 10 minutes, one process may replace it and retry compile once.
6. If bounded polling and stale-lock recovery fail, return `runtime_index_compile_failed` and stop. Do not answer from memory.

After a successful compile owned by this process, release the lock:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/runtime_index_precheck.py \
  --repo . \
  --index-key "<runtime_index_key>" \
  --release-lock \
  --json
```

## Compile Summary

`compile` converts stable facts into a tool-consumable runtime index:

- `map_pool_signature`: per-map `map_context`, per-slot map-evidence `candidate_projection`, and full-map `candidate_index` covering every available brawler. `candidate_projection` preserves all concrete map candidates for each legal slot; there is no strength ranking to cut against. `candidate_index` carries only map-evidence fields: `fit`, `map_floor_fit`, `mode_contract_fit`, `recall_channels`, `slot_eligibility`, `conditional_lift`, `failure_gates`, and `required_build_ids`.
- `brawler_runtime_cards`: global brawler capability, build, map hook, objective, failure, and slot-note fragments stored once for hydration.
- `matchup_index`: conditional matchup edges keyed by brawler for draft-state filtering.
- `evidence_refs`: source refs for map and brawler pages so detailed explanations can hydrate only the final shortlist.
- `audit_summary`: compact coverage and size summary for human review.

Compile must not use any tier or environment mention to upgrade `fit`, `map_floor_fit`, or `slot_eligibility`; those fields come from stable map hooks and matched capabilities. `mode_contract_fit` is evidence-only, not playability. `candidate_index` keeps `map_floor_fit`, `mode_contract_fit`, `recall_channels`, `slot_eligibility`, `conditional_lift`, and `failure_gates` separate so runtime fact tools can expose map fit, mode evidence, relation windows, and failure risks without deciding what wins.

The compiled index may be richer than the prompt window, but decide must consume it through `query_runtime_facts.py` and `hydrate_runtime_facts.py`. Use `--debug-output` only for compile debugging. Missing environment evidence remains explicit uncertainty, not a license to invent tiers or meta claims.

## Decide Summary

`decide` uses `query_runtime_facts.py` for the neutral map/entity fact window and `hydrate_runtime_facts.py` for the final few entities, then the LLM produces `candidate_eval`, `turn_decision_trace`, and `bp_recommendation`. The model should reason from returned facts, conditional relations, map hooks, objective contracts, and failure modes. The tools must not choose candidates, label answers, or produce a team plan.

For ban turns, the LLM must add `side_asymmetric_ban_strategy` before finalizing bans. Blue bans reason from `first_pick_initiative`: protect_first_pick, preserve flexible opener/fog value, and avoid `ban_overlap_risk` from generic map-power mirroring. Red bans reason from `last_counter_leverage`: `deny_blue_safe_opener`, preserve_red6_counter_pool, force blue slot-1 exposure, and evaluate `last_pick_counterability`. Both sides still query only neutral facts; side, purpose, `opener_safety`, and counter exposure are LLM interpretations, not tool outputs.

Use `decision_effort_policy` to choose the recall budget before each fact query. Runtime only has two normal presets: `low=24` and `high=32`. Slot power supplies the baseline and `strategy_bias` supplies the default posture, but the player may still use explicit `--limit` for a single hand when it needs finer control. Do not reintroduce broad offline tiers as normal BP presets.

Default policy:

| turn | baseline effort | reason |
| --- | --- | --- |
| ban phase | `low` | enough to compare map pressure, opener safety, and ban overlap without turning the turn into an exhaustive audit |
| blue slot 1 | `low` | first-pick initiative needs opener/flex/counter-exposure evidence, but the draft state is still sparse |
| red slots 2-3 | `low` | answer blue 1 while preserving red 6 counter geometry |
| blue slots 4-5 | `high` | blue must finish its trio while checking exposure to red 6 |
| red slot 6 | `high` | highest visible-information counter slot |
| final_draft_review | selected hydration only | hydrate selected brawlers and relevant relation targets; do not run a full-pool query |

Strategy defaults:

| strategy_bias | default effort posture |
| --- | --- |
| `conservative` | use baseline; prefer hydration of serious options over expanding the pool |
| `balanced` | use baseline |
| `aggressive` | use `high` for ban, blue 4-5, red 6, and route / punish probes; otherwise baseline |
| `high_variance` | use `high` for all broad fact windows; use explicit `--limit` only for deliberate stress tests |

Each selected candidate and top decision must include a report-facing summary layer authored by the player side: `report_summary`, `priority_factors`, `risk_summary`, and `build_summary`. These fields are intentionally short and weighted; they explain the most important map duty, relation evidence, comp role, risk, and star power / gadget / gear implication for the human match report. They must use Chinese concepts such as 金库输出、长线压制、开墙改地形、续航守线、反突保护, not raw hook ids or underscore-heavy runtime labels. The LLM writes this reasoning from neutral facts; tools must not provide pre-authored decision labels.

When the caller needs a decision audit, also return `retrieval_audit` for each turn. This field is not BP advice from a tool; it is the LLM's bookkeeping over neutral tool metadata: query focus, include/exclude/relation filters, recalled candidate count, `fragments_returned`, `payload_kb`, and a compact summary of recalled map/entity/relation facts.

Every ban/pick turn must return `turn_decision_trace`, even when no audit was requested. This is the real runtime thinking record, not a later explanation. It must include `decision_style`, `map_problem`, `visible_state`, `query_intent`, `retrieval_audit`, `candidate_comparison`, `selected_reason`, `rejected_options`, `examined_options` (every inspected option with why it was examined), and `risk_and_build_implication`. If a field is unknown, write the uncertainty directly instead of omitting it.

When revealed entities are visible, the caller may pass them as `--relation-target` so relation facts are available. The LLM decides whether those facts are counters, answers, soft pressure, irrelevant, or risky in the current BP state. Tool output must keep the neutral `conditional_relations` shape.

Ordering logic:

1. Hard gates beat everything.
2. Mode objective and map duty coverage beat isolated matchup comfort.
3. Conditional matchups count only when their active conditions match the map, mode, comp, build, and slot.
4. Evidence-backed map fit (concrete hooks / matched capabilities) beats generic matchup comfort.
5. Relation edges can matter only when the revealed draft state activates their mechanism; they do not reclassify the entity as generally strong on the map.
6. For paired response slots, build a team plan first. Relation coverage is useful only when it also serves map / mode / comp shape or avoids a named failure.
7. There is no strength ranking or tier in this system; environment evidence is labeled corroboration, never a candidate ordering.
8. Slot exposure can demote otherwise strong candidates. Route-only or objective-only picks need a real endpoint and failure mitigation.
9. Strategy bias changes judgment among viable candidates; it cannot make a false-positive map fit viable.

Always run `balanced_threat_probe`. A balanced draft must still evaluate one legal `route_based_tank_or_assassin` / `proactive_threat_candidate` when the map exposes a real route, endpoint payoff, and constrained enemy answer set. Use `do_not_demote_tank_assassin_for_style_alone`: demotion requires a named failed route, missing `route_endpoint_payoff`, or realistic remaining counter.

For `balanced`, the 2-4 candidate decisions must include at least one proactive threat candidate, including a tank/assassin, unless hard_gate_result.must_avoid or map false-positive filters rule it out.

After all six draft positions are locked, run `final_draft_review` for each side. This review cannot change picks. It re-reads the full visible draft, hydrates only the selected brawlers and relevant relation targets if needed, then returns win condition, play pattern, primary risks, risk mitigation, and `role_build_plan` for every selected brawler. The judge may copy this review into the human report, but must not invent it. In match-scoped play, append the final review to your player log (`{PLAYER_LOG_PATH}`) as well; the per-turn outputs stay lean and fast.

## Examined-Options Audit

Every ban/pick turn must also produce `examined_options`: the structured record of every option the player actually examined this hand, with the reason it was examined. This is the audit core for later decision optimization.

Output mode depends on the caller:

- **Standalone single-hand BP runs** (this skill's decide output): return the full `examined_options` per turn, as specified below. The audit is part of the turn itself.
- **Match-scoped turns** (judge-driven via `run-brawl-stars-bp/references/turn-prompt-template.md`): the judge's per-turn contract is intentionally lean (`decision` / `key_reason` / `confidence` / `retrieval`) to keep every turn fast and cheap. Do NOT emit the full `examined_options` in the reply — append it to your side's player log (`{PLAYER_LOG_PATH}`, passed in every 对局信息 block): a section per own turn with every option seriously inspected, `why_examined`, `evidence_used`, `verdict`, `verdict_reason`, and the ranking order in which they were considered. The judge reads both player logs after the match and assembles the verbose decision log from them.

```yaml
examined_options:
  - option: <brawler>
    why_examined: 为什么查它（进入候选池的来源：哪个检索窗口/bucket、哪条关系边、哪个地图职责或失败门核查）
    evidence_used: 查到的关键证据（机制 hook / ladder / monthly，一句）
    verdict: selected | rejected | deferred
    verdict_reason: 一句理由
```

Rules:

- Cover every candidate that was seriously inspected in this hand, not only the rejected ones: the final selection, rejected alternatives, and deferred options all appear. `why_examined` answers "why did this option enter the candidate pool at all" — the neutral query window, relation edge, map duty, or failure-gate check that surfaced it.
- `evidence_used` must name the actual retrieved facts for that option (map hook / relation edge / ladder / monthly), so a later audit can see what the option was judged against.
- `verdict` is one of `selected`, `rejected`, `deferred`. `deferred` means "serious candidate but intentionally held back for a later slot / different situation", distinct from a plain rejection.
- `verdict_reason` is the one-line player-authored conclusion. Do not leave it as "see other fields".
- The full `turn_decision_trace` (query intent, retrieval audit, candidate comparison, evidence roles) stays the source of how the decision was built; `examined_options` is the per-option inventory that audit reports consume. A trace that lists a candidate in `candidate_comparison` must also carry it in `examined_options` with its `why_examined`.

## Output Contract

Return a compact recommendation:

```yaml
bp_recommendation:
  context_summary:
  fact_sources:
    map:
    entities:
    relation_targets:
  candidate_evals:
  examined_options: # 本手查验过的每个选项（含选中、否决、推迟）；独立单手 BP 的审计核心，格式见上方 Examined-Options Audit
  top_decisions:
  draft_eval:
  uncertainty:
  retrieval_audit:
turn_decision_trace:
  decision_style:
  map_problem:
  visible_state:
  query_intent:
  retrieval_audit:
  candidate_comparison:
  selected_reason:
  rejected_options: # 可由 examined_options(verdict=rejected) 派生；保留作兼容摘要
  examined_options: # 本手查验过的每个选项 + 为什么查它（审计核心，必须与 candidate_comparison 覆盖一致）
  risk_and_build_implication:
final_draft_review:
  full_draft_read:
  win_condition:
  play_pattern:
  primary_risks:
  risk_mitigation:
  role_build_plan:
  cannot_change_picks: true
# match-scoped：详细思考过程（含 per-turn examined_options 全量 + 查验排序）写入选手日志 {PLAYER_LOG_PATH}，裁判整局结束后读取汇总 verbose decision log
```

Each candidate must include:

```yaml
candidate_eval:
  candidate:
  decision_type: pick | ban
  why_now:
  evidence_used:
  map_duties_covered:
  relation_edges_considered:
  accepted_risks:
  required_builds:
  rejection_or_selection_reason:
```

## Common Mistakes

- Do not output a single pick without alternatives.
- Do not use `open`, `wall density`, `water`, or `summary_tags` as direct scoring signals.
- Do not treat `A counters B` as unconditional; explain mechanism, active conditions, fail conditions, and BP use.
- Do not invent T0/meta claims from memory. Environment evidence is read from the compiled index only; do not fabricate tiers or rankings.
- Do not let `strategy_bias: aggressive` justify a tank/assassin without route, follow-up, and endpoint safety.
- Do not let `balanced` collapse into only range/control/sustain shells.
- Do not let `scripts/bp_index.py` output become the answer; it only locates stable pages and skill references.
