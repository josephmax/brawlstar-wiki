---
name: brawl-stars-bp-slot-decision
description: Use when compiling or using a Brawl Stars Ranked Ban Pick runtime index, deciding a specific draft slot, evaluating bans or picks, comparing candidates, or checking map fit, hard gates, counter-picks, strategy bias, and strength context from this vault.
---

# Brawl Stars BP Slot Decision

## Core Boundary

This skill has two modes:

- `compile`: read stable entity facts and strength input, then generate a `runtime_bp_index`.
- `decide`: read the compiled `runtime_bp_index`, current draft state, and runtime decision rules, then return one ban or pick recommendation set.

The skill must not use the wiki's synthesis/topic discussion layer as a runtime dependency. Those pages are maintainer workspace, not player-facing knowledge. The skill is self-contained through its own references and stable entity pages.

## Mode Required Reads

### compile

Read:

- `skills/brawl-stars-bp-slot-decision/references/compile-knowledge.md`
- Relevant map pages under `wiki/entities/maps/`
- Relevant brawler pages under `wiki/entities/brawlers/`
- User, judge, or external `strength_profile` supplied for this session

Output:

- `runtime_bp_index`

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
- The compiled `runtime_bp_index`
- Current ban/pick state, side, slot, available pool, and `strategy_bias`

If no `runtime_bp_index` exists, run `compile` first or state that the decision is incomplete. Do not silently fall back to maintainer discussion pages.

## Input Contract

Normalize requests into one of these objects:

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

```yaml
decide_input:
  runtime_bp_index:
  map:
  mode:
  current_global_slot: 1 | 2 | 3 | 4 | 5 | 6
  our_picks:
  enemy_picks:
  bans:
  candidate_pool:
  known_player_constraints:
  strategy_bias: conservative | balanced | aggressive | high_variance
```

If `map`, `mode`, or slot is missing, state the assumption. Ask only when the missing field changes the decision.

## Compile Summary

`compile` converts stable facts into a compact runtime index:

- `map_duties`: objective contracts, required capabilities, route gates, false-positive filters.
- `brawler_cards`: capabilities, builds, failure modes, strength visibility, proof thresholds.
- `map_brawler_edges`: map fit, terrain dependency, objective conversion, failure conditions.
- `draft_edges`: conditional matchups, bans that matter, protected picks, exposed routes.

Strength matters only as a separate evidence layer. A high strength signal can raise priority or become a must-pick / must-ban only after map duties, counter availability, and failure modes are checked.

The compiled index should expose `strength_context` with `meta_pressure`, `overpowered_or_t0_exception`, counter availability, and balance volatility. Unknown strength remains explicit uncertainty, not a license to invent tiers.

## Decide Summary

`decide` uses the runtime index to produce `candidate_eval` and `bp_recommendation`.

Ordering logic:

1. Hard gates beat everything.
2. Mode objective and map duty coverage beat isolated matchup comfort.
3. Conditional matchups count only when their active conditions match the map, mode, comp, build, and slot.
4. Evidence-backed `overpowered_or_t0_exception` can become a hard gate when cheap reliable answers are unavailable.
5. Slot exposure can demote otherwise strong candidates.
6. Strategy bias changes ranking among viable candidates; it cannot make a false-positive map fit viable.

Always run `balanced_threat_probe`. A balanced draft must still evaluate one legal `route_based_tank_or_assassin` / `proactive_threat_candidate` when the map exposes a real route, endpoint payoff, and constrained enemy answer set. Use `do_not_demote_tank_assassin_for_style_alone`: demotion requires a named failed route, missing `route_endpoint_payoff`, or realistic remaining counter.

For `balanced`, the 2-4 candidate decisions must include at least one proactive threat candidate, including a tank/assassin, unless hard_gate_result.must_avoid or map false-positive filters rule it out.

## Output Contract

Return a compact recommendation:

```yaml
bp_recommendation:
  context_summary:
  hard_gate_result:
  active_conditions:
    map_factor_summary:
    activated_matchups:
    disabled_matchups:
    stable_knowledge_refs:
    strength_context:
  required_capabilities:
  candidate_evals:
  top_decisions:
  draft_eval:
  uncertainty:
```

Each candidate must include:

```yaml
candidate_eval:
  candidate:
  decision_type: pick | ban
  why_now:
  construct_direction:
  capabilities_provided:
  answers_enemy_picks:
  answers_map_factors:
  risks_removed:
  new_risks_created:
  followup_needs:
  rejected_options:
```

## Common Mistakes

- Do not output a single pick without alternatives.
- Do not use `open`, `wall density`, `water`, or `summary_tags` as direct scoring signals.
- Do not treat `A counters B` as unconditional; explain mechanism, active conditions, fail conditions, and BP use.
- Do not invent T0/meta claims from memory. If no strength source is provided, write `strength_context.source: unknown`.
- Do not let `strategy_bias: aggressive` justify a tank/assassin without route, follow-up, and endpoint safety.
- Do not let `balanced` collapse into only range/control/sustain shells.
- Do not let `scripts/bp_index.py` output become the answer; it only locates stable pages and skill references.
