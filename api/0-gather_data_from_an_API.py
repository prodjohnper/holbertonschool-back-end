#!/usr/bin/python3
'''
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''

import json
import requests
from sys import argv


def get_data():
    '''
        Function that returns information about his/her TODO list progress
    '''
    # Get the employee ID
    employee_id = int(argv[1])

    # Get the employee name
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url)
    employee = response.json()

    # Get the employee's tasks
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_id)
    response = requests.get(url)
    todos = response.json()

    # Print the employee's tasks
    done_tasks = []
    for task in todos:
        if task.get('completed'):
            done_tasks.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(
        employee.get('name'), len(done_tasks), len(todos)))

    # Print the tasks
    for task in done_tasks:
        print('\t {}'.format(task))


if __name__ == '__main__':
    get_data()
