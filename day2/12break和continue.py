# break
i = 1
for i in range(1, 11):
    if i == 5:
        break  # 当i等于5时，跳出循环
    print(i)
print(i)

# continue
for i in range(1, 11):
    if i == 5:
        continue  # 当i等于5时，跳过本次循环，继续下一次循环
    print(i)
print(i)     