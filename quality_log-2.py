# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: QualityLog
class QualityLog:
    def __init__(self):
        self.checks = []
        self.defects = []
        self.solutions = []
    
    def validate_input(self, text: str) -> bool:
        if not isinstance(text, str) or len(text.strip()) == 0:
            return False
        return True
    
    def add_check(self, name: str, description: str):
        if not self.validate_input(name) or not self.validate_input(description):
            print("Ошибка валидации данных для проверки.")
            return None
        self.checks.append({"name": name, "description": description})
    
    def add_defect(self, check_name: str, defect_type: str, severity: int):
        if not self.validate_input(check_name) or not self.validate_input(defect_type):
            print("Ошибка валидации данных для дефекта.")
            return None
        if not isinstance(severity, int) or severity < 1 or severity > 5:
            print("Ошибка валидации уровня серьезности (1-5).")
            return None
        self.defects.append({"check_name": check_name, "type": defect_type, "severity": severity})
    
    def add_solution(self, defect_id: int, solution_text: str):
        if not self.validate_input(solution_text) or defect_id < 0:
            print("Ошибка валидации данных для решения.")
            return None
        self.solutions.append({"defect_id": defect_id, "text": solution_text})
