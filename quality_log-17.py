# === Stage 17: Добавь группировку записей по категориям ===
# Project: QualityLog
import json, os

def group_records_by_category(records):
    categories = {}
    for r in records:
        cat = r.get("category") or "Uncategorized"
        if cat not in categories:
            categories[cat] = {"items": [], "count": 0}
        categories[cat]["items"].append(r)
        categories[cat]["count"] += 1
    return sorted(categories.items(), key=lambda x: (-x[1]["count"], x[0]))

def add_category_to_record(record, category):
    if not record.get("category"):
        record["category"] = category
    return record

def load_records(path="quality_log.json"):
    try:
        with open(path) as f:
            data = json.load(f)
        records = data.get("records", [])
        if isinstance(records[0], dict):
            return records
        return [dict(zip(records[i::len(records)], records[i+1::len(records)])) for i in range(len(records))]
    except Exception:
        return []

def save_records(path, records):
    with open(path, "w") as f:
        json.dump({"records": records}, f, indent=2)
