from operator import index

ages = [21, 25, 21, 23, 22, 20]

ages.append(31)
ages.extend([29, 33, 30])
age_1 = ages.pop(0)
age_2 = ages.pop()
index = ages.index(31)
print("ages:", ages)
print("age_1:", age_1)
print("age_2:", age_2)
print("index:", index)
