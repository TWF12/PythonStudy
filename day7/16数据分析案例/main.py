from pyecharts.charts import Bar
from pyecharts.options import TitleOpts, LabelOpts, InitOpts

from data_define import Record
from file_define import TextFileReader, JsonFileReader

# 分别创建txt和json文件读取对象
text_file_reader = TextFileReader("data/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("data/2011年2月销售数据JSON.txt")

# 读取数据
jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()

# 合并数据
all_data = jan_data + feb_data

# 计算每天的销售额
sales_dict = {}
for record in all_data:
    date = record.date
    money = record.money
    if date not in sales_dict:
        sales_dict[date] = money
    else:
        sales_dict[date] += money

# 创建柱状图对象
bar = Bar(init_opts=InitOpts(theme="light"))

# 添加数据
bar.add_xaxis(list(sales_dict.keys()))
bar.add_yaxis("销售额", list(sales_dict.values()), label_opts=LabelOpts(is_show=False))

# 设置全局选项
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

# 渲染
bar.render("每日销售额.html")
