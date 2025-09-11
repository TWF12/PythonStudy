#某公司,账户余额1万元,给20名员工发工资
#编号1-20,依次发1000元
#员工绩效分(1-10, 随机生成), 如果低于5,不发工资
# 账户余额发完了, 结束发工资
import random
account = 10000
for i in range(1, 21):
    performance = random.randint(1, 10)
    if account >= 1000:
        if performance < 5:
            print(f"员工{i}绩效分{performance}, 不发工资, 账户余额{account}元")
            continue
        account -= 1000
        print(f"员工{i}绩效分{performance}, 发工资1000元, 账户余额{account}元")
    else:
        print(f"员工{i}绩效分{performance}, 账户余额不足, 发工资结束")
        break