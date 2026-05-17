from colorama import Fore, init, Style
from datetime import datetime
from plyer import notification

init()

def check_reminders(tasks):

    current_date = datetime.now().date()

    overdue_count = 0
    today_count = 0
    tomorrow_count = 0

    overdue_titles = []
    today_titles = []
    tomorrow_titles = []

    for task in tasks:

        try:

            due = datetime.strptime(
                task['due_date'],
                "%d-%m-%Y"
            ).date()

            if task['status'] != "Completed":

                # OVERDUE
                if due < current_date:

                    overdue_count += 1
                    overdue_titles.append(task['title'])

                    print(
                        Fore.RED +
                        f"OVERDUE: {task['title']}" +
                        Style.RESET_ALL
                    )

                # TODAY
                elif due == current_date:

                    today_count += 1
                    today_titles.append(task['title'])

                    print(
                        Fore.YELLOW +
                        f"DUE TODAY: {task['title']}" +
                        Style.RESET_ALL
                    )

                # TOMORROW
                elif (due - current_date).days == 1:

                    tomorrow_count += 1
                    tomorrow_titles.append(task['title'])

                    print(
                        Fore.CYAN +
                        f"DUE TOMORROW: {task['title']}" +
                        Style.RESET_ALL
                    )

        except:
            pass

    # POPUP NOTIFICATIONS

    if overdue_count > 0:

        notification.notify(
            title="OVERDUE TASKS",
            message=f"{overdue_count} overdue task(s)\n" +
            ", ".join(overdue_titles),
            timeout=10
        )

    if today_count > 0:

        notification.notify(
            title="TASKS DUE TODAY",
            message=f"{today_count} task(s) due today\n" +
            ", ".join(today_titles),
            timeout=10
        )

    if tomorrow_count > 0:

        notification.notify(
            title="TASKS DUE TOMORROW",
            message=f"{tomorrow_count} task(s) due tomorrow\n" +
            ", ".join(tomorrow_titles),
            timeout=10
        )

def add_task(tasks):

    title = input("Enter title: ").strip()

    if not title:
     print(Fore.RED + "Title cannot be empty" + Style.RESET_ALL)
     return


    description = input("Enter description: ").strip()

    if not description:
      print(Fore.RED + "Description cannot be empty" + Style.RESET_ALL)
      return


    priority = input("Enter priority: ").strip().capitalize()

    if priority not in ["High", "Medium", "Low"]:
      print(Fore.RED + "Priority must be High, Medium, or Low" + Style.RESET_ALL)
      return


    due_date = input("Enter due date: ").strip()

    if not due_date:
     print(Fore.RED + "Due date cannot be empty" + Style.RESET_ALL)
     return


    category = input("Enter category: ").strip()

    if not category:
      print(Fore.RED + "Category cannot be empty" + Style.RESET_ALL)
      return

    task = {
    "id": len(tasks) + 1,
    "title": title,
    "description": description,
    "priority": priority,
    "status": "Pending",
    "due_date": due_date,
    "category": category
}

    tasks.append(task)

    print(Fore.CYAN + "Task added successfully"+ Style.RESET_ALL)

def edit_task(tasks):

    try:
     task_id = int(input("Enter task ID to edit: "))
    except ValueError:
     print(Fore.RED + "Invalid input")
     return

    for task in tasks:

        if task["id"] == task_id:

            print("Leave blank to keep old value")

            new_title = input("New title: ")
            new_description = input("New description: ")
            new_priority = input("New priority: ")
            new_due_date = input("New due date: ")
            new_category = input("New category: ")

            if new_title:
                task["title"] = new_title

            if new_description:
                task["description"] = new_description

            if new_priority:
                task["priority"] = new_priority

            if new_due_date:
                task["due_date"] = new_due_date

            if new_category:
                task["category"] = new_category

            print(Fore.CYAN + "Task updated successfully"+ Style.RESET_ALL)

            break

def view_tasks(tasks):

    current_date = datetime.now().date()

    for task in tasks:
     
     try:
        due = datetime.strptime(task['due_date'], "%d-%m-%Y").date()

        if due < current_date and task['status'] != "Completed":
            print(Fore.RED + "OVERDUE TASK")

     except:
        pass        

    if task["priority"] == "High":

      print(Fore.RED + f"""
ID: {task['id']}
Title: {task['title']}
Description: {task['description']}
Priority: {task['priority']}
Status: {task['status']}
Due Date: {task['due_date']}
Category: {task['category']}
-------------------------
"""+ Style.RESET_ALL)

    elif task["priority"] == "Medium":

      print(Fore.YELLOW + f"""
ID: {task['id']}
Title: {task['title']}
Description: {task['description']}
Priority: {task['priority']}
Status: {task['status']}
Due Date: {task['due_date']}
Category: {task['category']}
-------------------------
"""+ Style.RESET_ALL)

    else:

     print(Fore.BLUE + f"""
ID: {task['id']}
Title: {task['title']}
Description: {task['description']}
Priority: {task['priority']}
Status: {task['status']}
Due Date: {task['due_date']}
Category: {task['category']}
-------------------------
"""+ Style.RESET_ALL)

def delete_task(tasks):

      try:
       task_id = int(input("Enter task ID to delete: "))
      except ValueError:
       print(Fore.RED + "Invalid input")
       return

      for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            print(Fore.LIGHTRED_EX +"Task deleted successfully"+ Style.RESET_ALL)

            break

def complete_task(tasks):

    try:
      task_id = int(input("Enter task ID to complete: "))
    except ValueError:
      print(Fore.RED + "Invalid input")
      return

    for task in tasks:

        if task["id"] == task_id:

            task["status"] = "Completed"

            print(Fore.GREEN +"Task marked as completed"+ Style.RESET_ALL)

            break

def search_task(tasks):

    keyword = input("Enter keyword to search: ").lower()

    found = False

    for task in tasks:

        if (
    keyword in task["title"].lower()
    or keyword in task["description"].lower()
    or keyword in task["priority"].lower()
    or keyword in task["status"].lower()
    or keyword in task["category"].lower()
    or keyword in task["due_date"].lower()
):

            print(Fore.MAGENTA + f"""

ID: {task['id']}
Title: {task['title']}
Description: {task['description']}
Priority: {task['priority']}
Status: {task['status']}
Due Date: {task['due_date']}
Category: {task['category']}
"""+ Style.RESET_ALL)

            found = True

    if not found:
           print(Fore.RED + "No task found")

# FILTER BY PRIORITY
def filter_by_priority(tasks, priority):

    filtered = []

    for task in tasks:

        if task["priority"].lower() == priority.lower():

            filtered.append(task)

    return filtered



# FILTER BY STATUS
def filter_by_status(tasks, status):

    filtered = []

    for task in tasks:

        if task["status"].lower() == status.lower():

            filtered.append(task)

    return filtered



# FILTER BY CATEGORY
def filter_by_category(tasks, category):

    filtered = []

    for task in tasks:

        if task["category"].lower() == category.lower():

            filtered.append(task)

    return filtered



# FILTER BY EXACT DUE DATE
def filter_by_due_date(tasks, due_date):

    filtered = []

    for task in tasks:

        if task["due_date"] == due_date:

            filtered.append(task)

    return filtered



# FILTER TASKS DUE TODAY
def filter_due_today(tasks):

    today = datetime.now().date()

    filtered = []

    for task in tasks:

        try:

            due = datetime.strptime(
                task["due_date"],
                "%d-%m-%Y"
            ).date()

            if due == today:

                filtered.append(task)

        except:

            pass

    return filtered



# FILTER OVERDUE TASKS
def filter_overdue(tasks):

    today = datetime.now().date()

    filtered = []

    for task in tasks:

        try:

            due = datetime.strptime(
                task["due_date"],
                "%d-%m-%Y"
            ).date()

            if due < today and task["status"] != "Completed":

                filtered.append(task)

        except:

            pass

    return filtered



# SHOW FILTERED TASKS
def show_filtered_tasks(task_list):

    if len(task_list) == 0:

        print("\nNo matching tasks found.")

        return


    for task in task_list:

        print("\n---------------------------")

        print(f"ID         : {task['id']}")

        print(f"Title      : {task['title']}")

        print(f"Description: {task['description']}")

        print(f"Priority   : {task['priority']}")

        print(f"Status     : {task['status']}")

        print(f"Due Date   : {task['due_date']}")

        print(f"Category   : {task['category']}")

# MAIN FILTER MENU
def filter_tasks(tasks):

    while True:

        print("\n===== FILTER TASKS =====")

        print("1. Filter by Priority")

        print("2. Filter by Status")

        print("3. Filter by Category")

        print("4. Filter by Due Date")

        print("5. Tasks Due Today")

        print("6. Overdue Tasks")

        print("7. Exit Filters")


        choice = input("\nEnter choice: ")


        # PRIORITY
        if choice == "1":

            priority = input(
                "Enter priority (High/Medium/Low): "
            )

            result = filter_by_priority(
                tasks,
                priority
            )

            show_filtered_tasks(result)


        # STATUS
        elif choice == "2":

            status = input(
                "Enter status (Pending/Completed): "
            )

            result = filter_by_status(
                tasks,
                status
            )

            show_filtered_tasks(result)


        # CATEGORY
        elif choice == "3":

            category = input(
                "Enter category: "
            )

            result = filter_by_category(
                tasks,
                category
            )

            show_filtered_tasks(result)


        # DUE DATE
        elif choice == "4":

            due_date = input(
                "Enter due date (DD-MM-YYYY): "
            )

            result = filter_by_due_date(
                tasks,
                due_date
            )

            show_filtered_tasks(result)


        # DUE TODAY
        elif choice == "5":

            result = filter_due_today(tasks)

            show_filtered_tasks(result)


        # OVERDUE
        elif choice == "6":

            result = filter_overdue(tasks)

            show_filtered_tasks(result)


        # EXIT
        elif choice == "7":

            break


        else:

            print("Invalid choice.")

    


