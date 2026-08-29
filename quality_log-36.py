# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: QualityLog
def repair_simple(self):
        """Проверка целостности и ремонт простых проблем."""
        if not self.checks:
            print("Ошибка: журнал пуст. Нет данных для проверки.")
            return
        for check in self.checks:
            if check.status == "failed" and check.responsible:
                print(f"Ремонт: проверка '{check.name}' не пройдена. Ответственный: {check.responsible}")
                check.status = "pending"
                check.resolved = False
        if not any(c.status == "failed" for c in self.checks):
            print("Все проверки прошли успешно. Целостность данных подтверждена.")
        else:
            print("Обнаружены проблемы. Рекомендуется перепроверка.")
