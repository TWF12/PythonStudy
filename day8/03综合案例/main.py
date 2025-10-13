from file_define import TextFileReader, JsonFileReader
from pymysql import Connection

# 分别创建txt和json文件读取对象
text_file_reader = TextFileReader("data/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("data/2011年2月销售数据JSON.txt")

# 读取数据
jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()

# 合并数据
all_data = jan_data + feb_data

# 创建MySQL连接对象
conn = Connection(host="localhost", port=3306, user="root", password="123456", autocommit=True)

# 选择数据库
conn.select_db("py_sql")

# 创建游标对象
cursor = conn.cursor()

# 执行SQL语句
for record in all_data:
    cursor.execute(f"insert into sales values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')")

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
