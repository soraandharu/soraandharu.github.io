<template>
<view class="list-section">
      <view class="list-title">学生列表</view>
      
      <view class="student-list">
        <view class="student-item" v-for="(student, index) in studentList" :key="student.id">
          <view class="student-info">
            <text class="student-id">学号: {{student.id}}</text>
            <text class="student-name">{{student.name}}</text>
            <text class="student-age">{{student.age}}岁</text>
            <text class="student-grade">{{student.grade}}</text>
          </view>
        </view>
     
        <view class="empty-tip" v-if="studentList.length === 0">
          暂无学生数据
        </view>
      </view>
    </view>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 响应式数据
const studentList = ref([])

// 获取所有学生列表
const getStudentsList = () => {
  uni.request({
    url: 'http://localhost:50721/students', // 学生列表接口地址
    method: 'GET',
    header: {
      'Content-Type': 'application/json'
    },
    success: (res) => {
      console.log('获取学生列表成功:', res.data);
      // 将获取的数据赋值给studentList
      studentList.value = res.data;
    },
    fail: (err) => {
      console.error('获取学生列表失败:', err);
      // 显示错误提示
      uni.showToast({
        title: '获取学生数据失败',
        icon: 'none'
      });
    }
  });
}

// 页面加载时获取数据
onMounted(() => {
  getStudentsList();
})
</script>

<style scoped>
.list-section {
  padding: 15px;
}

.list-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 15px;
}

.student-item {
  padding: 10px;
  border-bottom: 1px solid #eee;
  background-color: #fff;
  margin-bottom: 10px;
  border-radius: 5px;
}

.student-info {
  display: flex;
  flex-direction: column;
}

.student-name {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
}

.student-id, .student-age, .student-grade {
  font-size: 14px;
  color: #666;
  margin-bottom: 3px;
}

.empty-tip {
  text-align: center;
  color: #999;
  padding: 30px 0;
}
</style>