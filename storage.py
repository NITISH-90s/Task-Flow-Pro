import json

def save_tasks(tasks):

    with open("tasks.json", "w") as file:

        json.dump(tasks, file)

def load_tasks():

    try:

        with open("tasks.json", "r") as file:

            tasks = json.load(file)

            return tasks

    except:

        return []

import csv

def export_csv(tasks):

    with open("tasks.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Title",
            "Description",
            "Priority",
            "Status",
            "Due Date"
        ])

        for task in tasks:

            writer.writerow([
                task["id"],
                task["title"],
                task["description"],
                task["priority"],
                task["status"],
                task["due_date"]
            ])

    print("CSV exported successfully")
