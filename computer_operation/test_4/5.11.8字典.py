weekday_dict = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday",5:"Friday", 6:"Saturday", 7:"Sunday"}

# 输出键
for k in weekday_dict:
    print(k, end=" ")

print()

# 输出值
for v in weekday_dict.values():
    print(v, end=" ")

print()

# 输出键值对(元组形式)
for k, v in weekday_dict.items():
    print((k, v), end=" ")