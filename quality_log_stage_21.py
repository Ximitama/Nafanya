# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: QualityLog
from datetime import date, timedelta

class Reminder:
    def __init__(self, title, due_date=None):
        self.title = title
        self.due_date = due_date or date.today() + timedelta(days=1)
        self.is_done = False
        self.created_at = date.today()

    @property
    def days_left(self):
        delta = (self.due_date - date.today()).days
        return max(0, delta) if not self.is_done else 0

    @property
    def status_text(self):
        if self.is_done:
            return "✅ Выполнено"
        elif self.days_left <= 0:
            return f"⚠️ Пропущено ({self.days_left} дн.)"
        else:
            return f"📅 До {self.due_date.strftime('%d.%m')}: {self.days_left} дн."

    def mark_done(self):
        self.is_done = True

    def __str__(self):
        return f"[{self.status_text}] {self.title}"


def add_reminders(reminders, count=3):
    for i in range(count):
        due = date.today() + timedelta(days=(i+1)*7)
        r = Reminder(f"Проверка #{i+1} на неделе", due_date=due)
        reminders.append(r)


def show_reminders(reminders):
    if not reminders:
        print("📋 Напоминаний нет.")
        return
    for i, r in enumerate(reminders, 1):
        print(f"{i}. {r}")
