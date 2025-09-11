# import random
from random import randint

num = randint(1, 100)
count = 0
while True:
    guess = int(input("请输入你猜的数字（1-100）："))
    count += 1
    if guess == num:
        print(f"恭喜你，猜对了！你总共猜了{count}次。")
        break
    if guess > num:
        print("你猜的数字大了！")
    else:
        print("你猜的数字小了！")

