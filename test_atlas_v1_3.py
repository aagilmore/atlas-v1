"""Run with: python3 -m unittest test_atlas_v1_3.py"""
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import atlas_weekly_archive_v1_3 as archive
import web_app_v10 as app_module


def record(period, score=82):
    return {
        "week": {"date_range": period, "reporting_week": "Test"},
        "strategic_scorecard": {"performance_score": {"score": score}},
        "weekly_execution_scorecard": {"nutrition": {"fiber": {"actual": 30}, "saturated_fat": {"actual": 18}}},
        "atlas_weekly_brief": {"narrative": "Original Wilson coaching retained"},
    }


class WeeklyHistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.archive_path = Path(self.temp.name) / "weekly.json"
        self.health_path = Path(self.temp.name) / "health.json"
        self.health_path.write_text(json.dumps({"measurements": [{"metric": "apob", "date": "2024-01", "value": 109}]}))
        self.path_patch = patch.object(archive, "PATH", self.archive_path)
        self.health_patch = patch.object(app_module, "HEALTH_HISTORY_FILE", self.health_path)
        self.path_patch.start()
        self.health_patch.start()
        self.addCleanup(self.path_patch.stop)
        self.addCleanup(self.health_patch.stop)
        self.client = app_module.app.test_client()

    def test_lossless_and_corrected_upload(self):
        original = record("Oct 10–16, 2026")
        archive.store([original])
        self.assertEqual(archive.read()["weekly_checkins"][original["week"]["date_range"]], original)
        corrected = record("Oct 10–16, 2026", 85)
        archive.store([corrected])
        self.assertEqual(len(archive.read()["weekly_checkins"]), 1)
        self.assertEqual(archive.read()["weekly_checkins"][original["week"]["date_range"]]["strategic_scorecard"]["performance_score"]["score"], 85)

    def test_bulk_import_and_export_preserve_metabolic(self):
        records = [record("Aug 1–7, 2026"), record("Aug 8–14, 2026")]
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as bundle:
            for i, item in enumerate(records):
                bundle.writestr(f"week{i}.json", json.dumps(item))
        stream.seek(0)
        response = self.client.post("/history/import", data={"history_files": (stream, "history.zip")})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(archive.read()["weekly_checkins"]), 2)
        download = self.client.get("/history/download")
        self.assertEqual(download.status_code, 200)
        payload = json.loads(download.data)
        self.assertEqual(len(payload["weekly_checkins"]), 2)
        self.assertEqual(payload["metabolic_history"]["measurements"][0]["value"], 109)

    def test_bad_batch_does_not_modify_archive(self):
        archive.store([record("Aug 1–7, 2026")])
        valid = io.BytesIO(json.dumps(record("Aug 8–14, 2026")).encode())
        invalid = io.BytesIO(b"{invalid")
        result = self.client.post("/history/import", data={"history_files": [(valid, "valid.json"), (invalid, "bad.json")]})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(len(archive.read()["weekly_checkins"]), 1)

    def test_old_week_does_not_need_new_nutrients(self):
        item = record("Sep 1–7, 2026")
        item["weekly_execution_scorecard"]["nutrition"] = {}
        archive.store([item])
        self.assertEqual(len(archive.read()["weekly_checkins"]), 1)

    def test_rejects_missing_week_and_preserves_archive(self):
        with self.assertRaises(ValueError):
            archive.store([{"strategic_scorecard": {}, "weekly_execution_scorecard": {}, "atlas_weekly_brief": {}}])
        self.assertFalse(self.archive_path.exists())


if __name__ == "__main__":
    unittest.main()
