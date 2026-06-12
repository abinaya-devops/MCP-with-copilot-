import json
import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import app as app_module


class PersistenceTests(unittest.TestCase):
    def test_load_activities_reads_json_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "activities.json"
            expected = {
                "Chess Club": {
                    "description": "Test activity",
                    "schedule": "Fridays",
                    "max_participants": 5,
                    "participants": ["student@example.edu"],
                }
            }
            file_path.write_text(json.dumps(expected), encoding="utf-8")

            loaded = app_module.load_activities(file_path)

            self.assertEqual(loaded, expected)

    def test_save_activities_writes_json_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "activities.json"
            activities = {
                "Chess Club": {
                    "description": "Test activity",
                    "schedule": "Fridays",
                    "max_participants": 5,
                    "participants": ["student@example.edu"],
                }
            }

            app_module.save_activities(activities, file_path)

            self.assertTrue(file_path.exists())
            self.assertEqual(json.loads(file_path.read_text(encoding="utf-8")), activities)


if __name__ == "__main__":
    unittest.main()
