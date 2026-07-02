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

  map_duties:
    map:
      mode:
      objective_contracts:
      required_capabilities:
      route_gates:
      terrain_state_plan:
      false_positive_filters:
      slot_pressure:
        early_pick:
        mid_pick:
        late_pick:
        ban:

  brawler_cards:
    brawler:
      capabilities:
      builds:
      objective_contracts:
      map_hooks:
      failure_modes:
      slot_notes:
      strength_visibility:
        tier:
        source:
        confidence:
      proof_threshold:

  map_brawler_edges:
    map:
      brawler:
        fit: strong | playable | conditional | weak | reject
        active_routes:
        objective_conversion:
        terrain_dependency:
        required_build:
        failure_if:
        false_positive_if:

  draft_edges:
    brawler:
      answers:
        - target:
          active_when:
          fails_when:
          bp_use: early_pick | mid_pick | late_pick | ban | avoid
      is_answered_by:
        - target:
          active_when:
          fails_when:
          mitigation:
```

## Strength Integration

Strength is a separate layer, not a rewrite of entity facts.

Rules:

- Unknown strength means `strength_context.source: unknown`; do not fabricate tiers.
- Global strength can raise or lower priority, but map and mode duties still filter viability.
- Mode or map strength overrides global strength only inside its declared scope.
- A weak hero may remain a counter line, but the index must raise its `proof_threshold`.
- A high-tier hero can become `must_pick` or `must_ban` only when reliable answers are unavailable, banned, picked away, or false-positive on this map.

Compile strength into:

```yaml
strength_context:
  source:
  meta_pressure:
  overpowered_or_t0_exception:
  counter_availability:
  balance_volatility:
```

## Quality Gates

Reject or mark incomplete any index entry that lacks:

- a map or mode context
- a route, position, or objective payoff
- a failure condition
- a slot use
- a source entity reference

The output must be smaller than the underlying wiki pages and must not require the decider to search the wiki.

## Compiler Output Discipline

Write generated indexes to `outputs/` or another caller-provided intermediate path. Do not write generated runtime indexes back into the long-term wiki unless the user explicitly asks for an audit artifact.
