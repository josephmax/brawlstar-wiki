# Runtime Decision Knowledge

Use this reference only in `decide` mode. The decider consumes a compiled `runtime_bp_index` through neutral fact-retrieval tools. It does not search maintainer notes, load the full index into the prompt, rebuild the index during a pick turn, or delegate BP judgment to scripts.

## Core Boundary

工具只做事实召回. The tools may:

- validate that a compiled index covers the requested map.
- return a compact map fact packet.
- return entity fact windows selected by neutral `include-id`, `exclude-id`, `relation-target`, and bucket filters.
- return conditional relation facts as source/target edges.
- return strength evidence and source refs.

The tools must not:

- receive business-role parameters such as `our_pick`, `enemy_pick`, `bans`, `strategy_bias`, `strength_weight`, or `decision_seed`.
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
  strength_weight: 0.0-1.0

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

- `--include-id`: force an entity's facts into the returned fact window.
- `--exclude-id`: exclude an entity from the returned fact window.
- `--relation-target`: return conditional relation facts involving this target entity.
- `--bucket`: select a precompiled retrieval bucket by id. The bucket id is an index partition, not a recommendation.
- `--effort`: recall budget preset. `low=24` and `high=32`; default is `low`.
- `--field`: optional caller hint for requested fields.
- `--limit`: explicit override for entity fragments. Prefer `--effort` unless a caller needs a precise budget.
- `--summary`: emit an agent-readable summary table. Use it for manual inspection and audit drafting instead of writing fragile one-off `python3 -c` parsers.

Output:

- `manifest`: compact index identity.
- `scope`: map and mode.
- `request`: neutral retrieval request echo.
- `map_fact_packet`: source ref, objective contracts, required capabilities, route gates, hard gates, and false-positive filters.
- `fact_window`: returned entities with map fit evidence, strength evidence, scalar `strength_tier`, scalar `strength_rank`, map hook IDs, matched capabilities, failure gates, build IDs, selected runtime-card fragments, `runtime_card_counts`, `conditional_relations`, and `relation_count`.
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

Hydration returns each requested entity's runtime-card facts, retrieval bucket hits, map strength, conditional relations, and source refs. The JSON keeps `entities` as a dictionary keyed by brawler and also returns `entity_window` as a list for safe iteration. Each entity includes scalar `strength_tier`, scalar `strength_rank`, `runtime_card_counts`, and `relation_count`; use those instead of comparing nested dictionaries. If returned facts are not enough to support a claim, mark the claim uncertain or reject that line of reasoning; do not bypass the tool by reading full wiki pages in decide mode.

## LLM Decision Pipeline

1. Run `runtime_index_precheck`; continue only with a validated `index_path`.
2. Translate BP state into neutral tool filters:
   - already unavailable entities -> `--exclude-id`
   - revealed or important entities to inspect -> `--include-id`
   - visible entities whose relation edges matter -> `--relation-target`
   - desired evidence window -> `--bucket`
3. Call `query_runtime_facts.py`.
4. Read `map_fact_packet` first: objective, route gates, hard gates, and false-positive filters define the map problem.
5. Read `fact_window` as evidence, not as a recommendation. A returned entity is merely relevant enough to inspect.
6. Interpret conditional relations yourself. A relation edge is not automatically a counter, answer, ban, or pick.
7. Compare candidates by explicit reasoning: map duty coverage, relation activation, current draft needs, failure modes, required builds, strength evidence, and strategy bias.
8. Call `hydrate_runtime_facts.py` for the few entities whose detailed facts matter.
9. Produce `candidate_eval`, `turn_decision_trace`, and `bp_recommendation` in the LLM response.
10. Produce `retrieval_audit` from the actual tool requests and `retrieval_summary` values. This is evidence bookkeeping only: include query focus, neutral filters, recalled entities, `fragments_returned`, and `payload_kb`; do not turn it into a recommendation.

## Reasoning Rules

- Do not rank by strength first and then explain around it. Strength is a separate evidence layer.
- Do not let a tier or mode mention create map fit. Map fit must come from concrete map hooks, objective contracts, or matched capabilities.
- Do not treat relation edges as unconditional. Name mechanism, active conditions, fail conditions, and whether the current map/draft activates them.
- Do not treat retrieval order as final ranking. Retrieval order exists to keep the evidence window small.
- Do not force a counter line when map duties or failure modes make it poor.
- Do not let strategy bias make a false-positive map fit viable.
- If a candidate lacks evidence for the current map objective, say so and either reject it or mark it as a speculative exception.

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

Required structure:

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
  candidate_comparison:
    selected:
    serious_alternatives:
    comparison_axes:
  selected_reason:
  rejected_options:
  risk_and_build_implication:
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
      strength_context:
      accepted_risks:
      required_builds:
      rejection_or_selection_reason:
  top_decisions:
  draft_eval:
  uncertainty:
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

Each candidate explanation should cite facts from `map_fact_packet`, `fact_window`, or hydrated entity facts. It may use BP terms in the final reasoning, but those terms must be authored by the LLM, not copied from tool-produced decision labels.

`retrieval_audit` is copied from tool metadata plus the LLM's compact summary of what facts were actually recalled. It must be suitable for the judge to rewrite into `decision_audit_narrative`, including recall size and candidate coverage, without exposing long raw JSON.

## Common Mistakes

- Passing BP role names to fact tools instead of neutral entity IDs.
- Treating `fact_window` order as a recommendation.
- Treating conditional relation facts as automatic counters.
- Loading the full runtime JSON instead of using `query_runtime_facts.py` and `hydrate_runtime_facts.py`.
- Inventing T0/meta claims from memory when strength evidence is missing.
- Ignoring map false-positive filters because a relation edge looks attractive.
