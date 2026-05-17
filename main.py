from task_manager import*
from storage import*
from analytics import*

print("TaskFlow Pro Started")
tasks = load_tasks()

check_reminders(tasks)

while True:
        
        print("1. Add Task")
        print("2. Edit/Update Task")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Show Dashboard")
        print("7. Search Task")
        print("8. Filter Task")
        print("9. Export CSV")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
          add_task(tasks)
          save_tasks(tasks)

        elif choice == "2":
         edit_task(tasks)
         save_tasks(tasks)

        elif choice == "3":
          view_tasks(tasks)

        elif choice == "4":
          delete_task(tasks)
          save_tasks(tasks)

        elif choice == "5":
          complete_task(tasks)
          save_tasks(tasks)

        elif choice == "6":
          show_dashboard(tasks)

        elif choice == "7":
         search_task(tasks)

        elif choice == "8":
         filter_tasks(tasks)

        elif choice == "9":
         export_csv(tasks)

        elif choice == "10":
          break

