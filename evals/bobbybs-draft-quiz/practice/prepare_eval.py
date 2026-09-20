"""Stage only public MCQs, runtime rules and neutral retrieval into an isolated folder."""
import argparse, hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SCRIPTS=ROOT/'skills/brawl-stars-bp-slot-decision/scripts'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--index',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    skill=ROOT/'skills/brawl-stars-bp-slot-decision/SKILL.md'
    rules=ROOT/'skills/brawl-stars-bp-slot-decision/references/runtime-decision-knowledge.md'
    system=skill.read_text()+'\n'+rules.read_text()+'''
本次执行有限选项的 BP 机制回归。调用方已经按全部可见选项及双方英雄完成中性事实查询与 hydrate，不再扩展全英雄池。所有选项都必须得到比较，不能用地图软桶缺失直接排除；事实来自正常工具，不含答案。
根据完整队伍组合、顺位与实际机制评价每个选项，不预设任何选项数量分布。correct=在本局有可兑现、无明显更好替代的成立方案；reasonable=可兑现但有具体可改善的成本或职责缺口；poor=具体失败链使方案不合理。仅有操作门槛或可能反制不自动降档；多个选项可为 correct。不能从熟悉的视频/作者名单作答，不能编造当前版本统计。不足以判断时用 insufficient_evidence。
只返回 JSON：{"options":[{"id":"A","grade":"correct|reasonable|poor|insufficient_evidence","reason":"简短证据总结","evidence":["实际卡片字段或关系机制"],"conditions":"成立与失败条件"}],"best":["A"],"uncertainties":[] }。不输出隐含思维链，输出可核查结论。
'''
    (args.out/'system.txt').write_text(system)
    rows=[json.loads(s) for s in (HERE/'inputs.options-only.jsonl').read_text().splitlines()]
    traces=[]
    for row in rows:
        names=sorted(set(row['state']['allies']+row['state']['enemies']+[n for o in row['options'] for n in o['members']]))
        common=['--index',str(args.index),'--map',row['state']['map'],'--json']
        includes=[v for n in names for v in ('--include-id',n)]
        relations=[v for n in names for v in ('--relation-target',n)]
        neutral={}
        trace=[]
        for op,extra in [('query', ['--effort','high','--limit','100']),('hydrate',[])]:
            argv=[sys.executable,str(SCRIPTS/('query_runtime_facts.py' if op=='query' else 'hydrate_runtime_facts.py')),*common,*includes,*relations,*extra]
            run=subprocess.run(argv,capture_output=True,text=True,check=True)
            raw=json.loads(run.stdout);body=next(iter(raw.values()))
            trace.append({'operation':op,'argv':argv[2:],'sha256':hashlib.sha256(run.stdout.encode()).hexdigest(),'stderr':run.stderr.strip()})
            if op=='query':
                # Limit root window to named options/visible players; preserve neutral map packet.
                neutral['query']={k:v for k,v in body.items() if k in ('map_fact_packet','scope','manifest')}
            else:
                neutral['map']=body['map_fact_packet']
                neutral['entities']={}
                for name,entity in body['entities'].items():
                    card={k:v for k,v in entity['runtime_card'].items() if k!='environment_evidence'}
                    neutral['entities'][name]={'runtime_card':card,'conditional_relations':entity['conditional_relations'],'candidate_map_fit':entity['candidate_map_fit'],'evidence_ref':entity['evidence_ref']}
        (args.out/(row['id']+'.json')).write_text(json.dumps({'question':row,'neutral_facts':neutral},ensure_ascii=False))
        traces.append({'id':row['id'],'retrieval':trace})
    (args.out/'manifest.json').write_text(json.dumps({'ids':[r['id'] for r in rows],'index_sha256':sha(args.index),'skill_sha256':sha(skill),'rules_sha256':sha(rules),'inputs_sha256':sha(HERE/'inputs.options-only.jsonl'),'retrieval':traces},ensure_ascii=False,indent=2))
    print(json.dumps({'staged':len(rows),'out':str(args.out)}))
