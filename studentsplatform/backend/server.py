"""学生管理系统 - 简化版双存储"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from json_storage import JSONStudentStorage
from sqlite_storage import SQLiteStudentStorage

class StudentManager:
    def __init__(self):
        self.json = JSONStudentStorage()
        self.sqlite = SQLiteStudentStorage()
        self.storage = self.sqlite

# Flask应用
app = Flask(__name__)
CORS(app)
manager = StudentManager()

# 基础API（JSON存储）
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(manager.storage.get_all_students())

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    if manager.storage.add_student(data['id'], data['name'], data['age'], data['grade']):
        return jsonify({'message': 'Success'}), 201
    return jsonify({'error': 'Student exists'}), 400

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    if manager.storage.update_student(id, data.get('name'), data.get('age'), data.get('grade')):
        return jsonify({'message': 'Success'})
    return jsonify({'error': 'Not found'}), 404

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    if manager.storage.delete_student(id):
        return jsonify({'message': 'Success'})
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    print("学生管理系统启动 - JSON + SQLite双存储")
    print("API: /students (JSON), /students/json, /students/sqlite")
    app.run(host='0.0.0.0', port=50721, debug=False)
