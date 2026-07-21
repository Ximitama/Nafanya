# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: QualityLog
def show_record(record):
    """Компактный вывод одной записи журнала качества."""
    parts = []
    if record.get("check"):
        parts.append(f"Проверка: {record['check']}")
    else:
        parts.append(f"Дефект: {record.get('defect', 'Не указан')}")

    if record.get("solution"):
        parts.append(f"Решение: {record['solution']}")
    elif record.get("open_issue"):
        parts.append(f"Открытый вопрос: {record['open_issue']}")

    status = record.get("status", "Неизвестный")
    if status in ("resolved", "closed"):
        parts.append(f"[{status.upper()}]")
    else:
        parts.append(f"[{status}]")

    responsible = record.get("responsible_person", "")
    if responsible:
        parts.append(f"Ответственный: {responsible}")

    created = record.get("created_at", "Без даты")
    last_updated = record.get("last_updated", None)
    if last_updated and last_updated != created:
        parts.append(f"Обновлено: {last_updated}")

    print("--- Запись журнала качества ---")
    for line in parts:
        print(line)
