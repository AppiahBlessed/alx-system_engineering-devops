'''This script fetches all data from a JSON Placeholder API'''

# Imports
if __name__ == "__main__":
    import json
    import requests

    # Endpoint for users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Dictionary to store tasks for all employees
    all_tasks_data = {}

    # Iterate over each user
    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        # Endpoint for TODO list for the current user
        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

        # Make request
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Create a list of tasks in the specified format for the current user
        tasks_list = [{"username": username, "task": todo["title"], "completed": todo["completed"]} for todo in todo_data]

        # Add the tasks list to the dictionary with the user_id as the key
        all_tasks_data[str(user_id)] = tasks_list

    # Save the data to a JSON file named 'todo_all_employees.json'
    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as json_file:
        json.dump(all_tasks_data, json_file)
