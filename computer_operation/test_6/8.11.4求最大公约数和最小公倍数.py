def gcd1(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd2(a, b):
    return a if b == 0 else gcd2(b, a % b)


def lcm1(a, b):
    # return a * b // gcd1(a, b)
    if a == 0 or b == 0:
        return 0
    c = max(a, b)
    while True:
        if c % a == 0 and c % b == 0:
            return c
        c += max(a, b)  # 下一个倍数, 注意不要写成乘于2了


def lcm2(a, b, c = None):
    if a == 0 or b == 0:
        return 0
    if not c:
        c = max(a, b)
    if c % a == 0 and c % b == 0:
        return c
    return lcm2(a, b, c + max(a, b))


a = int(input("请输入第一个整数: "))
b = int(input("请输入第二个整数: "))
print(f"(循环方法){a}和{b}的最大公约数为{gcd1(a, b)}, 最小公倍数为{lcm1(a, b)}")
print(f"(递归方法){a}和{b}的最大公约数为{gcd2(a, b)}, 最小公倍数为{lcm2(a, b)}")
