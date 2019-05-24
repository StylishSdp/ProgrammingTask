def coinChange(coins, amount):
    if not coins:
        return 0

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i - coin] + 1, dp[i])

    dp[-1] = dp[-1] if dp[-1] != float('inf') else -1
    return dp[-1]


coins = [186,419,83,408]
amount = 6249
print(coinChange(coins, amount))
