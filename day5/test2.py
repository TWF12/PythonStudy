__all__ = ['fun1'] # __all__变量指定了from module import *时导入的内容, 如果不指定, 则默认导入所有不以下划线开头的内容

def fun1(a, b):
    return a - b

def fun2(a, b):
    return a + b