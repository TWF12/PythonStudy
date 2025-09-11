# i的作用域为for循环内,在for循环外仍可以使用, 但是不建议这样使用,这是一种规定,不遵守也可以正常运行
i = 0
for i in range(5):
    print(i)
print("循环结束后i的值是:", i)