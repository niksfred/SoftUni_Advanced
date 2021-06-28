def math_operations(*args, a, s, d, m):
    args = [int(num) for num in args]
    dict_nums = {}
    n = 0
    for num in range(len(args)):
        n += 1
        if n == 4:
            m *= args[num]
            n = 0
        elif n == 3:
            if args[num] != 0:
                d /= args[num]
        elif n == 2:
            s -= args[num]
        elif n == 1:
            a += args[num]
    dict_nums["a"] = a
    dict_nums["s"] = s
    dict_nums["d"] = d
    dict_nums["m"] = m
    return dict_nums


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))