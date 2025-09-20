# JSON数据格式就是一种轻量级的数据交换格式, 采用完全独立于编程语言的文本格式来存储和表示数据
# 本质上是一种字符串, 但它的格式是有规则的, 可以被解析成各种编程语言中的数据类型


import json

# python数据与json数据互转

# python数据转json数据
# 字典转json
data = {
    "name": "张三",
    "age": 20
}

json_str = json.dumps(data, ensure_ascii=False)  # ensure_ascii=False参数可以让中文正常显示
print(type(json_str))
print("转换后的JSON字符串:", json_str)
print("--------------------")

# 列表转json(列表元素需要是字典)
data = [{"name": "TWF", "age": 21}, {"name": "ZJL", "age": "21"}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)
print("--------------------")

# json数据转python数据
# json转字典
json_str = '{"name": "张三","age": 20}'
d = json.loads(json_str)
print(type(d))
print(d)
print("--------------------")

# json转列表
json_str = '[{"name": "TWF", "age": 21}, {"name": "ZJL", "age": "21"}]'
l = json.loads(json_str)
print(type(l))
print(l)
