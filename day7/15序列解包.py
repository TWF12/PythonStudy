*a, = range(5) # a的类型为list
b = (*a,) # 此处不写括号默认为元组
f = (a,)
print(type(a), a) # list [0, 1, 2, 3, 4]
print(type(b), b) # tuple (0, 1, 2, 3, 4)
print(type(f), f) # tuple ([0, 1, 2, 3, 4],)

(*c, )= range(5)
d = [*c, ]
e = [c, ]
print(type(c), c) # list [0, 1, 2, 3, 4]
print(type(d), d) # list [0, 1, 2, 3, 4]
print(type(e), e) # list [[0, 1, 2, 3, 4],]