# === Stage 32: Добавь журнал действий пользователя ===
# Project: QualityLog
class UserActionLog:
    def __init__(self):
        self.actions = []

    def log(self, user, action_type, description, timestamp=None):
        if timestamp is None:
            import datetime; timestamp = datetime.datetime.now()
        record = {
            'user': user,
            'type': action_type,
            'description': description,
            'timestamp': timestamp.isoformat(),
        }
        self.actions.append(record)

    def get_actions(self):
        return self.actions.copy()

    def clear_log(self):
        self.actions.clear()
