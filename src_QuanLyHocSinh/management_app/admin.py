from management_app import admin, db
from management_app.models import Grade, Student
from flask_admin.contrib.sqla import ModelView

admin.add_view((ModelView(Grade, db.session)))
admin.add_view((ModelView(Student, db.session)))

