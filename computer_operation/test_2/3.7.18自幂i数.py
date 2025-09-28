n = int(input("请输入自幂数位数(>=1且<=10): "))

count = 0
digit_list = []
start, end = pow(10, n-1), pow(10, n)
for digit in range(start, end):
    sum = 0
    temp = digit
    digit_per_list = list(map(int, str(digit)))
    for digit_per in digit_per_list:
        sum += pow(digit_per, n)
    # while temp > 0:
    #     per = temp % 10
    #     sum += pow(per, n)
    #     temp = temp // 10
    if sum == digit:
        count += 1
        digit_list.append(digit)
if n == 1:
    print(f"独身数{count}个: {digit_list}")
elif n == 2:
    print(f"两位数没有自幂数{count}个: {digit_list}")
elif n == 3:
    print(f"水仙花数{count}个: {digit_list}")
elif n == 4:
    print(f"玫瑰花数{count}个: {digit_list}")
elif n == 5:
    print(f"五角星数{count}个: {digit_list}")
elif n == 6:
    print(f"六合数{count}个: {digit_list}")
elif n == 7:
    print(f"北斗七星数{count}个: {digit_list}")
elif n == 8:
    print(f"八仙数{count}个: {digit_list}")
elif n == 9:
    print(f"九九重阳数{count}: {digit_list}")
elif n == 10:
    print(f"十全十美数{count}: {digit_list}")







