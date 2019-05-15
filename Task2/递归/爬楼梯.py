def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

print(climbStairs(35))

#空间换时间
#前n阶的次数 = 前n-1阶的次数 + 前n-2阶的次数

def climbStairs2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    temp = [None] * n
    temp[0] = 1
    temp[1] = 2
    for i in range(2, n):
        temp[i] = temp[i - 1] + temp[i - 2]

    return temp[-1]
print(climbStairs2(35))