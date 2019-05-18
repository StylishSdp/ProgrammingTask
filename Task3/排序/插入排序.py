def InsertSort(nums):
    '''
    时间复杂度：O(n**2)
    空间复杂度：O(1)
    稳定排序
    :param nums:
    :return:
    '''
    for i in range(1, len(nums)):
        #前j个元素已排序
        j = i -1
        #将第j个元素插入合适位置
        insertNum = nums[i]
        while j >= 0 and insertNum < nums[j]:
            #插入的数小于nums[j],将后移nums[j]，给插入的数腾位置
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = insertNum
    return nums

nums = [3,5,3,1,12,6,3,9,10]
print(InsertSort(nums))

