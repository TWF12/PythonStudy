# 元组与列表最大的不同是, 元组一旦创建, 其内容不可更改.
# 元组使用小括号()定义, 列表使用中括号[]定义
# 元组的元素不能修改, 但可以通过连接组合生成新的元组

t1 = (1, "hello", 3.14, True, (1, 2, 3), [4, 5, 6])
print(t1)
print(type(t1))

# 定义一个空元组
t2 = ()
print(t2)
print(type(t2))

t3 = tuple()
print(t3)
print(type(t3))
print("------------------")

# 定义一个只有一个元素的元组
t4 = (1,)# 注意: 定义只有一个元素的元组时, 需要在元素后面添加逗号, 否则括号会被当作数学运算中的小括号来使用
print(t4)
print(type(t4))

# 通过下标或索引访问元组元素
print(t1[0])
print(t1[4][2])
print(t1[5][1])
print("------------------")

# index()方法查找元素的索引
index = t1.index(3.14)
print("3.14的index:", index)
index = t1.index((1, 2, 3))
print("(1, 2, 3)的index:", index)
print("------------------")

# count()方法统计元素出现的次数
t5 = (1, 2, 3, 1, 2, 1, 1, 1)
count_1 = t5.count(1)
count_2 = t5.count(2)
count_3 = t5.count(3)
print("1出现的次数:", count_1)
print("2出现的次数:", count_2)
print("3出现的次数:", count_3)
print("------------------")

# len()方法获取元组的长度
length = len(t5)
print("t5的长度是:", length)
print("------------------")

# 遍历元组
for item in t1:
    print(item)
print("------------------")

i = 0
while i < len(t1):
    print(t1[i])
    i += 1
print("------------------")
