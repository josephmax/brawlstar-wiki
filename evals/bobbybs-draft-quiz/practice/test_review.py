"""Verify the exported draft contract, not the strategic truth of its grades."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
load=lambda name:[json.loads(s) for s in (ROOT/name).read_text().splitlines()]
questions=load('questions.draft.jsonl')
inputs=load('inputs.options-only.jsonl')
labels={r['id']:r for r in load('labels.draft.jsonl')}
assert len(questions)==56
assert len({q['id'] for q in questions})==56
assert all(not q['enabled'] and not q['gold_enabled'] for q in questions)
assert [q['ordinal'] for q in questions if q['status'].startswith('blocked')]==[41,44,47]
for item in inputs:
    assert set(item)=={'id','state','task','answer_format','options'}
    assert set(item['state'])=={'map','mode','pick_slot','allies','enemies','bans','ban_status'}
    assert 3<=len(item['options'])<=5
    assert all(set(o)=={'id','members'} for o in item['options'])
    expected=labels[item['id']]['options']
    assert {o['id'] for o in item['options']}==set(expected)
    assert {v['proposed_grade'] for v in expected.values()}=={'correct','reasonable','poor'}
    assert sum(v['proposed_grade']=='correct' for v in expected.values()) in (1,2,3)
    unavailable=set(item['state']['allies']+item['state']['enemies']+item['state']['bans'])
    assert all(not unavailable.intersection(o['members']) for o in item['options'])
    assert all(len(o['members'])==(2 if item['answer_format']=='unordered_pair' else 1) for o in item['options'])
assert set(labels)=={i['id'] for i in inputs}
for q in questions:
    if q['status'].startswith('blocked'):continue
    shown=set()
    for i in inputs:
        if labels[i['id']]['case_id']==q['id']:
            shown.update(tuple(sorted(o['members'])) for o in i['options'])
    assert shown=={tuple(sorted(o['members'])) for o in q['options']}
manifest=json.loads((ROOT/'validation.json').read_text())
for name,sha in manifest['artifacts'].items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==sha
print(f'PASS: {len(questions)} drafts; {len(inputs)} answer-isolated 3–5-option variants; 3 blocked cases; all proposed options covered. Strategy/model validation remains pending.')
