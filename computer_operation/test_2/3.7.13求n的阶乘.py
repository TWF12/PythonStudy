import math

n = 0
while True:
    n = input("请输入非负整数: ")
    n = float(n)
    if n >= 0 and n == math.floor(n):
        n = int(n)
        break

sum = 1
for i in range(1, n + 1):
    sum *= i
print(f"while循环: {n}! = {sum}")



sum = 1
i = n
while i >= 1:
    sum *= i
    i -= 1
print(f"for循环: {n}! = {sum}")
