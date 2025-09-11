# 计算从1-num(不包含num)之间的偶数个数
num = int(input("请输入一个数字: "))
count = 0
for i in range(1, num):
    if i % 2 == 0:
        count += 1
print(f"1-{num}(不包含{num})之间的偶数个数是: {count}")