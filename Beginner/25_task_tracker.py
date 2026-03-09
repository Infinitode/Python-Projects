# 25. Task Tracker (To-Do List)

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(index):
    try:
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' deleted.")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\n=== Task Tracker ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            task = input("Enter Task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            if tasks:
                try:
                    index = int(input("Enter task number to delete: "))
                    delete_task(index)
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()
