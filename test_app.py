import os
import json
import pytest
from app import app, TASK_FILE

@pytest.fixture(autouse=True)
def clean_tasks_file():
    # Remove tasks.json before and after each test to isolate test state
    if os.path.exists(TASK_FILE):
        os.remove(TASK_FILE)
    yield
    if os.path.exists(TASK_FILE):
        os.remove(TASK_FILE)

def test_homepage_loads():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'My To-Do App' in response.data

def test_add_task():
    with app.test_client() as client:
        client.post('/add', data={'task': 'Write unit test'})
        with open(TASK_FILE, 'r') as f:
            tasks = json.load(f)
        assert len(tasks) == 1
        assert tasks[0]['content'] == 'Write unit test'
        assert tasks[0]['done'] is False

def test_toggle_task_status():
    with app.test_client() as client:
        # Add a task
        client.post('/add', data={'task': 'Check toggle'})
        # Toggle it to done
        client.post('/toggle/0')
        with open(TASK_FILE, 'r') as f:
            tasks = json.load(f)
        assert tasks[0]['done'] is True
        # Toggle it back to not done
        client.post('/toggle/0')
        with open(TASK_FILE, 'r') as f:
            tasks = json.load(f)
        assert tasks[0]['done'] is False

def test_delete_task():
    with app.test_client() as client:
        # Add two tasks
        client.post('/add', data={'task': 'Task A'})
        client.post('/add', data={'task': 'Task B'})
        # Delete the first one
        client.post('/delete/0')
        with open(TASK_FILE, 'r') as f:
            tasks = json.load(f)
        assert len(tasks) == 1
        assert tasks[0]['content'] == 'Task B'
