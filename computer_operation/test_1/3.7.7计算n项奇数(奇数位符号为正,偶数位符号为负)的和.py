# Sn = 1-3+5-7+9-11+...

n = int(input('请输入n的值: '))
sum = 0
Sn = ''
for i in range(1, n + 1):
    an = 2 * i - 1
    if i % 2 != 0:
        sum += an
        Sn += '+' + str(an)
    else:
        sum -= an
        Sn += '-' + str(an)
Sn = Sn[1:]


print(f'S{n}={Sn}={sum}')
