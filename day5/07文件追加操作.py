# 以追加的模式创建文件对象, 不会覆盖原有内容
f = open('test.txt', 'a', encoding='utf-8')

# 写入内容到文件
f.write("Hello, World!\n")
f.write("This is a test file.\n")

# 关闭文件
f.close()