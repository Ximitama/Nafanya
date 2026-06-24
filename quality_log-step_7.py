# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: QualityLog
def sort_records(records, key='date', reverse=True):
    if not records: return []
    order = {'priority': 10, 'severity': 20, 'status': 30}
    def get_sort_key(item):
        val = item.get(key) or ''
        if isinstance(val, str):
            try: int(val); return (order.get(key, 40), -int(val))
            except ValueError: return (order.get(key, 40), val.lower())
        elif key == 'date':
            dt = item.get('created_at') or item.get('updated_at')
            if isinstance(dt, str):
                try: return (order.get(key, 40), datetime.strptime(dt[:19], '%Y-%m-%d %H:%M:%S'))
                except ValueError: return (order.get(key, 40), dt)
        elif key == 'priority':
            p = item.get('priority') or item.get('severity', '')
            if isinstance(p, str):
                try: return (order.get(key, 40), -int(p))
                except ValueError: return (order.get(key, 40), p.lower())
        elif key == 'status':
            s = item.get('status') or ''
            status_map = {'open': 1, 'in_progress': 2, 'resolved': 3, 'closed': 4}
            return (order.get(key, 40), status_map.get(s.lower(), 5))
        elif key == 'name' or key == 'title':
            n = item.get('name') or item.get('title', '')
            if isinstance(n, str): return (order.get(key, 40), n.lower())
        return (order.get(key, 40), val)
    sorted_records = sorted(records, key=get_sort_key, reverse=reverse)
    for i in range(len(sorted_records)):
        r = sorted_records[i]
        if 'sort_order' not in r: r['sort_order'] = i + 1
    return sorted_records
