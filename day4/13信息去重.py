my_list = ["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast"]
my_set = set()
for item in my_list:
    my_set.add(item)
print(my_set)





my_set = set(my_list)
new_list = list(my_set)
print(new_list)