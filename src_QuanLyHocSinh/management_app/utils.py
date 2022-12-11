import json, os
from management_app import app
from management_app.models import Grade, Student



def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_grades():
    return Grade.query.all()
    # return read_json(os.path.join(app.root_path, 'data/grades.json'))


def load_students(g_id=None, kw=None, from_total_score=None):
    students = Student.query.all()

    if g_id:
        students = students.filter(Student.)
    # students = read_json(os.path.join(app.root_path, 'data/students.json'))
    # if g_id:
    #     students = [g for g in students if g['grade_id'] == int(g_id)]
    # if kw:
    #     students = [g for g in students if g['name'].lower().find(kw.lower()) >= 0]
    # if from_total_score:
    #     students = [g for g in students if g['total_score'] >= float(from_total_score)]
    #
    # return students
