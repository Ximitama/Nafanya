# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: QualityLog
import json
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

class QualityLogEntry:
    def __init__(self, entry_type: str, title: str, description: str, responsible_person: str, status: str = "open", created_at: Optional[datetime] = None):
        self.id = len(QualityLog._entries) + 1 if hasattr(QualityLog, '_entries') else 0
        QualityLog._entries.append(self)
        self.entry_type = entry_type
        self.title = title
        self.description = description
        self.responsible_person = responsible_person
        self.status = status
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "entry_type": self.entry_type,
            "title": self.title,
            "description": self.description,
            "responsible_person": self.responsible_person,
            "status": self.status,
            "created_at": self.created_at.isoformat() if isinstance(self.created_at, datetime) else str(self.created_at)
        }

class QualityLog:
    _entries: List[QualityLogEntry] = []
    
    @staticmethod
    def add_check(title: str, description: str, responsible_person: str):
        return QualityLogEntry("check", title, description, responsible_person, "open")
    
    @staticmethod
    def add_defect(title: str, description: str, responsible_person: str):
        return QualityLogEntry("defect", title, description, responsible_person, "critical")
    
    @staticmethod
    def get_all_entries() -> List[Dict[str, Any]]:
        return [entry.to_dict() for entry in QualityLog._entries]

# Демонстрационные данные
QualityLog.add_check("Проверка сборки", "Валидация всех модулей перед релизом", "Иванов И.И.")
QualityLog.add_defect("Ошибка в модуле auth", "Некорректная обработка токена при экспирации", "Петров П.П.", status="in_progress")
