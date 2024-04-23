#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID, returns information about,
his/her TODO list progress.
"""

import requests
import sys


def get_employee_info(em_id):
    """
        fun to retrieve info about the employee
    """

    url = f'https://jsonplaceholder.typicode.com/todos?userId={em_id}'
    response = requests.get(url)

    if response.status_code == 200:
        todo_list = response.json()

        done_tasks = [
            done for done in todo_list if done['completed']
        ]

        total_tasks = len(todo_list)
        num_of_done_tasks = len(done_tasks)

        user_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{em_id}'
        )

        if user_response.status_code == 200:
            user_data = user_response.json()
            username = user_data['username']

        print(f'Employee {username} is done with tasks \
                ({num_of_done_tasks}/{total_tasks}):')
        for todo in done_tasks:
            print(f'\t{todo["title"]}')


if __name__ == "__main__":
    em_id = sys.argv[1]
    get_employee_info(em_id)
