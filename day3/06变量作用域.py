# 局部变量
def func1():
    a = 10  # a是func1的局部变量
    print(a)
func1()
# print(a)  # NameError: name 'a' is not defined


# 全局变量
b = 20  # b是全局变量
def func2():
    global b # 声明使用全局变量b
    print(b)
    b = 30  # 修改全局变量b的值
func2()
print(b)