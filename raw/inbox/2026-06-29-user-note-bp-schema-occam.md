# User note: BP schema should avoid noisy fields

- Date: 2026-06-29
- Source: user conversation in this Codex thread
- Scope: BP reasoning DSL / map profile schema governance

User position:

Schema-level information should be added conservatively. Any field can provide a more detailed reasoning dimension for an LLM, but it can also introduce noise and distract from higher-quality decisions.

By Occam's razor, information that does not clearly improve BP decision quality should not be included in the schema. `summary_tags` is suspect because the BP decision layer has already been decomposed into fine-grained map factors, capabilities, routes, objective payoffs, false positives, and slot tasks. A coarse tag layer cannot support reliable judgment and may interfere with reasoning.

Local modeling implication:

- A BP schema field must have a clear consumer.
- If a field is not consumed by hard gates, required capabilities, map BP factors, candidate evaluation, or output explanation, it should not enter Canonical Input.
- Coarse labels such as `high`, `medium`, `low`, or `summary_tags` should not be used as decision evidence.
