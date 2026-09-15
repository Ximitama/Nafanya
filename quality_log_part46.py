# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: QualityLog
import sys
import csv
import json
from pathlib import Path
from datetime import datetime

def migrate_quality_log(log_file: str) -> None:
    """
    Миграция структуры данных журнала контроля качества.
    Проверяет, что все строки журнала имеют обязательные поля:
    - id
    - date
    - type (check/defect/solution/responsible)
    - description
    - status (open/closed)
    - assigned_to (для type=responsible)
    """
    log_path = Path(log_file)
    if not log_path.exists():
        print(f"Файл журнала не найден: {log_file}")
        return

    rows = []
    with open(log_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            # Обработка полей с возможными пустыми значениями
            row['id'] = row.get('id', '').strip() or f"Q{i}"
            row['date'] = row.get('date', '').strip() or datetime.now().strftime('%Y-%m-%d')
            row['type'] = row.get('type', '').strip().lower()
            row['description'] = row.get('description', '').strip()
            row['status'] = row.get('status', 'open').strip().lower()

            if row['type'] == 'responsible':
                row['assigned_to'] = row.get('assigned_to', '').strip() or 'unknown'
            else:
                row['assigned_to'] = ''

            # Запись в новый формат
            new_row = {
                'id': row['id'],
                'date': row['date'],
                'type': row['type'],
                'description': row['description'],
                'status': row['status'],
                'assigned_to': row['assigned_to']
            }
            rows.append(new_row)

    # Запись в новый формат CSV
    fieldnames = ['id', 'date', 'type', 'description', 'status', 'assigned_to']
    with open(log_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Миграция завершена. Обновлено {len(rows)} записей в {log_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python migrate.py <путь_к_файлу_журнала>")
        sys.exit(1)
    migrate_quality_log(sys.argv[1])
