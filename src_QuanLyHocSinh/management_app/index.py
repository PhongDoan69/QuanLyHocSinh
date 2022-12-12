from management_app import app
from flask import render_template, request
import utils
import json
from management_app.admin import *


@app.route("/")
def home():
    gras = utils.load_grades()

    g_id = request.args.get('grade_id')
    kw = request.args.get('keyword')
    students = utils.load_students(g_id=g_id, kw=kw)

    return render_template('index.html', grades=gras, students=students)


@app.route("/students")
def student_list():
    g_id = request.args.get("grade_id")
    kw = request.args.get("keyword")
    from_total_score = request.args.get("from_total_score")


    students = utils.load_students(g_id=g_id, kw=kw, from_total_score=from_total_score)



    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
