"""This script uses JSON Placeholder
  - This REST API has fake data that can be used for testing
  - And exports that data into a JSON format
"""
# Import files
import json
import requests
import sys

# Get id from command line
employee_id = sys.argv[1]

# End point for users
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

# Write to csv file
with open(file_name, 'w') as json_file:
    json.dump(output_data, json_file)
