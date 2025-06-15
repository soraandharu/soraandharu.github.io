# 学生管理系统 - 前端

基于 uni-app 框架的跨平台前端应用，支持 H5、小程序、APP 多端发布。

## 技术栈

- **框架**: uni-app (Vue 3 Composition API)
- **UI**: 原生组件 + 自定义样式
- **HTTP**: 封装的 request 工具类
- **开发工具**: HBuilderX / VS Code

## 项目结构

```
Students Platform/
├── App.vue                 # 应用主入口
├── main.js                # 应用启动文件
├── manifest.json          # 应用配置文件
├── pages.json             # 页面路由配置
├── uni.scss              # 全局样式变量
├── api/
│   └── student.js         # 学生管理 API
├── pages/
│   ├── index/
│   │   └── index.vue      # 首页
│   └── students/
│       └── index.vue      # 学生管理页面
├── utils/
│   └── request.js         # HTTP 请求封装
├── static/
│   └── logo.png           # 应用图标
└── unpackage/             # 编译输出目录
```

## 功能模块

### 🏠 首页 (`pages/index/`)
- 应用导航入口
- 快速访问学生管理功能

### 👥 学生管理 (`pages/students/`)
- **学生列表**: 展示所有学生信息
- **添加学生**: 表单添加新学生
- **编辑学生**: 修改学生信息
- **删除学生**: 删除学生记录
- **响应式UI**: 适配不同屏幕尺寸

### 🔧 工具模块 (`utils/`)
- **request.js**: 统一的 HTTP 请求封装
  - 请求拦截器
  - 响应拦截器
  - 错误处理
  - 超时设置

### 📡 API 模块 (`api/`)
- **student.js**: 学生管理相关 API
  - `getAllStudents()` - 获取学生列表
  - `addStudent(data)` - 添加学生
  - `updateStudent(id, data)` - 更新学生
  - `deleteStudent(id)` - 删除学生

## 开发指南

### 环境要求
- Node.js 14+
- HBuilderX 或 uni-app CLI
- 微信开发者工具（小程序开发）

### 本地开发

#### 使用 HBuilderX
1. 打开 HBuilderX
2. 导入项目: `frontend/Students Platform`
3. 运行到浏览器或模拟器

#### 使用 CLI
```bash
# 安装 uni-app CLI
npm install -g @vue/cli @dcloudio/uvm

# 运行到 H5
npm run dev:h5

# 运行到微信小程序
npm run dev:mp-weixin

# 运行到 APP
npm run dev:app-plus
```

### 配置说明

#### API 配置
在 `api/student.js` 中修改后端服务地址：
```javascript
const BASE_URL = 'http://localhost:50721'; // 修改为实际后端地址
```

#### 请求配置
在 `utils/request.js` 中配置请求参数：
```javascript
const config = {
  timeout: 10000,        // 请求超时时间
  baseURL: '',          // 基础URL
  headers: {}           // 请求头
};
```

## 页面路由

配置文件: `pages.json`

```json
{
  "pages": [
    {
      "path": "pages/index/index",
      "style": { "navigationBarTitleText": "首页" }
    },
    {
      "path": "pages/students/index", 
      "style": { "navigationBarTitleText": "学生管理" }
    }
  ]
}
```

## 样式规范

### 全局样式
- 使用 `uni.scss` 定义全局样式变量
- 统一的颜色主题和字体规范

### 组件样式
- 使用 scoped 样式避免污染
- 响应式设计，适配不同设备
- 遵循 uni-app 样式编写规范

## 构建发布

### H5 发布
```bash
npm run build:h5
```
输出目录: `unpackage/dist/build/h5`

### 小程序发布
```bash
npm run build:mp-weixin
```
输出目录: `unpackage/dist/build/mp-weixin`

### APP 发布
```bash
npm run build:app-plus
```
输出目录: `unpackage/dist/build/app-plus`

## 调试技巧

### 网络调试
1. 在 `utils/request.js` 中开启调试模式
2. 查看 Network 面板的请求响应
3. 使用 `console.log` 打印调试信息

### 设备调试
- **H5**: 浏览器开发者工具
- **小程序**: 微信开发者工具
- **APP**: HBuilderX 真机调试

## 常见问题

### Q: 请求后端接口失败？
A: 检查以下几点：
1. 后端服务是否启动（端口 50721）
2. API 地址配置是否正确
3. 网络连接是否正常
4. 跨域配置是否正确

### Q: 页面样式显示异常？
A: 确认：
1. 样式单位使用 rpx 而非 px
2. 避免使用浏览器特定的 CSS 属性
3. 检查 uni-app 兼容性文档

### Q: 真机调试问题？
A: 建议：
1. 使用 HBuilderX 的真机运行功能
2. 确保手机和电脑在同一网络
3. 检查手机开发者选项设置

## 贡献指南

1. 遵循 Vue 3 + uni-app 开发规范
2. 保持代码风格一致性
3. 添加必要的注释和文档
4. 测试多端兼容性