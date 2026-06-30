---
name: brawl-stars-bp-slot-decision
description: Use when deciding Brawl Stars Ranked Ban Pick picks or bans for a specific draft slot, evaluating slot 1, 2-3, 4-5, or 6 decisions, comparing candidate brawlers, judging bans, counter-picks, map fit, hard gates, or ideal BP choices from this vault.
---

# Brawl Stars BP Slot Decision

## Core Principle

Make each BP slot decision from the vault's stable runtime layer, not from memory, tier lists, or raw strength. The ideal slot decision is the pick or ban that best satisfies current hard gates, map duties, mode objectives, role gaps, matchup conditions, and future exposure risk.

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
```

If `map`, `mode`, or current slot is missing, state that the conclusion is incomplete. Ask only when the missing field changes the decision; otherwise proceed with explicit assumptions.

## Decision Pipeline

1. Read the required runtime pages and target map/brawler pages.
2. Build `mode_objective_profile`: define how this mode wins on this map.
3. Build `map_factor_summary`: active objective contract, map BP factors, duty coverage, terrain state plan, false-positive alerts.
4. Update `draft_state`: known picks, bans, revealed plans, role gaps, protected picks, exposed picks.
5. Update `pick_slot_state`: team side, known own/enemy picks, remaining enemy answers, current slot job.
6. Run `hard_gate_result`: `must_pick`, `must_ban`, `must_answer`, `must_avoid`.
7. Derive required capabilities before naming heroes.
8. Generate 2-4 candidate decisions from available heroes or bans.
9. For each candidate, write `candidate_eval`: purpose, map factor fit, mode fit, role coverage, conditional matchups, build requirement, exposure risk, likely enemy response.
10. Rank by current slot value, not isolated hero strength.

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
4. Slot exposure can demote an otherwise strong candidate.
5. Build requirements must be explicit when they change the candidate's role.
6. A ban is ideal only when it removes a low-cost route, protects a real plan, or prevents a hard gate that picks cannot answer efficiently.

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
  required_capabilities:
  candidate_evals:
  top_decisions:
  draft_eval:
  uncertainty:
```

Include 2-4 top decisions. For each decision include `why_now`, required build, risk control, likely enemy response, and next step.

## Common Mistakes

- Do not output a single pick without alternatives.
- Do not use `open`, `wall density`, `water`, or `summary_tags` as direct scoring signals.
- Do not treat `A counters B` as unconditional. Explain mechanism, active conditions, fails conditions, and BP use.
- Do not read version/meta audit pages as runtime overlays. If a version item is not merged into stable hero/map/index fields, keep it out of the decision or mark it as uncertainty.
- Do not include `Buzz Lightyear` in BP-active pools.
- Do not let the script's retrieved lines become the answer. Use them to choose what to read next.
