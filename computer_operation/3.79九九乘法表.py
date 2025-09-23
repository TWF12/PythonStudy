# 左上三角
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%dx%d=%d' % (j, i, i * j), end='\t')
    print()

print("------------------------------------------------------------------------------")

# 等腰上三角
for i in range(1, 10):
    for k in range(9 - i):
        print('', end='\t')
    for j in range(1, i + 1):
        print('%dx%d=%d' % (j, i, i * j), end='\t')
    print()

print("------------------------------------------------------------------------------")

# 右上三角
for i in range(1, 10):
    for k in range(18 - i * 2):
        print('', end='\t')
    for j in range(1, i + 1):
        print('%dx%d=%d' % (j, i, i * j), end='\t')
    print()

print("------------------------------------------------------------------------------")

# 左下三角
for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print('%dx%d=%d' % (j, i, i * j), end='\t')
    print()

print("------------------------------------------------------------------------------")

# 等腰下三角
for i in range(9, 0, -1):
    for k in range(9 - i):
        print('', end='\t')
    for j in range(1, i + 1):
        print('%dx%d=%d' % (j, i, i * j), end='\t')
    print()

print("------------------------------------------------------------------------------")

# 右下三角
for i in range(9, 0, -1):
    for k in range(18 - i * 2):
        print('', end='\t')
    for j in range(1, i + 1):
        print('%dx%d=%d' % (j, i, i * j), end='\t')
    print()

print("------------------------------------------------------------------------------")

# 矩形
count = 0
for i in range(1, 10):
    for j in range(1, i + 1):
        count += 1
        print('%dx%d=%d' % (j, i, i * j), end='\t')
        if count % 9 == 0:
            print()

