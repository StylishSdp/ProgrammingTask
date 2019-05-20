def myAtoi(s):
    s = s.strip()
    res = 0
    if s == '' or s[0] not in '0123456789+-' or s == '+' or s == '-':
        return res
    temp = []
    if s[0] == '+':
        for i in range(1, len(s)):
            if s[i] not in '0123456789':
                break
            else:
                temp.append(s[i])
        if len(temp) == 0:
            return res
        res = int(''.join(temp))
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return res
    elif s[0] in '0123456789':
        for i in range(len(s)):
            if s[i] not in '0123456789':
                break
            else:
                temp.append(s[i])
        if len(temp) == 0:
            return res
        res = int(''.join(temp))
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return res

    elif s[0] == '-':
        for i in range(1, len(s)):
            if s[i] not in '0123456789':
                break
            else:
                temp.append(s[i])

        if len(temp) == 0:
            return res
        res = -int(''.join(temp))
        if res < -2 ** 31:
            return -2 ** 31
        else:
            return res