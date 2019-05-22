def func(nums, k):
    '''
    利用堆排序
    找前k大，就把堆顶摘出来k次
    :param nums:
    :param k:
    :return:
    '''
    def heap_build(nums):
        last_node = len(nums) - 1
        root = (last_node - 1) // 2
        while root >= 0:
            heapify(nums, root, last_node)
            root -= 1

    def heapify(nums, start, end):
        temp = nums[start]
        son = start * 2 + 1
        while son <= end:
            if son < end and nums[son] < nums[son + 1]:
                son += 1

            if temp > nums[son]:
                break

            nums[start] = nums[son]
            start = son
            son = start * 2 + 1
        nums[start] = temp

    heap_build(nums)
    i = len(nums) - 1
    index = k
    while i >= 0 and k >= 0:
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, 0, i - 1)
        i -= 1
        k -= 1

    return nums[-index:]

nums = [3,5,3,1,12,6,3,9,2,4,6,8,23,45,88,90,1,21]
    #[1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 8, 9, 12, 21, 23, 45, 88, 90]
print(func(nums, 5))