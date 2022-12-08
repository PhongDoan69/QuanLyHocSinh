import json, os
from management_app import app

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_grades():
    return read_json(os.path.join(app.root_path, 'data/grades.json'))

def load_students():
    return read_json(os.path.join(app.root_path, 'data/students.json'))