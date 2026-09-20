import json,sys,contextlib,io,hashlib,collections
from pathlib import Path
from types import SimpleNamespace
import argparse
ap=argparse.ArgumentParser();ap.add_argument('--output-dir',required=True,type=Path);args=ap.parse_args()
R=Path(__file__).resolve().parents[4];sys.path.insert(0,str(R/'skills/brawl-stars-bp-slot-decision/scripts'))
import query_runtime_facts as q
P=R/'outputs/runtime-bp-index/default-runtime-index.json';assert hashlib.sha256(P.read_bytes()).hexdigest()=='bbe2026807bcaaa250179344c01cae88300316426b87489227669e3b0c14dd1f','index drift';idx=json.loads(P.read_text())['runtime_bp_index'];q.load_runtime_index=lambda _:idx
E=R/'evals/bobbybs-draft-quiz/analysis/bp-index-audit-2026-09-20/index-evidence.jsonl';es=[json.loads(l) for l in E.read_text().splitlines()]
# Predetermined, same capability axes for every case; no answer names in query inputs.
axes=['effective_range','burst','objective_damage','mobility','survivability','anti_aggro','anti_tank','throw_or_wall_bypass','area_control','team_support','crowd_control','scouting_or_vision']
records=[]
for e in es:
 inp=e['input'];ref=e['reference_for_audit_only'];task='ban' if e['ordinal'] in [21,22,23] else 'pick';slot=inp['pick_slot'];bucket='ban_pressure' if task=='ban' else 'early_pick' if slot==1 else 'late_pick' if slot==6 else 'response_pick';effort='high' if slot>=4 and task=='pick' else 'low'
 base=dict(index=str(P),entity_type='brawler',candidate_mask_file=None,map=inp['map'],mode=inp['mode'],include_id=[],exclude_id=inp['allies']+inp['enemies']+inp['bans'],relation_target=inp['enemies'],bucket=[bucket],capability=[],archetype=[],require_floor=[],field=[],effort=effort,limit=None,cache_dir='')
 row={'ordinal':e['ordinal'],'id':e['id'],'task':task,'input':inp,'bucket':bucket,'effort':effort,'runs':{},'candidates':{}}
 specs=[('bucket_enemy_budget',{}),('bucket_enemy_unlimited',{'limit':0})]+[(axis+'_high',{'require_floor':[axis+'@high']}) for axis in axes]
 for label,override in specs:
  kwargs={**base,**override}
  with contextlib.redirect_stderr(io.StringIO()):body=q.query_runtime_facts(SimpleNamespace(**kwargs))['runtime_fact_query']
  ids=[v['id'] for v in body['fact_window']]
  row['runs'][label]={'query':{k:kwargs[k] for k in ['bucket','capability','archetype','require_floor','relation_target','exclude_id','include_id','effort','limit']},'returned_count':len(ids),'returned_ids':ids}
 for n,v in e['candidates'].items():
  card=v['card'];own=idx['matchup_index']['by_brawler'].get(n,{})
  owns=[(d,x['target']) for d,xs in own.items() for x in xs if x['target'] in inp['enemies']]
  all_edges=v['relations_with_actual_enemies'];reverse_only=[ed for ed in all_edges if ed['stored_on']!=n and (('answers' if ed['favored']==n else 'is_answered_by',ed['stored_on']) not in owns)]
  row['candidates'][n]={'available':n not in base['exclude_id'],'projection_fit':v['projection']['fit'],'bucket_present':bucket in v['projection'].get('projection_buckets',[]),'query_membership':{label:n in rr['returned_ids'] for label,rr in row['runs'].items()},'query_positions_1based':{label:rr['returned_ids'].index(n)+1 if n in rr['returned_ids'] else None for label,rr in row['runs'].items()},'high_axes':[a for a in axes if n in row['runs'][a+'_high']['returned_ids']],'capability_levels':card['capability_levels'],'candidate_side_enemy_edges':owns,'enemy_side_edges_not_on_candidate':reverse_only,'failure_gate_activation':v['projection']['failure_gate_activation'],'mode_objective': [x for x in card['objective_contracts'] if inp['mode'] in x['mode']],'slot_note':card['slot_notes'].get('slot_'+str(slot),card['slot_notes'].get('slot_4_5') if slot in [4,5] else card['slot_notes'].get('slot_2_3'))}
 records.append(row)
out=args.output_dir;out.mkdir(parents=True,exist_ok=True);(out/'matrix.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
summary={'cases':56,'candidate_records':sum(len(r['candidates']) for r in records),'query_calls':len(records)*len(specs),'probe_axes':axes}
for key,f in [('all',lambda r:True),('slot6_pick',lambda r:r['task']=='pick' and r['input']['pick_slot']==6)]:
 cs=[(r['ordinal'],n,c) for r in records if f(r) for n,c in r['candidates'].items()]
 summary[key]={'cases':sum(f(r) for r in records),'records':len(cs),'missing_bucket':[(i,n) for i,n,c in cs if not c['bucket_present']],'missing_budget':[(i,n) for i,n,c in cs if not c['query_membership']['bucket_enemy_budget']],'missing_unlimited':[(i,n) for i,n,c in cs if not c['query_membership']['bucket_enemy_unlimited']],'no_high_window':[(i,n) for i,n,c in cs if not c['high_axes']],'reverse_only_relation_records':[(i,n) for i,n,c in cs if c['enemy_side_edges_not_on_candidate']]}
(out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps(summary,ensure_ascii=False))
