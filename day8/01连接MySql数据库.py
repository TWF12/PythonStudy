from pymysql import Connection

# 连接MySQL数据库
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)

# print(conn.get_server_info())

# 选择数据库
conn.select_db("studentsdb")

# 创建游标对象
cursor = conn.cursor()

# 执行SQL语句
# cursor.execute("create table test_pymysql(id int)")
cursor.execute("select * from student_info")
results = cursor.fetchall()
print(results)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()