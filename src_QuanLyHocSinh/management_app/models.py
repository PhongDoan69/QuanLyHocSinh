from management_app import app
from sqlalchemy import Column, Integer, String, Enum, Float, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from enum import Enum as UserEnum
from flask_login import UserMixin
from management_app import db, app
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class UserRole(UserEnum):
    USER = 1
    EMPLOYEE = 2
    ADMIN = 3
    pass


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


class Grade(BaseModel):
    __tablename__ = 'grade'

    name = Column(String(20), nullable=False)
    students = relationship('Student', backref='grade', lazy=False)

    def __str__(self):
        return self.name


class Student(BaseModel):
    __tablename__ = 'student'

    name = Column(String(50), nullable=False)
    dob = Column(Integer)
    class_name = Column(String(10))
    sex = Column(String(10))
    phone_number = Column(String(15))
    address = Column(String(50))
    total_score = Column(Float, default=0)

    grade_id = Column(Integer, ForeignKey(Grade.id), nullable=False)

    # score15s = relationship('Score15', backref='student', lazy=True)

    def __str__(self):
        return self.name


# class Score15(BaseModel):
#     __tablename__ = 'score15'
#
#     score15_value1 = Column(Float, default=0)
#     score15_value2 = Column(Float, default=0)
#     score15_value3 = Column(Float, default=0)
#     score15_value4 = Column(Float, default=0)
#     score15_value5 = Column(Float, default=0)
#     student_id = Column(Float, ForeignKey(Student.id), nullable=False)
#     grade_id = Column(Float, ForeignKey(Grade.id), nullable=False)
#
#     def __str__(self):
#         return self.name

# class Score45(BaseModel):
#     __tablename__ = 'score45'
#
#     score45_value1 = Column(Float, default=0)
#     score45_value2 = Column(Float, default=0)
#     score45_value3 = Column(Float, default=0)
#     student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
#
#     def __str__(self):
#         return self.name
#
#
# class ScoreFinalExam(BaseModel):
#     __tablename__ = 'score_final_exam'
#
#     score_final_exam = Column(Float, default=0)
#
#     student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
#
#     def __str__(self):
#         return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # g1 = Grade(name='L???p 10')
        # g2 = Grade(name='L???p 11')
        # g3 = Grade(name='L???p 12')
        # # db.session.add_all([g1, g2, g3])
        # # db.session.commit()
        #
        # s1 = Student(name='Nguyen Van A', dob=2008, class_name='10C1', sex='male',
        #                   phone_number='0123456789', address='TP. HCM', total_score=0,
        #                   grade_id=1)
        # s2 = Student(name='Nguyen Thi Ngoc B', dob=2008, class_name='11C1', sex='female',
        #              phone_number='0123456789', address='TP. HCM', total_score=0,
        #              grade_id=2)
        # s3 = Student(name='Dang Van C', dob=2008, class_name='12C1', sex='male',
        #              phone_number='0123456789', address='TP. HCM', total_score=0,
        #              grade_id=3)
        # db.session.add_all([s1, s2, s3])
        # db.session.commit()