# 学生管理系统 - 后端

基于 Flask 的 RESTful API 服务，支持双存储模式（JSON 文件 + SQLite 数据库）。

## 技术栈

- **Web框架**: Flask 2.2.5
- **数据库**: SQLite 3
- **ORM**: Peewee 3.18.1
- **跨域处理**: Flask-CORS 6.0.0
- **Python版本**: 3.7+

## 项目结构

```
backend/
├── server.py               # Flask 主服务器
├── storage_interface.py    # 存储接口抽象类
├── json_storage.py         # JSON 文件存储实现
├── sqlite_storage.py       # SQLite 数据库存储实现
├── requirements.txt        # Python 依赖包
├── test_simple.py          # 简单功能测试
├── data/                   # 数据存储目录
│   ├── students.db         # SQLite 数据库文件
│   └── students.json       # JSON 数据文件
└── __pycache__/            # Python 缓存文件
```

## 核心模块

### 🖥️ 服务器模块 (`server.py`)
- Flask 应用主入口
- RESTful API 路由定义
- 存储管理器集成
- CORS 跨域配置

### 🔧 存储接口 (`storage_interface.py`)
定义了统一的存储接口规范：
```python
class StudentStorageInterface:
    def add_student(self, student_id, name, age, grade)
    def get_all_students(self)
    def get_student_by_id(self, student_id)
    def update_student(self, student_id, name=None, age=None, grade=None)
    def delete_student(self, student_id)
```

### 📄 JSON 存储 (`json_storage.py`)
- 基于 JSON 文件的轻量级存储
- 适合开发调试和小规模数据
- 文件位置: `data/students.json`

### 🗄️ SQLite 存储 (`sqlite_storage.py`)
- 基于 SQLite 的关系型数据库存储
- 使用 Peewee ORM 管理数据模型
- 支持事务和数据完整性
- 文件位置: `data/students.db`

## API 接口文档

### 基础信息
- **服务地址**: `http://localhost:50721`
- **数据格式**: JSON
- **编码方式**: UTF-8

### 学生管理 API

#### 1. 获取所有学生
```http
GET /students
```

**响应示例**:
```json
[
  {
    "id": 1001,
    "name": "张三",
    "age": 18,
    "grade": "高三1班"
  },
  {
    "id": 1002, 
    "name": "李四",
    "age": 17,
    "grade": "高二3班"
  }
]
```

#### 2. 添加学生
```http
POST /students
Content-Type: application/json

{
  "id": 1003,
  "name": "王五",
  "age": 16,
  "grade": "高一2班"
}
```

**响应**:
- 成功: `201 Created` + `{"message": "Success"}`
- 失败: `400 Bad Request` + `{"error": "Student exists"}`

#### 3. 更新学生信息
```http
PUT /students/{id}
Content-Type: application/json

{
  "name": "王五五",
  "age": 17
}
```

**响应**:
- 成功: `200 OK` + `{"message": "Success"}`
- 失败: `404 Not Found` + `{"error": "Not found"}`

#### 4. 删除学生
```http
DELETE /students/{id}
```

**响应**:
- 成功: `200 OK` + `{"message": "Success"}`
- 失败: `404 Not Found` + `{"error": "Not found"}`

## 数据模型

### 学生 (Student)
| 字段 | 类型 | 说明 | 约束 |
|------|------|------|------|
| id | Integer | 学生ID | 主键，唯一 |
| name | String | 学生姓名 | 非空 |
| age | Integer | 学生年龄 | 非空，正整数 |
| grade | String | 所在班级 | 非空 |

## 环境配置

### 安装依赖
```bash
# 使用 pip 安装
pip install -r requirements.txt

# 或者单独安装
pip install Flask==2.2.5
pip install Flask-Cors==6.0.0  
pip install peewee==3.18.1
```

### 运行服务
```bash
# 开发模式
python server.py

# 生产模式建议使用 Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:50721 server:app
```

## 存储配置

### 切换存储模式
在 `server.py` 中修改存储实现：

```python
class StudentManager:
    def __init__(self):
        self.json = JSONStudentStorage()
        self.sqlite = SQLiteStudentStorage()
        
        # 选择存储方式
        self.storage = self.sqlite    # 使用 SQLite (默认)
        # self.storage = self.json    # 使用 JSON 文件
```

### 数据目录配置
- **SQLite**: 数据库文件路径在 `sqlite_storage.py` 中配置
- **JSON**: 文件路径在 `json_storage.py` 中配置

```python
# SQLite 配置
db = SqliteDatabase('./data/students.db')

# JSON 配置  
def __init__(self, file_path='./data/students.json'):
```

## 开发指南

### 添加新存储实现
1. 继承 `StudentStorageInterface` 抽象类
2. 实现所有必需的方法
3. 在 `StudentManager` 中集成新实现

示例：
```python
class RedisStudentStorage(StudentStorageInterface):
    def __init__(self):
        # Redis 连接配置
        pass
        
    def add_student(self, student_id, name, age, grade):
        # Redis 实现
        pass
```

### 添加新 API 端点
```python
@app.route('/students/search', methods=['GET'])
def search_students():
    keyword = request.args.get('keyword', '')
    # 搜索逻辑
    return jsonify(results)
```

### 错误处理
```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500) 
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500
```

## 测试

### 运行测试
```bash
python test_simple.py
```

### API 测试工具
推荐使用以下工具测试 API：
- **Postman**: 图形化接口测试
- **curl**: 命令行测试
- **httpie**: 简化的 HTTP 客户端

### 测试示例
```bash
# 获取所有学生
curl -X GET http://localhost:50721/students

# 添加学生
curl -X POST http://localhost:50721/students \
  -H "Content-Type: application/json" \
  -d '{"id":1001,"name":"测试学生","age":18,"grade":"测试班级"}'

# 更新学生
curl -X PUT http://localhost:50721/students/1001 \
  -H "Content-Type: application/json" \
  -d '{"name":"更新姓名"}'

# 删除学生  
curl -X DELETE http://localhost:50721/students/1001
```

## 部署说明

### 开发环境
```bash
python server.py
```
- 自动重载代码变更
- 详细错误信息
- 单进程运行

### 生产环境
```bash
# 使用 Gunicorn (推荐)
gunicorn -w 4 -b 0.0.0.0:50721 server:app

# 使用 uWSGI
uwsgi --http :50721 --wsgi-file server.py --callable app

# 使用 Docker
docker build -t student-api .
docker run -p 50721:50721 student-api
```

## 监控与日志

### 添加日志记录
```python
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/students', methods=['POST'])
def add_student():
    logger.info(f"Adding student: {request.json}")
    # 业务逻辑
```

### 性能监控
- 使用 Flask 中间件记录请求时间
- 监控数据库查询性能
- 设置适当的超时时间

## 安全考虑

- 输入验证和数据清理
- SQL 注入防护（使用 ORM）
- 请求频率限制
- HTTPS 传输加密
- 敏感信息环境变量配置

## 常见问题

### Q: 端口被占用？
A: 修改 `server.py` 中的端口号或停止占用进程

### Q: 数据库连接失败？
A: 检查 `data` 目录权限和磁盘空间

### Q: 跨域请求被阻止？
A: 确认 Flask-CORS 配置正确

## 贡献指南

1. 遵循 PEP 8 Python 编码规范
2. 添加适当的错误处理
3. 编写测试用例
4. 更新相关文档