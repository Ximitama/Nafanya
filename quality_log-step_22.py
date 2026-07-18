# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: QualityLog
def check_overdue_reminders(self):
        """Проверяет просроченные напоминания (проверки с deadline, у которых статус не 'passed' и текущая дата > deadline)."""
        overdue = []
        today = datetime.date.today()
        for check in self.checks:
            if hasattr(check, 'deadline') and check.deadline and check.status != 'passed':
                if today > check.deadline:
                    overdue.append({
                        'id': check.id,
                        'name': check.name,
                        'deadline': str(check.deadline),
                        'status': check.status,
                        'assigned_to': getattr(check, 'assigned_to', None) or '',
                    })
        self._log(f'Просрочено {len(overdue)} напоминание{"" if len(overdue)==1 else "я"}: ', overdue)
