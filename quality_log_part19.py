# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: QualityLog
def archive_records(records, cutoff_days=365):
    """Archive records older than cutoff_days into a new log."""
    import datetime
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=cutoff_days)
    archived = [r for r in records if r['date'] < cutoff]
    active = [r for r in records if r['date'] >= cutoff]
    new_log = {
        'records': active,
        'archived_records': archived,
        'archive_date': now.isoformat(),
        'status': 'completed' if not archived else 'partial',
    }
    return new_log

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'date': '2023-01-15', 'type': 'inspection', 'status': 'closed'},
        {'id': 2, 'date': '2024-06-20', 'type': 'defect', 'status': 'open'},
    ]
    result = archive_records(sample_data)
    print(result)
