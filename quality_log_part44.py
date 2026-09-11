# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: QualityLog
def backup_data_file(filepath: str, backup_dir: str = "backups") -> str:
    """Create a timestamped backup of the data file."""
    import shutil, os, datetime
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(filepath)}_{ts}")
    shutil.copy2(filepath, backup_path)
    return backup_path
