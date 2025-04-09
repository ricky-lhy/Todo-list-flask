from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)
TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    tasks = load_tasks()
    sort_order = request.args.get('sort', 'desc')
    tasks.sort(key=lambda t: (t['done'], datetime.fromisoformat(t['created_at']).timestamp() * (-1 if sort_order == 'desc' else 1)))
    return render_template('index.html', tasks=enumerate(tasks), sort_order=sort_order)

@app.route('/add', methods=['POST'])
def add():
    tasks = load_tasks()
    task_content = request.form.get('task')
    if task_content:
        tasks.append({
            'content': task_content,
            'done': False,
            'created_at': datetime.now().isoformat()
        })
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):
    tasks = load_tasks()
    new_content = request.form.get('content')
    if new_content and 0 <= task_id < len(tasks):
        tasks[task_id]['content'] = new_content
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = not tasks[task_id]['done']
        save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
