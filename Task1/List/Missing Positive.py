def firstMissingPositive(nums):
    if not nums:
        return 1

    for i in range(len(nums)):  #这里是利用nums[i] = i + 1
        while nums[i] >0  and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
            #先按照nums[i] = i + 1 的顺序排序
            temp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = temp

    for i in range(len(nums)):
        #找到第一个nums[i] != i + 1的数字
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1

nums = [7,8,9,11,12]
res = firstMissingPositive(nums)
print(res)