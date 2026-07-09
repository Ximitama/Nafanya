# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: QualityLog
def monthly_stats(log_entries, start_date='2024-01-01', end_date=None):
    """Вычисляет месячную статистику за указанный диапазон дат."""
    if end_date is None:
        import datetime as dt
        end_date = (dt.datetime.now() + dt.timedelta(days=1)).strftime('%Y-%m-%d')

    stats = {}
    for entry in log_entries:
        date_str = entry.get('date', '')
        year, month, day = map(int, date_str.split('-'))[:3]
        key = f'{year}-{month:02}'
        if key not in stats:
            stats[key] = {'checks': 0, 'defects': 0, 'solutions': 0, 'responsible': set()}

        for k in ('checks', 'defects', 'solutions'):
            if entry.get(k):
                stats[key][k] += 1
        name = entry.get('responsible', '')
        if name:
            stats[key]['responsible'].add(name)

    return sorted(stats.items())


if __name__ == '__main__':
    print(monthly_stats([{'date':'2024-03-15','checks':True,'defects':False,'solutions':True,'responsible':'Алекс'}]))
