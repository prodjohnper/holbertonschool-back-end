#!/usr/bin/python3
'''
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress and exports
    it to JSON format.
'''

import json
import requests
from sys import argv


def get_all_users():
    '''
        Function that returns information about all users
    '''
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()
    return users


def get_tasks(employee_id):
    '''
        Function that returns tasks for a given employee ID
    '''
    # Get the employee name
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url)
    employee = response.json()

    # Get the employee's tasks
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_id)
    response = requests.get(url)
    todos = response.json()

    return employee, todos


def get_data():
    '''
        Function that returns information about his/her TODO list progress
    '''
    # Check if employee ID is provided
    if len(argv) == 1:
        # Fetch data for all users
        users = get_all_users()
        all_employees_tasks = {}
        for user in users:
            employee_id = user['id']
            employee, tasks = get_tasks(employee_id)
            employee_tasks = []
            for task in tasks:
                task_info = {
                    "username": employee.get('name'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                employee_tasks.append(task_info)
            all_employees_tasks[employee_id] = employee_tasks

    # If employee ID is provided
    elif len(argv) == 2:
        # Get the employee ID
        employee_id = int(argv[1])
        employee, tasks = get_tasks(employee_id)
        all_employees_tasks = {employee_id: []}
        for task in tasks:
            task_info = {
                "username": employee.get('name'),
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            all_employees_tasks[employee_id].append(task_info)

    # Write the data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employees_tasks, json_file)


if __name__ == '__main__':
    get_data()
