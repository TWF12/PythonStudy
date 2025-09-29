x = input("请输入操作数x: ")
y = input("请输入操作数y: ")
op = input("请输入操作符: ")
result = 0
try:
    x = float(x)
    y = float(y)
    if op == "+":
        result =  x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    elif op == "%":
        result = x % y
    else:
        print("操作符不合法")
except ZeroDivisionError:
    print("分母 = 0, 零除异常!")
except ValueError:
    print("操作数不合法!")
else:
    print(f"{x} {op} {y} = {result}")

