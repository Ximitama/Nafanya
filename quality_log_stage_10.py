# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: QualityLog
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "checks": checks,
        "defects": defects,
        "solutions": solutions,
        "owners": owners
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
