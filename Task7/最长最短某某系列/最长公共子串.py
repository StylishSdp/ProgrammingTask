def search(s1, s2):
    if not s1 or not s2:
        return 0

    '''
    1. dp[i][j] 表示s1前i个字符和s2前j个字符的最大公共子序列长度
    2. if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 0
    '''

    m = len(s1)
    n = len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    res = 0
    x = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                # res = max(res, dp[i][j])
                if res < dp[i][j]:
                    res = dp[i][j]
                    x = i
            else:
                dp[i][j] = 0

    return res, s1[x-res:x]

s1 = 'watch'
s2 = 'tch'

print(search(s1, s2))