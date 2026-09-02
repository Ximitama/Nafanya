# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: QualityLog
import unittest


class TestEdgeCases(unittest.TestCase):
    def test_empty_log(self):
        from project import QualityLog
        log = QualityLog()
        self.assertEqual(len(log), 0)

    def test_duplicate_check(self):
        from project import QualityLog
        log = QualityLog()
        log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01")
        log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01")
        self.assertEqual(len(log), 1)

    def test_missing_field(self):
        from project import QualityLog
        log = QualityLog()
        with self.assertRaises(ValueError):
            log.add_check("", "load > 90%", "Critical", "admin", "2024-01-01")

    def test_invalid_date(self):
        from project import QualityLog
        log = QualityLog()
        with self.assertRaises(ValueError):
            log.add_check("CPU", "load > 90%", "Critical", "admin", "not-a-date")

    def test_invalid_priority(self):
        from project import QualityLog
        log = QualityLog()
        with self.assertRaises(ValueError):
            log.add_check("CPU", "load > 90%", "Urgent", "admin", "2024-01-01")

    def test_empty_status(self):
        from project import QualityLog
        log = QualityLog()
        with self.assertRaises(ValueError):
            log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01", "")

    def test_nonexistent_check(self):
        from project import QualityLog
        log = QualityLog()
        log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01")
        with self.assertRaises(KeyError):
            log.add_defect("NonExistent", "load > 90%", "Critical", "admin", "2024-01-01")

    def test_nonexistent_check_defect(self):
        from project import QualityLog
        log = QualityLog()
        log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01")
        with self.assertRaises(KeyError):
            log.add_defect("NonExistent", "load > 90%", "Critical", "admin", "2024-01-01", "Fix")

    def test_nonexistent_check_solution(self):
        from project import QualityLog
        log = QualityLog()
        log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01")
        with self.assertRaises(KeyError):
            log.add_solution("NonExistent", "CPU", "load > 90%", "Critical", "Fix")

    def test_nonexistent_check_solution_defect(self):
        from project import QualityLog
        log = QualityLog()
        log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01")
        log.add_defect("CPU", "load > 90%", "Critical", "admin", "2024-01-01", "Fix")
        with self.assertRaises(KeyError):
            log.add_solution("NonExistent", "CPU", "load > 90%", "Critical", "Fix")

    def test_nonexistent_check_solution_defect(self):
        from project import QualityLog
        log = QualityLog()
        log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01")
        log.add_defect("CPU", "load > 90%", "Critical", "admin", "2024-01-01", "Fix")
        with self.assertRaises(KeyError):
            log.add_solution("NonExistent", "CPU", "load > 90%", "Critical", "Fix")

    def test_nonexistent_check_solution_defect(self):
        from project import QualityLog
        log = QualityLog()
        log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01")
        log.add_defect("CPU", "load > 90%", "Critical", "admin", "2024-01-01", "Fix")
        with self.assertRaises(KeyError):
            log.add_solution("NonExistent", "CPU", "load > 90%", "Critical", "Fix")

    def test_nonexistent_check_solution_defect(self):
        from project import QualityLog
        log = QualityLog()
        log.add_check("CPU", "load > 90%", "Critical", "admin", "2024-01-01")
        log.add_defect("CPU", "load > 90%", "Critical", "admin", "2024-01-01", "Fix")
        with self.assertRaises(KeyError):
            log.add_solution("NonExistent", "CPU", "load > 90%", "Critical", "Fix")


if __name__ == '__main__':
    unittest.main()
