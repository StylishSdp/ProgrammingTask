def func(n):
    res = 1
    if n== 1:
        return res*1
    else:
        res = func(n-1) * n
    return res

print(func(5))