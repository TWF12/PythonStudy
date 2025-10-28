def fib(n = 0):
    if n <= 0:
        return -1
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def get_n_fib(n = 0):
    if n <= 0:
        return -1
    i = 1
    while i <= n:
        if i % 10 == 0:
            print(f"{fib(i):5}")
        else:
            print(f"{fib(i):5}", end="")
        i += 1


get_n_fib(20)
