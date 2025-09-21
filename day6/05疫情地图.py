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

# 拿到省份数据
province_data_list = data_dict["areaTree"][0]["children"]

for province_data in province_data_list:
    province_name = province_data["name"]
    if province_name in ("北京", "天津", "上海", "重庆"):
        province_name += "市"
    elif province_name in ("内蒙古", "西藏"):
        province_name += "自治区"
    elif province_name == "广西":
        province_name += "壮族自治区"
    elif province_name == "宁夏":
        province_name += "回族自治区"
    elif province_name == "新疆":
        province_name += "维吾尔自治区"
    else:
        province_name += "省"
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))


# 创建地图对象
map = Map()

# 添加数据
map.add("各省份确诊人数", data_list, "china")

# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
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
map.render("全国疫情地图.html")
