# === Stage 45: Добавь восстановление из резервной копии ===
# Project: QualityLog
import copy, json, os, shutil

def restore_from_backup(backup_path, log_dir="."):
    """Восстанавливает журнал из резервной копии, если файл не повреждён."""
    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f"Резервная копия не найдена: {backup_path}")
    if not backup_path.endswith('.json'):
        raise ValueError("Резервная копия должна иметь расширение .json")
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise ValueError("Резервная копия повреждена или невалидна")
    backup_dir = os.path.dirname(backup_path)
    base = os.path.basename(backup_path)
    for item in data:
        if isinstance(item, dict) and 'type' in item:
            item['id'] = item.get('id', base)
            item['created'] = item.get('created', 'unknown')
            item['status'] = item.get('status', 'unknown')
            item['assignee'] = item.get('assignee', 'unknown')
        elif isinstance(item, dict) and 'check' in item:
            item['id'] = item.get('id', base)
            item['created'] = item.get('created', 'unknown')
            item['status'] = item.get('status', 'unknown')
            item['assignee'] = item.get('assignee', 'unknown')
        elif isinstance(item, dict) and 'defect' in item:
            item['id'] = item.get('id', base)
            item['created'] = item.get('created', 'unknown')
            item['status'] = item.get('status', 'unknown')
            item['assignee'] = item.get('assignee', 'unknown')
        elif isinstance(item, dict) and 'solution' in item:
            item['id'] = item.get('id', base)
            item['created'] = item.get('created', 'unknown')
            item['status'] = item.get('status', 'unknown')
            item['assignee'] = item.get('assignee', 'unknown')
        elif isinstance(item, dict) and 'responsible' in item:
            item['id'] = item.get('id', base)
            item['created'] = item.get('created', 'unknown')
            item['status'] = item.get('status', 'unknown')
            item['assignee'] = item.get('assignee', 'unknown')
        else:
            continue
    return copy.deepcopy(data)
