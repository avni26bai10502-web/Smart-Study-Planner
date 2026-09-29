import os
import tempfile
import unittest

import database
import validation


class TestValidation(unittest.TestCase):

    def test_valid_text(self):
        self.assertTrue(
            validation.validate_text("Python")
        )

    def test_empty_text(self):
        self.assertFalse(
            validation.validate_text("")
        )

    def test_valid_date(self):
        self.assertTrue(
            validation.validate_date("30-09-2026")
        )

    def test_invalid_date(self):
        self.assertFalse(
            validation.validate_date("hello")
        )

    def test_valid_priority(self):
        self.assertTrue(
            validation.validate_priority("High")
        )

    def test_invalid_priority(self):
        self.assertFalse(
            validation.validate_priority("ABC")
        )

    def test_valid_duration(self):
        self.assertTrue(
            validation.validate_duration("60")
        )

    def test_invalid_duration(self):
        self.assertFalse(
            validation.validate_duration("-10")
        )

    def test_valid_id(self):
        self.assertTrue(
            validation.validate_id("1")
        )

    def test_invalid_id(self):
        self.assertFalse(
            validation.validate_id("0")
        )


class TestDatabase(unittest.TestCase):

    def setUp(self):

        self.temp_file = tempfile.NamedTemporaryFile(
            delete=False
        )

        self.temp_file.close()

        database.set_database(
            self.temp_file.name
        )

        database.create_tables()

    def tearDown(self):

        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

        database.set_database(
            "study_planner.db"
        )

    def test_add_subject(self):

        result = database.add_subject(
            "Python"
        )

        self.assertTrue(result)

        subjects = database.get_subjects()

        self.assertEqual(
            len(subjects),
            1
        )

        self.assertEqual(
            subjects[0][1],
            "Python"
        )

    def test_duplicate_subject(self):

        database.add_subject("Python")

        result = database.add_subject(
            "Python"
        )

        self.assertFalse(result)

    def test_add_task(self):

        task_id = database.add_task(
            "Python Assignment",
            "Python",
            "30-09-2026",
            "High"
        )

        self.assertIsNotNone(task_id)

        tasks = database.get_tasks()

        self.assertEqual(
            len(tasks),
            1
        )

        self.assertEqual(
            tasks[0][1],
            "Python Assignment"
        )

    def test_complete_task(self):

        task_id = database.add_task(
            "Python Assignment",
            "Python",
            "30-09-2026",
            "High"
        )

        result = database.complete_task(
            task_id
        )

        self.assertTrue(result)

        tasks = database.get_tasks()

        self.assertEqual(
            tasks[0][5],
            "Completed"
        )

    def test_add_study_session(self):

        session_id = database.add_study_session(
            "Python",
            "30-09-2026",
            60
        )

        self.assertIsNotNone(
            session_id
        )

        sessions = database.get_study_sessions()

        self.assertEqual(
            len(sessions),
            1
        )

        self.assertEqual(
            sessions[0][3],
            60
        )

    def test_progress(self):

        task_id = database.add_task(
            "Python Assignment",
            "Python",
            "30-09-2026",
            "High"
        )

        database.complete_task(
            task_id
        )

        database.add_task(
            "Math Assignment",
            "Mathematics",
            "01-10-2026",
            "Medium"
        )

        total, completed = (
            database.get_task_progress()
        )

        self.assertEqual(
            total,
            2
        )

        self.assertEqual(
            completed,
            1
        )

    def test_total_study_time(self):

        database.add_study_session(
            "Python",
            "30-09-2026",
            60
        )

        database.add_study_session(
            "Mathematics",
            "01-10-2026",
            90
        )

        total = (
            database.get_total_study_time()
        )

        self.assertEqual(
            total,
            150
        )


if __name__ == "__main__":
    unittest.main()