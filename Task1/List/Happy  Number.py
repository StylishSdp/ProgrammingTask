def isHappy(n):
    while n != 1 or n != 4:  #所以的非快乐数都会在循环中都会出现n=4的情况
        res = 0
        while n > 0:
            res = res + (n % 10) ** 2
            n = n // 10
        if res == 1:
            return True
        elif res == 4:
            return False
        else:
            n = res