# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: QualityLog
class ActionRollback:
    def __init__(self):
        self._history = []
        self._current = None

    def push(self, state):
        self._current = state
        self._history.append(self._current)

    def rollback(self):
        if len(self._history) <= 1:
            return None
        previous = self._history[-2]
        self._history.pop()
        return previous
