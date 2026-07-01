# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: QualityLog
def load_from_json(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [QualityLogItem.from_dict(item) for item in data]
        elif isinstance(data, dict):
            return [QualityLogItem.from_dict(v) for k, v in data.items()]
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в {filepath}: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке {filepath}: {e}")
        return []
