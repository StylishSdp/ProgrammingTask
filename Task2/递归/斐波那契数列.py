

def func(n):
    res = 0
    if n == 1:
        return res + 1
    elif n == 2:
        return res + 1
    else:
        res = func(n - 1) + func(n - 2)

    return res

print(func(6))