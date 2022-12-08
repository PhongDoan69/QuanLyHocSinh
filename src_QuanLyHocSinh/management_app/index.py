from management_app import app
from flask import render_template
import utils
import json

@app.route("/")
def home():
    grades = utils.load_grades()
    return render_template('index.html', grades=grades)



@app.route("/students")
def student_list():
    students = utils.load_students()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
