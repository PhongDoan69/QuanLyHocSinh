from urllib import request

from flask import redirect, render_template

from management_app.models import Grade, Student, User
from flask_login import current_user, login_user, logout_user
from sqlalchemy import func
import hashlib
import json
import utils


def read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_grades():
    return Grade.query.all()
    # return read_json(os.path.join(app.root_path, 'data/grades.json'))


def load_students(g_id=None, kw=None, from_total_score=None):
    students = Student.query.filter()

    if g_id:
        students = students.filter(Student.grade_id.__eq__(g_id))

    if kw:
        students = students.filter(Student.name.contains(kw))

    if from_total_score:
        students = students.filter(Student.total_score.__ge__(from_total_score))

    return students


def get_student_by_id(student_id):
    return Student.query.get(student_id)

def login_my_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = utils.auth_user(username=username, password=password)
        if user:
            login_user(user)

            u = request.args.get('next')
            return redirect(u if u else '/')

    return render_template('login.html')

def login_admin():
    username = request.form['username']
    password = request.form['password']

    user = utils.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


def logout_my_user():
    logout_user()
    return redirect('/login')