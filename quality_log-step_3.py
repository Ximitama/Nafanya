# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: QualityLog
class QualityLog:
    def __init__(self):
        self._checks = []
        self._defects = []
        self._solutions = []
        self._owners = {}

    def add_check(self, name, criteria, owner_id=None):
        record = {'id': len(self._checks) + 1, 'name': name, 'criteria': criteria, 'owner_id': owner_id}
        if owner_id:
            self._owners[owner_id] = record['name']
        self._checks.append(record)

    def add_defect(self, check_name, description, severity='medium', status='open'):
        for c in self._checks:
            if c['name'] == check_name:
                defect = {'id': len(self._defects) + 1, 'check_id': c['id'], 'description': description, 'severity': severity, 'status': status}
                self._defects.append(defect)
                return defect['id']
        raise ValueError(f"Check '{check_name}' not found")

    def add_solution(self, defect_id, resolution, verified_by=None):
        for d in self._defects:
            if d['id'] == defect_id:
                solution = {'id': len(self._solutions) + 1, 'defect_id': defect_id, 'resolution': resolution, 'verified_by': verified_by}
                self._solutions.append(solution)
                return solution['id']
        raise ValueError(f"Defect '{defect_id}' not found")

    def get_status_summary(self):
        open_defects = [d for d in self._defects if d['status'] == 'open']
        resolved_count = len([s for s in self._solutions])
        return {'total_checks': len(self._checks), 'open_defects': len(open_defects), 'resolved_issues': resolved_count}
