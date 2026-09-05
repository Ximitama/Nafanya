# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: QualityLog
import argparse

def main():
    parser = argparse.ArgumentParser(description="QualityLog CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_check = sub.add_parser("check", help="Run quality checks")
    p_check.add_argument("--file", default="quality_log.txt")

    p_defect = sub.add_parser("defect", help="Add a defect")
    p_defect.add_argument("--title", required=True)
    p_defect.add_argument("--assignee", required=True)

    p_solve = sub.add_parser("solve", help="Mark defect as solved")
    p_solve.add_argument("--id", required=True)

    p_report = sub.add_parser("report", help="Generate report")
    p_report.add_argument("--file", default="quality_log.txt")
    p_report.add_argument("--output", default="report.txt")

    args = parser.parse_args()

    if args.command == "check":
        with open(args.file, "r") as f:
            print(f.read())
    elif args.command == "defect":
        with open(args.file, "a") as f:
            f.write(f"\n[DEFECT]\nTitle: {args.title}\nAssignee: {args.assignee}\nStatus: open\n")
    elif args.command == "solve":
        with open(args.file, "r") as f:
            content = f.read()
        new_content = content.replace(f"Status: open\n", f"Status: solved\n", 1)
        with open(args.file, "w") as f:
            f.write(new_content)
        print(f"Defect {args.id} marked as solved.")
    elif args.command == "report":
        with open(args.file, "r") as f:
            content = f.read()
        defects = content.count("[DEFECT]")
        solved = content.count("Status: solved")
        with open(args.output, "w") as f:
            f.write(f"Total defects: {defects}\nSolved: {solved}\nOpen: {defects - solved}\n")
        print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
