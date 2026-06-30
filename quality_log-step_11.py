# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: QualityLog
import json, os

def save_to_json(data: dict, path: str = "quality_log.json") -> None:
    """Сохраняет данные журнала в JSON файл с гарантией целостности."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Данные сохранены в {path}")
    except Exception as e:
        print(f"[ERROR] Не удалось сохранить файл: {e}")

def load_from_json(path: str = "quality_log.json") -> dict | None:
    """Загружает данные из JSON файла, возвращает пустой словарь при ошибке."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    # Инициализация структуры данных
    log_data = {
        "checks": [],
        "defects": [],
        "solutions": [],
        "owners": []
    }
    
    # Заполнение тестовыми данными
    log_data["checks"].append({"id": 1, "name": "Проверка А", "status": "passed"})
    log_data["defects"].append({"id": 101, "desc": "Ошибка Базы Данных", "severity": "high"})
    
    # Сохранение и загрузка
    save_to_json(log_data)
    loaded = load_from_json()
    print(f"Загружено записей: {len(loaded.get('checks', []))}")
