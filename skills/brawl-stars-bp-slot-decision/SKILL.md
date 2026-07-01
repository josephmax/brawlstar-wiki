---
name: brawl-stars-bp-slot-decision
description: Use when deciding Brawl Stars Ranked Ban Pick picks or bans for a specific draft slot, evaluating slot 1, 2-3, 4-5, or 6 decisions, comparing candidate brawlers, judging bans, counter-picks, map fit, hard gates, or ideal BP choices from this vault.
---

# Brawl Stars BP Slot Decision

## Core Principle

Make each BP slot decision from the vault's stable runtime layer, not from memory, tier lists, or raw strength. The ideal slot decision is the pick or ban that best satisfies current hard gates, map duties, mode objectives, role gaps, matchup conditions, and future exposure risk.

Strength matters when there is evidence. Do not ignore current meta pressure or overpowered brawlers, but do not invent tier lists from memory. Treat strength as a separate evidence layer that can raise or lower priority only after map/mode duties and counter availability are checked.

## Required Reads

Always read these files before a serious BP answer:

- `wiki/index.md`
- `wiki/syntheses/BP-推理DSL规范.md`
- `wiki/syntheses/条件化对位模型.md`
- `wiki/syntheses/Ban-Pick-问题拆分.md`
- `wiki/syntheses/地图特征建模Schema.md`
- `wiki/syntheses/地图因素BP表达规范.md`
- `wiki/syntheses/Ranked-Season-46-地图Map-Profile总览.md`
- `wiki/syntheses/英雄BP建模执行状态.md`
- `wiki/syntheses/BP-条件化对位边索引.md`
- `wiki/syntheses/BP-英雄地图特征适配索引.md`

Then read the relevant single-map page under `wiki/entities/maps/`, relevant brawler pages under `wiki/entities/brawlers/`, and any source pages only when a stable page points to them or a claim needs provenance.

Use `scripts/bp_index.py` to find likely pages and reviewed runtime-index hits:

```bash
python3 skills/brawl-stars-bp-slot-decision/scripts/bp_index.py \
  --repo . \
  --map "Safe Zone" \
  --brawler "Brock" \
  --enemy "Mortis" \
  --json
```

Treat script output as retrieval only. It does not rank candidates and does not replace reading the matched pages.

## Input Contract

Normalize the user request into:

```yaml
bp_case:
  map:
  mode:
  current_global_slot: 1 | 2 | 3 | 4 | 5 | 6
  our_picks:
  enemy_picks:
  bans:
  candidate_pool:
  known_player_constraints:
  strategy_bias: conservative | balanced | aggressive | high_variance
  strength_context:
    source: stable_wiki | user_supplied | source_page | unknown
    meta_pressure:
    overpowered_or_t0_exception:
    counter_availability:
    balance_volatility:
```

If `map`, `mode`, or current slot is missing, state that the conclusion is incomplete. Ask only when the missing field changes the decision; otherwise proceed with explicit assumptions.

## Decision Pipeline

1. Read the required runtime pages and target map/brawler pages.
2. Build `mode_objective_profile`: define how this mode wins on this map.
3. Build `map_factor_summary`: active objective contract, map BP factors, duty coverage, terrain state plan, false-positive alerts.
4. Update `draft_state`: known picks, bans, revealed plans, role gaps, protected picks, exposed picks.
5. Update `pick_slot_state`: team side, known own/enemy picks, remaining enemy answers, current slot job.
6. Run `hard_gate_result`: `must_pick`, `must_ban`, `must_answer`, `must_avoid`.
7. Check `strength_context`: current meta pressure, overpowered_or_t0_exception, balance volatility, and whether counters are realistic in this map/slot.
8. Derive required capabilities before naming heroes.
9. Run `balanced_threat_probe`: identify whether the current map/draft exposes a real `route_based_tank_or_assassin` lane.
10. Generate 2-4 candidate decisions from available heroes or bans.
11. For each candidate, write `candidate_eval`: purpose, map factor fit, mode fit, strength fit, role coverage, conditional matchups, build requirement, exposure risk, likely enemy response.
12. Rank by current slot value, strategy bias, and evidence-backed strength context; never by isolated hero strength alone.

## Proactive Threat Probe

Before ranking picks, run `balanced_threat_probe` even when `strategy_bias: balanced`. This prevents balanced drafts from collapsing into only long-range/control/sustain shells.

Create a `proactive_threat_candidate` when all are true:

- The map exposes a route, pocket, grass lane, wall edge, goal window, safe entry, carrier retreat, zone entrance, or thrower pocket that a tank/assassin can actually reach.
- The route has `route_endpoint_payoff`: score, safe damage, gem drop, star pick, thrower removal, zone flip, carrier peel, or forced defender resource.
- Enemy remaining answers are not a clear hard gate, or those answers are already banned, picked elsewhere, on cooldown in the plan, or must cover a different route.
- The candidate can name required teammate support or build when needed.

For every pick turn, the 2-4 candidate decisions must include at least one proactive threat candidate, including a tank/assassin, unless hard_gate_result.must_avoid or a map false-positive filter explicitly rules it out. If ruled out, write the route that failed and the exact blocker. Do not simply omit tanks/assassins because they are volatile.

The proactive candidate does not have to be the top decision. It must be honestly evaluated beside control, range, sustain, and spawnable options.

## Slot Policies

| Slot | Main job | Prefer | Reject |
| --- | --- | --- | --- |
| 1 | Stable first pick; establish an extendable plan; cover a non-negotiable map/mode duty. | Flexible brawlers with narrow counter windows and real objective conversion. | Picks that need later protection, expose a cheap 2-3 response, or only hit a coarse map tag. |
| 2-3 | Answer enemy slot 1 while creating the second team's first win route. | One answer plus one plan-builder; paired picks that pressure 4-5 in different ways. | Two purely defensive picks, or two picks sharing the same hard weakness. |
| 4-5 | Answer the enemy 2-3 pair, repair/protect own slot 1, complete basic duties, and avoid a slot-6 collapse. | Picks that both cover gaps and reduce last-pick punishment. | Leaving vision, wallbreak, anti-aggro, safe DPS, zone body, scoring window, or thrower answer open when slot 6 can exploit it. |
| 6 | Final punish or final repair after all enemy picks are known. | High-upside punish only when own core duties are already covered and enemy has no remaining repair slot. | Gambling on execution, ignoring missing core duties, or selecting a name-counter without route/condition proof. |

For paired slots, evaluate the pair as a unit. Slot 2 and 3 should not be two independent "good picks"; slot 4 and 5 should not leave one structural failure for enemy slot 6.

## Candidate Scoring Heuristic

Use this as ordering logic, not a numeric formula:

1. Hard gates beat everything.
2. Mode objective and map duty coverage beat matchup comfort.
3. A conditional matchup counts only when its `active_when` conditions match the map, mode, comp, and build.
4. Evidence-backed `overpowered_or_t0_exception` can create a must-pick or must-ban, but only if the map/mode does not provide cheap reliable answers.
5. Slot exposure can demote an otherwise strong candidate.
6. Build requirements must be explicit when they change the candidate's role.
7. A ban is ideal only when it removes a low-cost route, protects a real plan, prevents a hard gate, or removes an evidence-backed overpowered route that picks cannot answer efficiently.
8. Use `do_not_demote_tank_assassin_for_style_alone`: do not demote a route-based tank or assassin only because it is volatile. Demotion requires a named failed route, missing `route_endpoint_payoff`, or a realistic remaining counter.
9. When a tank/assassin route is valid and enemy answers are constrained, treat it as structural pressure, not high variance by default.

## Strength Context

Use this object when the request, source pages, user notes, or current wiki pages provide strength information:

```yaml
strength_context:
  source: stable_wiki | user_supplied | source_page | unknown
  meta_pressure:
    - brawler:
      signal: t0 | overpowered | high_pick_ban | strong | normal | weak
      reason:
      evidence_ref:
  overpowered_or_t0_exception:
    must_pick:
    must_ban:
    still_requires_map_fit:
    cheap_answers_available:
  counter_availability:
    realistic_answers:
    answers_banned_or_taken:
    answers_false_positive_if:
  balance_volatility:
    patch_sensitive:
    confidence:
```

Rules:

- If strength source is `unknown`, state that meta strength was not available and do not fabricate tiers.
- If a hero is evidence-backed T0/overpowered and reliable answers are banned, unavailable, or map-false-positive, promote it into `hard_gate_result.must_pick` or `must_ban`.
- If a hero is strong but invites cheap slot response on this map, keep it in candidate eval instead of hard gate.
- Do not let strength erase failure modes. Example: a strong thrower on a wall map still needs anti-dive or wallbreak protection; a strong assassin still needs a route and endpoint safety.

## Strategy Bias

Apply the judge-provided `strategy_bias` after hard gates and strength context:

| bias | Pick/ban preference | Risk posture |
| --- | --- | --- |
| `conservative` | stable first picks, flexible role coverage, low exposure bans | demote volatile tanks/assassins unless all routes and peel are proven |
| `balanced` | default BP DSL ordering plus one proactive threat check | use strongest map/mode fit with manageable exposure, but must include at least one proactive threat candidate, including a tank/assassin, unless hard_gate_result.must_avoid or map false-positive filters rule it out |
| `aggressive` | route-based engage, last-pick punish, early pressure if counters are constrained | allow tanks/assassins when map route, build, and teammate follow-up are explicit |
| `high_variance` | unusual punish lines and stress-test picks | allowed only with written failure modes and recovery plan |

The bias changes ranking among viable candidates; it cannot make a false-positive map fit viable. Balanced is not conservative: it must compare one proactive route to one stable/control route when both are legal.

## Required Output

Return a compact BP recommendation with:

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

Include 2-4 top decisions. For each decision include `why_now`, required build, risk control, likely enemy response, and next step.

Each ban or pick must include:

```yaml
decision_detail:
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
- Do not treat `A counters B` as unconditional. Explain mechanism, active conditions, fails conditions, and BP use.
- Do not read version/meta audit pages as runtime overlays. If a version item is not merged into stable hero/map/index fields, keep it out of the decision or mark it as uncertainty.
- Do not ignore evidence-backed T0/overpowered signals just because they are not elegant map theory; strength can become a hard gate when reliable answers are unavailable.
- Do not invent T0/meta claims from memory. If no strength source is provided or present in the wiki, write `strength_context.source: unknown`.
- Do not let `strategy_bias: aggressive` justify a tank/assassin without route, follow-up, and endpoint safety.
- Do not include `Buzz Lightyear` in BP-active pools.
- Do not let the script's retrieved lines become the answer. Use them to choose what to read next.
