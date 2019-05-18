def QuickSort(nums):
    '''
    1.以任意一个元素pivot为基准，将nums以pivot分开，前半部分小于pivot，后边部分大于pivot
    2.对前后两部分递归分割，直至左右两部分有序或只剩一个元素
    时间复杂度:O(log(n))
    空间复杂度:O(log(n))
    非稳定排序
    :param nums:
    :return:
    '''
    def partition(nums, left, right):
        pivot = left
        while left < right:
            #找到小于pivot的值
            while left < right and nums[right] >= nums[pivot]:
                right -= 1
            #找到大于pivot的值
            while left < right and nums[left] <= nums[pivot]:
                left += 1
            #交换
            nums[left], nums[right] = nums[right], nums[left]
        #上一个循环结束时，left == right，会同时指向比pivot小的值，然后和pivot交换
        nums[left], nums[pivot] = nums[pivot], nums[left]
        return left

    def quicksort(arr, left, right):
        if left >= right:
            return

        mid = partition(arr, left, right)
        quicksort(arr, left, mid-1)
        quicksort(arr, mid + 1, right)

    quicksort(nums, 0, len(nums) - 1)
    return nums

nums = [3, 5, 3, 4, 2, 6, 3, 9, 10]
print(QuickSort(nums))