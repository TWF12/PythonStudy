# 将数字类型转成字符串
num = 123
num_str = str(num)
print(num_str)  # 输出: '123'
print(type(num_str)) # 输出: <class 'str'>

# 将字符串类型转成数字
num_int = int(num_str)
print(num_int)  # 输出: 123
print(type(num_int)) # 输出: <class 'int'>

# 将整数类型转成浮点数
num_float = float(num_int)
print(num_float)  # 输出: 123.0
print(type(num_float)) # 输出: <class 'float'>

# 将浮点数类型转成整数,会舍弃小数部分
num_int2 = int(num_float)
print(num_int2)  # 输出: 123
print(type(num_int2)) # 输出: <class 'int'>

# 所有类型都可以转成字符串,但不是所有字符串都能转成数字
str = "hello"
str_int = int(str)
print(str_int)  # 报错: ValueError: invalid literal for int() with base 10: 'hello'
