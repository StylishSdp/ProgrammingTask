def BubbleSort(nums):
    '''
    时间复杂度：O(n**2)
    空间复杂度：O(1)
    稳定排序
    :param nums:
    :return:
    '''
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            #遍历nums,如果后边一个比前边一个小，就交换
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

nums = [3,5,3,1,12,6,3,9,10]
print(BubbleSort(nums))

