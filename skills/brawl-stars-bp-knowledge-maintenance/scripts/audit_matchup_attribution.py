#!/usr/bin/env python3
"""Inventory every matchup for human attribution review; never changes facts.

Cues are not error verdicts. Opposite directions can have different conditions;
a PLP list change neither proves nor disproves a conditional mechanism.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def audit(repo: Path) -> dict:
    compiler = load_module('attribution_compiler', repo / 'skills/brawl-stars-bp-slot-decision/scripts/compile_runtime_index.py')
    coverage = load_module('attribution_coverage', repo / 'skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_plp_matchup_coverage.py')
    paths = sorted((repo / 'wiki/entities/brawlers').glob('*.md'))
    cards = [compiler.compile_brawler_card(path, repo) for path in paths]
    lookup = coverage.name_lookup({card['brawler'] for card in cards})
    plp = coverage.plp_matchup_pairs(repo, repo / 'raw/sources/pl-prodigy/brawlers', lookup)
    source_pairs = {(r['subject'], r['direction'], r['target']) for r in plp}
    source_subjects = {r['subject'] for r in plp}
    pairs = defaultdict(list)
    heroes, entries = [], []
    for path, card in zip(paths, cards):
        text = path.read_text(encoding='utf-8')
        rows = card['conditional_matchups']
        start = text.find('  conditional_matchups:')
        end = re.search(r'^  [a-z_]+:', text[start + 1:], re.M) if start >= 0 else None
        section = text[start:start + 1 + end.start()] if end else text[start:]
        locations = [start + m.start() for m in re.finditer(r'^    - target:', section, re.M)]
        if len(locations) != len(rows):
            raise ValueError(f'{path}: source location / compiler row mismatch')
        heroes.append({'brawler': card['brawler'], 'path': str(path.relative_to(repo)),
                       'sha256': hashlib.sha256(text.encode()).hexdigest(),
                       'entries': len(rows), 'expanded_targets': sum(len(r['target']) for r in rows),
                       'review_status': 'inventoried_not_semantically_verified' if rows else 'no_matchup_entries'})
        for ordinal, (row, location) in enumerate(zip(rows, locations), 1):
            record = {'id': f"{card['brawler']}:{ordinal}", 'brawler': card['brawler'],
                      'path': str(path.relative_to(repo)), 'line': text.count('\n', 0, location) + 1,
                      **row, 'cues': [], 'not_in_latest_plp': [], 'unknown_targets': []}
            if len(row['target']) > 1:
                record['cues'].append('shared_target_scope_needs_per_target_review')
            missing = [k for k in ('target', 'direction', 'source', 'mechanism', 'active_when', 'fails_when', 'bp_use') if not row.get(k)]
            if missing:
                record['missing_fields'] = missing
            if row.get('direction') not in ('subject_favored', 'target_favored'):
                record['cues'].append('invalid_direction')
            # This signals a provenance gap, not that the explanation is false.
            source = str(row.get('source', ''))
            if 'PLP-' in source and 'Fandom-' not in source:
                record['cues'].append('plp_named_without_fandom_in_row_source')
            direction = {'subject_favored': 'answers', 'target_favored': 'is_answered_by'}.get(row.get('direction'))
            for target in row['target']:
                canonical = coverage.canonical_name(target, lookup)
                if canonical is None:
                    record['unknown_targets'].append(target)
                    continue
                key = (card['brawler'], direction, canonical)
                pairs[key].append(record['id'])
                if card['brawler'] in source_subjects and key not in source_pairs:
                    record['not_in_latest_plp'].append(canonical)
            entries.append(record)
    duplicates = [{'subject': k[0], 'direction': k[1], 'target': k[2], 'entries': v}
                  for k, v in sorted(pairs.items()) if len(v) > 1]
    bidirectional = [{'subject': s, 'target': t, 'answers': pairs[(s, d, t)],
                      'is_answered_by': pairs[(s, 'is_answered_by', t)]}
                     for s, d, t in sorted(pairs) if d == 'answers' and (s, 'is_answered_by', t) in pairs]
    return {'schema': 'matchup-attribution-audit.v1',
            'knowledge_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip(),
            'scope': 'Frozen local knowledge; cues are not semantic verdicts. Per-file hashes identify scanned content.',
            'summary': {'heroes': len(heroes), 'heroes_with_entries': sum(bool(h['entries']) for h in heroes),
                        'entries': len(entries), 'expanded_targets': sum(len(r['target']) for r in entries),
                        'unique_directed_pairs': len(pairs), 'multi_target_entries': sum(len(r['target']) > 1 for r in entries),
                        'duplicate_pair_groups': len(duplicates), 'both_directions_within_subject': len(bidirectional),
                        'entries_missing_fields': sum(bool(r.get('missing_fields')) for r in entries),
                        'unknown_targets': sum(len(r['unknown_targets']) for r in entries)},
            'heroes': heroes, 'entries': entries, 'duplicate_pairs': duplicates,
            'both_directions_within_subject': bidirectional}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--output', type=Path, default=Path('outputs/matchup-audit/inventory.json'))
    args = parser.parse_args()
    repo = args.repo.resolve()
    result = audit(repo)
    output = args.output if args.output.is_absolute() else repo / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result['summary'], ensure_ascii=False))


if __name__ == '__main__':
    main()
