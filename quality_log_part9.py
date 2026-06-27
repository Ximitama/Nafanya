# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: QualityLog
import json, sys

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект (dict)")
        
        # Валидация структуры данных
        required_keys = ['checks', 'defects', 'solutions']
        for key in required_keys:
            if key not in data:
                print(f"Предупреждение: отсутствует ключ '{key}'")
        
        return {
            "checks": data.get("checks", []),
            "defects": data.get("defects", []),
            "solutions": data.get("solutions", [])
        }

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Пример использования с тестовой строкой
    sample_json = '''
    {
        "checks": [
            {"id": 1, "title": "Проверка базы данных", "status": "passed"}
        ],
        "defects": [],
        "solutions": []
    }
    '''
    
    loaded_data = load_initial_data(sample_json)
    print(f"Загружено проверок: {len(loaded_data['checks'])}")
