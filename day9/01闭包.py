# 闭包：函数嵌套定义，并且内部函数引用了外部函数的变量
# 好处, 可以让内部函数使用外部函数的变量，并且可以保护这些变量不被外部访问

#  简单闭包
def outer(logo):

    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner

fn1 = outer("黑马程序员")
fn1("大家好")

fn2 = outer("传智教育")
fn2("大家好")

def account_create(initial_balance = 0):

    def account_action(num, deposit = True):
        nonlocal initial_balance # 声明使用外部函数变量
        if deposit:
            initial_balance += num
        else:
            initial_balance -= num
        return initial_balance

    return account_action

my_account = account_create(100000)
my_balance = my_account(10000)
print("存款后余额:", my_balance)