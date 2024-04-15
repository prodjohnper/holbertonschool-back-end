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
        Function that returns information about his/her TODO
        list progress and export data in the JSON format.
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

    # Export the data to a JSON file
    data = {}
    data[employee_id] = []

    # Add the tasks to the data
    for task in todos:
        data[employee_id].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': employee.get('username')
        })

    with open('{}.json'.format(employee_id), 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    get_data()
