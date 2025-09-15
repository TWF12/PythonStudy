# 定义字典
my_dict = {"王力宏": 175, "张学友": 180, "刘德华": 178}
print(my_dict)
print(type(my_dict))
print("------------------")

# 定义一个空字典
empty_dict = {} # 或者使用 empty_dict = dict()
print(empty_dict)
print(type(empty_dict))
print("------------------")

# 通过键访问字典中的值
print("王力宏的身高:", my_dict["王力宏"])
print("张学友的身高:", my_dict["张学友"])
print("刘德华的身高:", my_dict["刘德华"])
print("------------------")

# 字典嵌套(key不能是字典或列表,value可以是任意类型)
my_dict = {
    "name": "张三",
    "age": 20,
    "is_student": True,
    "scores": [95, 88, 92],
    "address": {
        "city": "北京",
        "street": "朝阳区",
        "zip": "100000"
    },
    (1, 2, 3): "这是一个元组键"
}
print(my_dict)
print("姓名:", my_dict["name"])
print("年龄:", my_dict["age"])
print("是否是学生:", my_dict["is_student"])
print("成绩:", my_dict["scores"])
print("地址:", my_dict["address"])
print("城市:", my_dict["address"]["city"])
print("街道:", my_dict["address"]["street"])
print("邮编:", my_dict["address"]["zip"])
print("------------------")

# 添加或修改键值对
my_dict["phone"] = "123-456-7890" # 添加新的键值对
my_dict["age"] = 21 # 修改已有的键值对
print(my_dict)
print("------------------")

# 删除键值对
del my_dict["is_student"] # 删除键值对
print(my_dict)
value = my_dict.pop("phone") # 删除键值对并返回该值
print("被删除的phone值:", value)
print(my_dict)
print("------------------")

# 获取所有的键以及遍历字典
keys = my_dict.keys()
print("所有的键:", keys)
for key in keys:
    print(f"{key}: {my_dict[key]}")
print("------------------")

for key in my_dict:
    print(f"{key}: {my_dict[key]}")
print("------------------")

# len()方法
length = len(my_dict)
print("字典的长度:", length)
print("------------------")


# 清空字典
my_dict.clear()
print(my_dict)
print("------------------")


