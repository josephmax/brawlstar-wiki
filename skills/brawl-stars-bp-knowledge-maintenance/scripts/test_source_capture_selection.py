import tempfile
import unittest
from pathlib import Path

from ingest_brawler_sources import latest_direct_raw


class SourceSelectionTest(unittest.TestCase):
    def test_newer_dated_capture_beats_old_canonical_and_ignores_other_slug(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for filename, date in [('gus.md', '2026-09-17'), ('gus-2026-10-21.md', '2026-10-21'), ('gus-extra-2026-10-22.md', '2026-10-22')]:
                (root / filename).write_text(f'# Direct Raw Capture: Fandom Gus\n\n- Capture date: {date}\n')
            self.assertEqual(latest_direct_raw(root, 'gus').name, 'gus-2026-10-21.md')

    def test_newer_canonical_and_inaccessible_capture(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'gus.md').write_text('# Direct Raw Capture: Fandom Gus\n- Capture date: 2026-10-21\n')
            (root / 'gus-2026-09-17.md').write_text('# Direct Raw Capture: Fandom Gus\n- Capture date: 2026-09-17\n')
            (root / 'gus-2026-10-22.md').write_text('# Inaccessible Raw Capture\n- Capture date: 2026-10-22\n')
            self.assertEqual(latest_direct_raw(root, 'gus').name, 'gus.md')


if __name__ == '__main__':
    unittest.main()
