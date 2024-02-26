import requests
import json

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def get_employee_data(employee_id):

    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()


    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    filename = f'{id}.json'

    employee_tasks = []
    for task in todo_data:
        task_info = {
            "username": employee_data,
            "task": task["title"],
            "completed": task["completed"]
        }
        employee_tasks.append(task_info)
    
    return employee_tasks


def display_todo_progress(employee_data, todo_data):
    employee_name = employee_data.get('name')
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)
    completed_task_titles = [task['title'] for task in todo_data if task['completed']]

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in completed_task_titles:
        print(f"\t{title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data, todo_data = get_employee_data(employee_id)
    display_todo_progress(employee_data, todo_data)
