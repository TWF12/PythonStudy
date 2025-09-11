for i in range(1, 366):
    print("今天是2025年的第%d天" % i)
    for j in range(1, 101):
        print("今天写了%d行代码" % j)
print("2025年写了36500行代码")



#九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()