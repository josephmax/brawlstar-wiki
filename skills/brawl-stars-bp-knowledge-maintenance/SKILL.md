---
name: brawl-stars-bp-knowledge-maintenance
description: "Use when maintaining this vault's Brawl Stars BP knowledge: ingesting raw/source materials, creating or repairing brawler BP profiles, modeling maps, running BP profile audits, updating maintenance references, or preparing stable facts for runtime BP skills."
---

# Brawl Stars BP Knowledge Maintenance

This is the maintainer skill for turning source material into stable BP knowledge. It is a domain-specific subset of the vault's `$markdown-llm-wiki` workflow, using the companion skill from `https://github.com/josephmax/skills/tree/main/skills/markdown-llm-wiki`: first enforce wiki intake hygiene, then apply BP modeling rules, then validate that runtime skills can consume only stable facts or generated indexes.

## Required Gate

Before any maintenance task, apply the `LLM-wiki intake gate` from the companion `$markdown-llm-wiki` skill (`https://github.com/josephmax/skills/tree/main/skills/markdown-llm-wiki`):

1. Read `AGENTS.md` and `wiki/index.md`.
2. Keep `raw/` immutable except for explicit capture or cleanup tasks.
3. Create or update `wiki/sources/` before changing stable facts.
4. Preserve provenance, uncertainty, and source boundaries.
5. Update `wiki/index.md` only when navigation changes.
6. Normalize brawler names from user notes, external tier lists, or community slang through `wiki/concepts/英雄名称归一化.md` before writing source summaries, entity updates, or runtime inputs.
7. Append `wiki/log.md` for ingest, important maintenance, audits, and cleanup.

Then load only the relevant reference below.

## Reference Routing

- For layer ownership, runtime boundaries, and two-stage intake, read `references/repo-layering.md`.
- For Fandom, PLP, roster, patch, map, or user-note ingest, read `references/source-ingest.md`.
- For `wiki/entities/brawlers/` profiles, read `references/brawler-modeling.md`.
- For `wiki/entities/maps/` and `map_bp_factor` work, read `references/map-modeling.md`.
- For quality gates, script use, and contract tests, read `references/audit-and-validation.md`.
- For separating maintenance knowledge from `runtime_bp_index`, read `references/runtime-boundary.md`.

## Minimal Request Handling

A caller only needs to name the target brawler or map, such as "update Brock BP knowledge" or "update Center Stage map BP knowledge." Do not ask the caller to restate source checks, source summary updates, stable entity writes, audits, or log updates; those are this skill's internal workflow. Treat extra caller text only as an optional focus, not as a required checklist.

## Core Boundary

This skill may read `raw/`, `wiki/sources/`, `wiki/syntheses/`, `wiki/entities/`, `skills/`, and `outputs/` when doing maintenance.

Runtime BP skills must remain narrower:

- `skills/run-brawl-stars-bp/` is a neutral judge and report coordinator.
- `skills/brawl-stars-bp-slot-decision/` compiles or decides from stable entity facts, strength input, and `runtime_bp_index`.
- Runtime decision work must not read maintenance discussion pages to patch a pick.

## Domain Scripts

The current domain scripts live under this skill's `scripts/` directory:

- `scripts/capture_brawler_sources.py`
- `scripts/ingest_brawler_sources.py`
- `scripts/ingest_brawler_bp_profiles.py`
- `scripts/audit_bp_profile_quality.py`
- `scripts/audit_plp_matchup_coverage.py`
- `scripts/test_bp_skill_contract.py`

Use `--dry-run` when a script offers it before large writes. Treat script output as a maintenance aid, not proof that a brawler or map is strategically correct.

`scripts/capture_brawler_sources.py` is the repeatable hero source capture script. Its `--sites` parameter accepts `fandom`, `plp`, or both; map Fandom raw capture is handled through the map ingest flow in `references/source-ingest.md`.

`scripts/audit_plp_matchup_coverage.py` compares PLP raw `countersThese` / `counteredBy` pairs with a compiled `runtime_bp_index.matchup_index`. It writes generated reports to `outputs/` and treats PLP-only pairs as review seeds, not runtime matchup edges. Promote a seed only by adding mechanism, `active_when`, `fails_when`, and `bp_use` to the relevant brawler entity page.

For current-coverage audits, it reads the latest direct raw per Brawler. Older dated captures remain immutable history but must not be unioned into the current PLP matchup set.

## Completion Checklist

- Stable facts live in `wiki/entities/brawlers/` or `wiki/entities/maps/`, not in temporary syntheses pages.
- Non-BP concept pages and broad synthesis pages are handled by the general wiki workflow, not as this skill's primary outputs.
- Source summaries explain what each source can and cannot prove.
- Version strength and short-lived meta stay in source/audit/log layers unless they change a stable capability, map hook, matchup condition, or slot rule.
- Audits and generated runtime indexes go to `outputs/` or caller-provided paths.
- `scripts/test_bp_skill_contract.py` passes after changing BP skills, references, or maintenance boundaries.
