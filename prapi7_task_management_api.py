import requests

base_url = 'https://jsonplaceholder.typicode.com/todos'


def get_all_tasks():
    """Fetch all tasks"""
    response = requests.get(base_url)
    return response.json()


def get_task(task_id):
    """Fetch one specific task"""
    response = requests.get(f"{base_url}/{task_id}")
    return response.json()


def create_task(title, user_id=1):
    """Create a new task"""
    new_task = {"userId": user_id, "title": title, "completed": False}
    response = requests.post(base_url, json=new_task)
    return response.json()


def update_task(task_id, title=None, completed=None):
    """Update existing task"""
    data = {}
    if title is not None:
        data["title"] = title
    if completed is not None:
        data["completed"] = completed
    response = requests.patch(f"{base_url}/{task_id}", json=data)
    return response.json()


def delete_task(task_id):
    """Delete a task"""
    response = requests.delete(f"{base_url}/{task_id}")
    return response.status_code == 200

tasks = get_task(1)

print(tasks)