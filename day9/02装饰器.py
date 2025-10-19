
# 装饰器的一般写法(闭包)
def outer(func):

    def inner():
        print("睡觉开始")
        func()
        print("睡觉结束")

    return inner

def sleep():
    import time
    import random
    time.sleep(random.randint(1, 5))


fn = outer(sleep)
fn()

# 装饰器的简化写法(语法糖)
@outer
def sleep():
    import time
    import random
    time.sleep(random.randint(1, 5))

sleep()


