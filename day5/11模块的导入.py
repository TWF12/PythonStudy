import time

print(123)
time.sleep(5)
print(456)

from time import sleep

print(789)
sleep(5)
print(101112)

from time import * # 导入所有, 不推荐使用, 可能会覆盖掉其他模块的同名函数
print(131415)
sleep(5)
print(161718)

import time as t # 给模块起别名
print(192021)
t.sleep(5)
print(222324)

from time import sleep as sl # 给函数起别名
print(252627)
sl(5)

