from pymysql import Connection

# 连接MySQL数据库
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
    # autocommit=True #自动提交事务
)

# print(conn.get_server_info())

# 选择数据库
conn.select_db("test")

# 创建游标对象
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("insert into test_pymysql values(10086)")

# 提交事务
conn.commit()

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()