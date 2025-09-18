def fun1(a, b):
    return a + b

if __name__ == '__main__': # __name__是一个特殊变量, 当该模块被直接运行时, __name__的值是'__main__'; 当该模块被其他模块导入时, __name__的值是模块的名称
    print(fun1(1, 2))