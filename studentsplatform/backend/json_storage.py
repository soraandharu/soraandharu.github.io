"""JSON存储实现"""
import json
import os
from storage_interface import StudentStorageInterface

class JSONStudentStorage(StudentStorageInterface):
    def __init__(self, file_path='./data/students.json'):
        self.file_path = file_path
        self.students = self._load_students()

    def _load_students(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def _save_students(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.students, f, ensure_ascii=False, indent=2)

    def get_student_by_id(self, student_id):
        return next((s for s in self.students if s['id'] == student_id), None)

    def add_student(self, student_id, name, age, grade):
        if self.get_student_by_id(student_id):
            return False
        self.students.append({'id': student_id, 'name': name, 'age': age, 'grade': grade})
        self._save_students()
        return True
    
    def get_all_students(self):
        return self.students
    
    def update_student(self, student_id, name=None, age=None, grade=None):
        student = self.get_student_by_id(student_id)
        if not student:
            return False
        if name: student['name'] = name
        if age: student['age'] = age
        if grade: student['grade'] = grade
        self._save_students()
        return True
    
    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)
        if not student:
            return False
        self.students.remove(student)
        self._save_students()
        return True
