str = input("请输入字符串: ")
alphabet_count = 0
number_count = 0
space_count = 0
others_count = 0
total = 0

for i in str:
    if i.isalpha():
        alphabet_count += 1
    elif i.isdigit():
        number_count += 1
    elif i.isspace():
        space_count += 1
    else:
        others_count += 1
total = alphabet_count + number_count + space_count + others_count
print(f'''
所有字符的总数为: {total} 
英文字母出现的次数: {alphabet_count}
数字出现的次数: {number_count}
空格出现的次数: {space_count}
其它字符出现的次数: {others_count}       
''')
