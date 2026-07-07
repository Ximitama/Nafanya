# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: QualityLog
def weekly_stats(log):
    from datetime import date, timedelta
    today = date.today()
    for week_offset in range(4):
        end_date = today - timedelta(days=week_offset * 7)
        start_date = end_date - timedelta(days=6)
        stats = {"start": start_date, "end": end_date, "checks": 0, "defects": 0, "resolved": 0}
        for entry in log:
            if isinstance(entry, dict):
                d = entry.get("date") or today
                try:
                    d = date.fromisoformat(d) if not isinstance(d, date) else d
                except (ValueError, TypeError):
                    continue
                if start_date <= d <= end_date:
                    stats["checks"] += 1
                    if entry.get("status") in ("defect", "open"):
                        stats["defects"] += 1
                    elif entry.get("status") == "resolved":
                        stats["resolved"] += 1
        print(f"Week {start_date} to {end_date}: checks={stats['checks']}, defects={stats['defects']}, resolved={stats['resolved']}")

weekly_stats(log)
