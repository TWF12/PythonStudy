from numpy.ma.extras import average

s = [9, 7, 8, 3, 2, 1, 55, 6]

# 方法一
count = len(s)
max_s = max(s)
min_s = min(s)
sum_s = sum(s)
average_s = average(s)
print(f"元数个数: {count}, 最大值: {max_s}, 最小值: {min_s}, 元素之和: {sum_s}, 平均值: {average_s}")


# 方法二
count = 0
max_s = s[0]
min_s = s[0]
sum_s = 0
average_s = 0
for item in s:
    count += 1
    if item > max_s:
        max_s = item
    elif item < min_s:
        min_s = item
    sum_s += item
average_s = sum_s / count
print(f"元数个数: {count}, 最大值: {max_s}, 最小值: {min_s}, 元素之和: {sum_s}, 平均值: {average_s}")





