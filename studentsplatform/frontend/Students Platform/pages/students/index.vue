<template>
  <view class="container">
    <view class="header">
      <text class="title">学生管理系统</text>
      <button type="primary" @click="showAddForm">添加学生</button>
    </view>
    
    <!-- 学生列表 -->
    <view class="student-list" v-if="students.length">
      <view class="student-card" v-for="(student, index) in students" :key="student.id">
        <view class="student-info">
          <view class="student-name">{{student.name}}</view>
          <view class="student-details">
            <text>ID: {{student.id}}</text>
            <text>年龄: {{student.age}}岁</text>
            <text>班级: {{student.grade}}</text>
          </view>
        </view>
        <view class="student-actions">
          <button size="mini" type="default" @click="handleEdit(student)">编辑</button>
          <button size="mini" type="warn" @click="handleDelete(student.id)">删除</button>
        </view>
      </view>
    </view>
    
    <!-- 无数据提示 -->
    <view class="empty-tip" v-else>
      <text>暂无学生数据</text>
    </view>
    
    <!-- 添加/编辑表单 -->
    <view class="form-container" v-if="showForm">
      <view class="form-mask" @click="closeForm"></view>
      <view class="form-content">
        <view class="form-header">
          <text class="form-title">{{isEdit ? '编辑学生' : '添加学生'}}</text>
          <text class="close-btn" @click="closeForm">×</text>
        </view>
        <view class="form-body">
          <view class="form-item" v-if="!isEdit">
            <text class="form-label">学号:</text>
            <input v-model="formData.id" type="number" placeholder="请输入学号" />
          </view>
          <view class="form-item">
            <text class="form-label">姓名:</text>
            <input v-model="formData.name" type="text" placeholder="请输入姓名" />
          </view>
          <view class="form-item">
            <text class="form-label">年龄:</text>
            <input v-model="formData.age" type="number" placeholder="请输入年龄" />
          </view>
          <view class="form-item">
            <text class="form-label">班级:</text>
            <input v-model="formData.grade" type="text" placeholder="请输入班级" />
          </view>
          <view class="form-btns">
            <button type="primary" @click="submitForm">保存</button>
          </view>
        </view>
      </view>
    </view>
  </view>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getAllStudents, addStudent, updateStudent, deleteStudent } from '../../api/student.js'

// 响应式数据
const students = ref([])
const formData = ref({
  id: '',
  name: '',
  age: '',
  grade: ''
})
const isEdit = ref(false)
const currentId = ref(null)
const showForm = ref(false)

// 加载学生列表
const loadStudents = async () => {
  try {
    const result = await getAllStudents()
    students.value = result
  } catch (error) {
    uni.showToast({
      title: '获取学生列表失败',
      icon: 'none'
    })
  }
}

// 显示添加表单
const showAddForm = () => {
  isEdit.value = false
  resetForm()
  showForm.value = true
}

// 显示编辑表单
const handleEdit = (student) => {
  isEdit.value = true
  currentId.value = student.id
  formData.value = { ...student }
  showForm.value = true
}

// 关闭表单
const closeForm = () => {
  showForm.value = false
}

// 重置表单数据
const resetForm = () => {
  formData.value = {
    id: '',
    name: '',
    age: '',
    grade: ''
  }
  currentId.value = null
}

// 表单验证
const validateForm = () => {
  if (!isEdit.value && !formData.value.id) {
    uni.showToast({ title: '请输入学号', icon: 'none' })
    return false
  }
  if (!formData.value.name) {
    uni.showToast({ title: '请输入姓名', icon: 'none' })
    return false
  }
  if (!formData.value.age) {
    uni.showToast({ title: '请输入年龄', icon: 'none' })
    return false
  }
  if (!formData.value.grade) {
    uni.showToast({ title: '请输入班级', icon: 'none' })
    return false
  }
  return true
}

// 提交表单
const submitForm = async () => {
  try {
    // 表单验证
    if (validateForm()) {
      if (isEdit.value) {
        // 编辑模式
        await updateStudent(currentId.value, {
          name: formData.value.name,
          age: parseInt(formData.value.age),
          grade: formData.value.grade
        })
        uni.showToast({ title: '更新成功', icon: 'success' })
      } else {
        // 添加模式
        await addStudent({
          id: parseInt(formData.value.id),
          name: formData.value.name,
          age: parseInt(formData.value.age),
          grade: formData.value.grade
        })
        uni.showToast({ title: '添加成功', icon: 'success' })
      }
      closeForm()
      loadStudents() // 重新加载数据
    }
  } catch (error) {
    uni.showToast({
      title: error.message || '操作失败',
      icon: 'none'
    })
  }
}

// 删除学生
const handleDelete = async (studentId) => {
  uni.showModal({
    title: '提示',
    content: '确定要删除该学生吗？',
    success: async (res) => {
      if (res.confirm) {
        try {
          await deleteStudent(studentId)
          uni.showToast({ title: '删除成功', icon: 'success' })
          loadStudents() // 重新加载数据
        } catch (error) {
          uni.showToast({
            title: error.message || '删除失败',
            icon: 'none'
          })
        }
      }
    }
  })
}

// 页面加载时获取数据
onMounted(() => {
  loadStudents()
})
</script>

<style scoped>
.container {
  padding: 20rpx;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30rpx;
}

.title {
  font-size: 36rpx;
  font-weight: bold;
}

.student-list {
  margin-bottom: 20rpx;
}

.student-card {
  display: flex;
  justify-content: space-between;
  padding: 20rpx;
  margin-bottom: 20rpx;
  background-color: #fff;
  border-radius: 10rpx;
  box-shadow: 0 2rpx 10rpx rgba(0, 0, 0, 0.1);
}

.student-info {
  flex: 1;
}

.student-name {
  font-size: 32rpx;
  font-weight: bold;
  margin-bottom: 10rpx;
}

.student-details {
  font-size: 28rpx;
  color: #666;
}

.student-details text {
  margin-right: 20rpx;
  display: block;
  line-height: 1.6;
}

.student-actions {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.student-actions button {
  margin: 10rpx 0;
}

.empty-tip {
  text-align: center;
  padding: 100rpx 0;
  color: #999;
}

.form-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
}

.form-mask {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1;
}

.form-content {
  width: 600rpx;
  background-color: #fff;
  border-radius: 10rpx;
  overflow: hidden;
  z-index: 2;
  position: relative;
}

.form-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20rpx;
  background-color: #f8f8f8;
  border-bottom: 1rpx solid #eee;
}

.form-title {
  font-size: 32rpx;
  font-weight: bold;
}

.close-btn {
  font-size: 40rpx;
  font-weight: bold;
  padding: 0 10rpx;
}

.form-body {
  padding: 30rpx;
}

.form-item {
  margin-bottom: 20rpx;
}

.form-label {
  display: block;
  margin-bottom: 10rpx;
  font-size: 28rpx;
}

.form-item input {
  width: 100%;
  height: 80rpx;
  border: 1rpx solid #ddd;
  border-radius: 6rpx;
  padding: 0 20rpx;
  font-size: 28rpx;
}

.form-btns {
  margin-top: 30rpx;
}
</style>
