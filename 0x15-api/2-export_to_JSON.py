#!/usr/bin/python3
"""
A Script that, uses a REST API, for a given userployee ID, returns
information about his/her TODO list progress
extend Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv


def getAndExportToJson(user_id):
    sessionReq = requests.Session()

    name_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    name_response = sessionReq.get(name_url)
    todos_response = sessionReq.get(todo_url)

    name = name_response.json()['username']
    todos = todos_response.json()

    all_tasks = []
    data = {}

    for task in todos:
        all_tasks.append(
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": name
            }
        )
    data = {user_id:all_tasks}
    file_name = user_id + '.json'

    with open(file=file_name, mode='w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    user_id = argv[1]
    getAndExportToJson(user_id=user_id)
