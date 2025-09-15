# 定义一个列表
my_list = [10, 20, 30, 40, 50]

# 定义一个元组
my_tuple = (1, 2, 3, 4, 5)

# 定义一个字符串
my_str = "Hello, World!"

# 定义一个集合
my_set = {100, 200, 300, 400, 500}

# 定义一个字典
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# len()函数
print("列表长度:", len(my_list))
print("元组长度:", len(my_tuple))
print("字符串长度:", len(my_str))
print("集合长度:", len(my_set))
print("字典长度:", len(my_dict))

print("------------------")

# max()函数
print("列表最大值:", max(my_list))
print("元组最大值:", max(my_tuple))
print("字符串最大值:", max(my_str))  # 按照ASCII值比较
print("集合最大值:", max(my_set))
print("字典最大键:", max(my_dict))  # 比较字典的键

print("------------------")

# min()函数
print("列表最小值:", min(my_list))
print("元组最小值:", min(my_tuple))
print("字符串最小值:", min(my_str))  # 按照ASCII值比较
print("集合最小值:", min(my_set))
print("字典最小键:", min(my_dict))  # 比较字典的键

print("------------------")

# list()转列表
print("元组转列表:", list(my_tuple))
print("字符串转列表:", list(my_str))
print("集合转列表:", list(my_set))
print("字典转列表(键):", list(my_dict))  # 转换为字典的键列表

print("------------------")

# tuple()转元组
print("列表转元组:", tuple(my_list))
print("字符串转元组:", tuple(my_str))
print("集合转元组:", tuple(my_set))
print("字典转元组(键):", tuple(my_dict))  # 转换为字典的键元组

print("------------------")

# str()转字符串
print("列表转字符串:", str(my_list))
print("元组转字符串:", str(my_tuple))
print("集合转字符串:", str(my_set))
print("字典转字符串:", str(my_dict))

print("------------------")

# set()转集合
print("列表转集合:", set(my_list))
print("元组转集合:", set(my_tuple))
print("字符串转集合:", set(my_str))
print("字典转集合(键):", set(my_dict))  # 转换为字典的键集合

print("------------------")

# dict()转字典
# 注意: 只能将包含键值对的可迭代对象转换为字典
key_value_list = [("name", "Alice"), ("age", 30), ("city", "New York")]
print("列表转字典:", dict(key_value_list))

print("------------------")

# sorted()排序, 返回一个新的列表
print("列表排序:", sorted(my_list))
print("元组排序:", sorted(my_tuple))
print("字符串排序:", sorted(my_str))
print("集合排序:", sorted(my_set))
print("字典排序(键):", sorted(my_dict))  # 排序字典的键

print("------------------")

# sorted(, reverse=True)降序排序, 返回一个新的列表
print("列表降序排序:", sorted(my_list, reverse=True))
print("元组降序排序:", sorted(my_tuple, reverse=True))
print("字符串降序排序:", sorted(my_str, reverse=True))
print("集合降序排序:", sorted(my_set, reverse=True))
print("字典降序排序(键):", sorted(my_dict, reverse=True))  # 降序排序字典的键
