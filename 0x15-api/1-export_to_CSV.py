#!/usr/bin/python3
'''This script uses JSON Placeholder'''
# Import files
import csv
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

# Any file saved would be named with the id argument passed
file_name = f"{user_id}.csv"

# Write to csv file
with open(file_name, 'w', newline='') as csv_file:
# quotechar="'" To prevent triplicating
    csv_writer = csv.writer(csv_file, quotechar="'")
    for todo in todo_data:
        csv_writer.writerow([f'"{user_id}"', f'"{username}"', f'"{todo["completed"]}"', f'"{todo["title"]}"'])
