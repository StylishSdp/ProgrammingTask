def twosplit(nums, target):
    '''
    前提条件：有序数组，无重复值
    :param nums:
    :param target:
    :return:
    '''
    left = 0
    right = len(nums) - 1
    while left <= right:
        # <=
        mid = (right - left) // 2 + left
        #防溢出写法
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return 'No find!'

nums = [1,2,3,4,5,6,7,8,9]
target = 1
print(two(nums, target))

