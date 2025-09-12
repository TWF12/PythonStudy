#return的作用是结束函数，并且可以携带一个值作为函数的返回值
def add(a, b):
    return a + b
print(add(1, 2))

#如果没有返回值，默认返回None
def no_return():
    pass

print(no_return())  # None