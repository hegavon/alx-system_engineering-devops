#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    resp = requests.get(url)
    users = resp.json()

    all_tasks = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        resp = requests.get(url)
        tasks = resp.json()

        user_tasks = []
        for task in tasks:
            task_completed_status = task.get('completed')
            task_title = task.get('title')
            user_tasks.append({
                "task": task_title,
                "completed": task_completed_status,
                "username": username
            })

        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f)
