# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: QualityLog
def delete_record(record_id, record_type):
    if not isinstance(record_id, int) or record_id <= 0:
        raise ValueError("ID должен быть положительным целым числом")
    
    try:
        if record_type == 'check':
            del checks[record_id]
        elif record_type == 'defect':
            del defects[record_id]
        elif record_type == 'solution':
            del solutions[record_id]
        elif record_type == 'responsible':
            del responsible[record_id]
        else:
            raise ValueError(f"Неизвестный тип записи: {record_type}")
    except KeyError:
        print(f"Запись с ID {record_id} не найдена.")
