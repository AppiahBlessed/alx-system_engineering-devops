#!/usr/bin/python3
"""This script uses JSON Placeholder"""
# Importing modules
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Endpoint to user
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Query url
    user_data = requests.get(user_url)

    # Convert to json string
    id_data = user_data.json()
    emp_name = id_data["name"]

    # The completed number of tasks
    t_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_result = requests.get(t_url)

    # Error handling
    if user_data.status_code != 200:
        print(f"Error:Status code: {user_data.status_code}")
        sys.exit(1)

    if todo_result.status_code != 200:
        print(f"Error:Status code: {todo_result.status_code}")
        sys.exit(1)

    # Result is a json list
    todo_data = todo_result.json()

    # Initialize count
    count = 0
    for key in todo_data:
        if key["completed"] is True:
            count += 1

    print(f"Employee {emp_name} is done with tasks({count}/20):")
    for key in todo_data:
        if key["completed"] is True:
            # I would have used " instead of ' but the interpreter
            # might take the other one as the end of the f string
            print(f"\t {key['title']}")
