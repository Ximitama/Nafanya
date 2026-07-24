# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: QualityLog
def demo_quality_log():
    import sys, os
    print("=" * 60)
    print("DEMO: QualityLog — быстрый ручной тест")
    print("=" * 60)
    print(f"Python {sys.version}")
    print(f"Файл проекта: {os.path.abspath(__file__)}")
    print()

    # Имитация создания записи о проверке
    record = {"id": 1, "type": "test", "result": True, "status": "passed"}
    print("[DEMO] Тестовая проверка #1 — результат:", record)

    # Имитация добавления дефекта
    defect = {"id": 2, "severity": "medium", "description": "Визуальный баг", "assignee": "dev_01"}
    print("[DEMO] Дефект #2 — статус:", defect["severity"], "-", defect["description"])

    # Имитация решения
    solution = {"id": 3, "for_defect": 2, "action": "исправить", "verified": True}
    print("[DEMO] Решение #3 для дефекта:", solution)

    # Подсчёт записей
    total_records = len([record]) + len([defect]) + len([solution])
    print(f"[DEMO] Всего демо-записей: {total_records}")
    print()
    print("=" * 60)
    print("Demo завершён. Для запуска полноценного проекта используйте main().")
    print("=" * 60)

if __name__ == "__main__":
    demo_quality_log()
