# 定义以一个多返回值函数
def calc(a, b):
    sum = a + b
    diff = a - b
    return sum, diff  # 返回多个值，实际上是返回一个元组
# 调用函数并接收返回值
result = calc(10, 5)
print("返回的结果:", result)
print("返回的结果类型:", type(result))

x, y = calc(20, 8)  # 使用多个变量接收返回的多个值
print("x =", x)
print("y =", y)