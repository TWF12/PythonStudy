my_str = "itheima"

# 通过下标或索引访问字符串中的字符
print(my_str[0])
print(my_str[1])
print(my_str[2])
print(my_str[3])
print(my_str[4])
print(my_str[5])
print(my_str[6])
print("------------------")
# 通过负数索引访问字符串中的字符
print(my_str[-1])
print(my_str[-2])
print(my_str[-3])
print(my_str[-4])
print(my_str[-5])
print(my_str[-6])
print(my_str[-7])
print("------------------")
# 字符串不可以修改
# my_str[0] = "I" # TypeError: 'str' object does not support item assignment

# index()方法查找字符的索引
index = my_str.index("h")
print("h的index:", index)
index = my_str.index("i")
print("i的index:", index)
print("------------------")

# replace()方法替换字符串中的字符
new_str = my_str.replace("i", "I")
print("替换后的字符串:", new_str)
print("原字符串:", my_str)
print("------------------")

# split()方法拆分字符串为列表
s = "hello world itcast itheima python"
list1 = s.split(" ")
print("拆分后的列表:", list1)
print("原字符串:", s)
print("------------------")

# strip()方法去除字符串两端的空白字符
s2 = "   hello world   "
print("原字符串:", repr(s2))
new_s2 = s2.strip()  # 默认为去除空白字符, 也可以指定其他字符
print("去除两端空白字符后的字符串:", repr(new_s2))
print("------------------")

# count()方法统计字符出现的次数
count_i = my_str.count("i")
count_t = my_str.count("t")
count_a = my_str.count("a")
print("i出现的次数:", count_i)
print("t出现的次数:", count_t)
print("a出现的次数:", count_a)
print("------------------")

# len()方法获取字符串的长度
length = len(my_str)
print("字符串的长度是:", length)
print("------------------")
