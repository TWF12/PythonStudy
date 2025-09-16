# 函数作为参数
def add(x, y, f):
    print("x =", x)
    print("y =", y)
    print("f =", f)
    print(type(f))
    return f(x) + f(y)


result = add(-5, 6, abs)  # 传入内置函数 abs 作为参数
print("result:", result)  # 输出结果: result: 11
print("------------------")

# 匿名函数
result = add(-5, 6, lambda x: x * x)  # 传入匿名函数作为参数
print("result:", result)  # 输出结果: result: 61
print("------------------")


