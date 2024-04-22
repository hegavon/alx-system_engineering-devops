#!/usr/bin/python3
"""Gathers employee data from API and exports it in JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    all_employee_data = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        user_tasks = []
        for todo in todos:
            if todo["userId"] == user_id:
                user_tasks.append({
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"]
                })

        all_employee_data[user_id] = user_tasks

    output_file = "todo_all_employees.json"

    with open(output_file, "w") as file:
        json.dump(all_employee_data, file)

    print("Data exported to {} successfully.".format(output_file))
