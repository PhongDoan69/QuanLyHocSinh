from management_app import app
from flask import render_template
import utils

@app.route("/")
def home():
    grades = utils.load_grades()
    return render_template('index.html', grades=grades)


if __name__ == '__main__':
    app.run(debug=True)
