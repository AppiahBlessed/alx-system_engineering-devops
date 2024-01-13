#!/usr/bin/python3
"""This script uses JSON Placeholder"""
# Importing module
import json
import requests
import sys

if __name__ == "__main__":
    # Get id from command line
    employee_id = sys.argv[1]

    # Endpoint for users
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Make GET request
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Get information to display
    username = user_data["username"]
    user_id = user_data["id"]

    # Endpoint for TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Make request
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    tasks_list = [{"task": todo["title"], "completed": todo["completed"], "username": username} for todo in todo_data]
    output_data = {str(user_id): tasks_list}

    # Any file saved would be named with the id argument passed
    file_name = f"{user_id}.json"

    # Write to JSON file
    with open(file_name, 'w') as json_file:
        json.dump(output_data, json_file)
