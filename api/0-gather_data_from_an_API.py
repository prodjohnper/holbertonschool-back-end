#!/usr/bin/python3
'''
    Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''

import requests
from sys import argv


def get_employee(id=None):
    '''
        Function that, using this REST API, for a given employee ID,
        returns information about his/her TODO list progress.
    '''
    # Check if the argument is a number
    if len(argv) > 1:
        try:
            id = int(argv[1])
        except ValueError:
            return

    # Check if the argument is an integer
    if isinstance(id, int):
        base = "https://jsonplaceholder.typicode.com"
        user = requests.get(f"{base}/users/{id}").json()
        to_dos = requests.get(f"{base}/todos/?userId={id}").json()

        # Check if the user and the to_dos are not empty
        if user and to_dos:
            total_tasks = len(to_dos)
            titles_completed = [task["title"]
                                for task in to_dos
                                if task["completed"]]
            tasks_completed = len(titles_completed)

            # Print the result
            print(
                "Employee {} is done with tasks({}/{}):".format(
                    user["name"], tasks_completed, total_tasks
                )
            )

            # Print the titles of the completed tasks
            for title in titles_completed:
                print('\t {}'.format(title))


if __name__ == "__main__":
    get_employee()
