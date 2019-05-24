def findLengthOfLCIS(nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    res = 1
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1
        res = max(res, dp[i])
    return res


nums = [2,-1,4,3,5,8,9,5]
print(findLengthOfLCIS(nums))