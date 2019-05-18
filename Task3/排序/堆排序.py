#基于交换排序
#大顶堆：任意父节点都大于其子节点的完全二叉树，根节点最大
#先取出堆顶，再重新堆化
#以数组（列表）实现大顶堆时，从上到下，从左到右编号
# 用list表示堆，索引为i的元素对应的父节点为（i-1)//2 左右孩子 2*i+1  2*i+2

def HeapSort(nums):
    '''
    时间复杂度:O(nlog(n))
    空间复杂度:O(1)
    非稳定排序
    :param nums:
    :return:
    '''
    #对无序数组建堆
    #从最后一个非叶子节点开始，倒着往前做
    #最后一个非叶子节点的索引=最后一个的节点的父节点
    def heap_build(nums):
        n = len(nums)
        last_node = n - 1
        root = (last_node -1) // 2
        while root >= 0:
            heapify(nums, root, n-1)
            root -= 1

    #堆化，从根节点开始，依次向下调整节点
    def heapify(nums, start, end):
        #调整父节点和左右孩子的大小关系，使父节点中值最大
        temp = nums[start]
        son = 2*start + 1
        while son <= end:
            if son < end and nums[son] < nums[son+1]:
                son += 1
            if temp >= nums[son]:
                break
            nums[start] = nums[son]
            start = son
            son = 2*son + 1
        nums[start] = temp

    heap_build(nums)
    i = len(nums) - 1
    while i >= 0:
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, 0, i-1)
        i -= 1
    return nums

nums = [3,5,3,1,12,6,3,9,2,4,6,8,23,45,88,90,1,21]
print(HeapSort(nums))
