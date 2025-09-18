try:
    f = open("non_existent_file.txt", "r")
except: #默认捕获所有类型的异常
    print("捕获到异常: 文件不存在")

try:
    f = open("non_existent_file.txt", "r")
except Exception as e: # 捕获所有类型的异常, 并将异常信息给变量 e
    print("捕获到异常:", e)


try:
    print(name)
except NameError as e: # 捕获指定类型的异常, 并将异常信息给变量 e
    print("捕获到异常:", e)

try:
    result = 10 / 0
    print(name) #如果第一个错误, 则不会执行
except (NameError, ZeroDivisionError) as e: # 捕获多种类型的异常, 如果有一种异常匹配成功, 就会执行对应的异常处理代码
    print("捕获到异常:", e)

try:
    # f = open("non_existent_file.txt", "r")
    print("Hello, World!")
except Exception as e:
    print("捕获到异常:", e)
else:
    print("没有异常执行")
finally:
    print("无论是否有异常, 都会执行")
