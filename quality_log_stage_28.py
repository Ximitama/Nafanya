# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: QualityLog
def print_metrics(logs):
    if not logs:
        print("Нет данных для анализа.")
        return
    total = len(logs)
    checks = [l for l in logs if isinstance(l, dict) and 'type' in l and l['type'] == 'check']
    defects = [l for l in logs if isinstance(l, dict) and 'type' in l and l['type'] == 'defect']
    resolutions = [l for l in logs if isinstance(l, dict) and 'type' in l and l['type'] == 'resolution']
    print(f"Всего записей: {total}")
    print(f"Проверки пройдены: {len(checks)}")
    print(f"Дефекты найдено: {len(defects)}")
    print(f"Решения внесено: {len(resolutions)}")
    if defects and resolutions:
        print(f"Решено дефектов: {sum(1 for r in resolutions if any(d['id'] == r.get('defect_id') for d in defects))}")
