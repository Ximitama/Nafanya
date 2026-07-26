# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: QualityLog
def reset_demo_data():
    """Сбросить все данные в журнал к демо-состоянию."""
    global checks, defects, solutions, assignments
    
    checks = [
        {"id": 1, "title": "Проверка 1: Размер партии", "status": "passed", "date": "2024-01-15"},
        {"id": 2, "title": "Проверка 2: Качество упаковки", "status": "failed", "date": "2024-01-16"},
    ]
    
    defects = [
        {"id": 1, "check_id": 2, "description": "Повреждения при упаковке", "severity": "medium", "responsible": "Иванов И.И.", "status": "in_progress"},
    ]
    
    solutions = []
    assignments = [
        {"defect_id": 1, "assigned_to": "Петрова А.А.", "deadline": "2024-02-01", "status": "pending"},
    ]

def clear_all_data():
    """Полная очистка всех данных в журнале."""
    global checks, defects, solutions, assignments
    
    checks = []
    defects = []
    solutions = []
    assignments = []
