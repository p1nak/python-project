import os

TODO_FILE = "todo_file.txt"

# it check file is exists or not
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE , "r") as file:
            return file.read().splitlines()
    return[]

# this function save the tasks in file 
def save_tasks(tasks):
    with open(TODO_FILE , "w") as file:
        file.write("\n".join(tasks))

# this function show the tasks 
def show_tasks(tasks):
    if not tasks:
        print("\n No task yet!")
    else:
        print("\n You todo list")
        for i, task in enumerate(tasks , 1):
            status = "[X] " if task.startswith("[X] ") else "[ ] "
            print(f"{i}. {status}{task.replace('[X] ', '')}")

# this function can add the task
def add_task(tasks):
    task = input("Enter new task : ").strip()
    if task:
        tasks.append("[ ]" + task)
        save_tasks(tasks)
        print(f"ADD... {task}")
    else:
        print("task cannot be empty!")

# this function is used for remove task
def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return


    try:
        task_num = int(input("Enter task number to remove : "))
        if 1<= task_num <= len(tasks):
            remove_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"REMOVED : {remove_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Enter valid number plzz!")
        
# this function is used mark done to task
def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
           if not tasks[task_num - 1].startswith("[X] "):
                tasks[task_num - 1] = f"[X] {tasks[task_num - 1]}"
                save_tasks(tasks)
                print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# it's a main function 
def main():
    tasks = load_tasks()

    while True:
        print("\n Option")
        print("\n 1. View Task")
        print("\n 2. Add Task")
        print("\n 3. Remove Task")
        print("\n 4. Marked As Done")
        print("\n 5. Exit")

        choice = input("\n Choose an option (1 - 5) : ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("GoodBye!")
            break
        else:
            print("Enter valid option!")

if __name__ == "__main__":
    main()
