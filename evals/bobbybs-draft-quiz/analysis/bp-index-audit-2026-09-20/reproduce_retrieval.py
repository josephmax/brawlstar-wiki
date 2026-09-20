#!/usr/bin/env python3
"""Replay two neutral query policies. Reference names only score output, never guide queries."""
import argparse,contextlib,hashlib,io,json,sys
from pathlib import Path
from types import SimpleNamespace
A=Path(__file__).resolve().parent;R=A.parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--index',required=True,type=Path);ap.add_argument('--output',required=True,type=Path);args=ap.parse_args()
 meta=json.loads((A/'provenance.json').read_text());digest=hashlib.sha256(args.index.read_bytes()).hexdigest()
 if digest!=meta['primary']['sha256']:raise SystemExit('Index hash differs: this replay requires the original audited index.')
 sys.path.insert(0,str(R/'skills/brawl-stars-bp-slot-decision/scripts'));import query_runtime_facts as q
 idx=json.loads(args.index.read_text())['runtime_bp_index'];q.load_runtime_index=lambda _:idx
 es=[json.loads(l) for l in (A/'index-evidence.jsonl').read_text().splitlines()];reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines()];out=[]
 for e,r in zip(es,reviews):
  inp=e['input'];slot=inp['pick_slot'];bucket='ban_pressure' if r['task']=='ban' else 'early_pick' if slot==1 else 'late_pick' if slot==6 else 'response_pick'
  row={'ordinal':e['ordinal'],'id':e['id'],'bucket':bucket,'limit':0,'runs':{}}
  params=dict(entity_type='brawler',index=str(args.index),candidate_mask_file=None,map=inp['map'],mode=inp['mode'],include_id=[],exclude_id=inp['allies']+inp['enemies']+inp['bans'],capability=[],archetype=[],require_floor=[],bucket=[bucket],field=[],effort='low',limit=0,cache_dir='')
  for label,targets in [('bucket_only',[]),('bucket_plus_enemy_relations',inp['enemies'])]:
   with contextlib.redirect_stderr(io.StringIO()):fs=q.query_runtime_facts(SimpleNamespace(**params,relation_target=targets))['runtime_fact_query']['fact_window']
   names={f['id'] for f in fs};row['runs'][label]={'returned_count':len(names),'returned_ids':sorted(names),'reference_components_present':[n for n in e['candidates'] if n in names],'reference_components_missing':[n for n in e['candidates'] if n not in names],'reference_relations':{f['id']:f['conditional_relations'] for f in fs if f['id'] in e['candidates']}}
  out.append(row)
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 expected=json.loads((A/'retrieval-results.json').read_text());assert out==expected,'Query behavior differs from audited result'
 print(json.dumps({'ok':True,'query_calls':112,'matches_audited_result':True}))
if __name__=='__main__':main()
