# 集合的特点:
# 1. 集合中的元素是无序的
# 2. 集合中的元素是唯一的, 不允许重复
# 3. 集合中的元素是不可变的, 不能是可变类型
# 4. 集合本身是可变的, 可以添加或删除元素

# 定义集合
my_set = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3}
print(my_set)
print(type(my_set))

# 定义空集合
empty_set = set()
print(empty_set)
print(type(empty_set))

# 添加元素
my_set.add(12)
print(my_set)

# 删除元素
my_set.remove(3)  # 如果元素不存在, 会抛出KeyError
print(my_set)

element = my_set.pop() # 随机删除一个元素, 并返回该元素
print("被删除的元素:", element)
print(my_set)

# 清空集合
my_set.clear()
print(my_set)

# 取两个集合差集
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
diff_set = set1 - set2 # 或者 diff_set = set1.difference(set2)
print("set1与set2的差集:", diff_set)

# 取两个集合的交集
inter_set = set1 & set2 # 或者 inter_set = set1.intersection(set2)
print("set1与set2的交集:", inter_set)

# 取两个集合的并集
union_set = set1 | set2 # 或者 union_set = set1.union(set2)
print("set1与set2的并集:", union_set)

# 消除交集
set1.difference_update(set2)
print("消除set1与set2的交集后, set1:", set1)
print("set2不变:", set2)

# 集合元素数量
count = len(set2)
print("set2的元素数量:", count)

# 集合的遍历
for item in set2:
    print(item)
print("------------------")