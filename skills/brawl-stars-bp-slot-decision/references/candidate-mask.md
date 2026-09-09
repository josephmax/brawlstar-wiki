# Caller-supplied recall masks

A mask defines which canonical IDs are visible as root entities in one retrieval invocation. The caller determines the window and combines its own conditions before invoking the tool. Knowledge scripts apply the resulting mask without receiving or interpreting the reasons behind it. A hidden entity is outside this call's recall window; the mask makes no claim about that entity's properties or suitability.

Query and hydration accept `--candidate-mask-file <path>`:

```json
{"schema":"candidate_mask.v1","mode":"allowlist","ids":["Brock","Colt"],"context_id":"window-42","index_source_hash":"manifest.source_hash from the selected index"}
```

`ids` lists visible canonical root IDs. An empty allowlist yields no roots. Omitting the flag leaves recall unrestricted; explicit `unrestricted` mode requires empty IDs. Invalid schemas/modes, unknown IDs, missing files and mismatched index hashes fail. The optional `context_id` is an opaque caller correlation token and does not affect filtering. Temporary mask files are not wiki dependencies.

The mask is scoped to the current invocation, not stored on the index. Reusing an index with another mask, or without a mask, must not inherit the previous window. Keep the complete runtime index unchanged.

Bucket, explicit include, relation recall and capability/archetype/floor scans enforce the mask before root detail construction and result limits. Include may bypass soft windows but never the mask or excludes. Hydration also filters root entities and corresponding environment rows. Relationships attached to a returned root may refer to IDs outside the mask: those are evidence, not extra candidate roots. The caller chooses the window independently for each query/hydration.

`query_matchup_census.py` accepts the same flag. Original `answered_by` / `answers` and their counts keep their existing ban-filter semantics. Additional `masked_answered_by` intersects surviving `answered_by` targets with the visible IDs. Its `alive` rows, `alive_count` and `removed_by_mask` describe this intersection only; they add no decision verdict and do not change global counts.

Returned mask summaries contain `applied`, `mode`, `visible_id_count`, `context_id` and `hash`. `visible_id_count` counts distinct IDs in the supplied allowlist, not matched or returned roots; it is null when recall is unrestricted. The digest identifies the supplied file without repeating the ID list.

The `candidate_mask.v1` input shape is unchanged. Query/hydration cache namespace v3 separates the current output fields from older cached responses. Cache identity includes actual index content, all window parameters and mask content; replacing a mask at the same path cannot reuse another window's result.
