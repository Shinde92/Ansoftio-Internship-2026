# Load tasks from file (if exists)


tasks = []

try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    pass  # File not found, start with empty list


while True:
    print("\n--- To-Do Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(i, ".", t)

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(i, ".", t)
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print("Deleted:", removed)
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    # Exit and Save
    elif choice == "4":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved. Exiting application...")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please try again.")
