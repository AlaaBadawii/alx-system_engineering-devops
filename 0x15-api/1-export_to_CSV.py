#!/usr/bin/python3

"""
A Script that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
exporting data in the CSV format.
"""

import csv
import requests
from sys import argv


def getAndExportToCsv(em_id):
    sessionReq = requests.Session()

    name_url = f'https://jsonplaceholder.typicode.com/users/{em_id}'
    todo_list_url = f'https://jsonplaceholder.typicode.com/users/{em_id}/todos'

    name_res = sessionReq.get(name_url)
    todos_list_res = sessionReq.get(todo_list_url)

    name = name_res.json()['username']
    todos = todos_list_res.json()
    file_name = em_id + '.csv'

    with open(file_name, 'w', newline='') as f:
        write = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in todos:
            write.writerow([em_id, name, i.get('completed'), i.get('title')])


if __name__ == "__main__":
    em_id = argv[1]
    getAndExportToCsv(em_id=em_id)
