import json
import os
from datetime import datetime

TASK_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task_desc):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": task_desc,
        "status": "Pending",
        "timestamp": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.")
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']}")
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "Done"
            break
    save_tasks(tasks)
    print("✔️ Task marked as done.")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print("🗑️ Task deleted.")
def menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter task: ")
            add_task(desc)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to complete: "))
            complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()
