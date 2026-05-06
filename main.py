import json
import os

FILE_NAME = "tasks.json"
# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)
# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
# Add new task
def add_task(tasks):
    title = input("Enter task: ")
    task = {"title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i+1}. {task['title']} [{status}]")

# Mark task as completed
def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except:
        print("Invalid input!")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except:
        print("Invalid input!")

# Main Menu
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Run program
main()
