# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: QualityLog
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record.get('status') != status: continue
        if category and record.get('category') != category: continue
        if tags is not None:
            rec_tags = set(record.get('tags', []))
            if tags and not any(t in rec_tags for t in tags): continue
        filtered.append(record)
    return filtered

def search_records(query=None, status=None, category=None, tags=None):
    results = filter_records(status=status, category=category, tags=tags)
    if query is None: return results
    q_lower = query.lower()
    final_results = []
    for r in results:
        text = f"{r.get('id')} {r.get('title', '')} {r.get('description', '')}".lower()
        if any(q_lower in text.split() or q_lower in text.replace(' ', '') for q in query.lower().split()):
            final_results.append(r)
    return final_results
