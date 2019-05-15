def threeSum(nums):
    if len(nums) <= 2:
        return []
    res = []

    nums = sorted(nums)  # 关键点1：list先排序
    for i in range(len(nums) - 2):  # 技巧点1：range的范围
        if i > 0 and nums[i] == nums[i - 1]:  # 关键点2：第一层循环去重
            continue
        need = -nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == need:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # 关键点3：第三层循环去重
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

            elif nums[left] + nums[right] > need:  # 关键点4：指针移动的条件
                right -= 1
            else:
                left += 1
    return res
