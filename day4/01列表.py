# 定义列表
# 元素类型没有限制
my_list = ["itheima", "itcast", "python", 123, 3.14, True,
[1, 2, 3], (4, 5, 6), None
           ]
print(my_list)
print(type(my_list))

print("------------------")


# 通过下标或索引访问列表元素
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

print("------------------")

# 通过负数索引访问列表元素
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])

print("------------------")

# 访问嵌套列表元素
print(my_list[6][0])
print(my_list[6][1])
print(my_list[6][2])