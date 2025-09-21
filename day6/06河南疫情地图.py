import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# 创建文件对象
f = open("地图数据/疫情.txt", "r", encoding="utf-8")

# 读取数据
data = f.read()

# 关闭文件
f.close()

# json数据转python数据
data_dict = json.loads(data)

# 数据
data_list = []

# 得到河南省各城市数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]

# 遍历每一个城市, 并得到城市名和确诊人数组成的元组, 把元组添加到列表中
for city_data in cities_data:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 添加济源市数据
data_list.append(("济源市", 5))
map = Map()
# 创建地图对象
map = Map()

# 添加数据
map.add("河南省疫情数据", data_list, "河南")

# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"},
        ]
    )
)

# 生成地图文件
map.render("河南省疫情地图.html")