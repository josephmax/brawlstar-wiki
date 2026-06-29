# User note: hero BP ingest plan

- Date: 2026-06-29
- Source: user conversation in this Codex thread
- Scope: Brawler source preservation and BP-ready hero modeling plan
- Important constraint: do not execute the ingest in this session; only prepare a precise handoff plan.

User requirements:

- Current brawler count should be treated as 105, not the existing local 72.
- The plan must be complete enough for another session to continue after quota reset.
- Original information must be preserved first.
- Fandom and Power League Prodigy brawler detail pages should each be captured into `raw/` where available, so the knowledge base has richer source material.
- After raw preservation, information should be decomposed and ingested according to clear standards.
- The ingest should explain how each piece of brawler information affects BP decisions.
- The abstraction should use the intermediate layer developed in prior discussion: capability vectors, map feature hooks, objective contracts, failure modes, build switches, conditional matchup seeds, slot usage, and candidate evaluation.
- Avoid adding noisy schema fields. Every field must have a clear downstream consumer in BP reasoning.

Non-goal for this session:

- Do not scrape websites.
- Do not batch-edit 105 brawler pages.
- Do not generate BP-ready profiles without raw evidence.
