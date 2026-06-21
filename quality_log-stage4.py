# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: QualityLog
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in ['id', 'created_at']:
            continue  # Запрещаем изменение ключевых полей и времени создания
        records[record_id][key] = value
    
    print(f"Запись {record_id} успешно обновлена.")
    return True
