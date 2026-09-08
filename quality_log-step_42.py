# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: QualityLog
import sys

try:
    _use_color = sys.stdout.isatty()
except Exception:
    _use_color = False

def _color(code, text):
    return f"\033[{code}m{text}\033[0m"

def _red(t): return _color("31", t)
def _green(t): return _color("32", t)
def _yellow(t): return _color("33", t)
def _cyan(t): return _color("36", t)
def _bold(t): return _color("1", t)

def _print_pass(msg):
    print(_green(_bold("✓ ")), _green(msg))

def _print_fail(msg):
    print(_red(_bold("✗ ")), _red(msg))

def _print_warn(msg):
    print(_yellow(_bold("⚠ ")), _yellow(msg))

def _print_info(msg):
    print(_cyan(msg))

def _print_header(title):
    print(_bold(_cyan(f"\n═══ {title} ═══\n")))
