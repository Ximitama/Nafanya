# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: QualityLog
import json, os
from pathlib import Path

PROFILES_FILE = Path(__file__).parent / "profiles.json"

def load_profiles() -> list[dict]:
    if PROFILES_FILE.exists():
        with open(PROFILES_FILE) as f:
            return [json.loads(line) for line in f]
    return []

def save_profiles(profiles: list[dict]) -> None:
    with open(PROFILES_FILE, "w") as f:
        for p in profiles:
            json.dump(p, f)
            f.write("\n")

def add_profile(name: str, email: str = "", role: str = "user", level: int = 1) -> dict:
    profile = {"name": name, "email": email, "role": role, "level": level}
    profiles = load_profiles()
    for p in profiles:
        if p["name"] == name or p["email"] == email:
            raise ValueError(f"Profile already exists: {name}")
    save_profiles(profiles + [profile])
    return profile

def get_profile(name_or_email: str) -> dict | None:
    for p in load_profiles():
        if p["name"] == name_or_email or p["email"] == name_or_email:
            return p
    return None

def delete_profile(name_or_email: str) -> bool:
    profiles = load_profiles()
    remaining = [p for p in profiles if p["name"] != name_or_email and p["email"] != name_or_email]
    if len(remaining) == len(profiles):
        return False
    save_profiles(remaining)
    return True

def list_profiles() -> list[dict]:
    return load_profiles()
