my_str = "万过薪月,员序程马黑来,nohtyP学"
# 1. 通过切片将字符串逆序
reversed_str = my_str[::-1]
print("逆序后的字符串:", reversed_str)

# 2. 将逆序后的字符串按照逗号分割成两个部分
parts = reversed_str.split(",")
print("分割后的部分:", parts)

print(parts[1].replace("来", ""))


print(my_str[9:4:-1])