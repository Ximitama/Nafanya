# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: QualityLog
def search_logs(query, fields=None):
    if not query: return []
    q = query.lower()
    results = [log for log in logs]
    if fields is None:
        fields = ['check_name', 'defect_desc', 'solution_text']
    filtered = []
    for log in results:
        found = False
        for field in fields:
            val = str(log.get(field, '')).lower()
            if q in val:
                found = True
                break
        if found:
            filtered.append(log)
    return filtered
