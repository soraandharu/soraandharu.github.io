# 学生管理系统 (Students Platform)

一个基于 Flask + uni-app 的全栈学生管理系统，支持双存储模式（JSON 和 SQLite）。

## 学习记录
- **总结与讨论**
由于上次的任务我已经用uniapp实现了，这段时间我花时间深入学习了uniapp组件那一块内容，并学习了peewee orm来管理数据库，自己试过连接mysql和sqlite做过基础的测试，效果比预期的好。于是这次任务我在原有基础上新增了sqlite数据库存储数据，在前端方面用组合式API把一些部分优化了。
~
- **目标与规划**
通过最近的学习我掌握了前后端开发的大致内容，之后计划在完成基础任务并新增设计管理员登录，界面上使用首页导航，自己写组件简化。

接下来的内容由AI分析整个项目生成，我稍微改了一些。

## 项目架构

```
studentsplatform/
├── backend/           # Flask 后端服务
├── frontend/          # uni-app 前端应用
└── test/             # 测试文件
```

## 功能特性

- ✅ 学生信息增删改查（CRUD）
- ✅ 双存储支持（JSON 文件 + SQLite 数据库）
- ✅ 跨平台前端（uni-app 支持 H5、小程序、APP）
- ✅ RESTful API 设计
- ✅ 响应式 UI 界面

## 技术栈

### 后端 (Backend)
- **框架**: Flask 2.2.5
- **数据库**: SQLite + JSON 文件存储, 默认SQLite
- **ORM**: Peewee 3.18.1
- **跨域**: Flask-CORS 6.0.0

### 前端 (Frontend)
- **框架**: uni-app (Vue 3)
- **UI**: 原生组件
- **HTTP**: 封装的 request 工具

## 快速开始

### 1. 后端服务启动

```bash
# 进入后端目录
cd backend

# 安装依赖
pip install -r requirements.txt

# 启动服务
python server.py
```

服务将在 `http://localhost:50721` 启动

### 2. 前端开发

```bash
# 进入前端目录
cd "frontend/Students Platform"

# 使用 HBuilderX 打开项目
# 或者使用 uni-app CLI 运行
```

## API 接口

### 基础路径
```
http://localhost:50721
```

### 学生管理接口

| 方法 | 路径 | 描述 | 参数 |
|------|------|------|------|
| GET | `/students` | 获取所有学生 | - |
| POST | `/students` | 添加学生 | `{id, name, age, grade}` |
| PUT | `/students/{id}` | 更新学生信息 | `{name?, age?, grade?}` |
| DELETE | `/students/{id}` | 删除学生 | - |

### 请求示例

**添加学生**
```json
POST /students
{
  "id": 1001,
  "name": "张三",
  "age": 18,
  "grade": "高三1班"
}
```

**更新学生**
```json
PUT /students/1001
{
  "name": "张三丰",
  "age": 19
}
```

## 数据存储

项目支持两种存储方式：

1. **SQLite 数据库** (默认)
   - 文件位置: `backend/data/students.db`
   - 使用 Peewee ORM 管理

2. **JSON 文件存储**
   - 文件位置: `backend/data/students.json`
   - 纯文本存储，便于调试

## 项目结构详解

### 后端目录结构
```
backend/
├── server.py              # Flask 主服务器
├── storage_interface.py   # 存储接口定义
├── json_storage.py        # JSON 存储实现
├── sqlite_storage.py      # SQLite 存储实现
├── requirements.txt       # Python 依赖
├── test_simple.py         # 简单测试
└── data/                  # 数据文件目录
    ├── students.db        # SQLite 数据库
    └── students.json      # JSON 数据文件
```

### 前端目录结构
```
frontend/Students Platform/
├── App.vue               # 应用主入口
├── main.js              # 应用启动文件
├── manifest.json        # 应用配置
├── pages.json           # 页面路由配置
├── api/
│   └── student.js       # 学生API调用
├── pages/
│   ├── index/           # 首页
│   └── students/        # 学生管理页面
├── utils/
│   └── request.js       # HTTP 请求封装
└── static/              # 静态资源
```

## 开发说明

### 后端开发
- 采用接口模式设计，支持多种存储实现
- 默认使用 SQLite 存储，可在 `server.py` 中切换为 JSON 存储
- 所有 API 支持 CORS 跨域请求

### 前端开发
- 基于 uni-app 框架，支持多端发布
- 使用 Vue 3 Composition API
- 响应式设计，适配移动端和桌面端

## 配置说明

### 后端配置
- **端口**: 默认 50721，可在 `server.py` 修改
- **存储方式**: 在 `StudentManager` 类中切换 `self.storage`
- **数据目录**: `backend/data/`

### 前端配置
- **API 地址**: 在 `api/student.js` 中的 `BASE_URL` 修改
- **请求超时**: 在 `utils/request.js` 中配置

## 部署建议

### 开发环境
1. 后端使用开发模式启动 (`debug=False`)
2. 前端使用 HBuilderX 或 CLI 工具运行



## 许可证

MIT License