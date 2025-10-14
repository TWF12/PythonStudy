s = [9, 7, 8, 3, 2, 1, 5, 6]

print(f"交换前: s= {s}")

# 偶数平方, 奇数不变
for i, e in enumerate(s):
    if e % 2 == 0:
        s[i] = e ** 2

print(f"交换后: s= {s}")
