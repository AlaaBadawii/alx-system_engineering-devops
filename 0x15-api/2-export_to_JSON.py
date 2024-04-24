#!/usr/bin/python3
"""
A Script that, using a REST API, for a given user ID, returns
information about his/her TODO list progress and exports it in JSON format.
"""

import json
import requests
from sys import argv


def get_and_export_to_json(user_id):
    session_req = requests.Session()

    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    user_response = session_req.get(user_url)
    todos_response = session_req.get(todos_url)

    user_data = user_response.json()
    tasks_data = todos_response.json()

    all_tasks = []
    for task in tasks_data:
        all_tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_data.get('username')
        })

    data = {user_id: all_tasks}

    file_name = f'{user_id}.json'

    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    user_id = argv[1]
    get_and_export_to_json(user_id)
