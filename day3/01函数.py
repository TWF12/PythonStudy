# 函数:组织好的, 可重复使用的, 用来实现单一, 或相关联功能的代码段
# 函数的好处: 提高代码的复用性, 提高代码
# 分为自定义函数和内置函数


# 内置函数
print(abs(-10))  # 绝对值
print(len("hello"))  # 长度

# 自定义函数
def my_len(s):
    count = 0
    for i in s:
        count += 1
    return count
print(my_len("hello"))

# 计算两个数的和
def my_sum(a, b):
    return a+b
print(my_sum(10, 20))