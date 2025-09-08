print("欢迎来到黑马儿童游乐场, 儿童免费, 成人收费")
age = int(input("请输入你的年龄:"))
if age >= 18:
    print("您已成年, 游玩需要补票10元")
print("祝您游玩愉快")




print("欢迎来到黑马动物园")
height = int(input("请输入你的身高(cm): "))
if height <= 120:
    print("您的身高未超出120cm, 可以免费游玩")
else:
    print("您的身高超出120cm, 游玩需要补票10元")
print("祝您游玩愉快")


height = int(input("请输入你的身高: "))
vip_level = int(input("请输入你的VIP的等级(1-5): "))
day = int(input("今天多少号?"))
if height <= 120:
    print("身高小于120cm, 可以免费游玩")
elif vip_level >3:
    print("VIP等级大于3, 可以免费游玩")
elif day == 1:
    print("今天是会员日, 所有人均可免费游玩")
else:
    print("不好意思, 上述条件均不符合, 需要补票10元")


