def SelectSort(nums):
    '''
    时间复杂度：O(n**2)
    空间复杂度：O(1)
    非稳定排序
    :param nums:
    :return:
    '''
    for i in range(len(nums)-1):
        min = i + 1
        #先找出从i之后的最小值
        for j in range(i + 2, len(nums)):
            if nums[min] > nums[j]:
                min = j
        #如果nums[i]大于后边数组的最小值，则交换
        #这里是与冒泡法的区别
        if nums[i] > nums[min]:
            nums[i], nums[min] = nums[min], nums[i]
    return nums

nums = [3,5,3,1,12,6,3,9,10]
print(SelectSort(nums))