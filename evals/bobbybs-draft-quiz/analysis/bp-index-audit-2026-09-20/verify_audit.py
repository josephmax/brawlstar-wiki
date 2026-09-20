#!/usr/bin/env python3
"""Check audit coverage, references, counts and integrity; not gameplay truth."""
import argparse, collections, hashlib, json
from pathlib import Path
A=Path(__file__).resolve().parent; R=A.parents[3]
def readl(name):return [json.loads(l) for l in (A/name).read_text().splitlines()]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check-live',action='store_true');args=ap.parse_args()
 es=readl('index-evidence.jsonl');rs=readl('reviews.jsonl');ss=readl('source-only-comparison.jsonl');summary=json.loads((A/'summary.json').read_text());meta=json.loads((A/'provenance.json').read_text())
 assert [x['ordinal'] for x in es]==list(range(1,57))
 assert len(rs)==len(ss)==56
 assert len({x['id'] for x in es})==56
 for e,r,s in zip(es,rs,ss):
  assert e['ordinal']==r['ordinal']==s['ordinal'] and e['id']==r['id']==s['id']
  ref=e['reference_for_audit_only'];expected=set(ref['accepted'])|{n for pair in ref.get('accepted_pairs',[]) for n in pair}|{v['brawler'] for v in ref.get('conditional',[])}
  assert expected==set(e['candidates'])==set(r['candidates'])
  for n,d in r['candidates'].items():
   assert d['logic_status'] in {'S','P','T'} and d['reasoning'] and d['conditions_and_counterevidence']
   assert d['evidence']['bundle_line']==e['ordinal'] and d['evidence']['candidate_key']==n
   card=e['candidates'][n]['card']
   for i in d['evidence']['mode_contract_indices']:assert card['objective_contracts'][i]['mode']==e['input']['mode']
   assert d['projection_weak']==(e['candidates'][n]['projection']['fit']=='weak')
   for edge in e['candidates'][n]['relations_with_actual_enemies']:
    assert n in [edge['favored'],edge['disfavored']]
    other=edge['disfavored'] if edge['favored']==n else edge['favored'];assert other in e['input']['enemies']
  expected_status='T' if any(x['status']=='T' for x in r['answer_plans']) else 'P' if any(x['status']=='P' for x in r['answer_plans']) else 'S'
  assert r['case_status']==expected_status
 assert {frozenset(x['brawlers']) for x in rs[1]['answer_plans']}=={frozenset(['Sprout','R-T']),frozenset(['Sprout','Pearl'])}
 assert [x for x in rs[40]['answer_plans'] if x['conditional']][0]['brawlers']==['Bull']
 assert dict(collections.Counter(r['case_status'] for r in rs))==summary['case_status_counts']
 assert dict(collections.Counter(d['logic_status'] for r in rs for d in r['candidates'].values()))==summary['component_status_counts']
 assert dict(collections.Counter(d['status'] for r in rs for d in r['answer_plans']))==summary['answer_plan_status_counts']
 assert sum(len(r['candidates']) for r in rs)==summary['candidate_component_count']==115
 assert sum(len(r['answer_plans']) for r in rs)==summary['answer_plan_count']==114
 for key in ['bucket_only','bucket_plus_enemy_relations']:
  missing=[{'ordinal':r['ordinal'],'candidate':n} for r in rs for n in r['retrieval']['runs'][key]['reference_components_missing']]
  assert missing==summary[key]['missing']
  assert len(missing)==summary[key]['missing_components']
  assert len(set(x['ordinal'] for x in missing))==summary[key]['affected_cases']
 hashes=A/'artifact-hashes.json'
 if hashes.exists():
  for name,digest in json.loads(hashes.read_text()).items():assert h(A/name)==digest,('artifact_drift',name)
 if args.check_live:
  assert h(R/'evals/bobbybs-draft-quiz/cases.calibrated.jsonl')==meta['case_sha256']
  scripts=R/'skills/brawl-stars-bp-slot-decision/scripts'
  for filename,key in [('compile_runtime_index.py','compiler_sha256'),('query_runtime_facts.py','query_script_sha256'),('runtime_index_tools.py','runtime_tools_sha256')]:assert h(scripts/filename)==meta[key],filename
  for mapping in [meta['live_source_hashes'],meta['live_map_hashes']]:
   for name,digest in mapping.items():assert h(R/name)==digest,('source_drift',name)
  for path,key in [('primary_path_at_audit','primary'),('jev_path_at_audit','jev_snapshot')]:
   assert h(R/meta[path])==meta[key]['sha256'],('index_drift',path)
 print(json.dumps({'ok':True,'cases':56,'candidate_components':115,'answer_plans':114,'case_status_counts':summary['case_status_counts'],'artifact_hashes_checked':hashes.exists(),'live_sources_checked':args.check_live,'semantic_correctness_proven':False},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
