# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: QualityLog
TEMPLATE_REGISTRY = {}
def register_template(name, fields):
    TEMPLATE_REGISTRY[name] = fields
def create_from_template(name, **kwargs):
    if name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Unknown template: {name}")
    record = {"template": name, "status": "new", "date": datetime.now().strftime("%Y-%m-%d %H:%M")}
    record.update(kwargs)
    return record
