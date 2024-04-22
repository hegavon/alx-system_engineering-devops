#!/usr/bin/python3
"""
Gathers employee data from API
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    """Retrieve employee data from the API."""
    employee_response = requests.get(f"{REST_API}/users/{employee_id}")
    employee_info = employee_response.json()
    tasks_response = requests.get(f"{REST_API}/todos?userId={employee_id}")
    tasks_info = tasks_response.json()
    return employee_info, tasks_info


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py [employee_id]")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not re.match(r'\d+', employee_id):
        print("Invalid employee ID. Please provide a valid integer ID.")
        sys.exit(1)

    employee_id = int(employee_id)
    employee_data, tasks_data = get_employee_data(employee_id)
    completed_tasks = [task for task in tasks_data if task.get("completed")]

    print(f"Employee {employee_data.get('name')} is done with tasks"
          f"({len(completed_tasks)}/{len(tasks_data)}):")

    if completed_tasks:
        for task in completed_tasks:
            print(f"\t{task.get('title')}")
