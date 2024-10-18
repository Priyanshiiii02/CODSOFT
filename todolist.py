# To-Do List Program
todo_list = []

# Function to add a new task
def add_task(task):
    todo_list.append({"Task": task, "Completed": False})
    print(f"Task '{task}' added successfully!")

# Function to view all tasks
def view_tasks():
    if todo_list:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            status = "Completed" if task["Completed"] else "Not Completed"
            print(f"{idx}. {task['Task']} - {status}")
    else:
        print("\nYour To-Do List is empty!")

# Function to mark a task as completed
def mark_task_completed(task_number):
    if 0 < task_number <= len(todo_list):
        todo_list[task_number - 1]["Completed"] = True
        print(f"Task '{todo_list[task_number - 1]['Task']}' marked as completed!")
    else:
        print("Invalid task number!")

# Function to delete a task
def delete_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task['Task']}' deleted successfully!")
    else:
        print("Invalid task number!")

# Main program loop
def todo_list_menu():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                mark_task_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid option! Please choose a valid number.")

# Run the To-Do List
todo_list_menu()
