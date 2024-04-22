#!/usr/bin/python3
"""Gathers employee ID information from database."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py [employee_id]")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    user_response = requests.get(base_url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print("Error: Employee not found.")
        sys.exit(1)

    todos_response = requests.get(
        base_url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error: Unable to retrieve employee's tasks.")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed_tasks), len(todos_data)))

    if completed_tasks:
        for task in completed_tasks:
            print("\t{}".format(task.get("title")))
