# 位置参数, 平常使用的就是位置参数
def func1(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)
func1(10, 20, 30)
print("------------------")

# 关键字参数
def func2(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)
func2(c=30, a=10, b=20)
print("------------------")

# 混合使用位置参数和关键字参数, 位置参数必须在关键字参数前面
def func3(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)
func3(10, c=30, b=20)
print("------------------")

# 默认参数, 默认参数必须放在参数列表的最后面
def func4(a, b=200, c=300):
    print("a =", a)
    print("b =", b)
    print("c =", c)
func4(10)
func4(10, 20)
func4(10, 20, 30)
print("------------------")

# 可变参数, 传入的参数个数可以是0个, 1个, 多个
def func5(*args):
    print("args =", args)
    print("args的类型:", type(args))
    for index, value in enumerate(args):
        print("index =", index, "value =", value)
func5()
func5(10)
func5(10, 20, 30, 40, 50)
print("------------------")

# 关键字可变参数, 传入的参数个数可以是0个, 1个, 多个
def func6(**kwargs):
    print("kwargs =", kwargs)
    print("kwargs的类型:", type(kwargs))
    for key, value in kwargs.items():
        print("key =", key, "value =", value)
func6()
func6(a=10)
func6(a=10, b=20, c=30)
print("------------------")
