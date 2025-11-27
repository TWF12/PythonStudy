def norm(*args):
    if not args:
        return []
    norm_list = []
    x_min = min(args)
    x_max = max(args)
    for x in args:
        if x_min == x_max:
            norm_list.append(0.5)
        else:
            norm_list.append((x - x_min) / (x_max - x_min))
    return norm_list


assert norm() == []
assert norm(1) == [0.5]
assert norm(1, 1) == [0.5, 0.5]
assert norm(1, 2, 3) == [0, 0.5, 1]
