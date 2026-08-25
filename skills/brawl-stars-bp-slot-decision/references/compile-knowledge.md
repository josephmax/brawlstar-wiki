# Compile Knowledge

Use this reference only in `compile` mode. The goal is to generate a session-local `runtime_bp_index` from stable entity facts plus archived environment signals. There is no strength layer: the only environment signal in this system is high-rank pick rate (paired with ban rate), folded in by compile as labeled evidence from the `wiki/environment/` archive. Compile never infers or fabricates environment signals from memory, old tier lists, or maintainer discussion.

## Boundary

Allowed inputs:

- This reference.
- Relevant `wiki/entities/maps/` pages.
- Relevant `wiki/entities/brawlers/` pages.
- The environment archive pointer `wiki/environment/current.json` and the monthly/ladder signal files it references (the only environment inputs).
- Current map pool and available brawler pool supplied by the user, judge, or caller.

Forbidden inputs:

- Maintainer discussion pages.
- Raw source captures.
- Historical audit pages.
- Old hand-written decision indexes.
- Memory-only tier lists, strength profiles, or any tier-based concept.
- Retired strength artifacts (`outputs/_retired/`, `wiki/sources/iKaoss11-July-2026-Strength-Profile.md`, `tools/strength-profile-editor/` outputs).

If the needed map pool is missing, compile a partial index and mark the gap in `manifest.missing_inputs`.

## Environment Signal (high-rank pickrate)

The system's environment signal is `high_rank_pickrate` (Brawl Planet Legendary+ pick layer, `wiki/environment/pickrate.sqlite3`) paired with `ban_rate` (Liquipedia monthly aggregation, `wiki/environment/<YYYY-MM>/archive.sqlite3`). The archive lives under `wiki/environment/` and `current.json` is the machine-readable pointer. **Compile is the only aggregator**: it folds the archived signals into the index as per-brawler `environment_evidence` (`ladder_anchor` / `monthly_finals`) plus `environment_ladder_per_map`. `decide` never reads signal files; it consumes the embedded evidence from the index through `hydrate_runtime_facts.py`.

- With the archive present, `manifest.pickrate_status` is `"loaded"` and `manifest.pickrate_source` records the pointer path; without the pointer (or with `--no-environment`) the slot stays `"empty"`.
- Compile does not invent pick rates, tiers, or rankings. Missing environment evidence is explicit uncertainty; it must not upgrade or demote any candidate.
- Map fit (`fit`, `map_floor_fit`, `slot_eligibility`, projection buckets) comes only from stable map hooks, matched capabilities, and mode contracts. Environment evidence can never create or rewrite those fields.
- The signal enters the decision path only as labeled evidence with provenance (`rank_floor`, `window`, `fetched_at` / `captured_at`, sample denominators), embedded in the index by compile; evidence strength updates with each refresh without changing the framework.
- `manifest.environment_provenance` records the exact pointer, archive id, windows, and sample denominators folded into this index, so every index is traceable to its archived signal inputs.

## compile_input

```yaml
compile_input:
  patch_id:
  map_pool:
    id:
    maps:
      - name:
        mode:
  available_brawlers:
    - name:
  source_policy:
    read_stable_entities_only: true
    no_synthesis_runtime_dependency: true
```

## Entity Extraction

From map pages, extract:

- `map_profile`
- `objective_access`
- lane and route contracts
- `map_bp_factors`
- `hard_gates`
- terrain state assumptions
- false-positive filters

From brawler pages, extract:

- `capability_vector`
- `build_switches`
- `map_feature_hooks`
- `objective_contracts`
- `failure_modes`
- `conditional_matchups`
- `slot_notes`

Only the first `bp_brawler_profile` YAML block is a runtime compile input. Ignore any later `combat_breakpoint_profile` block and never read `balance_breakpoint_audit.v1` or `outputs/balance-breakpoints/` directly. A maintainer must first promote a validated numerical consequence into one of the stable qualitative fields above.

Do not convert coarse labels directly into decisions. `open`, `wall density`, `water`, and similar tags must become route, position, target payoff, failure condition, or slot task before they enter the index.

## runtime_bp_index

The compiled output must be compact and directly consumable by `decide`.

```yaml
runtime_bp_index:
  manifest:
    patch_id:
    map_pool_id:
    pickrate_source: null | wiki/environment/current.json
    pickrate_status: empty | loaded
    environment_provenance: null | {pointer, monthly, ladder}
    source_hash:
    compiler_version:
    compiled_at:
    missing_inputs:

  map_pool_signature:
    map:
      map_context:
        map:
        mode:
        source_ref:
        objective_contracts:
        required_capabilities:
        route_gates:
        hard_gates:
        slot_pressure:
        false_positive_filters:
      candidate_projection:
        early_pick:
        response_pick:
        late_pick:
        ban_pressure:
      candidate_index:
        brawler:
          fit:
          map_floor_fit:
          mode_contract_fit:
          projection_buckets:
          active_hook_ids:
          matched_capabilities:
          mode_contract_hit:
          recall_channels:
            - map_core
            - map_secondary
            - counter_response
          slot_eligibility:
            early_pick:
            response_pick:
            late_pick:
          conditional_lift:
            - enemy_targets_answered_by_candidate
          failure_gates:
          required_build_ids:

  brawler_runtime_cards:
    brawler:
      capability_tags:
      build_switches:
      map_hooks:
      objective_contracts:
      failure_modes:
      slot_notes:
      environment_evidence:   # only when the archive is folded
        ladder_anchor: null | {use_rate, win_rate, window, rank_floor, fetched_at}
        monthly_finals: null | {picks, pick_rate, win_rate_when_picked, ban_rate, window, rank_floor, captured_at}

  environment_ladder_per_map: {}   # only when the archive is folded; per-map rows keyed by map_mode

  matchup_index:
    by_brawler:
      brawler:
        answers:
        is_answered_by:

  evidence_refs:
    maps:
    brawlers:

  audit_summary:
    map_count:
    brawler_count:
    candidate_index_entries:
    cards_with_map_hooks:
    cards_with_matchups:
    runtime_payload_bytes_estimate:
```

Detailed raw extracted `map_duties`, unpruned `brawler_cards`, `map_brawler_edges`, and `draft_edges` belong in optional debug traces, not the runtime index. Generate them only with `--debug-output`.

## Environment Signal Integration

Compile folds the archived environment signal only when `wiki/environment/current.json` resolves (pass `--no-environment` to force the empty slot, or point `--environment-manifest` elsewhere). There is no strength layer and no tier input.

Rules:

- Without the archive, `manifest.pickrate_source` is `null` and `manifest.pickrate_status` is `"empty"`; do not fabricate pick rates or rankings. With the archive, status is `"loaded"` and the per-brawler evidence is labeled with window / rank_floor / fetch or capture time.
- `mode_contract_hit` is only evidence that the brawler page has a contract for this mode. It is not map eligibility. Store `mode_contract_fit: evidence_only` when present, never `playable`.
- Only concrete map signals such as `active_hook_ids` or `matched_capabilities` can make `map_floor_fit: strong` or `fit: strong`. A brawler with only `mode_contract_hit` must remain `fit: weak` until current draft context activates a counter line.
- `early_pick`, `response_pick`, `late_pick`, and `ban_pressure` projections require concrete map fit first. Preserve all concrete map candidates that are legal for that slot; do not cut projection to a short strength-ranked list.
- `map_floor_fit` records map-evidence level; `mode_contract_fit` records mode-contract evidence only. Runtime must not combine `mode_contract_fit` into map fit.
- `slot_eligibility` is a compile-time guardrail based on map evidence, not tier or mode mention.
- `recall_channels` separates why a brawler may be queried. `map_core` comes from map evidence; `counter_response` means the brawler has matchup edges and can be recalled only when current enemy picks activate those edges.
- `conditional_lift` stores only compact trigger names. For `enemy_targets_answered_by_candidate`, `decide` must check the current slot and enemy picks against `matchup_index` before granting a lift; this trigger does not create a normal map candidate.
- `failure_gates` is the only candidate-index risk key; do not duplicate the same IDs as `risk_ids`.
- Ban pressure is map-evidence driven: a candidate enters `ban_pressure` only with `fit: strong` plus concrete map signals. It is not driven by any tier or environment ranking.

Use the bundled compiler to produce the first runtime artifact:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/compile_runtime_index.py \
  --repo . \
  --output outputs/runtime-bp-index/default-runtime-index.json
```

The default `--environment-manifest wiki/environment/current.json` folds the current archived signals into the index when the pointer exists. Use `--no-environment` for a stable-facts-only index, and `--environment-manifest <path>` to fold a different archive snapshot.

Use `--map "Safe Zone"` only when compiling a single-map index. Omit `--map` to compile the full map pool under `wiki/entities/maps/`.

If you need an audit/debug file:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/compile_runtime_index.py \
  --repo . \
  --output outputs/runtime-bp-index/default-runtime-index.json \
  --debug-output outputs/runtime-bp-index/debug/default-runtime-index-debug.json
```

## Quality Gates

Reject or mark incomplete any index entry that lacks:

- a map or mode context
- a route, position, or objective payoff
- a failure condition
- a slot use
- a source entity reference

The output must be smaller than the underlying wiki pages and must not require the decider to search the wiki. Because v2 stores global brawler cards, matchup edges, and the folded environment evidence once, file size is allowed to be larger than the earlier minimal index, but tool returns must remain small:

- single-map runtime-v2 index: under 2MB
- current full map pool runtime-v2 index: under 6MB (environment embedding grows the file; tool windows stay small)
- normal `query_runtime_facts.py` return: expected low single-digit KB for a bounded fact window
- normal `hydrate_runtime_facts.py` return: expected low single-digit to low tens of KB for 2-4 entities (plus the current map's environment ladder rows, projected to the requested heroes)

## Compiler Output Discipline

Write generated indexes to `outputs/` or another caller-provided intermediate path. Do not write generated runtime indexes back into the long-term wiki unless the user explicitly asks for an audit artifact.
