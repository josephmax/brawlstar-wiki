#!/usr/bin/env python3
"""Render breakpoint_audit.v1 as a self-contained readable infographic and exhaustive HTML."""
import argparse,base64,collections,html,json,re,subprocess,sys,tempfile
from pathlib import Path
from urllib.parse import quote

def esc(v): return html.escape(str(v),quote=True)
def slug(v):
 v=v.lower().replace('&','and').replace("'",''); return re.sub(r'[^a-z0-9]+','-',v).strip('-')
def main():
 p=argparse.ArgumentParser();p.add_argument('--audit',required=True,type=Path);p.add_argument('--portraits',required=True,type=Path);p.add_argument('--output-dir',required=True,type=Path);p.add_argument('--title',default='平衡断点快报');p.add_argument('--chrome');p.add_argument('--editorial',type=Path,help='reviewed patch-specific editorial JSON');p.add_argument('--manifest-source',type=Path,help='patch source with balance_patch_manifest');a=p.parse_args()
 x=json.loads(a.audit.read_text());
 if x.get('schema')!='balance_breakpoint_audit.v1': raise SystemExit('Expected balance_breakpoint_audit.v1')
 pairs=x['pair_deltas'];pressure=x['build_pressure_deltas']; editorial=json.loads(a.editorial.read_text()) if a.editorial else {}; patch_ids=x.get('selected_patch_ids') or [z['patch_id'] for z in x['patches']];
 if editorial and editorial.get('patch_id') not in patch_ids: raise SystemExit('Editorial patch does not match audit')
 manifest={}
 if a.manifest_source:
  blocks=re.findall(r'```json\s*\n(.*?)\n```',a.manifest_source.read_text(),re.S)
  for block in blocks:
   data=json.loads(block)
   if data.get('balance_patch_manifest',{}).get('patch_id') in patch_ids: manifest=data['balance_patch_manifest'];break
  if not manifest: raise SystemExit('No matching patch manifest')
 names={z['attacker'] for z in pairs}|{z['target'] for z in pairs}|{z['attacker'] for z in pressure}|{z['target'] for z in pressure}|{n for h in editorial.get('mechanic_highlights',[]) for n in h['brawlers']}; portraits={};missing=[]
 for n in sorted(names):
  file=a.portraits/(slug(n)+'.png')
  if not file.is_file(): missing.append(n);continue
  portraits[n]='data:image/png;base64,'+base64.b64encode(file.read_bytes()).decode()
 if missing: raise SystemExit('Missing portraits: '+', '.join(missing))
 def img(n,cls='face'):
  return f'<img class="{cls}" src="{portraits[n]}" title="{esc(n)}" alt="{esc(n)}">'
 body=[z for z in pairs if z['target_state']=='body' and z.get('comparison_kind')=='repeated_identical_packets']
 grouped=collections.defaultdict(list)
 for z in body:
  if 'damage_packet' in z.get('change_drivers',[]): grouped[(z['attacker'],z['packet_id'],z['packet_damage_before'],z['packet_damage_after'])].append(z)
 packet_names={'main.full_connect':'普攻全中','main.impact':'普攻直击','main.clyde_impact':'Clyde 普攻','main.max_range':'普攻 · 最远距离'}
 cards=[]
 for (who,pid,old,new),rows in sorted(grouped.items(),key=lambda z:(-len(z[1]),z[0][0])):
  groups=collections.defaultdict(list)
  for row in rows:groups[(row['hits_to_kill_before'],row['hits_to_kill_after'])].append(row)
  lines=[]
  compact=next((v for v in editorial.get('compact_packets',[]) if v['brawler']==who and v['packet_id']==pid),None)
  if compact:
   lines.append('<div class="compact">'+esc(compact['reason'])+' · '+str(len(rows))+' 条，见 HTML 明细</div>')
  for (before,after),entries in ([] if compact else sorted(groups.items())):
   icons=''.join('<span class="target">'+img(e['target'])+('<b title="等值边界需核验">·</b>' if e.get('rounding_review_required') else '')+('<i title="攻击与目标同时变化">+</i>' if len(e.get('change_drivers',[]))>1 else '')+'</span>' for e in entries)
   cls='up' if after<before else 'down'
   lines.append(f'<div class="group"><div class="change {cls}">{before}<small>→</small>{after}<em>发</em></div><div class="faces">{icons}</div><span class="count">{len(entries)}</span></div>')
  label='普攻 · 5 弹全中' if who=='Shelly' and pid=='main.full_connect' else packet_names.get(pid,pid); cards.append(f'<article class="card"><header>{img(who,"hero")}<div><strong>{esc(who)}</strong><p>{esc(label)} · {esc(old)} → {esc(new)}</p></div><span class="badge">{len(rows)} 条</span></header>{"".join(lines)}</article>')
 target_changes=[z for z in pairs if any(v in z.get('change_drivers',[]) for v in ('target_health','damage_reduction')) and z.get('comparison_kind')=='repeated_identical_packets']
 defense_cards=[]
 for target in sorted({z['target'] for z in target_changes}):
  rows=[z for z in target_changes if z['target']==target and z['target_state']=='body']
  special=[z for z in target_changes if z['target']==target and z['target_state'] not in ('body','body+shield_gear_full')]
  if not rows and not special: continue
  changes=[v for v in manifest.get('changes',[]) if v.get('brawler')==target and v.get('type') in ('target_state','defense_modifier')]
  labels=[]
  for v in changes:
   if v['type']=='target_state': labels.append('生命 '+format(v['old']*2/(1+0.1*(v.get('power_level',1)-1)),'g')+' → '+format(v['new']*2/(1+0.1*(v.get('power_level',1)-1)),'g'))
   else: labels.append('减伤 '+str(round(v['old']*100))+'% → '+str(round(v['new']*100))+'%（技能窗口）')
  grouping=collections.defaultdict(list)
  for z in rows: grouping[(z['hits_to_kill_before'],z['hits_to_kill_after'])].append(z)
  lines=[]
  for (before,after),entries in sorted(grouping.items()):
   faces=''.join('<span class="target">'+img(e['attacker'])+('<b title="等值边界需核验">·</b>' if e.get('rounding_review_required') else '')+('<i title="攻击与目标同时变化">+</i>' if len(e.get('change_drivers',[]))>1 else '')+'</span>' for e in entries)
   lines.append(f'<div class="group"><div class="change {"up" if after>before else "down"}">{before}<small>→</small>{after}<em>发</em></div><div class="faces">{faces}</div><span class="count">{len(entries)}</span></div>')
  conditional=[z for z in special if 'shield_gear_full' not in z['target_state']]
  if conditional:
   lines.append('<div class="compact">技能减伤窗口 · 头像为攻击者</div>')
   cg=collections.defaultdict(list)
   for z in conditional: cg[(z['target_state'],z['hits_to_kill_before'],z['hits_to_kill_after'])].append(z)
   for (state,before,after),entries in sorted(cg.items()):
    faces=''.join('<span class="target">'+img(e['attacker'])+('<b title="等值边界需核验">·</b>' if e.get('rounding_review_required') else '')+('<i title="攻击与目标同时变化">+</i>' if len(e.get('change_drivers',[]))>1 else '')+'</span>' for e in entries)
    lines.append(f'<div class="group"><div class="change {"up" if after>before else "down"}">{before}<small>→</small>{after}<em>发</em></div><div class="faces">{faces}</div><span class="count">{len(entries)}</span></div>')
  if special: lines.append('<div class="compact">专属防御状态 '+str(len(special))+' 条，含满盾组合；完整条件见明细</div>')
  defense_cards.append(f'<article class="card"><header>{img(target,"hero")}<div><strong>{esc(target)}</strong><p>{esc(" · ".join(labels) or "生存状态变化")}</p></div><span class="badge">受击</span></header>{"".join(lines)}</article>')
 highlights=[]
 for h in editorial.get('mechanic_highlights',[]):
  highlights.append('<div class="highlight"><div class="highlight-faces">'+''.join(img(n,'hero') for n in h['brawlers'])+'</div><div><b>'+esc(h['title'])+'</b><p>'+esc(h['description'])+'</p></div></div>')
 def cells(row):
  a1=row.get('hits_to_kill_before');b1=row.get('hits_to_kill_after')
  if a1 is None: a1='击杀' if row.get('kills_in_one_packet_before') else '未击杀';b1='击杀' if row.get('kills_in_one_packet_after') else '未击杀'
  fields=[row['attacker'],row['packet_id'],row['target'],row['target_state'],f'{a1} → {b1}',row['packet_damage_before'],row['packet_damage_after'],row['effective_health_before'],row['effective_health_after'],', '.join(row.get('change_drivers',[])), '是' if row.get('rounding_review_required') else '否', '; '.join(row.get('requirements',[])+row.get('conditions',[]))]
  return '<tr>'+''.join('<td>'+esc(q)+'</td>' for q in fields)+'</tr>'
 detail=''.join(cells(z) for z in pairs)
 pressure_rows=''.join('<tr>'+''.join('<td>'+esc(v)+'</td>' for v in [z['attacker'],z['packet_id'],z['target'],z['target_state'],z['direction'],z['base_hits_to_kill_before'],z['base_hits_to_kill_after'],z['defense_state_hits_to_kill_before'],z['defense_state_hits_to_kill_after'],', '.join(z.get('requirements',[]))])+'</tr>' for z in pressure)
 if detail.count('<tr>')!=len(pairs) or pressure_rows.count('<tr>')!=len(pressure):raise SystemExit('Incomplete row rendering')
 c=x['coverage'];shield=sum(z['target_state']=='body+shield_gear_full' for z in pairs);other=len(pairs)-len(body)-shield; exact=sum(bool(z.get('rounding_review_required')) for z in pairs)
 patch=', '.join(x.get('selected_patch_ids') or [z['patch_id'] for z in x['patches']]); exclusions=[z for z in x.get('exclusions',[]) if z.get('patch_id') in (x.get('selected_patch_ids') or [])];
 css='''*{box-sizing:border-box}body{margin:0;background:#101428;color:#fff;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif}#poster{padding:56px 64px 46px;width:2400px;min-height:1600px;background:radial-gradient(ellipse at 20% 0,#304796 0,#202653 27%,#101428 80%)}.top{display:flex;justify-content:space-between;align-items:end;border-bottom:3px solid #4755a0;padding-bottom:25px}.eyebrow{letter-spacing:.2em;font-weight:800;color:#b2c4ff;font-size:19px}.title{font-size:68px;line-height:1.05;font-weight:950;letter-spacing:-.04em;margin:8px 0}.sub{font-size:22px;color:#b9c4eb}.stats{display:flex;gap:15px}.stat{background:#292f5d;border:1px solid #58639b;border-radius:16px;padding:12px 22px;min-width:165px}.stat b{font-size:35px;display:block}.stat span{color:#c4cbed;font-size:16px}.section{display:flex;align-items:center;gap:20px;margin:28px 0 18px}.section h2{font-size:28px;margin:0}.section p{color:#b8c5ec;font-size:17px;margin:0}.grid{column-count:3;column-gap:18px}.card{break-inside:avoid;background:#252c55;border:1px solid #4c5b9d;border-radius:16px;padding:16px;margin:0 0 17px;box-shadow:0 8px 20px #080b1b55}.card header{display:flex;gap:14px;align-items:center;padding-bottom:10px;border-bottom:1px solid #4d5785;margin-bottom:5px}.hero{width:58px;height:58px;object-fit:cover;border-radius:13px;background:#6c83d1}.card strong{font-size:24px}.card p{font-size:15px;color:#c4ceee;margin:3px 0}.badge{margin-left:auto;font-size:15px;color:#d6e2ff;background:#3a487e;padding:6px 10px;border-radius:8px}.group{display:flex;align-items:center;gap:10px;padding:7px 0;border-bottom:1px solid #ffffff10}.change{font-weight:900;font-size:23px;min-width:78px}.change small{color:#bdc7ee;padding:0 3px}.change em{font-size:13px;font-style:normal;margin-left:3px}.up{color:#5bf0a2}.down{color:#ff899a}.faces{display:flex;flex-wrap:wrap;gap:4px;flex:1}.target{position:relative;display:inline-flex}.face{width:31px;height:31px;border-radius:7px;background:#7286cf;object-fit:cover}.target b,.target i{position:absolute;bottom:-5px;font-size:16px;font-style:normal;color:#ffdf70;text-shadow:0 1px 2px #000}.target b{left:0}.target i{right:0}.count{font-size:14px;color:#afbadf}.foot{margin-top:24px;border-top:2px solid #4b5992;padding-top:16px;display:flex;justify-content:space-between;color:#d3dcfa;font-size:16px}.foot b{color:#fff}.compact{padding:9px 0;color:#c5ccef;font-size:15px}.highlight{display:flex;align-items:center;gap:22px;background:#304e67;border:1px solid #5fcba4;border-radius:16px;padding:16px 20px}.highlight-faces{display:flex;gap:8px}.highlight b{font-size:23px;color:#b0ffdc}.highlight p{margin:5px 0 0;color:#d5f1e7;font-size:17px}.defense-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;align-items:start}.detail{width:2400px;padding:40px 64px;background:#f6f7fc;color:#1a2445}details{margin:16px 0;background:white;padding:18px;border:1px solid #d9dfee;border-radius:10px}summary{font-size:24px;font-weight:700;cursor:pointer}table{border-collapse:collapse;font-size:14px;width:100%;margin-top:15px}td,th{border-bottom:1px solid #ddd;padding:7px;text-align:left;vertical-align:top}th{background:#edf0fb} .hint{font-size:16px}'''
 page=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>{esc(a.title)}</title><style>{css}</style><body><main id="poster"><div class="top"><div><div class="eyebrow">BRAWL STARS / BREAKPOINT AUDIT</div><h1 class="title">{esc(a.title)}</h1><div class="sub">{esc(patch)} · 等级 {x['power_level']} · 裸身攻击与受击断点 · 目标头像分组</div></div><div class="stats"><div class="stat"><b>{c['active_target_count']}</b><span>已索引英雄</span></div><div class="stat"><b>{len(pairs)}</b><span>全部状态变化</span></div><div class="stat"><b>{len(pressure)}</b><span>构筑压力变化</span></div></div></div>{('<div class="section"><h2>机制变化</h2><p>基于官方补丁人工归纳，独立于断点计算</p></div>'+''.join(highlights)) if highlights else '<div class="section"><p>机制亮点未提供人工审校配置，尚未整理</p></div>'}<div class="section"><h2>攻击变化 / 裸身</h2><p>绿：击倒更快　红：击倒更慢　头像上的 · 精确等值待核验　+ 攻防双方同时变化</p></div><div class="grid">{''.join(cards)}</div><div class="section"><h2>坦度变化 / 裸身受击</h2><p>头像为攻击方；绿：更耐打　红：更易被击倒 · 高发数、特殊状态完整保留在 HTML</p></div><div class="defense-grid">{''.join(defense_cards)}</div><div class="foot"><div><b>概览范围</b> 裸身重复变化 {len(body)} 条（含编辑压缩）；满盾 {shield} 条、其他状态及单包 {other} 条见 HTML 明细。</div><div>满盾 +900 · 当前材料含 {len(exclusions)} 项排除 · 精确等值 {exact} 条待核验</div></div></main><section class="detail"><h2>完整审计明细</h2><p class="hint">概览按攻击与受击分区，人工压缩项及其他状态均在下方；保留全部 {len(pairs)} 条逐状态变化和 {len(pressure)} 条构筑压力变化。数值仅描述已建模状态，不推导强度或无条件对位。</p><details><summary>逐状态变化 · {len(pairs)} 条</summary><table><thead><tr>{''.join('<th>'+h+'</th>' for h in ['攻击者','攻击包','目标','目标状态','前→后','伤害前','伤害后','有效血前','有效血后','驱动','等值复核','条件'])}</tr></thead><tbody>{detail}</tbody></table></details><details><summary>构筑压力变化 · {len(pressure)} 条</summary><table><thead><tr>{''.join('<th>'+h+'</th>' for h in ['攻击者','攻击包','目标','防御状态','变化类型','裸身前','裸身后','防御前','防御后','要求'])}</tr></thead><tbody>{pressure_rows}</tbody></table></details><details><summary>本期排除项 · {len(exclusions)} 条</summary><pre>{esc(json.dumps(exclusions,ensure_ascii=False,indent=2))}</pre></details><p>输入文件：{esc(a.audit.name)}；来源与完整条件以源审计 JSON 为准。HTML 使用本地头像的内嵌副本。</p></section><script>document.body.setAttribute("data-poster-height",document.getElementById("poster").offsetHeight)</script></body></html>'''
 a.output_dir.mkdir(parents=True,exist_ok=True); out=a.output_dir/'brief.html';out.write_text(page);print(json.dumps({'html':str(out.resolve()),'pair_rows':len(pairs),'pressure_rows':len(pressure),'body_overview':len(body),'other':other,'shield':shield,'excluded':len(exclusions)},ensure_ascii=False))
 if a.chrome:
  image=a.output_dir/'brief.png'
  with tempfile.TemporaryDirectory(prefix='brawl-brief-chrome-') as profile:
   common=[a.chrome,'--headless','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files','--user-data-dir='+profile]
   measure=subprocess.run(common+['--window-size=2400,1600','--dump-dom',out.resolve().as_uri()],capture_output=True,text=True,timeout=60)
   match=re.search(r'data-poster-height="(\d+)"',measure.stdout)
   if measure.returncode or not match: raise SystemExit('PNG export failed: could not measure poster: '+measure.stderr[-1000:])
   height=int(match.group(1))
   if height>12000: raise SystemExit('Poster too tall for safe PNG export; split or adjust layout')
   cmd=common+['--screenshot='+str(image.resolve()),f'--window-size=2400,{height}',out.resolve().as_uri()]
   r=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
   if r.returncode or not image.exists():raise SystemExit('PNG export failed: '+r.stderr[-2000:])
   print('PNG: '+str(image.resolve())+' height='+str(height))
if __name__=='__main__':main()
