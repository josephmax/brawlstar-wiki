# Player candidate masks

Keep the complete runtime index. Account eligibility constrains candidate retrieval, not knowledge of opponents or relation targets. Query and hydration accept `--candidate-mask-file <path>`:

```json
{"schema":"candidate_mask.v1","mode":"allowlist","ids":["Brock","Colt"],"context_id":"caller-owned context ID","index_source_hash":"manifest.source_hash from the selected index"}
```

Use canonical names. Empty IDs mean zero candidates; omitting the flag keeps unrestricted behavior. Invalid schemas/modes, unknown names, missing files and mismatched index hashes fail closed. Explicit unrestricted mode requires empty IDs. These caller-created temporary files are not wiki dependencies.

Bucket, explicit include, relation recall and full capability/archetype/floor scans all enforce the mask before entity payload construction. Include may bypass soft windows but never the mask or excludes. Hydration retains relationships involving non-owned targets. Use separate unmasked calls for observed opponents, locked lineups and unknown teammates; do not present those outputs as the current player's candidates.

`query_matchup_census.py` accepts the same flag. Original `answered_by` / `answers` and their counts retain full ecology. Additional `selectable_answered_by` projects surviving predators to the supplied pool. A player's unowned heroes do not disappear from the opponent's ecology.

`resolve_player_pool.py --repo <root>` accepts minimal `brawlers: [{id,name,power}]` on stdin, reads the existing canonical entity/alias index and returns P11+ `eligible_ids`, resolved rows and explicit `below_min_power` / `unmapped` reasons. Numeric IDs remain external identity; unknown names are not guessed. It neither fetches player data nor writes knowledge.

Cache identity includes actual index content, all window parameters and mask content. Replacing a mask at the same path, including changing to an empty list, cannot reuse another pool's result. Returned mask summaries expose status/count/context/digest without repeating the entire roster.
