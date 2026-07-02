# User note: BP runtime index should be compiled per version context

- Date: 2026-07-02
- Source: user conversation in this Codex thread
- Scope: BP runtime architecture, strength profiles, index governance

User position:

The BP skill should not permanently maintain a separate hand-written decision index between the hero/map facts and the final BP decision. By Occam's razor, the durable wiki should keep the stable bottom-layer BP facts: hero capability vectors, builds, common conditional matchups, map hooks, objective contracts, failure modes, slot notes, map profiles, and map BP factors.

Strength understanding changes by user, community, player, season, and patch. Therefore it should be passed in as a runtime input or profile rather than being written into hero encyclopedias or stable map pages.

The BP skill should have two domains:

1. Understand version context: combine stable wiki facts with the current strength profile and compile a runtime BP decision index for the current map pool/session.
2. Decide: consume that compiled runtime index to draft bans and picks for each slot, with strategy bias affecting choices inside the compiled context.

Modeling implication:

- Long-lived hand-written indexes such as matchup and map-hook summaries are likely noise if they duplicate bottom-layer facts and drift into slot, strength, or candidate-priority judgment.
- A runtime index is still useful, but it should be reproducible compile output, not a manually maintained wiki fact source.
- Existing Markdown runtime indexes should be treated as legacy retrieval/debug views until the compile command exists, then deleted or regenerated outside durable wiki facts.
