import argparse
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE) as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks, name):
    tasks.append({"name": name, "done": False})
    save_tasks(tasks)
    print(f"Added {name}")

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['name']}")
    else:
        print("Invalid task number.")

def list_tasks(tasks):
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
    add_p.add_argument("name", help="Task name")
    sub.add_parser("list", help="List tasks")
    delete_p = sub.add_parser("delete", help="Delete a task")
    delete_p.add_argument("index", type=int, help="Task number")

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == "add":
        add_task(tasks, args.name)
    elif args.command == "list":
        list_tasks(tasks)
    elif args.command == "delete":
        delete_task(tasks, args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
