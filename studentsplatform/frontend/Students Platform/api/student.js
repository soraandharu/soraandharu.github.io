// 学生管理相关API
import { request } from '../utils/request';

// 基础URL配置 - 根据你的后端服务地址调整
const BASE_URL = 'http://localhost:50721';

/**
 * 获取所有学生列表
 * @returns {Promise} 返回学生列表数据
 */
export function getAllStudents() {
  return request({
    url: `${BASE_URL}/students`,
    method: 'GET'
  });
}

/**
 * 获取单个学生信息
 * @param {number} studentId - 学生ID
 * @returns {Promise} 返回学生信息
 */
export function getStudentById(studentId) {
  return request({
    url: `${BASE_URL}/students/${studentId}`,
    method: 'GET'
  });
}

/**
 * 添加学生
 * @param {Object} studentData - 学生数据
 * @param {number} studentData.id - 学生ID
 * @param {string} studentData.name - 学生姓名
 * @param {number} studentData.age - 学生年龄
 * @param {string} studentData.grade - 学生年级
 * @returns {Promise} 添加结果
 */
export function addStudent(studentData) {
  return request({
    url: `${BASE_URL}/students`,
    method: 'POST',
    data: studentData
  });
}

/**
 * 更新学生信息
 * @param {number} studentId - 学生ID
 * @param {Object} studentData - 需要更新的学生数据(部分字段)
 * @returns {Promise} 更新结果
 */
export function updateStudent(studentId, studentData) {
  return request({
    url: `${BASE_URL}/students/${studentId}`,
    method: 'PUT',
    data: studentData
  });
}

/**
 * 删除学生
 * @param {number} studentId - 要删除的学生ID
 * @returns {Promise} 删除结果
 */
export function deleteStudent(studentId) {
  return request({
    url: `${BASE_URL}/students/${studentId}`,
    method: 'DELETE'
  });
}
