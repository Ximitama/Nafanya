# === Stage 20: Добавь восстановление записей из архива ===
# Project: QualityLog
def archive_recovery():
    import json, time
    ARCHIVE_FILE = "archive.json"
    if not os.path.exists(ARCHIVE_FILE): return
    with open(ARCHIVE_FILE) as f: records = json.load(f)
    now = time.strftime("%Y-%m-%d %H:%M")
    for r in records: print(json.dumps(r, indent=2))
