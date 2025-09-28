a = int(input("请输入一个三位自然数: "))

# 方法一
ones_place = a % 10
tens_place = a // 10 % 10
hundreds_place = a // 100 % 10

print(f"方法一: {hundreds_place} {tens_place} {ones_place}")

# 方法二
b, ones_place = divmod(a, 10)
c, tens_place = divmod(b, 10)
_, hundreds_place = divmod(c, 10)
print(f"方法二: {hundreds_place} {tens_place} {ones_place}")

# 方法三
hundreds_place, tens_place, ones_place = map(int, str(a))
print(f"方法三: {hundreds_place} {tens_place} {ones_place}")
