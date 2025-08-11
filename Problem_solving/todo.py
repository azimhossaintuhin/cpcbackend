todos= []

while True:
    print("Welcome to the To-Do List App!")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")   
    print("5. Exit")
    choice = int(input("Please enter your choice (1-5): "))
    
    if choice == 1:
        task = input("Enter the task you want to add: ")
        todos.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")
    
    if choice == 2:
        if not todos:
             print("No tasks available.")
        else:
            print(f"Your total tasks: {len(todos)}")
            for index , todo  in enumerate(todos, start=1):
                print("========================\n")
                status = "Completed" if todo["completed"] else "Not Completed"
                print(f"{index}. {todo['task']} - {status}")
                print("========================\n")
    elif choice == 3:
       if not todos:
             print("========================\n")
             print("No tasks available.")
             print("========================\n")
       else:
           task_number = int(input("Enter the task number to mark as completed: "))
           if 1 <= task_number <= len(todos):
               print("========================\n")
               todos[task_number - 1]["completed"] = True
               print(f"Task '{todos[task_number - 1]['task']}' marked as completed!")
               print("========================\n")
           else:
               print("========================\n")
               print("Invalid task number.")
               print("========================\n")
    
    elif choice == 4:
        if not todos:
            print("========================\n")
            print("No tasks available.")
            print("========================\n")
        else:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(todos):
                print("========================\n")
                removed_task = todos.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' removed successfully!")
                print("========================\n")
            else:
                print("========================\n")
                print("Invalid task number.")
                print("========================\n")
    elif choice == 5:
        print("Exiting the To-Do List App. Goodbye!")
        break
