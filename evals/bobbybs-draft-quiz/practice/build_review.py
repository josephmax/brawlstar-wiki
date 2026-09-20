"""Build a review draft and answer-isolated MCQ inputs; never promote to gold."""
import argparse
import hashlib
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DATA = HERE.parent
LABELS = {'correct': '对', 'reasonable': '合理，但是有改进空间', 'poor': '不太合理'}


def readl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def writej(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def writel(path, values):
    path.write_text(''.join(json.dumps(v, ensure_ascii=False) + '\n' for v in values))


def build(index_path):
    index = json.loads(index_path.read_text())['runtime_bp_index']
    cards = index['brawler_runtime_cards']
    cases = readl(DATA / 'cases.calibrated.jsonl')
    supplements = {r['ordinal']: r for r in readl(HERE / 'supplements.draft.jsonl')}
    audits = {r['ordinal']: r for r in readl(DATA / 'analysis/bp-index-audit-2026-09-20/reviews.jsonl')}
    old_evidence = readl(DATA / 'analysis/bp-index-audit-2026-09-20/index-evidence.jsonl')
    for row in old_evidence:
        for name, evidence in row['candidates'].items():
            without_environment = lambda c: {k: v for k, v in c.items() if k != 'environment_evidence'}
            if without_environment(evidence['card']) != without_environment(cards[name]):
                raise ValueError(f"Re-review changed original-answer card: {row['ordinal']} {name}")
    assert set(supplements) == {c['ordinal'] for c in cases}
    review, inputs, labels, evidence, failures = [], [], [], [], []
    markdown = ['# BobbyBS BP 练习题清洗稿（待确认）', '',
        '56 题均已补一项中间档和一项反面选项。所有新等级都是维护者提案，不是作者原话、当前版本 gold 或模型实测成绩。', '',
        '**请先确认逐题分档；没有把风险大自动当成错误，也没有把作者名单外的英雄一律当错。** 中间档和反面选项仍需反证审阅及隔离模型回归。', '',
        '第 4、48 题保留可解释的正确分支，争议分支单列；第 41 题 Bull 带熟练度前提，不默认替用户满足；第 44、47 题原答案闭环不足。这三题暂不进入正式抽题。', '',
        '选项池可多于 5 项，实际题卡固定选出 3–5 项，至少各一项三档选项；正确分支轮换展示。一次选一个方案，不要求找齐所有正确答案；第 2 题选一个双人组合。', '',
        '本稿暂以英雄／组合为选项标题，解释在答题后展示。新增等级与正确分支的比较不是全局最优证明。历史补丁未知，已知 ban 按题面，其余不假定已知。', '']
    for case in cases:
        n, state = case['ordinal'], case['input']
        audit, supplement = audits[n], supplements[n]
        original = case['reference']
        plans = original.get('accepted_pairs') or [[name] for name in original['accepted']]
        for conditional in original.get('conditional', []):
            name = conditional if isinstance(conditional, str) else conditional.get('brawler', conditional.get('name'))
            if name and [name] not in plans:
                plans.append([name])
        options, unresolved = [], []
        for members in plans:
            reviews = [audit['candidates'][name] for name in members]
            item = {'members': members, 'explanation': '；'.join(r['reasoning'] for r in reviews),
                    'conditions': '；'.join(r['conditions_and_counterevidence'] for r in reviews),
                    'provenance': 'historical_author_option_with_index_review',
                    'source_review_status': [r['logic_status'] for r in reviews]}
            special_conditions = [c['condition'] for c in original.get('conditional', []) if isinstance(c, dict) and c.get('brawler') in members]
            item['required_player_conditions'] = special_conditions
            if special_conditions:
                item['conditions'] += '；玩家前提：' + '；'.join(special_conditions)
            if all(r['logic_status'] == 'S' for r in reviews) and not special_conditions:
                options.append(dict(item, proposed_grade='correct'))
            else:
                unresolved.append(item)
        for grade in ('reasonable', 'poor'):
            names, reason = supplement[grade]
            options.append({'members': names if isinstance(names, list) else [names],
                            'proposed_grade': grade, 'explanation': reason,
                            'provenance': 'maintainer_proposal_not_author_testimony',
                            'semantic_validation': 'pending_user_review_and_isolated_model_eval'})
        unavailable = set(state['allies'] + state['enemies'] + state['bans'])
        keys = []
        for option in options:
            assert all(name in cards for name in option['members']), (n, option)
            assert not unavailable.intersection(option['members']), (n, 'illegal', option)
            assert len(set(option['members'])) == len(option['members'])
            assert len(option['members']) == (2 if state.get('decision_scope') == 'paired_4_5' else 1)
            key = tuple(sorted(option['members']))
            assert key not in keys, (n, 'duplicate', key)
            keys.append(key)
        ready = any(o['proposed_grade'] == 'correct' for o in options)
        if not ready:
            failures.append(n)
        row = {'id': case['id'], 'ordinal': n, 'task': case['task'],
               'state': {k: state[k] for k in ('map', 'mode', 'pick_slot', 'allies', 'enemies', 'bans', 'ban_status')},
               'answer_format': 'unordered_pair' if state.get('decision_scope') == 'paired_4_5' else 'single_choice',
               'status': 'pending_confirmation' if ready else 'blocked_correct_branch_evidence',
               'enabled': False, 'gold_enabled': False, 'options': options,
               'unresolved_author_options': unresolved, 'original_reference': original,
               'source_case_sha256': digest(DATA / 'cases.calibrated.jsonl')}
        review.append(row)
        # Inputs expose all shown names equally; labels/reasons/source IDs never enter the prompt.
        # Round-robin variants ensure every correct proposal appears despite a five-option display cap.
        good = [o for o in options if o['proposed_grade'] == 'correct']
        for offset in range(0, len(good), 3):
            selected = good[offset:offset+3] + [o for o in options if o['proposed_grade'] != 'correct']
            random.Random(f'bobby-mcq-v1:{n}:{offset}').shuffle(selected)
            inputs.append({'id': f'practice-{n:03d}-{offset//3+1}', 'state': row['state'],
                           'task': case['task'], 'answer_format': row['answer_format'],
                           'options': [{'id': chr(65+i), 'members': o['members']} for i, o in enumerate(selected)]})
            labels.append({'id': inputs[-1]['id'], 'case_id': case['id'], 'status': 'draft_not_gold',
                           'options': {chr(65+i): {'proposed_grade': o['proposed_grade'], 'explanation': o['explanation'], 'conditions': o.get('conditions', '')} for i, o in enumerate(selected)}})
        all_names = set(state['allies'] + state['enemies'])
        for o in options + unresolved:
            all_names.update(o['members'])
        evidence.append({'ordinal': n, 'map': state['map'],
                         'map_context': index['map_pool_signature'][state['map']]['map_context'],
                         'cards': {name: {k: v for k, v in cards[name].items() if k != 'environment_evidence'} for name in sorted(all_names)},
                         'relations': {name: index['matchup_index']['by_brawler'].get(name, {}) for name in sorted(all_names)},
                         'evidence_refs': {name: index['evidence_refs']['brawlers'].get(name) for name in sorted(all_names)}})
        markdown += [f"## {n}. {state['map']} · {state['mode']} · {'禁用题' if case['task']=='ban' else '第 '+str(state['pick_slot'])+' 手'}", '',
                     f"己方：{'、'.join(state['allies']) or '未选'}；敌方：{'、'.join(state['enemies']) or '未选'}；已知禁用：{'、'.join(state['bans']) or '未提供'}。", '',
                     '| 提议评价 | 选项 | 解释与边界 |', '|---|---|---|']
        for o in options:
            explanation = o['explanation'] + (' 条件：'+o['conditions'] if o.get('conditions') else '')
            markdown.append(f"| {LABELS[o['proposed_grade']]} | {' + '.join(o['members'])} | {explanation.replace('|','／')} |")
        for o in unresolved:
            markdown.append(f"| 待复核，不强行分档 | {' + '.join(o['members'])} | {(o['explanation']+' '+o['conditions']).replace('|','／')} |")
        if not ready:
            markdown += ['', '**暂不开放抽题：原答案尚无充分支持的分支。**']
        if len(good)>3:
            markdown += ['', '正确分支超过单次题卡容量，分批轮换；不删除未展示的正确答案。']
        markdown += ['', f"依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 {n} 行。", '']
    writel(HERE/'questions.draft.jsonl', review)
    writel(HERE/'inputs.options-only.jsonl', inputs)
    writel(HERE/'labels.draft.jsonl', labels)
    writel(HERE/'index-evidence.jsonl', evidence)
    (HERE/'REVIEW.md').write_text('\n'.join(markdown)+'\n')
    skill_dir = ROOT/'skills/brawl-stars-bp-slot-decision'
    skill_hashes = {str(p.relative_to(ROOT)):digest(p) for p in sorted(skill_dir.rglob('*')) if p.is_file() and (p.suffix in ('.md','.py'))}
    writej(HERE/'validation.json', {'cases':len(review), 'supplements':len(supplements)*2,
        'correct_branch_supported_cases':len(review)-len(failures), 'blocked_cases':failures,
        'input_variants':len(inputs), 'enabled_cases':0, 'gold_cases':0,
        'checks_passed':['56 source cases retained','original candidate mechanisms unchanged', 'canonical option names',
                         'known bans/picks excluded','pair cardinality','distinct options', 'option-only export'],
        'not_verified':['new option semantic grades','user confirmation','isolated model correctness','current patch validity','application UI'],
        'runtime_index_sha256':digest(index_path), 'skill_hashes':skill_hashes,
        'artifacts':{name:digest(HERE/name) for name in ('supplements.draft.jsonl','questions.draft.jsonl','inputs.options-only.jsonl','labels.draft.jsonl','index-evidence.jsonl')}})
    print(json.dumps({'cases':len(review),'supplements':len(supplements)*2,'blocked':failures,'input_variants':len(inputs)},ensure_ascii=False))


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--index',type=Path,required=True)
    build(parser.parse_args().index)
