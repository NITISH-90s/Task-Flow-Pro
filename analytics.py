from datetime import datetime
from matplotlib import pyplot as plt

def count_completed(tasks):

    completed = 0

    for task in tasks:

        if task["status"] == "Completed":

            completed += 1

    return completed


def count_pending(tasks):

    pending = 0

    for task in tasks:

        if task["status"] == "Pending":

            pending += 1

    return pending


def calculate_productivity(tasks):

    total = len(tasks)

    completed = count_completed(tasks)

    if total == 0:

        return 0

    productivity = (completed / total) * 100

    return productivity


def show_dashboard(tasks):

    completed = count_completed(tasks)

    pending = count_pending(tasks)

    productivity = calculate_productivity(tasks)

    current_date = datetime.now().date()

    completed_today = 0

    completed_week = 0


    for task in tasks:

        try:

            due = datetime.strptime(
                task['due_date'],
                "%d-%m-%Y"
            ).date()

            if task['status'] == "Completed":

                # Completed today
                if due == current_date:

                    completed_today += 1

                # Completed this week
                elif (current_date - due).days <= 7:

                    completed_week += 1

        except:

            pass


    print("\n----- DASHBOARD -----")

    print(f"Completed Tasks : {completed}")

    print(f"Pending Tasks   : {pending}")

    print(f"Productivity    : {productivity:.2f}%")

    print(f"Completed Today : {completed_today}")

    print(f"Completed This Week : {completed_week}")

# -------------------------------
    # PRODUCTIVITY PIE CHART
    # -------------------------------

    labels = ["Completed", "Pending"]

    values = [completed, pending]

    if completed != 0 or pending != 0:

        plt.figure(figsize=(6, 6))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )

        plt.title("TASK FLOW PRO - Productivity")

        plt.show()


    # -------------------------------
    # PRIORITY ANALYSIS
    # -------------------------------

    high = 0
    medium = 0
    low = 0

    for task in tasks:

        priority = task["priority"].lower()

        if priority == "high":
            high += 1

        elif priority == "medium":
            medium += 1

        elif priority == "low":
            low += 1

    priorities = ["High", "Medium", "Low"]

    priority_values = [high, medium, low]

    plt.figure(figsize=(6, 5))

    plt.bar(priorities, priority_values)

    plt.title("Priority Analysis")

    plt.xlabel("Priority")

    plt.ylabel("Number of Tasks")

    plt.show()


    # -------------------------------
    # CATEGORY ANALYSIS
    # -------------------------------

    categories = {}

    for task in tasks:

        category = task["category"]

        if category in categories:

            categories[category] += 1

        else:

            categories[category] = 1

    plt.figure(figsize=(7, 5))

    plt.bar(categories.keys(), categories.values())

    plt.title("Category Analysis")

    plt.xlabel("Category")

    plt.ylabel("Tasks")

    plt.show()


    # -------------------------------
    # WEEKLY ANALYSIS
    # -------------------------------

    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    weekly_completed = [0, 0, 0, 0, 0, 0, 0]

    for task in tasks:

        try:

            if task["status"] == "Completed":

                due = datetime.strptime(
                    task["due_date"],
                    "%d-%m-%Y"
                )

                day_index = due.weekday()

                weekly_completed[day_index] += 1

        except:

            pass

    plt.figure(figsize=(8, 5))

    plt.plot(week_days, weekly_completed, marker="o")

    plt.title("Weekly Analysis")

    plt.xlabel("Days")

    plt.ylabel("Completed Tasks")

    plt.show()


    # -------------------------------
    # STATUS ANALYSIS
    # -------------------------------

    status_labels = ["Completed", "Pending"]

    status_values = [completed, pending]

    plt.figure(figsize=(6, 5))

    plt.bar(status_labels, status_values)

    plt.title("Status Analysis")

    plt.xlabel("Status")

    plt.ylabel("Tasks")

    plt.show()