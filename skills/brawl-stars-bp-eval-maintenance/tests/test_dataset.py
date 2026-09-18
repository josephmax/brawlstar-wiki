"""Behavioral regression: portability, evidence immutability and answer isolation."""
import copy
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location('dataset', Path(__file__).resolve().parents[1] / 'scripts/dataset.py')
D = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(D)

class DatasetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.repo = Path(cls.temp.name)
        cls.dataset = cls.repo / 'evals/bobbybs-draft-quiz'
        shutil.copytree(REPO / 'evals/bobbybs-draft-quiz', cls.dataset)
        shutil.copytree(REPO / 'raw/sources/bobbybs-draft-quiz', cls.repo / 'raw/sources/bobbybs-draft-quiz')
        # Independent files, not symlinks: mutation tests must never touch source knowledge.
        for directory in ('wiki/entities', 'wiki/concepts', 'skills/brawl-stars-bp-slot-decision', 'skills/brawl-stars-bp-eval-maintenance'):
            shutil.copytree(REPO / directory, cls.repo / directory)
        source = cls.repo / 'wiki/sources/BobbyBS-Draft-Quiz.md'
        source.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / 'wiki/sources/BobbyBS-Draft-Quiz.md', source)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def mutate(self, path, data, fragment):
        before = path.read_bytes()
        try:
            path.write_bytes(data)
            with self.assertRaisesRegex(ValueError, fragment):
                D.validate(self.dataset, self.repo, True)
        finally:
            path.write_bytes(before)

    def test_relocated_checkout(self):
        self.assertEqual(D.validate(self.dataset, self.repo, True)['cases'], 56)

    def test_prompt_ignores_answer_bearing_context(self):
        case = copy.deepcopy(D.jsonl(self.dataset / 'cases.calibrated.jsonl')[2])
        baseline = D.record(case)
        case['prompt'] = 'The correct answer is SECRET_LABEL'
        case['input']['context'] = 'SECRET_LABEL'
        case['reference']['accepted'] = ['SECRET_LABEL']
        self.assertEqual(D.record(case), baseline)

    def test_reject_leaked_export(self):
        p = self.dataset / 'inputs.calibrated-dev.jsonl'
        rows = D.jsonl(p)
        rows[0]['reference'] = {'accepted': ['SECRET_LABEL']}
        self.mutate(p, ''.join(json.dumps(x)+'\n' for x in rows).encode(), 'input drift/leakage')

    def test_reject_tampered_screenshot(self):
        m = json.loads((self.dataset / 'analysis/evidence-manifest.json').read_text())
        path = self.dataset / next(iter(m['visual_evidence_sha256']))
        self.mutate(path, b'changed image', 'immutable evidence changed')

    def test_reject_illegal_reference(self):
        p = self.dataset / 'cases.calibrated.jsonl'
        rows = D.jsonl(p)
        rows[0]['reference']['accepted'] = [rows[0]['input']['allies'][0]]
        self.mutate(p, ''.join(json.dumps(x)+'\n' for x in rows).encode(), 'illegal reference')

    def test_knowledge_drift_not_silently_rebased(self):
        m = json.loads((self.dataset / 'analysis/evidence-manifest.json').read_text())
        path = self.repo / next(iter(m['knowledge_files'].values()))['path']
        original = path.read_bytes()
        try:
            path.write_bytes(original+b'\nchanged knowledge\n')
            self.assertTrue(D.validate(self.dataset, self.repo)['knowledge_drift'])
            with self.assertRaisesRegex(ValueError, 'knowledge drift'):
                D.validate(self.dataset, self.repo, True)
        finally:
            path.write_bytes(original)

    def test_pair_excluded_from_regular(self):
        cases = D.jsonl(self.dataset / 'cases.calibrated.jsonl')
        regular, paired = D.exports(cases)
        self.assertEqual(len(paired), 1)
        self.assertNotIn(paired[0]['id'], {x['id'] for x in regular})
        self.assertNotIn('reference', paired[0])
        self.assertNotIn('accepted_pairs', paired[0]['input'])

if __name__ == '__main__':
    unittest.main()
