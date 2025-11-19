import os

TASK_FILE = "task.txt"
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    print("\n===== YOUR TASKS =====")
    if not tasks:
        print("No tasks yet.")
    else:
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    print("======================\n")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Select task number to update: "))
        new_task = input("Enter new task description: ")
        tasks[number - 1] = new_task
        save_tasks(tasks)
        print("Task updated.")
    except:
        print("Invalid selection!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Select task number to delete: "))
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except:
        print("Invalid selection!")

def menu():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        print("=============================")

        choice = input("Choose option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if _name_ == "_main_":
    menu()

