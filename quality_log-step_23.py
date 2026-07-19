# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: QualityLog
import sys, textwrap
from datetime import datetime

def print_table(data, header, col_widths=None):
    """Выводит данные в компактную консольную таблицу."""
    if not data:
        print("Нет данных")
        return
    if col_widths is None:
        col_widths = [len(h) for h in header]
        for row in data:
            for i, (val, w) in enumerate(zip(row, col_widths)):
                s = str(val)
                if len(s) > w:
                    col_widths[i] = max(col_widths[i], min(len(s), 40))
    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
    print(fmt.format(*header).replace("|", "-|"))
    print("-+-".join("-" * w for w in col_widths))
    for row in data:
        print(fmt.format(*row))

def demo_table():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    header = ["#", "Дата", "Тип", "Статус", "Описание"]
    rows = [
        (1, now, "Проверка", "✅ Успешно", "Температура в норме"),
        (2, now, "Дефект", "⚠️ Неисправность", "Высокий ток утечки"),
        (3, now, "Решение", "🔧 Применено", "Замена конденсатора C1"),
    ]
    print_table(rows, header)

if __name__ == "__main__":
    demo_table()
