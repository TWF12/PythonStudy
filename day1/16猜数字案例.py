import random

count = 0
# 生成一个随机数字
num = random.randint(1, 100)
while True:
    a = int(input('输入你猜的数字'))
    count += 1
    if num == a:
        print(f'恭喜你在{count}次猜对')
        break
    if num < a:
        print('大了')
    else:
        print('小了')
