def majorityElement(nums):
    '''
    使用hash表保存每个元素出现的次数
   :param : nums
   :return: i
    '''
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] in hashmap.keys():
            hashmap[nums[i]] += 1
        else:
            hashmap[nums[i]] = 1

    for i in hashmap.keys():
        if hashmap[i] > len(nums) // 2:
            return i