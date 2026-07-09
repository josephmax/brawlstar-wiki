# Compile Knowledge

Use this reference only in `compile` mode. The goal is to generate a session-local `runtime_bp_index` from stable entity facts plus the supplied strength profile.

## Boundary

Allowed inputs:

- This reference.
- Relevant `wiki/entities/maps/` pages.
- Relevant `wiki/entities/brawlers/` pages.
- User, judge, community, or external `strength_profile` supplied for this session.
- Current map pool and available brawler pool supplied by the user, judge, or caller.

Forbidden inputs:

- Maintainer discussion pages.
- Raw source captures.
- Historical audit pages.
- Old hand-written decision indexes.
- Memory-only tier lists.

If the needed map pool or strength profile is missing, compile a partial index and mark the gap in `manifest.missing_inputs`.

## Compile Modes

### Default current-version compile

Use this when the caller does not provide a strength profile.

```yaml
strength_profile:
  profile_id: ikaoss11-july-2026-screenshot
  owner: runtime_default
  scope: global
  path: skills/brawl-stars-bp-slot-decision/references/default-strength-profile.json
```

The default profile is the adopted first-version strength input from `wiki/sources/iKaoss11-July-2026-Strength-Profile.md`, copied into the skill reference layer for runtime use. The compiler still reads stable map and brawler facts; strength remains a separate layer and must not rewrite entity pages. Runtime exposes only map-scoped candidate strength from `map_pool_signature[*].candidate_index`, not a top-level strength table. Do not infer S/A/B tiers from memory, old reports, or maintainer synthesis pages.

An explicit empty profile is still allowed when the caller wants no strength signal:

```yaml
strength_profile:
  profile_id: default_current_version_unknown
  owner: runtime_default
  scope: global
  entries: []
```

### User-supplied strength compile

This mode is reserved for caller-provided current-version judgment. Treat user entries as a separate strength layer that can change priority, proof thresholds, and ban pressure. It must not rewrite:

- map structure
- hero capability facts
- matchup mechanisms
- map hooks
- stable failure modes

When user strength input is partial, compile the missing heroes as unknown and record the coverage gap in `manifest.missing_inputs`.

### Strength order inside tiers

`strength_profile` tier order is not only categorical. Within each tier, earlier entries are stronger than later entries. Compile must preserve:

- `tier`
- `tier_rank`
- `tier_size`
- `total_rank`
- `ordered_score`
- `within_tier_score`

For example, `S: [Brock, 8-Bit, Meg]` means Brock has stronger current-version pressure than 8-Bit, and 8-Bit stronger than Meg, even though all three remain S-tier.

### Scoped strength layers

`strength_profile` can carry three independent scopes:

- map-specific profile for `mode/map`
- mode-specific profile for `mode`
- global profile

Map-specific strength is an explicit map judgment, not something inferred from global order. Strength remains a current-version priority signal after map duties and candidate fit have been established; it must not rewrite `fit`, `map_floor_fit`, or `slot_eligibility`. If a declared scope omits a brawler, compile that brawler as `unknown` in that scope and record the gap in `manifest.missing_inputs`.

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
  strength_profile:
    profile_id:
    owner:
    scope: global | mode | map | custom
    entries:
      - brawler:
        mode:
        map:
        tier: S | A | B | C | D | E | unknown
        signal:
        reason:
        evidence_ref:
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

Do not convert coarse labels directly into decisions. `open`, `wall density`, `water`, and similar tags must become route, position, target payoff, failure condition, or slot task before they enter the index.

## runtime_bp_index

The compiled output must be compact and directly consumable by `decide`.

```yaml
runtime_bp_index:
  manifest:
    patch_id:
    map_pool_id:
    strength_profile_id:
    strength_profile_hash:
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
        avoid_without_proof:
      candidate_index:
        brawler:
          fit:
          map_floor_fit:
          mode_contract_fit:
          tier:
          rank:
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

  matchup_index:
    by_brawler:
      brawler:
        answers:
        is_answered_by:

  evidence_refs:
    strength_profile:
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

## Strength Integration

Strength is a separate layer, not a rewrite of entity facts.

Rules:

- Unknown strength means `strength_context.source: unknown`; do not fabricate tiers.
- Global, mode, or map strength can raise or lower runtime priority only through `strength_weight`; compile must keep ability fit independent from tier.
- Mode or map strength applies only inside its declared scope.
- `mode_contract_hit` is only evidence that the brawler page has a contract for this mode. It is not map eligibility. Store `mode_contract_fit: evidence_only` when present, never `playable`.
- Only concrete map signals such as `active_hook_ids` or `matched_capabilities` can make `map_floor_fit: strong` or `fit: strong`. A brawler with only `mode_contract_hit` must remain `fit: weak` until current draft context activates a counter line.
- `early_pick`, `response_pick`, `late_pick`, and `ban_pressure` projections require concrete map fit first. Preserve all concrete map candidates that are legal for that slot; do not cut projection to the first few strength-ranked names. Strength rank may order compact recall within eligible groups, but it must not create eligibility or decide the coverage width.
- `map_floor_fit` records map-evidence level; `mode_contract_fit` records mode-contract evidence only. Runtime must not combine `mode_contract_fit` into map fit.
- `slot_eligibility` is a compile-time guardrail based on map evidence, not tier or mode mention. A brawler with only mode-level evidence is not eligible for early, response, or late projection.
- `recall_channels` separates why a brawler may be queried. `map_core` comes from map evidence; `counter_response` means the brawler has matchup edges and can be recalled only when current enemy picks activate those edges.
- `conditional_lift` stores only compact trigger names. For `enemy_targets_answered_by_candidate`, `decide` must check the current slot and enemy picks against `matchup_index` before granting a lift; this trigger does not create a normal map candidate.
- `failure_gates` is the only candidate-index risk key; do not duplicate the same IDs as `risk_ids`.
- A weak hero may remain a counter line, but the index must raise its `proof_threshold`.
- A high-tier hero can become `must_pick` or `must_ban` only at runtime, after `strength_weight`, reliable answers, bans, picked-away options, and map false positives are evaluated.

Compile strength into:

```yaml
strength_context:
  source:
  meta_pressure:
  overpowered_or_t0_exception:
  counter_availability:
  balance_volatility:
```

Use the bundled compiler to produce the first runtime artifact:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/compile_runtime_index.py \
  --repo . \
  --strength-profile skills/brawl-stars-bp-slot-decision/references/default-strength-profile.json \
  --output outputs/runtime-bp-index/default-tierlist-all-maps-thin.json
```

Use `--map "Safe Zone"` only when compiling a single-map index. Omit `--map` to compile the full map pool under `wiki/entities/maps/`.

If you need an audit/debug file:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/compile_runtime_index.py \
  --repo . \
  --output outputs/runtime-bp-index/default-tierlist-all-maps-thin.json \
  --debug-output outputs/runtime-bp-index/debug/default-tierlist-all-maps-debug.json
```

## Quality Gates

Reject or mark incomplete any index entry that lacks:

- a map or mode context
- a route, position, or objective payoff
- a failure condition
- a slot use
- a source entity reference

The output must be smaller than the underlying wiki pages and must not require the decider to search the wiki. Because v2 stores global brawler cards and matchup edges once, file size is allowed to be larger than the earlier minimal index, but tool returns must remain small:

- single-map runtime-v2 index: under 1.5MB
- current full map pool runtime-v2 index: under 3MB
- normal `query_runtime_facts.py` return: expected low single-digit KB for a bounded fact window
- normal `hydrate_runtime_facts.py` return: expected low single-digit to low tens of KB for 2-4 entities

## Compiler Output Discipline

Write generated indexes to `outputs/` or another caller-provided intermediate path. Do not write generated runtime indexes back into the long-term wiki unless the user explicitly asks for an audit artifact.
