"""SQLite存储实现"""
from peewee import *
from storage_interface import StudentStorageInterface

db = SqliteDatabase('./data/students.db')

class Student(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    age = IntegerField()
    grade = CharField()
    
    class Meta:
        database = db
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'age': self.age, 'grade': self.grade}

class SQLiteStudentStorage(StudentStorageInterface):
    def __init__(self):
        if db.is_closed():
            db.connect()
        db.create_tables([Student], safe=True)

    def get_all_students(self):
        return [s.to_dict() for s in Student.select()]

    def get_student_by_id(self, student_id):
        try:
            return Student.get_by_id(student_id).to_dict()
        except Student.DoesNotExist:
            return None

    def add_student(self, student_id, name, age, grade):
        if self.get_student_by_id(student_id):
            return False
        Student.create(id=student_id, name=name, age=age, grade=grade)
        return True

    def update_student(self, student_id, name=None, age=None, grade=None):
        try:
            student = Student.get_by_id(student_id)
            if name: student.name = name
            if age: student.age = age
            if grade: student.grade = grade
            student.save()
            return True
        except Student.DoesNotExist:
            return False

    def delete_student(self, student_id):
        try:
            Student.get_by_id(student_id).delete_instance()
            return True
        except Student.DoesNotExist:
            return False
