#!/usr/bin/python3
"""
    script that, using REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

import requests
from sys import argv


def get_em_todo_list(em_id):
    sessionReq = requests.Session()

    user_url = f'https://jsonplaceholder.typicode.com/users/{em_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={em_id}'

    user_response = sessionReq.get(user_url)
    todos_response = sessionReq.get(todos_url)

    user_data = user_response.json()
    user_name = user_data['name']

    todos_data = todos_response.json()

    done_tasks = [task for task in todos_data if task['completed']]
    num_of_done_tasks = len(done_tasks)
    total_num_of_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".
          format(user_name, num_of_done_tasks, total_num_of_tasks))

    for task in done_tasks:
        print(f'\t{task["title"]}')


if __name__ == "__main__":
    em_id = argv[1]
    get_em_todo_list(em_id)