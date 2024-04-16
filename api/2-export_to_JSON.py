#!/usr/bin/python3
'''
    Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress and
    export it to JSON.
'''

import json
import requests
from sys import argv


def get_employee(id=None):
    '''
        Function that, using this REST API, for a given employee ID,
        returns information about his/her TODO list progress and export
        it to JSON.
    '''
    # Check if the argument is a number
    if len(argv) > 1:
        try:
            id = int(argv[1])
        except ValueError:
            pass
            return

    # Check if the argument is a number
    if isinstance(id, int):
        user = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
        to_dos = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/?userId={id}"
        )

        # Check if the request was successful
        if to_dos.status_code == 200 and user.status_code == 200:
            user = json.loads(user.text)
            to_dos = json.loads(to_dos.text)

            # Count total tasks and completed tasks
            total_tasks = len(to_dos)
            tasks_completed = 0
            titles_completed = []

            # Count and append titles of completed tasks
            for to_do in to_dos:
                # Count and append titles of completed tasks
                if to_do['completed'] is True:
                    tasks_completed += 1
                    titles_completed.append(to_do['title'])

            tasks_completed = len(titles_completed)

            # Print the data
            print(f"Employee {user['name']} is done \
                  with tasks({tasks_completed}/{total_tasks})")
            for title in titles_completed:
                print(f"\t {title}")

            # Data for json of a single user
            json_dict = {}
            user_list = []

            # Append data to user_list
            for task in to_dos:
                user_dict = {}
                user_dict.update(
                    {'task': task['title'],
                     'completed': task['completed'],
                     'username': user['username']})
                user_list.append(user_dict)

            json_dict[user['id']] = user_list

            # Export to JSON
            with open(f"{user['id']}.json", 'w') as json_file:
                json.dump(json_dict, json_file)


if __name__ == '__main__':
    get_employee()
