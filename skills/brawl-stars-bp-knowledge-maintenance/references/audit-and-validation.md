# Audit and Validation

Use this reference before finishing BP maintenance, changing BP skill boundaries, or upgrading profile statuses.

## Script Ownership

The BP maintenance skill owns the workflow for these repo scripts:

- `scripts/capture_brawler_sources.py`
- `scripts/ingest_brawler_sources.py`
- `scripts/ingest_brawler_bp_profiles.py`
- `scripts/audit_bp_profile_quality.py`
- `scripts/audit_plp_matchup_coverage.py`
- `scripts/test_bp_skill_contract.py`

They live inside `skills/brawl-stars-bp-knowledge-maintenance/scripts/`. Do not recreate a repository-level helper directory for these BP maintenance scripts.

## Script Path and Artifact Check

All bundled scripts should resolve the repository root from their own location with `Path(__file__).resolve().parents[3]`, because they live at `skills/brawl-stars-bp-knowledge-maintenance/scripts/*.py`.

Expected write targets:

| Script | Writes | Artifact class |
| --- | --- | --- |
| `scripts/capture_brawler_sources.py` | `raw/sources/fandom/heroes/`, `raw/sources/pl-prodigy/brawlers/` | canonical raw capture |
| `scripts/ingest_brawler_sources.py` | `wiki/sources/Fandom-*`, `wiki/sources/PLP-*` | canonical source summary |
| `scripts/ingest_brawler_bp_profiles.py` | `wiki/entities/brawlers/` | canonical brawler entity draft/profile |
| `scripts/audit_bp_profile_quality.py --write` | `outputs/bp-profile-quality-audit.md` | generated audit report |
| `scripts/audit_plp_matchup_coverage.py --write` | `outputs/plp-matchup-coverage-audit.md` | generated audit report |
| `scripts/test_bp_skill_contract.py` | stdout only | validation output |

Canonical knowledge writes belong in `raw/` or `wiki/` as listed above. Generated audit reports and runtime indexes go to `outputs/`.

## Quality Audit

Run:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py
```

To write the current report:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write
```

The report belongs in `outputs/bp-profile-quality-audit.md`, not `wiki/syntheses/`.

## PLP Matchup Coverage Audit

Run this after changing PLP ingest, brawler matchup fields, or runtime matchup compilation:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_plp_matchup_coverage.py \
  --runtime-index outputs/runtime-bp-index/default-tierlist-all-maps-thin.json \
  --write
```

The report belongs in `outputs/plp-matchup-coverage-audit.md`. PLP-only rows are `conditional_matchup_seed` candidates. They must not be copied into runtime as hard matchup edges until a maintainer adds mechanism, `active_when`, `fails_when`, map/mode conditions, and `bp_use` to the relevant brawler entity page.

The audit selects the latest direct raw per Brawler by dated filename. Historical captures stay in `raw/` for provenance, but current coverage must not merge superseded matchup lists with the latest guide state. The summary reports both current `plp_raw_pages` and total historical `plp_raw_files`.

Audit blockers include:

- `auto_placeholder`
- `missing_mechanism`
- `missing_map_route_or_objective`
- `missing_failure_modes`
- `missing_slot_specificity`
- `unreviewed_matchup_candidate`
- `unreviewed_build_delta`
- `source_traceability_gap`

The audit checks structure and obvious placeholders. It does not prove strategic correctness.

## Contract Test

Run:

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/test_bp_skill_contract.py
```

This protects:

- judge skill neutrality and report format
- slot-decision compile/decide separation
- maintenance skill `$markdown-llm-wiki` intake and reference routing, using `https://github.com/josephmax/skills/tree/main/skills/markdown-llm-wiki`
- the ban on runtime dependence on maintainer syntheses

If changing skill references, update the contract test first, watch it fail, then update the skill.

## Done Criteria

- `scripts/test_bp_skill_contract.py` passes.
- Relevant audits are clean or blockers are explicitly logged.
- Index/log changes are made only when durable navigation or maintenance state changed.
- Generated outputs remain in `outputs/`.
