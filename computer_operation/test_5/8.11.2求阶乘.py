def fact_1(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_1(n - 1)

def fact_2(n):
    ret = 1
    while n > 1:
        ret *= n
        n -= 1
    return ret


n = int(input("请输入整数n(n>=0): "))
print(f"{n}! = {fact_1(n)}")
print(f"{n}! = {fact_2(n)}")