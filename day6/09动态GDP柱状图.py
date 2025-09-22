from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

# 创建文件对象
f = open("动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")

# 读取数据
data_linnes = f.readlines()

# 关闭文件
f.close()

# 删除多余内容
data_linnes.pop(0)

# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 数据
data_dict = {}
for line in data_linnes:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    try:
        data_dict[year].append([country, gdp])  # 键(年份)值(列表)存在时,直接把数据添加到列表中
    except KeyError:
        data_dict[year] = []  # 不存在时, 创建一个键值对(年份:列表),再把数据添加到列表中
        data_dict[year].append([country, gdp])

# 年份排序
sorted_year_list = sorted(data_dict.keys())
# 遍历得到每一年的数据
for year in sorted_year_list:
    # 对每一年的数据降序排序
    data_dict[year].sort(key=lambda e: e[1], reverse=True)
    year_data = data_dict[year][:8]  # 只取前八名国家数据
    country_list = []
    gdp_list = []
    # 得到国家名和gdp数据并存放到列表中
    for country_gdp in year_data:
        country_list.append(country_gdp[0])
        gdp_list.append(country_gdp[1] / 100000000)
    # 创建柱状图对象
    bar = Bar()
    # 添加数据
    bar.add_xaxis(country_list[::-1])
    bar.add_yaxis("GDP(亿)", gdp_list[::-1], label_opts=LabelOpts(position="right"))
    # 反转x和y轴
    bar.reversal_axis()
    # 设置标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前八GDP数据")
    )
    # 把柱状图对象添加到时间线中
    timeline.add(bar, str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

# 绘图
timeline.render("1960-2019全球GDP前8国家.html")
