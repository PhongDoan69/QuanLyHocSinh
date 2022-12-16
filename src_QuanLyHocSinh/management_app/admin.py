from flask import redirect
from flask_admin import BaseView, AdminIndexView, expose

from management_app import admin, db, utils
from management_app.models import Grade, Student, UserRole
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user

admin.add_view((ModelView(Grade, db.session)))
admin.add_view((ModelView(Student, db.session)))


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class StudentModeView(AuthenticatedView):

    column_filters = ['name', 'grade_id']
    column_searchable_list = ['name', 'grade_id']
    column_exclude_list = ['name', 'grade_id']
    can_view_details = True
    can_export = True
    column_labels = {
        'name': 'Họ và tên',
        'dob': 'Năm sinh',
        'class': 'Lớp',
        'sex': 'Giới tính',
        'phone_number': 'Số điện thoại',
        'address': 'Địa chỉ',
        'total_score': 'Điểm trung bình'
    }
    page_size = 5

class LogoutView(AuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


class MyAdminView(AdminIndexView):
    @expose('/')
    def index(self):
        stats = utils.count_product_by_cate()
        return self.render('admin/index.html', stats=stats)