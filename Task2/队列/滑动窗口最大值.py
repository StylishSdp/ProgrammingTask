def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []
    if k == 1:
        return nums
    # 索引队列
    queue = [0]
    res = []
    for i in range(1, len(nums)):
        # 队列的第一个索引始终为最大值索引，（当前索引-队列第一个索引）大于滑动窗口长度时，删除第一个索引
        if i - queue[0] >= k:
            queue.pop(0)
        # 保证当前最大的值的索引是第一个
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop(-1)
        queue.append(i)
        if i >= k - 1:
            res.append(nums[queue[0]])
    return res