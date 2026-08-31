# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: QualityLog
import unittest

class TestQualityLog(unittest.TestCase):
    def test_create_check(self):
        check = Check("test_check", "Check description")
        self.assertEqual(check.name, "test_check")
        self.assertEqual(check.description, "Check description")
        self.assertEqual(check.status, "pending")

    def test_create_defect(self):
        defect = Defect("defect_1", "Severity: High", "Component: Engine")
        self.assertEqual(defect.name, "defect_1")
        self.assertEqual(defect.severity, "High")
        self.assertEqual(defect.component, "Engine")

    def test_create_solution(self):
        solution = Solution("sol_1", "Fix applied", "Engine")
        self.assertEqual(solution.name, "sol_1")
        self.assertEqual(solution.description, "Fix applied")
        self.assertEqual(solution.component, "Engine")

    def test_create_person(self):
        person = Person("John Doe", "+1234567890", "john@example.com")
        self.assertEqual(person.name, "John Doe")
        self.assertEqual(person.phone, "+1234567890")
        self.assertEqual(person.email, "john@example.com")

    def test_create_quality_log(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        self.assertEqual(log.name, "qlog_1")
        self.assertEqual(log.description, "Quality Log Description")
        self.assertEqual(log.checks, [])
        self.assertEqual(log.defects, [])
        self.assertEqual(log.solutions, [])
        self.assertEqual(log.persons, [])

    def test_add_check_to_log(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        check = Check("test_check", "Check description")
        log.add_check(check)
        self.assertEqual(len(log.checks), 1)
        self.assertEqual(log.checks[0].name, "test_check")

    def test_add_defect_to_log(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        defect = Defect("defect_1", "Severity: High", "Component: Engine")
        log.add_defect(defect)
        self.assertEqual(len(log.defects), 1)
        self.assertEqual(log.defects[0].name, "defect_1")

    def test_add_solution_to_log(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        solution = Solution("sol_1", "Fix applied", "Engine")
        log.add_solution(solution)
        self.assertEqual(len(log.solutions), 1)
        self.assertEqual(log.solutions[0].name, "sol_1")

    def test_add_person_to_log(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        person = Person("John Doe", "+1234567890", "john@example.com")
        log.add_person(person)
        self.assertEqual(len(log.persons), 1)
        self.assertEqual(log.persons[0].name, "John Doe")

    def test_get_defect_by_name(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        defect = Defect("defect_1", "Severity: High", "Component: Engine")
        log.add_defect(defect)
        found = log.get_defect_by_name("defect_1")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "defect_1")

    def test_get_defect_not_found(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        found = log.get_defect_by_name("nonexistent")
        self.assertIsNone(found)

    def test_get_solution_by_name(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        solution = Solution("sol_1", "Fix applied", "Engine")
        log.add_solution(solution)
        found = log.get_solution_by_name("sol_1")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "sol_1")

    def test_get_solution_not_found(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        found = log.get_solution_by_name("nonexistent")
        self.assertIsNone(found)

    def test_get_person_by_name(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        person = Person("John Doe", "+1234567890", "john@example.com")
        log.add_person(person)
        found = log.get_person_by_name("John Doe")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "John Doe")

    def test_get_person_not_found(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        found = log.get_person_by_name("Nonexistent")
        self.assertIsNone(found)

    def test_get_check_by_name(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        check = Check("test_check", "Check description")
        log.add_check(check)
        found = log.get_check_by_name("test_check")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "test_check")

    def test_get_check_not_found(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        found = log.get_check_by_name("nonexistent")
        self.assertIsNone(found)

    def test_mark_check_done(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        check = Check("test_check", "Check description")
        log.add_check(check)
        log.mark_check_done(check)
        self.assertEqual(check.status, "done")

    def test_mark_check_failed(self):
        log = QualityLog("qlog_1", "Quality Log Description")
        check = Check("test_check", "Check description")
        log.add_check(check)
        log.mark_check_failed(check)
        self.assertEqual(check.status, "failed")
