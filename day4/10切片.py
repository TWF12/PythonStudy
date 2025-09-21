# 对my_list进行切片, 从索引1开始, 到索引4结束, 但不包含索引4
my_list = [1, 2, 3, 4, 5, 6]
ret = my_list[1:4] #步长默认是1
print(ret)

# 对my_tuple进行切片, 从索引0开始, 到索引3结束, 但不包含索引3, 步长为2
my_tuple = (1, 2, 3, 4, 5, 6)
ret2 = my_tuple[0:3:2]
print(ret2)

# 对my_str进行切片, 从头到-2(不包含)
my_str = "itheima"
ret3 = my_str[:-2] #开始和结束都省略, 步长默认是1
print(ret3)

# 对my_str进行切片, 从头到尾, 步长为2
ret5 = my_str[::2] #开始和结束都省略, 步长为2
print(ret5)


# 对my_str进行切片, 从尾到头, 步长为-1
ret4 = my_str[::-1] #开始和结束都省略, 步长为-1
print(ret4)

# 对my_str进行切片, 尾到头, 步长为-2
ret6 = my_str[::-2] #开始和结束都省略, 步长为-2
print(ret6)