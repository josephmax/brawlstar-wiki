"""Compatibility entrypoint; validation lives in the repository maintenance skill."""
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
module = runpy.run_path(str(ROOT / 'skills/brawl-stars-bp-eval-maintenance/scripts/dataset.py'))
if __name__ == '__main__':
    import json
    print(json.dumps(module['validate'](Path(__file__).resolve().parents[1], ROOT, True), ensure_ascii=False, indent=2))
