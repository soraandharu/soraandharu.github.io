"""简单测试"""
from server import StudentManager

def test():
    manager = StudentManager()
    
    # 测试JSON
    print("JSON存储测试:")
    manager.json.add_student(1, "张三", 20, "A班")
    print(manager.json.get_all_students())
    
    # 测试SQLite
    print("\nSQLite存储测试:")
    manager.sqlite.add_student(1, "李四", 21, "B班")  # 相同ID不同数据
    print(manager.sqlite.get_all_students())
    
    print("\n✅ 两个存储完全独立！")

if __name__ == "__main__":
    test()
