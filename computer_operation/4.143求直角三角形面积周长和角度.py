import math

a = float(input("请输入直角三角形的直角边a(a>0): "))
b = float(input("请输入直角三角形的直角边b(b>0): "))
c = math.sqrt(a ** 2 + b ** 2)
S = round(a * b / 2, 1)
C = round(a + b + c, 1)
A = math.asin(a / c) * 180 / math.pi
B = math.acos(a / c) * 180 / math.pi

print('直角三角形三边分别为: a=%.1f, b=%.1f, c=%.1f' % (a, b, c))
print(f'三角形的周长 = {C}, 面积 = {S}')
print('三角形两个锐角的度数分别为: %.1f 和 %.1f' % (A, B))
