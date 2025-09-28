sum_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
print(f'2+4+6+8+...+100={sum_even}')