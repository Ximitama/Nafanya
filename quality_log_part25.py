# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: QualityLog
def _format_error(msg: str) -> str:
    return f"❌ Ошибка: {msg}"

def parse_date(date_str):
    for fmt in ["%Y-%m-%d", "%d.%m.%y"]:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Некорректная дата: '{date_str}'")

def validate_entry(entry):
    errors = []
    if not entry.get("check"):
        errors.append("Необходимо указать проверку")
    if not entry.get("defect"):
        errors.append("Необходимо указать дефект")
    if not entry.get("resolution"):
        errors.append("Необходимо указать решение")
    date_str = entry.get("date")
    if date_str:
        try:
            parse_date(date_str)
        except ValueError as e:
            errors.append(str(e))
    owner = entry.get("owner", "")
    if owner and not owner.strip():
        errors.append("Необходимо указать ответственного")
    return _format_error("; ".join(errors)) if errors else None

def add_entry(entry, log):
    err = validate_entry(entry)
    if err:
        print(err); return None
    date_str = entry.get("date", "2024-01-01")
    parsed_date = parse_date(date_str)
    entry_copy = {k: v for k, v in entry.items() if k != "date"}
    entry_copy["date"] = parsed_date.isoformat()
    log.append(entry_copy)
    print(f"✅ Запись добавлена: {entry_copy['check']}")

def get_report(log):
    checks = [e.get("check", "") for e in log]
    defects = [e.get("defect", "") for e in log]
    resolutions = [e.get("resolution", "") for e in log]
    owners = [e.get("owner", "") for e in log if e.get("owner")]
    print(f"📊 Отчёт: проверок={len(log)}, уникальных дефектов={len(set(defects))}")
