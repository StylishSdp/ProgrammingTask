def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if nums is None:
        return []
    if len(nums) == 1:
        return [nums]
    res = []
    for i in nums:
        temp = nums + []
        temp.remove(i)
        for y in self.permute(temp):
            res.append([i] + y)
    return res