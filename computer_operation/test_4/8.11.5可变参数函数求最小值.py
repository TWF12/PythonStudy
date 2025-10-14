def min_n(a, b, *c):
    min_value = a if a < b else b
    for i in c:
        if i < min_value:
            min_value = i
    return f"最小值为 {min_value}"

print(min_n(8, 2))
print(min_n(16, 1, 7, 4, 15))