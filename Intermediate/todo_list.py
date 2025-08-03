import json
import os
from datetime import datetime

TODO_FILE = "todo_file.txt"

# it check file is exists or not
def load_tasks():
    try:
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, "r") as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        print("Warning: Corrupted task file. Starting fresh.")
        return []

# this function save the tasks in file 
def save_tasks(tasks):
    with open(TODO_FILE , "w") as file:
        json.dump(tasks, file, indent=4 )

# this function show the tasks 
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet! Add one to get started.")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task.get("done", False) else " "
        due_date = task.get("due_date", "No deadline")
        print(f"{i}. [{status}] {task['task']} (Due: {due_date})")

# this function can add the task
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if not task:
        print("Error: Task cannot be empty!")
        return
    
    due_date = input("Due date (YYYY-MM-DD, optional): ").strip()
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format! Use YYYY-MM-DD.")
            return
    
    tasks.append({
        "task": task,
        "due_date": due_date if due_date else "No deadline",
        "done": False  # Default to not completed
    })
    save_tasks(tasks)
    print(f"✓ Added: '{task}'")

# this function is used for remove task
def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"✗ Removed: '{removed['task']}'")
        else:
            print("Error: Invalid task number!")
    except ValueError:
        print("Error: Please enter a valid number!")
        
# this function is used mark done to task
def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to toggle status: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            task["done"] = not task["done"]  # Toggle status
            save_tasks(tasks)
            status = "DONE" if task["done"] else "PENDING"
            print(f"✓ Updated: '{task['task']}' → {status}")
        else:
            print("Error: Invalid task number!")
    except ValueError:
        print("Error: Please enter a valid number!")

# it's a main function 
def main():
    tasks = load_tasks()
    
    while True:
        print("\n" + "="*30)
        print(" TO-DO LIST MANAGER ".center(30, "♥"))
        print("="*30)
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Toggle Done Status")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("\nGoodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()
