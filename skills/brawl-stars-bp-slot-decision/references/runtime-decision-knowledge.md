# Runtime Decision Knowledge

Use this reference only in `decide` mode. The decider consumes a compiled `runtime_bp_index`; it does not search maintainer notes or rebuild the index during a pick turn.

## decide_input

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

If the index is missing, stale, or does not cover the selected map / mode / pool, run `runtime_index_precheck` before normal decision work. Do not patch the answer with memory.

## runtime_index_precheck

`decide` must have a validated `runtime_bp_index` before ranking candidates.

Use the bundled script for the file-level coordination step:

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

1. Build `runtime_index_key` from patch id, map pool id, available brawler pool, and strength profile hash. If the caller supplied a full `runtime_bp_index`, validate its manifest against the current request.
2. Look for a matching index under `outputs/runtime-bp-index/` or the caller-provided path.
3. If a valid index exists, continue to the Decision Pipeline.
4. If no valid index exists, try to create `<runtime_index_key>.lock` with:

```yaml
state: compiling
owner:
started_at:
compile_input_hash:
attempt: 1
```

5. If lock creation succeeds, run `compile`. When it succeeds, write the index, then release the lock.
6. If the lock already exists, another process is compiling. Poll for the index instead of compiling again.
7. Poll at most 12 times. If the index appears and validates, continue. If it does not appear, check lock age.
8. If the lock is older than 10 minutes, treat it as stale. One process may replace it and retry compile once.
9. If retry also fails or the lock cannot be safely recovered, stop with:

```yaml
uncertainty:
  failure: runtime_index_compile_failed
  reason: missing_or_stale_runtime_bp_index_after_bounded_wait
```

Never wait forever. Never read maintainer discussion pages or memory-only tier lists to bypass the failed compile.

After a successful compile owned by this process, release the lock with:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/runtime_index_precheck.py \
  --repo . \
  --index-key "<runtime_index_key>" \
  --release-lock \
  --json
```

## Decision Pipeline

1. Run `runtime_index_precheck`, then read `runtime_bp_index.manifest` and verify map, mode, pool, patch, and strength profile.
2. Build `mode_objective_profile` from `map_duties`.
3. Build `map_factor_summary`: objective contract, hard gates, terrain state plan, slot pressure, false-positive filters.
4. Update `draft_state`: picks, bans, revealed plans, role gaps, protected picks, exposed picks.
5. Determine current `slot_policy`.
6. Run `hard_gate_result`: `must_pick`, `must_ban`, `must_answer`, `must_avoid`.
7. Apply `strength_context` from the index without inventing tiers.
8. Derive required capabilities before naming heroes.
9. Run `balanced_threat_probe`.
10. Generate 2-4 candidate decisions from index entries.
11. Write `candidate_eval` for each.
12. Rank by slot value, strategy bias, map duty fit, matchup conditions, strength evidence, and exposure risk.

## slot_policy

| Slot | Main job | Prefer | Reject |
| --- | --- | --- | --- |
| 1 | Stable first pick; establish an extendable plan; cover a non-negotiable map or mode duty. | Flexible brawlers with narrow counter windows and real objective conversion. | Picks needing later protection, cheap 2-3 responses, or only coarse map tags. |
| 2-3 | Answer enemy slot 1 while creating the second team's first win route. | One answer plus one plan-builder; paired picks that pressure 4-5 in different ways. | Two purely defensive picks, or two picks sharing the same hard weakness. |
| 4-5 | Answer enemy 2-3, repair own slot 1, complete duties, and avoid a slot-6 collapse. | Picks that cover gaps and reduce last-pick punishment. | Leaving vision, wallbreak, anti-aggro, safe DPS, zone body, scoring window, or thrower answer open. |
| 6 | Final punish or final repair after all enemy picks are known. | High-upside punish when own core duties are covered and enemy has no repair slot. | Gambling on execution, ignoring missing duties, or selecting a name-counter without route proof. |

For paired slots, evaluate the pair as one unit.

## hard_gate_result

Hard gates filter candidates before style preference.

```yaml
hard_gate_result:
  must_pick:
  must_ban:
  must_answer:
  must_avoid:
  reason:
```

Examples:

- Heist needs effective safe pressure, defense, or counter-race value.
- Gem Grab needs mine control, carrier safety, or a credible carrier punish route.
- Bounty needs low-risk pressure, vision, or reliable kill confirmation.
- Hot Zone needs standing, clearing, or denying zone time.
- Brawl Ball needs scoring conversion, wall/goal handling, or defensive reset.
- Knockout needs first-kill pressure, collapse, late-circle plan, or anti-engage.

## balanced_threat_probe

Run this before ranking, even with `strategy_bias: balanced`.

Create a `proactive_threat_candidate` when all are true:

- The index exposes a route, pocket, grass lane, wall edge, goal window, safe entry, carrier retreat, zone entrance, or thrower pocket that a tank/assassin can actually reach.
- The route has `route_endpoint_payoff`: score, safe damage, gem drop, star pick, thrower removal, zone flip, carrier peel, or forced defender resource.
- Enemy remaining answers are unavailable, banned, picked away, overloaded, or false-positive on this map.
- The candidate has a named build, teammate support, or timing plan when needed.

The candidate does not have to win. It must be honestly evaluated beside control, range, sustain, thrower, spawnable, and utility options. Do not apply style-only demotion; use `do_not_demote_tank_assassin_for_style_alone`.

## candidate_eval

```yaml
candidate_eval:
  candidate:
  decision_type: pick | ban
  purpose:
  map_factor_fit:
  mode_fit:
  strength_fit:
  role_coverage:
  conditional_matchups:
  build_requirement:
  terrain_state_dependency:
  exposure_risk:
  likely_enemy_response:
  verdict: prefer | playable | conditional | reject | ban_priority
```

Each eval must name at least one active map duty or matchup condition from the index. If it cannot, reject the candidate.

## Strategy Bias

Apply bias only after hard gates:

| bias | Pick/ban preference | Risk posture |
| --- | --- | --- |
| `conservative` | stable first picks, flexible role coverage, low-exposure bans | demote volatile threats unless routes and peel are proven |
| `balanced` | strongest map/mode fit plus one proactive threat check | compare stable and proactive routes when both are legal |
| `aggressive` | route-based engage, last-pick punish, early pressure if counters are constrained | allow threats when route, build, and follow-up are explicit |
| `high_variance` | unusual punish lines and stress-test picks | allowed only with written failure modes and recovery plan |

Bias cannot make a false-positive map fit viable.

## bp_recommendation

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

Include 2-4 top decisions. For each decision include `why_now`, build, risk control, likely enemy response, and next step.

## Runtime Failure Modes

- Single-pick output without alternatives.
- Coarse map tags used as direct scores.
- Unconditional counter claims.
- Strength tier used without map fit.
- Strategy bias used to bypass failure conditions.
- Missing proactive threat probe in balanced drafts.
- Candidate copied from index without explaining active conditions.
