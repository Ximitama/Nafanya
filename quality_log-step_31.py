# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: QualityLog
def switch_profile(new_name):
    """Переключить активный профиль: проверить, что пользователь существует."""
    if new_name not in profiles:
        print(f"Профиль '{new_name}' не найден.")
        return False
    active = profiles[new_name]
    print(f"Активный профиль изменён на: {active.name}")
    return True

def list_profiles():
    """Вывести список всех зарегистрированных профилей."""
    for name, profile in profiles.items():
        status_marker = " [активен]" if active is not None and active.name == profile.name else ""
        print(f"  {name}: {profile.role}{status_marker}")
