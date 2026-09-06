# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: QualityLog
def dry_run_mode():
    import sys
    dry = os.environ.get("QUALITYLOG_DRY_RUN", "").lower() in ("1", "true", "yes")
    if dry:
        print("[DRY-RUN] Операция будет записана в лог, но не сохранена в файл.")
        sys.stdout.flush()
    return dry

def log_action(action, data, dry=False):
    if dry:
        print(f"[DRY-RUN] {action}: {json.dumps(data, ensure_ascii=False)}")
        return False
    with open(QUALITYLOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{action}\t{json.dumps(data, ensure_ascii=False)}\n")
    return True

def read_log():
    if not os.path.exists(QUALITYLOG_FILE):
        return []
    entries = []
    with open(QUALITYLOG_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t", 1)
            if len(parts) == 2:
                action, payload = parts
                entries.append({"action": action, "data": json.loads(payload)})
    return entries

def save_log(entries):
    with open(QUALITYLOG_FILE, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(f"{e['action']}\t{json.dumps(e['data'], ensure_ascii=False)}\n")

def log_check(check_type, name, result, details=None, dry=False):
    record = {"type": "check", "name": name, "result": result, "details": details or {}}
    return log_action(record["type"], record, dry)

def log_defect(defect_type, description, severity, assignee, status="open", dry=False):
    record = {"type": "defect", "description": description, "severity": severity,
              "assignee": assignee, "status": status}
    return log_action(record["type"], record, dry)

def log_resolution(related_defect, description, assignee, dry=False):
    record = {"type": "resolution", "related_defect": related_defect,
              "description": description, "assignee": assignee}
    return log_action(record["type"], record, dry)

def log_feedback(feedback_type, target, content, dry=False):
    record = {"type": "feedback", "target": target, "content": content}
    return log_action(record["type"], record, dry)
