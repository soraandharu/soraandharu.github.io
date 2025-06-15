"""学生存储接口"""
from abc import ABC, abstractmethod

class StudentStorageInterface(ABC):
    @abstractmethod
    def get_all_students(self): pass
    
    @abstractmethod
    def get_student_by_id(self, student_id): pass
    
    @abstractmethod
    def add_student(self, student_id, name, age, grade): pass
    
    @abstractmethod
    def update_student(self, student_id, name=None, age=None, grade=None): pass
    
    @abstractmethod
    def delete_student(self, student_id): pass
