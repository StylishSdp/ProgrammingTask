def MergeSort(nums):
    '''
    分治法：二分+合并
    1.将数组分为两组
    2.对左右两组递归排序
    时间复杂度:O(nlog(n))
    空间复杂度:O(n)
    稳定排序
    :param nums:
    :return:
    '''
    def merge(nums, left, mid, right):
        '''
        合并两个有序数组
        '''
        temp = []
        m = left
        n = mid + 1
        while m <= mid and n <= right:
            if nums[m] > nums[n]:
                temp.append(nums[n])
                n += 1
            else:
                temp.append(nums[m])
                m += 1

        while m <= mid:
            temp.append(nums[m])
            m += 1
        while n <= right:
            temp.append(nums[n])
            n += 1

        for i in range(left, right+1):
            nums[i] = temp[i-left]

    def mergesort(nums, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        mergesort(nums, left, mid)
        mergesort(nums, mid + 1, right)
        merge(nums, left, mid, right)

    mergesort(nums, 0, len(nums)-1)
    return nums

nums = [3,5,3,1,12,6,3,9,2,4,6,8,23,45,88,90,1,21]
print(MergeSort(nums))


