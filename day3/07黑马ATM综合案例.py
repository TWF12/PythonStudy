money = 5000000  # 银行卡余额
name = None  # 用户名


# 查询余额
def check_balance():
    print(f"{name}, 您好, 您的当前余额为{money}元")


# 存款
def deposit(amount):
    global money
    if amount > 0:
        money += amount
        print(f"成功存入{amount}元, 您当前余额为{money}元")
    else:
        print("存款金额必须大于0")


# 取款
def withdraw(amount):
    global money
    if amount > 0:
        if amount <= money:
            money -= amount
            print(f"成功取出{amount}元, 您当前余额为{money}元")
        else:
            print("余额不足")
    else:
        print("取款金额必须大于0")


# 主菜单
def main():
    global name
    name = input("请输入您的姓名: ")
    while True:
        print(f"\n{name}, 您好, 欢迎使用黑马ATM, 请选择操作:")
        print("1. 查询余额")
        print("2. 存款")
        print("3. 取款")
        print("4. 退出")
        choice = input("请输入操作编号(1-4): ")
        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = float(input("请输入存款金额: "))
            deposit(amount)
        elif choice == '3':
            amount = float(input("请输入取款金额: "))
            withdraw(amount)
        elif choice == '4':
            print("感谢使用黑马ATM, 再见!")
            break
        else:
            print("无效的操作编号, 请重新输入")


main()
