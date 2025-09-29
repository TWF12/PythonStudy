def get_pascals_triangle(n: int):
    # 数据
    triangle = []

    # 将每行数据初始化为1
    for i in range(n):
        row = [1] * ( i + 1)
        # 计算中间元素的值
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle # list[list]

n = int(input("请输入要打印杨辉三角的行数: "))

triangle = get_pascals_triangle(n)

for i, row in enumerate(triangle):
    for k in range(n-i-1):
        print('', end='\t')
    for col in row:
        print(col, end='\t\t')
    print()
