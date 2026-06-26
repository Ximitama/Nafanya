# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: QualityLog
def main():
    print("QualityLog v1 — Меню действий")
    while True:
        try:
            cmd = input("\nВыберите действие (1-4 или 'q' для выхода): ").strip().lower()
            if cmd == "q": break
            elif cmd in ("1", "2", "3", "4"): print(f"Команда {cmd} выполнена.")
            else: print("Неизвестная команда.")
        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break

if __name__ == "__main__": main()
