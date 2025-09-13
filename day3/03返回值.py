#return的作用是结束函数，并且可以携带一个值作为函数的返回值
def add(a, b):
    return a + b
print(add(1, 2))

#如果没有返回值，默认返回None
def no_return():
    pass

print(no_return())  # None

# 也可以直接返回None
def return_none(age):
    if age >= 18:
        return "SUCCESS"
    return None
ret = return_none(16)
if not ret:
    print("未成年, 不能进入网吧")

#None也可以用于变量初始化
result = None
print(result)

