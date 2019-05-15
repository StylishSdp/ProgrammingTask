def twoSum(nums, target):
    hashmap = {} #hashmap  {diff：index}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nums[i]] = i






















