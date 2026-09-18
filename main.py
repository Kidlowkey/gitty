import argparse

tasks = []

def add_task(name):
    tasks.append({"name": name, "done": False})
    print(f"Added {name}")

def list_tasks():
    if not tasks:
        print("No tasks yet")
        return

    for i,t in enumerate(tasks, start=1):
        mark = "x" if t["done"] else ""
        print(f"[{mark}] {i}. {t['name']}")

def main():
    parser = argparse.ArgumentParser(prog="taskman")
    sub = parser.add_subparsers(dest="command")

    add_p = sub.add_parser("add", help="Add a task")
    add_p.add_argument("list", help="List tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.name)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
