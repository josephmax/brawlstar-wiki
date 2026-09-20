"""No file/tool interface is exposed to the model. Run under the host file sandbox."""
import argparse, concurrent.futures, json, os, time, urllib.request
from pathlib import Path

def run_one(root,config,system,identifier):
    destination=root/'results'/(identifier+'.json')
    if destination.exists():return {'id':identifier,'status':'reused'}
    body={'model':config['model'],'messages':[{'role':'system','content':system},{'role':'user','content':(root/(identifier+'.json')).read_text()}],
          'stream':False,'max_tokens':12000,'thinking':{'type':'enabled'},'reasoning_effort':'high'}
    started=time.time()
    request=urllib.request.Request(config['baseURL'].rstrip('/')+'/chat/completions',data=json.dumps(body).encode(),headers={'Content-Type':'application/json','Authorization':'Bearer '+os.environ['BP_EVAL_API_KEY']})
    try:
        with urllib.request.urlopen(request,timeout=240) as response: result=json.load(response)
        choice=result['choices'][0]
        record={'id':identifier,'status':'completed','model':config['model'],'reasoning_effort':'high','finish_reason':choice['finish_reason'],'usage':result.get('usage'),
                'content':choice['message'].get('content'),'elapsed_seconds':round(time.time()-started,2)}
        # Deliberately discard private chain-of-thought; retain the verifiable answer and usage.
    except Exception as error:
        record={'id':identifier,'status':'failed','error':type(error).__name__+': '+str(error)[:300],'elapsed_seconds':round(time.time()-started,2)}
    destination.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    return {k:record[k] for k in ('id','status','elapsed_seconds')}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--dir',type=Path,required=True);parser.add_argument('--limit',type=int);parser.add_argument('--workers',type=int,default=3);args=parser.parse_args()
    root=args.dir;config=json.loads((root/'provider.json').read_text());system=(root/'system.txt').read_text();ids=json.loads((root/'manifest.json').read_text())['ids']
    if args.limit:ids=ids[:args.limit]
    (root/'results').mkdir(exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures=[pool.submit(run_one,root,config,system,i) for i in ids]
        for future in concurrent.futures.as_completed(futures):print(json.dumps(future.result()),flush=True)
