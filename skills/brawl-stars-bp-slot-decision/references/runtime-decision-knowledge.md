# Runtime Decision Knowledge

When the caller supplies player eligibility, apply [candidate-mask.md](candidate-mask.md) to personal candidate queries and hydration. Include and capability windows cannot override the mask. Inspect opponents/locked entities separately; retain global census counts and use the additional selectable projection for personal responses.

Use this reference only in `decide` mode. The decider consumes a compiled `runtime_bp_index` through neutral fact-retrieval tools. It does not search maintainer notes, load the full index into the prompt, rebuild the index during a pick turn, or delegate BP judgment to scripts.

## Core Boundary

工具只做事实召回. The tools may:

- validate that a compiled index covers the requested map.
- return a compact map fact packet.
- return entity fact windows selected by neutral `include-id`, `exclude-id`, `relation-target`, and bucket filters.
- return conditional relation facts as source/target edges.
- return map fit evidence and source refs.

The tools must not:

- receive business-role parameters such as `our_pick`, `enemy_pick`, `bans`, `strategy_bias`, or `decision_seed`.
- output decision-shaped fields such as `judgment_brief`, `current_team_plan`, `candidate_shortlist`, `ability_gate`, `capability_gate`, `adjudication`, `ban_purposes`, `must_ban`, `top_decisions`, or `answers_enemy_picks`.
- call something an answer, counter, protected pick, team gap, or ban purpose.

The LLM owns all BP interpretation: map duty reasoning, current draft interpretation, threat framing, candidate comparison, risk acceptance, and final ban/pick choice.

## decide_input

Normalize the user or judge state into two layers:

```yaml
bp_reasoning_context:
  map:
  mode:
  current_global_slot: 1 | 2 | 3 | 4 | 5 | 6
  draft_state:
    own_picks:
    opposing_picks:
    unavailable:
  candidate_pool:
  known_player_constraints:
  strategy_bias: conservative | balanced | aggressive | high_variance

tool_query_context:
  include_ids: []        # entities whose facts must be visible
  exclude_ids: []        # entities unavailable to the current choice
  relation_targets: []   # visible entities whose conditional relation edges should be recalled
  buckets: []            # compiled retrieval bucket ids to inspect
```

`bp_reasoning_context` stays in the LLM prompt. Convert only neutral entity IDs and retrieval filters into tool calls.

If the index is missing, stale, or does not cover the selected map / mode / pool, run `runtime_index_precheck` before normal decision work. Do not patch the answer with memory.

## Runtime Index Precheck

Use the bundled script for file-level coordination:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/runtime_index_precheck.py \
  --repo . \
  --index-key "<runtime_index_key>" \
  --json
```

The script returns one of three operational states:

- `ready`: a validated index exists; read `index_path`.
- `compile_required`: this process owns `lock_path`; run `compile`, write `index_path`, then release the lock.
- `runtime_index_compile_failed`: bounded wait and stale-lock recovery failed; stop.

Never wait forever. Never read maintainer discussion pages or memory-only tier lists to bypass the failed compile.

## Neutral Fact Tools

After `runtime_index_precheck` returns `ready`, call `query_runtime_facts.py` instead of reading the full JSON.

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

Inputs:

- `--include-id`: force an entity's facts into the returned fact window (always honored, even when `--capability` is active).
- `--exclude-id`: exclude an entity from the returned fact window.
- `--relation-target`: return conditional relation facts involving this target entity.
- `--capability`: capability-window retrieval primitive. Repeatable, OR semantics. Keeps only brawlers whose stable `runtime_card.capability_tags` include any requested tag (e.g. `throw_or_wall_bypass`, `crowd_control`, `wall_break`). Capability hits are never truncated by `--effort`/`--limit`: every matching brawler is visible, so a W-Z name like Willow cannot be starved by an alphabetical window. This is how a player answers "I need a wall-bypass thrower" instead of waiting for the generic map-fit window.
  - **Tag ≠ threshold**: a tag only says the axis exists; use `--require-floor "throw_or_wall_bypass@high"` when the hand needs the strong version of the axis. A raw tag window mixes "true arc throwers" with "one gadget briefly touches over a wall" — always prefer the floor form for capability-window queries.
  - **Window scans the full pool**: when any window is active, candidates outside the map's projection buckets are still returned (marked `capability_window` in `retrieval_matches`), ranked below in-map fits by their `map_fit`. A fit=weak thrower on an open map is visible information, not a nonexistent hero — treat window hits with weak fit as situational answers and say so explicitly.
- `--archetype`: require a derived archetype class (`assassin`, `sniper`, `thrower_core`, `tank_front`, `area_controller`, `vision_controller`, `dual_duty_mid`). Archetypes are conjunctions of capability predicates evaluated at compile time — never hand-listed — so a new brawler is classified automatically and "why is X an assassin" is always printable as its matching predicates.
- `--require-floor "dim1,dim2@level"`: floor query for the "no weak axis" allrounder shape (R-T / Pearl style): every named axis must reach at least that level. This is a minimum query, the complement of peak/threshold queries — use it when the hand needs lane-safe balance rather than a spike.
- `--bucket`: select a precompiled retrieval bucket by id. The bucket id is an index partition, not a recommendation. `ban_pressure` recall is ordered by the map's own environment ladder — active ladder rows first by use_rate then win_rate, names without an active row keeping the generic evidence-relevance order behind them — so the effort cut lands on environment-hot candidates instead of hook-count/name order. Bucket membership is unchanged.
- `--effort`: recall budget preset. `low=24` and `high=32`; default is `low`.
- `--field`: optional caller hint for requested fields.
- `--limit`: explicit override for entity fragments. Prefer `--effort` unless a caller needs a precise budget.
- `--summary`: emit an agent-readable summary table. Use it for manual inspection and audit drafting instead of writing fragile one-off `python3 -c` parsers.
- `--cache-dir`: directory for a cross-query disk cache. Same index + query parameters hit the cache and skip reloading the 4.4MB index and recomputing the window; the response carries `cache_hit: true`. Reuse one cache dir across a whole match so repeated `query_runtime_facts` / `hydrate_runtime_facts` calls (same map + same parameters) are served from disk instead of recomputed. Prefer narrowing with `--relation-target` / `--exclude-id` over widening; never cache environment evidence — it is read from separate signal files and does not participate in the index cache.
- Window discipline: one serious capability window per hand. A bucket window (`ban_pressure`, `early_pick`, `response_pick`) and a `--capability` window overlap heavily on the same pool — if the first window already returned the candidates this hand needs, do not scan a second full-pool window to double-check coverage. If truncation is the fear, narrow or target instead of widening: shape the pool with `--relation-target` / `--exclude-id`, set a deliberate per-hand recall budget with `--limit`, then hydrate the specific `--include-id` entities the window surfaced. A widened second scan must be justified in the retrieval audit with what the first window could not answer.

Output:

- `manifest`: compact index identity.
- `scope`: map and mode.
- `request`: neutral retrieval request echo.
- `map_fact_packet`: source ref, objective contracts, required capabilities, route gates, hard gates, and false-positive filters.
- `fact_window`: returned entities with map fit evidence, map hook IDs, matched capabilities, failure gates, build IDs, selected runtime-card fragments, `runtime_card_counts`, `conditional_relations`, and `relation_count`.
- `retrieval_summary`: fragment count and payload size.

Use `hydrate_runtime_facts.py` only after the LLM narrows to a few serious entities:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/hydrate_runtime_facts.py \
  --index "<index_path>" \
  --map "Safe Zone" \
  --include-id "Crow" \
  --include-id "Pierce" \
  --relation-target "8-Bit" \
  --json
```

Hydration returns each requested entity's runtime-card facts, retrieval bucket hits, map fit, conditional relations, source refs, and `environment_evidence` (the ladder / monthly dimensions folded into the index by compile, with window / rank_floor / fetch-or-capture labels; a dimension is `null` when the hero has no sample). The JSON keeps `entities` as a dictionary keyed by brawler and also returns `entity_window` as a list for safe iteration. Each entity includes `runtime_card_counts` and `relation_count`; use those instead of comparing nested dictionaries. If returned facts are not enough to support a claim, mark the claim uncertain or reject that line of reasoning; do not bypass the tool by reading full wiki pages in decide mode.

Environment evidence lives inside the compiled index — `hydrate_runtime_facts.py` is the only evidence reader. The hydration response also carries `environment_ladder`, the Legendary+ per-map rows for the current map (projected to the requested heroes) with `match_count` and `active` labels. For several heroes, hydrate them in one call by repeating `--include-id`; there is no separate environment tool.

Census of surviving counters lives in `query_matchup_census.py` — give it a hero and the current ban set, and it filters the compiled matchup edges into `answered_by` (who can still punish this hero) and `answers` (who this hero still punishes), each with alive/removed counts plus the raw mechanism / active_when / fails_when text for condition interpretation. It is the mechanical input to first-response discipline (see that section): counts decide whether an early opponent pick lost its predators or its prey; the named edges are what you interpret.

When you have already hydrated a hero in an earlier turn of the same match (its facts are already in your context), reuse that result instead of querying again. A batched call is for heroes not yet seen; it is not a reason to re-fetch everything.

## LLM Decision Pipeline

1. Run `runtime_index_precheck`; continue only with a validated `index_path`.
2. **Capability-Window First**: before querying, define the capability window this hand needs. Derive it from (a) the map's `required_capabilities` / route gates, (b) the current draft's missing duties, and (c) the opponent's revealed picks (which capability would answer them). Express it as concrete tags (`throw_or_wall_bypass`, `wall_break`, `crowd_control`, `scouting_or_vision`, `goal_area_denial`, ...) and pass them as `--capability`. The window is the candidate pool; map fit and relations are then judged *inside* the pool.
3. Translate BP state into neutral tool filters:
   - already unavailable entities -> `--exclude-id`
   - revealed or important entities to inspect -> `--include-id`
   - visible entities whose relation edges matter -> `--relation-target`
   - desired evidence window -> `--bucket`
   - capability window derived in step 2 -> `--capability`
4. Call `query_runtime_facts.py`.
5. Read `map_fact_packet` first: objective, route gates, hard gates, and false-positive filters define the map problem.
6. Read `fact_window` as evidence, not as a recommendation. A returned entity is merely relevant enough to inspect.
7. Interpret conditional relations yourself. A relation edge is not automatically a counter, answer, ban, or pick.
8. **Mode-feature filter inside the pool**: not every capability-tagged brawler is a real answer on this map/mode. Check each pool member against the mode's objective behavior (e.g. in Brawl Ball a thrower that cannot participate in ball carry, score conversion, or goal defense is a false positive even with a strong wall-bypass tag). The map's false-positive filters and each candidate's `objective_contracts.false_positive` are the evidence for this step.
9. Compare candidates by explicit reasoning: capability-window fit, mode-feature fit, map duty coverage, relation activation, current draft needs, failure modes, required builds, and strategy bias. For every option that survives into the comparison set, record why it entered the candidate pool at all (which capability window / bucket, which relation edge, which map duty or failure-gate check surfaced it) — this becomes the `examined_options` audit row.
10. Call `hydrate_runtime_facts.py` for the few entities whose detailed facts matter.
11. When a serious candidate's pick-rate or ban-rate matters (high-stakes slots 4-6, contested openers, or when two candidates are otherwise close), hydrate it and read its `environment_evidence` (Legendary+ ladder anchor + monthly finals) plus the current map's `environment_ladder` rows. Treat them as labeled evidence, not as a ranking.
12. Produce `candidate_eval`, `turn_decision_trace`, and `bp_recommendation` in the LLM response.
11. Produce `retrieval_audit` from the actual tool requests and `retrieval_summary` values. This is evidence bookkeeping only: include query focus, neutral filters, recalled entities, `fragments_returned`, and `payload_kb`; do not turn it into a recommendation.

## Reasoning Rules

- Do not rank by environment signal first and then explain around it. The environment slot (high-rank pickrate) is currently empty; there is no tier or strength layer in this system.
- Do not let a tier or mode mention create map fit. Map fit must come from concrete map hooks, objective contracts, or matched capabilities.
- Do not treat a capability tag as a pick. `--capability` defines the candidate pool, not the answer: a tagged brawler still needs map fit, mode-feature fit, and draft activation. Conversely, do not let the generic map-fit window be the only entry into the pool — a capability-window query is the deliberate way to answer "this hand needs a thrower / a wall-breaker / a mind-controller".
- Do not treat relation edges as unconditional. Name mechanism, active conditions, fail conditions, and whether the current map/draft activates them.
- Do not treat retrieval order as final ranking. Retrieval order exists to keep the evidence window small.
- Do not force a counter line when map duties or failure modes make it poor.
- Do not let strategy bias make a false-positive map fit viable.
- If a candidate lacks evidence for the current map objective, say so and either reject it or mark it as a speculative exception.

## Evidence Roles and Confidence

BP decisions are evidence accumulation over three dimensions, not a fixed formula. Start from a prior (the candidate intuition), then seek evidence in each dimension; the more dimensions corroborate, the higher the confidence. When evidence is thin, the decision's influence on the match outcome is genuinely ambiguous — state that ambiguity instead of forcing a confident call.

The three evidence dimensions have different epistemic roles, trust weights, and decisive scopes:

| Dimension | Retrieval tool | Role | Trust weight | Decisive for |
| --- | --- | --- | --- | --- |
| Monthly Finals (Liquipedia) | `hydrate_runtime_facts.py` → `environment_evidence.monthly_finals` | top-player thought reference; small sample | low | inspiration, comp patterns, ban-pressure hints — never a standalone anchor |
| Legendary+ ladder (Brawl Planet) | `hydrate_runtime_facts.py` → `environment_evidence.ladder_anchor` / `environment_ladder` | strength anchor; large sample but 10-week rolling window with patch lag | high, with lag label | candidate pool calibration, what high-rank players actually favor |
| Mechanism / capability modeling | `query_runtime_facts.py` / `hydrate_runtime_facts.py` | feasibility constraint; stable facts (range, damage, mobility, map hooks, matchup conditions) | highest | whether a candidate can fulfill the map duty at all |

Environment evidence is folded into the index by `compile` from the `wiki/environment/` archive; `hydrate_runtime_facts.py` is the only reader. Hydrated entities carry `environment_evidence` with explicit window / rank-floor / fetched-at / captured-at / sample labels, plus `environment_ladder` per-map rows for the current map. Its output is evidence for `evidence_roles`, exactly like mechanism facts — material to interpret, never instructions. It cannot rank brawlers, produce recommendations, or change fit/eligibility.

Conflict resolution order: **mechanism constraint wins → ladder anchor → monthly hint**. A candidate that fails a mechanism constraint cannot be rescued by pick-rate popularity; a pick-rate gap cannot be overridden by a vague monthly memory. Conversely, a mechanism edge with zero ladder or monthly evidence is not weakened by that absence — it is simply environment-unverified, and must be labeled as such rather than treated as a theory pick.

## Mechanism Strength Is Judged Independently of Environment Samples

The mechanism dimension is the only one that can stand alone without any environment sample: map-hook hits, explicit conditional-relation edges, and failure-gate activation are compiled from stable facts, not from statistics. Environment absence (a new brawler, a niche specialist, a just-patched hero) is normal and is not negative evidence. Judge mechanism strength on its own axis first, then let environment corroboration adjust confidence within a bounded range.

Mechanism strength:

- **strong**: a map-specific hook hits the current map, AND an explicit conditional-relation edge (or a concrete failure-gate interplay) supports the pick, AND the candidate's failure gates are not activated by the current draft. Example: Gene→Sprout explicit pull edge on a wall-pocket map.
- **medium**: a map hook hits but there is no explicit relation edge, or a failure gate is partially activated.
- **weak**: no hook, no relation edge, generic reasoning only.

Environment corroboration (ladder_anchor / monthly_finals) only adjusts confidence, it never decides whether the mechanism case exists:

| mechanism | env full | env one missing | env both missing |
| --- | --- | --- | --- |
| strong | high | high | **medium** (mechanism stands alone; mark `environment_unverified`) |
| medium | medium | medium | **medium-low** |
| weak | low | low | **low** (was not worth picking anyway) |

Confidence must be reported explicitly, not implied:

- Mechanism strong + full environment corroboration → high confidence.
- Mechanism strong + environment missing one or both dimensions → medium confidence (`environment_unverified`), not a theory pick; the mechanism case is real, only the statistical corroboration is absent.
- Mechanism + one environment dimension supports, the other contradicts (or vice versa) → medium confidence with the conflict named.
- Mechanism medium with thin environment → medium-low; label the pick as mechanism-first.
- Mechanism weak, or evidence insufficient for the current map/draft → low confidence; state that the decision's influence on the outcome is ambiguous; do not invent confidence.

Sample-size honesty applies to every dimension: a Legendary+ use rate under roughly 2% is a small-sample number and must not be treated as a stable anchor; a monthly pick count under ~5 is anecdotal. Report the sample with the number, do not let a single number carry more weight than its denominator allows.

This is not a strength layer and does not rank brawlers. It is a per-decision evidence protocol: the LLM states which dimension each piece of reasoning came from, and how much the evidence supports the choice. `decide` never receives pick-rate numbers as a tier; it receives them as labeled evidence with a window and a sample size. If a hydrated hero's `environment_evidence` has `ladder_anchor: null` or `monthly_finals: null`, the trace must report `no_ladder_sample` / `no_monthly_sample` — that dimension is absent, not filled from memory.

## First-Response Discipline (answering an early opponent pick)

When the opponent picks early (first pick, or an early slot that finishes before your response), the question is **not** "which hero counters this pick". It is a three-step exposure diagnosis before any counter budget is spent:

1. **Exposure diagnosis (does the weakness even fire on this map?)** Read the pick's `failure_gates` with their per-map `failure_gate_activation` levels (compiled from each gate's precondition type against the map's approach geometry). A gate marked `low` on this map — e.g. a "punished by close-range divers" gate on an open sniper map — is a paper weakness; a gate marked `high` is a live one. A threat whose killing gates are all `low` here is a structural pick, not an emergency.
2. **Predator census (did the ban phase move its ecosystem?)** Run `query_matchup_census.py --hero <pick> --banned ...`. Read both counts: shrinking `answered_by.alive_count` means the ban phase removed its predators (the pick got safer); shrinking `answers.alive_count` means its prey is gone (banning/picking it loses value). Interpret from the named survivors, not from memory — matchup edges are the record, not your recollection.
3. **Budget discipline (is a dedicated counter worth a pick slot?)** Spend a pick on a direct counter only when **all three** hold: (a) at least one failure gate activates with high likelihood on this map; (b) the answering heroes are alive and themselves viable here; (c) the counter does not break your own team structure (range floor, duty coverage, exposure to the opponent's remaining picks). Otherwise build your own structure first (map hard gates + required capabilities) and keep counter picks as reserve ammunition for later slots where the opponent's shape is revealed.

A first-response decision that skips step 1–2 and jumps to "pick the counter" is a discipline violation; the `turn_decision_trace.query_intent` must show the exposure diagnosis and census retrieval when a dedicated counter is chosen.

## Side-Asymmetric Ban Strategy

Ban phase is simultaneous, but blue and red do not own the same slot power. This is LLM-side reasoning over neutral facts: both sides may query the same `ban_pressure` bucket, and tools still receive only neutral `include-id`, `exclude-id`, `relation-target`, `--bucket`, and `--effort` inputs. Do not pass side labels, future plans, or ban purposes into fact tools.

Every ban turn must include `side_asymmetric_ban_strategy` before listing final bans:

```yaml
side_asymmetric_ban_strategy:
  side: blue | red
  slot_power: first_pick_initiative | last_counter_leverage
  ban_purpose_order:
  candidate_eval:
    map_power:
    opener_safety:
    counter_exposure:
    comp_flexibility:
    last_pick_counterability:
    ban_overlap_risk:
  selected_bans:
  preserved_options:
```

Blue owns `first_pick_initiative`: blue slot 1 can take a high-map-impact opener before red has counter information. Blue bans should be evaluated through these purposes:

- `protect_first_pick`: remove cheap, broad counters to likely blue-1 openers.
- Deny an enemy unanswerable opener only when blue cannot first-pick it or keep a reliable later answer.
- Preserve flex and fog: avoid banning flexible openers that blue wants to threaten with the first pick.
- Reduce `ban_overlap_risk`: do not spend all bans on generic top map power if those bans merely mirror red's likely denial pattern.

Red owns `last_counter_leverage`: red slot 6 can answer the completed blue trio. Red bans should be evaluated through these purposes:

- `deny_blue_safe_opener`: remove blue-1 candidates that combine high map power, high `opener_safety`, low `counter_exposure`, and strong flex/fog value.
- `preserve_red6_counter_pool`: avoid banning candidates red can hold as final answers unless they are also dangerous blue safe openers.
- Remove flex or counter-denial picks that make `last_pick_counterability` low by hiding the real target until too late.
- Force blue exposure: prefer bans that make blue slot 1 reveal lane, range band, damage type, or comp direction.

This should naturally reduce mirrored bans: blue is protecting and shaping a first-pick path, while red is attacking safe openers and preserving last-pick counter geometry. If both sides still ban the same brawler, the trace must explain why that brawler served both slot powers, not merely that it ranked high on the map.

## Decision Evidence Protocol

Every runtime ban/pick must produce `turn_decision_trace`. This is the decision record used by later audit reports; do not rely on the judge to reconstruct it after the match.

Output depth depends on the caller:

- **Standalone single-hand BP runs**: return the full `turn_decision_trace` below, including `examined_options` and `evidence_roles` per turn.
- **Match-scoped turns** (judge-driven via `run-brawl-stars-bp/references/turn-prompt-template.md`): the judge's per-turn contract is lean — `decision` / `key_reason` / `confidence` / `retrieval`. Do NOT emit the full trace in the reply; **append it to your side's player log** (`{PLAYER_LOG_PATH}`, passed in every 对局信息 block): a section per own turn with the structure below, including the full `examined_options` and the ranking order in which options were considered. The judge reads both player logs after the match and assembles the verbose `.decision-log.md` from them. This is the primary speed/token optimization: per-turn reply shrinks from ~1-3 KB of narrative to a few lines, while the full audit survives in the log and is summarized once at the end.

Required structure (standalone / internal bookkeeping):

```yaml
turn_decision_trace:
  decision_style: conservative | balanced | aggressive | high_variance
  map_problem:
  visible_state:
    map:
    mode:
    own_picks:
    opposing_picks:
    unavailable:
  decision_effort_policy:
    slot_power:
    strategy_bias_default:
    selected_effort: low | high
    explicit_limit:
  query_intent:
    bucket:
    effort: low | high
    neutral_filters:
      include_ids:
      exclude_ids:
      relation_targets:
    why_this_query:
  retrieval_audit:
    recalled_candidates_count:
    fragments_returned:
    payload_kb:
    recalled_fact_summary:
  side_asymmetric_ban_strategy: # required for ban turns
  examined_options: # every option seriously inspected this hand, including selected/rejected/deferred; audit core
    - option:
      why_examined: # why it entered the candidate pool: query window/bucket, relation edge, map duty, or failure-gate check
      evidence_used: # retrieved facts it was judged against (mechanism hook / ladder / monthly)
      verdict: selected | rejected | deferred
      verdict_reason: # one-line player-authored conclusion
  candidate_comparison:
    selected:
    serious_alternatives:
    comparison_axes:
  selected_reason:
  rejected_options:
  risk_and_build_implication:
  evidence_roles: # per-dimension evidence actually used in this turn
    monthly_finals: none | hint | corroborating | contradicting | no_monthly_sample
    ladder_anchor: none | supporting | contradicting | no_ladder_sample
    mechanism: strong | medium | weak   # judged independently of environment samples
    mechanism_basis: # why the mechanism case stands (hook hit / relation edge / failure-gate check)
    environment_unverified: true | false  # mechanism strong but env sample(s) missing
    conflict_resolution: # which dimension won and why
    confidence: high | medium | medium-low | low | ambiguous
```

Use `decision_effort_policy` deliberately. Normal runtime uses only two presets:

| effort | limit | Use when |
| --- | ---: | --- |
| `low` | 24 | normal BP decisions, ban phase, blue slot 1, red slots 2-3, and stable maps |
| `high` | 32 | blue slots 4-5, red slot 6, aggressive or high-variance probes, and high-uncertainty turns |

Default by slot:

| turn | baseline effort |
| --- | --- |
| ban phase | `low` |
| blue slot 1 | `low` |
| red slots 2-3 | `low` |
| blue slots 4-5 | `high` |
| red slot 6 | `high` |
| final_draft_review | selected hydration only |

`strategy_bias` adjusts the baseline but does not replace slot-power reasoning:

- `conservative`: keep the slot baseline and hydrate serious options for risk checks.
- `balanced`: keep the slot baseline.
- `aggressive`: use `high` for ban, blue slots 4-5, red slot 6, and route / punish probes.
- `high_variance`: use `high` for all broad fact windows, then use explicit `--limit` only when intentionally stress-testing a narrow or wider window.

Use `--limit` for single-hand precision when 24 or 32 is not the right budget. The explicit limit is a caller-side recall control, not a BP judgment from the tool.

After slot 6, run a separate `final_draft_review` for each side. This is not another pick turn and cannot change picks. It must use the full visible draft, selected brawler facts, relevant relation targets, and already accepted risks to produce final play instructions:

```yaml
final_draft_review:
  full_draft_read:
    own_comp:
    opposing_comp:
    map:
    mode:
  win_condition:
  play_pattern:
  primary_risks:
  risk_mitigation:
  role_build_plan:
    - brawler:
      role:
      star_power_direction:
      gadget_direction:
      gear_direction:
      evidence_used:
  uncertainty:
  cannot_change_picks: true
# match-scoped：详细思考过程（含 per-turn examined_options 全量 + 查验排序）写入选手日志 {PLAYER_LOG_PATH}，裁判整局结束后读取汇总 verbose decision log
```

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
    - candidate:
      evidence_used:
      map_duties_covered:
      relation_edges_considered:
      accepted_risks:
      required_builds:
      rejection_or_selection_reason:
  examined_options: # every option inspected this hand + why it was examined (audit core for standalone single-hand BP)
    - option:
      why_examined:
      evidence_used:
      verdict: selected | rejected | deferred
      verdict_reason:
  top_decisions:
  draft_eval:
  uncertainty:
    evidence_gaps: # what evidence was missing (e.g. no ladder sample for this brawler, monthly not played)
    decisiveness_boundary: # how much this decision can influence the outcome given the gaps
    outcome_vs_decision_quality: # decision quality is observable even when the single-match outcome is not
retrieval_audit:
  query_focus:
  neutral_filters:
    include_ids:
    exclude_ids:
    relation_targets:
    buckets:
  recalled_candidates_count:
  fragments_returned:
  payload_kb:
  recalled_fact_summary:
turn_decision_trace:
  decision_style:
  map_problem:
  visible_state:
  query_intent:
  retrieval_audit:
  candidate_comparison:
  selected_reason:
  rejected_options:
  examined_options: # every option inspected this hand + why it was examined (audit core; see Decision Evidence Protocol)
  risk_and_build_implication:
final_draft_review:
  full_draft_read:
  win_condition:
  play_pattern:
  primary_risks:
  risk_mitigation:
  role_build_plan:
  cannot_change_picks: true
# match-scoped：详细思考过程写入选手日志 {PLAYER_LOG_PATH}（含 per-turn examined_options 全量 + 查验排序）
```

Each candidate explanation should cite facts from `map_fact_packet`, `fact_window`, or hydrated entity facts. It may use BP terms in the final reasoning, but those terms must be authored by the LLM, not copied from tool-produced decision labels.

`retrieval_audit` is copied from tool metadata plus the LLM's compact summary of what facts were actually recalled. It must be suitable for the judge to rewrite into `decision_audit_narrative`, including recall size and candidate coverage, without exposing long raw JSON.

## Common Mistakes

- Passing BP role names to fact tools instead of neutral entity IDs.
- Treating `fact_window` order as a recommendation.
- Treating conditional relation facts as automatic counters.
- Loading the full runtime JSON instead of using `query_runtime_facts.py` and `hydrate_runtime_facts.py`.
- Inventing meta/T0 claims from memory when the environment evidence is missing from the index. If you need a ladder or monthly number, hydrate the hero and read its `environment_evidence`; do not recite remembered pick rates.
- Treating a small-sample environment number as a stable anchor: a Legendary+ use rate under roughly 2% or a monthly pick count under ~5 is anecdotal, not a trend. Report the sample with the number.
- Ignoring map false-positive filters because a relation edge looks attractive.
- Producing a confident pick without naming which evidence dimension each reason came from, or without reporting confidence when evidence is thin.
