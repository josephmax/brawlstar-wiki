---
name: brawl-stars-bp-slot-decision
description: Use when compiling or using a Brawl Stars Ranked Ban Pick runtime index, deciding a specific draft slot, evaluating bans or picks, comparing candidates, or checking map fit, hard gates, counter-picks, strategy bias, and strength context from this vault.
---

# Brawl Stars BP Slot Decision

## Core Boundary

This skill has two modes:

- `compile`: read stable entity facts and strength input, then generate a `runtime_bp_index`.
- `decide`: validate the compiled `runtime_bp_index`, query it through bundled tools, combine the returned fragments with current draft state and runtime decision rules, then return one ban or pick recommendation set.

The skill must not use the wiki's synthesis/topic discussion layer as a runtime dependency. Those pages are maintainer workspace, not player-facing knowledge. The skill is self-contained through its own references and stable entity pages.

## Mode Required Reads

### compile

Read:

- `skills/brawl-stars-bp-slot-decision/references/compile-knowledge.md`
- Relevant map pages under `wiki/entities/maps/`
- Relevant brawler pages under `wiki/entities/brawlers/`
- User, judge, external, or adopted default `strength_profile`; the current adopted default is `skills/brawl-stars-bp-slot-decision/references/default-strength-profile.json`
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

For JSON consumers, read candidates from `runtime_fact_query.fact_window`. Each row includes scalar `strength_tier`, scalar `strength_rank`, `relation_count`, and `runtime_card_counts` so callers do not need to sort or compare nested dictionaries such as `strength`.

Hydrate details only for the few entities the LLM wants to inspect more deeply:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/hydrate_runtime_facts.py \
  --index "<index_path>" \
  --map "Safe Zone" \
  --include-id "Meg" \
  --include-id "Crow" \
  --json
```

Hydration JSON keeps `entities` as a dictionary keyed by brawler for backward compatibility, and also returns `entity_window` as a list for safe iteration. Each hydrated entity includes scalar `strength_tier`, scalar `strength_rank`, `relation_count`, `runtime_card_counts`, `retrieval_bucket_hits`, `candidate_map_fit`, and `evidence_ref`. Use `--summary` when the caller wants a readable entity audit without writing parsing code.

`--strength-weight` is LLM-side reasoning context, not a tool parameter: `0` means ignore strength while comparing recalled facts; `1` means treat map-scoped strength as the main tie-breaker inside the already recalled fact window; the default baseline is `0.4`. Strength never expands the fact window by itself.

## Input Contract

Normalize requests into one of these objects:

Before filling these objects, normalize brawler names through `wiki/concepts/英雄名称归一化.md`: canonical brawler page names pass through; `aliases` map automatically; `ambiguous` entries require user or judge confirmation instead of silent resolution.

```yaml
compile_input:
  patch_id:
  map_pool:
  available_brawlers:
  strength_profile:
    profile_id:
    owner:
    scope: global | mode | map | custom
    entries:
  source_policy:
    read_stable_entities_only: true
```

Default compile uses the adopted default strength profile:

```yaml
strength_profile:
  profile_id: ikaoss11-july-2026-screenshot
  owner: runtime_default
  scope: global
  path: skills/brawl-stars-bp-slot-decision/references/default-strength-profile.json
```

This means "use stable wiki facts plus the adopted version-strength input". User-supplied strength profiles are accepted as a separate strength layer and may replace this default for a session; using any strength profile to rewrite stable hero or map facts is forbidden. Runtime exposes only map-scoped candidate strength from `map_pool_signature[*].candidate_index`; it does not expose a top-level strength table. An explicit empty profile still means "mark strength as unknown".

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
  strength_weight: 0.0-1.0 # default 0.4
```

If `map`, `mode`, or slot is missing, state the assumption. Ask only when the missing field changes the decision.

## Runtime Index Precheck

`decide` must not start from free-form wiki reads. It first checks whether the requested map, mode, pool, patch, and strength profile are covered by a compiled runtime index.

Recommended index state files live under `outputs/runtime-bp-index/`:

```text
<runtime_index_key>.json
<runtime_index_key>.lock
```

The `runtime_index_key` should be derived from patch id, map pool id, available brawler pool, and strength profile hash. A supplied explicit `runtime_bp_index` can bypass file lookup if its manifest matches the current request.

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

- `map_pool_signature`: per-map `map_context`, per-slot map-evidence `candidate_projection`, and full-map `candidate_index` covering every available brawler. `candidate_projection` preserves all concrete map candidates for each legal slot instead of cutting at the strength front-rank. `candidate_index` is the only runtime strength surface: each map candidate carries map-scoped `tier` and `rank`.
- `brawler_runtime_cards`: global brawler capability, build, map hook, objective, failure, and slot-note fragments stored once for hydration.
- `matchup_index`: conditional matchup edges keyed by brawler for draft-state filtering.
- `evidence_refs`: source refs for map and brawler pages so detailed explanations can hydrate only the final shortlist.
- `audit_summary`: compact coverage and size summary for human review.

Strength matters only as a separate evidence layer. Compile must not use tier or mode mentions to upgrade `fit`, `map_floor_fit`, or `slot_eligibility`; those fields come from stable map hooks and matched capabilities. `mode_contract_fit` is evidence-only, not playability. `candidate_index` keeps `map_floor_fit`, `mode_contract_fit`, `recall_channels`, `slot_eligibility`, `conditional_lift`, and `failure_gates` separate so runtime fact tools can expose map fit, mode evidence, relation windows, and failure risks without deciding what wins.

The compiled index may be richer than the prompt window, but decide must consume it through `query_runtime_facts.py` and `hydrate_runtime_facts.py`. Use `--debug-output` only for compile debugging. Unknown strength remains explicit uncertainty, not a license to invent tiers.

## Decide Summary

`decide` uses `query_runtime_facts.py` for the neutral map/entity fact window and `hydrate_runtime_facts.py` for the final few entities, then the LLM produces `candidate_eval`, `turn_decision_trace`, and `bp_recommendation`. The model should reason from returned facts, conditional relations, map hooks, objective contracts, failure modes, and strength evidence. The tools must not choose candidates, label answers, or produce a team plan.

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

Every ban/pick turn must return `turn_decision_trace`, even when no audit was requested. This is the real runtime thinking record, not a later explanation. It must include `decision_style`, `map_problem`, `visible_state`, `query_intent`, `retrieval_audit`, `candidate_comparison`, `selected_reason`, `rejected_options`, and `risk_and_build_implication`. If a field is unknown, write the uncertainty directly instead of omitting it.

When revealed entities are visible, the caller may pass them as `--relation-target` so relation facts are available. The LLM decides whether those facts are counters, answers, soft pressure, irrelevant, or risky in the current BP state. Tool output must keep the neutral `conditional_relations` shape.

Ordering logic:

1. Hard gates beat everything.
2. Mode objective and map duty coverage beat isolated matchup comfort.
3. Conditional matchups count only when their active conditions match the map, mode, comp, build, and slot.
4. Evidence-backed `overpowered_or_t0_exception` can become a hard gate when cheap reliable answers are unavailable.
5. Relation edges can matter only when the revealed draft state activates their mechanism; they do not reclassify the entity as generally strong on the map.
6. For paired response slots, build a team plan first. Relation coverage is useful only when it also serves map / mode / comp shape or avoids a named failure.
7. Map-scoped strength rank is controlled by the LLM's `strength_weight` reasoning. It never expands the fact window by itself.
8. Slot exposure can demote otherwise strong candidates. Route-only or objective-only picks need a real endpoint and failure mitigation.
9. Strategy bias changes judgment among viable candidates; it cannot make a false-positive map fit viable.

Always run `balanced_threat_probe`. A balanced draft must still evaluate one legal `route_based_tank_or_assassin` / `proactive_threat_candidate` when the map exposes a real route, endpoint payoff, and constrained enemy answer set. Use `do_not_demote_tank_assassin_for_style_alone`: demotion requires a named failed route, missing `route_endpoint_payoff`, or realistic remaining counter.

For `balanced`, the 2-4 candidate decisions must include at least one proactive threat candidate, including a tank/assassin, unless hard_gate_result.must_avoid or map false-positive filters rule it out.

After all six draft positions are locked, run `final_draft_review` for each side. This review cannot change picks. It re-reads the full visible draft, hydrates only the selected brawlers and relevant relation targets if needed, then returns win condition, play pattern, primary risks, risk mitigation, and `role_build_plan` for every selected brawler. The judge may copy this review into the human report, but must not invent it.

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
  rejected_options:
  risk_and_build_implication:
final_draft_review:
  full_draft_read:
  win_condition:
  play_pattern:
  primary_risks:
  risk_mitigation:
  role_build_plan:
  cannot_change_picks: true
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
  strength_context:
  accepted_risks:
  required_builds:
  rejection_or_selection_reason:
```

## Common Mistakes

- Do not output a single pick without alternatives.
- Do not use `open`, `wall density`, `water`, or `summary_tags` as direct scoring signals.
- Do not treat `A counters B` as unconditional; explain mechanism, active conditions, fail conditions, and BP use.
- Do not invent T0/meta claims from memory. If no strength source is provided, write `strength_context.source: unknown`.
- Do not let `strategy_bias: aggressive` justify a tank/assassin without route, follow-up, and endpoint safety.
- Do not let `balanced` collapse into only range/control/sustain shells.
- Do not let `scripts/bp_index.py` output become the answer; it only locates stable pages and skill references.
