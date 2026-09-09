# Caller-supplied candidate masks

Keep the complete runtime index. Account eligibility constrains candidate retrieval, not knowledge of opponents or relation targets. Query and hydration accept `--candidate-mask-file <path>`:

```json
{"schema":"candidate_mask.v1","mode":"allowlist","ids":["Brock","Colt"],"context_id":"caller-owned context ID","index_source_hash":"manifest.source_hash from the selected index"}
```

Use canonical names. Empty IDs mean zero candidates; omitting the flag keeps unrestricted behavior. Invalid schemas/modes, unknown names, missing files and mismatched index hashes fail closed. Explicit unrestricted mode requires empty IDs. These caller-created temporary files are not wiki dependencies.

Bucket, explicit include, relation recall and full capability/archetype/floor scans all enforce the mask before entity payload construction. Include may bypass soft windows but never the mask or excludes. Hydration retains relationships involving non-owned targets. Use separate unmasked calls for observed opponents, locked lineups and unknown teammates; do not present those outputs as the current player's candidates.

`query_matchup_census.py` accepts the same flag. Original `answered_by` / `answers` and their counts retain full ecology. Additional `selectable_answered_by` projects surviving predators to the supplied pool. A player's unowned heroes do not disappear from the opponent's ecology.

The application owns external API records, account identity, roster adaptation, level thresholds and eligibility policy. It computes the canonical allowlist before invoking these tools. Knowledge scripts consume that allowlist only; they do not accept developer API player rows or derive account eligibility. Applications can read the existing canonical entity/alias index to resolve names without maintaining a second alias table.

Cache identity includes actual index content, all window parameters and mask content. Replacing a mask at the same path, including changing to an empty list, cannot reuse another pool's result. Returned mask summaries expose status/count/context/digest without repeating the entire roster.
