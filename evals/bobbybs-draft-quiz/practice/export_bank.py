"""Export the user-approved proposal, preserving draft/source history."""
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
if __name__=='__main__':
    draft=HERE/'questions.draft.jsonl'
    approval=json.loads((HERE/'approval.json').read_text())
    assert hashlib.sha256(draft.read_bytes()).hexdigest()==approval['questions_sha256'], 'Draft changed after approval'
    rows=[json.loads(s) for s in draft.read_text().splitlines()]
    questions=[]
    for q in rows:
        if q['ordinal'] in approval['withheld_ordinals']:continue
        assert q['status']=='pending_confirmation'
        questions.append({'id':q['id'],'ordinal':q['ordinal'],'task':q['task'],'state':q['state'],
                          'answerFormat':q['answer_format'],
                          'options':[{'id':f'o{i+1}','members':o['members'],'grade':o['proposed_grade'],
                                      'explanation':o['explanation'],'conditions':o.get('conditions','')}
                                     for i,o in enumerate(q['options'])]})
    assert len(questions)==53
    data={'schema':'bobby_bp_practice.v1','approval':approval,'gold':False,'questions':questions}
    out=HERE/'bank.json'
    out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'questions':len(questions),'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
