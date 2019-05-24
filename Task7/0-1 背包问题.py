
# def bag0_1(w, v, index, C):
#     if index < 0 or C <= 0:
#         return 0
#     res = bag0_1(w, v, index-1, C)  #不放第index个物品
#     if w[index] <= C:
#         res = max(res, v[index] + bag0_1(w, v, index-1, C-w[index]))
#
#     return res

def bag(w, v, C):
    n = len(w)
    if n<=0:
        return 0
    dp = [[0]*(C+1) for _ in range(n+1)]
    #n行C+1列
    #dp[i][j]，一行为1个物品，表示容量为j的背包的总价值
    #二维空间解决
    for i in range(1, n+1):
        for j in range(1, C+1):
            if w[i-1] > j:
                dp[i][j] = dp[i-1][j]  #超重，无法选
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])  #在选和不选之间选取最大值

    return dp[-1][-1]

def bag2(w, v, C):
    n = len(w)
    if n <= 0:
        return 0
    dp = [0] * (C+1)
    for j in range(C+1):
        if w[0] <= j:
            dp[j] = v[0]

    for i in range(1, n+1):
        for j in range(C, w[i-1], -1):
            dp[j] = max(dp[j], dp[j-w[i-1]] + v[i-1])
    return dp[C]

w = [2, 3, 4, 5, 9]
v = [3, 4, 5, 8, 10]
C = 20
print(bag2(w, v, C))

