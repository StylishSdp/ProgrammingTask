#大顶堆

def Max_heap(nums):
    n = len(nums)
    last_node = n - 1
    root = (last_node - 1) // 2
    while root >= 0:
        heapify(nums, root, n - 1)
        root -= 1

    return nums

def heapify(nums, start, end):
    temp = nums[start]
    son = 2 * start + 1
    while son <= end:
        if son < end and nums[son] < nums[son + 1]:
            son += 1
        if temp >= nums[son]:
            break
        nums[start] = nums[son]
        start = son
        son = 2 * son + 1
    nums[start] = temp

#小顶堆
def Min_heap(nums):
    n = len(nums)
    last_node = n - 1
    root = (last_node - 1) // 2
    while root >= 0:
        adheap(nums, root, n - 1)
        root -= 1

    return nums


def adheap(nums, start, end):
    temp = nums[start]
    son = 2 * start + 1
    while son <= end:
        if son < end and nums[son] >= nums[son + 1]:
            son += 1
        if temp < nums[son]:
            break
        nums[start] = nums[son]
        start = son
        son = 2 * son + 1
    nums[start] = temp

nums = [3,5,3,1,12,6,3,9,2,4,6,8]
print(Min_heap(nums))


#优先级队列
#参考https://www.cnblogs.com/zzy-9318/p/10445336.html
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, val, priority):
        heapq.heappush(self.queue, (-priority, self.index, val))  #优先级为负数的目的是使得元素按照优先级从高到低排序
        # index 变量的作用是保证同等优先级元素的正确排序。 通过保存一个不断增加的 index 下标变量，可以确保元素按照它们插入的顺序排序
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


# 下面是它的使用方式：


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())
print(q.pop())
print(q.pop())

# Item('bar')
# Item('spam')
# Item('foo')
# 第一个 pop() 操作返回优先级最高的元素。 另外注意到如果两个有着相同优先级的元素（ foo 和 grok ），pop 操作按照它们被插入到队列的顺序返回的。