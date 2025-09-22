from pyecharts.charts import Line
from pyecharts.options import TitleOpts

# 创建折线图对象
line = Line()

# 添加x轴数据
line.add_xaxis(["美国", "英国", "法国"])

# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])

# 设置全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="0%")

)

# 生成图像
line.render("基础折线图.html")
