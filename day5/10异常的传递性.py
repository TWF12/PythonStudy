def fun1():
    print("fun1 start")
    num = 10 / 0  # 这里会抛出异常, 异常会传递到调用处
    print("fun1 end")


def fun2():
    print("fun2 start")
    fun1()  # 异常会传递到这里
    print("fun2 end")


def main():
    fun2()  # 然后再传递到这里


try:
    main()  # 异常最终传递到这里, 导致程序崩溃
except ZeroDivisionError as e:
    print("捕获到异常:", e)
