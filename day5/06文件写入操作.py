import time

f = open("test.txt", "w", encoding="utf-8")  # 创建一个文件对象, 如果文件不存在会自动创建, 如果文件存在会清空原有内容
# 写入内容
f.write("Hello, World!\n")  # 写入内存中, 只有当程序结束或调用flush()才会写入硬盘中, 如果文件不存在会自动创建,
# time.sleep(10)

# f.flush() # 将内存中的内容写入硬盘中, 但文件仍然是打开状态
# time.sleep(1000)

f.close() # 关闭文件, 会自动调用flush()将内存中的内容写入硬盘中
# time.sleep(1000)

# 文件已经存在, 再次创建文件对象会清空原有内容
f = open("test.txt", "w", encoding="utf-8")
f.write("Hello, Python!\n")
f.close()
