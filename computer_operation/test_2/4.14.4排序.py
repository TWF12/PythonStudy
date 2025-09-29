import math
import random

a = math.floor(random.random() * 101)
b = math.floor(random.random() * 101)
c = math.floor(random.random() * 101)
print(f"原始值: a = {a}, b = {b}, c = {c}")

# 方法一
x, y, z = a, b, c
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(f"(方法一)升序值: a = {x}, b = {y}, c = {z}")

# 方法二
min_number = min(a, b, c)
max_number = max(a, b, c)
sum = a + b + c
second = sum - min_number - max_number
print(f"(方法二)升序值: a = {min_number}, b = {second}, c = {max_number}")

# 方法三
x, y, z = sorted([a, b, c])
print(f"(方法三)升序值: a = {x}, b = {y}, c = {z}")


