#!/usr/bin/python3

"""
    script that, using REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    export data in the JSON format.
"""

import requests
import json


def get_and_export_users_data():
    sessionReq = requests.Session()

    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = sessionReq.get(users_url)
    users_data = users_response.json()

    all_employees = {}

    for i in users_data:
        u_id = i['id']
        u_name = i['username']

        u_url = f'https://jsonplaceholder.typicode.com/users/{u_id}/todos'

        u_response = sessionReq.get(u_url)
        u_data = u_response.json()

        employee_tasks = []

        for data in u_data:
            employee_tasks.append(
                {
                    "username": u_name,
                    "task": data.get('title'),
                    "completed": data.get('completed')
                }
            )
        all_employees[u_id] = employee_tasks

    file_name = 'todo_all_employees.json'

    with open(file_name, 'w') as f:
        json.dump(all_employees, f)


if __name__ == '__main__':
    get_and_export_users_data()
