# 创建一个文件对象
file = open('example.txt', 'r', encoding='utf-8')
print(type(file))

# 读取文件内容
content = file.read(19) # 默认读取所有内容, 可以指定读取的字符数
print("文件内容:")
print(content)
print("内容类型:", type(content))

# 每次读取都是从上次读取的位置继续读取
print(file.read(19))
print(file.read(19))
print(file.read(19))
print(file.read(19))
print(file.read(19))
print(file.read(19))

# 读取一行内容
file.seek(0) # 将文件指针移动到文件开头
print("第一行内容:", file.readline())
print("第二行内容:", file.readline())
print("第三行内容:", file.readline())
print("第四行内容:", file.readline())
print("第五行内容:", file.readline())
print("第六行内容:", file.readline())
print("第七行内容:", file.readline())
print("第八行内容:", file.readline())
print("第九行内容:", file.readline())
print("第十行内容:", file.readline())

# 读取所有行内容, 返回一个列表
file.seek(0) # 将文件指针移动到文件开头
lines = file.readlines()
print("所有行内容:", lines)
print("行内容类型:", type(lines))

# 用循环读取每一行内容
file.seek(0) # 将文件指针移动到文件开头
for line in file:
    print("行内容:", line)

# 关闭文件
file.close()

with open("example.txt", "r", encoding="utf-8") as f:
      for line in f:
            print("行内容:", line.strip()) # 使用 strip() 去除行末的换行符
# 文件自动关闭, 不需要手动调用 close() 方法
