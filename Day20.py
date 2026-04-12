# Create empty task list
tasks = []

while True:
    print("\n--- To-Do Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

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

    # Exit
    elif choice == "3":
        print("Exiting application...")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please try again.")
