# 📝 Flask To-Do List App

A clean and simple to-do list web application built with Flask.  
Supports task creation, editing, completion tracking, priority levels, dark mode, and file-based persistence.

---

## 🚀 Features

- ✅ Add, delete, and edit tasks
- ✅ Mark tasks as completed with checkboxes
- ✅ Persistent task storage via `tasks.json`

---

## 📂 Project Structure
```
/
├── app.py                 # Main Flask app
├── tasks.json             # JSON file for task storage
├── test_app.py            # Pytest-based unit tests
├── requirements.txt       # Python package requirements
├── README.md              # Project overview and instructions
├── static/
│   └── style.css          # Custom styling (light/dark modes, priorities)
└── templates/
    ├── base.html          # Layout template with header/footer and dark mode toggle
    └── index.html         # Main task list page
```

## Getting started
Clone this repo
```
git clone https://github.com/your-username/Todo-list-flask.git
cd Todo-list-flask
```
Run the app
```
export FLASK_APP=app.py
flask run
```
Then open your browser to:
http://127.0.0.1:5000