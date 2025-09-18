# from test1 import fun1
#
# print(fun1(1, 2))


# from test1 import fun1
#
# from test2 import fun1
#
# print(fun1(1, 2)) # 调用test2中的fun1, 因为后导入的会覆盖先导入的



import test1 #这里输出内容是因为test1.py中有print语句, 导入时会执行test1.py中的代码,
             # 如果不想在导入时执行, 而又想保留, 可以把print语句添加到 if __name__ == "__main__": 下面



from test2 import *
print(test1.fun1(1, 2)) # 调用test1中的fun1
print(test2.fun2(1, 2)) # 调用test2中的fun1, 报错是因为from test2 import * 导入了__all__变量中指定的内容, 但是该变量没有包含fun2