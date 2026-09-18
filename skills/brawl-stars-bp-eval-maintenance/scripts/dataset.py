#!/usr/bin/env python3
"""Portable BP evaluation exports and integrity checks (stdlib only)."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

FIELDS = ('map', 'mode', 'pick_slot', 'allies', 'enemies', 'bans', 'ban_status')
PAIR_FIELDS = ('map', 'mode', 'allies', 'enemies', 'bans', 'ban_status', 'decision_scope', 'pick_slots')

def require(condition, message):
    if not condition:
        raise ValueError(message)

def jsonl(path):
    return [json.loads(s) for s in path.read_text().splitlines() if s.strip()]

def resolve(base, name, repo):
    require(not Path(name).is_absolute(), f'absolute path: {name}')
    p = (base / name).resolve()
    require(p.is_relative_to(repo), f'path escapes repository: {name}')
    require(p.is_file(), f'missing file: {name}')
    return p

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def record(c, paired=False):
    s = c['input']
    names = lambda x: '、'.join(x) if x else '尚未选择／未提供'
    clean = {k: s[k] for k in (PAIR_FIELDS if paired else FIELDS)}
    if paired:
        prompt = (f"荒野乱斗 BP：{s['mode']}，地图 {s['map']}。己方已选：{names(s['allies'])}；"
                  f"敌方已选：{names(s['enemies'])}。现在是己方第4、5手连选，对方还留第6手。"
                  f"已知禁用：{names(s['bans'])}；其余禁用未知。请给出一个两人组合（两手顺序不作要求），"
                  '说明职责分工、地图与技能资源条件，以及对方可能的第6手回应。')
    elif c['task'] == 'ban':
        require(s['pick_slot'] in (1, 6), 'ban side must be first/last')
        side = '首选方' if s['pick_slot'] == 1 else '末选方'
        prompt = (f"荒野乱斗禁用决策：{s['mode']}，地图 {s['map']}，{side}。"
                  f"已知禁用：{names(s['bans'])}；其余禁用未知。"
                  '提出一个首要禁用，最多两个备选，解释它们与本方开局和对方回应的关系。')
    else:
        prompt = (f"荒野乱斗 BP：{s['mode']}，地图 {s['map']}，当前位次 {s['pick_slot']}。"
                  f"己方已选：{names(s['allies'])}；敌方已选：{names(s['enemies'])}。"
                  f"已知禁用：{names(s['bans'])}；其余禁用未知。请选择首选、最多两个备选，"
                  '说明地图目标、阵容分工、关键资源条件和剩余回应。')
    return {'id': c['id'], 'input': clean, 'prompt': prompt}

def exports(cases):
    regular, paired = [], []
    for c in cases:
        if c['scoring'].get('provisional_enabled'):
            require(not c['calibration']['remaining_issues'], f"unresolved regular case: {c['id']}")
            require(c['input'].get('decision_scope') != 'paired_4_5', 'pair in single-pick set')
            regular.append(record(c))
        if c['scoring'].get('paired_exploratory_enabled'):
            require(c['input'].get('decision_scope') == 'paired_4_5', 'invalid pair scope')
            paired.append(record(c, True))
    return regular, paired

def validate(dataset, repo, strict=False):
    repo, dataset = Path(repo).resolve(), Path(dataset).resolve()
    require(dataset.is_relative_to(repo), "dataset outside repository")
    cases = jsonl(dataset / 'cases.calibrated.jsonl')
    m = json.loads((dataset / 'manifest.json').read_text())
    e = json.loads((dataset / 'analysis/evidence-manifest.json').read_text())
    ids = [c['id'] for c in cases]
    require(len(ids) == len(set(ids)), 'duplicate case ID')
    require(len({(c['video_id'], c['question_index']) for c in cases}) == len(cases), 'duplicate video question')
    require(len({c['ordinal'] for c in cases}) == len(cases), 'duplicate display ordinal')
    require(len(cases) == m['case_count'] == e['case_count'], 'case count mismatch')
    require(len({c['video_id'] for c in cases}) == m['video_count'] == e['episode_count'], 'video count mismatch')
    require(set(ids) == {i for v in m['videos'] for i in v['case_ids']}, 'video manifest ID coverage')
    drift = []
    for key, value in e['knowledge_files'].items():
        p = resolve(repo, value['path'], repo)
        if digest(p) != value['sha256']:
            drift.append(key)
    for table in ('source_sha256', 'visual_evidence_sha256'):
        for name, expected in e.get(table, {}).items():
            require(digest(resolve(dataset, name, repo)) == expected, f'immutable evidence changed: {name}')
    for c in cases:
        s, a = c['input'], c['analysis']
        require(c['task'] in ('pick', 'ban'), f"unknown task: {c['id']}")
        resolve(repo, 'wiki/entities/maps/' + s['map'] + '.md', repo)
        resolve(dataset, c['source']['transcript'], repo)
        selected = s['allies'] + s['enemies']
        require(len(selected) == len(set(selected)), f"duplicate selected hero: {c['id']}")
        require(not set(selected) & set(s['bans']), f"selected ban: {c['id']}")
        answers = c['reference']['accepted'] + [v['brawler'] for v in c['reference']['conditional']]
        if c['task'] == 'pick':
            require(not set(answers) & set(selected + s['bans']), f"illegal reference: {c['id']}")
        else:
            require(not set(answers) & set(s['bans']), f"already banned reference: {c['id']}")
        for hero in selected + s['bans'] + answers:
            resolve(repo, 'wiki/entities/brawlers/' + hero + '.md', repo)
        for pair in c['reference'].get('accepted_pairs', []):
            require(len(pair) == len(set(pair)) == 2, f"invalid pair: {c['id']}")
            require(not set(pair) & set(selected + s['bans']), f"illegal pair: {c['id']}")
            for hero in pair:
                resolve(repo, 'wiki/entities/brawlers/' + hero + '.md', repo)
        require(all(a.get(k) for k in ('title', 'reasoning', 'rubric', 'failure_example', 'counterfactual', 'evidence')), f"missing analysis: {c['id']}")
        for r in a['evidence']:
            p = resolve(repo, r['path'], repo)
            require(r['sha256'] == e['knowledge_files'][r['relative_path']]['sha256'], 'citation snapshot mismatch')
            if r['relative_path'] not in drift:
                require(r['section'] in p.read_text().splitlines()[r['line'] - 1], f"bad citation: {c['id']}")
        if c['scoring'].get('gold_enabled'):
            require(c['calibration'].get('full_case_audiovisual_verified') and not c['calibration']['remaining_issues'], 'gold without full source review')
    regular, paired = exports(cases)
    require(jsonl(dataset / 'inputs.calibrated-dev.jsonl') == regular, 'regular input drift/leakage; export-inputs required')
    require(jsonl(dataset / 'inputs.paired-review.jsonl') == paired, 'paired input drift/leakage; export-inputs required')
    rev = m['analysis_revision']
    require(len(regular) == rev['development_input_count'] == e['development_input_count'], 'development count mismatch')
    require(len(cases)-len(regular) == rev['withheld_count'] == e['withheld_from_dev_input'], 'withheld count mismatch')
    require(len(paired) == rev['paired_review_count'], 'paired count mismatch')
    require(sum(bool(c['scoring'].get('gold_enabled')) for c in cases) == rev['gold_count'] == e['gold_count'], 'gold count mismatch')
    links = 0
    for p in dataset.rglob('*.md'):
        if 'archive' in p.relative_to(dataset).parts:
            continue  # historical snapshots retain original layout semantics
        for target in re.findall(r'\]\((<[^>]+>|[^)]+)\)', p.read_text()):
            target = target.strip('<>')
            if target.startswith(('https://', 'http://', 'mailto:')):
                continue
            target = unquote(target.split('#')[0])
            if target:
                resolve(p.parent, re.sub(r':\d+$', '', target), repo)
                links += 1
    require(not strict or not drift, 'knowledge drift: '+', '.join(drift))
    return {'checks': 'passed', 'cases': len(cases), 'videos': m['video_count'],
            'development_inputs': len(regular), 'paired_review_inputs': len(paired),
            'withheld_from_regular': len(cases)-len(regular), 'gold': rev['gold_count'],
            'transcript_hashes': len(e['source_sha256']), 'screenshot_hashes': len(e.get('visual_evidence_sha256', {})),
            'knowledge_files': len(e['knowledge_files']), 'knowledge_drift': drift, 'local_links': links,
            'scope': 'integrity, export isolation and source hashes; not strategy or model performance'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['export-inputs', 'validate'])
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--dataset', type=Path, default=Path('evals/bobbybs-draft-quiz'))
    parser.add_argument('--strict-knowledge', action='store_true')
    args = parser.parse_args()
    repo = args.repo.resolve()
    dataset = (repo / args.dataset).resolve()
    require(dataset.is_relative_to(repo), 'dataset outside repository')
    if args.command == 'export-inputs':
        regular, paired = exports(jsonl(dataset / 'cases.calibrated.jsonl'))
        for name, items in [('inputs.calibrated-dev.jsonl', regular), ('inputs.paired-review.jsonl', paired)]:
            (dataset / name).write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in items))
        print(json.dumps({'development_inputs': len(regular), 'paired_review_inputs': len(paired)}))
    else:
        print(json.dumps(validate(dataset, repo, args.strict_knowledge), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
