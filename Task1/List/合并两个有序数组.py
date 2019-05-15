def merge(nums1, nums2):
    m = len(nums1)
    n = len(nums2)

    count = m + n - 1
    i = m - 1
    j = n - 1
    res = [None] * (count + 1)

    while i >= 0 and j >= 0:  #逆序进行判断，nums1和nums2中最大的那个肯定在res中也是最大的
        if nums1[i] >= nums2[j]:
            res[count] = nums1[i]
            count -= 1
            i -= 1
        else:
            res[count] = nums2[j]
            count -= 1
            j -= 1

    while i >= 0:   #如果最小值在nums1中，需要接着将小的值放到res中
        res[count] = nums1[i]
        count -= 1
        i -= 1

    while j >= 0:   #如果最小值在nums2中，需要接着将小的值放到res中
        res[count] = nums2[j]
        count -= 1
        j -= 1

    return res


nums1 = [2, 2, 3, 9]
nums2 = [1, 5, 6]
print(merge(nums1, nums2))



