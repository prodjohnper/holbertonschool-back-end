#!/usr/bin/python3
'''
    Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress and
    export it to JSON.
'''
import json
import requests


def get_employee(id=None):
    '''
        Function that, using this REST API, for a given employee ID,
        returns information about his/her TODO list progress and export
        it to JSON.
    '''
    # Get the users and todos from the API
    api_users_url = 'https://jsonplaceholder.typicode.com/users'
    api_todos_url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(api_users_url)
    users = response.json()

    # Get the user ids
    user_ids = []
    for user in users:
        user_ids.append(user["id"])

    # Create a dictionary with the user id as key and a list of tasks as value
    json_dict = {}

    # Get the tasks for each user
    for employee_id in user_ids:
        api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        response = requests.get(api_url)

        # Get the employee name
        employee_name = response.json()["username"]

        # Get the tasks for the employee
        api_url2 = (
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        response = requests.get(api_url2)

        # Get the tasks
        tasks = response.json()

        # Add the tasks to the dictionary
        json_dict[employee_id] = []
        for task in tasks:
            json_format = {
                "username": employee_name,
                "task": task["title"],
                "completed": task["completed"]
            }

            # Append the task to the list
            json_dict[employee_id].append(json_format)

    # Export the dictionary to a json file
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(json_dict, json_file)


if __name__ == "__main__":
    get_employee()
