# Repository Layering

Use this reference before any BP knowledge maintenance task. It defines how the vault-level `$markdown-llm-wiki` rules constrain the BP maintainer workflow.

Companion wiki skill: `https://github.com/josephmax/skills/tree/main/skills/markdown-llm-wiki`.

## Two Gates

Every input must pass two gates:

1. `LLM-wiki intake gate` from `$markdown-llm-wiki` (`https://github.com/josephmax/skills/tree/main/skills/markdown-llm-wiki`): preserve source material, create source summaries, keep provenance, update navigation/logs when needed.
2. BP domain gate: convert only stable, BP-consumable facts into brawler or map structures.

Do not skip the first gate because a BP conclusion seems obvious.

## Layer Ownership

| Layer | Path | Role | BP maintainer access |
| --- | --- | --- | --- |
| Raw source | `raw/` | Immutable captures, screenshots, source exports, user notes | Read for ingest; write only for explicit capture/cleanup |
| Source summary | `wiki/sources/` | Single-source summaries, boundaries, provenance | Create/update before stable facts |
| Stable BP facts | `wiki/entities/brawlers/`, `wiki/entities/maps/` | Runtime-consumable brawler and map facts | Primary output layer |
| Event facts | `wiki/entities/events/` | Tournament identity, results, played sets, and map/mode occurrence | Maintenance evidence only; not a runtime input |
| Maintainer synthesis | `wiki/syntheses/` | Methodology, architecture, audit interpretation | Read for maintenance; not runtime input |
| Skill rules | `skills/*/SKILL.md`, `skills/*/references/` | Executable agent instructions | Update when rules become operational |
| Outputs | `outputs/` | Audits, generated runtime indexes, temporary reports | Write generated artifacts here |

## Promotion Rule

A claim may move upward only when its consumer is clear:

- Source observation -> `wiki/sources/`.
- Trackable event result -> `wiki/entities/events/` after its source summary exists.
- Stable brawler ability -> `wiki/entities/brawlers/`.
- Stable map structure or BP factor -> `wiki/entities/maps/`.
- Process or schema rule -> this skill's references, then contract tests if runtime-critical.
- Session-specific index -> `runtime_bp_index` in `outputs/`, not a hand-written wiki page.

Non-BP concepts, resource systems, and broad synthesis pages belong to the general wiki workflow, not this BP maintenance skill's primary output path.

## Forbidden Collapses

- Do not use `wiki/sources/` as a replacement for `raw/`.
- Do not write current meta strength into stable brawler or map pages unless it changes capability semantics.
- Do not let runtime BP decisions read `wiki/syntheses/` to repair missing index facts.
- Do not treat `summary_tags`, `open`, `closed`, `grass`, `water`, or `high/medium/low` as direct BP signals.
