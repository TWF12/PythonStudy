import threading
import time


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

# target, 执行的目标任务(函数)
# args, 传递给目标任务的位置参数, 必须是元组
# kwargs, 传递给目标任务的关键字参数, 必须是字典
# 创建线程用于唱歌
sing_thread = threading.Thread(target=sing, args=("我在唱歌",))
# 创建线程用于跳舞
dance_thread = threading.Thread(target=dance, kwargs={"msg": "我在跳舞"})

# 启动线程
sing_thread.start()
dance_thread.start()

bind