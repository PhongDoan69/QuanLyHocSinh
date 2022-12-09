import json, os
from management_app import app


def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_grades():
    return read_json(os.path.join(app.root_path, 'data/grades.json'))


def load_students(g_id=None, kw=None, to_total_score=None):
    students = read_json(os.path.join(app.root_path, 'data/students.json'))
    if g_id:
        students = [g for g in students if g['grade_id'] == int(g_id)]
    if kw:
        students = [g for g in students if g['name'].lower().find(kw.lower) >= 0]
    if to_total_score:
        students = [g for g in students if g['total_score'] == float(to_total_score)]

    return students
