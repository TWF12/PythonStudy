import random

# 随机数种子
random.seed(0x1010)

# 生成10个随机密码, 长度为10, 由字母大小写, 数字以及"!,@,#,$,%,^,&,*"八个特俗符号组成, 每个密码首字符不能一样

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
password_first_char_list = []
with open("随机密码.txt", "w", encoding="utf-8") as f:
    for _ in range(10):
        password = ""

        # 生成首字符
        while True:
            first_char = random.choice(characters)
            if first_char not in password_first_char_list:
                password += first_char
                password_first_char_list.append(first_char)
                break
        # 生成剩余9个字符
        for i in range(9):
            password += random.choice(characters)

        # 将密码写入文件
        f.write(password + '\n')
