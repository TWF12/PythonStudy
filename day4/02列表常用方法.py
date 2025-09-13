mylist = ["itheima", "itcast", "python"]

# index()方法用于从列表中找出某个值第一个匹配项的索引位置
index = mylist.index("itcast")
print("itcast的索引是:", index)

# print(mylist.index("Hello"))# ValueError: 'Hello' is not in list

# insert()方法用于将指定对象插入列表的指定位置
mylist.insert(1, "Hello")
print(mylist)

# append()方法用于在列表末尾添加新的对象
mylist.append("world")
print(mylist)

# extend()方法用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
mylist.extend(["A", "B", "C"])
print(mylist)

# del删除指定下标的元素
del mylist[7]
print(mylist)

# pop()方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
last = mylist.pop() #可以指定下标
print("被删除的元素是:", last)
print(mylist)

# remove()方法用于移除列表中某个值的第一个匹配项
mylist.remove("Hello")
print(mylist)

# count()方法用于统计某个元素在列表中出现的次数
mylist.append("A")
count = mylist.count("A")
print("A出现的次数是:", count)

# len()函数用于获取列表的长度(元素个数)
length = len(mylist)
print("列表的长度是:", length)

# clear()方法用于清空列表
mylist.clear()
print(mylist)
