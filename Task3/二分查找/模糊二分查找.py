def twosplit(nums, target):

    if not nums:
        return None

    left = 0
    right = len(nums)-1
    while left < right:
        mid = (right - left) // 2 + left
        if nums[mid] <= target:
            if nums[mid] == target:
                while nums[mid] == target:
                    mid -= 1
                return mid+1
            else:
                left = mid + 1
        else:
            right = mid - 1

    return mid + 1


nums = [1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 8, 9, 12, 21, 23, 45, 88, 90]
print(twosplit(nums,90))