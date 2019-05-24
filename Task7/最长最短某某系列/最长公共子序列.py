def search(s1, s2):
    if not s1 or not s2:
        return 0

    '''
    1. dp[i][j] 表示s1前i个字符和s2前j个字符的最大公共子序列长度
    2. if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        state 记录回溯的位置
    '''

    m = len(s1)
    n = len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    state = [['']*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                state[i][j] = 'ok'
            else:
                # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                    state[i][j] = 'up'
                else:
                    dp[i][j] = dp[i][j-1]
                    state[i][j] = 'left'

    # print(state)
    res = []
    while dp[m][n]:
        c = state[m][n]
        if c == 'ok':
            res.append(s1[m-1])
            m -= 1
            n -= 1
        elif c== 'left':
            n -= 1
        else:
            m -= 1
    res.reverse()
    return dp[-1][-1], ''.join(res)

s1 = 'cnblogs'
s2 = 'bselong'

print(search(s1, s2))

