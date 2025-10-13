from pymysql import Connection

data_dict = {}
date = None
order_id = None
money = None
province = None
f = open("data/2011年销售数据.txt", "w", encoding="utf-8")
# 创建MySQL连接对象
conn = Connection(host="localhost", port=3306, user="root", password="123456", autocommit=True)

# 选择数据库
conn.select_db("py_sql")

# 创建游标对象
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("select * from sales")
data_tuple_tuple = cursor.fetchall() # 得到所有数据(元组的元组)

for data_tuple in data_tuple_tuple:
    f.write(str({"date": data_tuple[0], "order_id": data_tuple[1], "money": data_tuple[2], "province": data_tuple[3]}) + '\n')



# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
