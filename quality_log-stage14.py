# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: QualityLog
def generate_summary(records):
    if not records: return "Нет данных для сводки."
    checks = [r for r in records if isinstance(r, CheckRecord)]
    defects = [r for r in records if isinstance(r, DefectRecord)]
    solutions = [r for r in records if isinstance(r, SolutionRecord)]
    
    total_checks = len(checks)
    passed_checks = sum(1 for c in checks if c.status == "passed")
    failed_checks = total_checks - passed_checks
    
    active_defects = sum(1 for d in defects if d.status != "resolved")
    resolved_defects = len(defects) - active_defects
    
    open_solutions = sum(1 for s in solutions if s.status == "open")
    
    summary_lines = [
        f"Сводка по журналу контроля качества",
        "=" * 40,
        "",
        "Проверки:",
        f"  Всего: {total_checks}",
        f"  Успешно: {passed_checks}",
        f"  Не пройдено: {failed_checks}",
        "",
        "Дефекты:",
        f"  Активных: {active_defects}",
        f"  Решено: {resolved_defects}",
        "",
        "Решения:",
        f"  Открытых: {open_solutions}",
        "",
        "=" * 40,
    ]
    
    if failed_checks > 0 or active_defects > 0:
        summary_lines.append("Внимание! Требуется внимание.")
        
    return "\n".join(summary_lines)
